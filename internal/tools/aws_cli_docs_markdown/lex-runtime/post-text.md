# post-textÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/post-text.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/post-text.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lex-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/index.html#cli-aws-lex-runtime) ]

# post-text

## Description

Sends user input to Amazon Lex. Client applications can use this API to send requests to Amazon Lex at runtime. Amazon Lex then interprets the user input using the machine learning model it built for the bot.

In response, Amazon Lex returns the next `message` to convey to the user an optional `responseCard` to display. Consider the following example messages:

- For a user input âI would like a pizzaâ, Amazon Lex might return a response with a message eliciting slot data (for example, PizzaSize): âWhat size pizza would you like?â
- After the user provides all of the pizza order information, Amazon Lex might return a response with a message to obtain user confirmation âProceed with the pizza order?â.
- After the user replies to a confirmation prompt with a âyesâ, Amazon Lex might return a conclusion statement: âThank you, your cheese pizza has been ordered.â.

Not all Amazon Lex messages require a user response. For example, a conclusion statement does not require a response. Some messages require only a âyesâ or ânoâ user response. In addition to the `message` , Amazon Lex provides additional context about the message in the response that you might use to enhance client behavior, for example, to display the appropriate client user interface. These are the `slotToElicit` , `dialogState` , `intentName` , and `slots` fields in the response. Consider the following examples:

- If the message is to elicit slot data, Amazon Lex returns the following context information:
- `dialogState` set to ElicitSlot
- `intentName` set to the intent name in the current context
- `slotToElicit` set to the slot name for which the `message` is eliciting information
- `slots` set to a map of slots, configured for the intent, with currently known values
- If the message is a confirmation prompt, the `dialogState` is set to ConfirmIntent and `SlotToElicit` is set to null.
- If the message is a clarification prompt (configured for the intent) that indicates that user intent is not understood, the `dialogState` is set to ElicitIntent and `slotToElicit` is set to null.

In addition, Amazon Lex also returns your application-specific `sessionAttributes` . For more information, see [Managing Conversation Context](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/runtime.lex-2016-11-28/PostText)

## Synopsis

```
post-text
--bot-name <value>
--bot-alias <value>
--user-id <value>
[--session-attributes <value>]
[--request-attributes <value>]
--input-text <value>
[--active-contexts <value>]
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

`--bot-name` (string)

The name of the Amazon Lex bot.

`--bot-alias` (string)

The alias of the Amazon Lex bot.

`--user-id` (string)

The ID of the client application user. Amazon Lex uses this to identify a userâs conversation with your bot. At runtime, each request must contain the `userID` field.

To decide the user ID to use for your application, consider the following factors.

- The `userID` field must not contain any personally identifiable information of the user, for example, name, personal identification numbers, or other end user personal information.
- If you want a user to start a conversation on one device and continue on another device, use a user-specific identifier.
- If you want the same user to be able to have two independent conversations on two different devices, choose a device-specific identifier.
- A user canât have two independent conversations with two different versions of the same bot. For example, a user canât have a conversation with the PROD and BETA versions of the same bot. If you anticipate that a user will need to have conversation with two different versions, for example, while testing, include the bot alias in the user ID to separate the two conversations.

`--session-attributes` (map)

Application-specific information passed between Amazon Lex and a client application.

For more information, see [Setting Session Attributes](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-session-attribs) .

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

`--request-attributes` (map)

Request-specific information passed between Amazon Lex and a client application.

The namespace `x-amz-lex:` is reserved for special attributes. Donât create any request attributes with the prefix `x-amz-lex:` .

For more information, see [Setting Request Attributes](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-request-attribs) .

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

`--input-text` (string)

The text that the user entered (Amazon Lex interprets this text).

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

intentName -> (string)

The current user intent that Amazon Lex is aware of.

nluIntentConfidence -> (structure)

Provides a score that indicates how confident Amazon Lex is that the returned intent is the one that matches the userâs intent. The score is between 0.0 and 1.0. For more information, see [Confidence Scores](https://docs.aws.amazon.com/lex/latest/dg/confidence-scores.html) .

The score is a relative score, not an absolute score. The score may change based on improvements to Amazon Lex.

score -> (double)

A score that indicates how confident Amazon Lex is that an intent satisfies the userâs intent. Ranges between 0.00 and 1.00. Higher scores indicate higher confidence.

alternativeIntents -> (list)

One to four alternative intents that may be applicable to the userâs intent.

Each alternative includes a score that indicates how confident Amazon Lex is that the intent matches the userâs intent. The intents are sorted by the confidence score.

(structure)

An intent that Amazon Lex suggests satisfies the userâs intent. Includes the name of the intent, the confidence that Amazon Lex has that the userâs intent is satisfied, and the slots defined for the intent.

intentName -> (string)

The name of the intent that Amazon Lex suggests satisfies the userâs intent.

nluIntentConfidence -> (structure)

Indicates how confident Amazon Lex is that an intent satisfies the userâs intent.

score -> (double)

A score that indicates how confident Amazon Lex is that an intent satisfies the userâs intent. Ranges between 0.00 and 1.00. Higher scores indicate higher confidence.

slots -> (map)

The slot and slot values associated with the predicted intent.

key -> (string)

value -> (string)

slots -> (map)

The intent slots that Amazon Lex detected from the user input in the conversation.

Amazon Lex creates a resolution list containing likely values for a slot. The value that it returns is determined by the `valueSelectionStrategy` selected when the slot type was created or updated. If `valueSelectionStrategy` is set to `ORIGINAL_VALUE` , the value provided by the user is returned, if the user value is similar to the slot values. If `valueSelectionStrategy` is set to `TOP_RESOLUTION` Amazon Lex returns the first value in the resolution list or, if there is no resolution list, null. If you donât specify a `valueSelectionStrategy` , the default is `ORIGINAL_VALUE` .

key -> (string)

value -> (string)

sessionAttributes -> (map)

A map of key-value pairs representing the session-specific context information.

key -> (string)

value -> (string)

message -> (string)

The message to convey to the user. The message can come from the botâs configuration or from a Lambda function.

If the intent is not configured with a Lambda function, or if the Lambda function returned `Delegate` as the `dialogAction.type` its response, Amazon Lex decides on the next course of action and selects an appropriate message from the botâs configuration based on the current interaction context. For example, if Amazon Lex isnât able to understand user input, it uses a clarification prompt message.

When you create an intent you can assign messages to groups. When messages are assigned to groups Amazon Lex returns one message from each group in the response. The message field is an escaped JSON string containing the messages. For more information about the structure of the JSON string returned, see  msg-prompts-formats .

If the Lambda function returns a message, Amazon Lex passes it to the client in its response.

sentimentResponse -> (structure)

The sentiment expressed in and utterance.

When the bot is configured to send utterances to Amazon Comprehend for sentiment analysis, this field contains the result of the analysis.

sentimentLabel -> (string)

The inferred sentiment that Amazon Comprehend has the highest confidence in.

sentimentScore -> (string)

The likelihood that the sentiment was correctly inferred.

messageFormat -> (string)

The format of the response message. One of the following values:

- `PlainText` - The message contains plain UTF-8 text.
- `CustomPayload` - The message is a custom format defined by the Lambda function.
- `SSML` - The message contains text formatted for voice output.
- `Composite` - The message contains an escaped JSON object containing one or more messages from the groups that messages were assigned to when the intent was created.

dialogState -> (string)

Identifies the current state of the user interaction. Amazon Lex returns one of the following values as `dialogState` . The client can optionally use this information to customize the user interface.

- `ElicitIntent` - Amazon Lex wants to elicit user intent.  For example, a user might utter an intent (âI want to order a pizzaâ). If Amazon Lex cannot infer the user intent from this utterance, it will return this dialogState.
- `ConfirmIntent` - Amazon Lex is expecting a âyesâ or ânoâ response.  For example, Amazon Lex wants user confirmation before fulfilling an intent.  Instead of a simple âyesâ or âno,â a user might respond with additional information. For example, âyes, but make it thick crust pizzaâ or âno, I want to order a drinkâ. Amazon Lex can process such additional information (in these examples, update the crust type slot value, or change intent from OrderPizza to OrderDrink).
- `ElicitSlot` - Amazon Lex is expecting a slot value for the current intent.  For example, suppose that in the response Amazon Lex sends this message: âWhat size pizza would you like?â. A user might reply with the slot value (e.g., âmediumâ). The user might also provide additional information in the response (e.g., âmedium thick crust pizzaâ). Amazon Lex can process such additional information appropriately.
- `Fulfilled` - Conveys that the Lambda function configured for the intent has successfully fulfilled the intent.
- `ReadyForFulfillment` - Conveys that the client has to fulfill the intent.
- `Failed` - Conveys that the conversation with the user failed.  This can happen for various reasons including that the user did not provide an appropriate response to prompts from the service (you can configure how many times Amazon Lex can prompt a user for specific information), or the Lambda function failed to fulfill the intent.

slotToElicit -> (string)

If the `dialogState` value is `ElicitSlot` , returns the name of the slot for which Amazon Lex is eliciting a value.

responseCard -> (structure)

Represents the options that the user has to respond to the current prompt. Response Card can come from the bot configuration (in the Amazon Lex console, choose the settings button next to a slot) or from a code hook (Lambda function).

version -> (string)

The version of the response card format.

contentType -> (string)

The content type of the response.

genericAttachments -> (list)

An array of attachment objects representing options.

(structure)

Represents an option rendered to the user when a prompt is shown. It could be an image, a button, a link, or text.

title -> (string)

The title of the option.

subTitle -> (string)

The subtitle shown below the title.

attachmentLinkUrl -> (string)

The URL of an attachment to the response card.

imageUrl -> (string)

The URL of an image that is displayed to the user.

buttons -> (list)

The list of options to show to the user.

(structure)

Represents an option to be shown on the client platform (Facebook, Slack, etc.)

text -> (string)

Text that is visible to the user on the button.

value -> (string)

The value sent to Amazon Lex when a user chooses the button. For example, consider button text âNYC.â When the user chooses the button, the value sent can be âNew York City.â

sessionId -> (string)

A unique identifier for the session.

botVersion -> (string)

The version of the bot that responded to the conversation. You can use this information to help determine if one version of a bot is performing better than another version.

activeContexts -> (list)

A list of active contexts for the session. A context can be set when an intent is fulfilled or by calling the `PostContent` , `PostText` , or `PutSession` operation.

You can use a context to control the intents that can follow up an intent, or to modify the operation of your application.

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