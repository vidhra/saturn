# create-model-explainability-job-definitionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-model-explainability-job-definition.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-model-explainability-job-definition.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-model-explainability-job-definition

## Description

Creates the definition for a model explainability job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateModelExplainabilityJobDefinition)

## Synopsis

```
create-model-explainability-job-definition
--job-definition-name <value>
[--model-explainability-baseline-config <value>]
--model-explainability-app-specification <value>
--model-explainability-job-input <value>
--model-explainability-job-output-config <value>
--job-resources <value>
[--network-config <value>]
--role-arn <value>
[--stopping-condition <value>]
[--tags <value>]
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

`--job-definition-name` (string)

The name of the model explainability job definition. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.

`--model-explainability-baseline-config` (structure)

The baseline configuration for a model explainability job.

BaseliningJobName -> (string)

The name of the baseline model explainability job.

ConstraintsResource -> (structure)

The constraints resource for a monitoring job.

S3Uri -> (string)

The Amazon S3 URI for the constraints resource.

Shorthand Syntax:

```
BaseliningJobName=string,ConstraintsResource={S3Uri=string}
```

JSON Syntax:

```
{
  "BaseliningJobName": "string",
  "ConstraintsResource": {
    "S3Uri": "string"
  }
}
```

`--model-explainability-app-specification` (structure)

Configures the model explainability job to run a specified Docker container image.

ImageUri -> (string)

The container image to be run by the model explainability job.

ConfigUri -> (string)

JSON formatted Amazon S3 file that defines explainability parameters. For more information on this JSON configuration file, see [Configure model explainability parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-config-json-monitor-model-explainability-parameters.html) .

Environment -> (map)

Sets the environment variables in the Docker container.

key -> (string)

value -> (string)

Shorthand Syntax:

```
ImageUri=string,ConfigUri=string,Environment={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "ImageUri": "string",
  "ConfigUri": "string",
  "Environment": {"string": "string"
    ...}
}
```

`--model-explainability-job-input` (structure)

Inputs for the model explainability job.

EndpointInput -> (structure)

Input object for the endpoint

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

JSON Syntax:

```
{
  "EndpointInput": {
    "EndpointName": "string",
    "LocalPath": "string",
    "S3InputMode": "Pipe"|"File",
    "S3DataDistributionType": "FullyReplicated"|"ShardedByS3Key",
    "FeaturesAttribute": "string",
    "InferenceAttribute": "string",
    "ProbabilityAttribute": "string",
    "ProbabilityThresholdAttribute": double,
    "StartTimeOffset": "string",
    "EndTimeOffset": "string",
    "ExcludeFeaturesAttribute": "string"
  },
  "BatchTransformInput": {
    "DataCapturedDestinationS3Uri": "string",
    "DatasetFormat": {
      "Csv": {
        "Header": true|false
      },
      "Json": {
        "Line": true|false
      },
      "Parquet": {

      }
    },
    "LocalPath": "string",
    "S3InputMode": "Pipe"|"File",
    "S3DataDistributionType": "FullyReplicated"|"ShardedByS3Key",
    "FeaturesAttribute": "string",
    "InferenceAttribute": "string",
    "ProbabilityAttribute": "string",
    "ProbabilityThresholdAttribute": double,
    "StartTimeOffset": "string",
    "EndTimeOffset": "string",
    "ExcludeFeaturesAttribute": "string"
  }
}
```

`--model-explainability-job-output-config` (structure)

The output configuration for monitoring jobs.

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

JSON Syntax:

```
{
  "MonitoringOutputs": [
    {
      "S3Output": {
        "S3Uri": "string",
        "LocalPath": "string",
        "S3UploadMode": "Continuous"|"EndOfJob"
      }
    }
    ...
  ],
  "KmsKeyId": "string"
}
```

`--job-resources` (structure)

Identifies the resources to deploy for a monitoring job.

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

Shorthand Syntax:

```
ClusterConfig={InstanceCount=integer,InstanceType=string,VolumeSizeInGB=integer,VolumeKmsKeyId=string}
```

JSON Syntax:

```
{
  "ClusterConfig": {
    "InstanceCount": integer,
    "InstanceType": "ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.8xlarge"|"ml.r5d.12xlarge"|"ml.r5d.16xlarge"|"ml.r5d.24xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge",
    "VolumeSizeInGB": integer,
    "VolumeKmsKeyId": "string"
  }
}
```

`--network-config` (structure)

Networking options for a model explainability job.

EnableInterContainerTrafficEncryption -> (boolean)

Whether to encrypt all communications between the instances used for the monitoring jobs. Choose `True` to encrypt communications. Encryption provides greater security for distributed jobs, but the processing might take longer.

EnableNetworkIsolation -> (boolean)

Whether to allow inbound and outbound network calls to and from the containers used for the monitoring job.

VpcConfig -> (structure)

Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

Shorthand Syntax:

```
EnableInterContainerTrafficEncryption=boolean,EnableNetworkIsolation=boolean,VpcConfig={SecurityGroupIds=[string,string],Subnets=[string,string]}
```

JSON Syntax:

```
{
  "EnableInterContainerTrafficEncryption": true|false,
  "EnableNetworkIsolation": true|false,
  "VpcConfig": {
    "SecurityGroupIds": ["string", ...],
    "Subnets": ["string", ...]
  }
}
```

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.

`--stopping-condition` (structure)

A time limit for how long the monitoring job is allowed to run before stopping.

MaxRuntimeInSeconds -> (integer)

The maximum runtime allowed in seconds.

### Note

The `MaxRuntimeInSeconds` cannot exceed the frequency of the job. For data quality and model explainability, this can be up to 3600 seconds for an hourly schedule. For model bias and model quality hourly schedules, this can be up to 1800 seconds.

Shorthand Syntax:

```
MaxRuntimeInSeconds=integer
```

JSON Syntax:

```
{
  "MaxRuntimeInSeconds": integer
}
```

`--tags` (list)

(Optional) An array of key-value pairs. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-whatURL) in the *Amazon Web Services Billing and Cost Management User Guide* .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

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

JobDefinitionArn -> (string)

The Amazon Resource Name (ARN) of the model explainability job.