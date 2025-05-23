# post-contentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/post-content.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/post-content.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lex-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/index.html#cli-aws-lex-runtime) ]

# post-content

## Description

Sends user input (text or speech) to Amazon Lex. Clients use this API to send text and audio requests to Amazon Lex at runtime. Amazon Lex interprets the user input using the machine learning model that it built for the bot.

The `PostContent` operation supports audio input at 8kHz and 16kHz. You can use 8kHz audio to achieve higher speech recognition accuracy in telephone audio applications.

In response, Amazon Lex returns the next message to convey to the user. Consider the following example messages:

- For a user input âI would like a pizza,â Amazon Lex might return a response with a message eliciting slot data (for example, `PizzaSize` ): âWhat size pizza would you like?â.
- After the user provides all of the pizza order information, Amazon Lex might return a response with a message to get user confirmation: âOrder the pizza?â.
- After the user replies âYesâ to the confirmation prompt, Amazon Lex might return a conclusion statement: âThank you, your cheese pizza has been ordered.â.

Not all Amazon Lex messages require a response from the user. For example, conclusion statements do not require a response. Some messages require only a yes or no response. In addition to the `message` , Amazon Lex provides additional context about the message in the response that you can use to enhance client behavior, such as displaying the appropriate client user interface. Consider the following examples:

- If the message is to elicit slot data, Amazon Lex returns the following context information:
- `x-amz-lex-dialog-state` header set to `ElicitSlot`
- `x-amz-lex-intent-name` header set to the intent name in the current context
- `x-amz-lex-slot-to-elicit` header set to the slot name for which the `message` is eliciting information
- `x-amz-lex-slots` header set to a map of slots configured for the intent with their current values
- If the message is a confirmation prompt, the `x-amz-lex-dialog-state` header is set to `Confirmation` and the `x-amz-lex-slot-to-elicit` header is omitted.
- If the message is a clarification prompt configured for the intent, indicating that the user intent is not understood, the `x-amz-dialog-state` header is set to `ElicitIntent` and the `x-amz-slot-to-elicit` header is omitted.

In addition, Amazon Lex also returns your application-specific `sessionAttributes` . For more information, see [Managing Conversation Context](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/runtime.lex-2016-11-28/PostContent)

## Synopsis

```
post-content
--bot-name <value>
--bot-alias <value>
--user-id <value>
[--session-attributes <value>]
[--request-attributes <value>]
--content-type <value>
[--accept <value>]
--input-stream <value>
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

Name of the Amazon Lex bot.

`--bot-alias` (string)

Alias of the Amazon Lex bot.

`--user-id` (string)

The ID of the client application user. Amazon Lex uses this to identify a userâs conversation with your bot. At runtime, each request must contain the `userID` field.

To decide the user ID to use for your application, consider the following factors.

- The `userID` field must not contain any personally identifiable information of the user, for example, name, personal identification numbers, or other end user personal information.
- If you want a user to start a conversation on one device and continue on another device, use a user-specific identifier.
- If you want the same user to be able to have two independent conversations on two different devices, choose a device-specific identifier.
- A user canât have two independent conversations with two different versions of the same bot. For example, a user canât have a conversation with the PROD and BETA versions of the same bot. If you anticipate that a user will need to have conversation with two different versions, for example, while testing, include the bot alias in the user ID to separate the two conversations.

`--session-attributes` (JSON)

You pass this value as the `x-amz-lex-session-attributes` HTTP header.

Application-specific information passed between Amazon Lex and a client application. The value must be a JSON serialized and base64 encoded map with string keys and values. The total size of the `sessionAttributes` and `requestAttributes` headers is limited to 12 KB.

For more information, see [Setting Session Attributes](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-session-attribs) .

`--request-attributes` (JSON)

You pass this value as the `x-amz-lex-request-attributes` HTTP header.

Request-specific information passed between Amazon Lex and a client application. The value must be a JSON serialized and base64 encoded map with string keys and values. The total size of the `requestAttributes` and `sessionAttributes` headers is limited to 12 KB.

The namespace `x-amz-lex:` is reserved for special attributes. Donât create any request attributes with the prefix `x-amz-lex:` .

For more information, see [Setting Request Attributes](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-request-attribs) .

`--content-type` (string)

You pass this value as the `Content-Type` HTTP header.

Indicates the audio format or text. The header value must start with one of the following prefixes:

- PCM format, audio data must be in little-endian byte order.
- audio/l16; rate=16000; channels=1
- audio/x-l16; sample-rate=16000; channel-count=1
- audio/lpcm; sample-rate=8000; sample-size-bits=16; channel-count=1; is-big-endian=false
- Opus format
- audio/x-cbr-opus-with-preamble; preamble-size=0; bit-rate=256000; frame-size-milliseconds=4
- Text format
- text/plain; charset=utf-8

`--accept` (string)

You pass this value as the `Accept` HTTP header.

The message Amazon Lex returns in the response can be either text or speech based on the `Accept` HTTP header value in the request.

- If the value is `text/plain; charset=utf-8` , Amazon Lex returns text in the response.
- If the value begins with `audio/` , Amazon Lex returns speech in the response. Amazon Lex uses Amazon Polly to generate the speech (using the configuration you specified in the `Accept` header). For example, if you specify `audio/mpeg` as the value, Amazon Lex returns speech in the MPEG format.
- If the value is `audio/pcm` , the speech returned is `audio/pcm` in 16-bit, little endian format.
- The following are the accepted values:
- audio/mpeg
- audio/ogg
- audio/pcm
- text/plain; charset=utf-8
- audio/* (defaults to mpeg)

`--input-stream` (streaming blob)

User input in PCM or Opus audio format or text format as described in the `Content-Type` HTTP header.

You can stream audio data to Amazon Lex or you can create a local buffer that captures all of the audio data before sending. In general, you get better performance if you stream audio data rather than buffering the data locally.

### Note

This argument is of type: streaming blob. Its value must be the path to a file (e.g. `path/to/file`) and must **not** be prefixed with `file://` or `fileb://`

`--active-contexts` (JSON)

A list of contexts active for the request. A context can be activated when a previous intent is fulfilled, or by including the context in the request,

If you donât specify a list of contexts, Amazon Lex will use the current list of contexts for the session. If you specify an empty list, all contexts for the session are cleared.

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

Current user intent that Amazon Lex is aware of.

nluIntentConfidence -> (JSON)

Provides a score that indicates how confident Amazon Lex is that the returned intent is the one that matches the userâs intent. The score is between 0.0 and 1.0.

The score is a relative score, not an absolute score. The score may change based on improvements to Amazon Lex.

alternativeIntents -> (JSON)

One to four alternative intents that may be applicable to the userâs intent.

Each alternative includes a score that indicates how confident Amazon Lex is that the intent matches the userâs intent. The intents are sorted by the confidence score.

slots -> (JSON)

Map of zero or more intent slots (name/value pairs) Amazon Lex detected from the user input during the conversation. The field is base-64 encoded.

Amazon Lex creates a resolution list containing likely values for a slot. The value that it returns is determined by the `valueSelectionStrategy` selected when the slot type was created or updated. If `valueSelectionStrategy` is set to `ORIGINAL_VALUE` , the value provided by the user is returned, if the user value is similar to the slot values. If `valueSelectionStrategy` is set to `TOP_RESOLUTION` Amazon Lex returns the first value in the resolution list or, if there is no resolution list, null. If you donât specify a `valueSelectionStrategy` , the default is `ORIGINAL_VALUE` .

sessionAttributes -> (JSON)

Map of key/value pairs representing the session-specific context information.

sentimentResponse -> (string)

The sentiment expressed in an utterance.

When the bot is configured to send utterances to Amazon Comprehend for sentiment analysis, this field contains the result of the analysis.

message -> (string)

You can only use this field in the de-DE, en-AU, en-GB, en-US, es-419, es-ES, es-US, fr-CA, fr-FR, and it-IT locales. In all other locales, the `message` field is null. You should use the `encodedMessage` field instead.

The message to convey to the user. The message can come from the botâs configuration or from a Lambda function.

If the intent is not configured with a Lambda function, or if the Lambda function returned `Delegate` as the `dialogAction.type` in its response, Amazon Lex decides on the next course of action and selects an appropriate message from the botâs configuration based on the current interaction context. For example, if Amazon Lex isnât able to understand user input, it uses a clarification prompt message.

When you create an intent you can assign messages to groups. When messages are assigned to groups Amazon Lex returns one message from each group in the response. The message field is an escaped JSON string containing the messages. For more information about the structure of the JSON string returned, see  msg-prompts-formats .

If the Lambda function returns a message, Amazon Lex passes it to the client in its response.

encodedMessage -> (string)

The message to convey to the user. The message can come from the botâs configuration or from a Lambda function.

If the intent is not configured with a Lambda function, or if the Lambda function returned `Delegate` as the `dialogAction.type` in its response, Amazon Lex decides on the next course of action and selects an appropriate message from the botâs configuration based on the current interaction context. For example, if Amazon Lex isnât able to understand user input, it uses a clarification prompt message.

When you create an intent you can assign messages to groups. When messages are assigned to groups Amazon Lex returns one message from each group in the response. The message field is an escaped JSON string containing the messages. For more information about the structure of the JSON string returned, see  msg-prompts-formats .

If the Lambda function returns a message, Amazon Lex passes it to the client in its response.

The `encodedMessage` field is base-64 encoded. You must decode the field before you can use the value.

messageFormat -> (string)

The format of the response message. One of the following values:

- `PlainText` - The message contains plain UTF-8 text.
- `CustomPayload` - The message is a custom format for the client.
- `SSML` - The message contains text formatted for voice output.
- `Composite` - The message contains an escaped JSON object containing one or more messages from the groups that messages were assigned to when the intent was created.

dialogState -> (string)

Identifies the current state of the user interaction. Amazon Lex returns one of the following values as `dialogState` . The client can optionally use this information to customize the user interface.

- `ElicitIntent` - Amazon Lex wants to elicit the userâs intent. Consider the following examples:  For example, a user might utter an intent (âI want to order a pizzaâ). If Amazon Lex cannot infer the user intent from this utterance, it will return this dialog state.
- `ConfirmIntent` - Amazon Lex is expecting a âyesâ or ânoâ response.  For example, Amazon Lex wants user confirmation before fulfilling an intent. Instead of a simple âyesâ or ânoâ response, a user might respond with additional information. For example, âyes, but make it a thick crust pizzaâ or âno, I want to order a drink.â Amazon Lex can process such additional information (in these examples, update the crust type slot or change the intent from OrderPizza to OrderDrink).
- `ElicitSlot` - Amazon Lex is expecting the value of a slot for the current intent.  For example, suppose that in the response Amazon Lex sends this message: âWhat size pizza would you like?â. A user might reply with the slot value (e.g., âmediumâ). The user might also provide additional information in the response (e.g., âmedium thick crust pizzaâ). Amazon Lex can process such additional information appropriately.
- `Fulfilled` - Conveys that the Lambda function has successfully fulfilled the intent.
- `ReadyForFulfillment` - Conveys that the client has to fulfill the request.
- `Failed` - Conveys that the conversation with the user failed.  This can happen for various reasons, including that the user does not provide an appropriate response to prompts from the service (you can configure how many times Amazon Lex can prompt a user for specific information), or if the Lambda function fails to fulfill the intent.

slotToElicit -> (string)

If the `dialogState` value is `ElicitSlot` , returns the name of the slot for which Amazon Lex is eliciting a value.

inputTranscript -> (string)

The text used to process the request.

You can use this field only in the de-DE, en-AU, en-GB, en-US, es-419, es-ES, es-US, fr-CA, fr-FR, and it-IT locales. In all other locales, the `inputTranscript` field is null. You should use the `encodedInputTranscript` field instead.

If the input was an audio stream, the `inputTranscript` field contains the text extracted from the audio stream. This is the text that is actually processed to recognize intents and slot values. You can use this information to determine if Amazon Lex is correctly processing the audio that you send.

encodedInputTranscript -> (string)

The text used to process the request.

If the input was an audio stream, the `encodedInputTranscript` field contains the text extracted from the audio stream. This is the text that is actually processed to recognize intents and slot values. You can use this information to determine if Amazon Lex is correctly processing the audio that you send.

The `encodedInputTranscript` field is base-64 encoded. You must decode the field before you can use the value.

audioStream -> (streaming blob)

The prompt (or statement) to convey to the user. This is based on the bot configuration and context. For example, if Amazon Lex did not understand the user intent, it sends the `clarificationPrompt` configured for the bot. If the intent requires confirmation before taking the fulfillment action, it sends the `confirmationPrompt` . Another example: Suppose that the Lambda function successfully fulfilled the intent, and sent a message to convey to the user. Then Amazon Lex sends that message in the response.

botVersion -> (string)

The version of the bot that responded to the conversation. You can use this information to help determine if one version of a bot is performing better than another version.

sessionId -> (string)

The unique identifier for the session.

activeContexts -> (JSON)

A list of active contexts for the session. A context can be set when an intent is fulfilled or by calling the `PostContent` , `PostText` , or `PutSession` operation.

You can use a context to control the intents that can follow up an intent, or to modify the operation of your application.