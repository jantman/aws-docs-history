+-----------------------------------+-----------------------------------+
|                                   | [«                                |
|                                   | Previous](GetTheTools.html){.awst |
|                                   | oc}[Next                          |
|                                   | »](api-retries.html){.awstoc}     |
+-----------------------------------+-----------------------------------+
|                                   | Did this page help                |
|                                   | you?  [Yes](feedbackyes.html?topi |
|                                   | c_id=aws_service_limits){.awstoc} |
|                                   |  | [No](feedbackno.html?topic_id= |
|                                   | aws_service_limits){.awstoc} |  [ |
|                                   | Tell                              |
|                                   | us about                          |
|                                   | it...](https://portal.aws.amazon. |
|                                   | com/gp/aws/html-forms-controller/ |
|                                   | documentation/aws_doc_feedback_04 |
|                                   | ?service_name=Regions&guide_name= |
|                                   | General%20Reference&api_version=1 |
|                                   | .0&file_name=aws_service_limits){ |
|                                   | .awstoc}                          |
+-----------------------------------+-----------------------------------+

AWS Service Limits {#aws-service-limits .topictitle}
==================

The following tables provide the default limits for AWS services for an AWS account. Unless otherwise noted, each limit is per region. The limits listed below are only the limits that can be changed. Many services contain limits that cannot be changed. For more information about the limits for a specific service, see the documentation for that service.

If your support plan includes AWS Trusted Advisor, you can use it to display your usage and limits for each service in a specific region. For more information, see [AWS Trusted Advisor](http://aws.amazon.com/premiumsupport/trustedadvisor){.ulink}.

You can request an increase for these limits by performing the following steps. These increases are not granted immediately, so it may take a couple of days for your increase to become effective.

1.  Go to the [AWS Support Center](https://aws.amazon.com/support/){.ulink} page, sign in, if necessary, and click [Open a new case]{.guilabel}.

2.  Under [Regarding]{.guilabel}, select [Service Limit Increase]{.guilabel}.

3.  Under [Limit Type]{.guilabel}, select the type of limit to be increased, then fill in all of the necessary fields in the form and click the button at the bottom of the page for your desired method of contact.

**Topics**

-   [AWS CloudFormation Limits](aws_service_limits.html#limits_cloudformation)
-   [Amazon CloudFront Limits](aws_service_limits.html#limits_cloudfront)
-   [Amazon CloudSearch Limits](aws_service_limits.html#limits_cloudsearch)
-   [AWS Data Pipeline Limits](aws_service_limits.html#limits_data_pipeline)
-   [DynamoDB Limits](aws_service_limits.html#limits_dynamodb)
-   [Amazon EBS Limits](aws_service_limits.html#limits_ebs)
-   [Amazon EC2 Limits](aws_service_limits.html#limits_ec2)
-   [Auto Scaling Limits](aws_service_limits.html#limits_autoscaling)
-   [ElastiCache Limits](aws_service_limits.html#limits_elasticache)
-   [AWS Elastic Beanstalk Limits](aws_service_limits.html#limits_elastic_beanstalk)
-   [Elastic Load Balancing Limits](aws_service_limits.html#limits_elastic_load_balancer)
-   [Elastic Transcoder Limits](aws_service_limits.html#limits_elastictranscoder)
-   [IAM Limits](aws_service_limits.html#limits_iam)
-   [Amazon Kinesis Limits](aws_service_limits.html#limits_kinesis)
-   [AWS OpsWorks Limits](aws_service_limits.html#limits_opworks)
-   [Amazon RDS Limits](aws_service_limits.html#limits_rds)
-   [Amazon Redshift Limits](aws_service_limits.html#limits_redshift)
-   [Amazon Route 53 Limits](aws_service_limits.html#limits_route53)
-   [Amazon SES Limits](aws_service_limits.html#limits_ses_quota)
-   [Amazon SimpleDB Limits](aws_service_limits.html#limits_simpledb)
-   [Amazon Simple Notification Service Limits](aws_service_limits.html#limits_sns)
-   [Amazon VPC Limits](aws_service_limits.html#limits_vpc)

AWS CloudFormation Limits {#limits_cloudformation .title}
-------------------------

  Resource   Default Limit
  ---------- ---------------
  Stacks     20

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

DynamoDB Limits {#limits_dynamodb .title}
---------------

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

  Resource                                                               Default Limit
  ---------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Number of Elastic IP addresses                                         5
  Throttle on the emails that can be sent from your Amazon EC2 account   Throttle applied
  Number of on-demand instances                                          Varies depending on instance type. For more information, see [How many instances can I run in Amazon EC2](http://aws.amazon.com/ec2/faqs/#How_many_instances_can_I_run_in_Amazon_EC2){.ulink}.
  Number of Spot Instances                                               Varies depending on instance type. For more information, see [Spot Instance Limits](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-limits.html){.ulink}.
  Number of Reserved Instances                                           20 per Availability Zone, per month

Auto Scaling Limits {#limits_autoscaling .title}
-------------------

  Resource                          Default Limit
  --------------------------------- ---------------
  Number of launch configurations   100
  Number of Auto Scaling groups     20

ElastiCache Limits {#limits_elasticache .title}
------------------

  Resource   Default Limit
  ---------- ---------------
  Nodes      20

AWS Elastic Beanstalk Limits {#limits_elastic_beanstalk .title}
----------------------------

  Resource       Default Limit
  -------------- ---------------
  Applications   25
  Versions       500
  Environments   200

Elastic Load Balancing Limits {#limits_elastic_load_balancer .title}
-----------------------------

  Resource                   Default Limit
  -------------------------- ---------------
  Number of load balancers   20

Elastic Transcoder Limits {#limits_elastictranscoder .title}
-------------------------

  Resource                   Default Limit
  -------------------------- ---------------
  Pipelines                  4
  Active jobs per pipeline   1,000
  Outputs per job            30
  User-defined presets       50

IAM Limits {#limits_iam .title}
----------

  Resource              Default Limit
  --------------------- ---------------
  Users                 5,000
  Groups                100
  Groups per user       10
  Roles                 250
  Instance profiles     100
  Server certificates   10

Amazon Kinesis Limits {#limits_kinesis .title}
---------------------

  Resource                                  Default Limit
  ----------------------------------------- ---------------
  Number of shards per account per region   5

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

  Resource                             Default Limit
  ------------------------------------ ---------------
  Instances                            40
  Total storage for all DB instances   10 TB

Amazon Redshift Limits {#limits_redshift .title}
----------------------

  Resource                  Default Limit
  ------------------------- ---------------
  Nodes per cluster         16
  Total nodes per account   16

Amazon Route 53 Limits {#limits_route53 .title}
----------------------

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

Amazon Simple Notification Service Limits {#limits_sns .title}
-----------------------------------------

  Resource   Default Limit
  ---------- ---------------
  Topics     3,000

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

![](/web/20140215102927im_/http://docs.aws.amazon.com/general/latest/gr/images/expanderarrow.png)
  ----------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Document Conventions](/web/20140215102927/http://docs.aws.amazon.com/general/latest/gr/docconventions.html){.awstoc}   [« Previous](GetTheTools.html){.awstoc}[Next »](api-retries.html){.awstoc}
  [Terms of Use](http://aws.amazon.com/terms/){.awstoc}                                                                   Did this page help you?  [Yes](feedbackyes.html?topic_id=aws_service_limits){.awstoc} | [No](feedbackno.html?topic_id=aws_service_limits){.awstoc} |  [Tell us about it...](https://portal.aws.amazon.com/gp/aws/html-forms-controller/documentation/aws_doc_feedback_04?service_name=Regions&guide_name=General%20Reference&api_version=1.0&file_name=aws_service_limits){.awstoc}
  ----------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


