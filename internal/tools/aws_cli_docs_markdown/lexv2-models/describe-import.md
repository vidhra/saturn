# describe-importÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/describe-import.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/describe-import.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# describe-import

## Description

Gets information about a specific import.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/DescribeImport)

## Synopsis

```
describe-import
--import-id <value>
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

`--import-id` (string)

The unique identifier of the import to describe.

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

importId -> (string)

The unique identifier of the described import.

resourceSpecification -> (structure)

The specifications of the imported bot, bot locale, or custom vocabulary.

botImportSpecification -> (structure)

Parameters for importing a bot.

botName -> (string)

The name that Amazon Lex should use for the bot.

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role used to build and run the bot.

dataPrivacy -> (structure)

By default, data stored by Amazon Lex is encrypted. The `DataPrivacy` structure provides settings that determine how Amazon Lex handles special cases of securing the data for your bot.

childDirected -> (boolean)

For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Childrenâs Online Privacy Protection Act (COPPA) by specifying `true` or `false` in the `childDirected` field. By specifying `true` in the `childDirected` field, you confirm that your use of Amazon Lex **is** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying `false` in the `childDirected` field, you confirm that your use of Amazon Lex **is not** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the `childDirected` field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the [Amazon Lex FAQ](http://aws.amazon.com/lex/faqs#data-security) .

errorLogSettings -> (structure)

Allows you to configure destinations where error logs will be published during the bot import process.

enabled -> (boolean)

Settings parameters for the error logs, when it is enabled.

idleSessionTTLInSeconds -> (integer)

The time, in seconds, that Amazon Lex should keep information about a userâs conversation with the bot.

A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.

You can specify between 60 (1 minute) and 86,400 (24 hours) seconds.

botTags -> (map)

A list of tags to add to the bot. You can only add tags when you import a bot. You canât use the `UpdateBot` operation to update tags. To update tags, use the `TagResource` operation.

key -> (string)

value -> (string)

testBotAliasTags -> (map)

A list of tags to add to the test alias for a bot. You can only add tags when you import a bot. You canât use the `UpdateAlias` operation to update tags. To update tags on the test alias, use the `TagResource` operation.

key -> (string)

value -> (string)

botLocaleImportSpecification -> (structure)

Parameters for importing a bot locale.

botId -> (string)

The identifier of the bot to import the locale to.

botVersion -> (string)

The version of the bot to import the locale to. This can only be the `DRAFT` version of the bot.

localeId -> (string)

The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html) .

nluIntentConfidenceThreshold -> (double)

Determines the threshold where Amazon Lex will insert the `AMAZON.FallbackIntent` , `AMAZON.KendraSearchIntent` , or both when returning alternative intents. `AMAZON.FallbackIntent` and `AMAZON.KendraSearchIntent` are only inserted if they are configured for the bot.

For example, suppose a bot is configured with the confidence threshold of 0.80 and the `AMAZON.FallbackIntent` . Amazon Lex returns three alternative intents with the following confidence scores: IntentA (0.70), IntentB (0.60), IntentC (0.50). The response from the `PostText` operation would be:

- `AMAZON.FallbackIntent`
- `IntentA`
- `IntentB`
- `IntentC`

voiceSettings -> (structure)

Defines settings for using an Amazon Polly voice to communicate with a user.

Valid values include:

- `standard`
- `neural`
- `long-form`
- `generative`

voiceId -> (string)

The identifier of the Amazon Polly voice to use.

engine -> (string)

Indicates the type of Amazon Polly voice that Amazon Lex should use for voice interaction with the user. For more information, see the ` `engine` parameter of the `SynthesizeSpeech` operation <[https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#polly-SynthesizeSpeech-request-Engine](https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#polly-SynthesizeSpeech-request-Engine)>`__ in the *Amazon Polly developer guide* .

If you do not specify a value, the default is `standard` .

customVocabularyImportSpecification -> (structure)

Provides the parameters required for importing a custom vocabulary.

botId -> (string)

The identifier of the bot to import the custom vocabulary to.

botVersion -> (string)

The version of the bot to import the custom vocabulary to.

localeId -> (string)

The identifier of the local to import the custom vocabulary to. The value must be `en_GB` .

testSetImportResourceSpecification -> (structure)

Specifications for the test set that is imported.

testSetName -> (string)

The name of the test set.

description -> (string)

The description of the test set.

roleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that has permission to access the test set.

storageLocation -> (structure)

Contains information about the location that Amazon Lex uses to store the test-set.

s3BucketName -> (string)

The name of the Amazon S3 bucket in which the test set is stored.

s3Path -> (string)

The path inside the Amazon S3 bucket where the test set is stored.

kmsKeyArn -> (string)

The Amazon Resource Name (ARN) of an Amazon Web Services Key Management Service (KMS) key for encrypting the test set.

importInputLocation -> (structure)

Contains information about the input location from where test-set should be imported.

s3BucketName -> (string)

The name of the Amazon S3 bucket.

s3Path -> (string)

The path inside the Amazon S3 bucket pointing to the test-set CSV file.

modality -> (string)

Specifies whether the test-set being imported contains written or spoken data.

testSetTags -> (map)

A list of tags to add to the test set. You can only add tags when you import/generate a new test set. You canât use the `UpdateTestSet` operation to update tags. To update tags, use the `TagResource` operation.

key -> (string)

value -> (string)

importedResourceId -> (string)

The unique identifier that Amazon Lex assigned to the resource created by the import.

importedResourceName -> (string)

The name of the imported resource.

mergeStrategy -> (string)

The strategy used when there was a name conflict between the imported resource and an existing resource. When the merge strategy is `FailOnConflict` existing resources are not overwritten and the import fails.

importStatus -> (string)

The status of the import process. When the status is `Completed` the resource is imported and ready for use.

failureReasons -> (list)

If the `importStatus` field is `Failed` , this provides one or more reasons for the failure.

(string)

creationDateTime -> (timestamp)

The date and time that the import was created.

lastUpdatedDateTime -> (timestamp)

The date and time that the import was last updated.