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

[]{#d0e13617}
**To request a limit increase**

1.  Open the [AWS Support Center](https://console.aws.amazon.com/support/home#/){.ulink} page, sign in, if necessary, and then choose [Create Case]{.guilabel}.

2.  Under [Regarding]{.guilabel}, choose [Service Limit Increase]{.guilabel}.

3.  Under [Limit Type]{.guilabel}, choose the type of limit to increase, fill in the necessary fields in the form, and then choose your preferred method of contact.

**Default Limits**

-   [Amazon API Gateway Limits](aws_service_limits.html#limits_apigateway)
-   [AWS Application Discovery Service Limits](aws_service_limits.html#limits_appdiscserve)
-   [Amazon AppStream Limits](aws_service_limits.html#limits_appstream)
-   [Application Auto Scaling Limits](aws_service_limits.html#limits_as-app)
-   [Auto Scaling Limits](aws_service_limits.html#limits_autoscaling)
-   [AWS Certificate Manager Limits](aws_service_limits.html#limits_acm)
-   [AWS CloudFormation Limits](aws_service_limits.html#limits_cloudformation)
-   [Amazon CloudFront Limits](aws_service_limits.html#limits_cloudfront)
-   [AWS CloudHSM Limits](aws_service_limits.html#limits_cloudhsm)
-   [Amazon CloudSearch Limits](aws_service_limits.html#limits_cloudsearch)
-   [Amazon CloudWatch Limits](aws_service_limits.html#limits_cloudwatch)
-   [Amazon CloudWatch Events Limits](aws_service_limits.html#limits_cloudwatch_events)
-   [Amazon CloudWatch Logs Limits](aws_service_limits.html#limits_cloudwatch_logs)
-   [AWS CodeCommit Limits](aws_service_limits.html#limits_codecommit)
-   [AWS CodeDeploy Limits](aws_service_limits.html#limits_codedeploy)
-   [AWS CodePipeline Limits](aws_service_limits.html#limits_codepipeline)
-   [AWS Data Pipeline Limits](aws_service_limits.html#limits_datapipeline)
-   [AWS Database Migration Service Limits](aws_service_limits.html#limits_dms)
-   [AWS Device Farm Limits](aws_service_limits.html#limits_devicefarm)
-   [AWS Direct Connect Limits](aws_service_limits.html#limits_directconnect)
-   [AWS Directory Service Limits](aws_service_limits.html#limits_ds)
-   [Amazon DynamoDB Limits](aws_service_limits.html#limits_dynamodb)
-   [Amazon EC2 Container Registry (Amazon ECR) Limits](aws_service_limits.html#limits_ecr)
-   [Amazon EC2 Container Service (Amazon ECS) Limits](aws_service_limits.html#limits_ecs)
-   [Amazon EC2 Simple Systems Manager Limits](aws_service_limits.html#limits_ssm)
-   [AWS Elastic Beanstalk Limits](aws_service_limits.html#limits_elastic_beanstalk)
-   [Amazon Elastic Block Store (Amazon EBS) Limits](aws_service_limits.html#limits_ebs)
-   [Amazon Elastic Compute Cloud (Amazon EC2) Limits](aws_service_limits.html#limits_ec2)
-   [Amazon Elastic File System Limits](aws_service_limits.html#limits_elasticfilesystem)
-   [Elastic Load Balancing Limits](aws_service_limits.html#limits_elastic_load_balancer)
-   [Amazon Elastic Transcoder Limits](aws_service_limits.html#limits_elastictranscoder)
-   [Amazon ElastiCache Limits](aws_service_limits.html#limits_elasticache)
-   [Amazon Elasticsearch Service Limits](aws_service_limits.html#limits_es)
-   [Amazon GameLift Limits](aws_service_limits.html#limits_gamelift)
-   [AWS Identity and Access Management (IAM) Limits](aws_service_limits.html#limits_iam)
-   [AWS Import/Export Limits](aws_service_limits.html#limits-import-export)
-   [Amazon Inspector Limits](aws_service_limits.html#limits_inspector)
-   [AWS IoT Limits](aws_service_limits.html#limits_iot)
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
-   [Amazon Simple Queue Service (Amazon SQS)](aws_service_limits.html#limits_sqs)
-   [Amazon Simple Storage Service (Amazon S3) Limits](aws_service_limits.html#limits_s3)
-   [Amazon Simple Workflow Service (Amazon SWF) Limits](aws_service_limits.html#limits_swf)
-   [Amazon SimpleDB Limits](aws_service_limits.html#limits_simpledb)
-   [AWS Storage Gateway Limits](aws_service_limits.html#limits_storage_gateway)
-   [Amazon Virtual Private Cloud (Amazon VPC) Limits](aws_service_limits.html#limits_vpc)
-   [AWS WAF Limits](aws_service_limits.html#limits_waf)
-   [Amazon WorkSpaces Limits](aws_service_limits.html#limits_workspaces)

Amazon API Gateway Limits {#limits_apigateway .title}
-------------------------

The following limits apply to configuring and running an API in Amazon API Gateway and can be increased upon request to optimize performances of a deployed API in Amazon API Gateway.

  Resource or Operation             Default Limit
  --------------------------------- ---------------------------------------------------------------
  Throttle rate per account         1000 request per second (rps) with a burst limit of 2000 rps.
  APIs per account                  60
  API keys per account              500
  Usage plans per account           300
  Custom authorizers per API        10
  Client certificates per account   60
  Resources per API                 300
  Stages per API                    10

For information about additional documented limits, see [Limits in Amazon API Gateway](http://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html){.ulink} in the [*API Gateway Developer Guide*]{.emphasis}.

AWS Application Discovery Service Limits {#limits_appdiscserve .title}
----------------------------------------

  Resource                                               Default Limit
  ------------------------------------------------------ ---------------
  Inactive agents heartbeating but not collecting data   10,000
  Active agents sending data to the service              250
  Total collected data for all agents, per day           10 GB
  Data storage duration before being purged              90 days

Amazon AppStream Limits {#limits_appstream .title}
-----------------------

An Amazon AppStream account has a service limit of up to five concurrent streaming sessions:

-   Up to two concurrent streaming application deployments using the interactive wizard.

-   Up to three streaming applications in the [Building]{.guilabel}, [Active]{.guilabel}, or [Error]{.guilabel} states.

For more information, see [Amazon AppStream Application Lifecycle](http://docs.aws.amazon.com/appstream/latest/developerguide/appstream-application-lifecycle.html){.ulink} in the [*Amazon AppStream Developer Guide*]{.emphasis}.

Application Auto Scaling Limits {#limits_as-app .title}
-------------------------------

  Resource                               Default Limit
  -------------------------------------- ---------------
  Scalable targets                       500
  Scaling policies per scalable target   50
  Step adjustments per scaling policy    20

Auto Scaling Limits {#limits_autoscaling .title}
-------------------

  Resource                                   Default Limit
  ------------------------------------------ ---------------
  Launch configurations                      100
  Auto Scaling groups                        20
  Scaling policies per Auto Scaling group    50
  Scheduled actions per Auto Scaling group   125
  Lifecycle hooks per Auto Scaling group     50
  SNS topics per Auto Scaling group          10
  Load balancers per Auto Scaling group      50
  Target groups per Auto Scaling group       50
  Step adjustments per scaling policy        20

For information about additional documented limits, see [Auto Scaling Limits](http://docs.aws.amazon.com/autoscaling/latest/userguide/as-account-limits.html){.ulink} in the [*Auto Scaling User Guide*]{.emphasis}.

AWS Certificate Manager Limits {#limits_acm .title}
------------------------------

  Item                                         Default Limit
  -------------------------------------------- ---------------
  Number of ACM Certificates                   100
  Number of domain names per ACM Certificate   10

For more information about these limits, see [Limits](http://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html){.ulink} in the [*AWS Certificate Manager User Guide*]{.emphasis}.

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
  Custom headers that you can have Amazon CloudFront forward to the origin                                                                 10 name–value pairs

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

Amazon CloudWatch Limits {#limits_cloudwatch .title}
------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Resource                                                                                                                      Default Limit                       Comments
  ----------------------------------------------------------------------------------------------------------------------------- ----------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [DescribeAlarms](http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html){.ulink}             3 transactions per second (TPS)     The maximum number of operation requests you can make per second without being throttled.
                                                                                                                                                                    
                                                                                                                                                                    You can [request a limit increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-amazon-cloudwatch){.ulink}.

  [GetMetricStatistics](http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html){.ulink}   400 transactions per second (TPS)   The maximum number of operation requests you can make per second without being throttled.
                                                                                                                                                                    
                                                                                                                                                                    You can [request a limit increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-amazon-cloudwatch){.ulink}.

  [ListMetrics](http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html){.ulink}                   25 transactions per second (TPS)    The maximum number of operation requests you can make per second without being throttled.
                                                                                                                                                                    
                                                                                                                                                                    You can [request a limit increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-amazon-cloudwatch){.ulink}.

  [PutMetricAlarm](http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html){.ulink}             3 transactions per second (TPS)     The maximum number of operation requests you can make per second without being throttled.
                                                                                                                                                                    
                                                                                                                                                                    You can [request a limit increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-amazon-cloudwatch){.ulink}.

  [PutMetricData](http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricData.html){.ulink}               150 transactions per second (TPS)   The maximum number of operation requests you can make per second without being throttled.
                                                                                                                                                                    
                                                                                                                                                                    You can [request a limit increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-amazon-cloudwatch){.ulink}.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For information about additional documented limits, see [CloudWatch, CloudWatch Events, and CloudWatch Logs Limits](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_limits.html){.ulink} in the [*Amazon CloudWatch Developer Guide*]{.emphasis}.

Amazon CloudWatch Events Limits {#limits_cloudwatch_events .title}
-------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Resource   Default Limit   Comments
  ---------- --------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Rules      50/account      You can [request a limit increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-cloudwatch-events){.ulink}.
                             
                             Before requesting a limit increase, examine your rules. You may have multiple rules each matching to very specific events. Consider broadening their scope by using fewer identifiers in your [Events and Event Patterns](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.html){.ulink}. In addition, a rule can invoke several targets each time it matches an event. Consider adding more targets to your rules.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For information about additional documented limits, see [CloudWatch, CloudWatch Events, and CloudWatch Logs Limits](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_limits.html){.ulink} in the [*Amazon CloudWatch Developer Guide*]{.emphasis}.

Amazon CloudWatch Logs Limits {#limits_cloudwatch_logs .title}
-----------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Resource                                                                                                                        Default Limit                                    Comments
  ------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [CreateLogGroup](http://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.html){.ulink}           500 log groups/account/region                    If you exceed your log group limit, you get a `ResourceLimitExceeded`{.code} exception.
                                                                                                                                                                                   
                                                                                                                                                                                   You can [request a limit increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-cloudwatch-logs){.ulink}.

  [DescribeLogStreams](http://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogStreams.html){.ulink}   5 transactions per second (TPS)/account/region   If you experience frequent throttling, you can [request a limit increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-cloudwatch-logs){.ulink}.

  [FilterLogEvents](http://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.html){.ulink}         5 transactions per second (TPS)/account/region   This limit can be changed only in special circumstances. If you experience frequent throttling, contact AWS Support.

  [GetLogEvents](http://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.html){.ulink}               5 transactions per second (TPS)/account/region   We recommend subscriptions if you are continuously processing new data. If you need historical data, we recommend exporting your data to Amazon S3. This limit can be changed only in special circumstances. If you experience frequent throttling, contact AWS Support.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For information about additional documented limits, see [CloudWatch, CloudWatch Events, and CloudWatch Logs Limits](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_limits.html){.ulink} in the [*Amazon CloudWatch Developer Guide*]{.emphasis}.

AWS CodeCommit Limits {#limits_codecommit .title}
---------------------

  Resource                 Default Limit
  ------------------------ -----------------------
  Number of repositories   1,000 per AWS account

For information about additional documented limits, see [Limits in AWS CodeCommit](http://docs.aws.amazon.com/codecommit/latest/userguide/limits.html){.ulink} in the [*AWS CodeCommit User Guide*]{.emphasis}.

AWS CodeDeploy Limits {#limits_codedeploy .title}
---------------------

  Resource                                                           Default Limit
  ------------------------------------------------------------------ ---------------
  Number of applications under an account in a single region         40
  Number of concurrent deployments under an account                  10
  Number of deployment groups associated with a single application   50
  Number of instances in a single deployment                         50

For information about additional documented limits, see [Limits in AWS CodeDeploy](http://docs.aws.amazon.com/codedeploy/latest/userguide/limits.html){.ulink} in the [*AWS CodeDeploy User Guide*]{.emphasis}.

AWS CodePipeline Limits {#limits_codepipeline .title}
-----------------------

  Resource                                                   Default Limit
  ---------------------------------------------------------- ------------------------------
  Number of pipelines per AWS account                        20
  Number of stages in a pipeline                             Minimum of 2, maxi­mum of 10
  Number of actions in a stage                               Minimum of 1, maxi­mum of 20
  Number of parallel actions in a stage                      5
  Number of sequential actions in a stage                    5
  Number of custom actions per AWS account                   20
  Maximum number of revisions running across all pipelines   20
  Maximum size of source artifacts                           500 megabytes (MB)
  Maximum number of times an action can be run per month     1,000 per calendar month

It may take up to two weeks to process requests for a limit increase.

For information about additional documented limits, see [Limits in AWS CodePipeline](http://docs.aws.amazon.com/codepipeline/latest/userguide/limits.html){.ulink} in the [*AWS CodePipeline User Guide*]{.emphasis}.

AWS Data Pipeline Limits {#limits_datapipeline .title}
------------------------

  Attribute                                                Limit                            Adjustable
  -------------------------------------------------------- -------------------------------- ------------
  Number of pipelines                                      100                              Yes
  Number of objects per pipeline                           100                              Yes
  Number of active instances per object                    5                                Yes
  Number of fields per object                              50                               No
  Number of UTF8 bytes per field name or identifier        256                              No
  Number of UTF8 bytes per field                           10,240                           No
  Number of UTF8 bytes per object                          15,360 (including field names)   No
  Rate of creation of a instance from an object            1 per 5 minutes                  No
  Retries of a pipeline activity                           5 per task                       No
  Minimum delay between retry attempts                     2 minutes                        No
  Minimum scheduling interval                              15 minutes                       No
  Maximum number of roll-ups into a single object          32                               No
  Maximum number of EC2 instances per Ec2Resource object   1                                No

For additional limits, see [AWS Data Pipeline Limits](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-limits.html){.ulink} in the [*AWS Data Pipeline Developer Guide*]{.emphasis}.

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

  Resource                                                  Default Limit   Comments
  --------------------------------------------------------- --------------- --------------------------------------------------
  App file size you can upload                              4 GB            
  Number of devices AWS Device Farm can test during a run   5               This limit can be increased to 100 upon request.
  Number of devices you can include in a test run           None            
  Number of runs you can schedule                           None             
  Duration of a remote access session                       60 minutes       

AWS Direct Connect Limits {#limits_directconnect .title}
-------------------------

  Resource                                                       Default Limit   Comment
  -------------------------------------------------------------- --------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Virtual interfaces per AWS Direct Connect connection           50              If you need to increase this limit, [submit a request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-direct-connect){.ulink}.
  Active AWS Direct Connect connections per region per account   50              If you need to increase this limit, [submit a request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-direct-connect){.ulink}.
  Routes per Border Gateway Protocol (BGP) session               100             This limit cannot be increased.

AWS Directory Service Limits {#limits_ds .title}
----------------------------

  Resource                   Default Limit
  -------------------------- -----------------
  Simple AD directories      10
  AD Connector directories   10
  Manual snapshots           5 per Simple AD

Amazon DynamoDB Limits {#limits_dynamodb .title}
----------------------

  -------------------------------------------------------------------------------------------------------------------------
  Resource                                                     Default Limit
  ------------------------------------------------------------ ------------------------------------------------------------
  US East (N. Virginia) Region:                                40,000 read capacity units and 40,000 write capacity units
  Maximum capacity units per table or global secondary index   

  US East (N. Virginia) Region:                                80,000 read capacity units and 80,000 write capacity units
  Maximum capacity units per account                           

  All other regions:                                           10,000 read capacity units and 10,000 write capacity units
  Maximum capacity units per table or global secondary index   

  All other regions:                                           20,000 read capacity units and 20,000 write capacity units
  Maximum capacity units per account                           

  Maximum number of tables                                     256
  -------------------------------------------------------------------------------------------------------------------------

For information about additional documented limits, see [Limits in Amazon DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html){.ulink} in the [*Amazon DynamoDB Developer Guide*]{.emphasis}.

Amazon EC2 Container Registry (Amazon ECR) Limits {#limits_ecr .title}
-------------------------------------------------

  Resource                                     Default Limit
  -------------------------------------------- ---------------
  Maximum number of repositories per account   1,000
  Maximum number of images per repository      1,000

For information about additional documented limits, see [Amazon ECR Service Limits](http://docs.aws.amazon.com/AmazonECR/latest/userguide/service_limits.html){.ulink} in the [*Amazon EC2 Container Registry User Guide*]{.emphasis}.

Amazon EC2 Container Service (Amazon ECS) Limits {#limits_ecs .title}
------------------------------------------------

  Resource                                    Default Limit
  ------------------------------------------- ---------------
  Number of clusters per region per account   1000
  Number of container instances per cluster   1000
  Number of services per cluster              500

For information about additional documented limits, see [Amazon ECS Service Limits](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service_limits.html){.ulink} in the [*Amazon EC2 Container Service Developer Guide*]{.emphasis}.

Amazon EC2 Simple Systems Manager Limits {#limits_ssm .title}
----------------------------------------

  Resource                        Default Limit   Comment
  ------------------------------- --------------- -----------------------------------------------------------------------------------------
  Managed instances               1000            Each AWS account can register/activate a maximum of 1000 managed instances in a region.
  SSM documents                   200             Each AWS account can create a maximum of 200 documents.
  Privately shared SSM document   20              A single SSM document can be shared with a maximum of 20 AWS accounts.
  Publicly shared SSM document    5               Each AWS account can publicly share a maximum of five documents.
  Associations                    10,000          Each SSM document can be associated with a maximum of 10,000 instances.

AWS Elastic Beanstalk Limits {#limits_elastic_beanstalk .title}
----------------------------

  Resource               Default Limit
  ---------------------- ---------------
  Applications           75
  Application Versions   1000
  Environments           200

Amazon Elastic Block Store (Amazon EBS) Limits {#limits_ebs .title}
----------------------------------------------

  Resource                                                              Default Limit
  --------------------------------------------------------------------- ---------------
  Number of EBS volumes                                                 5,000
  Number of EBS snapshots                                               10,000
  Total volume storage of General Purpose SSD (`gp2`{.code}) volumes    20 TiB
  Total volume storage of Provisioned IOPS SSD (`io1`{.code}) volumes   20 TiB
  Total volume storage of Throughput Optimized HDD (`st1`{.code})       20 TiB
  Total volume storage of Cold HDD (`sc1`{.code})                       20 TiB
  Total volume storage of Magnetic volumes                              20 TiB
  Total provisioned IOPS                                                40,000 

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
  On-Demand instances                                                    Limits vary depending on instance type. For more information, see [How many instances can I run in Amazon EC2](http://aws.amazon.com/ec2/faqs/#How_many_instances_can_I_run_in_Amazon_EC2){.ulink}.
  Spot Instances                                                         Limits vary depending on instance type, region, and account. For more information, see [Spot Instance Limits](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-limits.html){.ulink}.
  Reserved Instances                                                     20 instance reservations per Availability Zone, per month.
  Dedicated Hosts                                                        Up to 2 Dedicated Hosts per instance family, per region can be allocated.
  AMI Copies                                                             Destination regions are limited to 50 concurrent AMI copies at a time, with no more than 25 of those coming from a single source region.

For information about related limits for EC2-VPC, see [Amazon Virtual Private Cloud (Amazon VPC) Limits](aws_service_limits.html#limits_vpc "Amazon Virtual Private Cloud (Amazon VPC) Limits"){.xref}.

For information about viewing your current limits, see [Amazon EC2 Service Limits](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html){.ulink} in the [*Amazon EC2 User Guide for Linux Instances*]{.emphasis}.

Amazon Elastic File System Limits {#limits_elasticfilesystem .title}
---------------------------------

  Resource                           Default Limit
  ---------------------------------- ----------------------------------
  Total throughput per file system   3 GB/s for all connected clients

For information about additional documented limits, see [Amazon EFS Limits](http://docs.aws.amazon.com/efs/latest/ug//limits.html){.ulink} in the [*Amazon Elastic File System User Guide*]{.emphasis}.

Elastic Load Balancing Limits {#limits_elastic_load_balancer .title}
-----------------------------

Elastic Load Balancing supports two types of load balancers: Application load balancers and Classic load balancers.

[]{#d0e15256}
**Application Load Balancers**

  Resource                                                       Default Limit
  -------------------------------------------------------------- -------------------
  Load balancers per region                                      20 [†]{.guilabel}
  Target groups per region                                       50
  Listeners per load balancer                                    10
  Targets per load balancer                                      1000
  Subnets per Availability Zone per load balancer                1
  Security groups per load balancer                              5
  Rules per load balancer (not counting default rules)           10
  Number of times a target can be registered per load balancer   100
  Load balancers per target group                                1
  Targets per target group                                       1000

\
[]{#d0e15321}
**Classic Load Balancers**

  Resource                                          Default Limit
  ------------------------------------------------- -------------------
  Load balancers per region                         20 [†]{.guilabel}
  Listeners per load balancer                       100
  Security groups per load balancer                 5
  Subnets per Availability Zone per load balancer   1

\
[†]{.guilabel} This limit includes both your Application load balancers and your Classic load balancers. This limit can be increased upon request.

Amazon Elastic Transcoder Limits {#limits_elastictranscoder .title}
--------------------------------

  ---------------------------------------------------------------------------------------------------------
  Resource                                                           Default Limit
  ------------------------------------------------------------------ --------------------------------------
  Pipelines per region                                               4

  User-defined presets                                               50

  Maximum number of jobs processed simultaneously by each pipeline   US East (N. Virginia) Region – 20
                                                                     
                                                                     US West (N. California) Region – 12
                                                                     
                                                                     US West (Oregon) Region – 20
                                                                     
                                                                     Asia Pacific (Singapore) Region – 12
                                                                     
                                                                     Asia Pacific (Sydney) Region – 12
                                                                     
                                                                     Asia Pacific (Tokyo) Region – 12
                                                                     
                                                                     EU (Ireland) Region – 20
  ---------------------------------------------------------------------------------------------------------

It may take up to two weeks to process requests for a limit increase.

For information about additional documented limits, see [Amazon Elastic Transcoder](http://docs.aws.amazon.com/elastictranscoder/latest/developerguide/limits.html){.ulink} limits in the [*Amazon Elastic Transcoder Developer Guide*]{.emphasis}.

Amazon ElastiCache Limits {#limits_elasticache .title}
-------------------------

  Resource                                 Default Limit   Description
  ---------------------------------------- --------------- --------------------------------------------------------------------------------------------------------------------------------
  Nodes per region                         50              The maximum number of nodes across all clusters in a region.
  Nodes per cluster (Memcached)            20              The maximum number of nodes in an individual Memcached cluster.
  Nodes per cluster (Redis)                1               The maximum number of nodes in an individual Redis cluster.
  Clusters per replication group (Redis)   6               The maximum number of clusters in a Redis replication group. One is the read/write primary. All others are read only replicas.
  Parameter groups per region              20              The maximum number of parameters groups you can create in a region.
  Security groups per region               50              The maximum number of security groups you can create in a region.
  Subnet groups per region                 50              The maximum number of subnet groups you can create in a region.
  Subnets per subnet group                 20              The maximum number of subnets you can define for a subnet group.

These limits are global limits per customer account. If you need to exceed these limits, make your request using the [ElastiCache Node request form](http://aws.amazon.com/contact-us/elasticache-node-limit-request/){.ulink}.

Amazon Elasticsearch Service Limits {#limits_es .title}
-----------------------------------

  Resource                                    Default Limit
  ------------------------------------------- ---------------
  Number of Amazon ES instances per cluster   20

Amazon GameLift Limits {#limits_gamelift .title}
----------------------

  ------------------------------------------------------------------------------------------
  Resource                           Default Limit
  ---------------------------------- -------------------------------------------------------
  Aliases                            20

  Fleets                             20

  Builds                             1000

  Total size of builds               100 GB

  Log upload size per game session   200 MB

  On-demand instances                Limits vary depending on instance type;
                                     20 instances per account, regardless of instance type

  Server processes per instance      1 with GameLift SDK v2.x
                                     
                                     50 with GameLift SDK v3.x and up

  Player sessions per game session   200
  ------------------------------------------------------------------------------------------

For information about additional documented limits, see [Scaling Amazon Elastic Compute Cloud (Amazon EC2) Instances](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html){.ulink} in the [*Amazon GameLift Developer Guide*]{.emphasis}.

AWS Identity and Access Management (IAM) Limits {#limits_iam .title}
-----------------------------------------------

  Resource              Default Limit
  --------------------- ---------------
  Groups per account    100
  Instance profiles     100
  Roles                 250
  Server certificates   20
  Users                 5000

For information about additional documented limits, see [Limitations on IAM Entities and Objects](http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html){.ulink} in the [*IAM User Guide*]{.emphasis}.

AWS Import/Export Limits {#limits-import-export .title}
------------------------

### AWS Snowball (Snowball) {#limits_snowball .title}

  Resource   Default Limit   Comments
  ---------- --------------- ----------------------------------------------------------
  Snowball   1               If you need to increase this limit, contact AWS Support.

Amazon Inspector Limits {#limits_inspector .title}
-----------------------

  Resource               Default Limit
  ---------------------- ---------------
  Running agents         500
  Assessment runs        50,000
  Assessment templates   500
  Assessment targets     50

For more information, see the [Amazon Inspector User Guide](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_introduction.html){.ulink}.

AWS IoT Limits {#limits_iot .title}
--------------

The following limits apply to the message broker:

[]{#d0e15707}
  ------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Topic length limit                                     The topic passed to the message broker when publishing a message cannot exceed 256 bytes encoded in UTF-8.

  Restricted topic prefix                                Topics beginning with '\$' are considered reserved and are not supported for publishing and subscribing except when working with the Thing Shadows service.

  Maximum number of slashes in topic and topic filter    A topic provided while publishing a message or a topic filter provided while subscribing can have no more than eight forward slashes (/).

  Client ID size limit                                   128 bytes encoded in UTF-8.

  Restricted client ID prefix                            '\$' is reserved for internally generated client IDs.

  Message size limit                                     The payload for every publish message is limited to 128 KB. The AWS IoT service will reject messages larger than this size.

  Throughput per connection                              AWS IoT limits the ingress and egress rate on each client connection to 512 KB/s. Data sent or received at a higher rate will be throttled to this throughput.

  Maximum subscriptions per subscribe call               A single subscribe call is limited to request a maximum of eight subscriptions.

  Subscriptions per session                              The message broker limits each client session to subscribe to up to 50 subscriptions. A subscribe request that pushes the total number of subscriptions past 50 will result in the connection being disconnected.

  Connection inactivity (keep-alive) limits              By default, an MQTT client connection is disconnected after 30 minutes of inactivity. When the client sends a PUBLISH, SUBSCRIBE, PING, or PUBACK message, the inactivity timer is reset.
                                                         
                                                         A client can request a shorter keep-alive interval by specifying a keep-alive value between 5-1,200 seconds in the MQTT CONNECT message sent to the server. If a keep-alive value is specified, the server will disconnect the client if it does not receive a PUBLISH, SUBSCRIBE, PINGREQ, or PUBACK message within a period 1.5 times the requested interval. The keep-alive timer starts after the sender sends a CONNACK.
                                                         
                                                         If a client sends a keep-alive value of zero, the default keep-alive behavior will remain in place.
                                                         
                                                         If a client request a keep-alive shorter than 5 seconds, the server will treat the client as though it requested a keep-alive interval of 5 seconds.
                                                         
                                                         The keep-alive timer begins immediately after the server returns a CONNACK to the client. There may be a brief delay between the client's sending of a CONNECT message and the start of keep-alive behavior.

  Maximum inbound unacknowledged messages                The message broker allows 100 in-flight unacknowledged messages (limit is across all messages requiring ACK). When this limit is reached, no new messages will be accepted until an ACK is returned by the server.

  Maximum outbound unacknowledged messages               The message broker only allows 100 in-flight unacknowledged messages (limit is across all messages requiring ACK). When this limit is reached, no new messages will be sent to the client until the client acknowledges the in-flight messages.

  Maximum retry interval for delivering QoS 1 messages   If a connected client is unable to receive an ACK on a QoS 1 message for one hour, the message broker will drop the message. The client may be unable to receive the message if it has 100 in-flight messages, it is being throttled due to large payloads, or other errors.

  WebSocket connection duration                          WebSocket connections are limited to 24 hours. If the limit is exceeded, the WebSocket connection will automatically be closed when an attempt is made to send a message by the client or server. If you need to maintain an active WebSocket connection for longer than 5 minutes, simply close and re-open the WebSocket connection from the client side before the 5 minutes elapses.
  ------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\
The following limits apply to thing shadows:

[]{#d0e15817}
  ------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Maximum size of a JSON state document                  The maximum size of a JSON state document is 8 KB.

  Maximum number of JSON objects per AWS account         There is no limit on the number of JSON objects per AWS account.

  Shadow lifetime                                        A thing shadow is deleted by AWS IoT if it has not been updated or retrieved in more than 1 year.

  Maximum number of in-flight, unacknowledged messages   The Thing Shadows service supports up to 10 in-flight unacknowledged messages. When this limit is reached, all new shadow requests will be rejected with a 429 error code.

  Maximum depth of JSON device state documents           The maximum number of levels in the "desired" or "reported" section of the JSON device state document is 5. For example:
                                                         ``` {.programlisting}
                                                         "desired": {
                                                             "one": {
                                                                 "two": {
                                                                     "three": {
                                                                         "four": {
                                                                             "five":{
                                                                             }
                                                                          }
                                                                      }
                                                                 }
                                                             }
                                                         }
                                                         ```
  ------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\
The following limits apply to security and identity:

-   You can attach up to 10 policies to an AWS IoT certificate.

-   You can keep up to 5 versions of a named policy.

-   Policy document size is limited to 2048 characters (excluding white space).

### Throttling Limits {#throttling-limits .title}

The following table lists the throttling limits for AWS IoT API:

[]{#d0e15867}
  API                         Transaction per Second
  --------------------------- ------------------------
  AcceptCertificateTransfer   10
  AttachThingPrincipal        15
  CancelCertificateTransfer   10
  CreateCertificateFromCsr    15
  CreatePolicy                10
  CreatePolicyVersion         10
  CreateThing                 15
  DeleteCertificate           10
  DeleteCACertificate         10
  DeletePolicy                10
  DeletePolicyVersion         10
  DeleteThing                 10
  DescribeCertificate         10
  DescribeCACertificate       10
  DescribeThing               10
  DetachThingPrincipal        10
  DetachPrincipalPolicy       15
  DeleteRegistrationCode      10
  GetPolicy                   10
  GetPolicyVersion            15
  GetRegistrationCode         10
  ListCertificates            10
  ListCertificatesByCA        10
  ListPolicies                10
  ListPolicyVersions          10
  ListPrincipalPolicies       15
  ListPrincipalThings         10
  ListThings                  10
  ListThingPrincipals         10
  RegisterCertificate         10
  RegisterCACertificate       10
  RejectCertificateTransfer   10
  SetDefaultPolicyVersion     10
  TransferCertificate         10
  UpdateCertificate           10
  UpdateCACertificate         10
  UpdateThing                 10

\

### AWS IoT Rules Engine Limits {#rules-limits .title}

The following limit applies to the AWS IoT rules engine

-   There is a limit of 1000 rules per AWS account.

AWS Key Management Service (AWS KMS) Limits {#limits_kms .title}
-------------------------------------------

  Resource                               Default Limit
  -------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Customer Master Keys (CMKs)            1000
  Aliases                                1100
  Grants per CMK                         2500
  Grants for a given principal per CMK   30
  Requests per second                    Varies by API operation; see [Limits](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html){.ulink} in the [*AWS Key Management Service Developer Guide*]{.emphasis}.

All limits in the preceding table apply per region and per AWS account.

For information about additional documented limits, see [Limits](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html){.ulink} in the [*AWS Key Management Service Developer Guide*]{.emphasis}.

Amazon Kinesis Firehose Limits {#limits-akf .title}
------------------------------

  ---------------------------------------------------------
  Resource                      Default Limit
  ----------------------------- ---------------------------
  Delivery streams per region   20

  Delivery stream capacity †    2,000 transactions/second
                                
                                5,000 records/second
                                
                                5 MB/second
  ---------------------------------------------------------

† The three capacity limits scale proportionally. For example, if you increase the throughput limit to 10MB/second, the other limits increase to 4,000 transactions/second and 10,000 records/second.

For information about additional documented limits, see [Amazon Kinesis Firehose Limits](http://docs.aws.amazon.com/firehose/latest/dev/limits.html){.ulink} in the [*Amazon Kinesis Firehose Developer Guide*]{.emphasis}.

Amazon Kinesis Streams Limits {#limits-aks .title}
-----------------------------

  -------------------------------------------------------
  Resource            Default Limit
  ------------------- -----------------------------------
  Shards per region   US East (N. Virginia) Region – 50
                      
                      US West (Oregon) Region – 50
                      
                      EU (Ireland) Region – 50
                      
                      All other supported regions – 25
  -------------------------------------------------------

For information about additional documented limits, see [Amazon Kinesis Streams Limits](http://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html){.ulink} in the [*Amazon Kinesis Streams Developer Guide*]{.emphasis}.

AWS Lambda Limits {#limits_lambda .title}
-----------------

[]{#d0e16216}
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

  Resource                                   Default Limit
  ------------------------------------------ ---------------
  Clusters                                   40
  Cluster parameter groups                   50
  DB Instances                               40
  Event subscriptions                        20
  Manual snapshots                           50
  Manual cluster snapshots                   50
  Option groups                              20
  Parameter groups                           50
  Read replicas per master                   5
  Reserved instances (purchased per month)   40
  Rules per security group                   20
  Security groups                            25
  Security groups (VPC)                      5
  Subnet groups                              20
  Subnets per subnet group                   20
  Tags per resource                          50
  Total storage for all DB instances         100 TB

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
  Portfolios                 25 per account
  Users, groups, and roles   25 per portfolio
  Products                   25 per portfolio, 25 total per account
  Product versions           50 per product
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

  Resource                                          Default Limit
  ------------------------------------------------- ---------------
  Topics per AWS account                            100,000
  Account Spend Threshold for SMS per AWS Account   10,000 USD

Amazon Simple Queue Service (Amazon SQS) {#limits_sqs .title}
----------------------------------------

For information about additional documented limits, see [Limits, Restrictions](http://aws.amazon.com/sqs/faqs/#Limits,_Restrictions){.ulink} in the Amazon SQS FAQs and [Amazon SQS Limits](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-limits.html){.ulink} in the [*Amazon Simple Queue Service Developer Guide*]{.emphasis}.

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

AWS Storage Gateway Limits {#limits_storage_gateway .title}
--------------------------

                                                                     Gateway-Cached Volumes   Gateway-Stored Volumes   Gateway–Virtual Tape Libraries
  ------------------------------------------------------------------ ------------------------ ------------------------ --------------------------------
  Maximum size of a volume                                           32 TiB                   16 TiB                   –
  Maximum number of volumes for a gateway                            32                       32                       –
  Total size of all volumes for a gateway                            1,024 TiB                512 TiB                  –
  Minimum size of a virtual tape                                     –                        –                        100 GiB
  Maximum size of a virtual tape                                     –                        –                        2.5 TiB
  Maximum number of virtual tapes for a virtual tape library (VTL)   –                        –                        1,500
  Total size of all tapes in a virtual tape library (VTL)            –                        –                        1 PiB
  Maximum number of virtual tapes for a virtual tape shelf (VTS)     –                        –                        No limit
  Total size of all tapes in a virtual tape shelf (VTS)              –                        –                        No limit

Note

If you create a snapshot from a cached volume that is more than 16 TiB in size, you cannot restore it to an Amazon Elastic Block Store (Amazon EBS) volume; however, it can be restored to a Storage Gateway volume. For more information, see [Restoring a Snapshot to an Amazon EBS Volume](http://docs.aws.amazon.com/storagegateway/latest/userguide/RestoringSnapshotEBS.html.html){.ulink}

The following table lists limits for configuration and performance.

                                                                Gateway-Cached Volumes   Gateway-Stored Volumes   Gateway–Virtual Tape Libraries
  ------------------------------------------------------------- ------------------------ ------------------------ --------------------------------
  Maximum size of a cache storage                               16 TiB                   –                        16 TiB
  Total maximum size of all cache storage for a gateway         16 TiB                   –                        16 TiB
  Maximum size of an upload buffer disk                         2 TiB                    2 TiB                    2 TiB
  Total maximum size of all upload buffer disks for a gateway   2 TiB                    2 TiB                    2 TiB
  Maximum upload rate                                           120 MB/s                 120 MB/s                 120 MB/s
  Maximum download rate                                         20 MB/s                  20 MB/s                  20 MB/s

Note

The maximum upload rate was achieved by using 100 percent sequential write operations and 256 KB I/Os. Depending on your I/O mix and network conditions, the actual rate might be lower.

Amazon Virtual Private Cloud (Amazon VPC) Limits {#limits_vpc .title}
------------------------------------------------

  Resource                                                                           Default limit        Comments
  ---------------------------------------------------------------------------------- -------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
  Inbound or outbound rules per security group                                       50                   You can have 50 inbound and 50 outbound rules per security group (giving a total of 100 combined inbound and outbound rules). If you need to increase or decrease this limit, you can contact AWS Support — a limit change applies to both inbound and outbound rules. However, the multiple of the limit for inbound or outbound rules per security group and the limit for security groups per network interface cannot exceed 250. For example, if you want to increase the limit to 100, we decrease your number of security groups per network interface to 2.
  Security groups per network interface                                              5                    If you need to increase or decrease this limit, you can contact AWS Support. The maximum is 16. The multiple of the limit for security groups per network interface and the limit for rules per security group cannot exceed 250. For example, if you want 10 security groups per network interface, we decrease your number of rules per security group to 25.
  Network interfaces per instance                                                    -                    This limit varies by instance type. For more information, see [Private IP Addresses Per ENI Per Instance Type](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI){.ulink}.
  Network interfaces per region                                                      350                  This limit is the greater of either the default limit (350) or your On-Demand instance limit multiplied by 5. The default limit for On-Demand instances is 20. If your On-Demand instance limit is below 70, the default limit of 350 applies. You can increase the number of network interfaces per region by contacting AWS Support, or by increasing your On-Demand instance limit.
  Network ACLs per VPC                                                               200                  You can associate one network ACL to one or more subnets in a VPC. This limit is not the same as the number of rules per network ACL.
  Rules per network ACL                                                              20                   This is the one-way limit for a single network ACL, where the limit for ingress rules is 20, and the limit for egress rules is 20. This limit can be increased upon request up to a maximum if 40; however, network performance may be impacted due to the increased workload to process the additional rules.
  Active VPC peering connections per VPC                                             50                   If you need to increase this limit, contact AWS Support . The maximum limit is 125 peering connections per VPC. The number of entries per route table should be increased accordingly; however, network performance may be impacted.
  Outstanding VPC peering connection requests                                        25                   This is the limit for the number of outstanding VPC peering connection requests that you've requested from your account. If you need to increase this limit, contact AWS Support.
  Expiry time for an unaccepted VPC peering connection request                       1 week (168 hours)   If you need to increase this limit, contact AWS Support.
  VPC endpoints per region                                                           20                   If you need to increase this limit, contact AWS Support. The maximum limit is 255 endpoints per VPC, regardless of your endpoint limit per region.
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

![](/web/20160826010603im_/http://docs.aws.amazon.com/general/latest/gr/images/expanderarrow.png)
[Document Conventions](/web/20160826010603/http://docs.aws.amazon.com/general/latest/gr/docconventions.html)

[« Previous](signature-version-2.html){.awstoc}[Next »](aws-ip-ranges.html){.awstoc}

© 2016, Amazon Web Services, Inc. or its affiliates. All rights reserved.
