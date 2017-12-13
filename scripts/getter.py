#!/usr/bin/env python

import os
import sys
import argparse
import logging
import requests
import re
import subprocess
from datetime import datetime
from git import Repo
from requests.utils import parse_header_links
from email.utils import parsedate, format_datetime
import lxml.html
from lxml.html.clean import Cleaner

FORMAT = "[%(asctime)s %(levelname)s] %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger()

for n in ['urllib3', 'urllib', 'requests', 'git']:
    l = logging.getLogger(n)
    l.setLevel(logging.ERROR)
    l.propagate = True

DOCS = {
    'docs.aws.amazon.com': {
        'general': {
            'aws_service_limits.html': 'http://docs.aws.amazon.com/general/'
            'latest/gr/aws_service_limits.html'
        }
    }
}

class AwsGetter(object):
    """Get AWS documentation"""

    _archive_link_re = re.compile(r'https?://web\.archive\.org/web/\d+/http')

    def __init__(self):
        self.basedir = os.path.abspath(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
        )
        logger.info('Base directory: %s', self.basedir)
        self._get = {}
        self._repo = Repo(self.basedir)
        logger.info(
            'Current branch: %s (%s)', self._repo.active_branch.name,
            self._repo.active_branch.commit
        )
        if self._repo.is_dirty():
            raise RuntimeError('Git repository is dirty; cannot continue')
        if len(self._repo.untracked_files) > 0:
            raise RuntimeError('Git repository has untracked files: %s' %
                               self._repo.untracked_files)
        self._cleaner = Cleaner(
            scripts=True, javascript=True, comments=True, style=True,
            inline_style=True, links=False, meta=True, page_structure=True,
            processing_instructions=True, embedded=True, frames=True,
            forms=False, annoying_tags=False, remove_unknown_tags=False,
            safe_attrs_only=False
        )

    def run(self):
        for k, v in DOCS.items():
            self._handle_dir(k, v)
        self._get_pages()

    def _get_pages(self):
        for path, url in self._get.items():
            logger.debug('Get %s to %s', url, path)
            orig = None
            if os.path.exists(path):
                with open(path, 'r') as fh:
                    orig = fh.read()
            r = requests.get(url)
            r.raise_for_status()
            content = self._clean_html(r.text, url)
            if orig == content:
                logger.info('%s not changed', url)
                continue
            with open(path, 'w') as fh:
                fh.write(content)
            mdpath = self._pandoc(path)
            self._repo.index.add([path, mdpath])
        if not self._repo.is_dirty():
            logger.info('No changes to commit.')
            return
        self._repo.index.commit('Update with current pages')

    def _handle_dir(self, path, item):
        if not isinstance(item, type({})):
            self._handle_url(path, item)
            return
        for k, v in item.items():
            self._handle_dir(os.path.join(path, k), v)

    def _handle_url(self, path, url):
        logger.info('Handle %s to %s', url, path)
        apath = os.path.join(self.basedir, path)
        dname = os.path.dirname(apath)
        if not os.path.exists(dname):
            os.makedirs(dname)
        if not os.path.exists(apath):
            self._get_archives(apath, url)
        self._get[apath] = url

    def _get_archives(self, path, url):
        # get information about the memento
        uri = 'http://web.archive.org/web/%s' % url
        logger.debug('Getting mementos for: %s', uri)
        r = requests.get(uri)
        r.raise_for_status()
        timemap = r.links['timemap']['url']
        if timemap.startswith('//'):
            timemap = 'http:' + timemap
        mementos = self._get_timemaps(timemap)
        logger.info('Found %d mementos (archive.org) for: %s',
                    len(mementos), url)
        for url, dt in mementos.items():
            self._get_and_commit_memento(path, url, dt)
        logger.info('Done with archives for %s', url)

    def _get_and_commit_memento(self, path, url, dt):
        logger.debug('Getting archive %s to: %s', url, path)
        r = requests.get(url)
        content = self._clean_html(r.text, url)
        content = self._archive_link_re.sub('http', content)
        with open(path, 'w') as fh:
            fh.write(content)
        mdpath = self._pandoc(path)
        self._repo.index.add([path, mdpath])
        c = self._repo.index.commit(
            'archive.org memento from %s - %s' % (dt, url),
            author_date=format_datetime(dt),
            commit_date=format_datetime(dt)
        )
        logger.debug('Committed: %s', c)

    def _pandoc(self, fpath):
        outpath = fpath + '.md'
        cmd = [
            'pandoc',
            '-f', 'html',
            '-t', 'markdown-raw_html-native_divs-native_spans',
            '-o', outpath,
            '--wrap=none',
            fpath
        ]
        logger.debug('Running: %s', cmd)
        rcode = subprocess.call(cmd)
        if rcode != 0:
            raise RuntimeError('Command exited %d: %s' % (rcode, cmd))
        return outpath

    def _clean_html(self, src, url):
        doc = lxml.html.fromstring(src)
        div = None
        for div_id in ['main-content', 'divRight']:
            try:
                div = doc.get_element_by_id(div_id)
                if div is None:
                    continue
            except Exception:
                pass
        if div is None:
            raise RuntimeError('Could not find content div in %s' % url)
        html = lxml.html.tostring(div).decode('utf-8')
        cleaned = self._cleaner.clean_html(html)
        return cleaned

    def _get_timemaps(self, url):
        mementos = {}
        logger.debug('Getting timemaps from: %s', url)
        r = requests.get(url)
        r.raise_for_status()
        for link in parse_header_links(r.text.replace("\n", " ")):
            if 'memento' in link['rel'] and 'datetime' in link:
                mementos[link['url']] = datetime(
                    *parsedate(link['datetime'])[:6]
                )
        return mementos


def parse_args(argv):
    p = argparse.ArgumentParser(description='Get AWS Documentation')
    p.add_argument('-v', '--verbose', dest='verbose', action='count', default=0,
                   help='verbose output. specify twice for debug-level output.')
    args = p.parse_args(argv)
    return args

def set_log_info():
    """set logger level to INFO"""
    set_log_level_format(logging.INFO,
                         '%(asctime)s %(levelname)s:%(name)s:%(message)s')


def set_log_debug():
    """set logger level to DEBUG, and debug-level output format"""
    set_log_level_format(
        logging.DEBUG,
        "%(asctime)s [%(levelname)s %(filename)s:%(lineno)s - "
        "%(name)s.%(funcName)s() ] %(message)s"
    )


def set_log_level_format(level, format):
    """
    Set logger level and format.

    :param level: logging level; see the :py:mod:`logging` constants.
    :type level: int
    :param format: logging formatter format string
    :type format: str
    """
    formatter = logging.Formatter(fmt=format)
    logger.handlers[0].setFormatter(formatter)
    logger.setLevel(level)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])

    # set logging level
    if args.verbose > 1:
        set_log_debug()
    elif args.verbose == 1:
        set_log_info()

    AwsGetter().run()
