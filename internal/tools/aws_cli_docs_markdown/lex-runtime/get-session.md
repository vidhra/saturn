# get-sessionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/get-session.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/get-session.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lex-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/index.html#cli-aws-lex-runtime) ]

# get-session

## Description

Returns session information for a specified bot, alias, and user ID.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/runtime.lex-2016-11-28/GetSession)

## Synopsis

```
get-session
--bot-name <value>
--bot-alias <value>
--user-id <value>
[--checkpoint-label-filter <value>]
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

The name of the bot that contains the session data.

`--bot-alias` (string)

The alias in use for the bot that contains the session data.

`--user-id` (string)

The ID of the client application user. Amazon Lex uses this to identify a userâs conversation with your bot.

`--checkpoint-label-filter` (string)

A string used to filter the intents returned in the `recentIntentSummaryView` structure.

When you specify a filter, only intents with their `checkpointLabel` field set to that string are returned.

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

recentIntentSummaryView -> (list)

An array of information about the intents used in the session. The array can contain a maximum of three summaries. If more than three intents are used in the session, the `recentIntentSummaryView` operation contains information about the last three intents used.

If you set the `checkpointLabelFilter` parameter in the request, the array contains only the intents with the specified label.

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

sessionAttributes -> (map)

Map of key/value pairs representing the session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

sessionId -> (string)

A unique identifier for the session.

dialogAction -> (structure)

Describes the current state of the bot.

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