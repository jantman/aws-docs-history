+-----------------------------------------------------------------------+
| [AWS Documentation](http://aws.amazon.com/documentation/) » [AWS      |
| General Reference](http://docs.aws.amazon.com/general/latest/gr/) »   |
| [AWS Service Limits]{.breadcrumb}                                     |
+-----------------------------------------------------------------------+

AWS Service Limits {#aws-service-limits .topictitle}
==================

The following tables provide the default limits for AWS services for an AWS account. Unless otherwise noted, each limit is region specific. Many services contain limits that cannot be changed. For more information about the limits for a specific service, see the documentation for that service.

If your support plan includes Trusted Advisor, you can use it to display your usage and limits for each service in a specific region. For more information, see [Trusted Advisor](http://aws.amazon.com/premiumsupport/trustedadvisor/){.ulink}.

You can take the following steps to request an increase for limits. These increases are not granted immediately, so it may take a couple of days for your increase to become effective.

[]{#d0e12229}
**To request a limit increase**

1.  Open the [AWS Support Center](https://console.aws.amazon.com/support/home#/){.ulink} page, sign in, if necessary, and then choose [Create Case]{.guilabel}.

2.  Under [Regarding]{.guilabel}, choose [Service Limit Increase]{.guilabel}.

3.  Under [Limit Type]{.guilabel}, choose the type of limit to increase, fill in the necessary fields in the form, and then choose your preferred method of contact.

**Default Limits**

-   [Amazon API Gateway Limits](aws_service_limits.html#limits_apigateway)
-   [Amazon AppStream Limits](aws_service_limits.html#limits_appstream)
-   [Auto Scaling Limits](aws_service_limits.html#limits_autoscaling)
-   [AWS Certificate Manager Limits](aws_service_limits.html#limits_acm)
-   [AWS CloudFormation Limits](aws_service_limits.html#limits_cloudformation)
-   [Amazon CloudFront Limits](aws_service_limits.html#limits_cloudfront)
-   [AWS CloudHSM Limits](aws_service_limits.html#limits_cloudhsm)
-   [Amazon CloudSearch Limits](aws_service_limits.html#limits_cloudsearch)
-   [AWS CodeCommit Limits](aws_service_limits.html#limits_codecommit)
-   [AWS CodeDeploy Limits](aws_service_limits.html#limits_codedeploy)
-   [AWS CodePipeline Limits](aws_service_limits.html#limits_codepipeline)
-   [AWS Database Migration Service Limits](aws_service_limits.html#limits_dms)
-   [AWS Device Farm Limits](aws_service_limits.html#limits_devicefarm)
-   [AWS Directory Service Limits](aws_service_limits.html#limits_ds)
-   [Amazon DynamoDB Limits](aws_service_limits.html#limits_dynamodb)
-   [Amazon EC2 Container Registry (Amazon ECR) Limits](aws_service_limits.html#limits_ecr)
-   [Amazon EC2 Container Service (Amazon ECS) Limits](aws_service_limits.html#limits_ecs)
-   [AWS Elastic Beanstalk Limits](aws_service_limits.html#limits_elastic_beanstalk)
-   [Amazon Elastic Block Store (Amazon EBS) Limits](aws_service_limits.html#limits_ebs)
-   [Amazon Elastic Compute Cloud (Amazon EC2) Limits](aws_service_limits.html#limits_ec2)
-   [Amazon EC2 Simple Systems Manager Limits](aws_service_limits.html#limits_ssm)
-   [Amazon ElastiCache Limits](aws_service_limits.html#limits_elasticache)
-   [Elastic Load Balancing Limits](aws_service_limits.html#limits_elastic_load_balancer)
-   [Amazon Elastic Transcoder Limits](aws_service_limits.html#limits_elastictranscoder)
-   [Amazon Elasticsearch Service Limits](aws_service_limits.html#limits_es)
-   [Amazon GameLift Limits](aws_service_limits.html#limits_gamelift)
-   [AWS Identity and Access Management (IAM) Limits](aws_service_limits.html#limits_iam)
-   [AWS Snowball (Snowball) Limits](aws_service_limits.html#limits_snowball)
-   [AWS Key Management Service (AWS KMS) Limits](aws_service_limits.html#limits_kms)
-   [Amazon Kinesis Firehose Limits](aws_service_limits.html#limits-akf)
-   [Amazon Kinesis Streams Limits](aws_service_limits.html#limits-aks)
-   [AWS Lambda Limits](aws_service_limits.html#limits_lambda)
-   [Amazon Machine Learning (Amazon ML) Limits](aws_service_limits.html#limits_machinelearning)
-   [AWS OpsWorks Limits](aws_service_limits.html#limits_opworks)
-   [Amazon Redshift Limits](aws_service_limits.html#limits_redshift)
-   [Amazon Relational Database Service (Amazon RDS) Limits](aws_service_limits.html#limits_rds)
-   [Amazon Route 53 Limits](aws_service_limits.html#limits_route53)
-   [AWS Service Catalog Limits](aws_service_limits.html#limits_servicecatalog)
-   [Amazon Simple Email Service (Amazon SES) Limits](aws_service_limits.html#limits_ses_quota)
-   [Amazon Simple Notification Service (Amazon SNS) Limits](aws_service_limits.html#limits_sns)
-   [Amazon Simple Storage Service (Amazon S3) Limits](aws_service_limits.html#limits_s3)
-   [Amazon Simple Workflow Service (Amazon SWF) Limits](aws_service_limits.html#limits_swf)
-   [Amazon SimpleDB Limits](aws_service_limits.html#limits_simpledb)
-   [Amazon Virtual Private Cloud (Amazon VPC) Limits](aws_service_limits.html#limits_vpc)
-   [AWS WAF Limits](aws_service_limits.html#limits_waf)
-   [Amazon WorkSpaces Limits](aws_service_limits.html#limits_workspaces)

Amazon API Gateway Limits {#limits_apigateway .title}
-------------------------

  ------------------------------------------------------------------------
  Resource                                                 Default Limit
  -------------------------------------------------------- ---------------
  APIs per account                                         60

  API keys per account                                     10,000

  Client certificates per account                          60

  Resources per API                                        300

  Stages per API                                           10

  Timeout for both AWS Lambda and HTTP integrations;       10
  this limit cannot be increased currently                 

  Sustained API requests per account                       500

  Throttled API requests per account                       1000

  Payload size; this limit cannot be increased currently   10 MB
  ------------------------------------------------------------------------

For information about additional documented limits, see [Limits in Amazon API Gateway](http://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html){.ulink} in the [*API Gateway Developer Guide*]{.emphasis}.

Amazon AppStream Limits {#limits_appstream .title}
-----------------------

An Amazon AppStream account has a service limit of up to five concurrent streaming sessions:

-   Up to two concurrent streaming application deployments using the interactive wizard.

-   Up to three streaming applications in the [Building]{.guilabel}, [Active]{.guilabel}, or [Error]{.guilabel} states.

For more information, see [Amazon AppStream Application Lifecycle](http://docs.aws.amazon.com/appstream/latest/developerguide/appstream-application-lifecycle.html){.ulink} in the [*Amazon AppStream Developer Guide*]{.emphasis}.

Auto Scaling Limits {#limits_autoscaling .title}
-------------------

  Resource                                 Default Limit
  ---------------------------------------- ---------------
  Launch configurations                    100
  Auto Scaling groups                      20
  Lifecycle hooks per Auto Scaling group   50
  Load balancers per Auto Scaling group    50
  Step adjustments per scaling policy      20

For information about additional documented limits, see [Auto Scaling Limits](http://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-account-limits.html){.ulink} in the [*Auto Scaling Developer Guide*]{.emphasis}.

AWS Certificate Manager Limits {#limits_acm .title}
------------------------------

  Object                                        Limit
  --------------------------------------------- -------
  Certificates (in Pending and Issued states)   20
  Names per Certificate                         10
  Certificates issued per year                  20

For information about additional documented limits, see [Limits](http://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html){.ulink} in the [*AWS Certificate Manager User Guide*]{.emphasis}.

AWS CloudFormation Limits {#limits_cloudformation .title}
-------------------------

  Resource   Default Limit
  ---------- ---------------
  Stacks     200

For information about additional documented limits, see [AWS CloudFormation Limits](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html){.ulink} in the [*AWS CloudFormation User Guide*]{.emphasis}.

Amazon CloudFront Limits {#limits_cloudfront .title}
------------------------

  Resource                                                                                                                                 Default Limit
  ---------------------------------------------------------------------------------------------------------------------------------------- ---------------------
  Data transfer rate per distribution                                                                                                      10 Gbps
  Requests per second per distribution                                                                                                     15,000
  Web distributions per account                                                                                                            200
  RTMP distributions per account                                                                                                           100
  Alternate domain names (CNAMEs) per distribution                                                                                         100
  Origins per distribution                                                                                                                 25
  Cache behaviors per distribution                                                                                                         25
  Whitelisted headers per cache behavior                                                                                                   10
  Whitelisted cookies per cache behavior                                                                                                   10
  SSL certificates per account when serving HTTPS requests using dedicated IP addresses (no limit when serving HTTPS requests using SNI)   2
  Custom headers that you can have Amazon CloudFront forward to the origin                                                                 10 name/value pairs

For information about additional documented limits, see [Limits](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html){.ulink} in the [*Amazon CloudFront Developer Guide*]{.emphasis}.

AWS CloudHSM Limits {#limits_cloudhsm .title}
-------------------

  Resource                             Default Limit
  ------------------------------------ ---------------
  HSM appliances                       3
  High-availability partition groups   20
  Clients                              800

Amazon CloudSearch Limits {#limits_cloudsearch .title}
-------------------------

  Resource           Default Limit
  ------------------ ---------------
  Partitions         10
  Search instances   50

For information about additional documented limits, see [Understanding Amazon CloudSearch Limits](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/limits.html){.ulink} in the [*Amazon CloudSearch Developer Guide*]{.emphasis}.

AWS CodeCommit Limits {#limits_codecommit .title}
---------------------

  Resource                 Default Limit
  ------------------------ -----------------------
  Number of repositories   1,000 per AWS account

For information about additional documented limits, see [Limits in AWS CodeCommit](http://docs.aws.amazon.com/codecommit/latest/userguide/limits.html){.ulink} in the [*AWS CodeCommit User Guide*]{.emphasis}.

AWS CodeDeploy Limits {#limits_codedeploy .title}
---------------------

  Resource                                                                                Default Limit
  --------------------------------------------------------------------------------------- ---------------
  Number of applications under an account in a single region                              40
  Number of concurrent deployments under an account                                       10
  Number of hours until a deployment fails if not completed                               8
  Number of hours until an individual deployment lifecycle event fails if not completed   1
  Number of deployment groups associated with a single application                        50
  Number of instances in a single deployment                                              50

For information about additional documented limits, see [Limits in AWS CodeDeploy](http://docs.aws.amazon.com/codedeploy/latest/userguide/limits.html){.ulink} in the [*AWS CodeDeploy User Guide*]{.emphasis}.

AWS CodePipeline Limits {#limits_codepipeline .title}
-----------------------

  Resource                                                   Default Limit
  ---------------------------------------------------------- ------------------------------
  Number of pipelines                                        20
  Number of stages                                           Minimum of 2, maxi­mum of 10
  Number of actions                                          Minimum of 1, maxi­mum of 20
  Maximum number of revisions running across all pipelines   20
  Maximum size of source artifacts                           500 megabytes (MB)
  Maximum number of times an action can be run per month     1,000 per calendar month

For information about additional documented limits, see [Limits in AWS CodePipeline](http://docs.aws.amazon.com/codepipeline/latest/userguide/limits.html){.ulink} in the [*AWS CodePipeline User Guide*]{.emphasis}.

AWS Database Migration Service Limits {#limits_dms .title}
-------------------------------------

  Resource                               Default Limit
  -------------------------------------- ---------------
  Replication instances                  20
  Total amount of storage                6 TB
  Event subscriptions                    100
  Replication subnet groups              20
  Subnets per replication subnet group   20
  Endpoints                              100
  Tasks                                  100
  Endpoints per instance                 100

AWS Device Farm Limits {#limits_devicefarm .title}
----------------------

  Resource                                                       Default Limit   Comments
  -------------------------------------------------------------- --------------- --------------------------------------------------
  Maximum app file size you can upload                           4 GB            
  Maximum number of devices Device Farm can test during a run    5               This limit can be increased to 100 upon request.
  Limit on the number of devices you can include in a test run   None            
  Limit on the number of runs you can schedule                   None            

AWS Directory Service Limits {#limits_ds .title}
----------------------------

  Resource                   Default Limit
  -------------------------- -----------------
  Simple AD directories      10
  AD Connector directories   10
  Manual snapshots           5 per Simple AD

Amazon DynamoDB Limits {#limits_dynamodb .title}
----------------------

  Resource                                  Default Limit
  ----------------------------------------- ---------------
  Read capacity units (individual table)    10,000
  Write capacity units (individual table)   10,000
  Read capacity units (account)             20,000
  Write capacity units (account)            20,000
  Maximum number of tables                  256

For information about additional documented limits, see [Limits in Amazon DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html){.ulink} in the [*Amazon DynamoDB Developer Guide*]{.emphasis}.

Amazon EC2 Container Registry (Amazon ECR) Limits {#limits_ecr .title}
-------------------------------------------------

  Resource                                     Default Limit
  -------------------------------------------- ---------------
  Maximum number of repositories per account   1,000
  Maximum number of images per repository      500

Amazon EC2 Container Service (Amazon ECS) Limits {#limits_ecs .title}
------------------------------------------------

  Resource                                                                            Default Limit
  ----------------------------------------------------------------------------------- ----------------------------------
  Number of clusters per region, per account                                          1000
  Number of container instances per cluster                                           1000
  Number of services per cluster                                                      500
  Number of load balancers per service                                                1
  Number of tasks per service                                                         1000
  Number of tasks launched (`count`{.literal}) per [**run-task**]{.command}           10
  Number of container instances per [**start-task**]{.command}                        10
  Throttle on number of container instances per second per [**run-task**]{.command}   5 per cluster
  Throttle on container instance registration rate                                    1 per second / 60 max per minute
  Task definition size limit                                                          32 KiB
  Task definition max containers                                                      10
  Throttle on task definition registration rate                                       1 per second / 60 max per minute

AWS Elastic Beanstalk Limits {#limits_elastic_beanstalk .title}
----------------------------

  Resource       Default Limit
  -------------- ---------------
  Applications   25
  Versions       500
  Environments   200

Amazon Elastic Block Store (Amazon EBS) Limits {#limits_ebs .title}
----------------------------------------------

  Resource                                                 Default Limit
  -------------------------------------------------------- ---------------
  Number of EBS volumes                                    5,000
  Number of EBS snapshots                                  10,000
  Total volume storage of General Purpose (SSD) volumes    20 TiB
  Total volume storage of Provisioned IOPS (SSD) volumes   20 TiB
  Total volume storage of Magnetic volumes                 20 TiB
  Total provisioned IOPS                                   40,000

For information about additional documented limits, see [Amazon EC2 Service Limits](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html){.ulink} in the [*Amazon EC2 User Guide for Linux Instances*]{.emphasis}.

Amazon Elastic Compute Cloud (Amazon EC2) Limits {#limits_ec2 .title}
------------------------------------------------

  Resource                                                               Default Limit
  ---------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Elastic IP addresses for EC2-Classic                                   5
  Security groups for EC2-Classic per instance                           500
  Rules per security group for EC2-Classic                               100
  Key pairs                                                              5,000
  Throttle on the emails that can be sent from your Amazon EC2 account   Throttle applied
  On-demand instances                                                    Limits vary depending on instance type. For more information, see [How many instances can I run in Amazon EC2](http://aws.amazon.com/ec2/faqs/#How_many_instances_can_I_run_in_Amazon_EC2){.ulink}.
  Spot Instances                                                         Limits vary depending on instance type, region, and account. For more information, see [Spot Instance Limits](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-limits.html){.ulink}.
  Reserved Instances                                                     20 instance reservations per Availability Zone, per month
  AMI Copies                                                             Destination regions are limited to 50 concurrent AMI copies at a time, with no more than 25 of those coming from a single source region.

For information about related limits for EC2-VPC, see [Amazon Virtual Private Cloud (Amazon VPC) Limits](aws_service_limits.html#limits_vpc "Amazon Virtual Private Cloud (Amazon VPC) Limits"){.xref}.

For information about viewing your current limits, see [Amazon EC2 Service Limits](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html){.ulink} in the [*Amazon EC2 User Guide for Linux Instances*]{.emphasis}.

Amazon EC2 Simple Systems Manager Limits {#limits_ssm .title}
----------------------------------------

  Resource                             Default Limit
  ------------------------------------ ---------------
  Number of documents per account      200
  Number of associations per account   10,000

Amazon ElastiCache Limits {#limits_elasticache .title}
-------------------------

  -------------------------------------------------------------
  Resource                                      Default Limit
  --------------------------------------------- ---------------
  Nodes per region                              50

  Nodes per cluster (Memcached)                 20
  Nodes per cluster (Redis)                     1

  Read replicas per replication group (Redis)   5
  Clusters per replication group (Redis)        6

  Parameter Groups per region                   20

  Security Groups per region                    50

  Subnet Groups per region                      50

  Subnets per Subnet Group                      20
  -------------------------------------------------------------

These limits are global limits per customer account. If you need to exceed these limits, make your request using the [Amazon ElastiCache Cache Node request form](http://aws.amazon.com/contact-us/elasticache-node-limit-request/){.ulink}.

Elastic Load Balancing Limits {#limits_elastic_load_balancer .title}
-----------------------------

  Resource                                          Default Limit   Comments
  ------------------------------------------------- --------------- ------------------------------------------
  Load balancers per region                         20              This limit can be increased upon request
  Listeners per load balancer                       100             This limit cannot be increased
  Security groups per load balancer                 5               This limit cannot be increased
  Subnets per Availability Zone per load balancer   1               This limit cannot be increased

For information about additional documented limits, see [Elastic Load Balancing Limits](http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/elb-limits.html){.ulink} in the [*Elastic Load Balancing Developer Guide*]{.emphasis}.

Amazon Elastic Transcoder Limits {#limits_elastictranscoder .title}
--------------------------------

  ---------------------------------------------------------------------------------------------------------
  Resource                                                           Default Limit
  ------------------------------------------------------------------ --------------------------------------
  Pipelines per region                                               4

  User-defined presets                                               50

  Maximum number of jobs processed simultaneously by each pipeline   US East (N. Virginia) region – 20
                                                                     
                                                                     US West (N. California) region – 12
                                                                     
                                                                     US West (Oregon) region – 20
                                                                     
                                                                     EU (Ireland) region – 20
                                                                     
                                                                     Asia Pacific (Singapore) region – 12
                                                                     
                                                                     Asia Pacific (Tokyo) region – 12
  ---------------------------------------------------------------------------------------------------------

For information about additional documented limits, see [Amazon Elastic Transcoder](http://docs.aws.amazon.com/elastictranscoder/latest/developerguide/limits.html){.ulink} limits in the [*Amazon Elastic Transcoder Developer Guide*]{.emphasis}.

Amazon Elasticsearch Service Limits {#limits_es .title}
-----------------------------------

[]{#d0e13451}
  Resource                                                Default Limit
  ------------------------------------------------------- ---------------
  Maximum number of Elasticsearch instances per cluster   10

\

Amazon GameLift Limits {#limits_gamelift .title}
----------------------

  ------------------------------------------------------------------------------------------
  Resource                           Default Limit
  ---------------------------------- -------------------------------------------------------
  Aliases                            100

  Fleets                             20

  Builds                             1000

  Total size of builds               100 GB

  Log upload size per game session   200 MB

  On-demand instances                Limits vary depending on instance type;
                                     20 instances per account, regardless of instance type

  Player sessions per game session   200
  ------------------------------------------------------------------------------------------

For information about additional documented limits, see [Scaling Amazon Elastic Compute Cloud (Amazon EC2) Instances](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html){.ulink} in the [*Amazon GameLift Developer Guide*]{.emphasis}.

AWS Identity and Access Management (IAM) Limits {#limits_iam .title}
-----------------------------------------------

For information about AWS Identity and Access Management (IAM) limits, see [Limitations on IAM Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html){.ulink} in the [*IAM User Guide*]{.emphasis}.

AWS Snowball (Snowball) Limits {#limits_snowball .title}
------------------------------

  Resource   Default limit   Comments
  ---------- --------------- ----------------------------------------------------------
  Snowball   1               If you need to increase this limit, contact AWS Support.

AWS Key Management Service (AWS KMS) Limits {#limits_kms .title}
-------------------------------------------

  Resource                               Default Limit
  -------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Customer Master Keys (CMKs)            1000
  Aliases                                1100
  Grants per CMK                         250
  Grants for a given principal per CMK   30
  Requests per second                    Varies by API operation; see [Limits](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html){.ulink} in the [*AWS Key Management Service Developer Guide*]{.emphasis}.

All limits in the preceding table apply per region and per AWS account.

For information about additional documented limits, see [Limits](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html){.ulink} in the [*AWS Key Management Service Developer Guide*]{.emphasis}.

Amazon Kinesis Firehose Limits {#limits-akf .title}
------------------------------

  Resource                      Default Limit
  ----------------------------- ---------------
  Delivery streams per region   20

For information about additional documented limits, see [Amazon Kinesis Firehose Limits](http://docs.aws.amazon.com/firehose/latest/dev/limits.html){.ulink} in the [*Amazon Kinesis Firehose Developer Guide*]{.emphasis}.

Amazon Kinesis Streams Limits {#limits-aks .title}
-----------------------------

  -------------------------------------------------------
  Resource            Default Limit
  ------------------- -----------------------------------
  Shards per region   US East (N. Virginia) region – 50
                      
                      US West (Oregon) region – 50
                      
                      EU (Ireland) region – 50
                      
                      All other supported regions – 25
  -------------------------------------------------------

For information about additional documented limits, see [Amazon Kinesis Streams Limits](http://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html){.ulink} in the [*Amazon Kinesis Streams Developer Guide*]{.emphasis}.

AWS Lambda Limits {#limits_lambda .title}
-----------------

[]{#d0e13692}
  Resource                                          Limit
  ------------------------------------------------- -------
  Concurrent requests safety throttle per account   100

\
For information about additional documented limits, see [AWS Lambda Limits](http://docs.aws.amazon.com/lambda/latest/dg/limits.html){.ulink} in the [*AWS Lambda Developer Guide*]{.emphasis}.

Amazon Machine Learning (Amazon ML) Limits {#limits_machinelearning .title}
------------------------------------------

  Resource                                                               Default Limit
  ---------------------------------------------------------------------- ---------------
  Data file size\*                                                       100 GB
  Batch prediction input size                                            1 TB
  Batch prediction input (number of records)                             100 million
  Number of variables in a data file (schema)                            1,000
  Recipe complexity (number of processed output variables)               10,000
  Transactions Per Second for each real-time prediction endpoint         200
  Total Transactions Per Second for all real-time prediction endpoints   10,000
  Total RAM for all real-time prediction endpoints                       10 GB
  Number of simultaneous jobs                                            5
  Longest run time for any job                                           7 days
  Number of classes for multiclass ML models                             100
  ML model size                                                          2 GB

Note

The size of your data files is limited to ensure that jobs finish in a timely manner. Jobs that have been running for more than seven days will be automatically terminated, resulting in a FAILED status.

For information about additional documented limits, see [Amazon ML Limits](http://docs.aws.amazon.com/machine-learning/latest/dg/system-limits.html){.ulink} in the [*Amazon Machine Learning Developer Guide*]{.emphasis}.

AWS OpsWorks Limits {#limits_opworks .title}
-------------------

  Resource              Default Limit
  --------------------- ---------------
  Stacks                40
  Layers per stack      40
  Instances per stack   40
  Apps per stack        40

Amazon Redshift Limits {#limits_redshift .title}
----------------------

  Resource                   Default Limit
  -------------------------- ---------------
  Nodes per cluster          101
  Nodes                      200
  Reserved Nodes             200
  Snapshots                  20
  Parameter Groups           20
  Security Groups            20
  Subnet Groups              20
  Subnets per Subnet Group   20
  Event Subscriptions        20

For information about additional documented limits, see [Limits in Amazon Redshift](http://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html){.ulink} in the [*Amazon Redshift Cluster Management Guide*]{.emphasis}.

Amazon Relational Database Service (Amazon RDS) Limits {#limits_rds .title}
------------------------------------------------------

  Resource                             Default Limit
  ------------------------------------ ---------------
  Instances                            40
  Reserved Instances                   40
  Total storage for all DB instances   100 TB
  Manual Snapshots                     50
  Parameter Groups                     50
  Security Groups                      25
  VPC Security Groups                  5
  Subnet Groups                        20
  Subnets per Subnet Group             20
  Option Groups                        20
  Event Subscriptions                  20
  Read Replicas per Master             5

Amazon Route 53 Limits {#limits_route53 .title}
----------------------

  Resource                                                        Default Limit
  --------------------------------------------------------------- ---------------
  Hosted zones                                                    500
  Domains                                                         50
  Resource record sets per hosted zone                            10,000
  Reusable delegation sets                                        100
  Hosted zones that can use the same reusable delegation set      100
  Amazon VPCs that you can associate with a private hosted zone   100
  Health checks                                                   50
  Traffic policies                                                50
  Policy records                                                  5

For information about additional documented limits, see [Amazon Route 53 Limits](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html){.ulink} in the [*Amazon Route 53 Developer Guide*]{.emphasis}.

AWS Service Catalog Limits {#limits_servicecatalog .title}
--------------------------

  Resource                   Default Limit
  -------------------------- ----------------------------------------------
  Portfolios                 25
  Users, groups, and roles   25 per portfolio
  Products                   25 per portfolio, 25 total
  Product versions           10 per product
  Constraints                25 per product per portfolio
  Tags                       3 per product, 3 per portfolio, 10 per stack
  Stacks                     200 (AWS CloudFormation limit)

Amazon Simple Email Service (Amazon SES) Limits {#limits_ses_quota .title}
-----------------------------------------------

The following are the default limits for Amazon SES in the sandbox environment.

  -------------------------------------------------------------------------------------------------------------------------------
  Resource                         Default Limit
  -------------------------------- ----------------------------------------------------------------------------------------------
  Daily sending quota              200 messages per 24 hour period.

  Maximum send rate                1 email per second.
                                   Note
                                   
                                   The rate at which Amazon SES accepts your messages might be less than the maximum send rate.

  Recipient address verification   All recipient addresses must be verified.
  -------------------------------------------------------------------------------------------------------------------------------

For information about additional documented limits, see [Limits in Amazon SES](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html){.ulink} in the [*Amazon Simple Email Service Developer Guide*]{.emphasis}.

Amazon Simple Notification Service (Amazon SNS) Limits {#limits_sns .title}
------------------------------------------------------

  Resource                 Default Limit
  ------------------------ ---------------
  Topics per AWS account   100,000

Amazon Simple Storage Service (Amazon S3) Limits {#limits_s3 .title}
------------------------------------------------

  Resource   Default Limit
  ---------- -----------------
  Buckets    100 per account

For information about additional documented limits, see [Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html){.ulink} limits in the [*[*Amazon Simple Storage Service Developer Guide*]{.emphasis}*]{.emphasis}.

Amazon Simple Workflow Service (Amazon SWF) Limits {#limits_swf .title}
--------------------------------------------------

For information about additional documented limits, see [Amazon SWF Service Limits](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-limits.html){.ulink} in the [*Amazon Simple Workflow Service Developer Guide*]{.emphasis}.

Amazon SimpleDB Limits {#limits_simpledb .title}
----------------------

  Resource   Default Limit
  ---------- ---------------
  Domains    250

For information about additional documented limits, see [Amazon SimpleDB Limits](http://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDBLimits.html){.ulink} in the [*Amazon SimpleDB Developer Guide*]{.emphasis}.

Amazon Virtual Private Cloud (Amazon VPC) Limits {#limits_vpc .title}
------------------------------------------------

  Resource                                                                           Default limit        Comments
  ---------------------------------------------------------------------------------- -------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  VPCs per region                                                                    5                    The limit for Internet gateways per region is directly correlated to this one. Increasing this limit will increase the limit on Internet gateways per region by the same amount. If you need to increase this limit, [submit a request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-vpc){.ulink}.
  Subnets per VPC                                                                    200                  If you need to increase this limit, [submit a request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-vpc){.ulink}.
  Internet gateways per region                                                       5                    This limit is directly correlated with the limit on VPCs per region. You cannot increase this limit individually; the only way to increase this limit is to increase the limit on VPCs per region. Only one Internet gateway can be attached to a VPC at a time.
  Virtual private gateways per region                                                5                    If you need to increase this limit, contact AWS Support; however, only one virtual private gateway can be attached to a VPC at a time.
  Customer gateways per region                                                       50                   If you need to increase this limit, contact AWS Support.
  VPN connections per region                                                         50                   If you need to increase this limit, [submit a request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-vpc){.ulink}.
  VPN connections per VPC (per virtual private gateway)                              10                   If you need to increase this limit, [submit a request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-vpc){.ulink}.
  Route tables per VPC                                                               200                  Including the main route table. You can associate one route table to one or more subnets in a VPC.
  Routes per route table (non-propagated routes)                                     50                   This is the limit for the number of non-propagated entries per route table. You can [submit a request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-vpc){.ulink} for an increase of up to a maximum of 100; however, network performance may be impacted.
  BGP advertised routes per route table (propagated routes)                          100                  You can have up to 100 propagated routes per route table; however, the total number of propagated and non-propagated entries per route table cannot exceed 100. For example, if you have 50 non-propagated entries (the default limit for this type of entry), you can only have 50 propagated entries. This limit cannot be increased. If you require more than 100 prefixes, advertise a default route.
  Elastic IP addresses per region for each AWS account                               5                    This is the limit for the number of VPC Elastic IP addresses you can allocate within a region. This is a separate limit from the Amazon EC2 Elastic IP address limit. If you need to increase this limit, [submit a request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-vpc){.ulink}.
  Security groups per VPC                                                            500                  If you need to increase this limit, you can [submit a request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-vpc){.ulink}.
  Inbound or outbound rules per security group                                       50                   You can have 50 inbound and 50 outbound rules per security group (giving a total of 100 combined inbound and outbound rules). If you need to increase or decrease this limit, you can contact AWS Support — a limit change applies to both inbound and outbound rules. However, the multiple of the limit for rules per security group and the limit for security groups per network interface cannot exceed 250. For example, if you want 100 rules per security group, we decrease your number of security groups per network interface to 2.
  Security groups per network interface                                              5                    If you need to increase or decrease this limit, you can contact AWS Support. The maximum is 16. The multiple of the limit for security groups per network interface and the limit for rules per security group cannot exceed 250. For example, if you want 10 security groups per network interface, we decrease your number of rules per security group to 25.
  Network interfaces per instance                                                    -                    This limit varies by instance type. For more information, see [Private IP Addresses Per ENI Per Instance Type](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI){.ulink}.
  Network interfaces per VPC                                                         100                  This limit is calculated by multiplying your On-Demand instance limit by 5. The default limit for On-Demand instances is 20. You can increase the number of network interfaces per VPC by contacting AWS Support, or by increasing your On-Demand instance limit.
  Network ACLs per VPC                                                               200                  You can associate one network ACL to one or more subnets in a VPC. This limit is not the same as the number of rules per network ACL.
  Rules per network ACL                                                              20                   This is the one-way limit for a single network ACL, where the limit for ingress rules is 20, and the limit for egress rules is 20. This limit can be increased upon request up to a maximum if 40; however, network performance may be impacted due to the increased workload to process the additional rules.
  Active VPC peering connections per VPC                                             50                   If you need to increase this limit, contact AWS Support . The maximum limit is 125 peering connections per VPC. The number of entries per route table should be increased accordingly; however, network performance may be impacted.
  Outstanding VPC peering connection requests                                        25                   This is the limit for the number of outstanding VPC peering connection requests that you've requested from your account. If you need to increase this limit, contact AWS Support.
  Expiry time for an unaccepted VPC peering connection request                       1 week (168 hours)   If you need to increase this limit, contact AWS Support.
  VPC endpoints per region                                                           20                   If you need to increase this limit, contact AWS Support; up to a maximum of 255 endpoints per VPC.
  Flow logs per single network interface, single subnet, or single VPC in a region   2                    You can effectively have 6 flow logs per network interface if you create 2 flow logs for the subnet, and 2 flow logs for the VPC in which your network interface resides. This limit cannot be increased.
  NAT gateways per Availability Zone                                                 5                    If you need to increase this limit, [submit a request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-vpc){.ulink}. A NAT gateway in the `pending`{.code}, `active`{.code}, or `deleting`{.code} state counts against your limit.

For information about additional documented limits, see [Amazon VPC Limits](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Appendix_Limits.html){.ulink} in the [*Amazon VPC User Guide*]{.emphasis}.

AWS WAF Limits {#limits_waf .title}
--------------

  Resource                 Default Limit
  ------------------------ ---------------
  Web ACLs per account     10
  Rules per account        50
  Conditions per account   50

For information about additional documented limits, see [AWS WAF Limits](http://docs.aws.amazon.com/waf/latest/developerguide/limits.html){.ulink} in the [*AWS WAF Developer Guide*]{.emphasis}.

Amazon WorkSpaces Limits {#limits_workspaces .title}
------------------------

  Resource     Default Limit   Comments
  ------------ --------------- ---------------------------------------------------------------------------------------------------------------------
  WorkSpaces   5               To prevent denial of service attacks, accounts new to the Amazon WorkSpaces service are limited to five WorkSpaces.

For information about additional documented limits, see [Amazon WorkSpaces Limits](http://docs.aws.amazon.com/workspaces/latest/adminguide/wsp_limits.html){.ulink} in the [*Amazon WorkSpaces Administration Guide*]{.emphasis}.

![](/web/20160413223641im_/https://docs.aws.amazon.com/general/latest/gr/images/expanderarrow.png)
[Document Conventions](/web/20160413223641/https://docs.aws.amazon.com/general/latest/gr/docconventions.html)

[« Previous](signature-version-2.html){.awstoc}[Next »](aws-ip-ranges.html){.awstoc}

© 2016, Amazon Web Services, Inc. or its affiliates. All rights reserved.
