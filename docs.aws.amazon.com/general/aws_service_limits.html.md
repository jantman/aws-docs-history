+-----------------------------------+-----------------------------------+
|                                   | [«                                |
|                                   | Previous](GetTheTools.html){.awst |
|                                   | oc}[Next                          |
|                                   | »](docconventions.html){.awstoc}  |
+-----------------------------------+-----------------------------------+
| [![Go to the AWS Discussion Forum | Did this page help                |
| for this                          | you?  [Yes](feedbackyes.html?topi |
| product.](/web/20130407171953im_/ | c_id=aws_service_limits){.awstoc} |
| http://docs.aws.amazon.com:80/gen |  | [No](feedbackno.html?topic_id= |
| eral/latest/gr/images/forum_butto | aws_service_limits){.awstoc} |  [ |
| n.png "Go to the AWS Discussion F | Tell                              |
| orum for this product.")](http:// | us about                          |
| forums.aws.amazon.com/forum.jspa? | it...](https://aws-portal.amazon. |
| forumID=0)                        | com/gp/aws/html-forms-controller/ |
|                                   | documentation/aws_doc_feedback_04 |
|                                   | ?service_name=General%20Reference |
|                                   | &guide_name=%A0&api_version=1.0&f |
|                                   | ile_name=aws_service_limits){.aws |
|                                   | toc}                              |
+-----------------------------------+-----------------------------------+

AWS Service Limits {#aws-service-limits .topictitle}
==================

The following tables provide the default limits for services for an account. Unless otherwise noted, each limit is per region. The limits listed below are only the limits that can be changed. Many services contain limits that cannot be changed. For more information about the limits for a specific service, see the documentation for that service.

You can request an increase for these limits by performing the following steps. These increases are not granted immediately, so it may take a couple of days for your increase to become effective.

1.  Go to the [Contact Us](http://aws.amazon.com/contact-us/){.ulink} page.

2.  Select the appropriate service limit in the [Service Limit increase]{.guilabel} section, and click [Go]{.guilabel}.

3.  Fill in all of the necessary fields in the form and click [Submit]{.guilabel}.

**Topics**

-   [AWS CloudFormation Limits](aws_service_limits.html#limits_cloudformation)
-   [Amazon CloudFront Limits](aws_service_limits.html#limits_cloudfront)
-   [Amazon CloudSearch Limits](aws_service_limits.html#limits_cloudsearch)
-   [AWS Data Pipeline Limits](aws_service_limits.html#limits_data_pipeline)
-   [Amazon DynamoDB Limits](aws_service_limits.html#limits_dynamodb)
-   [Amazon EBS Limits](aws_service_limits.html#limits_ebs)
-   [Amazon EC2 Limits](aws_service_limits.html#limits_ec2)
-   [ElastiCache Limits](aws_service_limits.html#limits_elasticache)
-   [Elastic Beanstalk Limits](aws_service_limits.html#limits_elastic_beanstalk)
-   [Elastic Load Balancing Limits](aws_service_limits.html#limits_elastic_load_balancer)
-   [Elastic Transcoder Limits](aws_service_limits.html#limits_elastictranscoder)
-   [IAM Limits](aws_service_limits.html#limits_iam)
-   [AWS OpsWorks Limits](aws_service_limits.html#limits_opworks)
-   [Amazon RDS Limits](aws_service_limits.html#limits_rds)
-   [Route 53 Limits](aws_service_limits.html#limits_route53)
-   [Amazon SES Limits](aws_service_limits.html#limits_ses_quota)
-   [Amazon SimpleDB Limits](aws_service_limits.html#limits_simpledb)
-   [Amazon VPC Limits](aws_service_limits.html#limits_vpc)

AWS CloudFormation Limits {#limits_cloudformation .title}
-------------------------

  Resource           Default Limit
  ------------------ ---------------
  Stacks             20
  Search instances   50

Amazon CloudFront Limits {#limits_cloudfront .title}
------------------------

  Resource                                          Default Limit
  ------------------------------------------------- ---------------
  Data transfer rate                                1,000 Mbps
  Requests per second                               1000
  Alternate domain names (CNAME) per distribution   10
  Origins per distribution                          10
  Cache behaviors per distribution                  10
  Whitelisted cookies per cache behavior            10

Amazon CloudSearch Limits {#limits_cloudsearch .title}
-------------------------

  Resource           Default Limit
  ------------------ ---------------
  Partitions         10
  Search instances   50

AWS Data Pipeline Limits {#limits_data_pipeline .title}
------------------------

  Resource               Default Limit
  ---------------------- ---------------
  Pipelines              20
  Objects per pipeline   50
  Active instances       5

Amazon DynamoDB Limits {#limits_dynamodb .title}
----------------------

  Resource                                  Default Limit
  ----------------------------------------- ---------------
  Read capacity units (individual table)    10,000
  Write capacity units (individual table)   10,000
  Read capacity units (account)             20,000
  Write capacity units (account)            20,000
  Maximum number of tables per region       256

Amazon EBS Limits {#limits_ebs .title}
-----------------

  Resource                                   Default Limit
  ------------------------------------------ -----------------------------------------------------------------------------------------
  Number of EBS volumes                      5,000
  Number of snapshots                        10,000
  Total volume storage of standard volumes   20 TiB
  Number of provisioned IOPS                 10,000 (or 20 TiB in total Provisioned IOPS volume storage, whichever is reached first)

Amazon EC2 Limits {#limits_ec2 .title}
-----------------

  Resource                                                            Default Limit
  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Number of Elastic IP addresses                                      5
  Throttle the emails that can be sent from your Amazon EC2 account   N/A
  Number of on-demand instances                                       Varies depending on instance type. For more information, see [How many instances can I run in Amazon EC2](http://aws.amazon.com/ec2/faqs/#How_many_instances_can_I_run_in_Amazon_EC2){.ulink}.
  Number of Spot Instances                                            100
  Number of Reserved Instances                                        20 per Availability Zone

ElastiCache Limits {#limits_elasticache .title}
------------------

  Resource   Default Limit
  ---------- ---------------
  Nodes      20

Elastic Beanstalk Limits {#limits_elastic_beanstalk .title}
------------------------

  Resource       Default Limit
  -------------- ---------------
  Applications   25
  Versions       500
  Environments   200

Elastic Load Balancing Limits {#limits_elastic_load_balancer .title}
-----------------------------

  Resource                   Default Limit
  -------------------------- ---------------
  Number of load balancers   10

Elastic Transcoder Limits {#limits_elastictranscoder .title}
-------------------------

  Resource                   Default Limit
  -------------------------- ---------------
  Pipelines                  4
  Active jobs per pipeline   1,000
  User-defined presets       50

IAM Limits {#limits_iam .title}
----------

  Resource                     Default Limit
  ---------------------------- ---------------
  Users                        5,000
  Groups                       100
  Groups per user              10
  Roles                        250
  Instance identity profiles   150
  Server certificates          10

AWS OpsWorks Limits {#limits_opworks .title}
-------------------

  Resource              Default Limit
  --------------------- ---------------
  Stacks                20
  Layers per stack      20
  Instances per stack   20
  Apps per stack        20

Amazon RDS Limits {#limits_rds .title}
-----------------

  Resource    Default Limit
  ----------- ---------------
  Instances   20

Route 53 Limits {#limits_route53 .title}
---------------

  Resource                               Default Limit
  -------------------------------------- ---------------
  Hosted zones                           100
  Resource record sets per hosted zone   10,000
  Health checks                          50

Amazon SES Limits {#limits_ses_quota .title}
-----------------

The following are the default limits for Amazon SES in the sandbox environment.

  Resource                         Default Limit
  -------------------------------- -------------------------------------------
  Daily sending quota              200 messages per 24 hour period.
  Maximum send rate                1 email per second.
  Recipient address verification   All recipient addresses must be verified.

The following are the default limits for Amazon SES in the production environment.

  Resource                         Default Limit
  -------------------------------- -------------------------------------------------
  Daily sending quota              10,000 messages per 24 hour period.
  Maximum send rate                5 emails per second.
  Recipient address verification   Recipient addresses do not need to be verified.

Amazon SimpleDB Limits {#limits_simpledb .title}
----------------------

  Resource   Default Limit
  ---------- ---------------
  Domains    250

Amazon VPC Limits {#limits_vpc .title}
-----------------

  Resource                                             Default Limit   Comments
  ---------------------------------------------------- --------------- ----------------------------------------------------------------------------------------------
  Number of VPCs per region                            5                
  Number of subnets per VPC                            200              
  Number of Internet gateways per region               5               One per VPC
  Number of virtual private gateways per region        5               One per VPC
  Number of customer gateways per region               50               
  Number of VPN connections per region                 50              10 per virtual private gateway
  Number of route tables per VPC                       10              Including the main route table
  Number of entries per route table                    20               
  Number of Elastic IP addresses per region            5               Amazon EC2 has a separate limit for its Elastic IP addresses per region for each AWS account
  Number of security groups per VPC                    100              
  Number of rules per security group                   50               
  Number of security groups per instance in a VPC      5                
  Number of network ACLs per VPC                       50               
  Number of rules per network ACL                      20               
  Number of BGP advertised routes per VPN connection   100              

![](/web/20130407171953im_/http://docs.aws.amazon.com:80/general/latest/gr/images/expanderarrow.png)
  --------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Document Conventions](http://docs.aws.amazon.com/general/latest/gr/docconventions.html){.awstoc}   [« Previous](GetTheTools.html){.awstoc}[Next »](docconventions.html){.awstoc}
  [Terms of Use](http://aws.amazon.com/terms/){.awstoc}                                               Did this page help you?  [Yes](feedbackyes.html?topic_id=aws_service_limits){.awstoc} | [No](feedbackno.html?topic_id=aws_service_limits){.awstoc} |  [Tell us about it...](https://aws-portal.amazon.com/gp/aws/html-forms-controller/documentation/aws_doc_feedback_04?service_name=General%20Reference&guide_name=%A0&api_version=1.0&file_name=aws_service_limits){.awstoc}
  --------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


