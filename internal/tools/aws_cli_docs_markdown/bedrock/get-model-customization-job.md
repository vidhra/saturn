# get-model-customization-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/get-model-customization-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/get-model-customization-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/index.html#cli-aws-bedrock) ]

# get-model-customization-job

## Description

Retrieves the properties associated with a model-customization job, including the status of the job. For more information, see [Custom models](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-2023-04-20/GetModelCustomizationJob)

## Synopsis

```
get-model-customization-job
--job-identifier <value>
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

`--job-identifier` (string)

Identifier for the customization job.

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

jobArn -> (string)

The Amazon Resource Name (ARN) of the customization job.

jobName -> (string)

The name of the customization job.

outputModelName -> (string)

The name of the output model.

outputModelArn -> (string)

The Amazon Resource Name (ARN) of the output model.

clientRequestToken -> (string)

The token that you specified in the `CreateCustomizationJob` request.

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role.

status -> (string)

The status of the job. A successful job transitions from in-progress to completed when the output model is ready to use. If the job failed, the failure message contains information about why the job failed.

failureMessage -> (string)

Information about why the job failed.

statusDetails -> (structure)

For a Distillation job, the details about the statuses of the sub-tasks of the customization job.

validationDetails -> (structure)

The status details for the validation sub-task of the job.

status -> (string)

The status of the validation sub-task of the job.

creationTime -> (timestamp)

The start time of the validation sub-task of the job.

lastModifiedTime -> (timestamp)

The latest update to the validation sub-task of the job.

dataProcessingDetails -> (structure)

The status details for the data processing sub-task of the job.

status -> (string)

The status of the data processing sub-task of the job.

creationTime -> (timestamp)

The start time of the data processing sub-task of the job.

lastModifiedTime -> (timestamp)

The latest update to the data processing sub-task of the job.

trainingDetails -> (structure)

The status details for the training sub-task of the job.

status -> (string)

The status of the training sub-task of the job.

creationTime -> (timestamp)

The start time of the training sub-task of the job.

lastModifiedTime -> (timestamp)

The latest update to the training sub-task of the job.

creationTime -> (timestamp)

Time that the resource was created.

lastModifiedTime -> (timestamp)

Time that the resource was last modified.

endTime -> (timestamp)

Time that the resource transitioned to terminal state.

baseModelArn -> (string)

Amazon Resource Name (ARN) of the base model.

hyperParameters -> (map)

The hyperparameter values for the job. For details on the format for different models, see [Custom model hyperparameters](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html) .

key -> (string)

value -> (string)

trainingDataConfig -> (structure)

Contains information about the training dataset.

s3Uri -> (string)

The S3 URI where the training data is stored.

invocationLogsConfig -> (structure)

Settings for using invocation logs to customize a model.

usePromptResponse -> (boolean)

Whether to use the modelâs response for training, or just the prompt. The default value is `False` .

invocationLogSource -> (tagged union structure)

The source of the invocation logs.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3Uri`.

s3Uri -> (string)

The URI of an invocation log in a bucket.

requestMetadataFilters -> (tagged union structure)

Rules for filtering invocation logs based on request metadata.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `equals`, `notEquals`, `andAll`, `orAll`.

equals -> (map)

Include results where the key equals the value.

key -> (string)

value -> (string)

notEquals -> (map)

Include results where the key does not equal the value.

key -> (string)

value -> (string)

andAll -> (list)

Include results where all of the based filters match.

(structure)

A mapping of a metadata key to a value that it should or should not equal.

equals -> (map)

Include results where the key equals the value.

key -> (string)

value -> (string)

notEquals -> (map)

Include results where the key does not equal the value.

key -> (string)

value -> (string)

orAll -> (list)

Include results where any of the base filters match.

(structure)

A mapping of a metadata key to a value that it should or should not equal.

equals -> (map)

Include results where the key equals the value.

key -> (string)

value -> (string)

notEquals -> (map)

Include results where the key does not equal the value.

key -> (string)

value -> (string)

validationDataConfig -> (structure)

Contains information about the validation dataset.

validators -> (list)

Information about the validators.

(structure)

Information about a validator.

s3Uri -> (string)

The S3 URI where the validation data is stored.

outputDataConfig -> (structure)

Output data configuration

s3Uri -> (string)

The S3 URI where the output data is stored.

customizationType -> (string)

The type of model customization.

outputModelKmsKeyArn -> (string)

The custom model is encrypted at rest using this key.

trainingMetrics -> (structure)

Contains training metrics from the job creation.

trainingLoss -> (float)

Loss metric associated with the custom job.

validationMetrics -> (list)

The loss metric for each validator that you provided in the createjob request.

(structure)

The metric for the validator.

validationLoss -> (float)

The validation loss associated with this validator.

vpcConfig -> (structure)

VPC configuration for the custom model job.

subnetIds -> (list)

An array of IDs for each subnet in the VPC to use.

(string)

securityGroupIds -> (list)

An array of IDs for each security group in the VPC to use.

(string)

customizationConfig -> (tagged union structure)

The customization configuration for the model customization job.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `distillationConfig`.

distillationConfig -> (structure)

The Distillation configuration for the custom model.

teacherModelConfig -> (structure)

The teacher model configuration.

teacherModelIdentifier -> (string)

The identifier of the teacher model.

maxResponseLengthForInference -> (integer)

The maximum number of tokens requested when the customization job invokes the teacher model.