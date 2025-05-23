# create-bot-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/create-bot-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/create-bot-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lex-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/index.html#cli-aws-lex-models) ]

# create-bot-version

## Description

Creates a new version of the bot based on the `$LATEST` version. If the `$LATEST` version of this resource hasnât changed since you created the last version, Amazon Lex doesnât create a new version. It returns the last created version.

### Note

You can update only the `$LATEST` version of the bot. You canât update the numbered versions that you create with the `CreateBotVersion` operation.

When you create the first version of a bot, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see  versioning-intro .

This operation requires permission for the `lex:CreateBotVersion` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/CreateBotVersion)

## Synopsis

```
create-bot-version
--name <value>
[--checksum <value>]
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

`--name` (string)

The name of the bot that you want to create a new version of. The name is case sensitive.

`--checksum` (string)

Identifies a specific revision of the `$LATEST` version of the bot. If you specify a checksum and the `$LATEST` version of the bot has a different checksum, a `PreconditionFailedException` exception is returned and Amazon Lex doesnât publish a new version. If you donât specify a checksum, Amazon Lex publishes the `$LATEST` version.

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

name -> (string)

The name of the bot.

description -> (string)

A description of the bot.

intents -> (list)

An array of `Intent` objects. For more information, see  PutBot .

(structure)

Identifies the specific version of an intent.

intentName -> (string)

The name of the intent.

intentVersion -> (string)

The version of the intent.

clarificationPrompt -> (structure)

The message that Amazon Lex uses when it doesnât understand the userâs request. For more information, see  PutBot .

messages -> (list)

An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(structure)

The message object that provides the message text and its type.

contentType -> (string)

The content type of the message string.

content -> (string)

The text of the message.

groupNumber -> (integer)

Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.

maxAttempts -> (integer)

The number of times to prompt the user for information.

responseCard -> (string)

A response card. Amazon Lex uses this prompt at runtime, in the `PostText` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .

abortStatement -> (structure)

The message that Amazon Lex uses to cancel a conversation. For more information, see  PutBot .

messages -> (list)

A collection of message objects.

(structure)

The message object that provides the message text and its type.

contentType -> (string)

The content type of the message string.

content -> (string)

The text of the message.

groupNumber -> (integer)

Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.

responseCard -> (string)

At runtime, if the client is using the [PostText](http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html) API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.

status -> (string)

When you send a request to create or update a bot, Amazon Lex sets the `status` response element to `BUILDING` . After Amazon Lex builds the bot, it sets `status` to `READY` . If Amazon Lex canât build the bot, it sets `status` to `FAILED` . Amazon Lex returns the reason for the failure in the `failureReason` response element.

failureReason -> (string)

If `status` is `FAILED` , Amazon Lex provides the reason that it failed to build the bot.

lastUpdatedDate -> (timestamp)

The date when the `$LATEST` version of this bot was updated.

createdDate -> (timestamp)

The date when the bot version was created.

idleSessionTTLInSeconds -> (integer)

The maximum time in seconds that Amazon Lex retains the data gathered in a conversation. For more information, see  PutBot .

voiceId -> (string)

The Amazon Polly voice ID that Amazon Lex uses for voice interactions with the user.

checksum -> (string)

Checksum identifying the version of the bot that was created.

version -> (string)

The version of the bot.

locale -> (string)

Specifies the target locale for the bot.

childDirected -> (boolean)

For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Childrenâs Online Privacy Protection Act (COPPA) by specifying `true` or `false` in the `childDirected` field. By specifying `true` in the `childDirected` field, you confirm that your use of Amazon Lex **is** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying `false` in the `childDirected` field, you confirm that your use of Amazon Lex **is not** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the `childDirected` field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.

If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the [Amazon Lex FAQ.](https://aws.amazon.com/lex/faqs#data-security)

enableModelImprovements -> (boolean)

Indicates whether the bot uses accuracy improvements. `true` indicates that the bot is using the improvements, otherwise, `false` .

detectSentiment -> (boolean)

Indicates whether utterances entered by the user should be sent to Amazon Comprehend for sentiment analysis.