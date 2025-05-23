# describe-monitoring-scheduleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-monitoring-schedule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-monitoring-schedule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-monitoring-schedule

## Description

Describes the schedule for a monitoring job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeMonitoringSchedule)

## Synopsis

```
describe-monitoring-schedule
--monitoring-schedule-name <value>
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

`--monitoring-schedule-name` (string)

Name of a previously created monitoring schedule.

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

MonitoringScheduleArn -> (string)

The Amazon Resource Name (ARN) of the monitoring schedule.

MonitoringScheduleName -> (string)

Name of the monitoring schedule.

MonitoringScheduleStatus -> (string)

The status of an monitoring job.

MonitoringType -> (string)

The type of the monitoring job that this schedule runs. This is one of the following values.

- `DATA_QUALITY` - The schedule is for a data quality monitoring job.
- `MODEL_QUALITY` - The schedule is for a model quality monitoring job.
- `MODEL_BIAS` - The schedule is for a bias monitoring job.
- `MODEL_EXPLAINABILITY` - The schedule is for an explainability monitoring job.

FailureReason -> (string)

A string, up to one KB in size, that contains the reason a monitoring job failed, if it failed.

CreationTime -> (timestamp)

The time at which the monitoring job was created.

LastModifiedTime -> (timestamp)

The time at which the monitoring job was last modified.

MonitoringScheduleConfig -> (structure)

The configuration object that specifies the monitoring schedule and defines the monitoring job.

ScheduleConfig -> (structure)

Configures the monitoring schedule.

ScheduleExpression -> (string)

A cron expression that describes details about the monitoring schedule.

The supported cron expressions are:

- If you want to set the job to start every hour, use the following:  `Hourly: cron(0 * ? * * *)`
- If you want to start the job daily:  `cron(0 [00-23] ? * * *)`
- If you want to run the job one time, immediately, use the following keyword:  `NOW`

For example, the following are valid cron expressions:

- Daily at noon UTC: `cron(0 12 ? * * *)`
- Daily at midnight UTC: `cron(0 0 ? * * *)`

To support running every 6, 12 hours, the following are also supported:

`cron(0 [00-23]/[01-24] ? * * *)`

For example, the following are valid cron expressions:

- Every 12 hours, starting at 5pm UTC: `cron(0 17/12 ? * * *)`
- Every two hours starting at midnight: `cron(0 0/2 ? * * *)`

### Note

- Even though the cron expression is set to start at 5PM UTC, note that there could be a delay of 0-20 minutes from the actual requested time to run the execution.
- We recommend that if you would like a daily schedule, you do not provide this parameter. Amazon SageMaker AI will pick a time for running every day.

You can also specify the keyword `NOW` to run the monitoring job immediately, one time, without recurring.

DataAnalysisStartTime -> (string)

Sets the start time for a monitoring job window. Express this time as an offset to the times that you schedule your monitoring jobs to run. You schedule monitoring jobs with the `ScheduleExpression` parameter. Specify this offset in ISO 8601 duration format. For example, if you want to monitor the five hours of data in your dataset that precede the start of each monitoring job, you would specify: `"-PT5H"` .

The start time that you specify must not precede the end time that you specify by more than 24 hours. You specify the end time with the `DataAnalysisEndTime` parameter.

If you set `ScheduleExpression` to `NOW` , this parameter is required.

DataAnalysisEndTime -> (string)

Sets the end time for a monitoring job window. Express this time as an offset to the times that you schedule your monitoring jobs to run. You schedule monitoring jobs with the `ScheduleExpression` parameter. Specify this offset in ISO 8601 duration format. For example, if you want to end the window one hour before the start of each monitoring job, you would specify: `"-PT1H"` .

The end time that you specify must not follow the start time that you specify by more than 24 hours. You specify the start time with the `DataAnalysisStartTime` parameter.

If you set `ScheduleExpression` to `NOW` , this parameter is required.

MonitoringJobDefinition -> (structure)

Defines the monitoring job.

BaselineConfig -> (structure)

Baseline configuration used to validate that the data conforms to the specified constraints and statistics

BaseliningJobName -> (string)

The name of the job that performs baselining for the monitoring job.

ConstraintsResource -> (structure)

The baseline constraint file in Amazon S3 that the current monitoring job should validated against.

S3Uri -> (string)

The Amazon S3 URI for the constraints resource.

StatisticsResource -> (structure)

The baseline statistics file in Amazon S3 that the current monitoring job should be validated against.

S3Uri -> (string)

The Amazon S3 URI for the statistics resource.

MonitoringInputs -> (list)

The array of inputs for the monitoring job. Currently we support monitoring an Amazon SageMaker AI Endpoint.

(structure)

The inputs for a monitoring job.

EndpointInput -> (structure)

The endpoint for a monitoring job.

EndpointName -> (string)

An endpoint in customerâs account which has enabled `DataCaptureConfig` enabled.

LocalPath -> (string)

Path to the filesystem where the endpoint data is available to the container.

S3InputMode -> (string)

Whether the `Pipe` or `File` is used as the input mode for transferring data for the monitoring job. `Pipe` mode is recommended for large datasets. `File` mode is useful for small files that fit in memory. Defaults to `File` .

S3DataDistributionType -> (string)

Whether input data distributed in Amazon S3 is fully replicated or sharded by an Amazon S3 key. Defaults to `FullyReplicated`

FeaturesAttribute -> (string)

The attributes of the input data that are the input features.

InferenceAttribute -> (string)

The attribute of the input data that represents the ground truth label.

ProbabilityAttribute -> (string)

In a classification problem, the attribute that represents the class probability.

ProbabilityThresholdAttribute -> (double)

The threshold for the class probability to be evaluated as a positive result.

StartTimeOffset -> (string)

If specified, monitoring jobs substract this time from the start time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html) .

EndTimeOffset -> (string)

If specified, monitoring jobs substract this time from the end time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html) .

ExcludeFeaturesAttribute -> (string)

The attributes of the input data to exclude from the analysis.

BatchTransformInput -> (structure)

Input object for the batch transform job.

DataCapturedDestinationS3Uri -> (string)

The Amazon S3 location being used to capture the data.

DatasetFormat -> (structure)

The dataset format for your batch transform job.

Csv -> (structure)

The CSV dataset used in the monitoring job.

Header -> (boolean)

Indicates if the CSV data has a header.

Json -> (structure)

The JSON dataset used in the monitoring job

Line -> (boolean)

Indicates if the file should be read as a JSON object per line.

Parquet -> (structure)

The Parquet dataset used in the monitoring job

LocalPath -> (string)

Path to the filesystem where the batch transform data is available to the container.

S3InputMode -> (string)

Whether the `Pipe` or `File` is used as the input mode for transferring data for the monitoring job. `Pipe` mode is recommended for large datasets. `File` mode is useful for small files that fit in memory. Defaults to `File` .

S3DataDistributionType -> (string)

Whether input data distributed in Amazon S3 is fully replicated or sharded by an S3 key. Defaults to `FullyReplicated`

FeaturesAttribute -> (string)

The attributes of the input data that are the input features.

InferenceAttribute -> (string)

The attribute of the input data that represents the ground truth label.

ProbabilityAttribute -> (string)

In a classification problem, the attribute that represents the class probability.

ProbabilityThresholdAttribute -> (double)

The threshold for the class probability to be evaluated as a positive result.

StartTimeOffset -> (string)

If specified, monitoring jobs substract this time from the start time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html) .

EndTimeOffset -> (string)

If specified, monitoring jobs subtract this time from the end time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html) .

ExcludeFeaturesAttribute -> (string)

The attributes of the input data to exclude from the analysis.

MonitoringOutputConfig -> (structure)

The array of outputs from the monitoring job to be uploaded to Amazon S3.

MonitoringOutputs -> (list)

Monitoring outputs for monitoring jobs. This is where the output of the periodic monitoring jobs is uploaded.

(structure)

The output object for a monitoring job.

S3Output -> (structure)

The Amazon S3 storage location where the results of a monitoring job are saved.

S3Uri -> (string)

A URI that identifies the Amazon S3 storage location where Amazon SageMaker AI saves the results of a monitoring job.

LocalPath -> (string)

The local path to the Amazon S3 storage location where Amazon SageMaker AI saves the results of a monitoring job. LocalPath is an absolute path for the output data.

S3UploadMode -> (string)

Whether to upload the results of the monitoring job continuously or after the job completes.

KmsKeyId -> (string)

The Key Management Service (KMS) key that Amazon SageMaker AI uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.

MonitoringResources -> (structure)

Identifies the resources, ML compute instances, and ML storage volumes to deploy for a monitoring job. In distributed processing, you specify more than one instance.

ClusterConfig -> (structure)

The configuration for the cluster resources used to run the processing job.

InstanceCount -> (integer)

The number of ML compute instances to use in the model monitoring job. For distributed processing jobs, specify a value greater than 1. The default value is 1.

InstanceType -> (string)

The ML compute instance type for the processing job.

VolumeSizeInGB -> (integer)

The size of the ML storage volume, in gigabytes, that you want to provision. You must specify sufficient ML storage for your scenario.

VolumeKmsKeyId -> (string)

The Key Management Service (KMS) key that Amazon SageMaker AI uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the model monitoring job.

MonitoringAppSpecification -> (structure)

Configures the monitoring job to run a specified Docker container image.

ImageUri -> (string)

The container image to be run by the monitoring job.

ContainerEntrypoint -> (list)

Specifies the entrypoint for a container used to run the monitoring job.

(string)

ContainerArguments -> (list)

An array of arguments for the container used to run the monitoring job.

(string)

RecordPreprocessorSourceUri -> (string)

An Amazon S3 URI to a script that is called per row prior to running analysis. It can base64 decode the payload and convert it into a flattened JSON so that the built-in container can use the converted data. Applicable only for the built-in (first party) containers.

PostAnalyticsProcessorSourceUri -> (string)

An Amazon S3 URI to a script that is called after analysis has been performed. Applicable only for the built-in (first party) containers.

StoppingCondition -> (structure)

Specifies a time limit for how long the monitoring job is allowed to run.

MaxRuntimeInSeconds -> (integer)

The maximum runtime allowed in seconds.

### Note

The `MaxRuntimeInSeconds` cannot exceed the frequency of the job. For data quality and model explainability, this can be up to 3600 seconds for an hourly schedule. For model bias and model quality hourly schedules, this can be up to 1800 seconds.

Environment -> (map)

Sets the environment variables in the Docker container.

key -> (string)

value -> (string)

NetworkConfig -> (structure)

Specifies networking options for an monitoring job.

EnableInterContainerTrafficEncryption -> (boolean)

Whether to encrypt all communications between distributed processing jobs. Choose `True` to encrypt communications. Encryption provides greater security for distributed processing jobs, but the processing might take longer.

EnableNetworkIsolation -> (boolean)

Whether to allow inbound and outbound network calls to and from the containers used for the processing job.

VpcConfig -> (structure)

Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

RoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.

MonitoringJobDefinitionName -> (string)

The name of the monitoring job definition to schedule.

MonitoringType -> (string)

The type of the monitoring job definition to schedule.

EndpointName -> (string)

The name of the endpoint for the monitoring job.

LastMonitoringExecutionSummary -> (structure)

Describes metadata on the last execution to run, if there was one.

MonitoringScheduleName -> (string)

The name of the monitoring schedule.

ScheduledTime -> (timestamp)

The time the monitoring job was scheduled.

CreationTime -> (timestamp)

The time at which the monitoring job was created.

LastModifiedTime -> (timestamp)

A timestamp that indicates the last time the monitoring job was modified.

MonitoringExecutionStatus -> (string)

The status of the monitoring job.

ProcessingJobArn -> (string)

The Amazon Resource Name (ARN) of the monitoring job.

EndpointName -> (string)

The name of the endpoint used to run the monitoring job.

FailureReason -> (string)

Contains the reason a monitoring job failed, if it failed.

MonitoringJobDefinitionName -> (string)

The name of the monitoring job.

MonitoringType -> (string)

The type of the monitoring job.