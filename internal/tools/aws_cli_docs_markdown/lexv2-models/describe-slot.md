# describe-slotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/describe-slot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/describe-slot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# describe-slot

## Description

Gets metadata information about a slot.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/DescribeSlot)

## Synopsis

```
describe-slot
--slot-id <value>
--bot-id <value>
--bot-version <value>
--locale-id <value>
--intent-id <value>
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

`--slot-id` (string)

The unique identifier for the slot.

`--bot-id` (string)

The identifier of the bot associated with the slot.

`--bot-version` (string)

The version of the bot associated with the slot.

`--locale-id` (string)

The identifier of the language and locale of the slot to describe. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html) .

`--intent-id` (string)

The identifier of the intent that contains the slot.

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

slotId -> (string)

The unique identifier generated for the slot.

slotName -> (string)

The name specified for the slot.

description -> (string)

The description specified for the slot.

slotTypeId -> (string)

The identifier of the slot type that determines the values entered into the slot.

valueElicitationSetting -> (structure)

Prompts that Amazon Lex uses to elicit a value for the slot.

defaultValueSpecification -> (structure)

A list of default values for a slot. Default values are used when Amazon Lex hasnât determined a value for a slot. You can specify default values from context variables, session attributes, and defined values.

defaultValueList -> (list)

A list of default values. Amazon Lex chooses the default value to use in the order that they are presented in the list.

(structure)

Specifies the default value to use when a user doesnât provide a value for a slot.

defaultValue -> (string)

The default value to use when a user doesnât provide a value for a slot.

slotConstraint -> (string)

Specifies whether the slot is required or optional.

promptSpecification -> (structure)

The prompt that Amazon Lex uses to elicit the slot value from the user.

messageGroups -> (list)

A collection of messages that Amazon Lex can send to the user. Amazon Lex chooses the actual message to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

maxRetries -> (integer)

The maximum number of times the bot tries to elicit a response from the user using this prompt.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech prompt from the bot.

messageSelectionStrategy -> (string)

Indicates how a message is selected from a message group among retries.

promptAttemptsSpecification -> (map)

Specifies the advanced settings on each attempt of the prompt.

key -> (string)

The attempt name of attempts of a prompt.

value -> (structure)

Specifies the settings on a prompt attempt.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech prompt attempt from the bot.

allowedInputTypes -> (structure)

Indicates the allowed input types of the prompt attempt.

allowAudioInput -> (boolean)

Indicates whether audio input is allowed.

allowDTMFInput -> (boolean)

Indicates whether DTMF input is allowed.

audioAndDTMFInputSpecification -> (structure)

Specifies the settings on audio and DTMF input.

startTimeoutMs -> (integer)

Time for which a bot waits before assuming that the customer isnât going to speak or press a key. This timeout is shared between Audio and DTMF inputs.

audioSpecification -> (structure)

Specifies the settings on audio input.

maxLengthMs -> (integer)

Time for how long Amazon Lex waits before speech input is truncated and the speech is returned to application.

endTimeoutMs -> (integer)

Time for which a bot waits after the customer stops speaking to assume the utterance is finished.

dtmfSpecification -> (structure)

Specifies the settings on DTMF input.

maxLength -> (integer)

The maximum number of DTMF digits allowed in an utterance.

endTimeoutMs -> (integer)

How long the bot should wait after the last DTMF character input before assuming that the input has concluded.

deletionCharacter -> (string)

The DTMF character that clears the accumulated DTMF digits and immediately ends the input.

endCharacter -> (string)

The DTMF character that immediately ends input. If the user does not press this character, the input ends after the end timeout.

textInputSpecification -> (structure)

Specifies the settings on text input.

startTimeoutMs -> (integer)

Time for which a bot waits before re-prompting a customer for text input.

sampleUtterances -> (list)

If you know a specific pattern that users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances.

(structure)

A sample utterance that invokes an intent or respond to a slot elicitation prompt.

utterance -> (string)

The sample utterance that Amazon Lex uses to build its machine-learning model to recognize intents.

waitAndContinueSpecification -> (structure)

Specifies the prompts that Amazon Lex uses while a bot is waiting for customer input.

waitingResponse -> (structure)

The response that Amazon Lex sends to indicate that the bot is waiting for the conversation to continue.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

continueResponse -> (structure)

The response that Amazon Lex sends to indicate that the bot is ready to continue the conversation.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

stillWaitingResponse -> (structure)

A response that Amazon Lex sends periodically to the user to indicate that the bot is still waiting for input from the user.

messageGroups -> (list)

One or more message groups, each containing one or more messages, that define the prompts that Amazon Lex sends to the user.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

frequencyInSeconds -> (integer)

How often a message should be sent to the user. Minimum of 1 second, maximum of 5 minutes.

timeoutInSeconds -> (integer)

If Amazon Lex waits longer than this length of time for a response, it will stop sending messages.

allowInterrupt -> (boolean)

Indicates that the user can interrupt the response by speaking while the message is being played.

active -> (boolean)

Specifies whether the bot will wait for a user to respond. When this field is false, wait and continue responses for a slot arenât used. If the `active` field isnât specified, the default is true.

slotCaptureSetting -> (structure)

Specifies the settings that Amazon Lex uses when a slot value is successfully entered by a user.

captureResponse -> (structure)

Specifies a list of message groups that Amazon Lex uses to respond the user input.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

captureNextStep -> (structure)

Specifies the next step that the bot runs when the slot value is captured before the code hook times out.

dialogAction -> (structure)

Defines the action that the bot executes at runtime when the conversation reaches this step.

type -> (string)

The action that the bot should execute.

slotToElicit -> (string)

If the dialog action is `ElicitSlot` , defines the slot to elicit from the user.

suppressNextMessage -> (boolean)

When true the next message for the intent is not used.

intent -> (structure)

Override settings to configure the intent state.

name -> (string)

The name of the intent. Only required when youâre switching intents.

slots -> (map)

A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map arenât overridden.

key -> (string)

value -> (structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

captureConditional -> (structure)

A list of conditional branches to evaluate after the slot value is captured.

active -> (boolean)

Determines whether a conditional branch is active. When `active` is false, the conditions are not evaluated.

conditionalBranches -> (list)

A list of conditional branches. A conditional branch is made up of a condition, a response and a next step. The response and next step are executed when the condition is true.

(structure)

A set of actions that Amazon Lex should run if the condition is matched.

name -> (string)

The name of the branch.

condition -> (structure)

Contains the expression to evaluate. If the condition is true, the branchâs actions are taken.

expressionString -> (string)

The expression string that is evaluated.

nextStep -> (structure)

The next step in the conversation.

dialogAction -> (structure)

Defines the action that the bot executes at runtime when the conversation reaches this step.

type -> (string)

The action that the bot should execute.

slotToElicit -> (string)

If the dialog action is `ElicitSlot` , defines the slot to elicit from the user.

suppressNextMessage -> (boolean)

When true the next message for the intent is not used.

intent -> (structure)

Override settings to configure the intent state.

name -> (string)

The name of the intent. Only required when youâre switching intents.

slots -> (map)

A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map arenât overridden.

key -> (string)

value -> (structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

response -> (structure)

Specifies a list of message groups that Amazon Lex uses to respond the user input.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

defaultBranch -> (structure)

The conditional branch that should be followed when the conditions for other branches are not satisfied. A conditional branch is made up of a condition, a response and a next step.

nextStep -> (structure)

The next step in the conversation.

dialogAction -> (structure)

Defines the action that the bot executes at runtime when the conversation reaches this step.

type -> (string)

The action that the bot should execute.

slotToElicit -> (string)

If the dialog action is `ElicitSlot` , defines the slot to elicit from the user.

suppressNextMessage -> (boolean)

When true the next message for the intent is not used.

intent -> (structure)

Override settings to configure the intent state.

name -> (string)

The name of the intent. Only required when youâre switching intents.

slots -> (map)

A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map arenât overridden.

key -> (string)

value -> (structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

response -> (structure)

Specifies a list of message groups that Amazon Lex uses to respond the user input.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

failureResponse -> (structure)

Specifies a list of message groups that Amazon Lex uses to respond the user input.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

failureNextStep -> (structure)

Specifies the next step that the bot runs when the slot value code is not recognized.

dialogAction -> (structure)

Defines the action that the bot executes at runtime when the conversation reaches this step.

type -> (string)

The action that the bot should execute.

slotToElicit -> (string)

If the dialog action is `ElicitSlot` , defines the slot to elicit from the user.

suppressNextMessage -> (boolean)

When true the next message for the intent is not used.

intent -> (structure)

Override settings to configure the intent state.

name -> (string)

The name of the intent. Only required when youâre switching intents.

slots -> (map)

A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map arenât overridden.

key -> (string)

value -> (structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

failureConditional -> (structure)

A list of conditional branches to evaluate when the slot value isnât captured.

active -> (boolean)

Determines whether a conditional branch is active. When `active` is false, the conditions are not evaluated.

conditionalBranches -> (list)

A list of conditional branches. A conditional branch is made up of a condition, a response and a next step. The response and next step are executed when the condition is true.

(structure)

A set of actions that Amazon Lex should run if the condition is matched.

name -> (string)

The name of the branch.

condition -> (structure)

Contains the expression to evaluate. If the condition is true, the branchâs actions are taken.

expressionString -> (string)

The expression string that is evaluated.

nextStep -> (structure)

The next step in the conversation.

dialogAction -> (structure)

Defines the action that the bot executes at runtime when the conversation reaches this step.

type -> (string)

The action that the bot should execute.

slotToElicit -> (string)

If the dialog action is `ElicitSlot` , defines the slot to elicit from the user.

suppressNextMessage -> (boolean)

When true the next message for the intent is not used.

intent -> (structure)

Override settings to configure the intent state.

name -> (string)

The name of the intent. Only required when youâre switching intents.

slots -> (map)

A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map arenât overridden.

key -> (string)

value -> (structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

response -> (structure)

Specifies a list of message groups that Amazon Lex uses to respond the user input.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

defaultBranch -> (structure)

The conditional branch that should be followed when the conditions for other branches are not satisfied. A conditional branch is made up of a condition, a response and a next step.

nextStep -> (structure)

The next step in the conversation.

dialogAction -> (structure)

Defines the action that the bot executes at runtime when the conversation reaches this step.

type -> (string)

The action that the bot should execute.

slotToElicit -> (string)

If the dialog action is `ElicitSlot` , defines the slot to elicit from the user.

suppressNextMessage -> (boolean)

When true the next message for the intent is not used.

intent -> (structure)

Override settings to configure the intent state.

name -> (string)

The name of the intent. Only required when youâre switching intents.

slots -> (map)

A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map arenât overridden.

key -> (string)

value -> (structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

response -> (structure)

Specifies a list of message groups that Amazon Lex uses to respond the user input.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

codeHook -> (structure)

Code hook called after Amazon Lex successfully captures a slot value.

enableCodeHookInvocation -> (boolean)

Indicates whether a Lambda function should be invoked for the dialog.

active -> (boolean)

Determines whether a dialog code hook is used when the intent is activated.

invocationLabel -> (string)

A label that indicates the dialog step from which the dialog code hook is happening.

postCodeHookSpecification -> (structure)

Contains the responses and actions that Amazon Lex takes after the Lambda function is complete.

successResponse -> (structure)

Specifies a list of message groups that Amazon Lex uses to respond the user input.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

successNextStep -> (structure)

Specifics the next step the bot runs after the dialog code hook finishes successfully.

dialogAction -> (structure)

Defines the action that the bot executes at runtime when the conversation reaches this step.

type -> (string)

The action that the bot should execute.

slotToElicit -> (string)

If the dialog action is `ElicitSlot` , defines the slot to elicit from the user.

suppressNextMessage -> (boolean)

When true the next message for the intent is not used.

intent -> (structure)

Override settings to configure the intent state.

name -> (string)

The name of the intent. Only required when youâre switching intents.

slots -> (map)

A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map arenât overridden.

key -> (string)

value -> (structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

successConditional -> (structure)

A list of conditional branches to evaluate after the dialog code hook finishes successfully.

active -> (boolean)

Determines whether a conditional branch is active. When `active` is false, the conditions are not evaluated.

conditionalBranches -> (list)

A list of conditional branches. A conditional branch is made up of a condition, a response and a next step. The response and next step are executed when the condition is true.

(structure)

A set of actions that Amazon Lex should run if the condition is matched.

name -> (string)

The name of the branch.

condition -> (structure)

Contains the expression to evaluate. If the condition is true, the branchâs actions are taken.

expressionString -> (string)

The expression string that is evaluated.

nextStep -> (structure)

The next step in the conversation.

dialogAction -> (structure)

Defines the action that the bot executes at runtime when the conversation reaches this step.

type -> (string)

The action that the bot should execute.

slotToElicit -> (string)

If the dialog action is `ElicitSlot` , defines the slot to elicit from the user.

suppressNextMessage -> (boolean)

When true the next message for the intent is not used.

intent -> (structure)

Override settings to configure the intent state.

name -> (string)

The name of the intent. Only required when youâre switching intents.

slots -> (map)

A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map arenât overridden.

key -> (string)

value -> (structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

response -> (structure)

Specifies a list of message groups that Amazon Lex uses to respond the user input.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

defaultBranch -> (structure)

The conditional branch that should be followed when the conditions for other branches are not satisfied. A conditional branch is made up of a condition, a response and a next step.

nextStep -> (structure)

The next step in the conversation.

dialogAction -> (structure)

Defines the action that the bot executes at runtime when the conversation reaches this step.

type -> (string)

The action that the bot should execute.

slotToElicit -> (string)

If the dialog action is `ElicitSlot` , defines the slot to elicit from the user.

suppressNextMessage -> (boolean)

When true the next message for the intent is not used.

intent -> (structure)

Override settings to configure the intent state.

name -> (string)

The name of the intent. Only required when youâre switching intents.

slots -> (map)

A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map arenât overridden.

key -> (string)

value -> (structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

response -> (structure)

Specifies a list of message groups that Amazon Lex uses to respond the user input.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

failureResponse -> (structure)

Specifies a list of message groups that Amazon Lex uses to respond the user input.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

failureNextStep -> (structure)

Specifies the next step the bot runs after the dialog code hook throws an exception or returns with the `State` field of the `Intent` object set to `Failed` .

dialogAction -> (structure)

Defines the action that the bot executes at runtime when the conversation reaches this step.

type -> (string)

The action that the bot should execute.

slotToElicit -> (string)

If the dialog action is `ElicitSlot` , defines the slot to elicit from the user.

suppressNextMessage -> (boolean)

When true the next message for the intent is not used.

intent -> (structure)

Override settings to configure the intent state.

name -> (string)

The name of the intent. Only required when youâre switching intents.

slots -> (map)

A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map arenât overridden.

key -> (string)

value -> (structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

failureConditional -> (structure)

A list of conditional branches to evaluate after the dialog code hook throws an exception or returns with the `State` field of the `Intent` object set to `Failed` .

active -> (boolean)

Determines whether a conditional branch is active. When `active` is false, the conditions are not evaluated.

conditionalBranches -> (list)

A list of conditional branches. A conditional branch is made up of a condition, a response and a next step. The response and next step are executed when the condition is true.

(structure)

A set of actions that Amazon Lex should run if the condition is matched.

name -> (string)

The name of the branch.

condition -> (structure)

Contains the expression to evaluate. If the condition is true, the branchâs actions are taken.

expressionString -> (string)

The expression string that is evaluated.

nextStep -> (structure)

The next step in the conversation.

dialogAction -> (structure)

Defines the action that the bot executes at runtime when the conversation reaches this step.

type -> (string)

The action that the bot should execute.

slotToElicit -> (string)

If the dialog action is `ElicitSlot` , defines the slot to elicit from the user.

suppressNextMessage -> (boolean)

When true the next message for the intent is not used.

intent -> (structure)

Override settings to configure the intent state.

name -> (string)

The name of the intent. Only required when youâre switching intents.

slots -> (map)

A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map arenât overridden.

key -> (string)

value -> (structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

response -> (structure)

Specifies a list of message groups that Amazon Lex uses to respond the user input.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

defaultBranch -> (structure)

The conditional branch that should be followed when the conditions for other branches are not satisfied. A conditional branch is made up of a condition, a response and a next step.

nextStep -> (structure)

The next step in the conversation.

dialogAction -> (structure)

Defines the action that the bot executes at runtime when the conversation reaches this step.

type -> (string)

The action that the bot should execute.

slotToElicit -> (string)

If the dialog action is `ElicitSlot` , defines the slot to elicit from the user.

suppressNextMessage -> (boolean)

When true the next message for the intent is not used.

intent -> (structure)

Override settings to configure the intent state.

name -> (string)

The name of the intent. Only required when youâre switching intents.

slots -> (map)

A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map arenât overridden.

key -> (string)

value -> (structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

response -> (structure)

Specifies a list of message groups that Amazon Lex uses to respond the user input.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

timeoutResponse -> (structure)

Specifies a list of message groups that Amazon Lex uses to respond the user input.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

timeoutNextStep -> (structure)

Specifies the next step that the bot runs when the code hook times out.

dialogAction -> (structure)

Defines the action that the bot executes at runtime when the conversation reaches this step.

type -> (string)

The action that the bot should execute.

slotToElicit -> (string)

If the dialog action is `ElicitSlot` , defines the slot to elicit from the user.

suppressNextMessage -> (boolean)

When true the next message for the intent is not used.

intent -> (structure)

Override settings to configure the intent state.

name -> (string)

The name of the intent. Only required when youâre switching intents.

slots -> (map)

A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map arenât overridden.

key -> (string)

value -> (structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

timeoutConditional -> (structure)

A list of conditional branches to evaluate if the code hook times out.

active -> (boolean)

Determines whether a conditional branch is active. When `active` is false, the conditions are not evaluated.

conditionalBranches -> (list)

A list of conditional branches. A conditional branch is made up of a condition, a response and a next step. The response and next step are executed when the condition is true.

(structure)

A set of actions that Amazon Lex should run if the condition is matched.

name -> (string)

The name of the branch.

condition -> (structure)

Contains the expression to evaluate. If the condition is true, the branchâs actions are taken.

expressionString -> (string)

The expression string that is evaluated.

nextStep -> (structure)

The next step in the conversation.

dialogAction -> (structure)

Defines the action that the bot executes at runtime when the conversation reaches this step.

type -> (string)

The action that the bot should execute.

slotToElicit -> (string)

If the dialog action is `ElicitSlot` , defines the slot to elicit from the user.

suppressNextMessage -> (boolean)

When true the next message for the intent is not used.

intent -> (structure)

Override settings to configure the intent state.

name -> (string)

The name of the intent. Only required when youâre switching intents.

slots -> (map)

A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map arenât overridden.

key -> (string)

value -> (structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

response -> (structure)

Specifies a list of message groups that Amazon Lex uses to respond the user input.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

defaultBranch -> (structure)

The conditional branch that should be followed when the conditions for other branches are not satisfied. A conditional branch is made up of a condition, a response and a next step.

nextStep -> (structure)

The next step in the conversation.

dialogAction -> (structure)

Defines the action that the bot executes at runtime when the conversation reaches this step.

type -> (string)

The action that the bot should execute.

slotToElicit -> (string)

If the dialog action is `ElicitSlot` , defines the slot to elicit from the user.

suppressNextMessage -> (boolean)

When true the next message for the intent is not used.

intent -> (structure)

Override settings to configure the intent state.

name -> (string)

The name of the intent. Only required when youâre switching intents.

slots -> (map)

A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map arenât overridden.

key -> (string)

value -> (structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

The slot values that Amazon Lex uses when it sets slot values in a dialog step.

shape -> (string)

When the shape value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

value -> (structure)

The current value of the slot.

interpretedValue -> (string)

The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the `resolvedValues` list.

values -> (list)

A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

key -> (string)

value -> (string)

response -> (structure)

Specifies a list of message groups that Amazon Lex uses to respond the user input.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

elicitationCodeHook -> (structure)

Code hook called when Amazon Lex doesnât capture a slot value.

enableCodeHookInvocation -> (boolean)

Indicates whether a Lambda function should be invoked for the dialog.

invocationLabel -> (string)

A label that indicates the dialog step from which the dialog code hook is happening.

slotResolutionSetting -> (structure)

An object containing information about whether assisted slot resolution is turned on for the slot or not.

slotResolutionStrategy -> (string)

Specifies whether assisted slot resolution is turned on for the slot or not. If the value is `EnhancedFallback` , assisted slot resolution is activated when Amazon Lex defaults to the `AMAZON.FallbackIntent` . If the value is `Default` , assisted slot resolution is turned off.

obfuscationSetting -> (structure)

Whether slot values are shown in Amazon CloudWatch logs. If the value is `None` , the actual value of the slot is shown in logs.

obfuscationSettingType -> (string)

Value that determines whether Amazon Lex obscures slot values in conversation logs. The default is to obscure the values.

botId -> (string)

The identifier of the bot associated with the slot.

botVersion -> (string)

The version of the bot associated with the slot.

localeId -> (string)

The language and locale specified for the slot.

intentId -> (string)

The identifier of the intent associated with the slot.

creationDateTime -> (timestamp)

A timestamp of the date and time that the slot was created.

lastUpdatedDateTime -> (timestamp)

A timestamp of the date and time that the slot was last updated.

multipleValuesSetting -> (structure)

Indicates whether the slot accepts multiple values in a single utterance.

If the `multipleValuesSetting` is not set, the default value is `false` .

allowMultipleValues -> (boolean)

Indicates whether a slot can return multiple values. When `true` , the slot may return more than one value in a response. When `false` , the slot returns only a single value.

Multi-value slots are only available in the en-US locale. If you set this value to `true` in any other locale, Amazon Lex throws a `ValidationException` .

If the `allowMutlipleValues` is not set, the default value is `false` .

subSlotSetting -> (structure)

Specifications for the constituent sub slots and the expression for the composite slot.

expression -> (string)

The expression text for defining the constituent sub slots in the composite slot using logical AND and OR operators.

slotSpecifications -> (map)

Specifications for the constituent sub slots of a composite slot.

key -> (string)

value -> (structure)

Subslot specifications.

slotTypeId -> (string)

The unique identifier assigned to the slot type.

valueElicitationSetting -> (structure)

Specifies the elicitation setting details for constituent sub slots of a composite slot.

defaultValueSpecification -> (structure)

Defines a list of values that Amazon Lex should use as the default value for a slot.

defaultValueList -> (list)

A list of default values. Amazon Lex chooses the default value to use in the order that they are presented in the list.

(structure)

Specifies the default value to use when a user doesnât provide a value for a slot.

defaultValue -> (string)

The default value to use when a user doesnât provide a value for a slot.

promptSpecification -> (structure)

Specifies a list of message groups that Amazon Lex sends to a user to elicit a response.

messageGroups -> (list)

A collection of messages that Amazon Lex can send to the user. Amazon Lex chooses the actual message to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

maxRetries -> (integer)

The maximum number of times the bot tries to elicit a response from the user using this prompt.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech prompt from the bot.

messageSelectionStrategy -> (string)

Indicates how a message is selected from a message group among retries.

promptAttemptsSpecification -> (map)

Specifies the advanced settings on each attempt of the prompt.

key -> (string)

The attempt name of attempts of a prompt.

value -> (structure)

Specifies the settings on a prompt attempt.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech prompt attempt from the bot.

allowedInputTypes -> (structure)

Indicates the allowed input types of the prompt attempt.

allowAudioInput -> (boolean)

Indicates whether audio input is allowed.

allowDTMFInput -> (boolean)

Indicates whether DTMF input is allowed.

audioAndDTMFInputSpecification -> (structure)

Specifies the settings on audio and DTMF input.

startTimeoutMs -> (integer)

Time for which a bot waits before assuming that the customer isnât going to speak or press a key. This timeout is shared between Audio and DTMF inputs.

audioSpecification -> (structure)

Specifies the settings on audio input.

maxLengthMs -> (integer)

Time for how long Amazon Lex waits before speech input is truncated and the speech is returned to application.

endTimeoutMs -> (integer)

Time for which a bot waits after the customer stops speaking to assume the utterance is finished.

dtmfSpecification -> (structure)

Specifies the settings on DTMF input.

maxLength -> (integer)

The maximum number of DTMF digits allowed in an utterance.

endTimeoutMs -> (integer)

How long the bot should wait after the last DTMF character input before assuming that the input has concluded.

deletionCharacter -> (string)

The DTMF character that clears the accumulated DTMF digits and immediately ends the input.

endCharacter -> (string)

The DTMF character that immediately ends input. If the user does not press this character, the input ends after the end timeout.

textInputSpecification -> (structure)

Specifies the settings on text input.

startTimeoutMs -> (integer)

Time for which a bot waits before re-prompting a customer for text input.

sampleUtterances -> (list)

If you know a specific pattern that users might respond to an Amazon Lex request for a sub slot value, you can provide those utterances to improve accuracy. This is optional. In most cases Amazon Lex is capable of understanding user utterances. This is similar to `SampleUtterances` for slots.

(structure)

A sample utterance that invokes an intent or respond to a slot elicitation prompt.

utterance -> (string)

The sample utterance that Amazon Lex uses to build its machine-learning model to recognize intents.

waitAndContinueSpecification -> (structure)

Specifies the prompts that Amazon Lex uses while a bot is waiting for customer input.

waitingResponse -> (structure)

The response that Amazon Lex sends to indicate that the bot is waiting for the conversation to continue.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

continueResponse -> (structure)

The response that Amazon Lex sends to indicate that the bot is ready to continue the conversation.

messageGroups -> (list)

A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

allowInterrupt -> (boolean)

Indicates whether the user can interrupt a speech response from Amazon Lex.

stillWaitingResponse -> (structure)

A response that Amazon Lex sends periodically to the user to indicate that the bot is still waiting for input from the user.

messageGroups -> (list)

One or more message groups, each containing one or more messages, that define the prompts that Amazon Lex sends to the user.

(structure)

Provides one or more messages that Amazon Lex should send to the user.

message -> (structure)

The primary message that Amazon Lex should send to the user.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

variations -> (list)

Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

(structure)

The object that provides message text and its type.

plainTextMessage -> (structure)

A message in plain text format.

value -> (string)

The message to send to the user.

customPayload -> (structure)

A message in a custom format defined by the client application.

value -> (string)

The string that is sent to your application.

ssmlMessage -> (structure)

A message in Speech Synthesis Markup Language (SSML).

value -> (string)

The SSML text that defines the prompt.

imageResponseCard -> (structure)

A message that defines a response card that the client application can show to the user.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

frequencyInSeconds -> (integer)

How often a message should be sent to the user. Minimum of 1 second, maximum of 5 minutes.

timeoutInSeconds -> (integer)

If Amazon Lex waits longer than this length of time for a response, it will stop sending messages.

allowInterrupt -> (boolean)

Indicates that the user can interrupt the response by speaking while the message is being played.

active -> (boolean)

Specifies whether the bot will wait for a user to respond. When this field is false, wait and continue responses for a slot arenât used. If the `active` field isnât specified, the default is true.