# describe-modelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/describe-model.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/describe-model.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutvision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/index.html#cli-aws-lookoutvision) ]

# describe-model

## Description

Describes a version of an Amazon Lookout for Vision model.

This operation requires permissions to perform the `lookoutvision:DescribeModel` operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutvision-2020-11-20/DescribeModel)

## Synopsis

```
describe-model
--project-name <value>
--model-version <value>
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

`--project-name` (string)

The project that contains the version of a model that you want to describe.

`--model-version` (string)

The version of the model that you want to describe.

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

ModelDescription -> (structure)

Contains the description of the model.

ModelVersion -> (string)

The version of the model

ModelArn -> (string)

The Amazon Resource Name (ARN) of the model.

CreationTimestamp -> (timestamp)

The unix timestamp for the date and time that the model was created.

Description -> (string)

The description for the model.

Status -> (string)

The status of the model.

StatusMessage -> (string)

The status message for the model.

Performance -> (structure)

Performance metrics for the model. Created during training.

F1Score -> (float)

The overall F1 score metric for the trained model.

Recall -> (float)

The overall recall metric value for the trained model.

Precision -> (float)

The overall precision metric value for the trained model.

OutputConfig -> (structure)

The S3 location where Amazon Lookout for Vision saves model training files.

S3Location -> (structure)

The S3 location for the output.

Bucket -> (string)

The S3 bucket that contains the training or model packaging job output. If you are training a model, the bucket must in your AWS account. If you use an S3 bucket for a model packaging job, the S3 bucket must be in the same AWS Region and AWS account in which you use AWS IoT Greengrass.

Prefix -> (string)

The path of the folder, within the S3 bucket, that contains the output.

EvaluationManifest -> (structure)

The S3 location where Amazon Lookout for Vision saves the manifest file that was used to test the trained model and generate the performance scores.

Bucket -> (string)

The bucket that contains the training output.

Key -> (string)

The location of the training output in the bucket.

EvaluationResult -> (structure)

The S3 location where Amazon Lookout for Vision saves the performance metrics.

Bucket -> (string)

The bucket that contains the training output.

Key -> (string)

The location of the training output in the bucket.

EvaluationEndTimestamp -> (timestamp)

The unix timestamp for the date and time that the evaluation ended.

KmsKeyId -> (string)

The identifer for the AWS Key Management Service (AWS KMS) key that was used to encrypt the model during training.

MinInferenceUnits -> (integer)

The minimum number of inference units used by the model. For more information, see  StartModel

MaxInferenceUnits -> (integer)

The maximum number of inference units Amazon Lookout for Vision uses to auto-scale the model. For more information, see  StartModel .