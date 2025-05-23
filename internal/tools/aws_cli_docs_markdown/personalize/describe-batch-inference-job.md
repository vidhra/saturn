# describe-batch-inference-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-batch-inference-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-batch-inference-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [personalize](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/index.html#cli-aws-personalize) ]

# describe-batch-inference-job

## Description

Gets the properties of a batch inference job including name, Amazon Resource Name (ARN), status, input and output configurations, and the ARN of the solution version used to generate the recommendations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/personalize-2018-05-22/DescribeBatchInferenceJob)

## Synopsis

```
describe-batch-inference-job
--batch-inference-job-arn <value>
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

`--batch-inference-job-arn` (string)

The ARN of the batch inference job to describe.

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

batchInferenceJob -> (structure)

Information on the specified batch inference job.

jobName -> (string)

The name of the batch inference job.

batchInferenceJobArn -> (string)

The Amazon Resource Name (ARN) of the batch inference job.

filterArn -> (string)

The ARN of the filter used on the batch inference job.

failureReason -> (string)

If the batch inference job failed, the reason for the failure.

solutionVersionArn -> (string)

The Amazon Resource Name (ARN) of the solution version from which the batch inference job was created.

numResults -> (integer)

The number of recommendations generated by the batch inference job. This number includes the error messages generated for failed input records.

jobInput -> (structure)

The Amazon S3 path that leads to the input data used to generate the batch inference job.

s3DataSource -> (structure)

The URI of the Amazon S3 location that contains your input data. The Amazon S3 bucket must be in the same region as the API endpoint you are calling.

path -> (string)

The file path of the Amazon S3 bucket.

kmsKeyArn -> (string)

The Amazon Resource Name (ARN) of the Key Management Service (KMS) key that Amazon Personalize uses to encrypt or decrypt the input and output files.

jobOutput -> (structure)

The Amazon S3 bucket that contains the output data generated by the batch inference job.

s3DataDestination -> (structure)

Information on the Amazon S3 bucket in which the batch inference jobâs output is stored.

path -> (string)

The file path of the Amazon S3 bucket.

kmsKeyArn -> (string)

The Amazon Resource Name (ARN) of the Key Management Service (KMS) key that Amazon Personalize uses to encrypt or decrypt the input and output files.

batchInferenceJobConfig -> (structure)

A string to string map of the configuration details of a batch inference job.

itemExplorationConfig -> (map)

A string to string map specifying the exploration configuration hyperparameters, including `explorationWeight` and `explorationItemAgeCutOff` , you want to use to configure the amount of item exploration Amazon Personalize uses when recommending items. See [User-Personalization](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html) .

key -> (string)

value -> (string)

roleArn -> (string)

The ARN of the Amazon Identity and Access Management (IAM) role that requested the batch inference job.

batchInferenceJobMode -> (string)

The jobâs mode.

themeGenerationConfig -> (structure)

The jobâs theme generation settings.

fieldsForThemeGeneration -> (structure)

Fields used to generate descriptive themes for a batch inference job.

itemName -> (string)

The name of the Items dataset column that stores the name of each item in the dataset.

status -> (string)

The status of the batch inference job. The status is one of the following values:

- PENDING
- IN PROGRESS
- ACTIVE
- CREATE FAILED

creationDateTime -> (timestamp)

The time at which the batch inference job was created.

lastUpdatedDateTime -> (timestamp)

The time at which the batch inference job was last updated.