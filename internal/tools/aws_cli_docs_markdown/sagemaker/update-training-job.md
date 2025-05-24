# update-training-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-training-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-training-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# update-training-job

## Description

Update a model training job to request a new Debugger profiling configuration or to change warm pool retention length.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateTrainingJob)

## Synopsis

```
update-training-job
--training-job-name <value>
[--profiler-config <value>]
[--profiler-rule-configurations <value>]
[--resource-config <value>]
[--remote-debug-config <value>]
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

`--training-job-name` (string)

The name of a training job to update the Debugger profiling configuration.

`--profiler-config` (structure)

Configuration information for Amazon SageMaker Debugger system monitoring, framework profiling, and storage paths.

S3OutputPath -> (string)

Path to Amazon S3 storage location for system and framework metrics.

ProfilingIntervalInMilliseconds -> (long)

A time interval for capturing system metrics in milliseconds. Available values are 100, 200, 500, 1000 (1 second), 5000 (5 seconds), and 60000 (1 minute) milliseconds. The default value is 500 milliseconds.

ProfilingParameters -> (map)

Configuration information for capturing framework metrics. Available key strings for different profiling options are `DetailedProfilingConfig` , `PythonProfilingConfig` , and `DataLoaderProfilingConfig` . The following codes are configuration structures for the `ProfilingParameters` parameter. To learn more about how to configure the `ProfilingParameters` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html) .

key -> (string)

value -> (string)

DisableProfiler -> (boolean)

To turn off Amazon SageMaker Debugger monitoring and profiling while a training job is in progress, set to `True` .

Shorthand Syntax:

```
S3OutputPath=string,ProfilingIntervalInMilliseconds=long,ProfilingParameters={KeyName1=string,KeyName2=string},DisableProfiler=boolean
```

JSON Syntax:

```
{
  "S3OutputPath": "string",
  "ProfilingIntervalInMilliseconds": long,
  "ProfilingParameters": {"string": "string"
    ...},
  "DisableProfiler": true|false
}
```

`--profiler-rule-configurations` (list)

Configuration information for Amazon SageMaker Debugger rules for profiling system and framework metrics.

(structure)

Configuration information for profiling rules.

RuleConfigurationName -> (string)

The name of the rule configuration. It must be unique relative to other rule configuration names.

LocalPath -> (string)

Path to local storage location for output of rules. Defaults to `/opt/ml/processing/output/rule/` .

S3OutputPath -> (string)

Path to Amazon S3 storage location for rules.

RuleEvaluatorImage -> (string)

The Amazon Elastic Container Registry Image for the managed rule evaluation.

InstanceType -> (string)

The instance type to deploy a custom rule for profiling a training job.

VolumeSizeInGB -> (integer)

The size, in GB, of the ML storage volume attached to the processing instance.

RuleParameters -> (map)

Runtime configuration for rule container.

key -> (string)

value -> (string)

Shorthand Syntax:

```
RuleConfigurationName=string,LocalPath=string,S3OutputPath=string,RuleEvaluatorImage=string,InstanceType=string,VolumeSizeInGB=integer,RuleParameters={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "RuleConfigurationName": "string",
    "LocalPath": "string",
    "S3OutputPath": "string",
    "RuleEvaluatorImage": "string",
    "InstanceType": "ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.8xlarge"|"ml.r5d.12xlarge"|"ml.r5d.16xlarge"|"ml.r5d.24xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge",
    "VolumeSizeInGB": integer,
    "RuleParameters": {"string": "string"
      ...}
  }
  ...
]
```

`--resource-config` (structure)

The training job `ResourceConfig` to update warm pool retention length.

KeepAlivePeriodInSeconds -> (integer)

The `KeepAlivePeriodInSeconds` value specified in the `ResourceConfig` to update.

Shorthand Syntax:

```
KeepAlivePeriodInSeconds=integer
```

JSON Syntax:

```
{
  "KeepAlivePeriodInSeconds": integer
}
```

`--remote-debug-config` (structure)

Configuration for remote debugging while the training job is running. You can update the remote debugging configuration when the `SecondaryStatus` of the job is `Downloading` or `Training` .To learn more about the remote debugging functionality of SageMaker, see [Access a training container through Amazon Web Services Systems Manager (SSM) for remote debugging](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-debugging.html) .

EnableRemoteDebug -> (boolean)

If set to True, enables remote debugging.

Shorthand Syntax:

```
EnableRemoteDebug=boolean
```

JSON Syntax:

```
{
  "EnableRemoteDebug": true|false
}
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

TrainingJobArn -> (string)

The Amazon Resource Name (ARN) of the training job.