# create-optimization-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-optimization-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-optimization-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-optimization-job

## Description

Creates a job that optimizes a model for inference performance. To create the job, you provide the location of a source model, and you provide the settings for the optimization techniques that you want the job to apply. When the job completes successfully, SageMaker uploads the new optimized model to the output destination that you specify.

For more information about how to use this action, and about the supported optimization techniques, see [Optimize model inference with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateOptimizationJob)

## Synopsis

```
create-optimization-job
--optimization-job-name <value>
--role-arn <value>
--model-source <value>
--deployment-instance-type <value>
[--optimization-environment <value>]
--optimization-configs <value>
--output-config <value>
--stopping-condition <value>
[--tags <value>]
[--vpc-config <value>]
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

`--optimization-job-name` (string)

A custom name for the new optimization job.

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker AI to perform tasks on your behalf.

During model optimization, Amazon SageMaker AI needs your permission to:

- Read input data from an S3 bucket
- Write model artifacts to an S3 bucket
- Write logs to Amazon CloudWatch Logs
- Publish metrics to Amazon CloudWatch

You grant permissions for all of these tasks to an IAM role. To pass this role to Amazon SageMaker AI, the caller of this API must have the `iam:PassRole` permission. For more information, see [Amazon SageMaker AI Roles.](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html)

`--model-source` (structure)

The location of the source model to optimize with an optimization job.

S3 -> (structure)

The Amazon S3 location of a source model to optimize with an optimization job.

S3Uri -> (string)

An Amazon S3 URI that locates a source model to optimize with an optimization job.

ModelAccessConfig -> (structure)

The access configuration settings for the source ML model for an optimization job, where you can accept the model end-user license agreement (EULA).

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

Shorthand Syntax:

```
S3={S3Uri=string,ModelAccessConfig={AcceptEula=boolean}}
```

JSON Syntax:

```
{
  "S3": {
    "S3Uri": "string",
    "ModelAccessConfig": {
      "AcceptEula": true|false
    }
  }
}
```

`--deployment-instance-type` (string)

The type of instance that hosts the optimized model that you create with the optimization job.

Possible values:

- `ml.p4d.24xlarge`
- `ml.p4de.24xlarge`
- `ml.p5.48xlarge`
- `ml.g5.xlarge`
- `ml.g5.2xlarge`
- `ml.g5.4xlarge`
- `ml.g5.8xlarge`
- `ml.g5.12xlarge`
- `ml.g5.16xlarge`
- `ml.g5.24xlarge`
- `ml.g5.48xlarge`
- `ml.g6.xlarge`
- `ml.g6.2xlarge`
- `ml.g6.4xlarge`
- `ml.g6.8xlarge`
- `ml.g6.12xlarge`
- `ml.g6.16xlarge`
- `ml.g6.24xlarge`
- `ml.g6.48xlarge`
- `ml.g6e.xlarge`
- `ml.g6e.2xlarge`
- `ml.g6e.4xlarge`
- `ml.g6e.8xlarge`
- `ml.g6e.12xlarge`
- `ml.g6e.16xlarge`
- `ml.g6e.24xlarge`
- `ml.g6e.48xlarge`
- `ml.inf2.xlarge`
- `ml.inf2.8xlarge`
- `ml.inf2.24xlarge`
- `ml.inf2.48xlarge`
- `ml.trn1.2xlarge`
- `ml.trn1.32xlarge`
- `ml.trn1n.32xlarge`

`--optimization-environment` (map)

The environment variables to set in the model container.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--optimization-configs` (list)

Settings for each of the optimization techniques that the job applies.

(tagged union structure)

Settings for an optimization technique that you apply with a model optimization job.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ModelQuantizationConfig`, `ModelCompilationConfig`, `ModelShardingConfig`.

ModelQuantizationConfig -> (structure)

Settings for the model quantization technique thatâs applied by a model optimization job.

Image -> (string)

The URI of an LMI DLC in Amazon ECR. SageMaker uses this image to run the optimization.

OverrideEnvironment -> (map)

Environment variables that override the default ones in the model container.

key -> (string)

value -> (string)

ModelCompilationConfig -> (structure)

Settings for the model compilation technique thatâs applied by a model optimization job.

Image -> (string)

The URI of an LMI DLC in Amazon ECR. SageMaker uses this image to run the optimization.

OverrideEnvironment -> (map)

Environment variables that override the default ones in the model container.

key -> (string)

value -> (string)

ModelShardingConfig -> (structure)

Settings for the model sharding technique thatâs applied by a model optimization job.

Image -> (string)

The URI of an LMI DLC in Amazon ECR. SageMaker uses this image to run the optimization.

OverrideEnvironment -> (map)

Environment variables that override the default ones in the model container.

key -> (string)

value -> (string)

Shorthand Syntax:

```
ModelQuantizationConfig={Image=string,OverrideEnvironment={KeyName1=string,KeyName2=string}},ModelCompilationConfig={Image=string,OverrideEnvironment={KeyName1=string,KeyName2=string}},ModelShardingConfig={Image=string,OverrideEnvironment={KeyName1=string,KeyName2=string}} ...
```

JSON Syntax:

```
[
  {
    "ModelQuantizationConfig": {
      "Image": "string",
      "OverrideEnvironment": {"string": "string"
        ...}
    },
    "ModelCompilationConfig": {
      "Image": "string",
      "OverrideEnvironment": {"string": "string"
        ...}
    },
    "ModelShardingConfig": {
      "Image": "string",
      "OverrideEnvironment": {"string": "string"
        ...}
    }
  }
  ...
]
```

`--output-config` (structure)

Details for where to store the optimized model that you create with the optimization job.

KmsKeyId -> (string)

The Amazon Resource Name (ARN) of a key in Amazon Web Services KMS. SageMaker uses they key to encrypt the artifacts of the optimized model when SageMaker uploads the model to Amazon S3.

S3OutputLocation -> (string)

The Amazon S3 URI for where to store the optimized model that you create with an optimization job.

Shorthand Syntax:

```
KmsKeyId=string,S3OutputLocation=string
```

JSON Syntax:

```
{
  "KmsKeyId": "string",
  "S3OutputLocation": "string"
}
```

`--stopping-condition` (structure)

Specifies a limit to how long a job can run. When the job reaches the time limit, SageMaker ends the job. Use this API to cap costs.

To stop a training job, SageMaker sends the algorithm the `SIGTERM` signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost.

The training algorithms provided by SageMaker automatically save the intermediate results of a model training job when possible. This attempt to save artifacts is only a best effort case as model might not be in a state from which it can be saved. For example, if training has just started, the model might not be ready to save. When saved, this intermediate data is a valid model artifact. You can use it to create a model with `CreateModel` .

### Note

The Neural Topic Model (NTM) currently does not support saving intermediate model artifacts. When training NTMs, make sure that the maximum runtime is sufficient for the training job to complete.

MaxRuntimeInSeconds -> (integer)

The maximum length of time, in seconds, that a training or compilation job can run before it is stopped.

For compilation jobs, if the job does not complete during this time, a `TimeOut` error is generated. We recommend starting with 900 seconds and increasing as necessary based on your model.

For all other jobs, if the job does not complete during this time, SageMaker ends the job. When `RetryStrategy` is specified in the job request, `MaxRuntimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt. The default value is 1 day. The maximum value is 28 days.

The maximum time that a `TrainingJob` can run in total, including any time spent publishing metrics or archiving and uploading models after it has been stopped, is 30 days.

MaxWaitTimeInSeconds -> (integer)

The maximum length of time, in seconds, that a managed Spot training job has to complete. It is the amount of time spent waiting for Spot capacity plus the amount of time the job can run. It must be equal to or greater than `MaxRuntimeInSeconds` . If the job does not complete during this time, SageMaker ends the job.

When `RetryStrategy` is specified in the job request, `MaxWaitTimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt.

MaxPendingTimeInSeconds -> (integer)

The maximum length of time, in seconds, that a training or compilation job can be pending before it is stopped.

### Note

When working with training jobs that use capacity from [training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html) , not all `Pending` job states count against the `MaxPendingTimeInSeconds` limit. The following scenarios do not increment the `MaxPendingTimeInSeconds` counter:

- The plan is in a `Scheduled` state: Jobs queued (in `Pending` status) before a planâs start date (waiting for scheduled start time)
- Between capacity reservations: Jobs temporarily back to `Pending` status between two capacity reservation periods

`MaxPendingTimeInSeconds` only increments when jobs are actively waiting for capacity in an `Active` plan.

Shorthand Syntax:

```
MaxRuntimeInSeconds=integer,MaxWaitTimeInSeconds=integer,MaxPendingTimeInSeconds=integer
```

JSON Syntax:

```
{
  "MaxRuntimeInSeconds": integer,
  "MaxWaitTimeInSeconds": integer,
  "MaxPendingTimeInSeconds": integer
}
```

`--tags` (list)

A list of key-value pairs associated with the optimization job. For more information, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference Guide* .

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

`--vpc-config` (structure)

A VPC in Amazon VPC that your optimized model has access to.

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your optimized model.

(string)

Shorthand Syntax:

```
SecurityGroupIds=string,string,Subnets=string,string
```

JSON Syntax:

```
{
  "SecurityGroupIds": ["string", ...],
  "Subnets": ["string", ...]
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

OptimizationJobArn -> (string)

The Amazon Resource Name (ARN) of the optimization job.