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

If your support plan includes Trusted Advisor, you can use it to display your usage and limits for each service in a specific region. For more information, see [Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor){.ulink}.

You can request an increase for these limits by performing the following steps. These increases are not granted immediately, so it may take a couple of days for your increase to become effective.

1.  Go to the [AWS Support Center](https://aws.amazon.com/support/){.ulink} page, sign in, if necessary, and click [Open a new case]{.guilabel}.

2.  Under [Regarding]{.guilabel}, select [Service Limit Increase]{.guilabel}.

3.  Under [Limit Type]{.guilabel}, select the type of limit to be increased, then fill in all of the necessary fields in the form and click the button at the bottom of the page for your desired method of contact.

**Topics**

-   [Amazon AppStream Limits](aws_service_limits.html#limits_appstream)
-   [Auto Scaling Limits](aws_service_limits.html#limits_autoscaling)
-   [AWS CloudFormation Limits](aws_service_limits.html#limits_cloudformation)
-   [Amazon CloudFront Limits](aws_service_limits.html#limits_cloudfront)
-   [Amazon CloudSearch Limits](aws_service_limits.html#limits_cloudsearch)
-   [DynamoDB Limits](aws_service_limits.html#limits_dynamodb)
-   [Amazon EBS Limits](aws_service_limits.html#limits_ebs)
-   [Amazon EC2 Limits](aws_service_limits.html#limits_ec2)
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
-   [Amazon WorkSpaces Limits](aws_service_limits.html#limits_workspaces)

Amazon AppStream Limits {#limits_appstream .title}
-----------------------

An Amazon AppStream account has a default limit of 10 simultaneous sessions per AWS account.

Auto Scaling Limits {#limits_autoscaling .title}
-------------------

  Resource                                 Default Limit
  ---------------------------------------- ---------------
  Number of launch configurations          100
  Number of Auto Scaling groups            20
  Number of Auto Scaling lifecycle hooks   50

For information about additional documented limits, see [Auto Scaling Limits](http://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-account-limits.html){.ulink}.

AWS CloudFormation Limits {#limits_cloudformation .title}
-------------------------

  Resource   Default Limit
  ---------- ---------------
  Stacks     20

For information about additional documented limits, see [AWS CloudFormation Limits](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html){.ulink}.

Amazon CloudFront Limits {#limits_cloudfront .title}
------------------------

  Resource                                                                                                                                     Default Limit
  -------------------------------------------------------------------------------------------------------------------------------------------- ---------------
  Data transfer rate                                                                                                                           1,000 Mbps
  Requests per second                                                                                                                          1000
  Web distributions per AWS account                                                                                                            200
  RTMP distributions per AWS account                                                                                                           100
  Alternate domain names (CNAMEs) per distribution                                                                                             100
  Origins per distribution                                                                                                                     25
  Cache behaviors per distribution                                                                                                             25
  Whitelisted headers per cache behavior                                                                                                       10
  Whitelisted cookies per cache behavior                                                                                                       10
  SSL certificates per AWS account when serving HTTPS requests using dedicated IP addresses (no limit when serving HTTPS requests using SNI)   0

Amazon CloudSearch Limits {#limits_cloudsearch .title}
-------------------------

  Resource           Default Limit
  ------------------ ---------------
  Partitions         10
  Search instances   50

For information about additional documented limits, see [Understanding Amazon CloudSearch Limits](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/limits.html){.ulink}.

DynamoDB Limits {#limits_dynamodb .title}
---------------

  Resource                                  Default Limit
  ----------------------------------------- ---------------
  Read capacity units (individual table)    10,000
  Write capacity units (individual table)   10,000
  Read capacity units (account)             20,000
  Write capacity units (account)            20,000
  Maximum number of tables                  256

For information about additional documented limits, see [Limits in Amazon DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html){.ulink}.

Amazon EBS Limits {#limits_ebs .title}
-----------------

  Resource                                                 Default Limit
  -------------------------------------------------------- ---------------
  Number of EBS volumes                                    5,000
  Number of EBS snapshots                                  10,000
  Total volume storage of General Purpose (SSD) volumes    20 TiB
  Total volume storage of Provisioned IOPS (SSD) volumes   20 TiB
  Total volume storage of Magnetic volumes                 20 TiB
  Total provisioned IOPS                                   40,000

For information about additional documented limits, see [Amazon EC2 Service Limits](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html){.ulink}.

Amazon EC2 Limits {#limits_ec2 .title}
-----------------

  Resource                                                                                                                                                                 Default Limit
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Number of Elastic IP addresses for EC2-Classic. For information about EC2-VPC, see [Amazon VPC Limits](aws_service_limits.html#limits_vpc "Amazon VPC Limits"){.xref}.   5
  Throttle on the emails that can be sent from your Amazon EC2 account                                                                                                     Throttle applied
  Number of on-demand instances                                                                                                                                            Varies depending on instance type. For more information, see [How many instances can I run in Amazon EC2](http://aws.amazon.com/ec2/faqs/#How_many_instances_can_I_run_in_Amazon_EC2){.ulink}.
  Number of Spot Instance requests                                                                                                                                         5 instance requests per region. New AWS accounts might have lower limits. For more information, see [Spot Request Limits](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-limits.html#using-spot-request-limit.html){.ulink}.
  Bid Price for Spot Instances                                                                                                                                             Four times the On-Demand price. For more information, see [Spot Bid Price Limits](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-limits.html#using-spot-bid-limits){.ulink}.
  Number of Reserved Instances                                                                                                                                             20 instance reservations per Availability Zone, per month

For information about additional documented limits, see [Amazon EC2 Service Limits](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html){.ulink}.

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

For information about additional documented limits, see [Elastic Load Balancing Limits](http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/elb-limits.html){.ulink}.

Elastic Transcoder Limits {#limits_elastictranscoder .title}
-------------------------

  Resource                   Default Limit
  -------------------------- ---------------
  Pipelines per region       4
  Active jobs per pipeline   1,000
  Outputs per job            30
  User-defined presets       50

For information about additional documented limits, see [Limits on Pipelines, Jobs, and Presets](http://docs.aws.amazon.com/elastictranscoder/latest/developerguide/limits.html){.ulink}.

IAM Limits {#limits_iam .title}
----------

  Resource              Default Limit
  --------------------- ---------------
  Users                 5,000
  Groups                100
  Groups per user       10
  Roles                 250
  Instance profiles     100
  Server certificates   20

For information about additional documented limits, see [Limitations on IAM Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html){.ulink}.

Amazon Kinesis Limits {#limits_kinesis .title}
---------------------

  Resource                       Default Limit
  ------------------------------ ---------------
  Number of shards per account   10

For information about additional documented limits, see [Amazon Kinesis Sizes and Limits](http://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html){.ulink}.

AWS OpsWorks Limits {#limits_opworks .title}
-------------------

  Resource              Default Limit
  --------------------- ---------------
  Stacks                40
  Layers per stack      40
  Instances per stack   40
  Apps per stack        40

Amazon RDS Limits {#limits_rds .title}
-----------------

  Resource                             Default Limit
  ------------------------------------ ---------------
  Instances                            40
  Reserved Instances                   40
  Total storage for all DB instances   100 TB
  Manual Snapshots                     50
  Parameter Groups                     50
  Security Groups                      25
  Subnet Groups                        20
  Subnets per Subnet Group             20
  Option Groups                        20
  Event Subscriptions                  20
  Read Replicas per Master             5

Amazon Redshift Limits {#limits_redshift .title}
----------------------

  Resource                   Default Limit
  -------------------------- ---------------
  Nodes per cluster          16
  Nodes                      16
  Reserved Nodes             16
  Snapshots                  20
  Parameter Groups           20
  Security Groups            20
  Subnet Groups              20
  Subnets per Subnet Group   20
  Event Subscriptions        20

For information about additional documented limits, see [Limits in Amazon Redshift](http://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html){.ulink}.

Amazon Route 53 Limits {#limits_route53 .title}
----------------------

  Resource                               Default Limit
  -------------------------------------- ---------------
  Hosted zones                           500
  Resource record sets per hosted zone   10,000
  Health checks                          50

For information about additional documented limits, see [Limits on Amazon Route 53 API Requests and Entity Counts](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html){.ulink}.

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

For information about additional documented limits, see [Limits in Amazon SES](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html){.ulink}.

Amazon SimpleDB Limits {#limits_simpledb .title}
----------------------

  Resource   Default Limit
  ---------- ---------------
  Domains    250

For information about additional documented limits, see [Limits](http://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDBLimits.html){.ulink}.

Amazon Simple Notification Service Limits {#limits_sns .title}
-----------------------------------------

  Resource   Default Limit
  ---------- ---------------
  Topics     3,000

Amazon VPC Limits {#limits_vpc .title}
-----------------

  Resource                                                       Default Limit        Comments
  -------------------------------------------------------------- -------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Number of VPCs                                                 5                     
  Number of subnets per VPC                                      200                   
  Number of Internet gateways                                    5                    You can create as many Internet gateways as your 'VPCs per region' limit. Only one Internet gateway can be attached to a VPC at a time.
  Number of virtual private gateways                             5                    Only one virtual private gateway can be attached to a VPC at a time.
  Number of customer gateways                                    50                    
  Number of VPN connections                                      50                   10 per virtual private gateway.
  Number of route tables per VPC                                 200                  Including the main route table. You can associate one route table to one or more subnets in a VPC.
  Number of entries per route table                              50                   This is the limit for the number of non-propagated entries per route table. If this limit is increased, network performance may be impacted.
  Number of Elastic IP addresses                                 5                    This is the limit for the number of VPC Elastic IPs you can allocate within a region. This is a separate limit from the EC2 Elastic IP address limit.
  Number of security groups per VPC                              100                  If this limit is increased, network performance may be impacted, depending on the way the security groups are configured.
  Number of rules per security group                             50                   The multiple of 'rules per security group' and 'security groups per network interface' cannot exceed 250. For example, if you want 100 rules per security group, we’d decrease your number of security groups per network interface to 2.
  Number of security groups per network interface                5                    The multiple of ‘security groups per network interface’ and ‘rules per security group’ cannot exceed 250. For example, if you want 10 security groups per network interface, we’d decrease your number of rules per security group to 25.
  Number of network ACLs per VPC                                 200                  You can associate one network ACL to one or more subnets in a VPC. This limit is not the same as the number of rules per network ACL.
  Number of rules per network ACL                                40                   This is the sum of both ingress and egress rules in a single network ACL, where the limit for ingress rules is 20, and the limit for egress rules is 20.
  Number of BGP advertised routes per VPN connection             100                  If this limit is increased, network performance may be impacted.
  Number of active VPC peering connections per VPC               50                   The maximum limit is 125 peering connections per VPC. The number of entries per route table should be increased accordingly; however, network performance may be impacted.
  Number of outstanding VPC peering connection requests          25                   This is the limit for the number of outstanding VPC peering connection requests that you've requested from your account.
  Expiry time for an unaccepted VPC peering connection request   1 week (168 hours)    

For information about additional documented limits, see [Amazon VPC Limits](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Appendix_Limits.html){.ulink}.

Amazon WorkSpaces Limits {#limits_workspaces .title}
------------------------

  Resource     Default Limit   Comments
  ------------ --------------- --------------------------------------------------------------------------------------------------------------------
  WorkSpaces   2               To prevent denial of service attacks, accounts new to the Amazon WorkSpaces service are limited to two WorkSpaces.

For information about additional documented limits, see [Amazon WorkSpaces Limits](http://docs.aws.amazon.com/workspaces/latest/adminguide/wsp_limits.html){.ulink}.

![](/web/20141004102426im_/http://docs.aws.amazon.com:80/general/latest/gr/images/expanderarrow.png)
  -------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Document Conventions](/web/20141004102426/http://docs.aws.amazon.com:80/general/latest/gr/docconventions.html){.awstoc}   [« Previous](GetTheTools.html){.awstoc}[Next »](api-retries.html){.awstoc}
  [Terms of Use](http://aws.amazon.com/terms/){.awstoc}                                                                      Did this page help you?  [Yes](feedbackyes.html?topic_id=aws_service_limits){.awstoc} | [No](feedbackno.html?topic_id=aws_service_limits){.awstoc} |  [Tell us about it...](https://portal.aws.amazon.com/gp/aws/html-forms-controller/documentation/aws_doc_feedback_04?service_name=Regions&guide_name=General%20Reference&api_version=1.0&file_name=aws_service_limits){.awstoc}
  -------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


