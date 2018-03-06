::: {#main-content}
::: {#main-col-body}
+-----------------------------------------------------------------------+
| ::: {.breadcrumb}                                                     |
| [AWS Documentation](http://aws.amazon.com/documentation) Â» [General  |
| Reference](index.html) Â» [AWS Service Limits]{.breadcrumb}           |
| :::                                                                   |
+-----------------------------------------------------------------------+

AWS Service Limits {#aws_service_limits .topictitle}
==================

The following tables provide the default limits for AWS services for an AWS account. Unless otherwise noted, each limit is region-specific. Many services contain limits that cannot be changed. For more information about the limits for a specific service, see the documentation for that service.

[AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/) offers a Service Limits check (in the Performance category) that displays your usage and limits for some aspects of some services. For more information, see [Service Limits Check Questions](https://aws.amazon.com/premiumsupport/ta-faqs/#service-limits-check-questions) in the Trusted Advisor FAQs.

You can take the following steps to request an increase for limits. These increases are not granted immediately, so it may take a couple of days for your increase to become effective.

**To request a limit increase**

1.  Open the [AWS Support Center](https://console.aws.amazon.com/support/home#/) page, sign in if necessary, and choose **Create Case**.

2.  For **Regarding**, choose **Service Limit Increase**.

3.  Complete **Limit Type**, **Use Case Description**, and **Contact method**. If this request is urgent, choose **Phone** as the method of contact instead of **Web**.

4.  Choose **Submit**.

::: {#inline-topiclist .highlights}
**Default Limits**

-   [Amazon API Gateway Limits](#limits_apigateway)
-   [Application Auto Scaling Limits](#limits_as-app)
-   [AWS Application Discovery Service Limits](#limits_appdiscserve)
-   [Amazon AppStream 2.0 Limits](#limits_appstream2)
-   [AWS AppSync Limits](#limits_appsync)
-   [Amazon Athena Limits](#amazon-athena-limits)
-   [AWS Auto Scaling Limits](#limits_aws_autoscaling)
-   [Auto Scaling Limits](#limits_autoscaling)
-   [AWS Batch Limits](#limits_batch)
-   [AWS Certificate Manager (ACM) Limits](#limits_acm)
-   [AWS Cloud9 Limits](#limits_cloud9)
-   [AWS CloudFormation Limits](#limits_cloudformation)
-   [Amazon CloudFront Limits](#limits_cloudfront)
-   [AWS CloudHSM Limits](#limits-cloudhsm)
-   [AWS CloudHSM Classic Limits](#limits-cloudhsm-classic)
-   [Amazon CloudSearch Limits](#limits_cloudsearch)
-   [AWS CloudTrail Limits](#limits_cloudtrail)
-   [Amazon CloudWatch Limits](#limits_cloudwatch)
-   [Amazon CloudWatch Events Limits](#limits_cloudwatch_events)
-   [Amazon CloudWatch Logs Limits](#limits_cloudwatch_logs)
-   [AWS CodeBuild Limits](#limits_codebuild)
-   [AWS CodeCommit Limits](#limits_codecommit)
-   [AWS CodeDeploy Limits](#limits_codedeploy)
-   [AWS CodePipeline Limits](#limits_codepipeline)
-   [Amazon Cognito User Pools Limits](#limits_cognito_user_pools)
-   [Amazon Cognito Federated Identities Limits](#limits_cognito_federated_identities)
-   [Amazon Cognito Sync Limits](#limits_cognito_sync)
-   [AWS Config Limits](#limits_config)
-   [Amazon Comprehend Limits](#limits_amazon_comprehend)
-   [Amazon Connect Limits](#limits_amazon_connect)
-   [AWS Data Pipeline Limits](#limits_datapipeline)
-   [AWS Database Migration Service Limits](#limits_dms)
-   [AWS Device Farm Limits](#limits_devicefarm)
-   [AWS Direct Connect Limits](#limits_directconnect)
-   [AWS Directory Service Limits](#limits_ds)
-   [Amazon DynamoDB Limits](#limits_dynamodb)
-   [AWS Elastic Beanstalk Limits](#limits_elastic_beanstalk)
-   [Amazon Elastic Block Store (Amazon EBS) Limits](#limits_ebs)
-   [Amazon Elastic Compute Cloud (Amazon EC2) Limits](#limits_ec2)
-   [Amazon Elastic Container Registry (Amazon ECR) Limits](#limits_ecr)
-   [Amazon Elastic Container Service (Amazon ECS) Limits](#limits_ecs)
-   [Amazon Elastic File System Limits](#limits_elasticfilesystem)
-   [Elastic Load Balancing Limits](#limits_elastic_load_balancer)
-   [Amazon Elastic Transcoder Limits](#limits_elastictranscoder)
-   [Amazon ElastiCache Limits](#limits_elasticache)
-   [Amazon Elasticsearch Service Limits](#limits_es)
-   [Amazon GameLift Limits](#limits_gamelift)
-   [Amazon Glacier Limits](#limits_glacier)
-   [AWS Glue Limits](#limits_glue)
-   [AWS Greengrass Limits](#limits_greengrass)
-   [Amazon GuardDuty Limits](#limits_guardduty)
-   [AWS Identity and Access Management (IAM) Limits](#limits_iam)
-   [AWS Import/Export Limits](#limits-import-export)
-   [Amazon Inspector Limits](#limits_inspector)
-   [AWS IoT Limits](#limits_iot)
-   [AWS Key Management Service (AWS KMS) Limits](#limits_kms)
-   [Amazon Kinesis Data Firehose Limits](#limits-akf)
-   [Amazon Kinesis Data Streams Limits](#limits-aks)
-   [Amazon Kinesis Data Analytics Limits](#limits-aka)
-   [Amazon Kinesis Video Streams Limits](#limits-akv)
-   [AWS Lambda Limits](#limits_lambda)
-   [Amazon Lightsail Limits](#limits_lightsail)
-   [Amazon Machine Learning (Amazon ML) Limits](#limits_machinelearning)
-   [AWS Elemental MediaConvert Limits](#limits_mediaconvert)
-   [AWS Elemental MediaLive Limits](#limits_medialive)
-   [AWS Elemental MediaPackage Limits](#limits_mediapackage)
-   [AWS Elemental MediaStore Limits](#limits_mediastore)
-   [AWS Elemental MediaTailor Limits](#limits_mediatailor)
-   [Amazon MQ Limits](#limits_amazon-mq)
-   [Amazon Neptune Limits](#limits_neptune)
-   [AWS OpsWorks for Chef Automate and AWS OpsWorks for Puppet Enterprise Limits](#limits_opworks)
-   [AWS OpsWorks Stacks Limits](#aws-opsworks-stacks-limits)
-   [AWS Organizations Limits](#aws-organizations-limits)
-   [Amazon Pinpoint Limits](#limits_pinpoint)
-   [Amazon Polly Limits](#limits_polly)
-   [Amazon Redshift Limits](#limits_redshift)
-   [Amazon Rekognition Limits](#limits_rekognition)
-   [Amazon Relational Database Service (Amazon RDS) Limits](#limits_rds)
-   [AWS Resource Groups Limits](#limits_resgrps)
-   [Amazon RouteÂ 53 Limits](#limits_route53)
-   [Amazon SageMaker Limits](#limits_sagemaker)
-   [AWS Server Migration Service Limits](#limits_server_migration)
-   [AWS Serverless Application Repository Limits](#limits_serverlessrepo)
-   [AWS Service Catalog Limits](#limits_servicecatalog)
-   [AWS Shield Advanced Limits](#limits_shield)
-   [Amazon Simple Email Service (Amazon SES) Limits](#limits_ses_quota)
-   [Amazon Simple Notification Service (Amazon SNS) Limits](#limits_sns)
-   [Amazon Simple Queue Service (Amazon SQS)](#limits_sqs)
-   [Amazon Simple Storage Service (Amazon S3) Limits](#limits_s3)
-   [Amazon Simple Workflow Service (Amazon SWF) Limits](#limits_swf)
-   [Amazon SimpleDB Limits](#limits_simpledb)
-   [AWS Step Functions Limits](#limits-step-functions)
-   [AWS Storage Gateway Limits](#limits-storage-gateway)
-   [AWS Systems Manager Limits](#limits_ssm)
-   [Amazon Virtual Private Cloud (Amazon VPC) Limits](#limits_vpc)
-   [Amazon VPC DNS Limits](#limits-vpc-dns)
-   [AWS WAF Limits](#limits_waf)
-   [Amazon WorkMail Limits](#limits_workmail)
-   [Amazon WorkSpaces Limits](#limits_workspaces)
-   [AWS X-Ray Limits](#limits_xray)
:::

Amazon API Gateway Limits {#limits_apigateway}
-------------------------

The following limits apply to configuring and running an API in Amazon API Gateway and can be increased upon request to optimize performances of a deployed API in Amazon API Gateway.

::: {.table}

::: {.table-contents}
  Resource or Operation                        Default Limit
  -------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Throttle rate per account per region         10000 request per second (rps) with an additional burst capacity provided by the [token bucket algorithm](https://en.wikipedia.org/wiki/Token_bucket), using a maximum bucket capacity of 5000 requests.
  APIs (or RestApis) per account per region    60
  API keys per account per region              500
  Custom authorizers per API                   10
  Client certificates per account per region   60
  Documentation parts per API                  2000
  Resources per API                            300
  Stages per API                               10
  Usage plans per account per region           300
  Usage plans per API key                      10
  VPC links per account per region             5
:::
:::

All of the per API limits can only be increased on specific APIs.

For more information about these limits, see [Limits in Amazon API Gateway](http://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html) in the *API Gateway Developer Guide*.

Application Auto Scaling Limits {#limits_as-app}
-------------------------------

::: {.table}
::: {.table-contents}
  Resource                               Default Limit
  -------------------------------------- ---------------
  Scalable targets                       500
  Scaling policies per scalable target   50
  Step adjustments per scaling policy    20
:::
:::

AWS Application Discovery Service Limits {#limits_appdiscserve}
----------------------------------------

::: {.table}

::: {.table-contents}
  Resource                                               Default Limit
  ------------------------------------------------------ ---------------
  Inactive agents heartbeating but not collecting data   10,000
  Active agents sending data to the service              250
  Total collected data for all agents, per day           10 GB
  Data storage duration before being purged              90 days
:::
:::

Amazon AppStream 2.0 Limits {#limits_appstream2}
---------------------------

::: {.table}
**Default Limits Per Region Per Account**

::: {.table-contents}
  Resource              Default Limit
  --------------------- ---------------
  Stacks                5
  Fleets                5
  Streaming instances   5 **\***
  Images                5
  Image builders        5 **â€ **
  Users                 5
:::
:::

**\*** This is the total limit across all instance families. Certain instance families have additional limits. For the Graphics Desktop and Graphics Pro instance families, the default limit is 0. For the Graphics Design instance family, the default limit is 2.

**â€ ** This is the total limit across all instance families. Certain instance families have additional limits. For the Graphics Desktop and Graphics Pro instance families, the default limit is 0. For the Graphics Design instance family, the default limit is 1.

AWS AppSync Limits {#limits_appsync}
------------------

::: {.table}

::: {.table-contents}
  Resource                                         Default Limit
  ------------------------------------------------ ---------------
  Maximum number of APIs per region                5 per account
  Maximum number of API keys                       10 per API
  Maximum schema document size                     5 MB
  Maximum GraphQL query execution time             30 seconds
  Maximum request/response mapping template size   64 KB
:::
:::

Amazon Athena Limits
--------------------

::: {.table}

::: {.table-contents}
  Resource                       Default Limit
  ------------------------------ ---------------
  Number of concurrent queries   5
  Query timeout                  30 minutes
:::
:::

For information about limits for databases, tables, and partitions, see [AWS Glue Limits](aws_service_limits.html#limits_glue).

AWS Auto Scaling Limits {#limits_aws_autoscaling}
-----------------------

::: {.table}
::: {.table-contents}
  Resource                                                 Default Limit
  -------------------------------------------------------- ---------------
  Scaling plans                                            100
  Target tracking configurations per scaling instruction   10
  Target tracking configurations per scaling plan          500
:::
:::

Auto Scaling Limits {#limits_autoscaling}
-------------------

::: {.table}

::: {.table-contents}
  Resource                                   Default Limit
  ------------------------------------------ ---------------
  Launch configurations per region           200
  Auto Scaling groups per region             200
  Scaling policies per Auto Scaling group    50
  Scheduled actions per Auto Scaling group   125
  Lifecycle hooks per Auto Scaling group     50
  SNS topics per Auto Scaling group          10
  Load balancers per Auto Scaling group      50
  Target groups per Auto Scaling group       50
  Step adjustments per scaling policy        20
:::
:::

For more information about these limits, see [Amazon EC2 Auto Scaling Limits](http://docs.aws.amazon.com/autoscaling/latest/userguide/as-account-limits.html) in the *Amazon EC2 Auto Scaling User Guide*.

AWS Batch Limits {#limits_batch}
----------------

::: {.table}

::: {.table-contents}
  Item                                                   Default Limit
  ------------------------------------------------------ ---------------
  Maximum number of job queues                           20
  Maximum number of compute environments per job queue   3
:::
:::

For more information about these limits, see [Service Limits](http://docs.aws.amazon.com/batch/latest/userguide/service_limits.html) in the *AWS Batch User Guide*.

AWS Certificate Manager (ACM) Limits {#limits_acm}
------------------------------------

::: {.table}

::: {.table-contents}
  Item                                                  Default Limit
  ----------------------------------------------------- ---------------
  Number of ACM-provided certificates                   100
  Number of imported certificates                       100
  Number of domain names per ACM-provided certificate   10
:::
:::

For more information about these limits, see [Limits](http://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html) in the *AWS Certificate Manager User Guide*.

AWS Cloud9 Limits {#limits_cloud9}
-----------------

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Item                              | Default Limit                     |
+===================================+===================================+
| Maximum number of AWS Cloud9 EC2  | ::: {.itemizedlist}               |
| development environments          | -   20 per IAM user               |
|                                   |                                   |
|                                   | -   100 per AWS account           |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
| Maximum number of SSH             | ::: {.itemizedlist}               |
| environments                      | -   10 per IAM user               |
|                                   |                                   |
|                                   | -   100 per AWS account           |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
| Maximum number of members in an   | 8                                 |
| environment                       |                                   |
+-----------------------------------+-----------------------------------+
| Maximum number of environments    | 10 total per IAM user, regardless |
| open at the same time             | of environment type (EC2 or SSH)  |
+-----------------------------------+-----------------------------------+
:::
:::

For more information about these limits, see [Limits](https://docs.aws.amazon.com/cloud9/latest/user-guide/limits.html) in the *AWS Cloud9 User Guide*.

AWS CloudFormation Limits {#limits_cloudformation}
-------------------------

::: {.table}

::: {.table-contents}
  Resource                        Default Limit
  ------------------------------- ---------------
  Stacks                          200
  Stack sets                      20
  Stack instances per stack set   500
:::
:::

For more information about these limits, see [AWS CloudFormation Limits](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the *AWS CloudFormation User Guide*.

Amazon CloudFront Limits {#limits_cloudfront}
------------------------

::: {.table}
**General Limits**

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Data transfer rate per            | 40 Gbps                           |
| distribution                      |                                   |
+-----------------------------------+-----------------------------------+
| Requests per second per           | 100,000                           |
| distribution                      |                                   |
+-----------------------------------+-----------------------------------+
| Web distributions per account     | 200                               |
+-----------------------------------+-----------------------------------+
| RTMP distributions per account    | 100                               |
+-----------------------------------+-----------------------------------+
| Alternate domain names (CNAMEs)   | 100                               |
| per distribution                  |                                   |
+-----------------------------------+-----------------------------------+
| Origins per distribution          | 25                                |
+-----------------------------------+-----------------------------------+
| Cache behaviors per distribution  | 25                                |
+-----------------------------------+-----------------------------------+
| Whitelisted headers per cache     | 10                                |
| behavior                          |                                   |
+-----------------------------------+-----------------------------------+
| Whitelisted cookies per cache     | 10                                |
| behavior                          |                                   |
+-----------------------------------+-----------------------------------+
| SSL certificates per account when | 2                                 |
| serving HTTPS requests using      |                                   |
| dedicated IP addresses (no limit  |                                   |
| when serving HTTPS requests using |                                   |
| SNI)                              |                                   |
+-----------------------------------+-----------------------------------+
| Custom headers that you can have  | 10 nameâ€"value pairs             |
| Amazon CloudFront forward to the  |                                   |
| origin                            |                                   |
+-----------------------------------+-----------------------------------+
| Whitelisted query strings per     | For more information, see         |
| cache behavior                    | [Configuring CloudFront to Cache  |
|                                   | Based on Query String             |
|                                   | Parameters](http://docs.aws.amazo |
|                                   | n.com/AmazonCloudFront/latest/Dev |
|                                   | eloperGuide/QueryStringParameters |
|                                   | .html)                            |
|                                   | in the *Amazon CloudFront         |
|                                   | Developer Guide*.                 |
+-----------------------------------+-----------------------------------+
| Response timeout per origin       | For more information, see         |
|                                   | [Response                         |
|                                   | Timeout](http://docs.aws.amazon.c |
|                                   | om/AmazonCloudFront/latest/Develo |
|                                   | perGuide/RequestAndResponseBehavi |
|                                   | orCustomOrigin.html#request-custo |
|                                   | m-request-timeout)                |
|                                   | in the *Amazon CloudFront         |
|                                   | Developer Guide*.                 |
+-----------------------------------+-----------------------------------+
:::
:::

::: {.table}
**Lambda@Edge Limits**

::: {.table-contents}
  Resource                                                         Default Limit
  ---------------------------------------------------------------- ---------------
  Distributions per AWS account that you can create triggers for   25
  Triggers per distribution                                        25
  Requests per second                                              10,000
  Concurrent executions                                            1,000
:::
:::

For more information about these limits, see [Limits](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) in the *Amazon CloudFront Developer Guide*.

AWS CloudHSM Limits {#limits-cloudhsm}
-------------------

::: {.table}
::: {.table-contents}
  Resource   Default Limit
  ---------- ---------------
  Clusters   4
  HSMs       6
:::
:::

For more information about these limits, see [Limits](http://docs.aws.amazon.com/cloudhsm/latest/userguide/limits.html) in the *AWS CloudHSM User Guide*.

AWS CloudHSM Classic Limits {#limits-cloudhsm-classic}
---------------------------

::: {.table}
::: {.table-contents}
  Resource                             Default Limit
  ------------------------------------ ---------------
  HSM appliances                       3
  High-availability partition groups   20
:::
:::

For more information about these limits, see [Limits](http://docs.aws.amazon.com/cloudhsm/classic/userguide/limits.html) in the *AWS CloudHSM Classic User Guide*.

Amazon CloudSearch Limits {#limits_cloudsearch}
-------------------------

::: {.table}

::: {.table-contents}
  Resource           Default Limit
  ------------------ ---------------
  Partitions         10
  Search instances   50
:::
:::

For more information about these limits, see [Understanding Amazon CloudSearch Limits](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/limits.html) in the *Amazon CloudSearch Developer Guide*.

AWS CloudTrail Limits {#limits_cloudtrail}
---------------------

CloudTrail has no increaseable limits. For more information, see [Limits in AWS CloudTrail](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html).

Amazon CloudWatch Limits {#limits_cloudwatch}
------------------------

::: {.table}

::: {.table-contents}
+-----------------------+-----------------------+-----------------------+
| Resource              | Default Limit         | Comments              |
+=======================+=======================+=======================+
| Alarms                | 10 per month per      | For the 5000 per      |
|                       | customer for free.    | region per account    |
|                       | 5000 per region per   | limit, you can        |
|                       | account.              | [request a limit      |
|                       |                       | increase](https://con |
|                       |                       | sole.aws.amazon.com/s |
|                       |                       | upport/home#/case/cre |
|                       |                       | ate?issueType=service |
|                       |                       | -limit-increase&limit |
|                       |                       | Type=service-code-ama |
|                       |                       | zon-cloudwatch).      |
+-----------------------+-----------------------+-----------------------+
| [DescribeAlarms](http | 9 transactions per    | The maximum number of |
| ://docs.aws.amazon.co | second (TPS)          | operation requests    |
| m/AmazonCloudWatch/la |                       | you can make per      |
| test/APIReference/API |                       | second without being  |
| _DescribeAlarms.html) |                       | throttled.            |
|                       |                       |                       |
|                       |                       | You can [request a    |
|                       |                       | limit                 |
|                       |                       | increase](https://con |
|                       |                       | sole.aws.amazon.com/s |
|                       |                       | upport/home#/case/cre |
|                       |                       | ate?issueType=service |
|                       |                       | -limit-increase&limit |
|                       |                       | Type=service-code-ama |
|                       |                       | zon-cloudwatch).      |
+-----------------------+-----------------------+-----------------------+
| [GetMetricStatistics] | 400 transactions per  | The maximum number of |
| (http://docs.aws.amaz | second (TPS)          | operation requests    |
| on.com/AmazonCloudWat |                       | you can make per      |
| ch/latest/APIReferenc |                       | second without being  |
| e/API_GetMetricStatis |                       | throttled.            |
| tics.html)            |                       |                       |
|                       |                       | You can [request a    |
|                       |                       | limit                 |
|                       |                       | increase](https://con |
|                       |                       | sole.aws.amazon.com/s |
|                       |                       | upport/home#/case/cre |
|                       |                       | ate?issueType=service |
|                       |                       | -limit-increase&limit |
|                       |                       | Type=service-code-ama |
|                       |                       | zon-cloudwatch).      |
+-----------------------+-----------------------+-----------------------+
| [ListMetrics](http:// | 25 transactions per   | The maximum number of |
| docs.aws.amazon.com/A | second (TPS)          | operation requests    |
| mazonCloudWatch/lates |                       | you can make per      |
| t/APIReference/API_Li |                       | second without being  |
| stMetrics.html)       |                       | throttled.            |
|                       |                       |                       |
|                       |                       | You can [request a    |
|                       |                       | limit                 |
|                       |                       | increase](https://con |
|                       |                       | sole.aws.amazon.com/s |
|                       |                       | upport/home#/case/cre |
|                       |                       | ate?issueType=service |
|                       |                       | -limit-increase&limit |
|                       |                       | Type=service-code-ama |
|                       |                       | zon-cloudwatch).      |
+-----------------------+-----------------------+-----------------------+
| [PutMetricAlarm](http | 3 transactions per    | The maximum number of |
| ://docs.aws.amazon.co | second (TPS)          | operation requests    |
| m/AmazonCloudWatch/la |                       | you can make per      |
| test/APIReference/API |                       | second without being  |
| _PutMetricAlarm.html) |                       | throttled.            |
|                       |                       |                       |
|                       |                       | You can [request a    |
|                       |                       | limit                 |
|                       |                       | increase](https://con |
|                       |                       | sole.aws.amazon.com/s |
|                       |                       | upport/home#/case/cre |
|                       |                       | ate?issueType=service |
|                       |                       | -limit-increase&limit |
|                       |                       | Type=service-code-ama |
|                       |                       | zon-cloudwatch).      |
+-----------------------+-----------------------+-----------------------+
| [PutMetricData](http: | 150 transactions per  | The maximum number of |
| //docs.aws.amazon.com | second (TPS)          | operation requests    |
| /AmazonCloudWatch/lat |                       | you can make per      |
| est/APIReference/API_ |                       | second without being  |
| PutMetricData.html)   |                       | throttled.            |
|                       |                       |                       |
|                       |                       | You can [request a    |
|                       |                       | limit                 |
|                       |                       | increase](https://con |
|                       |                       | sole.aws.amazon.com/s |
|                       |                       | upport/home#/case/cre |
|                       |                       | ate?issueType=service |
|                       |                       | -limit-increase&limit |
|                       |                       | Type=service-code-ama |
|                       |                       | zon-cloudwatch).      |
+-----------------------+-----------------------+-----------------------+
:::
:::

For more information about these and other CloudWatch limits, see [CloudWatch Limits](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_limits.html) in the *Amazon CloudWatch User Guide*.

Amazon CloudWatch Events Limits {#limits_cloudwatch_events}
-------------------------------

::: {.table}

::: {.table-contents}
+-----------------------+-----------------------+-----------------------+
| Resource              | Default Limit         | Comments              |
+=======================+=======================+=======================+
| Invocations           | 750 per second (after | You can [request a    |
|                       | 750 invocations, the  | limit                 |
|                       | invocations are       | increase](https://con |
|                       | throttled; that is,   | sole.aws.amazon.com/s |
|                       | they still happen but | upport/home#/case/cre |
|                       | they are delayed). If | ate?issueType=service |
|                       | the invocation of a   | -limit-increase&limit |
|                       | target fails due to a | Type=service-code-clo |
|                       | problem with the      | udwatch-events).      |
|                       | target service,       |                       |
|                       | account throttling,   |                       |
|                       | etc., new attempts    |                       |
|                       | are made for up to 24 |                       |
|                       | hours for a specific  |                       |
|                       | invocation.           |                       |
+-----------------------+-----------------------+-----------------------+
| Rules                 | 100 per region per    | You can [request a    |
|                       | account               | limit                 |
|                       |                       | increase](https://con |
|                       |                       | sole.aws.amazon.com/s |
|                       |                       | upport/home#/case/cre |
|                       |                       | ate?issueType=service |
|                       |                       | -limit-increase&limit |
|                       |                       | Type=service-code-clo |
|                       |                       | udwatch-events).      |
|                       |                       |                       |
|                       |                       | Before requesting a   |
|                       |                       | limit increase,       |
|                       |                       | examine your rules.   |
|                       |                       | You may have multiple |
|                       |                       | rules each matching   |
|                       |                       | to very specific      |
|                       |                       | events. Consider      |
|                       |                       | broadening their      |
|                       |                       | scope by using fewer  |
|                       |                       | identifiers in your   |
|                       |                       | [Events and Event     |
|                       |                       | Patterns](http://docs |
|                       |                       | .aws.amazon.com/Amazo |
|                       |                       | nCloudWatch/latest/De |
|                       |                       | veloperGuide/CloudWat |
|                       |                       | chEventsandEventPatte |
|                       |                       | rns.html).            |
|                       |                       | In addition, a rule   |
|                       |                       | can invoke several    |
|                       |                       | targets each time it  |
|                       |                       | matches an event.     |
|                       |                       | Consider adding more  |
|                       |                       | targets to your       |
|                       |                       | rules.                |
+-----------------------+-----------------------+-----------------------+
| [PutEvents](http://do | 10 entries per        | You can [request a    |
| cs.aws.amazon.com/Ama | request and 400       | limit                 |
| zonCloudWatchEvents/l | requests per second.  | increase](https://con |
| atest/APIReference/AP | Each request can be   | sole.aws.amazon.com/s |
| I_PutEvents.html)     | up to 256 KB in size. | upport/home#/case/cre |
|                       |                       | ate?issueType=service |
|                       |                       | -limit-increase&limit |
|                       |                       | Type=service-code-clo |
|                       |                       | udwatch-events).      |
+-----------------------+-----------------------+-----------------------+
:::
:::

For more information about these and other CloudWatch Events limits, see [CloudWatch Events Limits](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/cloudwatch_limits_cwe.html) in the *Amazon CloudWatch Events User Guide*.

Amazon CloudWatch Logs Limits {#limits_cloudwatch_logs}
-----------------------------

::: {.table}

::: {.table-contents}
+-----------------------+-----------------------+-----------------------+
| Resource              | Default Limit         | Comments              |
+=======================+=======================+=======================+
| [CreateLogGroup](http | 5000 log              | If you exceed your    |
| ://docs.aws.amazon.co | groups/account/Region | log group limit, you  |
| m/AmazonCloudWatchLog |                       | get a                 |
| s/latest/APIReference |                       | `ResourceLimitExceede |
| /API_CreateLogGroup.h |                       | d`{.code}             |
| tml)                  |                       | exception.            |
|                       |                       |                       |
|                       |                       | You can [request a    |
|                       |                       | limit                 |
|                       |                       | increase](https://con |
|                       |                       | sole.aws.amazon.com/s |
|                       |                       | upport/home#/case/cre |
|                       |                       | ate?issueType=service |
|                       |                       | -limit-increase&limit |
|                       |                       | Type=service-code-clo |
|                       |                       | udwatch-logs).        |
+-----------------------+-----------------------+-----------------------+
| [DescribeLogStreams]( | 5 transactions per    | If you experience     |
| http://docs.aws.amazo | second                | frequent throttling,  |
| n.com/AmazonCloudWatc | (TPS)/account/Region  | you can [request a    |
| hLogs/latest/APIRefer |                       | limit                 |
| ence/API_DescribeLogS |                       | increase](https://con |
| treams.html)          |                       | sole.aws.amazon.com/s |
|                       |                       | upport/home#/case/cre |
|                       |                       | ate?issueType=service |
|                       |                       | -limit-increase&limit |
|                       |                       | Type=service-code-clo |
|                       |                       | udwatch-logs).        |
+-----------------------+-----------------------+-----------------------+
| [FilterLogEvents](htt | 5 transactions per    | This limit can be     |
| p://docs.aws.amazon.c | second                | changed only in       |
| om/AmazonCloudWatchLo | (TPS)/account/region  | special               |
| gs/latest/APIReferenc |                       | circumstances. If you |
| e/API_FilterLogEvents |                       | experience frequent   |
| .html)                |                       | throttling, contact   |
|                       |                       | AWS Support.          |
+-----------------------+-----------------------+-----------------------+
| [GetLogEvents](http:/ | 10 transactions per   | We recommend          |
| /docs.aws.amazon.com/ | second                | subscriptions if you  |
| AmazonCloudWatchLogs/ | (TPS)/account/Region  | are continuously      |
| latest/APIReference/A |                       | processing new data.  |
| PI_GetLogEvents.html) |                       | If you need           |
|                       |                       | historical data, we   |
|                       |                       | recommend exporting   |
|                       |                       | your data to Amazon   |
|                       |                       | S3. This limit can be |
|                       |                       | changed only in       |
|                       |                       | special               |
|                       |                       | circumstances. If you |
|                       |                       | experience frequent   |
|                       |                       | throttling, contact   |
|                       |                       | AWS Support.          |
+-----------------------+-----------------------+-----------------------+
| [PutLogEvents](http:/ | 1500 transactions per | You can [request a    |
| /docs.aws.amazon.com/ | second per account    | limit                 |
| AmazonCloudWatchLogs/ | per Region, except    | increase](https://con |
| latest/APIReference/A | for the following     | sole.aws.amazon.com/s |
| PI_PutLogEvents.html) | Regions where the     | upport/home#/case/cre |
|                       | limit is 800          | ate?issueType=service |
|                       | transactions per      | -limit-increase&limit |
|                       | second per account    | Type=service-code-clo |
|                       | per Region:           | udwatch-logs).        |
|                       | ap-south-1,           |                       |
|                       | ap-northeast-1,       | The maximum batch     |
|                       | ap-northeast-2,       | size of a             |
|                       | ap-southeast-1,       | PutLogEvents request  |
|                       | ap-southeast-2,       | is 1MB.               |
|                       | eu-central-1,         |                       |
|                       | eu-west-2, sa-east-1, | 5 requests per second |
|                       | us-east-2, and        | per log stream.       |
|                       | us-west-1.            | Additional requests   |
|                       |                       | are throttled. This   |
|                       |                       | limit cannot be       |
|                       |                       | changed.              |
+-----------------------+-----------------------+-----------------------+
:::
:::

For more information about these and other CloudWatch Logs limits, see [CloudWatch Logs Limits](http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.html) in the *Amazon CloudWatch Logs User Guide*.

AWS CodeBuild Limits {#limits_codebuild}
--------------------

::: {.table}

::: {.table-contents}
  Resource                                         Default Limit
  ------------------------------------------------ ---------------
  Maximum number of build projects                 1,000
  Maximum number of concurrent running builds \*   20
:::
:::

\* Limits for the maximum number of concurrent running builds vary, depending on the compute type. For some compute types, the default is 20. To request a higher concurrent build limit or if you get a \"Cannot have more than X active builds for the account\" error, contact AWS support.

For more information about these limits, see [Limits for AWS CodeBuild](http://docs.aws.amazon.com/codebuild/latest/userguide/limits.html) in the *AWS CodeBuild User Guide*.

AWS CodeCommit Limits {#limits_codecommit}
---------------------

::: {.table}

::: {.table-contents}
  Resource                 Default Limit
  ------------------------ -----------------------
  Number of repositories   1,000 per AWS account
:::
:::

For more information about these limits, see [Limits in AWS CodeCommit](http://docs.aws.amazon.com/codecommit/latest/userguide/limits.html) in the *AWS CodeCommit User Guide*.

AWS CodeDeploy Limits {#limits_codedeploy}
---------------------

::: {.table}

::: {.table-contents}
  Resource                                                                           Default Limit
  ---------------------------------------------------------------------------------- ---------------
  Maximum number of applications associated with an AWS account in a single region   100
  Maximum number of concurrent deployments associated with an AWS account            10
  Maximum number of deployment groups associated with a single application           100
  Maximum number of instances in a single deployment                                 500
  Maximum number of event notification triggers in a deployment group                10
:::
:::

For more information about these limits, see [Limits in AWS CodeDeploy](http://docs.aws.amazon.com/codedeploy/latest/userguide/limits.html) in the *AWS CodeDeploy User Guide*.

AWS CodePipeline Limits {#limits_codepipeline}
-----------------------

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Maximum number of pipelines per   | US East (N. Virginia)             |
| region in an AWS account          | (us-east-1): 40                   |
|                                   |                                   |
|                                   | US West (Oregon) (us-west-2): 60  |
|                                   |                                   |
|                                   | EU (Ireland) (eu-west-1): 60      |
|                                   |                                   |
|                                   | All other supported regions: 20   |
+-----------------------------------+-----------------------------------+
| Number of stages in a pipeline    | Minimum of 2, maxiÂ­mum of 10     |
+-----------------------------------+-----------------------------------+
| Number of actions in a stage      | Minimum of 1, maxiÂ­mum of 20     |
+-----------------------------------+-----------------------------------+
| Maximum number of parallel        | Maximum of 5                      |
| actions in a stage                |                                   |
+-----------------------------------+-----------------------------------+
| Maximum number of sequential      | Maximum of 10                     |
| actions in a stage                |                                   |
+-----------------------------------+-----------------------------------+
| Number of custom actions per      | 50                                |
| region in an AWS account          |                                   |
+-----------------------------------+-----------------------------------+
| Maximum size of artifacts in a    | Artifacts stored in Amazon S3     |
| source stage                      | buckets: 2 GB                     |
|                                   |                                   |
|                                   | Artifacts stored in AWS           |
|                                   | CodeCommit or GitHub              |
|                                   | repositories: 1 GB                |
|                                   |                                   |
|                                   | Exception: If you are using       |
|                                   | Amazon EBS to deploy              |
|                                   | applications, the maximum         |
|                                   | artifact size is always 512 MB.   |
|                                   |                                   |
|                                   | Exception: If you are using AWS   |
|                                   | CloudFormation to deploy          |
|                                   | applications, the maximum         |
|                                   | artifact size is always 256 MB.   |
+-----------------------------------+-----------------------------------+
:::
:::

It may take up to two weeks to process requests for a limit increase.

For more information about these limits, see [Limits in AWS CodePipeline](http://docs.aws.amazon.com/codepipeline/latest/userguide/limits.html) in the *AWS CodePipeline User Guide*.

Amazon Cognito User Pools Limits {#limits_cognito_user_pools}
--------------------------------

::: {.table}

::: {.table-contents}
  Resource                                             Default Limit
  ---------------------------------------------------- ---------------
  Maximum number of apps per user pool                 25
  Maximum number of user pools per account             60
  Maximum number of user import jobs per user pool     50
  Maximum number of identity providers per user pool   25
  Maximum number of resource servers per user pool     20
  Maximum number of scopes per user pool               20
:::
:::

For information about additional documented limits, see [Limits in Amazon Cognito](http://docs.aws.amazon.com/cognito/latest/developerguide/limits.html) in the *Amazon Cognito Developer Guide*.

Amazon Cognito Federated Identities Limits {#limits_cognito_federated_identities}
------------------------------------------

::: {.table}

::: {.table-contents}
  Resource                                       Default Limit
  ---------------------------------------------- ---------------
  Maximum number of identity pools per account   60
:::
:::

For information about additional documented limits, see [Limits in Amazon Cognito](http://docs.aws.amazon.com/cognito/latest/developerguide/limits.html) in the *Amazon Cognito Developer Guide*.

Amazon Cognito Sync Limits {#limits_cognito_sync}
--------------------------

::: {.table}

::: {.table-contents}
  Resource                                  Default Limit
  ----------------------------------------- ---------------
  Maximum number of datasets per identity   20
  Maximum number of records per dataset     1024
  Maximum size of a single dataset          1 MB
:::
:::

For information about additional documented limits, see [Limits in Amazon Cognito](http://docs.aws.amazon.com/cognito/latest/developerguide/limits.html) in the *Amazon Cognito Developer Guide*.

AWS Config Limits {#limits_config}
-----------------

::: {.table}

::: {.table-contents}
+-----------------------+-----------------------+-----------------------+
| Resource              | Default Limit         | Notes                 |
+=======================+=======================+=======================+
| Number of AWS Config  | 50                    | You can [request a    |
| rules per region in   |                       | limit                 |
| your account          |                       | increase](https://con |
|                       |                       | sole.aws.amazon.com/s |
|                       |                       | upport/home#/case/cre |
|                       |                       | ate?issueType=service |
|                       |                       | -limit-increase&limit |
|                       |                       | Type=service-code-con |
|                       |                       | fig-service).         |
+-----------------------+-----------------------+-----------------------+
:::
:::

Amazon Comprehend Limits {#limits_amazon_comprehend}
------------------------

::: {.table}
::: {.table-contents}
  Resource                                                                                                             Default Limit
  -------------------------------------------------------------------------------------------------------------------- ---------------
  Transactions per second for synchronous APIs                                                                         20
  Transactions per second for the `StartTopicsDetectionJob`{.code} operation                                           1
  Transactions per second for the `DescribeTopicsDetectionJob`{.code} and `ListTopicDetectionJobs`{.code} operations   10
  Maximum concurrent jobs                                                                                              10
:::
:::

You can request an increase for any of the limits using the [Amazon Comprehend service limits increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-comprehend).

For information about additional documented limits, see [Guidelines and Limits](https://docs.aws.amazon.com/comprehend/latest/dg/guidelines-and-limits.html) in the *Amazon Comprehend Developer Guide*.

Amazon Connect Limits {#limits_amazon_connect}
---------------------

::: {.table}
::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Item                              | Default limit                     |
+===================================+===================================+
| Amazon Connect instances per      | 2                                 |
| account                           |                                   |
+-----------------------------------+-----------------------------------+
| Users per instance                | 500                               |
+-----------------------------------+-----------------------------------+
| Phone numbers per instance        | 10                                |
+-----------------------------------+-----------------------------------+
| Queues per instance               | 50                                |
+-----------------------------------+-----------------------------------+
| Queues per routing profile        | 50                                |
+-----------------------------------+-----------------------------------+
| Routing profiles per instance     | 100                               |
+-----------------------------------+-----------------------------------+
| Hours of operation per instance   | 100                               |
+-----------------------------------+-----------------------------------+
| Quick connects per instance       | 100                               |
+-----------------------------------+-----------------------------------+
| Prompts per instance              | 500                               |
+-----------------------------------+-----------------------------------+
| Agent status per instance         | 50                                |
+-----------------------------------+-----------------------------------+
| Security profiles per instance    | 100                               |
+-----------------------------------+-----------------------------------+
| Contact flows per instance        | 100                               |
+-----------------------------------+-----------------------------------+
| Groups per level                  | 50                                |
+-----------------------------------+-----------------------------------+
| Reports per instance              | 500                               |
+-----------------------------------+-----------------------------------+
| Scheduled reports per instance    | 50                                |
+-----------------------------------+-----------------------------------+
| Concurrent active calls per       | 10                                |
| instance                          |                                   |
+-----------------------------------+-----------------------------------+
:::
:::

These are the default limits for new Amazon Connect instances. You can create two instances per AWS account to start, but if you need more instances it is easy to request an increase. You can also request an increase for any of the limits using the [Amazon Connect service limits increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-connect). You need to be signed in to your AWS account to access the form.

AWS Data Pipeline Limits {#limits_datapipeline}
------------------------

::: {.table}

::: {.table-contents}
  Attribute                                                Limit                            Adjustable
  -------------------------------------------------------- -------------------------------- ------------
  Number of pipelines                                      100                              Yes
  Number of objects per pipeline                           100                              Yes
  Number of active instances per object                    5                                Yes
  Number of fields per object                              50                               No
  Number of UTF8 bytes per field name or identifier        256                              No
  Number of UTF8 bytes per field                           10,240                           No
  Number of UTF8 bytes per object                          15,360 (including field names)   No
  Rate of creation of an instance from an object           1 per 5 minutes                  No
  Retries of a pipeline activity                           5 per task                       No
  Minimum delay between retry attempts                     2 minutes                        No
  Minimum scheduling interval                              15 minutes                       No
  Maximum number of roll-ups into a single object          32                               No
  Maximum number of EC2 instances per Ec2Resource object   1                                No
:::
:::

For additional limits, see [AWS Data Pipeline Limits](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-limits.html) in the *AWS Data Pipeline Developer Guide*.

AWS Database Migration Service Limits {#limits_dms}
-------------------------------------

::: {.table}

::: {.table-contents}
  Resource                               Default Limit
  -------------------------------------- ---------------
  Replication instances                  20
  Total amount of storage                6 TB
  Replication subnet groups              20
  Subnets per replication subnet group   20
  Endpoints                              100
  Tasks                                  200
  Endpoints per instance                 20
:::
:::

AWS Device Farm Limits {#limits_devicefarm}
----------------------

::: {.table}

::: {.table-contents}
+-----------------------+-----------------------+-----------------------+
| Resource              | Default Limit         | Comments              |
+=======================+=======================+=======================+
| App file size you can | 4 GB                  |                       |
| upload                |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Number of devices     | 5                     | This limit can be     |
| that AWS Device Farm  |                       | increased to 100 upon |
| can test during a run |                       | request.              |
+-----------------------+-----------------------+-----------------------+
| Number of devices you | None                  |                       |
| can include in a test |                       |                       |
| run                   |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Number of runs you    | None                  |                       |
| can schedule          |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Duration of a remote  | 60 minutes            |                       |
| access session        |                       |                       |
+-----------------------+-----------------------+-----------------------+
:::
:::

AWS Direct Connect Limits {#limits_directconnect}
-------------------------

For more information about these limits, see [AWS Direct Connect Limits](http://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html#directconnect_limits) in the *AWS Direct Connect User Guide*.

AWS Directory Service Limits {#limits_ds}
----------------------------

::: {.table}

::: {.table-contents}
  Resource                                                                                Default Limit
  --------------------------------------------------------------------------------------- --------------------
  AD Connector directories                                                                10
  AWS Directory Service for Microsoft Active Directory (Enterprise Edition) directories   10
  Simple AD directories                                                                   10
  Manual snapshots                                                                        5 per Microsoft AD
  Manual snapshots                                                                        5 per Simple AD
:::
:::

For information about additional documented limits, including limits on Amazon Cloud Directory, see [AWS Directory Service Limits](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/limits.html) in the *AWS Directory Service Admin Guide*.

Amazon DynamoDB Limits {#limits_dynamodb}
----------------------

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| US East (N. Virginia) Region:     | 40,000 read capacity units and    |
|                                   | 40,000 write capacity units       |
| Maximum capacity units per table  |                                   |
| or global secondary index         |                                   |
+-----------------------------------+-----------------------------------+
| US East (N. Virginia) Region:     | 80,000 read capacity units and    |
|                                   | 80,000 write capacity units       |
| Maximum capacity units per        |                                   |
| account                           |                                   |
+-----------------------------------+-----------------------------------+
| All other regions:                | 10,000 read capacity units and    |
|                                   | 10,000 write capacity units       |
| Maximum capacity units per table  |                                   |
| or global secondary index         |                                   |
+-----------------------------------+-----------------------------------+
| All other regions:                | 20,000 read capacity units and    |
|                                   | 20,000 write capacity units       |
| Maximum capacity units per        |                                   |
| account                           |                                   |
+-----------------------------------+-----------------------------------+
| Maximum number of tables          | 256                               |
+-----------------------------------+-----------------------------------+
:::
:::

For more information about these limits, see [Limits in Amazon DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide*.

AWS Elastic Beanstalk Limits {#limits_elastic_beanstalk}
----------------------------

::: {.table}

::: {.table-contents}
  Resource               Default Limit
  ---------------------- ---------------
  Applications           75
  Application Versions   1000
  Environments           200
:::
:::

Amazon Elastic Block Store (Amazon EBS) Limits {#limits_ebs}
----------------------------------------------

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Number of EBS snapshots           | 10,000                            |
+-----------------------------------+-----------------------------------+
| Concurrent snapshots allowed for  | 5 for `io1`{.code}, `gp2`{.code}, |
| a single volume                   | `magnetic`{.code}; 1 for          |
|                                   | `st1`{.code}, `sc1`{.code}        |
+-----------------------------------+-----------------------------------+
| Concurrent snapshot copy requests | 5                                 |
| to a single destination region    |                                   |
+-----------------------------------+-----------------------------------+
| Total volume storage of General   | 100 TiB                           |
| Purpose SSD (`gp2`{.code})        |                                   |
| volumes                           |                                   |
+-----------------------------------+-----------------------------------+
| Total volume storage of           | 100 TiB                           |
| Provisioned IOPS SSD              |                                   |
| (`io1`{.code}) volumes            |                                   |
+-----------------------------------+-----------------------------------+
| Total volume storage of           | 300 TiB                           |
| Throughput Optimized HDD          |                                   |
| (`st1`{.code})                    |                                   |
+-----------------------------------+-----------------------------------+
| Total volume storage of Cold HDD  | 300 TiB                           |
| (`sc1`{.code})                    |                                   |
+-----------------------------------+-----------------------------------+
| Total volume storage of Magnetic  | 20 TiB                            |
| volumes (`standard`{.code})       |                                   |
+-----------------------------------+-----------------------------------+
| Total provisioned IOPS            | 200,000                           |
+-----------------------------------+-----------------------------------+
:::
:::

For more information about these limits, see [Amazon EC2 Service Limits](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) in the *Amazon EC2 User Guide for Linux Instances*.

Amazon Elastic Compute Cloud (Amazon EC2) Limits {#limits_ec2}
------------------------------------------------

::: {.table}

::: {.table-contents}
  Resource                                                               Default Limit
  ---------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Elastic IP addresses for EC2-Classic                                   5
  Security groups for EC2-Classic per instance                           500
  Rules per security group for EC2-Classic                               100
  Key pairs                                                              5,000
  Throttle on the emails that can be sent from your Amazon EC2 account   Throttle applied
  On-Demand Instances                                                    Limits vary depending on instance type. For more information, see [How many instances can I run in Amazon EC2](https://aws.amazon.com/ec2/faqs/#How_many_instances_can_I_run_in_Amazon_EC2).
  Spot Instances                                                         Limits vary depending on instance type, region, and account. For more information, see [Spot Instance Limits](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-limits.html).
  Reserved Instances                                                     20 Reserved Instances per Availability Zone, per month, plus 20 regional Reserved Instances. For more information, see [Reserved Instance Limits](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html#ri-limits).
  Dedicated Hosts                                                        Up to two Dedicated Hosts per instance family, per region can be allocated.
  AMI Copies                                                             Destination regions are limited to 50 concurrent AMI copies at a time, with no more than 25 of those coming from a single source region.
  Launch Templates                                                       1,000 launch templates per region and 10,000 versions per launch template.
:::
:::

For information about related limits for EC2-VPC, see [Amazon Virtual Private Cloud (Amazon VPC) Limits](aws_service_limits.html#limits_vpc).

For information about viewing your current limits, see [Amazon EC2 Service Limits](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) in the *Amazon EC2 User Guide for Linux Instances*.

Amazon Elastic Container Registry (Amazon ECR) Limits {#limits_ecr}
-----------------------------------------------------

::: {.table}

::: {.table-contents}
  Resource                                     Default Limit
  -------------------------------------------- ---------------
  Maximum number of repositories per account   1,000
  Maximum number of images per repository      1,000
:::
:::

For information about additional documented limits, see [Amazon ECR Service Limits](http://docs.aws.amazon.com/AmazonECR/latest/userguide/service_limits.html) in the *Amazon Elastic Container Registry User Guide*.

Amazon Elastic Container Service (Amazon ECS) Limits {#limits_ecs}
----------------------------------------------------

::: {.table}

::: {.table-contents}
  Resource                                                                    Default Limit
  --------------------------------------------------------------------------- ---------------
  Number of clusters per region per account                                   1000
  Number of container instances per cluster                                   1000
  Number of services per cluster                                              500
  Number of tasks using the EC2 launch type per service (the desired count)   1000
  Number of tasks using the Fargate launch type, per region, per account      20
  Number of public IP addresses for tasks using the Fargate launch type       20
:::
:::

For information about additional documented limits, see [Amazon ECS Service Limits](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service_limits.html) in the *Amazon Elastic Container Service Developer Guide*.

Amazon Elastic File System Limits {#limits_elasticfilesystem}
---------------------------------

Following are the limits for Amazon EFS that can be increased by contacting AWS Support.

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Number of file systems per        | 10                                |
| customer account per AWS region   |                                   |
+-----------------------------------+-----------------------------------+
| Total throughput per file system  | US East (Ohio) Region â€" 3 GB/s  |
| for all connected clients         |                                   |
|                                   | US East (N. Virginia) Region â€"  |
|                                   | 3 GB/s                            |
|                                   |                                   |
|                                   | US West (Oregon) Region â€" 3     |
|                                   | GB/s                              |
|                                   |                                   |
|                                   | EU (Frankfurt) Region â€" 1 GB/s  |
|                                   |                                   |
|                                   | EU (Ireland) Region â€" 3 GB/s    |
|                                   |                                   |
|                                   | Asia Pacific (Sydney) Region â€"  |
|                                   | 3 GB/s                            |
+-----------------------------------+-----------------------------------+
:::
:::

For more information about these limits, see [Amazon EFS Limits](http://docs.aws.amazon.com/efs/latest/ug//limits.html) in the *Amazon Elastic File System User Guide*.

Elastic Load Balancing Limits {#limits_elastic_load_balancer}
-----------------------------

Elastic Load Balancing supports three types of load balancers: Application Load Balancers, Network Load Balancers, and Classic Load Balancers.

::: {.table}
**Application Load Balancers**

::: {.table-contents}
  Resource                                                             Default Limit
  -------------------------------------------------------------------- ---------------
  Load balancers per region                                            20 **â€ **
  Target groups per region                                             3000
  Listeners per load balancer                                          50
  Targets per load balancer                                            1000
  Subnets per Availability Zone per load balancer                      1
  Security groups per load balancer                                    5
  Rules per load balancer (not counting default rules)                 100
  Certificates per load balancer (not counting default certificates)   25
  Number of times a target can be registered per load balancer         100
  Load balancers per target group                                      1
  Targets per target group                                             1000
:::
:::

**â€ ** This limit includes both your Application Load Balancers and your Classic Load Balancers. This limit can be increased upon request.

::: {.table}
**Network Load Balancers**

::: {.table-contents}
  Resource                                          Default Limit
  ------------------------------------------------- ---------------
  Network Load Balancers per region                 20
  Target groups per region                          3000 **\***
  Listeners per load balancer                       50
  Subnets per Availability Zone per load balancer   1
  Targets per load balancer per Availability Zone   200
  Load balancers per target group                   1
:::
:::

**\*** This limit is shared by target groups for your Application Load Balancers and Network Load Balancers.

::: {.table}
**Classic Load Balancers**

::: {.table-contents}
  Resource                                          Default Limit
  ------------------------------------------------- ---------------
  Load balancers per region                         20 **â€ **
  Listeners per load balancer                       100
  Security groups per load balancer                 5
  Subnets per Availability Zone per load balancer   1
:::
:::

**â€ ** This limit includes both your Application Load Balancers and your Classic Load Balancers. This limit can be increased upon request.

Amazon Elastic Transcoder Limits {#limits_elastictranscoder}
--------------------------------

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Pipelines per region              | 4                                 |
+-----------------------------------+-----------------------------------+
| User-defined presets              | 50                                |
+-----------------------------------+-----------------------------------+
| Maximum number of jobs processed  | US East (N. Virginia) Region â€"  |
| simultaneously by each pipeline   | 20                                |
|                                   |                                   |
|                                   | US West (N. California) Region    |
|                                   | â€" 12                            |
|                                   |                                   |
|                                   | US West (Oregon) Region â€" 20    |
|                                   |                                   |
|                                   | Asia Pacific (Mumbai) Region â€"  |
|                                   | 12                                |
|                                   |                                   |
|                                   | Asia Pacific (Singapore) Region   |
|                                   | â€" 12                            |
|                                   |                                   |
|                                   | Asia Pacific (Sydney) Region â€"  |
|                                   | 12                                |
|                                   |                                   |
|                                   | Asia Pacific (Tokyo) Region â€"   |
|                                   | 12                                |
|                                   |                                   |
|                                   | EU (Ireland) Region â€" 20        |
+-----------------------------------+-----------------------------------+
:::
:::

It may take up to two weeks to process requests for a limit increase.

For more information about these limits, see [Amazon Elastic Transcoder](http://docs.aws.amazon.com/elastictranscoder/latest/developerguide/limits.html) limits in the *Amazon Elastic Transcoder Developer Guide*.

Amazon ElastiCache Limits {#limits_elasticache}
-------------------------

For information on ElastiCache terminology, see [ElastiCache Components and Features](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/WhatIs.Components.html).

::: {.table}

::: {.table-contents}
  Resource                                                  Default Limit Description
  ------------------------------------------------------- --------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  NodesÂ perÂ region                                                  100 The maximum number of nodes across all clusters in a region. This limit applies to both your reserved and nonreserved nodes within the given region. You can have up to 100 reserved nodes and 100 nonreserved nodes in the same region.
  NodesÂ perÂ clusterÂ (Memcached)                                     20 The maximum number of nodes in an individual Memcached cluster.
  NodesÂ perÂ shardÂ (Redis)                                            6 The maximum number of nodes in an individual Redis shard (node group). One node is the read/write Primary. All other nodes are read-only Replicas.
  ShardsÂ perÂ Cluster (RedisÂ clusterÂ modeÂ disabled)                 1 The maximum number of shards (node groups) in a Redis (cluster mode disabled) cluster.
  ShardsÂ perÂ Cluster (RedisÂ clusterÂ modeÂ enabled)                 15 The maximum number of shards (node groups) in a Redis (cluster mode enabled) cluster.
  ParameterÂ groups per region                                         20 The maximum number of parameters groups you can create in a region.
  SecurityÂ groups per region                                          50 The maximum number of security groups you can create in a region.
  SubnetÂ groups per region                                            50 The maximum number of subnet groups you can create in a region.
  Subnets per subnet group                                             20 The maximum number of subnets you can define for a subnet group.
:::
:::

These limits are global limits per customer account. To exceed these limits, make your request using the [ElastiCache Node request form](https://aws.amazon.com/contact-us/elasticache-node-limit-request/).

Amazon Elasticsearch Service Limits {#limits_es}
-----------------------------------

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Number of Amazon ES instances per | 20 (except for T2 instance types, |
| cluster                           | which have a maximum of 10).      |
|                                   |                                   |
|                                   | ::: {.aws-note}                   |
|                                   | Note                              |
|                                   |                                   |
|                                   | The default limit is 20 instances |
|                                   | per domain. To request an         |
|                                   | increase up to 100 instances per  |
|                                   | domain, create a case with the    |
|                                   | [AWS Support                      |
|                                   | Center](https://console.aws.amazo |
|                                   | n.com/support/home#/).            |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::
:::

Amazon GameLift Limits {#limits_gamelift}
----------------------

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Aliases                           | 20                                |
+-----------------------------------+-----------------------------------+
| Fleets                            | 20                                |
+-----------------------------------+-----------------------------------+
| Builds                            | 1000                              |
+-----------------------------------+-----------------------------------+
| Total size of builds              | 100 GB                            |
+-----------------------------------+-----------------------------------+
| Log upload size per game session  | 200 MB                            |
+-----------------------------------+-----------------------------------+
| On-demand instances               | Per instance type: limits vary.   |
|                                   |                                   |
|                                   | Per account: 20 instances max,    |
|                                   | regardless of instance type.      |
|                                   |                                   |
|                                   | For more information, see         |
|                                   | [Scaling Amazon Elastic Compute   |
|                                   | Cloud (Amazon EC2)                |
|                                   | Instances](http://docs.aws.amazon |
|                                   | .com/gamelift/latest/developergui |
|                                   | de/gamelift-ec2-instances.html)   |
|                                   | for Amazon GameLift.              |
+-----------------------------------+-----------------------------------+
| Server processes per instance     | GameLift SDK v2.x: 1              |
|                                   |                                   |
|                                   | GameLift SDK v3.x and up: 50      |
+-----------------------------------+-----------------------------------+
| Player sessions per game session  | 200                               |
+-----------------------------------+-----------------------------------+
| Matchmakers per account           | 100                               |
+-----------------------------------+-----------------------------------+
| VPC peering connections           | For limits on active and pending  |
|                                   | VPC peering connections, see      |
|                                   | [Amazon Virtual Private Cloud     |
|                                   | (Amazon VPC)                      |
|                                   | Limits](aws_service_limits.html#l |
|                                   | imits_vpc).                       |
|                                   |                                   |
|                                   | The expiry time for an Amazon     |
|                                   | GameLift VPC peering              |
|                                   | authorization is 24 hours.        |
+-----------------------------------+-----------------------------------+
:::
:::

Amazon Glacier Limits {#limits_glacier}
---------------------

::: {.table}
::: {.table-contents}
  Resource                               Default Limit
  -------------------------------------- ---------------
  Number of vaults per account           1000
  Number of provisioned capacity units   2
:::
:::

AWS Glue Limits {#limits_glue}
---------------

::: {.table}
::: {.table-contents}
  Resource                                                  Default Limit
  --------------------------------------------------------- ---------------
  Number of databases per account                           100
  Number of tables per database                             1000
  Number of partitions per table                            20,000
  Number of crawlers per account                            25
  Number of jobs per account                                25
  Number of triggers per account                            25
  Number of concurrent job runs per account                 30
  Number of concurrent job runs per job                     3
  Number of jobs per trigger                                10
  Number of development endpoints per account               2
  Maximum DPUs used by a development endpoint at one time   5
  Maximum DPUs used by a role at one time                   100
:::
:::

AWS Greengrass Limits {#limits_greengrass}
---------------------

### AWS Greengrass Cloud API Limits {#gg_cloud_limits}

::: {.table}

::: {.table-contents}
  Description                                                                                           Limit
  ----------------------------------------------------------------------------------------------------- ----------------------------------------
  Maximum number of AWS IoT devices in a group.                                                         200
  Maximum number of Lambda functions in a group.                                                        200
  Maximum number of resources per Lambda function.                                                      10
  Maximum number of resources per group.                                                                50
  Maximum number of transactions per second (TPS) on the AWS Greengrass API.                            30
  Maximum number of subscriptions per AWS Greengrass group.                                             1000
  Maximum number of subscriptions that specify `Cloud`{.code} as the source per AWS Greengrass group.   50
  Maximum length of a Core thing name.                                                                  124 bytes of UTF-8 encoded characters.
:::
:::

### AWS Greengrass core Limits {#gg_core_limits}

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Description                       | Limit                             |
+===================================+===================================+
| Maximum number of routing table   | 50 (matches AWS IoT subscription  |
| entries that specify \"Cloud\" as | limit)                            |
| the source.                       |                                   |
+-----------------------------------+-----------------------------------+
| Maximum size of messages sent by  | 128 KB (matches AWS IoT message   |
| an AWS IoT device.                | size limit)                       |
+-----------------------------------+-----------------------------------+
| Maximum message queue size in the | 2.5 MB                            |
| Greengrass core router.           |                                   |
+-----------------------------------+-----------------------------------+
| Maximum length of a topic string  | 256 bytes of UTF-8 encoded        |
|                                   | characters.                       |
+-----------------------------------+-----------------------------------+
| Maximum number of forward slashes | 7                                 |
| \'/\' in a topic or topic filter. |                                   |
+-----------------------------------+-----------------------------------+
| Minimum disk space needed to run  | 128 MB                            |
| the Greengrass core software      |                                   |
+-----------------------------------+-----------------------------------+
| Minimum RAM to run the Greengrass | 128 MB                            |
| core software                     |                                   |
+-----------------------------------+-----------------------------------+
| Automatic IP detection should not | ::: {.itemizedlist}               |
| be used when:                     | -   IP address changes are        |
|                                   |     frequent.                     |
|                                   |                                   |
|                                   | -   Interruption of the           |
|                                   |     Greengrass core service is    |
|                                   |     unacceptable.                 |
|                                   |                                   |
|                                   | -   The Greengrass core is        |
|                                   |     multi-homed or Greengrass     |
|                                   |     devices cannot reliably       |
|                                   |     determine which IP address to |
|                                   |     use.                          |
|                                   |                                   |
|                                   | -   Reporting of Greengrass core  |
|                                   |     IP addresses to the cloud may |
|                                   |     raise security concerns.      |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::
:::

The Greengrass core software provides a service to automatically detect the IP address(es) of your Greengrass core devices. It sends this information to the AWS Greengrass cloud service and allows AWS IoT devices to download the IP address of the Greengrass core they need to connect to. This feature should not be used in the following circumstances:

::: {.itemizedlist}
-   The IP address of a Greengrass core device changes frequently.

-   The Greengrass core device must always be available to AWS IoT devices in it\'s group.

-   The Greengrass core has multiple IP addresses and an AWS IoT device is unable to reliably determine which address to use.

-   Sending IP addresses to the cloud raises security concerns.
:::

Amazon GuardDuty Limits {#limits_guardduty}
-----------------------

::: {.table}

::: {.table-contents}
  Resource                           Default Limit
  ---------------------------------- ---------------
  Detectors                          1
  Trusted IP sets                    1
  Threat intel sets                  6
  GuardDuty member accounts          1000
  GuardDuty finding retention time   90 days
:::
:::

For more information, see the [Amazon GuardDuty User Guide](http://docs.aws.amazon.com/guardduty/latest/ug/).

AWS Identity and Access Management (IAM) Limits {#limits_iam}
-----------------------------------------------

::: {.table}
::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Customer managed policies in an   | 1500                              |
| AWS account                       |                                   |
+-----------------------------------+-----------------------------------+
| Groups in an AWS account          | 300                               |
+-----------------------------------+-----------------------------------+
| Roles in an AWS account           | 1000                              |
+-----------------------------------+-----------------------------------+
| Users in an AWS account           | 5000 (If you need to add a large  |
|                                   | number of users, consider using   |
|                                   | [temporary security               |
|                                   | credentials](http://docs.aws.amaz |
|                                   | on.com/IAM/latest/UserGuide/id_cr |
|                                   | edentials_temp.html).)            |
+-----------------------------------+-----------------------------------+
| Virtual MFA devices (assigned or  | Equal to the user quota for the   |
| unassigned) in an AWS account     | account                           |
+-----------------------------------+-----------------------------------+
| Instance profiles in an AWS       | 1000                              |
| account                           |                                   |
+-----------------------------------+-----------------------------------+
| Server certificates stored in an  | 20                                |
| AWS account                       |                                   |
+-----------------------------------+-----------------------------------+
:::
:::

For more information about these limits, see [Limitations on IAM Entities and Objects](http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html) in the *IAM User Guide*.

AWS Import/Export Limits {#limits-import-export}
------------------------

### AWS Snowball (Snowball) {#limits_snowball}

::: {.table}

::: {.table-contents}
+-----------------------+-----------------------+-----------------------+
| Resource              | Default Limit         | Comments              |
+=======================+=======================+=======================+
| Snowball              | 1                     | To increase this      |
|                       |                       | limit, contact AWS    |
|                       |                       | Support.              |
+-----------------------+-----------------------+-----------------------+
:::
:::

Amazon Inspector Limits {#limits_inspector}
-----------------------

::: {.table}

::: {.table-contents}
  Resource               Default Limit
  ---------------------- ---------------
  Running agents         500
  Assessment runs        50,000
  Assessment templates   500
  Assessment targets     50
:::
:::

For more information, see the [Amazon Inspector User Guide](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_introduction.html).

AWS IoT Limits {#limits_iot}
--------------

### Thing Limits

::: {.table}

::: {.table-contents}
  Resource                                                             Limit
  -------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------
  Thing name size                                                      128 bytes of UTF-8 encoded characters. This limit applies for both the thing registry and Thing Shadow services.
  Maximum number of thing attributes for a thing with a thing type     50
  Maximum number of thing attribute for a thing without a thing type   3
  Number of thing types that can be associated with a thing            1
  Maximum number of thing types in an AWS account                      Unlimited
:::
:::

### Message Broker Limits

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Client ID size                    | 128 bytes of UTF-8 encoded        |
|                                   | characters.                       |
+-----------------------------------+-----------------------------------+
| Connection inactivity (keep-alive | By default, an MQTT client        |
| interval)                         | connection is disconnected after  |
|                                   | 30 minutes of inactivity. When    |
|                                   | the client sends a PUBLISH,       |
|                                   | SUBSCRIBE, PING, or PUBACK        |
|                                   | message, the inactivity timer is  |
|                                   | reset.                            |
|                                   |                                   |
|                                   | A client can request a shorter    |
|                                   | keep-alive interval by specifying |
|                                   | a value between 5-1,200 seconds   |
|                                   | in the MQTT CONNECT message sent  |
|                                   | to the server. If a keep-alive    |
|                                   | value is specified, the server    |
|                                   | disconnects the client if it does |
|                                   | not receive a PUBLISH, SUBSCRIBE, |
|                                   | PINGREQ, or PUBACK message within |
|                                   | a period 1.5 times the requested  |
|                                   | interval. The keep-alive timer    |
|                                   | starts after the sender sends a   |
|                                   | CONNACK.                          |
|                                   |                                   |
|                                   | If a client sends a keep-alive    |
|                                   | value of zero, the default        |
|                                   | keep-alive behavior remains in    |
|                                   | place.                            |
|                                   |                                   |
|                                   | If a client requests a keep-alive |
|                                   | shorter than 5 seconds, the       |
|                                   | server treats the client as       |
|                                   | though it requested a keep-alive  |
|                                   | interval of 5 seconds.            |
|                                   |                                   |
|                                   | The keep-alive timer begins       |
|                                   | immediately after the server      |
|                                   | returns a CONNACK to the client.  |
|                                   | There might be a brief delay      |
|                                   | between the client\'s sending of  |
|                                   | a CONNECT message and the start   |
|                                   | of keep-alive behavior.           |
+-----------------------------------+-----------------------------------+
| Connect requests per second per   | AWS IoT limits an account to a    |
| account                           | maximum of 300 MQTT CONNECT       |
|                                   | requests per second.              |
+-----------------------------------+-----------------------------------+
| Connect requests per second per   | AWS IoT AWS IoT throttles         |
| client ID                         | connects from the same accountId  |
|                                   | and clientId to 1 connect         |
|                                   | operation per second.             |
+-----------------------------------+-----------------------------------+
| Maximum number of slashes in      | A topic provided while publishing |
| topic and topic filter            | a message or a topic filter       |
|                                   | provided while subscribing can    |
|                                   | have no more than 7 forward       |
|                                   | slashes (/).                      |
+-----------------------------------+-----------------------------------+
| Maximum inbound unacknowledged    | The message broker allows 100     |
| messages                          | in-progress unacknowledged        |
|                                   | messages per client. (This limit  |
|                                   | is applied across all messages    |
|                                   | that require ACK.) When this      |
|                                   | limit is reached, no new messages |
|                                   | are accepted from this client     |
|                                   | until an ACK is returned by the   |
|                                   | server.                           |
+-----------------------------------+-----------------------------------+
| Maximum outbound unacknowledged   | The message broker allows only    |
| messages                          | 100 in-progress unacknowledged    |
|                                   | messages per client. (This limit  |
|                                   | is applied across all messages    |
|                                   | that require ACK.) When this      |
|                                   | limit is reached, no new messages |
|                                   | are sent to the client until the  |
|                                   | client acknowledges the           |
|                                   | in-progress messages.             |
+-----------------------------------+-----------------------------------+
| Maximum retry interval for        | If a connected client is unable   |
| delivering QoS 1 messages         | to receive an ACK on a QoS 1      |
|                                   | message for one hour, the message |
|                                   | broker drops the message. The     |
|                                   | client might be unable to receive |
|                                   | the message if it has 100         |
|                                   | in-flight messages, it is being   |
|                                   | throttled due to large payloads,  |
|                                   | or other errors.                  |
+-----------------------------------+-----------------------------------+
| Maximum subscriptions per         | A single SUBSCRIBE call is        |
| subscribe call                    | limited to request a maximum of   |
|                                   | eight subscriptions.              |
+-----------------------------------+-----------------------------------+
| Message size                      | The payload for every PUBLISH     |
|                                   | message is limited to 128 KB. The |
|                                   | AWS IoT service rejects messages  |
|                                   | larger than this size.            |
+-----------------------------------+-----------------------------------+
| Publish requests per second per   | 9000 per second per account       |
| account                           | (inbound publish requests - max.  |
|                                   | 3000 per second, outbound publish |
|                                   | requests - max. 6000 per second). |
|                                   |                                   |
|                                   | Inbound publish requests count    |
|                                   | for all the messages that the     |
|                                   | message broker processes before   |
|                                   | routing the messages to the       |
|                                   | subscribed clients or the rules   |
|                                   | engine. For example, a single     |
|                                   | message published on              |
|                                   | `$aws/things/device`{.code}/shado |
|                                   | w/update                          |
|                                   | topic can result in publishing    |
|                                   | three additional messages to      |
|                                   | `$aws/things/device`{.code}/shado |
|                                   | w/update/accepted,                |
|                                   | `$aws/things/device`{.code}/shado |
|                                   | w/update/documents,               |
|                                   | `$aws/things/device`{.code}/shado |
|                                   | w/delta                           |
|                                   | topics. In this case, AWS IoT     |
|                                   | counts those as 4 inbound publish |
|                                   | requests towards this limit.      |
|                                   | However, a single message to an   |
|                                   | unreserved topic like             |
|                                   | `"a/b"`{.code} is counted only as |
|                                   | a single inbound publish request. |
|                                   |                                   |
|                                   | Outbound publish requests count   |
|                                   | for every message that resulted   |
|                                   | in matching a client\'s           |
|                                   | subscription or matching a rules  |
|                                   | engine subscription. For example, |
|                                   | two clients are subscribed to     |
|                                   | topic filter `'a/b'`{.code} and a |
|                                   | rule is subscribed to topic       |
|                                   | filter `'a/#'`{.code}. An inbound |
|                                   | publish request message on topic  |
|                                   | \'a/b\' results in a total of 3   |
|                                   | outbound publish requests.        |
|                                   |                                   |
|                                   | ::: {.aws-note}                   |
|                                   | Note                              |
|                                   |                                   |
|                                   | Inbound and outbound publish      |
|                                   | requests cannot be traded for     |
|                                   | each other, for example, if only  |
|                                   | 1,000 inbound publish requests    |
|                                   | per second are used, the maximum  |
|                                   | outbound publish requests per     |
|                                   | second remains 6,000.             |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
| Publish requests per second per   | AWS IoT limits each client        |
| connection                        | connection to 100 inbound publish |
|                                   | requests per second and 100       |
|                                   | outbound publish requests per     |
|                                   | second. Publish requests          |
|                                   | exceeding that limit will be      |
|                                   | discarded.                        |
+-----------------------------------+-----------------------------------+
| Restricted client ID prefix       | \'\$\' is reserved for internally |
|                                   | generated client IDs.             |
+-----------------------------------+-----------------------------------+
| Restricted topic prefix           | Topics beginning with \'\$\' are  |
|                                   | considered reserved and are not   |
|                                   | supported for publishing and      |
|                                   | subscribing except when working   |
|                                   | with the Thing Shadows service.   |
+-----------------------------------+-----------------------------------+
| Subscriptions per second per      | AWS IoT limits an account to a    |
| account                           | maximum of 500 subscriptions per  |
|                                   | second. For example, if there are |
|                                   | two MQTT SUBSCRIBE calls within a |
|                                   | second with 3 subscriptions       |
|                                   | (topic filters) each, AWS IoT     |
|                                   | counts those as 6 subscriptions   |
|                                   | towards this limit.               |
+-----------------------------------+-----------------------------------+
| Subscriptions per connection      | AWS IoT limits each client        |
|                                   | connection to subscribe to up to  |
|                                   | 50 subscriptions. A SUBSCRIBE     |
|                                   | request that pushes the total     |
|                                   | number of subscriptions past 50   |
|                                   | results in the connection being   |
|                                   | disconnected.                     |
+-----------------------------------+-----------------------------------+
| Throughput per connection         | AWS IoT limits the ingress and    |
|                                   | egress rate on each client        |
|                                   | connection to 512 KB/s. Data sent |
|                                   | or received at a higher rate is   |
|                                   | throttled to this throughput.     |
+-----------------------------------+-----------------------------------+
| Topic size                        | The topic passed to the message   |
|                                   | broker when publishing a message  |
|                                   | cannot exceed 256 bytes of UTF-8  |
|                                   | encoded characters.               |
+-----------------------------------+-----------------------------------+
| WebSocket connection duration     | WebSocket connections are limited |
|                                   | to 24 hours. If the limit is      |
|                                   | exceeded, the WebSocket           |
|                                   | connection is automatically       |
|                                   | closed when an attempt is made to |
|                                   | send a message by the client or   |
|                                   | server. To maintain an active     |
|                                   | WebSocket connection for longer   |
|                                   | than 24 hours, simply close and   |
|                                   | reopen the WebSocket connection   |
|                                   | from the client side before the   |
|                                   | time limit elapses.               |
|                                   |                                   |
|                                   | AWS IoT supports keep-alive       |
|                                   | values specified in MQTT CONNECT  |
|                                   | messages. When a client specifies |
|                                   | a keep-alive value, the client    |
|                                   | tells the server to disconnect    |
|                                   | the client and transmit any       |
|                                   | last-will message associated with |
|                                   | the MQTT session if the server    |
|                                   | does not receive a message        |
|                                   | (PUBLISH, SUBSCRIBE, PUBACK,      |
|                                   | PINGREQ) within 1.5 times the     |
|                                   | keep-alive period. AWS IoT        |
|                                   | supports keep-alive values        |
|                                   | between 5 seconds and 20 minutes. |
|                                   | If a client requests no           |
|                                   | keep-alive (that is, sets the     |
|                                   | field to 0 in the MQTT CONNECT    |
|                                   | message), the server sets the     |
|                                   | keep-alive value to 20 minutes,   |
|                                   | which corresponds to the maximum  |
|                                   | idle time supported by AWS IoT of |
|                                   | 30 minutes. Most MQTT clients     |
|                                   | (including the AWS SDK clients)   |
|                                   | support keep-alive values by      |
|                                   | sending a PINGREQ if the          |
|                                   | keep-alive period expires without |
|                                   | the transmission of any other     |
|                                   | message by the client.            |
+-----------------------------------+-----------------------------------+
:::
:::

### Device Shadow Limits

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Maximum depth of JSON device      | The maximum number of levels in   |
| state documents                   | the `desired`{.code} or           |
|                                   | `reported`{.code} section of the  |
|                                   | JSON device state document is 5.  |
|                                   | For example:                      |
|                                   |                                   |
|                                   | ``` {.programlisting}             |
|                                   | "desired": {                      |
|                                   |     "one": {                      |
|                                   |         "two": {                  |
|                                   |             "three": {            |
|                                   |                 "four": {         |
|                                   |                     "five":{      |
|                                   |                     }             |
|                                   |                  }                |
|                                   |              }                    |
|                                   |         }                         |
|                                   |     }                             |
|                                   | }                                 |
|                                   | ```                               |
+-----------------------------------+-----------------------------------+
| Maximum number of in-flight,      | The Thing Shadows service         |
| unacknowledged messages           | supports up to 10 in-flight       |
|                                   | unacknowledged messages. When     |
|                                   | this limit is reached, all new    |
|                                   | shadow requests is rejected with  |
|                                   | a 429 error code.                 |
+-----------------------------------+-----------------------------------+
| Maximum number of JSON objects    | There is no limit on the number   |
| per AWS account                   | of JSON objects per AWS account.  |
+-----------------------------------+-----------------------------------+
| Maximum size of a JSON state      | 8 KB.                             |
| document                          |                                   |
+-----------------------------------+-----------------------------------+
| Maximum size of a thing name      | 128 bytes of UTF-8 encoded        |
|                                   | characters.                       |
+-----------------------------------+-----------------------------------+
| Shadow lifetime                   | A thing shadow is deleted by AWS  |
|                                   | IoT up to six months after the    |
|                                   | creating account is deleted or    |
|                                   | per customer request. For         |
|                                   | operational purposes, AWS IoT     |
|                                   | service backups are kept for 6    |
|                                   | months                            |
+-----------------------------------+-----------------------------------+
:::
:::

### Security and Identity Limits {#security-limits}

::: {.table}

::: {.table-contents}
  -------------------------------------------------------------------------------------------------- -----------------------------------------
  Maximum number of CA certificates with the same subject field allowed per AWS account per region   10
  Maximum number of policies that can be attached to a certificate or Amazon Cognito identity        10
  Maximum number of named policy versions                                                            5
  Maximum policy document size                                                                       2048 characters (excluding white space)
  Maximum number of device certificates that can be registered per second                            15
  -------------------------------------------------------------------------------------------------- -----------------------------------------
:::
:::

### Throttling Limits

::: {.table}

::: {.table-contents}
  API                         Transaction per Second
  --------------------------- ------------------------
  AcceptCertificateTransfer   10
  AttachPrincipalPolicy       15
  AttachThingPrincipal        15
  CancelCertificateTransfer   10
  CreateCertificateFromCsr    15
  CreatePolicy                10
  CreatePolicyVersion         10
  CreateThing                 15
  CreateThingType             15
  DeleteCertificate           10
  DeleteCACertificate         10
  DeletePolicy                10
  DeletePolicyVersion         10
  DeleteThing                 15
  DeleteThingType             15
  DeprecateThingType          15
  DescribeCertificate         10
  DescribeCACertificate       10
  DescribeThing               10
  DescribeThingType           10
  DetachThingPrincipal        15
  DetachPrincipalPolicy       15
  DeleteRegistrationCode      10
  GetPolicy                   10
  GetPolicyVersion            15
  GetRegistrationCode         10
  ListCACertificates          10
  ListCertificates            10
  ListCertificatesByCA        10
  ListOutgoingCertificates    10
  ListPolicies                10
  ListPolicyPrincipals        10
  ListPolicyVersions          10
  ListPrincipalPolicies       15
  ListPrincipalThings         10
  ListThings                  10
  ListThingPrincipals         10
  ListThingTypes              10
  RegisterCertificate         10
  RegisterCACertificate       10
  RejectCertificateTransfer   10
  SetDefaultPolicyVersion     10
  TransferCertificate         10
  UpdateCertificate           10
  UpdateCACertificate         10
  UpdateThing                 10
  UpdateThingShadow           10
:::
:::

### AWS IoT Rules Engine Limits {#rules-limits}

::: {.table}

::: {.table-contents}
  ----------------------------------------- -------------------------------------------------------------------
  Maximum number of rules per AWS account   1000
  Actions per rule                          A maximum of 10 actions can be defined per rule.
  Rule size                                 Up to 256 KB of UTF-8 encoded characters (including white space).
  ----------------------------------------- -------------------------------------------------------------------
:::
:::

### AWS IoT Job Limits {#job-limits}

::: {.table}

::: {.table-contents}
+-----------------+-----------------+-----------------+-----------------+
| Resource        | Min             | Max             | Note            |
+=================+=================+=================+=================+
| `JobId`{.code}  | 1 character     | 64 characters   | The             |
|                 |                 |                 | `JobId`{.code}  |
|                 |                 |                 | length must not |
|                 |                 |                 | exceed 64       |
|                 |                 |                 | characters.     |
+-----------------+-----------------+-----------------+-----------------+
| `Document`{.cod | N/A             | 32768 bytes     | The maximum     |
| e}              |                 |                 | size of a       |
|                 |                 |                 | document that   |
|                 |                 |                 | can be sent to  |
|                 |                 |                 | an AWS IoT      |
|                 |                 |                 | device is 32    |
|                 |                 |                 | KB.             |
+-----------------+-----------------+-----------------+-----------------+
| `DocumentSource | N/A             | 1350 characters | The maximum job |
| `{.code}        |                 |                 | document source |
|                 |                 |                 | size is 1350    |
|                 |                 |                 | characters.     |
+-----------------+-----------------+-----------------+-----------------+
| `Description`{. | N/A             | 2028 characters | The maximum job |
| code}           |                 |                 | description     |
|                 |                 |                 | size is 2028    |
|                 |                 |                 | characters.     |
+-----------------+-----------------+-----------------+-----------------+
| `Targets`{.code | 1               | 100             | The number of   |
| }               |                 |                 | targets a job   |
|                 |                 |                 | can have.       |
+-----------------+-----------------+-----------------+-----------------+
| `ExpiresInSec`{ | 60 seconds      | 3600 seconds    | The lifetime of |
| .code}          |                 |                 | pre-signed URLs |
|                 |                 |                 | must be         |
|                 |                 |                 | configured      |
|                 |                 |                 | greater than 60 |
|                 |                 |                 | seconds and     |
|                 |                 |                 | less than 1     |
|                 |                 |                 | hour.           |
+-----------------+-----------------+-----------------+-----------------+
| `Comment`{.code | N/A             | 2028 characters | The maximum     |
| }               |                 |                 | comment size is |
|                 |                 |                 | 2028            |
|                 |                 |                 | characters.     |
+-----------------+-----------------+-----------------+-----------------+
| `MaxResults`{.c | 1               | 250             | The maximum     |
| ode}            |                 |                 | list result per |
|                 |                 |                 | page is 250.    |
+-----------------+-----------------+-----------------+-----------------+
| `MaximumJobExec | 1               | 1000            | Configures the  |
| utionsPerMinute |                 |                 | rollout speed   |
| `{.code}        |                 |                 | for a job.      |
+-----------------+-----------------+-----------------+-----------------+
| Active snapshot | 0               | 100             | The maximum     |
| jobs            |                 |                 | number of       |
|                 |                 |                 | active snapshot |
|                 |                 |                 | jobs is 100     |
|                 |                 |                 | (irrespective   |
|                 |                 |                 | of the number   |
|                 |                 |                 | of active       |
|                 |                 |                 | continuous      |
|                 |                 |                 | jobs).          |
+-----------------+-----------------+-----------------+-----------------+
| Active          | 0               | 100             | The maximum     |
| continuous jobs |                 |                 | number of       |
|                 |                 |                 | active          |
|                 |                 |                 | continuous jobs |
|                 |                 |                 | is 100          |
|                 |                 |                 | (irrespective   |
|                 |                 |                 | of the number   |
|                 |                 |                 | of active       |
|                 |                 |                 | snapshot jobs). |
+-----------------+-----------------+-----------------+-----------------+
| Job document    | 0               | 10              | Up to 10        |
| variable        |                 |                 | variables       |
| substitution    |                 |                 | substitutions,  |
|                 |                 |                 | including the   |
|                 |                 |                 | presign URL,    |
|                 |                 |                 | are allowed in  |
|                 |                 |                 | a job document. |
+-----------------+-----------------+-----------------+-----------------+
| Data retention  | N/A             | 90 days         | Job data and    |
|                 |                 |                 | job execution   |
|                 |                 |                 | data will be    |
|                 |                 |                 | purged after 90 |
|                 |                 |                 | days.           |
+-----------------+-----------------+-----------------+-----------------+
| `StatusDetail`{ | 1 character     | 128 characters  |                 |
| .code}          |                 |                 |                 |
| map key size    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| `StatusDetail`{ | 1 character     | 128 characters  |                 |
| .code}          |                 |                 |                 |
| map value size  |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Job management  | N/A             | 30 TPS          | The AWS IoT     |
| APIs            |                 |                 | [Job Management |
|                 |                 |                 | and Control     |
|                 |                 |                 | APIs](http://do |
|                 |                 |                 | cs.aws.amazon.c |
|                 |                 |                 | om/iot/latest/d |
|                 |                 |                 | eveloperguide/j |
|                 |                 |                 | obs-api.html#jo |
|                 |                 |                 | bs-http-api)    |
|                 |                 |                 | have a maximum  |
|                 |                 |                 | of 30           |
|                 |                 |                 | transactions    |
|                 |                 |                 | per second      |
|                 |                 |                 | (TPS).          |
+-----------------+-----------------+-----------------+-----------------+
| Job messaging   | N/A             | 200 MPS         | The AWS IoT     |
| APIs            |                 |                 | [Jobs Device    |
|                 |                 |                 | MQTT and HTTPS  |
|                 |                 |                 | APIs](http://do |
|                 |                 |                 | cs.aws.amazon.c |
|                 |                 |                 | om/iot/latest/d |
|                 |                 |                 | eveloperguide/j |
|                 |                 |                 | obs-api.html#jo |
|                 |                 |                 | bs-mqtt-api)    |
|                 |                 |                 | have a maximum  |
|                 |                 |                 | of 200 messages |
|                 |                 |                 | per second      |
|                 |                 |                 | (MPS).          |
+-----------------+-----------------+-----------------+-----------------+
:::
:::

### AWS IoT Bulk Thing Registration Limits {#bulk-thing-reg-limits}

::: {.table}

::: {.table-contents}
  Resource                        Limit     Note
  ------------------------------- --------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------
  Registration task termination   30 days   Any pending/uncompleted bulk registration tasks are terminated after 30 days.
  Data retention policy           30 days   Once the associated bulk registration task has completed (which can be long lived), bulk Thing registration related data is permanently deleted after 30 days.
  Allowed registration tasks      1         For any given AWS account, only one bulk registration task can run at a time.
  Maximum line length             256K      Each line in an [Amazon S3 input JSON file](http://docs.aws.amazon.com/iot/latest/developerguide/bulk-provisioning.html) cannot exceed 256K in length.
:::
:::

AWS Key Management Service (AWS KMS) Limits {#limits_kms}
-------------------------------------------

::: {.table}

::: {.table-contents}
  Resource                               Default Limit
  -------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------
  Customer Master Keys (CMKs)            1000
  Aliases                                1100
  Grants per CMK                         2500
  Grants for a given principal per CMK   500
  Requests per second                    Varies by API operation; see [Limits](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html) in the *AWS Key Management Service Developer Guide*.
:::
:::

All limits in the preceding table apply per region and per AWS account.

For more information about these limits, see [Limits](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html) in the *AWS Key Management Service Developer Guide*.

Amazon Kinesis Data Firehose Limits {#limits-akf}
-----------------------------------

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Delivery streams per region       | 50                                |
+-----------------------------------+-----------------------------------+
| Delivery stream capacity for US   | 2,000 transactions/second         |
| East (N. Virginia), US West       |                                   |
| (Oregon), and EU (Ireland) â€     | 5,000 records/second              |
|                                   |                                   |
|                                   | 5 MB/second                       |
+-----------------------------------+-----------------------------------+
| Delivery stream capacity for      | 1,000 transactions/second         |
| other Regions where Kinesis Data  |                                   |
| Firehose is available â€          | 1,000 records/second              |
|                                   |                                   |
|                                   | 1 MB/second                       |
+-----------------------------------+-----------------------------------+
:::
:::

â€  The three capacity limits scale proportionally. For example, if you increase the throughput limit to 2 MB/second in Asia Pacific (Singapore), the other limits increase to 2,000 transactions/second and 2,000 records/second.

For more information about these limits, see [Amazon Kinesis Data Firehose Limits](http://docs.aws.amazon.com/firehose/latest/dev/limits.html) in the *Amazon Kinesis Data Firehose Developer Guide*.

Amazon Kinesis Data Streams Limits {#limits-aks}
----------------------------------

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Shards per region                 | US East (N. Virginia) Region â€"  |
|                                   | 500                               |
|                                   |                                   |
|                                   | US West (Oregon) Region â€" 500   |
|                                   |                                   |
|                                   | EU (Ireland) Region â€" 500       |
|                                   |                                   |
|                                   | All other supported regions â€"   |
|                                   | 200                               |
+-----------------------------------+-----------------------------------+
:::
:::

For more information about these limits, see [Amazon Kinesis Data Streams Limits](http://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html) in the *Amazon Kinesis Data Streams Developer Guide*.

Amazon Kinesis Data Analytics Limits {#limits-aka}
------------------------------------

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Kinesis Processing Units (KPUs)   | US East (N. Virginia) Region â€"  |
|                                   | 8                                 |
|                                   |                                   |
|                                   | US West (Oregon) Region â€" 8     |
|                                   |                                   |
|                                   | EU (Ireland) Region â€" 8         |
+-----------------------------------+-----------------------------------+
| Input Parallelism                 | 64 input streams                  |
+-----------------------------------+-----------------------------------+
| Applications                      | 50                                |
+-----------------------------------+-----------------------------------+
:::
:::

For more information about these limits, see [Limits](http://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html) in the *Amazon Kinesis Data Analytics Developer Guide*.

Amazon Kinesis Video Streams Limits {#limits-akv}
-----------------------------------

The limits below are either soft \[s\], which can be upgraded by submitting a support ticket, or hard \[h\], which cannot be increased.

### Control Plane API limits {#limits-akv-control}

The following section describes limits for control-plane APIs.

When an account-level Request limit is reached, a `ClientLimitExceededException`{.code} is thrown.

When an account-level Streams limit is reached, or a stream-level limit is reached, a `StreamLimitExceededException`{.code} is thrown.

::: {.table}
**Control Plane API limits**

::: {.table-contents}
  API                   Account Limit: Request   Account Limit: Streams          Stream-level limit   Relevant Exceptions and Notes
  --------------------- ------------------------ ------------------------------- -------------------- ---------------------------------------------------------------------------------------------------------------------------------------------
  **CreateStream**      50 TPS \[s\]             100 streams per account \[s\]   5 TPS \[h\]          Devices, CLIs, SDK-driven access and the console can all invoke this API. Only one API call succeeds if the stream doesnâ€™t already exist.
  **DescribeStream**    300 TPS \[h\]            N/A                             5 TPS \[h\]          
  **UpdateStream**      50 TPS \[h\]             N/A                             5 TPS \[h\]          
  **ListStreams**       300 TPS \[h\]            N/A                             5 TPS \[h\]          
  **DeleteStream**      50 TPS \[h\]             N/A                             5 TPS \[h\]          
  **GetDataEndpoint**   300 TPS \[h\]            N/A                             5 TPS \[h\]          When combined with account limit, this implies a maximum of 60 streams can be Put to and Read from (with 4 consumers).
:::
:::

### Data Plane API limits {#limits-akv-data}

The following section describes limits for control-plane APIs.

When a stream-level limit is exceeded, a `StreamLimitExceededException`{.code} is thrown.

When a connection-level limit is reached, a `ConnectionLimitExceededException`{.code} is thrown.

The following errors or acks are thrown when a fragment-level limit is reached:

::: {.itemizedlist}
-   A `MIN_FRAGMENT_DURATION_REACHED`{.code} ack is returned for a fragment below the minumum duration.

-   A `MAX_FRAGMENT_DURATION_REACHED`{.code} ack is returned for a fragment above the maximum duration.

-   A `MAX_FRAGMENT_SIZE`{.code} ack is returned for a fragment above the maximum data size.

-   A `FragmentLimitExceeded`{.code} exception is thrown if a fragment limit is reached in a `GetMediaForFragmentList`{.code} operation.
:::

::: {.table}
**Data Plane API limits**

::: {.table-contents}
+-----------+-----------+-----------+-----------+-----------+-----------+
| API       | Stream-le | Connectio | Bandwidth | Fragment- | Relevant  |
|           | vel       | n-level   | limit     | level     | Exception |
|           | limit     | limit     |           | limit     | s         |
|           |           |           |           |           | and Notes |
+===========+===========+===========+===========+===========+===========+
| **PutMedi | 5 TPS     | 1 \[s\]   | 12.5      | ::: {.ite | A typical |
| a**       | \[h\]     |           | MB/second | mizedlist | PutMedia  |
|           |           |           | ,         | }         | request   |
|           |           |           | or 100    | -   Minim | will      |
|           |           |           | Mbps      | um        | contain   |
|           |           |           | \[s\]     |     fragm | data for  |
|           |           |           |           | ent       | several   |
|           |           |           |           |     durat | seconds,  |
|           |           |           |           | ion:      | resulting |
|           |           |           |           |     1     | in a      |
|           |           |           |           |     secon | lower TPS |
|           |           |           |           | d         | per       |
|           |           |           |           |     \[h\] | stream.   |
|           |           |           |           |           | In the    |
|           |           |           |           | -   Maxim | case of   |
|           |           |           |           | um        | multiple  |
|           |           |           |           |     fragm | concurren |
|           |           |           |           | ent       | t         |
|           |           |           |           |     durat | connectio |
|           |           |           |           | ion:      | ns        |
|           |           |           |           |     10    | that      |
|           |           |           |           |     secon | exceed    |
|           |           |           |           | ds        | limits,   |
|           |           |           |           |     \[h\] | the last  |
|           |           |           |           |           | connectio |
|           |           |           |           | -   Maxim | n         |
|           |           |           |           | um        | is        |
|           |           |           |           |     fragm | accepted. |
|           |           |           |           | ent       |           |
|           |           |           |           |     size: |           |
|           |           |           |           |     50 MB |           |
|           |           |           |           |     \[h\] |           |
|           |           |           |           | :::       |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| **GetMedi | 5 TPS     | 3 \[s\]   | 25 MB/s   | N/A       | Only      |
| a**       | \[h\]     |           | or 200    |           | three     |
|           |           |           | Mbps      |           | clients   |
|           |           |           | \[s\]     |           | can       |
|           |           |           |           |           | concurren |
|           |           |           |           |           | tly       |
|           |           |           |           |           | receive   |
|           |           |           |           |           | content   |
|           |           |           |           |           | from the  |
|           |           |           |           |           | media     |
|           |           |           |           |           | stream at |
|           |           |           |           |           | any       |
|           |           |           |           |           | moment of |
|           |           |           |           |           | time.     |
|           |           |           |           |           | Further   |
|           |           |           |           |           | client    |
|           |           |           |           |           | connectio |
|           |           |           |           |           | ns        |
|           |           |           |           |           | are       |
|           |           |           |           |           | rejected. |
|           |           |           |           |           | A unique  |
|           |           |           |           |           | consuming |
|           |           |           |           |           | client    |
|           |           |           |           |           | shouldnâ€ |
|           |           |           |           |           | ™t        |
|           |           |           |           |           | need more |
|           |           |           |           |           | than 2 or |
|           |           |           |           |           | 3 TPS,    |
|           |           |           |           |           | since     |
|           |           |           |           |           | once the  |
|           |           |           |           |           | connectio |
|           |           |           |           |           | n         |
|           |           |           |           |           | is        |
|           |           |           |           |           | establish |
|           |           |           |           |           | ed,       |
|           |           |           |           |           | we        |
|           |           |           |           |           | anticipat |
|           |           |           |           |           | e         |
|           |           |           |           |           | that the  |
|           |           |           |           |           | applicati |
|           |           |           |           |           | on        |
|           |           |           |           |           | will read |
|           |           |           |           |           | continuou |
|           |           |           |           |           | sly.      |
|           |           |           |           |           |           |
|           |           |           |           |           | If a      |
|           |           |           |           |           | typical   |
|           |           |           |           |           | fragment  |
|           |           |           |           |           | is        |
|           |           |           |           |           | approxima |
|           |           |           |           |           | tely      |
|           |           |           |           |           | 5 MB,     |
|           |           |           |           |           | this      |
|           |           |           |           |           | limit     |
|           |           |           |           |           | will mean |
|           |           |           |           |           | \~75 MB/  |
|           |           |           |           |           | sec per   |
|           |           |           |           |           | Kinesis   |
|           |           |           |           |           | video     |
|           |           |           |           |           | stream.   |
|           |           |           |           |           | Such a    |
|           |           |           |           |           | stream    |
|           |           |           |           |           | would     |
|           |           |           |           |           | have an   |
|           |           |           |           |           | outgoing  |
|           |           |           |           |           | bit rate  |
|           |           |           |           |           | of 2x the |
|           |           |           |           |           | streams\' |
|           |           |           |           |           | maximum   |
|           |           |           |           |           | incoming  |
|           |           |           |           |           | bit rate. |
+-----------+-----------+-----------+-----------+-----------+-----------+
| **ListFra | 5 TPS     | 5 \[s\]   | N/A       | N/A       | Five      |
| gments**  | \[h\]     |           |           |           | fragment- |
|           |           |           |           |           | based     |
|           |           |           |           |           | consuming |
|           |           |           |           |           | applicati |
|           |           |           |           |           | ons       |
|           |           |           |           |           | can       |
|           |           |           |           |           | concurren |
|           |           |           |           |           | tly       |
|           |           |           |           |           | list      |
|           |           |           |           |           | fragments |
|           |           |           |           |           | based on  |
|           |           |           |           |           | processin |
|           |           |           |           |           | g         |
|           |           |           |           |           | requireme |
|           |           |           |           |           | nts.      |
+-----------+-----------+-----------+-----------+-----------+-----------+
| **GetMedi | 5 TPS     | 5 \[s\]   | 25 MB/s   | Maximum   | Five      |
| aForFragm | \[h\]     |           | or 200    | number of | fragment- |
| entList** |           |           | Mbps      | fragments | based     |
|           |           |           | \[s\]     | :         | consuming |
|           |           |           |           | 1000      | applicati |
|           |           |           |           | \[h\]     | ons       |
|           |           |           |           |           | can       |
|           |           |           |           |           | concurren |
|           |           |           |           |           | tly       |
|           |           |           |           |           | get       |
|           |           |           |           |           | media.    |
|           |           |           |           |           | Further   |
|           |           |           |           |           | connectio |
|           |           |           |           |           | ns        |
|           |           |           |           |           | are       |
|           |           |           |           |           | rejected. |
+-----------+-----------+-----------+-----------+-----------+-----------+
:::
:::

AWS Lambda Limits {#limits_lambda}
-----------------

::: {.table}

::: {.table-contents}
  Resource                Limit
  ----------------------- -------
  Concurrent executions   1000
:::
:::

For more information about these limits, see [AWS Lambda Limits](http://docs.aws.amazon.com/lambda/latest/dg/limits.html) in the *AWS Lambda Developer Guide*.

AWS Lambda dynamically scales capacity in response to increased traffic, subject to your account\'s concurrent execution limit. For more information, see [Managing Concurrency](http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html). To handle a burst in traffic, Lambda immediately increases your concurrently executing functions by a predetermined amount, dependent on which region it\'s executed (see table below).

If the default **Immediate Concurrency Increase** value, as noted in the table below, is not sufficient to accommodate the traffic surge, Lambda continues to increase the number of concurrent function executions by 500 per minute until your account safety limit has been reached or the number of concurrently executing functions is sufficient to successfully process the increased load.

::: {.table}
::: {.table-contents}
  Region                       Immediate Concurrency Increase (function executions)
  ---------------------------- ------------------------------------------------------
  Asia Pacific (Tokyo)         1000
  Asia Pacific (Seoul)         500
  Asia Pacific (Mumbai)        500
  Asia Pacific (Singapore)     500
  Asia Pacific (Sydney)        500
  Canada (Central)             500
  EU (Frankfurt)               1000
  EU (London)                  500
  EU (Ireland)                 3000
  AWS GovCloud (US)            500
  US East (Ohio)               500
  US West (N. California)      500
  US West (Oregon)             3000
  US East (N. Virginia)        3000
  South America (SÃ£o Paulo)   500
  China (Beijing)              500
  AWS GovCloud (US)            500
:::
:::

Amazon Lightsail Limits {#limits_lightsail}
-----------------------

::: {.table}

::: {.table-contents}
  Resource                             Default Limit                                Comment
  ------------------------------------ -------------------------------------------- ---------------------------------
  Number of instances                  20 per account                               This limit cannot be increased.
  Number of Elastic IP addresses       5 per account                                This limit cannot be increased.
  Number of parallel SSH connections   3 x the number of instances in the account   This limit cannot be increased.
  Number of hosted zones               3 per account                                This limit cannot be increased.
:::
:::

Amazon Machine Learning (Amazon ML) Limits {#limits_machinelearning}
------------------------------------------

::: {.table}

::: {.table-contents}
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
  Number of simultaneous jobs                                            25
  Longest run time for any job                                           7 days
  Number of classes for multiclass ML models                             100
  ML model size                                                          2 GB
:::
:::

::: {.aws-note}
Note

The size of your data files is limited to ensure that jobs finish in a timely manner. Jobs that have been running for more than seven days are automatically terminated, resulting in a FAILED status.
:::

For more information about these limits, see [Amazon ML Limits](http://docs.aws.amazon.com/machine-learning/latest/dg/system-limits.html) in the *Amazon Machine Learning Developer Guide*.

AWS Elemental MediaConvert Limits {#limits_mediaconvert}
---------------------------------

::: {.table}

::: {.table-contents}
  Resource                                                                    Default Limit
  --------------------------------------------------------------------------- -----------------------------------------------
  Number of queues                                                            10
  Concurrent jobs processed across all queues                                 100
  Concurrent jobs processed from a queue                                      100 divided by number of queues
  Number of custom output presets                                             100
  Number of custom output job templates                                       100
  DescribeEndpoints API calling rate per second                               0.01667 TPS (Once per 60 seconds, burst zero)
  Aggregate API calling rate per second for job, queue, preset and template   2 TPS (2 per second, burst 100)\]
:::
:::

AWS Elemental MediaLive Limits {#limits_medialive}
------------------------------

::: {.table}

::: {.table-contents}
  Resource                        Default Limit
  ------------------------------- ---------------
  Maximum inputs                  5
  Maximum input security groups   5
  Maximum channels                5
:::
:::

AWS Elemental MediaPackage Limits {#limits_mediapackage}
---------------------------------

::: {.table}

::: {.table-contents}
  Resource                        Default Limit
  ------------------------------- ---------------
  Maximum channels per account    10
  Maximum endpoints per channel   10
:::
:::

AWS Elemental MediaStore Limits {#limits_mediastore}
-------------------------------

::: {.table}

::: {.table-contents}
  Resource     Default Limit
  ------------ ---------------
  Containers   100
:::
:::

For information about AWS Elemental MediaStore limits, including limits that can\'t be increased, see [Limits](http://docs.aws.amazon.com/mediastore/latest/ug/limits.html) in the *AWS Elemental MediaStore User Guide*.

AWS Elemental MediaTailor Limits {#limits_mediatailor}
--------------------------------

::: {.table}

::: {.table-contents}
+-----------------------+-----------------------+-----------------------+
| Resource              | Default Limit         | Comment               |
+=======================+=======================+=======================+
| Transactions          | 3,000 concurrent      | This is an            |
|                       | transactions per      | account-level limit.  |
|                       | second across all     |                       |
|                       | request types (such   | Your transactions per |
|                       | as manifest requests  | second are largely    |
|                       | and tracking requests | dependent on how      |
|                       | for client-side       | often the player      |
|                       | reporting).           | requests updated      |
|                       |                       | manifests. For        |
|                       |                       | example, a player     |
|                       |                       | with eight second     |
|                       |                       | segments might update |
|                       |                       | the manifest every    |
|                       |                       | eight seconds. The    |
|                       |                       | player, then,         |
|                       |                       | generates 0.125       |
|                       |                       | transactions per      |
|                       |                       | second.               |
+-----------------------+-----------------------+-----------------------+
:::
:::

For more information about AWS Elemental MediaTailor limits, including limits that can\'t be increased, see [Limits](http://docs.aws.amazon.com/mediatailor/latest/ug/limits.html) in the *AWS Elemental MediaTailor User Guide*.

Amazon MQ Limits {#limits_amazon-mq}
----------------

For information about these limits, see [Amazon MQ Limits](http://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-limits.html) in the *Amazon MQ Developer Guide*.

Amazon Neptune Limits {#limits_neptune}
---------------------

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| US East (N. Virginia) Region:     | Maximum instances is 3.           |
|                                   |                                   |
| Maximum instances                 |                                   |
+-----------------------------------+-----------------------------------+
:::
:::

You can request an increase on this limit. For more information, see <https://aws.amazon.com/support>.

AWS OpsWorks for Chef Automate and AWS OpsWorks for Puppet Enterprise Limits {#limits_opworks}
----------------------------------------------------------------------------

::: {.table}

::: {.table-contents}
  Resource                                     Default Limit
  -------------------------------------------- ---------------
  Chef or Puppet servers                       5
  User-initiated (manual) backup generations   10
  Automated (scheduled) backup generations     30
:::
:::

AWS OpsWorks Stacks Limits
--------------------------

::: {.table}

::: {.table-contents}
  Resource              Default Limit
  --------------------- ---------------
  Stacks                40
  Layers per stack      40
  Instances per stack   40
  Apps per stack        40
:::
:::

AWS Organizations Limits
------------------------

::: {.table}

::: {.table-contents}
  Resource                    Default Limit
  --------------------------- -----------------------------------
  Accounts per organization   Varies. Contact Customer Support.
  Invitations sent per day    20
:::
:::

For more information about these limits, see [Limits of AWS Organizations](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html) in the *AWS Organizations User Guide*.

Amazon Pinpoint Limits {#limits_pinpoint}
----------------------

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Active campaigns per account      | 200 per account.                  |
|                                   |                                   |
|                                   | ::: {.aws-note}                   |
|                                   | Note                              |
|                                   |                                   |
|                                   | An *active campaign* is a         |
|                                   | campaign that hasn\'t completed   |
|                                   | or failed. Active campaigns have  |
|                                   | a status of `SCHEDULED`{.code},   |
|                                   | `EXECUTING`{.code}, or            |
|                                   | `PENDING_NEXT_RUN`{.code}.        |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
| Concurrent endpoint import jobs   | 2 per account.                    |
| per account                       |                                   |
+-----------------------------------+-----------------------------------+
| Message sends per campaign        | 100 million.                      |
| activity                          |                                   |
+-----------------------------------+-----------------------------------+
| Total file size per endpoint      | 1 GB per import job.              |
| import job                        |                                   |
+-----------------------------------+-----------------------------------+
| SMS account spend threshold       | USD\$1.00 per account.            |
+-----------------------------------+-----------------------------------+
| Maximum number of Amazon SNS      | 100,000 per account.              |
| topics for two-way SMS            |                                   |
+-----------------------------------+-----------------------------------+
| Number of emails that can be sent | 200 emails per 24-hour period for |
| per 24-hour period (*sending      | accounts in the sandbox           |
| quota*)                           | environment.                      |
+-----------------------------------+-----------------------------------+
| Number of emails that can be sent | 1 email per second for accounts   |
| each second (*sending rate*)      | in the sandbox environment.       |
+-----------------------------------+-----------------------------------+
| Email recipient addresses         | Accounts in the sandbox           |
|                                   | environment may only send email   |
|                                   | to recipients whose email         |
|                                   | addresses or domains have been    |
|                                   | verified.                         |
+-----------------------------------+-----------------------------------+
:::
:::

To increase any of the limits above, submit a [Amazon Pinpoint Limit Increase case](https://console.aws.amazon.com/support/home#/case/create).

For more information about Amazon Pinpoint limits, including limits that can\'t be increased, see [Limits](http://docs.aws.amazon.com/pinpoint/latest/developerguide/limits.html) in the Amazon Pinpoint Developer Guide.

Amazon Polly Limits {#limits_polly}
-------------------

::: {.itemizedlist}
-   Throttle rate per IP address: 100 transactions (requests) per second (tps) with a burst limit of 120 tps.

-   Throttle rate per operation:

    ::: {.table}
    **Throttle Rate per Operation**

    ::: {.table-contents}
    +-----------------------------------+-----------------------------------+
    | Operation                         | Limit                             |
    +===================================+===================================+
    | **Lexicon**                       |                                   |
    +-----------------------------------+-----------------------------------+
    | `DeleteLexicon`{.code}            | Any 2 transactions per second     |
    |                                   | (tps) from these operations       |
    | `PutLexicon`{.code}               | combined.                         |
    |                                   |                                   |
    | `GetLexicon`{.code}               | Maximum allowed burst of 4 tps.   |
    |                                   |                                   |
    | `ListLexicons`{.code}             |                                   |
    +-----------------------------------+-----------------------------------+
    | **Speech**                        |                                   |
    +-----------------------------------+-----------------------------------+
    | `DescribeVoices`{.code}           | 80 rps with a burst limit of 100  |
    |                                   | tps                               |
    +-----------------------------------+-----------------------------------+
    | `SynthesizeSpeech`{.code}         | 80 rps with a burst limit of 100  |
    |                                   | tps                               |
    +-----------------------------------+-----------------------------------+
    :::
    :::
:::

Amazon Redshift Limits {#limits_redshift}
----------------------

::: {.table}

::: {.table-contents}
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
:::
:::

For more information about these limits, see [Limits in Amazon Redshift](http://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Cluster Management Guide*.

Amazon Rekognition Limits {#limits_rekognition}
-------------------------

Amazon Rekognition does not have service limits that you can change. For information about Amazon Rekognition service limits, see [Amazon Rekognition Limits](http://docs.aws.amazon.com/rekognition/latest/dg/limits.html).

Amazon Relational Database Service (Amazon RDS) Limits {#limits_rds}
------------------------------------------------------

::: {.table}

::: {.table-contents}
  Resource                                   Default Limit
  ------------------------------------------ ---------------
  Clusters                                   40
  Cluster parameter groups                   50
  DB Instances                               40
  Event subscriptions                        20
  Manual snapshots                           100
  Option groups                              20
  Parameter groups                           50
  Read replicas per master                   5
  Reserved instances (purchased per month)   40
  Rules per security group                   20
  Security groups                            25
  Security groups (VPC)                      5
  Subnet groups                              50
  Subnets per subnet group                   20
  Tags per resource                          50
  Total storage for all DB instances         100 TB
:::
:::

AWS Resource Groups Limits {#limits_resgrps}
--------------------------

::: {.table}
::: {.table-contents}
  Resource                      Default Limit
  ----------------------------- ---------------
  Resource groups per account   100
:::
:::

Amazon RouteÂ 53 Limits {#limits_route53}
-----------------------

::: {.table}
**DNS and Domain Registration**

::: {.table-contents}
  Resource                                                        Default Limit
  --------------------------------------------------------------- ---------------
  Hosted zones                                                    500
  Domains                                                         50
  Resource record sets per hosted zone                            10,000
  Reusable delegation sets                                        100
  Hosted zones that can use the same reusable delegation set      100
  Amazon VPCs that you can associate with a private hosted zone   100
  Health checks                                                   200
  Traffic policies                                                50
  Traffic policy records                                          5
:::
:::

::: {.table}
**Auto Naming**

::: {.table-contents}
  Resource                     Default Limit
  ---------------------------- ------------------
  Namespaces per AWS account   50 per region
  Instances per namespace      2,000 per region
  Instances per service        100 per region
:::
:::

For more information about these limits, see [RouteÂ 53 Limits](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html) in the *Amazon RouteÂ 53 Developer Guide*.

Amazon SageMaker Limits {#limits_sagemaker}
-----------------------

The following tables group Amazon SageMaker limits by components.

Amazon SageMaker Notebooks

::: {.table}

::: {.table-contents}
  Resource                               Default Limit
  -------------------------------------- ---------------
  ml.t2.medium instances                 20
  ml.m4.xlarge instances                 20
  ml.p2.xlarge instances                 1
  Number of notebook instances           100
  Number of running notebook instances   20
:::
:::

Amazon SageMaker Training

::: {.table}

::: {.table-contents}
  Resource                                 Default Limit
  ---------------------------------------- ---------------
  ml.m4.xlarge instances                   20
  ml.m4.4xlarge instances                  10
  ml.m4.10xlarge instances                 5
  ml.c4.xlarge instances                   20
  ml.c4.2xlarge instances                  20
  ml.c4.8xlarge instances                  20
  ml.c5.xlarge instances                   0
  ml.c5.2xlarge instances                  0
  ml.c5.4xlarge instances                  0
  ml.c5.9xlarge instances                  0
  ml.c5.18xlarge instances                 0
  ml.p2.xlarge instances                   1
  ml.p2.8xlarge instances                  1
  ml.p2.16xlarge instances                 0
  ml.p3.2xlarge instances                  0
  ml.p3.8xlarge instances                  0
  ml.p3.16xlarge instances                 0
  Longest run time for a training job      5 days
  Number of instances                      20
  Number of instances for a training job   20
  Size of EBS volume for an instance       1 TB
:::
:::

Amazon SageMaker Hosting

::: {.table}

::: {.table-contents}
  Resource                              Default Limit
  ------------------------------------- ---------------
  ml.t2.medium instances                20
  ml.m4.xlarge instances                20
  ml.c4.xlarge instances                20
  ml.c4.2xlarge instances               20
  ml.c4.8xlarge instances               20
  ml.c5.xlarge instances                0
  ml.c5.2xlarge instances               0
  ml.c5.9xlarge instances               0
  ml.p2.xlarge instances                2
  ml.p3.2xlarge instances               0
  Number of instances                   20
  Number of instances for an endpoint   20
  Total TPS for all endpoints           10,000
  Hosting                               5 MB
:::
:::

AWS Server Migration Service Limits {#limits_server_migration}
-----------------------------------

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Concurrent VM migrations          | 50 per account                    |
+-----------------------------------+-----------------------------------+
| Maximum duration of service usage | 90 days                           |
| per VM (not per account),         |                                   |
| beginning with the initial        |                                   |
| replication of a VM. We terminate |                                   |
| an ongoing replication after this |                                   |
| period, unless a customer         |                                   |
| requests a limit increase.        |                                   |
+-----------------------------------+-----------------------------------+
:::
:::

AWS Serverless Application Repository Limits {#limits_serverlessrepo}
--------------------------------------------

::: {.table}
**Limits Per Account Per Region**

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Public Applications               | 100                               |
+-----------------------------------+-----------------------------------+
| Free Amazon S3 Storage for Code   | 5 GB                              |
| Packages                          |                                   |
+-----------------------------------+-----------------------------------+
:::
:::

AWS Service Catalog Limits {#limits_servicecatalog}
--------------------------

::: {.table}

::: {.table-contents}
  Resource                   Default Limit
  -------------------------- --------------------------------------------------------------
  Portfolios                 25 per account
  Users, groups, and roles   25 per portfolio
  Products                   25 per portfolio, 100 total per account
  Product versions           50 per product
  Constraints                25 per product per portfolio
  Tags                       20 per product, 20 per portfolio, 50 per provisioned product
  Stacks                     200 (AWS CloudFormation limit)
:::
:::

AWS Shield Advanced Limits {#limits_shield}
--------------------------

offers advanced monitoring and protection for Elastic IP addresses, CloudFront distributions, RouteÂ 53 hosted zones, or Elastic Load Balancing load balancers. You can monitor and protect up to 100 of each of these resource types per account. If you want to increase these limits, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/).

Amazon Simple Email Service (Amazon SES) Limits {#limits_ses_quota}
-----------------------------------------------

The following are the default limits for Amazon SES in the sandbox environment.

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Daily sending quota               | 200 messages per 24-hour period.  |
+-----------------------------------+-----------------------------------+
| Maximum send rate                 | 1 email per second.               |
|                                   |                                   |
|                                   | ::: {.aws-note}                   |
|                                   | Note                              |
|                                   |                                   |
|                                   | The rate at which Amazon SES      |
|                                   | accepts your messages might be    |
|                                   | less than the maximum send rate.  |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
| Recipient address verification    | All recipient addresses must be   |
|                                   | verified.                         |
+-----------------------------------+-----------------------------------+
:::
:::

For more information about these limits, see [Limits in Amazon SES](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html) in the *Amazon Simple Email Service Developer Guide*.

Amazon Simple Notification Service (Amazon SNS) Limits {#limits_sns}
------------------------------------------------------

::: {.table}

::: {.table-contents}
  Resource                                       Default Limit
  ---------------------------------------------- ------------------------
  Topics                                         100,000 per account
  Subscriptions                                  12,500,000 per topic
  Pending subscriptions                          5,000 per account
  Account spend threshold for SMS                1.00 USD per account
  Delivery rate for promotional SMS messages     20 messages per second
  Delivery rate for transactional SMS messages   20 messages per second
  Message filter policies                        100 per account
:::
:::

To increase any of the limits above, submit an [SNS Limit Increase case](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-sns).

### Amazon SNS API Throttling Limits {#limits_sns_api_throttles}

::: {.table}

::: {.table-contents}
  API                                  Transactions per Second
  ------------------------------------ -------------------------
  ListEndpointsByPlatformApplication   30
  ListTopics                           30
  ListPlatformApplications             15
  ListSubscriptions                    30
  ListSubscriptionsByTopic             30
  Subscribe                            100
  Unsubscribe                          100
:::
:::

The Amazon SNS API throttling limits cannot be increased.

Amazon Simple Queue Service (Amazon SQS) {#limits_sqs}
----------------------------------------

For more information about these limits, see [Amazon SQS Limits](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-limits.html) in the *Amazon Simple Queue Service Developer Guide* and the \"Limits and Restrictions\" section of the [Amazon SQS FAQs](https://aws.amazon.com/sqs/faqs/).

Amazon Simple Storage Service (Amazon S3) Limits {#limits_s3}
------------------------------------------------

::: {.table}

::: {.table-contents}
  Resource   Default Limit
  ---------- -----------------
  Buckets    100 per account
:::
:::

For more information about these limits, see [Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html) limits in the **Amazon Simple Storage Service Developer Guide**.

Amazon Simple Workflow Service (Amazon SWF) Limits {#limits_swf}
--------------------------------------------------

For more information about these limits, see [Amazon SWF Limits](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-limits.html) in the *Amazon Simple Workflow Service Developer Guide*.

Amazon SimpleDB Limits {#limits_simpledb}
----------------------

::: {.table}

::: {.table-contents}
  Resource   Default Limit
  ---------- ---------------
  Domains    250
:::
:::

For more information about these limits, see [Amazon SimpleDB Limits](http://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDBLimits.html) in the *Amazon SimpleDB Developer Guide*.

AWS Step Functions Limits {#limits-step-functions}
-------------------------

For more information about these limits, see [AWS Step Functions Limits](http://docs.aws.amazon.com/step-functions/latest/dg/limits.html) in the *AWS Step Functions Developer Guide*.

AWS Storage Gateway Limits {#limits-storage-gateway}
--------------------------

For more information about these limits, see [AWS Storage Gateway Limits](http://docs.aws.amazon.com/storagegateway/latest/userguide/resource-gateway-limits.html) in the *AWS Storage Gateway User Guide*.

AWS Systems Manager Limits {#limits_ssm}
--------------------------

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Concurrently executing            | 25                                |
| Automations                       |                                   |
|                                   | Each AWS account can execute a    |
|                                   | maximum of 25 Automations at one  |
|                                   | time. Concurrent executions       |
|                                   | greater than 25 are automatically |
|                                   | added to an execution queue.      |
+-----------------------------------+-----------------------------------+
| Additional Automation executions  | 75                                |
| that can be queued                |                                   |
+-----------------------------------+-----------------------------------+
| Maximum duration an Automation    | 12 hours                          |
| execution can run when running in |                                   |
| the context of a user             | If you expect an Automation to    |
|                                   | run longer than 12 hours, then    |
|                                   | you must execute the Automation   |
|                                   | by using a service role (or       |
|                                   | assume role).                     |
+-----------------------------------+-----------------------------------+
| Run Command execution history     | 30 days                           |
| retention                         |                                   |
|                                   | The history of each command is    |
|                                   | available for up to 30 days. In   |
|                                   | addition, you can store a copy of |
|                                   | all log files in Amazon Simple    |
|                                   | Storage Service or have an audit  |
|                                   | trail of all API calls in AWS     |
|                                   | CloudTrail.                       |
+-----------------------------------+-----------------------------------+
| On-premises managed instances     | Each AWS account can activate a   |
| registered through Amazon EC2     | maximum of 1,000 on-premises      |
| activation                        | instances in a region for use     |
|                                   | with Systems Manager.             |
|                                   |                                   |
|                                   | For more information about        |
|                                   | activating on-premises instances  |
|                                   | for use in your hybrid            |
|                                   | environment, see [Create a        |
|                                   | Managed-Instance                  |
|                                   | Activation](http://docs.aws.amazo |
|                                   | n.com/systems-manager/latest/user |
|                                   | guide/systems-manager-managedinst |
|                                   | ances.html#sysman-managed-instanc |
|                                   | e-activation)                     |
|                                   | in the *[AWS Systems Manager User |
|                                   | Guide](http://docs.aws.amazon.com |
|                                   | /systems-manager/latest/userguide |
|                                   | /)*.                              |
|                                   |                                   |
|                                   | ::: {.aws-note}                   |
|                                   | Note                              |
|                                   |                                   |
|                                   | Activation limits apply only to   |
|                                   | the on-premises instances you add |
|                                   | to your hybrid environment, and   |
|                                   | not to registered Amazon EC2      |
|                                   | instances.                        |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
| Systems Manager documents         | 200                               |
|                                   |                                   |
|                                   | Each AWS account can create a     |
|                                   | maximum of 200 documents per      |
|                                   | region.                           |
+-----------------------------------+-----------------------------------+
| Privately shared Systems Manager  | 1000                              |
| document                          |                                   |
|                                   | A single Systems Manager document |
|                                   | can be shared with a maximum of   |
|                                   | 1000 AWS accounts.                |
+-----------------------------------+-----------------------------------+
| Publicly shared Systems Manager   | 5                                 |
| document                          |                                   |
|                                   | Each AWS account can publicly     |
|                                   | share a maximum of five           |
|                                   | documents.                        |
+-----------------------------------+-----------------------------------+
| State Manager associations        | 10,000                            |
|                                   |                                   |
|                                   | Each Systems Manager document can |
|                                   | be associated with a maximum of   |
|                                   | 10,000 instances.                 |
+-----------------------------------+-----------------------------------+
| State Manager association         | 1,000                             |
| versions                          |                                   |
|                                   | You can created a maximum of      |
|                                   | 1,000 versions of a State Manager |
|                                   | association.                      |
+-----------------------------------+-----------------------------------+
| Inventory data collected per      | 1 MB                              |
| instance per call                 |                                   |
|                                   | This maximum adequately supports  |
|                                   | most inventory collection         |
|                                   | scenarios. When this limit is     |
|                                   | reached, no new inventory data is |
|                                   | collected for the instance.       |
|                                   | Inventory data previously         |
|                                   | collected is stored until the     |
|                                   | expiration.                       |
+-----------------------------------+-----------------------------------+
| Inventory data collected per      | 5 MB                              |
| instance per day                  |                                   |
|                                   | When this limit is reached, no    |
|                                   | new inventory data is collected   |
|                                   | for the instance. Inventory data  |
|                                   | previously collected is stored    |
|                                   | until the expiration.             |
+-----------------------------------+-----------------------------------+
| Custom Inventory Types            | 20                                |
|                                   |                                   |
|                                   | You can add up to 20 custom       |
|                                   | inventory types.                  |
+-----------------------------------+-----------------------------------+
| Custom Inventory Type Size        | 200 KB                            |
|                                   |                                   |
|                                   | This is the maximum size of the   |
|                                   | type, not the inventory           |
|                                   | collected.                        |
+-----------------------------------+-----------------------------------+
| Custom Inventory Type Attributes  | 50                                |
|                                   |                                   |
|                                   | This is the maximum number of     |
|                                   | attributes within the custom      |
|                                   | inventory type.                   |
+-----------------------------------+-----------------------------------+
| Inventory data expiration         | 30 days                           |
|                                   |                                   |
|                                   | If you terminate an instance,     |
|                                   | inventory data for that instance  |
|                                   | is deleted immediately. For       |
|                                   | running instances, inventory data |
|                                   | older than 30 days is deleted. If |
|                                   | you need to store inventory data  |
|                                   | longer than 30 days, you can use  |
|                                   | AWS Config to record history or   |
|                                   | periodically query and upload the |
|                                   | data to an Amazon S3 bucket. For  |
|                                   | more information, see, [Recording |
|                                   | Amazon EC2 managed instance       |
|                                   | inventory](http://docs.aws.amazon |
|                                   | .com/config/latest/developerguide |
|                                   | /resource-config-reference.html#r |
|                                   | ecording-managed-instance-invento |
|                                   | ry)                               |
|                                   | in the *AWS Config Developer      |
|                                   | Guide*.                           |
+-----------------------------------+-----------------------------------+
| Maintenance Windows per account   | 50                                |
+-----------------------------------+-----------------------------------+
| Tasks per Maintenance Window      | 20                                |
+-----------------------------------+-----------------------------------+
| Targets per Maintenance Window    | 50                                |
+-----------------------------------+-----------------------------------+
| Instance IDs per target           | 50                                |
+-----------------------------------+-----------------------------------+
| Targets per task                  | 10                                |
+-----------------------------------+-----------------------------------+
| Concurrent executions of a single | 1                                 |
| Maintenance Window                |                                   |
+-----------------------------------+-----------------------------------+
| Concurrent executions of          | 5                                 |
| Maintenance Windows               |                                   |
+-----------------------------------+-----------------------------------+
| Maintenance Window execution      | 30 days                           |
| history retention                 |                                   |
+-----------------------------------+-----------------------------------+
| Maximum number of parameters per  | 10,000                            |
| account                           |                                   |
+-----------------------------------+-----------------------------------+
| Max size for parameter value      | 4096 characters                   |
+-----------------------------------+-----------------------------------+
| Max history for a parameter       | 100 past values                   |
+-----------------------------------+-----------------------------------+
| Patch baselines per account       | 25                                |
+-----------------------------------+-----------------------------------+
| Patch groups per patch baseline   | 25                                |
+-----------------------------------+-----------------------------------+
:::
:::

Amazon Virtual Private Cloud (Amazon VPC) Limits {#limits_vpc}
------------------------------------------------

Unless otherwise noted, [submit a request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-vpc) to increase these limits.

::: {.table}

::: {.table-contents}
+-----------------------+-----------------------+-----------------------+
| Resource              | Default limit         | Comments              |
+=======================+=======================+=======================+
| VPCs per region       | 5                     | Increasing this limit |
|                       |                       | increases the limit   |
|                       |                       | on Internet gateways  |
|                       |                       | per region by the     |
|                       |                       | same amount. The      |
|                       |                       | multiple of the       |
|                       |                       | number of VPCs in the |
|                       |                       | region and the number |
|                       |                       | of security groups    |
|                       |                       | per VPC cannot exceed |
|                       |                       | 5000.                 |
+-----------------------+-----------------------+-----------------------+
| Subnets per VPC       | 200                   | \-                    |
+-----------------------+-----------------------+-----------------------+
| IPv4 CIDR blocks per  | 5                     | This limit is made up |
| VPC                   |                       | of the primary CIDR   |
|                       |                       | block plus 4          |
|                       |                       | secondary CIDR        |
|                       |                       | blocks.               |
+-----------------------+-----------------------+-----------------------+
| IPv6 CIDR blocks per  | 1                     | This limit cannot be  |
| VPC                   |                       | increased.            |
+-----------------------+-----------------------+-----------------------+
| Internet gateways per | 5                     | This limit is         |
| region                |                       | directly correlated   |
|                       |                       | with the limit on     |
|                       |                       | VPCs per region. To   |
|                       |                       | increase this limit,  |
|                       |                       | increase the limit on |
|                       |                       | VPCs per region. Only |
|                       |                       | one Internet gateway  |
|                       |                       | can be attached to a  |
|                       |                       | VPC at a time.        |
+-----------------------+-----------------------+-----------------------+
| Egress-only Internet  | 5                     | This limit is         |
| gateways per region   |                       | directly correlated   |
|                       |                       | with the limit on     |
|                       |                       | VPCs per region. To   |
|                       |                       | increase this limit,  |
|                       |                       | increase the limit on |
|                       |                       | VPCs per region. Only |
|                       |                       | one egress-only       |
|                       |                       | Internet gateway can  |
|                       |                       | be attached to a VPC  |
|                       |                       | at a time.            |
+-----------------------+-----------------------+-----------------------+
| Virtual private       | 5                     | Only one virtual      |
| gateways per region   |                       | private gateway can   |
|                       |                       | be attached to a VPC  |
|                       |                       | at a time.            |
+-----------------------+-----------------------+-----------------------+
| Customer gateways per | 50                    | To increase this      |
| region                |                       | limit, contact AWS    |
|                       |                       | Support.              |
+-----------------------+-----------------------+-----------------------+
| VPN connections per   | 50                    | \-                    |
| region                |                       |                       |
+-----------------------+-----------------------+-----------------------+
| VPN connections per   | 10                    | \-                    |
| VPC (per virtual      |                       |                       |
| private gateway)      |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Route tables per VPC  | 200                   | This limit includes   |
|                       |                       | the main route table. |
+-----------------------+-----------------------+-----------------------+
| Routes per route      | 50                    | You can increase this |
| table (non-propagated |                       | limit up to a maximum |
| routes)               |                       | of 100; however,      |
|                       |                       | network performance   |
|                       |                       | may be impacted. This |
|                       |                       | limit is enforced     |
|                       |                       | separately for IPv4   |
|                       |                       | routes and IPv6       |
|                       |                       | routes (50 each, and  |
|                       |                       | a maximum of 100      |
|                       |                       | each).                |
+-----------------------+-----------------------+-----------------------+
| BGP advertised routes | 100                   | This limit cannot be  |
| per route table       |                       | increased. If you     |
| (propagated routes)   |                       | require more than 100 |
|                       |                       | prefixes, advertise a |
|                       |                       | default route.        |
+-----------------------+-----------------------+-----------------------+
| Elastic IP addresses  | 5                     | This is the limit for |
| per region for        |                       | the number of Elastic |
| EC2-VPC               |                       | IP addresses for use  |
|                       |                       | in EC2-VPC. For       |
|                       |                       | Elastic IP addresses  |
|                       |                       | for EC2-Classic, see  |
|                       |                       | [Amazon Elastic       |
|                       |                       | Compute Cloud (Amazon |
|                       |                       | EC2)                  |
|                       |                       | Limits](aws_service_l |
|                       |                       | imits.html#limits_ec2 |
|                       |                       | ).                    |
+-----------------------+-----------------------+-----------------------+
| Security groups per   | 500                   | The multiple of the   |
| VPC                   |                       | number of VPCs in the |
|                       |                       | region and the number |
|                       |                       | of security groups    |
|                       |                       | per VPC cannot exceed |
|                       |                       | 5000.                 |
+-----------------------+-----------------------+-----------------------+
| Inbound or outbound   | 50                    | You can have 50       |
| rules per security    |                       | inbound and 50        |
| group                 |                       | outbound rules per    |
|                       |                       | security group        |
|                       |                       | (giving a total of    |
|                       |                       | 100 rules). To change |
|                       |                       | this limit, contact   |
|                       |                       | AWS Support â€" a     |
|                       |                       | limit change applies  |
|                       |                       | to both inbound and   |
|                       |                       | outbound rules. The   |
|                       |                       | multiple of the limit |
|                       |                       | for inbound or        |
|                       |                       | outbound rules per    |
|                       |                       | security group and    |
|                       |                       | the limit for         |
|                       |                       | security groups per   |
|                       |                       | network interface     |
|                       |                       | cannot exceed 250.    |
|                       |                       | For example, if you   |
|                       |                       | increase the limit to |
|                       |                       | 100, we decrease your |
|                       |                       | number of security    |
|                       |                       | groups per network    |
|                       |                       | interface to 2.       |
|                       |                       |                       |
|                       |                       | This limit is         |
|                       |                       | enforced separately   |
|                       |                       | for IPv4 rules and    |
|                       |                       | IPv6 rules. A rule    |
|                       |                       | that references a     |
|                       |                       | security group counts |
|                       |                       | as one rule for IPv4  |
|                       |                       | and one rule for      |
|                       |                       | IPv6.                 |
+-----------------------+-----------------------+-----------------------+
| Security groups per   | 5                     | To increase or        |
| network interface     |                       | decrease this limit,  |
|                       |                       | contact AWS Support.  |
|                       |                       | The maximum is 16.    |
|                       |                       | The multiple of the   |
|                       |                       | limit for security    |
|                       |                       | groups per network    |
|                       |                       | interface and the     |
|                       |                       | limit for rules per   |
|                       |                       | security group cannot |
|                       |                       | exceed 250. For       |
|                       |                       | example, if you       |
|                       |                       | increase the limit to |
|                       |                       | 10, we decrease your  |
|                       |                       | number of rules per   |
|                       |                       | security group to 25. |
+-----------------------+-----------------------+-----------------------+
| Network interfaces    | \-                    | This limit varies by  |
| per instance          |                       | instance type. For    |
|                       |                       | more information, see |
|                       |                       | [IP Addresses Per ENI |
|                       |                       | Per Instance          |
|                       |                       | Type](http://docs.aws |
|                       |                       | .amazon.com/AWSEC2/la |
|                       |                       | test/UserGuide/using- |
|                       |                       | eni.html#AvailableIpP |
|                       |                       | erENI).               |
+-----------------------+-----------------------+-----------------------+
| Network interfaces    | 350                   | This limit is the     |
| per region            |                       | greater of either the |
|                       |                       | default limit (350)   |
|                       |                       | or your On-Demand     |
|                       |                       | Instance limit        |
|                       |                       | multiplied by 5. The  |
|                       |                       | default limit for     |
|                       |                       | On-Demand Instances   |
|                       |                       | is 20. If your        |
|                       |                       | On-Demand Instance    |
|                       |                       | limit is below 70,    |
|                       |                       | the default limit of  |
|                       |                       | 350 applies. To       |
|                       |                       | increase this limit,  |
|                       |                       | submit a request or   |
|                       |                       | increase your         |
|                       |                       | On-Demand Instance    |
|                       |                       | limit.                |
+-----------------------+-----------------------+-----------------------+
| Network ACLs per VPC  | 200                   | You can associate one |
|                       |                       | network ACL to one or |
|                       |                       | more subnets in a     |
|                       |                       | VPC. This limit is    |
|                       |                       | not the same as the   |
|                       |                       | number of rules per   |
|                       |                       | network ACL.          |
+-----------------------+-----------------------+-----------------------+
| Rules per network ACL | 20                    | This is the one-way   |
|                       |                       | limit for a single    |
|                       |                       | network ACL, where    |
|                       |                       | the limit for ingress |
|                       |                       | rules is 20, and the  |
|                       |                       | limit for egress      |
|                       |                       | rules is 20. This     |
|                       |                       | limit includes both   |
|                       |                       | IPv4 and IPv6 rules,  |
|                       |                       | and includes the      |
|                       |                       | default deny rules    |
|                       |                       | (rule number 32767    |
|                       |                       | for IPv4 and 32768    |
|                       |                       | for IPv6, or an       |
|                       |                       | asterisk \* in the    |
|                       |                       | Amazon VPC console).  |
|                       |                       |                       |
|                       |                       | This limit can be     |
|                       |                       | increased up to a     |
|                       |                       | maximum if 40;        |
|                       |                       | however, network      |
|                       |                       | performance may be    |
|                       |                       | impacted.             |
+-----------------------+-----------------------+-----------------------+
| Active VPC peering    | 50                    | The maximum limit is  |
| connections per VPC   |                       | 125 peering           |
|                       |                       | connections per VPC.  |
|                       |                       | The number of entries |
|                       |                       | per route table       |
|                       |                       | should be increased   |
|                       |                       | accordingly; however, |
|                       |                       | network performance   |
|                       |                       | may be impacted.      |
+-----------------------+-----------------------+-----------------------+
| Outstanding VPC       | 25                    | This is the limit for |
| peering connection    |                       | the number of         |
| requests              |                       | outstanding VPC       |
|                       |                       | peering connection    |
|                       |                       | requests that you\'ve |
|                       |                       | requested from your   |
|                       |                       | account. To increase  |
|                       |                       | this limit, contact   |
|                       |                       | AWS Support.          |
+-----------------------+-----------------------+-----------------------+
| Expiry time for an    | 1 week (168 hours)    | To increase this      |
| unaccepted VPC        |                       | limit, contact AWS    |
| peering connection    |                       | Support.              |
| request               |                       |                       |
+-----------------------+-----------------------+-----------------------+
| VPC endpoints per     | 20                    | You can have 20       |
| region                |                       | interface endpoints   |
|                       |                       | and 20 gateway        |
|                       |                       | endpoints. The        |
|                       |                       | maximum limit for     |
|                       |                       | gateway endpoints is  |
|                       |                       | 255 endpoints per     |
|                       |                       | VPC, regardless of    |
|                       |                       | your endpoint limit   |
|                       |                       | per region.           |
+-----------------------+-----------------------+-----------------------+
| Flow logs per single  | 2                     | This limit cannot be  |
| network interface,    |                       | increased. You can    |
| single subnet, or     |                       | effectively have 6    |
| single VPC in a       |                       | flow logs per network |
| region                |                       | interface if you      |
|                       |                       | create 2 flow logs    |
|                       |                       | for the subnet, and 2 |
|                       |                       | flow logs for the VPC |
|                       |                       | in which your network |
|                       |                       | interface resides.    |
+-----------------------+-----------------------+-----------------------+
| NAT gateways per      | 5                     | A NAT gateway in the  |
| Availability Zone     |                       | `pending`{.code},     |
|                       |                       | `active`{.code}, or   |
|                       |                       | `deleting`{.code}     |
|                       |                       | state counts against  |
|                       |                       | your limit.           |
+-----------------------+-----------------------+-----------------------+
:::
:::

For more information about these limits, see [Amazon VPC Limits](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Appendix_Limits.html) in the *Amazon VPC User Guide*.

Amazon VPC DNS Limits {#limits-vpc-dns}
---------------------

For more information about these limits, see [DNS Limits](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-dns.html#vpc-dns-limits) in the *Amazon VPC User Guide*.

AWS WAF Limits {#limits_waf}
--------------

AWS WAF has default limits on the number of entities per account. You can [request an increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-waf) in these limits.

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Web ACLs per AWS account          | 50                                |
+-----------------------------------+-----------------------------------+
| Rules per AWS account             | 100                               |
+-----------------------------------+-----------------------------------+
| Conditions per AWS account        | 100 of each condition type (For   |
|                                   | example: 100 Size constraint      |
|                                   | conditions, 100 IP match          |
|                                   | conditions, etc.)                 |
+-----------------------------------+-----------------------------------+
| Requests per Second               | 10,000 per web ACL\*              |
+-----------------------------------+-----------------------------------+
:::
:::

\*This limit applies only to AWS WAF on an Application Load Balancer. Requests per Second (RPS) limits for AWS WAF on CloudFront are the same as the RPS limits support by CloudFront described in [the CloudFront developer guide](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html).

The following limits on AWS WAF entities can\'t be changed.

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Limit                             |
+===================================+===================================+
| Rules per web ACL                 | 10                                |
+-----------------------------------+-----------------------------------+
| Conditions per rule               | 10                                |
+-----------------------------------+-----------------------------------+
| IP address ranges (in CIDR        | 10,000                            |
| notation) per IP match condition  |                                   |
+-----------------------------------+-----------------------------------+
| Filters per cross-site scripting  | 10                                |
| match condition                   |                                   |
+-----------------------------------+-----------------------------------+
| Filters per size constraint       | 10                                |
| condition                         |                                   |
+-----------------------------------+-----------------------------------+
| Filters per SQL injection match   | 10                                |
| condition                         |                                   |
+-----------------------------------+-----------------------------------+
| Filters per string match          | 10                                |
| condition                         |                                   |
+-----------------------------------+-----------------------------------+
| In string match conditions, the   | 40                                |
| number of characters in HTTP      |                                   |
| header names, when you\'ve        |                                   |
| configured AWS WAF to inspect the |                                   |
| headers in web requests for a     |                                   |
| specified value                   |                                   |
+-----------------------------------+-----------------------------------+
| In string match conditions, the   | 50                                |
| number of characters in the value |                                   |
| that you want AWS WAF to search   |                                   |
| for                               |                                   |
+-----------------------------------+-----------------------------------+
| In regex match conditions, the    | 70                                |
| number of characters in the       |                                   |
| pattern that you want AWS WAF to  |                                   |
| search for                        |                                   |
+-----------------------------------+-----------------------------------+
:::
:::

These limits are the same for all regions in which AWS WAF is available. Each region is subject to these limits individually. That is, the limits are not cumulative across regions.

Amazon WorkMail Limits {#limits_workmail}
----------------------

For more information about these limits, see [Amazon WorkMail Limits](http://docs.aws.amazon.com/workmail/latest/adminguide/what_is.html).

Amazon WorkSpaces Limits {#limits_workspaces}
------------------------

::: {.table}

::: {.table-contents}
  Resource              Default Limit
  --------------------- ---------------
  WorkSpaces            1
  Graphics WorkSpaces   0
  Images                5
:::
:::

AWS X-Ray Limits {#limits_xray}
----------------

::: {.table}

::: {.table-contents}
+-----------------------------------+-----------------------------------+
| Resource                          | Default Limit                     |
+===================================+===================================+
| Trace and service graph retention | 30 days                           |
+-----------------------------------+-----------------------------------+
| Segment document size             | 64kB                              |
+-----------------------------------+-----------------------------------+
| Indexed annotations per trace     | 50                                |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {#js_error_message}
![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the AWS Documentation, Javascript must be enabled. Please refer to your browser\'s Help pages for instructions.
:::

::: {#main-col-footer}
::: {#doc-conventions}
[Document Conventions](/general/latest/gr/docconventions.html)
:::

::: {#next}
[Â« Previous](signature-version-2.html){.awstoc}[Next Â»](aws-ip-ranges.html){.awstoc}
:::

::: {#copyright-main-footer}
Â© 2018, Amazon Web Services, Inc. or its affiliates. All rights reserved.
:::
:::
:::
