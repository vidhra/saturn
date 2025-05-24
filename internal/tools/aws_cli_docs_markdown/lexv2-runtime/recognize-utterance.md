# recognize-utteranceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-runtime/recognize-utterance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-runtime/recognize-utterance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-runtime/index.html#cli-aws-lexv2-runtime) ]

# recognize-utterance

## Description

Sends user input to Amazon Lex V2. You can send text or speech. Clients use this API to send text and audio requests to Amazon Lex V2 at runtime. Amazon Lex V2 interprets the user input using the machine learning model built for the bot.

The following request fields must be compressed with gzip and then base64 encoded before you send them to Amazon Lex V2.

- requestAttributes
- sessionState

The following response fields are compressed using gzip and then base64 encoded by Amazon Lex V2. Before you can use these fields, you must decode and decompress them.

- inputTranscript
- interpretations
- messages
- requestAttributes
- sessionState

The example contains a Java application that compresses and encodes a Java object to send to Amazon Lex V2, and a second that decodes and decompresses a response from Amazon Lex V2.

If the optional post-fulfillment response is specified, the messages are returned as follows. For more information, see [PostFulfillmentStatusSpecification](https://docs.aws.amazon.com/lexv2/latest/dg/API_PostFulfillmentStatusSpecification.html) .

- **Success message** - Returned if the Lambda function completes successfully and the intent state is fulfilled or ready fulfillment if the message is present.
- **Failed message** - The failed message is returned if the Lambda function throws an exception or if the Lambda function returns a failed intent state without a message.
- **Timeout message** - If you donât configure a timeout message and a timeout, and the Lambda function doesnât return within 30 seconds, the timeout message is returned. If you configure a timeout, the timeout message is returned when the period times out.

For more information, see [Completion message](https://docs.aws.amazon.com/lexv2/latest/dg/streaming-progress.html#progress-complete.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/runtime.lex.v2-2020-08-07/RecognizeUtterance)

## Synopsis

```
recognize-utterance
--bot-id <value>
--bot-alias-id <value>
--locale-id <value>
--session-id <value>
[--session-state <value>]
[--request-attributes <value>]
--request-content-type <value>
[--response-content-type <value>]
[--input-stream <value>]
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

`--bot-id` (string)

The identifier of the bot that should receive the request.

`--bot-alias-id` (string)

The alias identifier in use for the bot that should receive the request.

`--locale-id` (string)

The locale where the session is in use.

`--session-id` (string)

The identifier of the session in use.

`--session-state` (string)

Sets the state of the session with the user. You can use this to set the current intent, attributes, context, and dialog action. Use the dialog action to determine the next step that Amazon Lex V2 should use in the conversation with the user.

The `sessionState` field must be compressed using gzip and then base64 encoded before sending to Amazon Lex V2.

`--request-attributes` (string)

Request-specific information passed between the client application and Amazon Lex V2

The namespace `x-amz-lex:` is reserved for special attributes. Donât create any request attributes for prefix `x-amz-lex:` .

The `requestAttributes` field must be compressed using gzip and then base64 encoded before sending to Amazon Lex V2.

`--request-content-type` (string)

Indicates the format for audio input or that the content is text. The header must start with one of the following prefixes:

- PCM format, audio data must be in little-endian byte order.
- audio/l16; rate=16000; channels=1
- audio/x-l16; sample-rate=16000; channel-count=1
- audio/lpcm; sample-rate=8000; sample-size-bits=16; channel-count=1; is-big-endian=false
- Opus format
- audio/x-cbr-opus-with-preamble;preamble-size=0;bit-rate=256000;frame-size-milliseconds=4
- Text format
- text/plain; charset=utf-8

`--response-content-type` (string)

The message that Amazon Lex V2 returns in the response can be either text or speech based on the `responseContentType` value.

- If the value is `text/plain;charset=utf-8` , Amazon Lex V2 returns text in the response.
- If the value begins with `audio/` , Amazon Lex V2 returns speech in the response. Amazon Lex V2 uses Amazon Polly to generate the speech using the configuration that you specified in the `responseContentType` parameter. For example, if you specify `audio/mpeg` as the value, Amazon Lex V2 returns speech in the MPEG format.
- If the value is `audio/pcm` , the speech returned is `audio/pcm` at 16 KHz in 16-bit, little-endian format.
- The following are the accepted values:
- audio/mpeg
- audio/ogg
- audio/pcm (16 KHz)
- audio/* (defaults to mpeg)
- text/plain; charset=utf-8

`--input-stream` (streaming blob)

User input in PCM or Opus audio format or text format as described in the `requestContentType` parameter.

### Note

This argument is of type: streaming blob. Its value must be the path to a file (e.g. `path/to/file`) and must **not** be prefixed with `file://` or `fileb://`

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

inputMode -> (string)

Indicates whether the input mode to the operation was text, speech, or from a touch-tone keypad.

contentType -> (string)

Content type as specified in the `responseContentType` in the request.

messages -> (string)

A list of messages that were last sent to the user. The messages are ordered based on the order that you returned the messages from your Lambda function or the order that the messages are defined in the bot.

The `messages` field is compressed with gzip and then base64 encoded. Before you can use the contents of the field, you must decode and decompress the contents. See the example for a simple function to decode and decompress the contents.

interpretations -> (string)

A list of intents that Amazon Lex V2 determined might satisfy the userâs utterance.

Each interpretation includes the intent, a score that indicates how confident Amazon Lex V2 is that the interpretation is the correct one, and an optional sentiment response that indicates the sentiment expressed in the utterance.

The `interpretations` field is compressed with gzip and then base64 encoded. Before you can use the contents of the field, you must decode and decompress the contents. See the example for a simple function to decode and decompress the contents.

sessionState -> (string)

Represents the current state of the dialog between the user and the bot.

Use this to determine the progress of the conversation and what the next action might be.

The `sessionState` field is compressed with gzip and then base64 encoded. Before you can use the contents of the field, you must decode and decompress the contents. See the example for a simple function to decode and decompress the contents.

requestAttributes -> (string)

The attributes sent in the request.

The `requestAttributes` field is compressed with gzip and then base64 encoded. Before you can use the contents of the field, you must decode and decompress the contents.

sessionId -> (string)

The identifier of the session in use.

inputTranscript -> (string)

The text used to process the request.

If the input was an audio stream, the `inputTranscript` field contains the text extracted from the audio stream. This is the text that is actually processed to recognize intents and slot values. You can use this information to determine if Amazon Lex V2 is correctly processing the audio that you send.

The `inputTranscript` field is compressed with gzip and then base64 encoded. Before you can use the contents of the field, you must decode and decompress the contents. See the example for a simple function to decode and decompress the contents.

audioStream -> (streaming blob)

The prompt or statement to send to the user. This is based on the bot configuration and context. For example, if Amazon Lex V2 did not understand the user intent, it sends the `clarificationPrompt` configured for the bot. If the intent requires confirmation before taking the fulfillment action, it sends the `confirmationPrompt` . Another example: Suppose that the Lambda function successfully fulfilled the intent, and sent a message to convey to the user. Then Amazon Lex V2 sends that message in the response.

recognizedBotMember -> (string)

The bot member that recognized the utterance.