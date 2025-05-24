# describe-language-modelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/describe-language-model.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/describe-language-model.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transcribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/index.html#cli-aws-transcribe) ]

# describe-language-model

## Description

Provides information about the specified custom language model.

This operation also shows if the base language model that you used to create your custom language model has been updated. If Amazon Transcribe has updated the base model, you can create a new custom language model using the updated base model.

If you tried to create a new custom language model and the request wasnât successful, you can use `DescribeLanguageModel` to help identify the reason for this failure.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/DescribeLanguageModel)

## Synopsis

```
describe-language-model
--model-name <value>
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

`--model-name` (string)

The name of the custom language model you want information about. Model names are case sensitive.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To get information about a specific custom language model**

The following `describe-language-model` example gets information about a specific custom language model. For example, under BaseModelName you can see whether your model is trained using a NarrowBand or WideBand model. Custom language models with a NarrowBand base model can transcribe audio with a sample rate less than 16 kHz. Language models using a WideBand base model can transcribe audio with a sample rate greater than 16 kHz. The S3Uri parameter indicates the Amazon S3 prefix youâve used to access the training data to create the custom language model.

```
aws transcribe describe-language-model \
    --model-name cli-clm-example
```

Output:

```
{
    "LanguageModel": {
        "ModelName": "cli-clm-example",
        "CreateTime": "2020-09-25T17:57:38.504000+00:00",
        "LastModifiedTime": "2020-09-25T17:57:48.585000+00:00",
        "LanguageCode": "language-code",
        "BaseModelName": "base-model-name",
        "ModelStatus": "IN_PROGRESS",
        "UpgradeAvailability": false,
        "InputDataConfig": {
            "S3Uri": "s3://amzn-s3-demo-bucket/Amazon-S3-Prefix/",
            "TuningDataS3Uri": "s3://amzn-s3-demo-bucket/Amazon-S3-Prefix/",
            "DataAccessRoleArn": "arn:aws:iam::AWS-account-number:role/IAM-role-with-permissions-to-create-a-custom-language-model"
        }
    }
}
```

For more information, see [Improving Domain-Specific Transcription Accuracy with Custom Language Models](https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html) in the *Amazon Transcribe Developer Guide*.

## Output

LanguageModel -> (structure)

Provides information about the specified custom language model.

This parameter also shows if the base language model you used to create your custom language model has been updated. If Amazon Transcribe has updated the base model, you can create a new custom language model using the updated base model.

If you tried to create a new custom language model and the request wasnât successful, you can use this `DescribeLanguageModel` to help identify the reason for this failure.

ModelName -> (string)

A unique name, chosen by you, for your custom language model.

This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account.

CreateTime -> (timestamp)

The date and time the specified custom language model was created.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.761000-07:00` represents 12:32 PM UTC-7 on May 4, 2022.

LastModifiedTime -> (timestamp)

The date and time the specified custom language model was last modified.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.761000-07:00` represents 12:32 PM UTC-7 on May 4, 2022.

LanguageCode -> (string)

The language code used to create your custom language model. Each custom language model must contain terms in only one language, and the language you select for your custom language model must match the language of your training and tuning data.

For a list of supported languages and their associated language codes, refer to the [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) table. Note that US English (`en-US` ) is the only language supported with Amazon Transcribe Medical.

BaseModelName -> (string)

The Amazon Transcribe standard language model, or base model, used to create your custom language model.

ModelStatus -> (string)

The status of the specified custom language model. When the status displays as `COMPLETED` the model is ready for use.

UpgradeAvailability -> (boolean)

Shows if a more current base model is available for use with the specified custom language model.

If `false` , your custom language model is using the most up-to-date base model.

If `true` , there is a newer base model available than the one your language model is using.

Note that to update a base model, you must recreate the custom language model using the new base model. Base model upgrades for existing custom language models are not supported.

FailureReason -> (string)

If `ModelStatus` is `FAILED` , `FailureReason` contains information about why the custom language model request failed. See also: [Common Errors](https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html) .

InputDataConfig -> (structure)

The Amazon S3 location of the input files used to train and tune your custom language model, in addition to the data access role ARN (Amazon Resource Name) that has permissions to access these data.

S3Uri -> (string)

The Amazon S3 location (URI) of the text files you want to use to train your custom language model.

Hereâs an example URI path: `s3://DOC-EXAMPLE-BUCKET/my-model-training-data/`

TuningDataS3Uri -> (string)

The Amazon S3 location (URI) of the text files you want to use to tune your custom language model.

Hereâs an example URI path: `s3://DOC-EXAMPLE-BUCKET/my-model-tuning-data/`

DataAccessRoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files. If the role that you specify doesnât have the appropriate permissions to access the specified Amazon S3 location, your request fails.

IAM role ARNs have the format `arn:partition:iam::account:role/role-name-with-path` . For example: `arn:aws:iam::111122223333:role/Admin` .

For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) .