# put-sessionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/put-session.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/put-session.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lex-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/index.html#cli-aws-lex-runtime) ]

# put-session

## Description

Creates a new session or modifies an existing session with an Amazon Lex bot. Use this operation to enable your application to set the state of the bot.

For more information, see [Managing Sessions](https://docs.aws.amazon.com/lex/latest/dg/how-session-api.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/runtime.lex-2016-11-28/PutSession)

## Synopsis

```
put-session
--bot-name <value>
--bot-alias <value>
--user-id <value>
[--session-attributes <value>]
[--dialog-action <value>]
[--recent-intent-summary-view <value>]
[--accept <value>]
[--active-contexts <value>]
<outfile>
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

`--bot-name` (string)

The name of the bot that contains the session data.

`--bot-alias` (string)

The alias in use for the bot that contains the session data.

`--user-id` (string)

The ID of the client application user. Amazon Lex uses this to identify a userâs conversation with your bot.

`--session-attributes` (map)

Map of key/value pairs representing the session-specific context information. It contains application information passed between Amazon Lex and a client application.

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

`--dialog-action` (structure)

Sets the next action that the bot should take to fulfill the conversation.

type -> (string)

The next action that the bot should take in its interaction with the user. The possible values are:

- `ConfirmIntent` - The next action is asking the user if the intent is complete and ready to be fulfilled. This is a yes/no question such as âPlace the order?â
- `Close` - Indicates that the there will not be a response from the user. For example, the statement âYour order has been placedâ does not require a response.
- `Delegate` - The next action is determined by Amazon Lex.
- `ElicitIntent` - The next action is to determine the intent that the user wants to fulfill.
- `ElicitSlot` - The next action is to elicit a slot value from the user.

intentName -> (string)

The name of the intent.

slots -> (map)

Map of the slots that have been gathered and their values.

key -> (string)

value -> (string)

slotToElicit -> (string)

The name of the slot that should be elicited from the user.

fulfillmentState -> (string)

The fulfillment state of the intent. The possible values are:

- `Failed` - The Lambda function associated with the intent failed to fulfill the intent.
- `Fulfilled` - The intent has fulfilled by the Lambda function associated with the intent.
- `ReadyForFulfillment` - All of the information necessary for the intent is present and the intent ready to be fulfilled by the client application.

message -> (string)

The message that should be shown to the user. If you donât specify a message, Amazon Lex will use the message configured for the intent.

messageFormat -> (string)

- `PlainText` - The message contains plain UTF-8 text.
- `CustomPayload` - The message is a custom format for the client.
- `SSML` - The message contains text formatted for voice output.
- `Composite` - The message contains an escaped JSON object containing one or more messages. For more information, see [Message Groups](https://docs.aws.amazon.com/lex/latest/dg/howitworks-manage-prompts.html) .

Shorthand Syntax:

```
type=string,intentName=string,slots={KeyName1=string,KeyName2=string},slotToElicit=string,fulfillmentState=string,message=string,messageFormat=string
```

JSON Syntax:

```
{
  "type": "ElicitIntent"|"ConfirmIntent"|"ElicitSlot"|"Close"|"Delegate",
  "intentName": "string",
  "slots": {"string": "string"
    ...},
  "slotToElicit": "string",
  "fulfillmentState": "Fulfilled"|"Failed"|"ReadyForFulfillment",
  "message": "string",
  "messageFormat": "PlainText"|"CustomPayload"|"SSML"|"Composite"
}
```

`--recent-intent-summary-view` (list)

A summary of the recent intents for the bot. You can use the intent summary view to set a checkpoint label on an intent and modify attributes of intents. You can also use it to remove or add intent summary objects to the list.

An intent that you modify or add to the list must make sense for the bot. For example, the intent name must be valid for the bot. You must provide valid values for:

- `intentName`
- slot names
- `slotToElict`

If you send the `recentIntentSummaryView` parameter in a `PutSession` request, the contents of the new summary view replaces the old summary view. For example, if a `GetSession` request returns three intents in the summary view and you call `PutSession` with one intent in the summary view, the next call to `GetSession` will only return one intent.

(structure)

Provides information about the state of an intent. You can use this information to get the current state of an intent so that you can process the intent, or so that you can return the intent to its previous state.

intentName -> (string)

The name of the intent.

checkpointLabel -> (string)

A user-defined label that identifies a particular intent. You can use this label to return to a previous intent.

Use the `checkpointLabelFilter` parameter of the `GetSessionRequest` operation to filter the intents returned by the operation to those with only the specified label.

slots -> (map)

Map of the slots that have been gathered and their values.

key -> (string)

value -> (string)

confirmationStatus -> (string)

The status of the intent after the user responds to the confirmation prompt. If the user confirms the intent, Amazon Lex sets this field to `Confirmed` . If the user denies the intent, Amazon Lex sets this value to `Denied` . The possible values are:

- `Confirmed` - The user has responded âYesâ to the confirmation prompt, confirming that the intent is complete and that it is ready to be fulfilled.
- `Denied` - The user has responded âNoâ to the confirmation prompt.
- `None` - The user has never been prompted for confirmation; or, the user was prompted but did not confirm or deny the prompt.

dialogActionType -> (string)

The next action that the bot should take in its interaction with the user. The possible values are:

- `ConfirmIntent` - The next action is asking the user if the intent is complete and ready to be fulfilled. This is a yes/no question such as âPlace the order?â
- `Close` - Indicates that the there will not be a response from the user. For example, the statement âYour order has been placedâ does not require a response.
- `ElicitIntent` - The next action is to determine the intent that the user wants to fulfill.
- `ElicitSlot` - The next action is to elicit a slot value from the user.

fulfillmentState -> (string)

The fulfillment state of the intent. The possible values are:

- `Failed` - The Lambda function associated with the intent failed to fulfill the intent.
- `Fulfilled` - The intent has fulfilled by the Lambda function associated with the intent.
- `ReadyForFulfillment` - All of the information necessary for the intent is present and the intent ready to be fulfilled by the client application.

slotToElicit -> (string)

The next slot to elicit from the user. If there is not slot to elicit, the field is blank.

Shorthand Syntax:

```
intentName=string,checkpointLabel=string,slots={KeyName1=string,KeyName2=string},confirmationStatus=string,dialogActionType=string,fulfillmentState=string,slotToElicit=string ...
```

JSON Syntax:

```
[
  {
    "intentName": "string",
    "checkpointLabel": "string",
    "slots": {"string": "string"
      ...},
    "confirmationStatus": "None"|"Confirmed"|"Denied",
    "dialogActionType": "ElicitIntent"|"ConfirmIntent"|"ElicitSlot"|"Close"|"Delegate",
    "fulfillmentState": "Fulfilled"|"Failed"|"ReadyForFulfillment",
    "slotToElicit": "string"
  }
  ...
]
```

`--accept` (string)

The message that Amazon Lex returns in the response can be either text or speech based depending on the value of this field.

- If the value is `text/plain; charset=utf-8` , Amazon Lex returns text in the response.
- If the value begins with `audio/` , Amazon Lex returns speech in the response. Amazon Lex uses Amazon Polly to generate the speech in the configuration that you specify. For example, if you specify `audio/mpeg` as the value, Amazon Lex returns speech in the MPEG format.
- If the value is `audio/pcm` , the speech is returned as `audio/pcm` in 16-bit, little endian format.
- The following are the accepted values:
- `audio/mpeg`
- `audio/ogg`
- `audio/pcm`
- `audio/*` (defaults to mpeg)
- `text/plain; charset=utf-8`

`--active-contexts` (list)

A list of contexts active for the request. A context can be activated when a previous intent is fulfilled, or by including the context in the request,

If you donât specify a list of contexts, Amazon Lex will use the current list of contexts for the session. If you specify an empty list, all contexts for the session are cleared.

(structure)

A context is a variable that contains information about the current state of the conversation between a user and Amazon Lex. Context can be set automatically by Amazon Lex when an intent is fulfilled, or it can be set at runtime using the `PutContent` , `PutText` , or `PutSession` operation.

name -> (string)

The name of the context.

timeToLive -> (structure)

The length of time or number of turns that a context remains active.

timeToLiveInSeconds -> (integer)

The number of seconds that the context should be active after it is first sent in a `PostContent` or `PostText` response. You can set the value between 5 and 86,400 seconds (24 hours).

turnsToLive -> (integer)

The number of conversation turns that the context should be active. A conversation turn is one `PostContent` or `PostText` request and the corresponding response from Amazon Lex.

parameters -> (map)

State variables for the current context. You can use these values as default values for slots in subsequent events.

key -> (string)

value -> (string)

Shorthand Syntax:

```
name=string,timeToLive={timeToLiveInSeconds=integer,turnsToLive=integer},parameters={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "timeToLive": {
      "timeToLiveInSeconds": integer,
      "turnsToLive": integer
    },
    "parameters": {"string": "string"
      ...}
  }
  ...
]
```

`outfile` (string)
Filename where the content will be saved

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

contentType -> (string)

Content type as specified in the `Accept` HTTP header in the request.

intentName -> (string)

The name of the current intent.

slots -> (JSON)

Map of zero or more intent slots Amazon Lex detected from the user input during the conversation.

Amazon Lex creates a resolution list containing likely values for a slot. The value that it returns is determined by the `valueSelectionStrategy` selected when the slot type was created or updated. If `valueSelectionStrategy` is set to `ORIGINAL_VALUE` , the value provided by the user is returned, if the user value is similar to the slot values. If `valueSelectionStrategy` is set to `TOP_RESOLUTION` Amazon Lex returns the first value in the resolution list or, if there is no resolution list, null. If you donât specify a `valueSelectionStrategy` the default is `ORIGINAL_VALUE` .

sessionAttributes -> (JSON)

Map of key/value pairs representing session-specific context information.

message -> (string)

The next message that should be presented to the user.

You can only use this field in the de-DE, en-AU, en-GB, en-US, es-419, es-ES, es-US, fr-CA, fr-FR, and it-IT locales. In all other locales, the `message` field is null. You should use the `encodedMessage` field instead.

encodedMessage -> (string)

The next message that should be presented to the user.

The `encodedMessage` field is base-64 encoded. You must decode the field before you can use the value.

messageFormat -> (string)

The format of the response message. One of the following values:

- `PlainText` - The message contains plain UTF-8 text.
- `CustomPayload` - The message is a custom format for the client.
- `SSML` - The message contains text formatted for voice output.
- `Composite` - The message contains an escaped JSON object containing one or more messages from the groups that messages were assigned to when the intent was created.

dialogState -> (string)

- `ConfirmIntent` - Amazon Lex is expecting a âyesâ or ânoâ response to confirm the intent before fulfilling an intent.
- `ElicitIntent` - Amazon Lex wants to elicit the userâs intent.
- `ElicitSlot` - Amazon Lex is expecting the value of a slot for the current intent.
- `Failed` - Conveys that the conversation with the user has failed. This can happen for various reasons, including the user does not provide an appropriate response to prompts from the service, or if the Lambda function fails to fulfill the intent.
- `Fulfilled` - Conveys that the Lambda function has sucessfully fulfilled the intent.
- `ReadyForFulfillment` - Conveys that the client has to fulfill the intent.

slotToElicit -> (string)

If the `dialogState` is `ElicitSlot` , returns the name of the slot for which Amazon Lex is eliciting a value.

audioStream -> (streaming blob)

The audio version of the message to convey to the user.

sessionId -> (string)

A unique identifier for the session.

activeContexts -> (JSON)

A list of active contexts for the session.