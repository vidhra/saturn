# put-botÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-bot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-bot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lex-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/index.html#cli-aws-lex-models) ]

# put-bot

## Description

Creates an Amazon Lex conversational bot or replaces an existing bot. When you create or update a bot you are only required to specify a name, a locale, and whether the bot is directed toward children under age 13. You can use this to add intents later, or to remove intents from an existing bot. When you create a bot with the minimum information, the bot is created or updated but Amazon Lex returns the response `FAILED` . You can build the bot after you add one or more intents. For more information about Amazon Lex bots, see  how-it-works .

If you specify the name of an existing bot, the fields in the request replace the existing values in the `$LATEST` version of the bot. Amazon Lex removes any fields that you donât provide values for in the request, except for the `idleTTLInSeconds` and `privacySettings` fields, which are set to their default values. If you donât specify values for required fields, Amazon Lex throws an exception.

This operation requires permissions for the `lex:PutBot` action. For more information, see  security-iam .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/PutBot)

## Synopsis

```
put-bot
--name <value>
[--description <value>]
[--intents <value>]
[--enable-model-improvements | --no-enable-model-improvements]
[--nlu-intent-confidence-threshold <value>]
[--clarification-prompt <value>]
[--abort-statement <value>]
[--idle-session-ttl-in-seconds <value>]
[--voice-id <value>]
[--checksum <value>]
[--process-behavior <value>]
--locale <value>
--child-directed | --no-child-directed
[--detect-sentiment | --no-detect-sentiment]
[--create-version | --no-create-version]
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

`--name` (string)

The name of the bot. The name is *not* case sensitive.

`--description` (string)

A description of the bot.

`--intents` (list)

An array of `Intent` objects. Each intent represents a command that a user can express. For example, a pizza ordering bot might support an OrderPizza intent. For more information, see  how-it-works .

(structure)

Identifies the specific version of an intent.

intentName -> (string)

The name of the intent.

intentVersion -> (string)

The version of the intent.

Shorthand Syntax:

```
intentName=string,intentVersion=string ...
```

JSON Syntax:

```
[
  {
    "intentName": "string",
    "intentVersion": "string"
  }
  ...
]
```

`--enable-model-improvements` | `--no-enable-model-improvements` (boolean)

Set to `true` to enable access to natural language understanding improvements.

When you set the `enableModelImprovements` parameter to `true` you can use the `nluIntentConfidenceThreshold` parameter to configure confidence scores. For more information, see [Confidence Scores](https://docs.aws.amazon.com/lex/latest/dg/confidence-scores.html) .

You can only set the `enableModelImprovements` parameter in certain Regions. If you set the parameter to `true` , your bot has access to accuracy improvements.

The Regions where you can set the `enableModelImprovements` parameter to `true` are:

- US East (N. Virginia) (us-east-1)
- US West (Oregon) (us-west-2)
- Asia Pacific (Sydney) (ap-southeast-2)
- EU (Ireland) (eu-west-1)

In other Regions, the `enableModelImprovements` parameter is set to `true` by default. In these Regions setting the parameter to `false` throws a `ValidationException` exception.

`--nlu-intent-confidence-threshold` (double)

Determines the threshold where Amazon Lex will insert the `AMAZON.FallbackIntent` , `AMAZON.KendraSearchIntent` , or both when returning alternative intents in a [PostContent](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html) or [PostText](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html) response. `AMAZON.FallbackIntent` and `AMAZON.KendraSearchIntent` are only inserted if they are configured for the bot.

You must set the `enableModelImprovements` parameter to `true` to use confidence scores in the following regions.

- US East (N. Virginia) (us-east-1)
- US West (Oregon) (us-west-2)
- Asia Pacific (Sydney) (ap-southeast-2)
- EU (Ireland) (eu-west-1)

In other Regions, the `enableModelImprovements` parameter is set to `true` by default.

For example, suppose a bot is configured with the confidence threshold of 0.80 and the `AMAZON.FallbackIntent` . Amazon Lex returns three alternative intents with the following confidence scores: IntentA (0.70), IntentB (0.60), IntentC (0.50). The response from the `PostText` operation would be:

- AMAZON.FallbackIntent
- IntentA
- IntentB
- IntentC

`--clarification-prompt` (structure)

When Amazon Lex doesnât understand the userâs intent, it uses this message to get clarification. To specify how many times Amazon Lex should repeat the clarification prompt, use the `maxAttempts` field. If Amazon Lex still doesnât understand, it sends the message in the `abortStatement` field.

When you create a clarification prompt, make sure that it suggests the correct response from the user. for example, for a bot that orders pizza and drinks, you might create this clarification prompt: âWhat would you like to do? You can say âOrder a pizzaâ or âOrder a drink.ââ

If you have defined a fallback intent, it will be invoked if the clarification prompt is repeated the number of times defined in the `maxAttempts` field. For more information, see [AMAZON.FallbackIntent](https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-fallback.html) .

If you donât define a clarification prompt, at runtime Amazon Lex will return a 400 Bad Request exception in three cases:

- Follow-up prompt - When the user responds to a follow-up prompt but does not provide an intent. For example, in response to a follow-up prompt that says âWould you like anything else today?â the user says âYes.â Amazon Lex will return a 400 Bad Request exception because it does not have a clarification prompt to send to the user to get an intent.
- Lambda function - When using a Lambda function, you return an `ElicitIntent` dialog type. Since Amazon Lex does not have a clarification prompt to get an intent from the user, it returns a 400 Bad Request exception.
- PutSession operation - When using the `PutSession` operation, you send an `ElicitIntent` dialog type. Since Amazon Lex does not have a clarification prompt to get an intent from the user, it returns a 400 Bad Request exception.

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

Shorthand Syntax:

```
messages=[{contentType=string,content=string,groupNumber=integer},{contentType=string,content=string,groupNumber=integer}],maxAttempts=integer,responseCard=string
```

JSON Syntax:

```
{
  "messages": [
    {
      "contentType": "PlainText"|"SSML"|"CustomPayload",
      "content": "string",
      "groupNumber": integer
    }
    ...
  ],
  "maxAttempts": integer,
  "responseCard": "string"
}
```

`--abort-statement` (structure)

When Amazon Lex canât understand the userâs input in context, it tries to elicit the information a few times. After that, Amazon Lex sends the message defined in `abortStatement` to the user, and then cancels the conversation. To set the number of retries, use the `valueElicitationPrompt` field for the slot type.

For example, in a pizza ordering bot, Amazon Lex might ask a user âWhat type of crust would you like?â If the userâs response is not one of the expected responses (for example, âthin crust, âdeep dish,â etc.), Amazon Lex tries to elicit a correct response a few more times.

For example, in a pizza ordering application, `OrderPizza` might be one of the intents. This intent might require the `CrustType` slot. You specify the `valueElicitationPrompt` field when you create the `CrustType` slot.

If you have defined a fallback intent the cancel statement will not be sent to the user, the fallback intent is used instead. For more information, see [AMAZON.FallbackIntent](https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-fallback.html) .

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

Shorthand Syntax:

```
messages=[{contentType=string,content=string,groupNumber=integer},{contentType=string,content=string,groupNumber=integer}],responseCard=string
```

JSON Syntax:

```
{
  "messages": [
    {
      "contentType": "PlainText"|"SSML"|"CustomPayload",
      "content": "string",
      "groupNumber": integer
    }
    ...
  ],
  "responseCard": "string"
}
```

`--idle-session-ttl-in-seconds` (integer)

The maximum time in seconds that Amazon Lex retains the data gathered in a conversation.

A user interaction session remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.

For example, suppose that a user chooses the OrderPizza intent, but gets sidetracked halfway through placing an order. If the user doesnât complete the order within the specified time, Amazon Lex discards the slot information that it gathered, and the user must start over.

If you donât include the `idleSessionTTLInSeconds` element in a `PutBot` operation request, Amazon Lex uses the default value. This is also true if the request replaces an existing bot.

The default is 300 seconds (5 minutes).

`--voice-id` (string)

The Amazon Polly voice ID that you want Amazon Lex to use for voice interactions with the user. The locale configured for the voice must match the locale of the bot. For more information, see [Voices in Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html) in the *Amazon Polly Developer Guide* .

`--checksum` (string)

Identifies a specific revision of the `$LATEST` version.

When you create a new bot, leave the `checksum` field blank. If you specify a checksum you get a `BadRequestException` exception.

When you want to update a bot, set the `checksum` field to the checksum of the most recent revision of the `$LATEST` version. If you donât specify the `checksum` field, or if the checksum does not match the `$LATEST` version, you get a `PreconditionFailedException` exception.

`--process-behavior` (string)

If you set the `processBehavior` element to `BUILD` , Amazon Lex builds the bot so that it can be run. If you set the element to `SAVE` Amazon Lex saves the bot, but doesnât build it.

If you donât specify this value, the default value is `BUILD` .

Possible values:

- `SAVE`
- `BUILD`

`--locale` (string)

Specifies the target locale for the bot. Any intent used in the bot must be compatible with the locale of the bot.

The default is `en-US` .

Possible values:

- `de-DE`
- `en-AU`
- `en-GB`
- `en-IN`
- `en-US`
- `es-419`
- `es-ES`
- `es-US`
- `fr-FR`
- `fr-CA`
- `it-IT`
- `ja-JP`
- `ko-KR`

`--child-directed` | `--no-child-directed` (boolean)

For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Childrenâs Online Privacy Protection Act (COPPA) by specifying `true` or `false` in the `childDirected` field. By specifying `true` in the `childDirected` field, you confirm that your use of Amazon Lex **is** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying `false` in the `childDirected` field, you confirm that your use of Amazon Lex **is not** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the `childDirected` field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.

If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the [Amazon Lex FAQ.](https://aws.amazon.com/lex/faqs#data-security)

`--detect-sentiment` | `--no-detect-sentiment` (boolean)

When set to `true` user utterances are sent to Amazon Comprehend for sentiment analysis. If you donât specify `detectSentiment` , the default is `false` .

`--create-version` | `--no-create-version` (boolean)

When set to `true` a new numbered version of the bot is created. This is the same as calling the `CreateBotVersion` operation. If you donât specify `createVersion` , the default is `false` .

`--tags` (list)

A list of tags to add to the bot. You can only add tags when you create a bot, you canât use the `PutBot` operation to update the tags on a bot. To update tags, use the `TagResource` operation.

(structure)

A list of key/value pairs that identify a bot, bot alias, or bot channel. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

key -> (string)

The key for the tag. Keys are not case-sensitive and must be unique.

value -> (string)

The value associated with a key. The value may be an empty string but it canât be null.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
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

enableModelImprovements -> (boolean)

Indicates whether the bot uses accuracy improvements. `true` indicates that the bot is using the improvements, otherwise, `false` .

nluIntentConfidenceThreshold -> (double)

The score that determines where Amazon Lex inserts the `AMAZON.FallbackIntent` , `AMAZON.KendraSearchIntent` , or both when returning alternative intents in a [PostContent](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html) or [PostText](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html) response. `AMAZON.FallbackIntent` is inserted if the confidence score for all intents is below this value. `AMAZON.KendraSearchIntent` is only inserted if it is configured for the bot.

clarificationPrompt -> (structure)

The prompts that Amazon Lex uses when it doesnât understand the userâs intent. For more information, see  PutBot .

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

When you send a request to create a bot with `processBehavior` set to `BUILD` , Amazon Lex sets the `status` response element to `BUILDING` .

In the `READY_BASIC_TESTING` state you can test the bot with user inputs that exactly match the utterances configured for the botâs intents and values in the slot types.

If Amazon Lex canât build the bot, Amazon Lex sets `status` to `FAILED` . Amazon Lex returns the reason for the failure in the `failureReason` response element.

When you set `processBehavior` to `SAVE` , Amazon Lex sets the status code to `NOT BUILT` .

When the bot is in the `READY` state you can test and publish the bot.

failureReason -> (string)

If `status` is `FAILED` , Amazon Lex provides the reason that it failed to build the bot.

lastUpdatedDate -> (timestamp)

The date that the bot was updated. When you create a resource, the creation date and last updated date are the same.

createdDate -> (timestamp)

The date that the bot was created.

idleSessionTTLInSeconds -> (integer)

The maximum length of time that Amazon Lex retains the data gathered in a conversation. For more information, see  PutBot .

voiceId -> (string)

The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user. For more information, see  PutBot .

checksum -> (string)

Checksum of the bot that you created.

version -> (string)

The version of the bot. For a new bot, the version is always `$LATEST` .

locale -> (string)

The target locale for the bot.

childDirected -> (boolean)

For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Childrenâs Online Privacy Protection Act (COPPA) by specifying `true` or `false` in the `childDirected` field. By specifying `true` in the `childDirected` field, you confirm that your use of Amazon Lex **is** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying `false` in the `childDirected` field, you confirm that your use of Amazon Lex **is not** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the `childDirected` field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.

If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the [Amazon Lex FAQ.](https://aws.amazon.com/lex/faqs#data-security)

createVersion -> (boolean)

`True` if a new version of the bot was created. If the `createVersion` field was not specified in the request, the `createVersion` field is set to false in the response.

detectSentiment -> (boolean)

`true` if the bot is configured to send user utterances to Amazon Comprehend for sentiment analysis. If the `detectSentiment` field was not specified in the request, the `detectSentiment` field is `false` in the response.

tags -> (list)

A list of tags associated with the bot.

(structure)

A list of key/value pairs that identify a bot, bot alias, or bot channel. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

key -> (string)

The key for the tag. Keys are not case-sensitive and must be unique.

value -> (string)

The value associated with a key. The value may be an empty string but it canât be null.