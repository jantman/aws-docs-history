# aws-docs-history

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)

Historical versions of AWS documentation and information

Let's admit it out loud - AWS's release notes are a joke, and finding out when
AWS-y things change, especially minor API changes and [service limit](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
changes, is virtually impossible unless it's a big, high-level change. This is
my attempt at figuring out when things change...

## Usage

Mainly, look through the git history for what you're interested in. If this is helpful
for people, I might give a try at building some summaries of changes.

Historical information before the creation of this repo has been pulled from
[Archive.org's Wayback Machine](https://archive.org/web/); see the commit messages
for date information.

For information on changes to the AWS APIs themselves, the
[JSON API descriptions from botocore](https://github.com/boto/botocore/tree/develop/botocore/data)
are probably the best source of information.

### Contents

* [http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) - [html](docs.aws.amazon.com/general/aws_service_limits.html) [markdown](docs.aws.amazon.com/general/aws_service_limits.html.md)

## Internals

To retrieve history for new URLs:

```
virtualenv .
source bin/activate
pip install requests GitPython python-dateutil lxml
scripts/getter.py
```

## License

The content of this repo is mainly AWS documentation and generated code, which
I believe is all [Apache2](http://aws.amazon.com/apache2.0/).

My own code here is horribly minimal. Just use it.
