# get-applicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-serverless/get-application.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-serverless/get-application.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr-serverless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-serverless/index.html#cli-aws-emr-serverless) ]

# get-application

## Description

Displays detailed information about a specified application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/emr-serverless-2021-07-13/GetApplication)

## Synopsis

```
get-application
--application-id <value>
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--application-id` (string)

The ID of the application that will be described.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Output

application -> (structure)

The output displays information about the specified application.

applicationId -> (string)

The ID of the application.

name -> (string)

The name of the application.

arn -> (string)

The ARN of the application.

releaseLabel -> (string)

The Amazon EMR release associated with the application.

type -> (string)

The type of application, such as Spark or Hive.

state -> (string)

The state of the application.

stateDetails -> (string)

The state details of the application.

initialCapacity -> (map)

The initial capacity of the application.

key -> (string)

Worker type for an analytics framework.

value -> (structure)

The initial capacity configuration per worker.

workerCount -> (long)

The number of workers in the initial capacity configuration.

workerConfiguration -> (structure)

The resource configuration of the initial capacity configuration.

cpu -> (string)

The CPU requirements for every worker instance of the worker type.

memory -> (string)

The memory requirements for every worker instance of the worker type.

disk -> (string)

The disk requirements for every worker instance of the worker type.

diskType -> (string)

The disk type for every worker instance of the work type. Shuffle optimized disks have higher performance characteristics and are better for shuffle heavy workloads. Default is `STANDARD` .

maximumCapacity -> (structure)

The maximum capacity of the application. This is cumulative across all workers at any given point in time during the lifespan of the application is created. No new resources will be created once any one of the defined limits is hit.

cpu -> (string)

The maximum allowed CPU for an application.

memory -> (string)

The maximum allowed resources for an application.

disk -> (string)

The maximum allowed disk for an application.

createdAt -> (timestamp)

The date and time when the application run was created.

updatedAt -> (timestamp)

The date and time when the application run was last updated.

tags -> (map)

The tags assigned to the application.

key -> (string)

value -> (string)

autoStartConfiguration -> (structure)

The configuration for an application to automatically start on job submission.

enabled -> (boolean)

Enables the application to automatically start on job submission. Defaults to true.

autoStopConfiguration -> (structure)

The configuration for an application to automatically stop after a certain amount of time being idle.

enabled -> (boolean)

Enables the application to automatically stop after a certain amount of time being idle. Defaults to true.

idleTimeoutMinutes -> (integer)

The amount of idle time in minutes after which your application will automatically stop. Defaults to 15 minutes.

networkConfiguration -> (structure)

The network configuration for customer VPC connectivity for the application.

subnetIds -> (list)

The array of subnet Ids for customer VPC connectivity.

(string)

securityGroupIds -> (list)

The array of security group Ids for customer VPC connectivity.

(string)

architecture -> (string)

The CPU architecture of an application.

imageConfiguration -> (structure)

The image configuration applied to all worker types.

imageUri -> (string)

The image URI.

resolvedImageDigest -> (string)

The SHA256 digest of the image URI. This indicates which specific image the application is configured for. The image digest doesnât exist until an application has started.

workerTypeSpecifications -> (map)

The specification applied to each worker type.

key -> (string)

Worker type for an analytics framework.

value -> (structure)

The specifications for a worker type.

imageConfiguration -> (structure)

The image configuration for a worker type.

imageUri -> (string)

The image URI.

resolvedImageDigest -> (string)

The SHA256 digest of the image URI. This indicates which specific image the application is configured for. The image digest doesnât exist until an application has started.

runtimeConfiguration -> (list)

The [Configuration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html) specifications of an application. Each configuration consists of a classification and properties. You use this parameter when creating or updating an application. To see the runtimeConfiguration object of an application, run the [GetApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetApplication.html) API operation.

(structure)

A configuration specification to be used when provisioning an application. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file.

classification -> (string)

The classification within a configuration.

properties -> (map)

A set of properties specified within a configuration classification.

key -> (string)

value -> (string)

configurations -> (list)

A list of additional configurations to apply within a configuration object.

(structure)

A configuration specification to be used when provisioning an application. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file.

classification -> (string)

The classification within a configuration.

properties -> (map)

A set of properties specified within a configuration classification.

key -> (string)

value -> (string)

monitoringConfiguration -> (structure)

The configuration setting for monitoring.

s3MonitoringConfiguration -> (structure)

The Amazon S3 configuration for monitoring log publishing.

logUri -> (string)

The Amazon S3 destination URI for log publishing.

encryptionKeyArn -> (string)

The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.

managedPersistenceMonitoringConfiguration -> (structure)

The managed log persistence configuration for a job run.

enabled -> (boolean)

Enables managed logging and defaults to true. If set to false, managed logging will be turned off.

encryptionKeyArn -> (string)

The KMS key ARN to encrypt the logs stored in managed log persistence.

cloudWatchLoggingConfiguration -> (structure)

The Amazon CloudWatch configuration for monitoring logs. You can configure your jobs to send log information to CloudWatch.

enabled -> (boolean)

Enables CloudWatch logging.

logGroupName -> (string)

The name of the log group in Amazon CloudWatch Logs where you want to publish your logs.

logStreamNamePrefix -> (string)

Prefix for the CloudWatch log stream name.

encryptionKeyArn -> (string)

The Key Management Service (KMS) key ARN to encrypt the logs that you store in CloudWatch Logs.

logTypes -> (map)

The types of logs that you want to publish to CloudWatch. If you donât specify any log types, driver STDOUT and STDERR logs will be published to CloudWatch Logs by default. For more information including the supported worker types for Hive and Spark, see [Logging for EMR Serverless with CloudWatch](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/logging.html#jobs-log-storage-cw) .

- **Key Valid Values** : `SPARK_DRIVER` , `SPARK_EXECUTOR` , `HIVE_DRIVER` , `TEZ_TASK`
- **Array Members Valid Values** : `STDOUT` , `STDERR` , `HIVE_LOG` , `TEZ_AM` , `SYSTEM_LOGS`

key -> (string)

Worker type for an analytics framework.

value -> (list)

(string)

Log type for a Spark/Hive job-run.

prometheusMonitoringConfiguration -> (structure)

The monitoring configuration object you can configure to send metrics to Amazon Managed Service for Prometheus for a job run.

remoteWriteUrl -> (string)

The remote write URL in the Amazon Managed Service for Prometheus workspace to send metrics to.

interactiveConfiguration -> (structure)

The interactive configuration object that enables the interactive use cases for an application.

studioEnabled -> (boolean)

Enables you to connect an application to Amazon EMR Studio to run interactive workloads in a notebook.

livyEndpointEnabled -> (boolean)

Enables an Apache Livy endpoint that you can connect to and run interactive jobs.

schedulerConfiguration -> (structure)

The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.

queueTimeoutMinutes -> (integer)

The maximum duration in minutes for the job in QUEUED state. If scheduler configuration is enabled on your application, the default value is 360 minutes (6 hours). The valid range is from 15 to 720.

maxConcurrentRuns -> (integer)

The maximum concurrent job runs on this application. If scheduler configuration is enabled on your application, the default value is 15. The valid range is 1 to 1000.