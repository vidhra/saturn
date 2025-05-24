# update-intentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/update-intent.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/update-intent.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# update-intent

## Description

Updates the settings for an intent.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/UpdateIntent)

## Synopsis

```
update-intent
--intent-id <value>
--intent-name <value>
[--description <value>]
[--parent-intent-signature <value>]
[--sample-utterances <value>]
[--dialog-code-hook <value>]
[--fulfillment-code-hook <value>]
[--slot-priorities <value>]
[--intent-confirmation-setting <value>]
[--intent-closing-setting <value>]
[--input-contexts <value>]
[--output-contexts <value>]
[--kendra-configuration <value>]
--bot-id <value>
--bot-version <value>
--locale-id <value>
[--initial-response-setting <value>]
[--qn-a-intent-configuration <value>]
[--q-in-connect-intent-configuration <value>]
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

`--intent-id` (string)

The unique identifier of the intent to update.

`--intent-name` (string)

The new name for the intent.

`--description` (string)

The new description of the intent.

`--parent-intent-signature` (string)

The signature of the new built-in intent to use as the parent of this intent.

`--sample-utterances` (list)

New utterances used to invoke the intent.

(structure)

A sample utterance that invokes an intent or respond to a slot elicitation prompt.

utterance -> (string)

The sample utterance that Amazon Lex uses to build its machine-learning model to recognize intents.

Shorthand Syntax:

```
utterance=string ...
```

JSON Syntax:

```
[
  {
    "utterance": "string"
  }
  ...
]
```

`--dialog-code-hook` (structure)

The new Lambda function to use between each turn of the conversation with the bot.

enabled -> (boolean)

Enables the dialog code hook so that it processes user requests.

Shorthand Syntax:

```
enabled=boolean
```

JSON Syntax:

```
{
  "enabled": true|false
}
```

`--fulfillment-code-hook` (structure)

The new Lambda function to call when all of the intents required slots are provided and the intent is ready for fulfillment.

enabled -> (boolean)

Indicates whether a Lambda function should be invoked to fulfill a specific intent.

postFulfillmentStatusSpecification -> (structure)

Provides settings for messages sent to the user for after the Lambda fulfillment function completes. Post-fulfillment messages can be sent for both streaming and non-streaming conversations.

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

successNextStep -> (structure)

Specifies the next step in the conversation that Amazon Lex invokes when the fulfillment code hook completes successfully.

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

A list of conditional branches to evaluate after the fulfillment code hook finishes successfully.

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

failureNextStep -> (structure)

Specifies the next step the bot runs after the fulfillment code hook throws an exception or returns with the `State` field of the `Intent` object set to `Failed` .

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

A list of conditional branches to evaluate after the fulfillment code hook throws an exception or returns with the `State` field of the `Intent` object set to `Failed` .

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

timeoutNextStep -> (structure)

Specifies the next step that the bot runs when the fulfillment code hook times out.

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

A list of conditional branches to evaluate if the fulfillment code hook times out.

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

fulfillmentUpdatesSpecification -> (structure)

Provides settings for update messages sent to the user for long-running Lambda fulfillment functions. Fulfillment updates can be used only with streaming conversations.

active -> (boolean)

Determines whether fulfillment updates are sent to the user. When this field is true, updates are sent.

If the `active` field is set to true, the `startResponse` , `updateResponse` , and `timeoutInSeconds` fields are required.

startResponse -> (structure)

Provides configuration information for the message sent to users when the fulfillment Lambda functions starts running.

delayInSeconds -> (integer)

The delay between when the Lambda fulfillment function starts running and the start message is played. If the Lambda function returns before the delay is over, the start message isnât played.

messageGroups -> (list)

1 - 5 message groups that contain start messages. Amazon Lex chooses one of the messages to play to the user.

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

Determines whether the user can interrupt the start message while it is playing.

updateResponse -> (structure)

Provides configuration information for messages sent periodically to the user while the fulfillment Lambda function is running.

frequencyInSeconds -> (integer)

The frequency that a message is sent to the user. When the period ends, Amazon Lex chooses a message from the message groups and plays it to the user. If the fulfillment Lambda returns before the first period ends, an update message is not played to the user.

messageGroups -> (list)

1 - 5 message groups that contain update messages. Amazon Lex chooses one of the messages to play to the user.

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

Determines whether the user can interrupt an update message while it is playing.

timeoutInSeconds -> (integer)

The length of time that the fulfillment Lambda function should run before it times out.

active -> (boolean)

Determines whether the fulfillment code hook is used. When `active` is false, the code hook doesnât run.

JSON Syntax:

```
{
  "enabled": true|false,
  "postFulfillmentStatusSpecification": {
    "successResponse": {
      "messageGroups": [
        {
          "message": {
            "plainTextMessage": {
              "value": "string"
            },
            "customPayload": {
              "value": "string"
            },
            "ssmlMessage": {
              "value": "string"
            },
            "imageResponseCard": {
              "title": "string",
              "subtitle": "string",
              "imageUrl": "string",
              "buttons": [
                {
                  "text": "string",
                  "value": "string"
                }
                ...
              ]
            }
          },
          "variations": [
            {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            }
            ...
          ]
        }
        ...
      ],
      "allowInterrupt": true|false
    },
    "failureResponse": {
      "messageGroups": [
        {
          "message": {
            "plainTextMessage": {
              "value": "string"
            },
            "customPayload": {
              "value": "string"
            },
            "ssmlMessage": {
              "value": "string"
            },
            "imageResponseCard": {
              "title": "string",
              "subtitle": "string",
              "imageUrl": "string",
              "buttons": [
                {
                  "text": "string",
                  "value": "string"
                }
                ...
              ]
            }
          },
          "variations": [
            {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            }
            ...
          ]
        }
        ...
      ],
      "allowInterrupt": true|false
    },
    "timeoutResponse": {
      "messageGroups": [
        {
          "message": {
            "plainTextMessage": {
              "value": "string"
            },
            "customPayload": {
              "value": "string"
            },
            "ssmlMessage": {
              "value": "string"
            },
            "imageResponseCard": {
              "title": "string",
              "subtitle": "string",
              "imageUrl": "string",
              "buttons": [
                {
                  "text": "string",
                  "value": "string"
                }
                ...
              ]
            }
          },
          "variations": [
            {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            }
            ...
          ]
        }
        ...
      ],
      "allowInterrupt": true|false
    },
    "successNextStep": {
      "dialogAction": {
        "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
        "slotToElicit": "string",
        "suppressNextMessage": true|false
      },
      "intent": {
        "name": "string",
        "slots": {"string": {
              "shape": "Scalar"|"List",
              "value": {
                "interpretedValue": "string"
              },
              "values": [
                {
                  "shape": "Scalar"|"List",
                  "value": {
                    "interpretedValue": "string"
                  },
                  "values": [
                    { ... recursive ... }
                    ...
                  ]
                }
                ...
              ]
            }
          ...}
      },
      "sessionAttributes": {"string": "string"
        ...}
    },
    "successConditional": {
      "active": true|false,
      "conditionalBranches": [
        {
          "name": "string",
          "condition": {
            "expressionString": "string"
          },
          "nextStep": {
            "dialogAction": {
              "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
              "slotToElicit": "string",
              "suppressNextMessage": true|false
            },
            "intent": {
              "name": "string",
              "slots": {"string": {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      {
                        "shape": "Scalar"|"List",
                        "value": {
                          "interpretedValue": "string"
                        },
                        "values": [
                          { ... recursive ... }
                          ...
                        ]
                      }
                      ...
                    ]
                  }
                ...}
            },
            "sessionAttributes": {"string": "string"
              ...}
          },
          "response": {
            "messageGroups": [
              {
                "message": {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                },
                "variations": [
                  {
                    "plainTextMessage": {
                      "value": "string"
                    },
                    "customPayload": {
                      "value": "string"
                    },
                    "ssmlMessage": {
                      "value": "string"
                    },
                    "imageResponseCard": {
                      "title": "string",
                      "subtitle": "string",
                      "imageUrl": "string",
                      "buttons": [
                        {
                          "text": "string",
                          "value": "string"
                        }
                        ...
                      ]
                    }
                  }
                  ...
                ]
              }
              ...
            ],
            "allowInterrupt": true|false
          }
        }
        ...
      ],
      "defaultBranch": {
        "nextStep": {
          "dialogAction": {
            "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
            "slotToElicit": "string",
            "suppressNextMessage": true|false
          },
          "intent": {
            "name": "string",
            "slots": {"string": {
                  "shape": "Scalar"|"List",
                  "value": {
                    "interpretedValue": "string"
                  },
                  "values": [
                    {
                      "shape": "Scalar"|"List",
                      "value": {
                        "interpretedValue": "string"
                      },
                      "values": [
                        { ... recursive ... }
                        ...
                      ]
                    }
                    ...
                  ]
                }
              ...}
          },
          "sessionAttributes": {"string": "string"
            ...}
        },
        "response": {
          "messageGroups": [
            {
              "message": {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              },
              "variations": [
                {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                }
                ...
              ]
            }
            ...
          ],
          "allowInterrupt": true|false
        }
      }
    },
    "failureNextStep": {
      "dialogAction": {
        "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
        "slotToElicit": "string",
        "suppressNextMessage": true|false
      },
      "intent": {
        "name": "string",
        "slots": {"string": {
              "shape": "Scalar"|"List",
              "value": {
                "interpretedValue": "string"
              },
              "values": [
                {
                  "shape": "Scalar"|"List",
                  "value": {
                    "interpretedValue": "string"
                  },
                  "values": [
                    { ... recursive ... }
                    ...
                  ]
                }
                ...
              ]
            }
          ...}
      },
      "sessionAttributes": {"string": "string"
        ...}
    },
    "failureConditional": {
      "active": true|false,
      "conditionalBranches": [
        {
          "name": "string",
          "condition": {
            "expressionString": "string"
          },
          "nextStep": {
            "dialogAction": {
              "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
              "slotToElicit": "string",
              "suppressNextMessage": true|false
            },
            "intent": {
              "name": "string",
              "slots": {"string": {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      {
                        "shape": "Scalar"|"List",
                        "value": {
                          "interpretedValue": "string"
                        },
                        "values": [
                          { ... recursive ... }
                          ...
                        ]
                      }
                      ...
                    ]
                  }
                ...}
            },
            "sessionAttributes": {"string": "string"
              ...}
          },
          "response": {
            "messageGroups": [
              {
                "message": {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                },
                "variations": [
                  {
                    "plainTextMessage": {
                      "value": "string"
                    },
                    "customPayload": {
                      "value": "string"
                    },
                    "ssmlMessage": {
                      "value": "string"
                    },
                    "imageResponseCard": {
                      "title": "string",
                      "subtitle": "string",
                      "imageUrl": "string",
                      "buttons": [
                        {
                          "text": "string",
                          "value": "string"
                        }
                        ...
                      ]
                    }
                  }
                  ...
                ]
              }
              ...
            ],
            "allowInterrupt": true|false
          }
        }
        ...
      ],
      "defaultBranch": {
        "nextStep": {
          "dialogAction": {
            "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
            "slotToElicit": "string",
            "suppressNextMessage": true|false
          },
          "intent": {
            "name": "string",
            "slots": {"string": {
                  "shape": "Scalar"|"List",
                  "value": {
                    "interpretedValue": "string"
                  },
                  "values": [
                    {
                      "shape": "Scalar"|"List",
                      "value": {
                        "interpretedValue": "string"
                      },
                      "values": [
                        { ... recursive ... }
                        ...
                      ]
                    }
                    ...
                  ]
                }
              ...}
          },
          "sessionAttributes": {"string": "string"
            ...}
        },
        "response": {
          "messageGroups": [
            {
              "message": {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              },
              "variations": [
                {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                }
                ...
              ]
            }
            ...
          ],
          "allowInterrupt": true|false
        }
      }
    },
    "timeoutNextStep": {
      "dialogAction": {
        "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
        "slotToElicit": "string",
        "suppressNextMessage": true|false
      },
      "intent": {
        "name": "string",
        "slots": {"string": {
              "shape": "Scalar"|"List",
              "value": {
                "interpretedValue": "string"
              },
              "values": [
                {
                  "shape": "Scalar"|"List",
                  "value": {
                    "interpretedValue": "string"
                  },
                  "values": [
                    { ... recursive ... }
                    ...
                  ]
                }
                ...
              ]
            }
          ...}
      },
      "sessionAttributes": {"string": "string"
        ...}
    },
    "timeoutConditional": {
      "active": true|false,
      "conditionalBranches": [
        {
          "name": "string",
          "condition": {
            "expressionString": "string"
          },
          "nextStep": {
            "dialogAction": {
              "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
              "slotToElicit": "string",
              "suppressNextMessage": true|false
            },
            "intent": {
              "name": "string",
              "slots": {"string": {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      {
                        "shape": "Scalar"|"List",
                        "value": {
                          "interpretedValue": "string"
                        },
                        "values": [
                          { ... recursive ... }
                          ...
                        ]
                      }
                      ...
                    ]
                  }
                ...}
            },
            "sessionAttributes": {"string": "string"
              ...}
          },
          "response": {
            "messageGroups": [
              {
                "message": {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                },
                "variations": [
                  {
                    "plainTextMessage": {
                      "value": "string"
                    },
                    "customPayload": {
                      "value": "string"
                    },
                    "ssmlMessage": {
                      "value": "string"
                    },
                    "imageResponseCard": {
                      "title": "string",
                      "subtitle": "string",
                      "imageUrl": "string",
                      "buttons": [
                        {
                          "text": "string",
                          "value": "string"
                        }
                        ...
                      ]
                    }
                  }
                  ...
                ]
              }
              ...
            ],
            "allowInterrupt": true|false
          }
        }
        ...
      ],
      "defaultBranch": {
        "nextStep": {
          "dialogAction": {
            "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
            "slotToElicit": "string",
            "suppressNextMessage": true|false
          },
          "intent": {
            "name": "string",
            "slots": {"string": {
                  "shape": "Scalar"|"List",
                  "value": {
                    "interpretedValue": "string"
                  },
                  "values": [
                    {
                      "shape": "Scalar"|"List",
                      "value": {
                        "interpretedValue": "string"
                      },
                      "values": [
                        { ... recursive ... }
                        ...
                      ]
                    }
                    ...
                  ]
                }
              ...}
          },
          "sessionAttributes": {"string": "string"
            ...}
        },
        "response": {
          "messageGroups": [
            {
              "message": {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              },
              "variations": [
                {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                }
                ...
              ]
            }
            ...
          ],
          "allowInterrupt": true|false
        }
      }
    }
  },
  "fulfillmentUpdatesSpecification": {
    "active": true|false,
    "startResponse": {
      "delayInSeconds": integer,
      "messageGroups": [
        {
          "message": {
            "plainTextMessage": {
              "value": "string"
            },
            "customPayload": {
              "value": "string"
            },
            "ssmlMessage": {
              "value": "string"
            },
            "imageResponseCard": {
              "title": "string",
              "subtitle": "string",
              "imageUrl": "string",
              "buttons": [
                {
                  "text": "string",
                  "value": "string"
                }
                ...
              ]
            }
          },
          "variations": [
            {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            }
            ...
          ]
        }
        ...
      ],
      "allowInterrupt": true|false
    },
    "updateResponse": {
      "frequencyInSeconds": integer,
      "messageGroups": [
        {
          "message": {
            "plainTextMessage": {
              "value": "string"
            },
            "customPayload": {
              "value": "string"
            },
            "ssmlMessage": {
              "value": "string"
            },
            "imageResponseCard": {
              "title": "string",
              "subtitle": "string",
              "imageUrl": "string",
              "buttons": [
                {
                  "text": "string",
                  "value": "string"
                }
                ...
              ]
            }
          },
          "variations": [
            {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            }
            ...
          ]
        }
        ...
      ],
      "allowInterrupt": true|false
    },
    "timeoutInSeconds": integer
  },
  "active": true|false
}
```

`--slot-priorities` (list)

A new list of slots and their priorities that are contained by the intent.

(structure)

Sets the priority that Amazon Lex should use when eliciting slot values from a user.

priority -> (integer)

The priority that Amazon Lex should apply to the slot.

slotId -> (string)

The unique identifier of the slot.

Shorthand Syntax:

```
priority=integer,slotId=string ...
```

JSON Syntax:

```
[
  {
    "priority": integer,
    "slotId": "string"
  }
  ...
]
```

`--intent-confirmation-setting` (structure)

New prompts that Amazon Lex sends to the user to confirm the completion of an intent.

promptSpecification -> (structure)

Prompts the user to confirm the intent. This question should have a yes or no answer.

Amazon Lex uses this prompt to ensure that the user acknowledges that the intent is ready for fulfillment. For example, with the `OrderPizza` intent, you might want to confirm that the order is correct before placing it. For other intents, such as intents that simply respond to user questions, you might not need to ask the user for confirmation before providing the information.

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

declinationResponse -> (structure)

When the user answers ânoâ to the question defined in `promptSpecification` , Amazon Lex responds with this response to acknowledge that the intent was canceled.

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

active -> (boolean)

Specifies whether the intentâs confirmation is sent to the user. When this field is false, confirmation and declination responses arenât sent. If the `active` field isnât specified, the default is true.

confirmationResponse -> (structure)

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

confirmationNextStep -> (structure)

Specifies the next step that the bot executes when the customer confirms the intent.

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

confirmationConditional -> (structure)

A list of conditional branches to evaluate after the intent is closed.

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

declinationNextStep -> (structure)

Specifies the next step that the bot executes when the customer declines the intent.

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

declinationConditional -> (structure)

A list of conditional branches to evaluate after the intent is declined.

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

The next step to take in the conversation if the confirmation step fails.

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

Provides a list of conditional branches. Branches are evaluated in the order that they are entered in the list. The first branch with a condition that evaluates to true is executed. The last branch in the list is the default branch. The default branch should not have any condition expression. The default branch is executed if no other branch has a matching condition.

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

The `DialogCodeHookInvocationSetting` object associated with intentâs confirmation step. The dialog code hook is triggered based on these invocation settings when the confirmation next step or declination next step or failure next step is `InvokeDialogCodeHook` .

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

The `DialogCodeHookInvocationSetting` used when the code hook is invoked during confirmation prompt retries.

enableCodeHookInvocation -> (boolean)

Indicates whether a Lambda function should be invoked for the dialog.

invocationLabel -> (string)

A label that indicates the dialog step from which the dialog code hook is happening.

JSON Syntax:

```
{
  "promptSpecification": {
    "messageGroups": [
      {
        "message": {
          "plainTextMessage": {
            "value": "string"
          },
          "customPayload": {
            "value": "string"
          },
          "ssmlMessage": {
            "value": "string"
          },
          "imageResponseCard": {
            "title": "string",
            "subtitle": "string",
            "imageUrl": "string",
            "buttons": [
              {
                "text": "string",
                "value": "string"
              }
              ...
            ]
          }
        },
        "variations": [
          {
            "plainTextMessage": {
              "value": "string"
            },
            "customPayload": {
              "value": "string"
            },
            "ssmlMessage": {
              "value": "string"
            },
            "imageResponseCard": {
              "title": "string",
              "subtitle": "string",
              "imageUrl": "string",
              "buttons": [
                {
                  "text": "string",
                  "value": "string"
                }
                ...
              ]
            }
          }
          ...
        ]
      }
      ...
    ],
    "maxRetries": integer,
    "allowInterrupt": true|false,
    "messageSelectionStrategy": "Random"|"Ordered",
    "promptAttemptsSpecification": {"Initial"|"Retry1"|"Retry2"|"Retry3"|"Retry4"|"Retry5": {
          "allowInterrupt": true|false,
          "allowedInputTypes": {
            "allowAudioInput": true|false,
            "allowDTMFInput": true|false
          },
          "audioAndDTMFInputSpecification": {
            "startTimeoutMs": integer,
            "audioSpecification": {
              "maxLengthMs": integer,
              "endTimeoutMs": integer
            },
            "dtmfSpecification": {
              "maxLength": integer,
              "endTimeoutMs": integer,
              "deletionCharacter": "string",
              "endCharacter": "string"
            }
          },
          "textInputSpecification": {
            "startTimeoutMs": integer
          }
        }
      ...}
  },
  "declinationResponse": {
    "messageGroups": [
      {
        "message": {
          "plainTextMessage": {
            "value": "string"
          },
          "customPayload": {
            "value": "string"
          },
          "ssmlMessage": {
            "value": "string"
          },
          "imageResponseCard": {
            "title": "string",
            "subtitle": "string",
            "imageUrl": "string",
            "buttons": [
              {
                "text": "string",
                "value": "string"
              }
              ...
            ]
          }
        },
        "variations": [
          {
            "plainTextMessage": {
              "value": "string"
            },
            "customPayload": {
              "value": "string"
            },
            "ssmlMessage": {
              "value": "string"
            },
            "imageResponseCard": {
              "title": "string",
              "subtitle": "string",
              "imageUrl": "string",
              "buttons": [
                {
                  "text": "string",
                  "value": "string"
                }
                ...
              ]
            }
          }
          ...
        ]
      }
      ...
    ],
    "allowInterrupt": true|false
  },
  "active": true|false,
  "confirmationResponse": {
    "messageGroups": [
      {
        "message": {
          "plainTextMessage": {
            "value": "string"
          },
          "customPayload": {
            "value": "string"
          },
          "ssmlMessage": {
            "value": "string"
          },
          "imageResponseCard": {
            "title": "string",
            "subtitle": "string",
            "imageUrl": "string",
            "buttons": [
              {
                "text": "string",
                "value": "string"
              }
              ...
            ]
          }
        },
        "variations": [
          {
            "plainTextMessage": {
              "value": "string"
            },
            "customPayload": {
              "value": "string"
            },
            "ssmlMessage": {
              "value": "string"
            },
            "imageResponseCard": {
              "title": "string",
              "subtitle": "string",
              "imageUrl": "string",
              "buttons": [
                {
                  "text": "string",
                  "value": "string"
                }
                ...
              ]
            }
          }
          ...
        ]
      }
      ...
    ],
    "allowInterrupt": true|false
  },
  "confirmationNextStep": {
    "dialogAction": {
      "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
      "slotToElicit": "string",
      "suppressNextMessage": true|false
    },
    "intent": {
      "name": "string",
      "slots": {"string": {
            "shape": "Scalar"|"List",
            "value": {
              "interpretedValue": "string"
            },
            "values": [
              {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  { ... recursive ... }
                  ...
                ]
              }
              ...
            ]
          }
        ...}
    },
    "sessionAttributes": {"string": "string"
      ...}
  },
  "confirmationConditional": {
    "active": true|false,
    "conditionalBranches": [
      {
        "name": "string",
        "condition": {
          "expressionString": "string"
        },
        "nextStep": {
          "dialogAction": {
            "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
            "slotToElicit": "string",
            "suppressNextMessage": true|false
          },
          "intent": {
            "name": "string",
            "slots": {"string": {
                  "shape": "Scalar"|"List",
                  "value": {
                    "interpretedValue": "string"
                  },
                  "values": [
                    {
                      "shape": "Scalar"|"List",
                      "value": {
                        "interpretedValue": "string"
                      },
                      "values": [
                        { ... recursive ... }
                        ...
                      ]
                    }
                    ...
                  ]
                }
              ...}
          },
          "sessionAttributes": {"string": "string"
            ...}
        },
        "response": {
          "messageGroups": [
            {
              "message": {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              },
              "variations": [
                {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                }
                ...
              ]
            }
            ...
          ],
          "allowInterrupt": true|false
        }
      }
      ...
    ],
    "defaultBranch": {
      "nextStep": {
        "dialogAction": {
          "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
          "slotToElicit": "string",
          "suppressNextMessage": true|false
        },
        "intent": {
          "name": "string",
          "slots": {"string": {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      { ... recursive ... }
                      ...
                    ]
                  }
                  ...
                ]
              }
            ...}
        },
        "sessionAttributes": {"string": "string"
          ...}
      },
      "response": {
        "messageGroups": [
          {
            "message": {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            },
            "variations": [
              {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              }
              ...
            ]
          }
          ...
        ],
        "allowInterrupt": true|false
      }
    }
  },
  "declinationNextStep": {
    "dialogAction": {
      "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
      "slotToElicit": "string",
      "suppressNextMessage": true|false
    },
    "intent": {
      "name": "string",
      "slots": {"string": {
            "shape": "Scalar"|"List",
            "value": {
              "interpretedValue": "string"
            },
            "values": [
              {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  { ... recursive ... }
                  ...
                ]
              }
              ...
            ]
          }
        ...}
    },
    "sessionAttributes": {"string": "string"
      ...}
  },
  "declinationConditional": {
    "active": true|false,
    "conditionalBranches": [
      {
        "name": "string",
        "condition": {
          "expressionString": "string"
        },
        "nextStep": {
          "dialogAction": {
            "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
            "slotToElicit": "string",
            "suppressNextMessage": true|false
          },
          "intent": {
            "name": "string",
            "slots": {"string": {
                  "shape": "Scalar"|"List",
                  "value": {
                    "interpretedValue": "string"
                  },
                  "values": [
                    {
                      "shape": "Scalar"|"List",
                      "value": {
                        "interpretedValue": "string"
                      },
                      "values": [
                        { ... recursive ... }
                        ...
                      ]
                    }
                    ...
                  ]
                }
              ...}
          },
          "sessionAttributes": {"string": "string"
            ...}
        },
        "response": {
          "messageGroups": [
            {
              "message": {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              },
              "variations": [
                {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                }
                ...
              ]
            }
            ...
          ],
          "allowInterrupt": true|false
        }
      }
      ...
    ],
    "defaultBranch": {
      "nextStep": {
        "dialogAction": {
          "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
          "slotToElicit": "string",
          "suppressNextMessage": true|false
        },
        "intent": {
          "name": "string",
          "slots": {"string": {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      { ... recursive ... }
                      ...
                    ]
                  }
                  ...
                ]
              }
            ...}
        },
        "sessionAttributes": {"string": "string"
          ...}
      },
      "response": {
        "messageGroups": [
          {
            "message": {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            },
            "variations": [
              {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              }
              ...
            ]
          }
          ...
        ],
        "allowInterrupt": true|false
      }
    }
  },
  "failureResponse": {
    "messageGroups": [
      {
        "message": {
          "plainTextMessage": {
            "value": "string"
          },
          "customPayload": {
            "value": "string"
          },
          "ssmlMessage": {
            "value": "string"
          },
          "imageResponseCard": {
            "title": "string",
            "subtitle": "string",
            "imageUrl": "string",
            "buttons": [
              {
                "text": "string",
                "value": "string"
              }
              ...
            ]
          }
        },
        "variations": [
          {
            "plainTextMessage": {
              "value": "string"
            },
            "customPayload": {
              "value": "string"
            },
            "ssmlMessage": {
              "value": "string"
            },
            "imageResponseCard": {
              "title": "string",
              "subtitle": "string",
              "imageUrl": "string",
              "buttons": [
                {
                  "text": "string",
                  "value": "string"
                }
                ...
              ]
            }
          }
          ...
        ]
      }
      ...
    ],
    "allowInterrupt": true|false
  },
  "failureNextStep": {
    "dialogAction": {
      "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
      "slotToElicit": "string",
      "suppressNextMessage": true|false
    },
    "intent": {
      "name": "string",
      "slots": {"string": {
            "shape": "Scalar"|"List",
            "value": {
              "interpretedValue": "string"
            },
            "values": [
              {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  { ... recursive ... }
                  ...
                ]
              }
              ...
            ]
          }
        ...}
    },
    "sessionAttributes": {"string": "string"
      ...}
  },
  "failureConditional": {
    "active": true|false,
    "conditionalBranches": [
      {
        "name": "string",
        "condition": {
          "expressionString": "string"
        },
        "nextStep": {
          "dialogAction": {
            "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
            "slotToElicit": "string",
            "suppressNextMessage": true|false
          },
          "intent": {
            "name": "string",
            "slots": {"string": {
                  "shape": "Scalar"|"List",
                  "value": {
                    "interpretedValue": "string"
                  },
                  "values": [
                    {
                      "shape": "Scalar"|"List",
                      "value": {
                        "interpretedValue": "string"
                      },
                      "values": [
                        { ... recursive ... }
                        ...
                      ]
                    }
                    ...
                  ]
                }
              ...}
          },
          "sessionAttributes": {"string": "string"
            ...}
        },
        "response": {
          "messageGroups": [
            {
              "message": {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              },
              "variations": [
                {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                }
                ...
              ]
            }
            ...
          ],
          "allowInterrupt": true|false
        }
      }
      ...
    ],
    "defaultBranch": {
      "nextStep": {
        "dialogAction": {
          "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
          "slotToElicit": "string",
          "suppressNextMessage": true|false
        },
        "intent": {
          "name": "string",
          "slots": {"string": {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      { ... recursive ... }
                      ...
                    ]
                  }
                  ...
                ]
              }
            ...}
        },
        "sessionAttributes": {"string": "string"
          ...}
      },
      "response": {
        "messageGroups": [
          {
            "message": {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            },
            "variations": [
              {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              }
              ...
            ]
          }
          ...
        ],
        "allowInterrupt": true|false
      }
    }
  },
  "codeHook": {
    "enableCodeHookInvocation": true|false,
    "active": true|false,
    "invocationLabel": "string",
    "postCodeHookSpecification": {
      "successResponse": {
        "messageGroups": [
          {
            "message": {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            },
            "variations": [
              {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              }
              ...
            ]
          }
          ...
        ],
        "allowInterrupt": true|false
      },
      "successNextStep": {
        "dialogAction": {
          "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
          "slotToElicit": "string",
          "suppressNextMessage": true|false
        },
        "intent": {
          "name": "string",
          "slots": {"string": {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      { ... recursive ... }
                      ...
                    ]
                  }
                  ...
                ]
              }
            ...}
        },
        "sessionAttributes": {"string": "string"
          ...}
      },
      "successConditional": {
        "active": true|false,
        "conditionalBranches": [
          {
            "name": "string",
            "condition": {
              "expressionString": "string"
            },
            "nextStep": {
              "dialogAction": {
                "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
                "slotToElicit": "string",
                "suppressNextMessage": true|false
              },
              "intent": {
                "name": "string",
                "slots": {"string": {
                      "shape": "Scalar"|"List",
                      "value": {
                        "interpretedValue": "string"
                      },
                      "values": [
                        {
                          "shape": "Scalar"|"List",
                          "value": {
                            "interpretedValue": "string"
                          },
                          "values": [
                            { ... recursive ... }
                            ...
                          ]
                        }
                        ...
                      ]
                    }
                  ...}
              },
              "sessionAttributes": {"string": "string"
                ...}
            },
            "response": {
              "messageGroups": [
                {
                  "message": {
                    "plainTextMessage": {
                      "value": "string"
                    },
                    "customPayload": {
                      "value": "string"
                    },
                    "ssmlMessage": {
                      "value": "string"
                    },
                    "imageResponseCard": {
                      "title": "string",
                      "subtitle": "string",
                      "imageUrl": "string",
                      "buttons": [
                        {
                          "text": "string",
                          "value": "string"
                        }
                        ...
                      ]
                    }
                  },
                  "variations": [
                    {
                      "plainTextMessage": {
                        "value": "string"
                      },
                      "customPayload": {
                        "value": "string"
                      },
                      "ssmlMessage": {
                        "value": "string"
                      },
                      "imageResponseCard": {
                        "title": "string",
                        "subtitle": "string",
                        "imageUrl": "string",
                        "buttons": [
                          {
                            "text": "string",
                            "value": "string"
                          }
                          ...
                        ]
                      }
                    }
                    ...
                  ]
                }
                ...
              ],
              "allowInterrupt": true|false
            }
          }
          ...
        ],
        "defaultBranch": {
          "nextStep": {
            "dialogAction": {
              "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
              "slotToElicit": "string",
              "suppressNextMessage": true|false
            },
            "intent": {
              "name": "string",
              "slots": {"string": {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      {
                        "shape": "Scalar"|"List",
                        "value": {
                          "interpretedValue": "string"
                        },
                        "values": [
                          { ... recursive ... }
                          ...
                        ]
                      }
                      ...
                    ]
                  }
                ...}
            },
            "sessionAttributes": {"string": "string"
              ...}
          },
          "response": {
            "messageGroups": [
              {
                "message": {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                },
                "variations": [
                  {
                    "plainTextMessage": {
                      "value": "string"
                    },
                    "customPayload": {
                      "value": "string"
                    },
                    "ssmlMessage": {
                      "value": "string"
                    },
                    "imageResponseCard": {
                      "title": "string",
                      "subtitle": "string",
                      "imageUrl": "string",
                      "buttons": [
                        {
                          "text": "string",
                          "value": "string"
                        }
                        ...
                      ]
                    }
                  }
                  ...
                ]
              }
              ...
            ],
            "allowInterrupt": true|false
          }
        }
      },
      "failureResponse": {
        "messageGroups": [
          {
            "message": {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            },
            "variations": [
              {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              }
              ...
            ]
          }
          ...
        ],
        "allowInterrupt": true|false
      },
      "failureNextStep": {
        "dialogAction": {
          "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
          "slotToElicit": "string",
          "suppressNextMessage": true|false
        },
        "intent": {
          "name": "string",
          "slots": {"string": {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      { ... recursive ... }
                      ...
                    ]
                  }
                  ...
                ]
              }
            ...}
        },
        "sessionAttributes": {"string": "string"
          ...}
      },
      "failureConditional": {
        "active": true|false,
        "conditionalBranches": [
          {
            "name": "string",
            "condition": {
              "expressionString": "string"
            },
            "nextStep": {
              "dialogAction": {
                "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
                "slotToElicit": "string",
                "suppressNextMessage": true|false
              },
              "intent": {
                "name": "string",
                "slots": {"string": {
                      "shape": "Scalar"|"List",
                      "value": {
                        "interpretedValue": "string"
                      },
                      "values": [
                        {
                          "shape": "Scalar"|"List",
                          "value": {
                            "interpretedValue": "string"
                          },
                          "values": [
                            { ... recursive ... }
                            ...
                          ]
                        }
                        ...
                      ]
                    }
                  ...}
              },
              "sessionAttributes": {"string": "string"
                ...}
            },
            "response": {
              "messageGroups": [
                {
                  "message": {
                    "plainTextMessage": {
                      "value": "string"
                    },
                    "customPayload": {
                      "value": "string"
                    },
                    "ssmlMessage": {
                      "value": "string"
                    },
                    "imageResponseCard": {
                      "title": "string",
                      "subtitle": "string",
                      "imageUrl": "string",
                      "buttons": [
                        {
                          "text": "string",
                          "value": "string"
                        }
                        ...
                      ]
                    }
                  },
                  "variations": [
                    {
                      "plainTextMessage": {
                        "value": "string"
                      },
                      "customPayload": {
                        "value": "string"
                      },
                      "ssmlMessage": {
                        "value": "string"
                      },
                      "imageResponseCard": {
                        "title": "string",
                        "subtitle": "string",
                        "imageUrl": "string",
                        "buttons": [
                          {
                            "text": "string",
                            "value": "string"
                          }
                          ...
                        ]
                      }
                    }
                    ...
                  ]
                }
                ...
              ],
              "allowInterrupt": true|false
            }
          }
          ...
        ],
        "defaultBranch": {
          "nextStep": {
            "dialogAction": {
              "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
              "slotToElicit": "string",
              "suppressNextMessage": true|false
            },
            "intent": {
              "name": "string",
              "slots": {"string": {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      {
                        "shape": "Scalar"|"List",
                        "value": {
                          "interpretedValue": "string"
                        },
                        "values": [
                          { ... recursive ... }
                          ...
                        ]
                      }
                      ...
                    ]
                  }
                ...}
            },
            "sessionAttributes": {"string": "string"
              ...}
          },
          "response": {
            "messageGroups": [
              {
                "message": {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                },
                "variations": [
                  {
                    "plainTextMessage": {
                      "value": "string"
                    },
                    "customPayload": {
                      "value": "string"
                    },
                    "ssmlMessage": {
                      "value": "string"
                    },
                    "imageResponseCard": {
                      "title": "string",
                      "subtitle": "string",
                      "imageUrl": "string",
                      "buttons": [
                        {
                          "text": "string",
                          "value": "string"
                        }
                        ...
                      ]
                    }
                  }
                  ...
                ]
              }
              ...
            ],
            "allowInterrupt": true|false
          }
        }
      },
      "timeoutResponse": {
        "messageGroups": [
          {
            "message": {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            },
            "variations": [
              {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              }
              ...
            ]
          }
          ...
        ],
        "allowInterrupt": true|false
      },
      "timeoutNextStep": {
        "dialogAction": {
          "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
          "slotToElicit": "string",
          "suppressNextMessage": true|false
        },
        "intent": {
          "name": "string",
          "slots": {"string": {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      { ... recursive ... }
                      ...
                    ]
                  }
                  ...
                ]
              }
            ...}
        },
        "sessionAttributes": {"string": "string"
          ...}
      },
      "timeoutConditional": {
        "active": true|false,
        "conditionalBranches": [
          {
            "name": "string",
            "condition": {
              "expressionString": "string"
            },
            "nextStep": {
              "dialogAction": {
                "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
                "slotToElicit": "string",
                "suppressNextMessage": true|false
              },
              "intent": {
                "name": "string",
                "slots": {"string": {
                      "shape": "Scalar"|"List",
                      "value": {
                        "interpretedValue": "string"
                      },
                      "values": [
                        {
                          "shape": "Scalar"|"List",
                          "value": {
                            "interpretedValue": "string"
                          },
                          "values": [
                            { ... recursive ... }
                            ...
                          ]
                        }
                        ...
                      ]
                    }
                  ...}
              },
              "sessionAttributes": {"string": "string"
                ...}
            },
            "response": {
              "messageGroups": [
                {
                  "message": {
                    "plainTextMessage": {
                      "value": "string"
                    },
                    "customPayload": {
                      "value": "string"
                    },
                    "ssmlMessage": {
                      "value": "string"
                    },
                    "imageResponseCard": {
                      "title": "string",
                      "subtitle": "string",
                      "imageUrl": "string",
                      "buttons": [
                        {
                          "text": "string",
                          "value": "string"
                        }
                        ...
                      ]
                    }
                  },
                  "variations": [
                    {
                      "plainTextMessage": {
                        "value": "string"
                      },
                      "customPayload": {
                        "value": "string"
                      },
                      "ssmlMessage": {
                        "value": "string"
                      },
                      "imageResponseCard": {
                        "title": "string",
                        "subtitle": "string",
                        "imageUrl": "string",
                        "buttons": [
                          {
                            "text": "string",
                            "value": "string"
                          }
                          ...
                        ]
                      }
                    }
                    ...
                  ]
                }
                ...
              ],
              "allowInterrupt": true|false
            }
          }
          ...
        ],
        "defaultBranch": {
          "nextStep": {
            "dialogAction": {
              "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
              "slotToElicit": "string",
              "suppressNextMessage": true|false
            },
            "intent": {
              "name": "string",
              "slots": {"string": {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      {
                        "shape": "Scalar"|"List",
                        "value": {
                          "interpretedValue": "string"
                        },
                        "values": [
                          { ... recursive ... }
                          ...
                        ]
                      }
                      ...
                    ]
                  }
                ...}
            },
            "sessionAttributes": {"string": "string"
              ...}
          },
          "response": {
            "messageGroups": [
              {
                "message": {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                },
                "variations": [
                  {
                    "plainTextMessage": {
                      "value": "string"
                    },
                    "customPayload": {
                      "value": "string"
                    },
                    "ssmlMessage": {
                      "value": "string"
                    },
                    "imageResponseCard": {
                      "title": "string",
                      "subtitle": "string",
                      "imageUrl": "string",
                      "buttons": [
                        {
                          "text": "string",
                          "value": "string"
                        }
                        ...
                      ]
                    }
                  }
                  ...
                ]
              }
              ...
            ],
            "allowInterrupt": true|false
          }
        }
      }
    }
  },
  "elicitationCodeHook": {
    "enableCodeHookInvocation": true|false,
    "invocationLabel": "string"
  }
}
```

`--intent-closing-setting` (structure)

The new response that Amazon Lex sends the user when the intent is closed.

closingResponse -> (structure)

The response that Amazon Lex sends to the user when the intent is complete.

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

active -> (boolean)

Specifies whether an intentâs closing response is used. When this field is false, the closing response isnât sent to the user. If the `active` field isnât specified, the default is true.

nextStep -> (structure)

Specifies the next step that the bot executes after playing the intentâs closing response.

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

conditional -> (structure)

A list of conditional branches associated with the intentâs closing response. These branches are executed when the `nextStep` attribute is set to `EvalutateConditional` .

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

JSON Syntax:

```
{
  "closingResponse": {
    "messageGroups": [
      {
        "message": {
          "plainTextMessage": {
            "value": "string"
          },
          "customPayload": {
            "value": "string"
          },
          "ssmlMessage": {
            "value": "string"
          },
          "imageResponseCard": {
            "title": "string",
            "subtitle": "string",
            "imageUrl": "string",
            "buttons": [
              {
                "text": "string",
                "value": "string"
              }
              ...
            ]
          }
        },
        "variations": [
          {
            "plainTextMessage": {
              "value": "string"
            },
            "customPayload": {
              "value": "string"
            },
            "ssmlMessage": {
              "value": "string"
            },
            "imageResponseCard": {
              "title": "string",
              "subtitle": "string",
              "imageUrl": "string",
              "buttons": [
                {
                  "text": "string",
                  "value": "string"
                }
                ...
              ]
            }
          }
          ...
        ]
      }
      ...
    ],
    "allowInterrupt": true|false
  },
  "active": true|false,
  "nextStep": {
    "dialogAction": {
      "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
      "slotToElicit": "string",
      "suppressNextMessage": true|false
    },
    "intent": {
      "name": "string",
      "slots": {"string": {
            "shape": "Scalar"|"List",
            "value": {
              "interpretedValue": "string"
            },
            "values": [
              {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  { ... recursive ... }
                  ...
                ]
              }
              ...
            ]
          }
        ...}
    },
    "sessionAttributes": {"string": "string"
      ...}
  },
  "conditional": {
    "active": true|false,
    "conditionalBranches": [
      {
        "name": "string",
        "condition": {
          "expressionString": "string"
        },
        "nextStep": {
          "dialogAction": {
            "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
            "slotToElicit": "string",
            "suppressNextMessage": true|false
          },
          "intent": {
            "name": "string",
            "slots": {"string": {
                  "shape": "Scalar"|"List",
                  "value": {
                    "interpretedValue": "string"
                  },
                  "values": [
                    {
                      "shape": "Scalar"|"List",
                      "value": {
                        "interpretedValue": "string"
                      },
                      "values": [
                        { ... recursive ... }
                        ...
                      ]
                    }
                    ...
                  ]
                }
              ...}
          },
          "sessionAttributes": {"string": "string"
            ...}
        },
        "response": {
          "messageGroups": [
            {
              "message": {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              },
              "variations": [
                {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                }
                ...
              ]
            }
            ...
          ],
          "allowInterrupt": true|false
        }
      }
      ...
    ],
    "defaultBranch": {
      "nextStep": {
        "dialogAction": {
          "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
          "slotToElicit": "string",
          "suppressNextMessage": true|false
        },
        "intent": {
          "name": "string",
          "slots": {"string": {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      { ... recursive ... }
                      ...
                    ]
                  }
                  ...
                ]
              }
            ...}
        },
        "sessionAttributes": {"string": "string"
          ...}
      },
      "response": {
        "messageGroups": [
          {
            "message": {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            },
            "variations": [
              {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              }
              ...
            ]
          }
          ...
        ],
        "allowInterrupt": true|false
      }
    }
  }
}
```

`--input-contexts` (list)

A new list of contexts that must be active in order for Amazon Lex to consider the intent.

(structure)

A context that must be active for an intent to be selected by Amazon Lex.

name -> (string)

The name of the context.

Shorthand Syntax:

```
name=string ...
```

JSON Syntax:

```
[
  {
    "name": "string"
  }
  ...
]
```

`--output-contexts` (list)

A new list of contexts that Amazon Lex activates when the intent is fulfilled.

(structure)

Describes a session context that is activated when an intent is fulfilled.

name -> (string)

The name of the output context.

timeToLiveInSeconds -> (integer)

The amount of time, in seconds, that the output context should remain active. The time is figured from the first time the context is sent to the user.

turnsToLive -> (integer)

The number of conversation turns that the output context should remain active. The number of turns is counted from the first time that the context is sent to the user.

Shorthand Syntax:

```
name=string,timeToLiveInSeconds=integer,turnsToLive=integer ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "timeToLiveInSeconds": integer,
    "turnsToLive": integer
  }
  ...
]
```

`--kendra-configuration` (structure)

New configuration settings for connecting to an Amazon Kendra index.

kendraIndex -> (string)

The Amazon Resource Name (ARN) of the Amazon Kendra index that you want the `AMAZON.KendraSearchIntent` intent to search. The index must be in the same account and Region as the Amazon Lex bot.

queryFilterStringEnabled -> (boolean)

Determines whether the `AMAZON.KendraSearchIntent` intent uses a custom query string to query the Amazon Kendra index.

queryFilterString -> (string)

A query filter that Amazon Lex sends to Amazon Kendra to filter the response from a query. The filter is in the format defined by Amazon Kendra. For more information, see [Filtering queries](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html) .

Shorthand Syntax:

```
kendraIndex=string,queryFilterStringEnabled=boolean,queryFilterString=string
```

JSON Syntax:

```
{
  "kendraIndex": "string",
  "queryFilterStringEnabled": true|false,
  "queryFilterString": "string"
}
```

`--bot-id` (string)

The identifier of the bot that contains the intent.

`--bot-version` (string)

The version of the bot that contains the intent. Must be `DRAFT` .

`--locale-id` (string)

The identifier of the language and locale where this intent is used. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html) .

`--initial-response-setting` (structure)

Configuration settings for a response sent to the user before Amazon Lex starts eliciting slots.

initialResponse -> (structure)

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

conditional -> (structure)

Provides a list of conditional branches. Branches are evaluated in the order that they are entered in the list. The first branch with a condition that evaluates to true is executed. The last branch in the list is the default branch. The default branch should not have any condition expression. The default branch is executed if no other branch has a matching condition.

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

Settings that specify the dialog code hook that is called by Amazon Lex at a step of the conversation.

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

JSON Syntax:

```
{
  "initialResponse": {
    "messageGroups": [
      {
        "message": {
          "plainTextMessage": {
            "value": "string"
          },
          "customPayload": {
            "value": "string"
          },
          "ssmlMessage": {
            "value": "string"
          },
          "imageResponseCard": {
            "title": "string",
            "subtitle": "string",
            "imageUrl": "string",
            "buttons": [
              {
                "text": "string",
                "value": "string"
              }
              ...
            ]
          }
        },
        "variations": [
          {
            "plainTextMessage": {
              "value": "string"
            },
            "customPayload": {
              "value": "string"
            },
            "ssmlMessage": {
              "value": "string"
            },
            "imageResponseCard": {
              "title": "string",
              "subtitle": "string",
              "imageUrl": "string",
              "buttons": [
                {
                  "text": "string",
                  "value": "string"
                }
                ...
              ]
            }
          }
          ...
        ]
      }
      ...
    ],
    "allowInterrupt": true|false
  },
  "nextStep": {
    "dialogAction": {
      "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
      "slotToElicit": "string",
      "suppressNextMessage": true|false
    },
    "intent": {
      "name": "string",
      "slots": {"string": {
            "shape": "Scalar"|"List",
            "value": {
              "interpretedValue": "string"
            },
            "values": [
              {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  { ... recursive ... }
                  ...
                ]
              }
              ...
            ]
          }
        ...}
    },
    "sessionAttributes": {"string": "string"
      ...}
  },
  "conditional": {
    "active": true|false,
    "conditionalBranches": [
      {
        "name": "string",
        "condition": {
          "expressionString": "string"
        },
        "nextStep": {
          "dialogAction": {
            "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
            "slotToElicit": "string",
            "suppressNextMessage": true|false
          },
          "intent": {
            "name": "string",
            "slots": {"string": {
                  "shape": "Scalar"|"List",
                  "value": {
                    "interpretedValue": "string"
                  },
                  "values": [
                    {
                      "shape": "Scalar"|"List",
                      "value": {
                        "interpretedValue": "string"
                      },
                      "values": [
                        { ... recursive ... }
                        ...
                      ]
                    }
                    ...
                  ]
                }
              ...}
          },
          "sessionAttributes": {"string": "string"
            ...}
        },
        "response": {
          "messageGroups": [
            {
              "message": {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              },
              "variations": [
                {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                }
                ...
              ]
            }
            ...
          ],
          "allowInterrupt": true|false
        }
      }
      ...
    ],
    "defaultBranch": {
      "nextStep": {
        "dialogAction": {
          "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
          "slotToElicit": "string",
          "suppressNextMessage": true|false
        },
        "intent": {
          "name": "string",
          "slots": {"string": {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      { ... recursive ... }
                      ...
                    ]
                  }
                  ...
                ]
              }
            ...}
        },
        "sessionAttributes": {"string": "string"
          ...}
      },
      "response": {
        "messageGroups": [
          {
            "message": {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            },
            "variations": [
              {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              }
              ...
            ]
          }
          ...
        ],
        "allowInterrupt": true|false
      }
    }
  },
  "codeHook": {
    "enableCodeHookInvocation": true|false,
    "active": true|false,
    "invocationLabel": "string",
    "postCodeHookSpecification": {
      "successResponse": {
        "messageGroups": [
          {
            "message": {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            },
            "variations": [
              {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              }
              ...
            ]
          }
          ...
        ],
        "allowInterrupt": true|false
      },
      "successNextStep": {
        "dialogAction": {
          "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
          "slotToElicit": "string",
          "suppressNextMessage": true|false
        },
        "intent": {
          "name": "string",
          "slots": {"string": {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      { ... recursive ... }
                      ...
                    ]
                  }
                  ...
                ]
              }
            ...}
        },
        "sessionAttributes": {"string": "string"
          ...}
      },
      "successConditional": {
        "active": true|false,
        "conditionalBranches": [
          {
            "name": "string",
            "condition": {
              "expressionString": "string"
            },
            "nextStep": {
              "dialogAction": {
                "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
                "slotToElicit": "string",
                "suppressNextMessage": true|false
              },
              "intent": {
                "name": "string",
                "slots": {"string": {
                      "shape": "Scalar"|"List",
                      "value": {
                        "interpretedValue": "string"
                      },
                      "values": [
                        {
                          "shape": "Scalar"|"List",
                          "value": {
                            "interpretedValue": "string"
                          },
                          "values": [
                            { ... recursive ... }
                            ...
                          ]
                        }
                        ...
                      ]
                    }
                  ...}
              },
              "sessionAttributes": {"string": "string"
                ...}
            },
            "response": {
              "messageGroups": [
                {
                  "message": {
                    "plainTextMessage": {
                      "value": "string"
                    },
                    "customPayload": {
                      "value": "string"
                    },
                    "ssmlMessage": {
                      "value": "string"
                    },
                    "imageResponseCard": {
                      "title": "string",
                      "subtitle": "string",
                      "imageUrl": "string",
                      "buttons": [
                        {
                          "text": "string",
                          "value": "string"
                        }
                        ...
                      ]
                    }
                  },
                  "variations": [
                    {
                      "plainTextMessage": {
                        "value": "string"
                      },
                      "customPayload": {
                        "value": "string"
                      },
                      "ssmlMessage": {
                        "value": "string"
                      },
                      "imageResponseCard": {
                        "title": "string",
                        "subtitle": "string",
                        "imageUrl": "string",
                        "buttons": [
                          {
                            "text": "string",
                            "value": "string"
                          }
                          ...
                        ]
                      }
                    }
                    ...
                  ]
                }
                ...
              ],
              "allowInterrupt": true|false
            }
          }
          ...
        ],
        "defaultBranch": {
          "nextStep": {
            "dialogAction": {
              "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
              "slotToElicit": "string",
              "suppressNextMessage": true|false
            },
            "intent": {
              "name": "string",
              "slots": {"string": {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      {
                        "shape": "Scalar"|"List",
                        "value": {
                          "interpretedValue": "string"
                        },
                        "values": [
                          { ... recursive ... }
                          ...
                        ]
                      }
                      ...
                    ]
                  }
                ...}
            },
            "sessionAttributes": {"string": "string"
              ...}
          },
          "response": {
            "messageGroups": [
              {
                "message": {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                },
                "variations": [
                  {
                    "plainTextMessage": {
                      "value": "string"
                    },
                    "customPayload": {
                      "value": "string"
                    },
                    "ssmlMessage": {
                      "value": "string"
                    },
                    "imageResponseCard": {
                      "title": "string",
                      "subtitle": "string",
                      "imageUrl": "string",
                      "buttons": [
                        {
                          "text": "string",
                          "value": "string"
                        }
                        ...
                      ]
                    }
                  }
                  ...
                ]
              }
              ...
            ],
            "allowInterrupt": true|false
          }
        }
      },
      "failureResponse": {
        "messageGroups": [
          {
            "message": {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            },
            "variations": [
              {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              }
              ...
            ]
          }
          ...
        ],
        "allowInterrupt": true|false
      },
      "failureNextStep": {
        "dialogAction": {
          "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
          "slotToElicit": "string",
          "suppressNextMessage": true|false
        },
        "intent": {
          "name": "string",
          "slots": {"string": {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      { ... recursive ... }
                      ...
                    ]
                  }
                  ...
                ]
              }
            ...}
        },
        "sessionAttributes": {"string": "string"
          ...}
      },
      "failureConditional": {
        "active": true|false,
        "conditionalBranches": [
          {
            "name": "string",
            "condition": {
              "expressionString": "string"
            },
            "nextStep": {
              "dialogAction": {
                "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
                "slotToElicit": "string",
                "suppressNextMessage": true|false
              },
              "intent": {
                "name": "string",
                "slots": {"string": {
                      "shape": "Scalar"|"List",
                      "value": {
                        "interpretedValue": "string"
                      },
                      "values": [
                        {
                          "shape": "Scalar"|"List",
                          "value": {
                            "interpretedValue": "string"
                          },
                          "values": [
                            { ... recursive ... }
                            ...
                          ]
                        }
                        ...
                      ]
                    }
                  ...}
              },
              "sessionAttributes": {"string": "string"
                ...}
            },
            "response": {
              "messageGroups": [
                {
                  "message": {
                    "plainTextMessage": {
                      "value": "string"
                    },
                    "customPayload": {
                      "value": "string"
                    },
                    "ssmlMessage": {
                      "value": "string"
                    },
                    "imageResponseCard": {
                      "title": "string",
                      "subtitle": "string",
                      "imageUrl": "string",
                      "buttons": [
                        {
                          "text": "string",
                          "value": "string"
                        }
                        ...
                      ]
                    }
                  },
                  "variations": [
                    {
                      "plainTextMessage": {
                        "value": "string"
                      },
                      "customPayload": {
                        "value": "string"
                      },
                      "ssmlMessage": {
                        "value": "string"
                      },
                      "imageResponseCard": {
                        "title": "string",
                        "subtitle": "string",
                        "imageUrl": "string",
                        "buttons": [
                          {
                            "text": "string",
                            "value": "string"
                          }
                          ...
                        ]
                      }
                    }
                    ...
                  ]
                }
                ...
              ],
              "allowInterrupt": true|false
            }
          }
          ...
        ],
        "defaultBranch": {
          "nextStep": {
            "dialogAction": {
              "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
              "slotToElicit": "string",
              "suppressNextMessage": true|false
            },
            "intent": {
              "name": "string",
              "slots": {"string": {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      {
                        "shape": "Scalar"|"List",
                        "value": {
                          "interpretedValue": "string"
                        },
                        "values": [
                          { ... recursive ... }
                          ...
                        ]
                      }
                      ...
                    ]
                  }
                ...}
            },
            "sessionAttributes": {"string": "string"
              ...}
          },
          "response": {
            "messageGroups": [
              {
                "message": {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                },
                "variations": [
                  {
                    "plainTextMessage": {
                      "value": "string"
                    },
                    "customPayload": {
                      "value": "string"
                    },
                    "ssmlMessage": {
                      "value": "string"
                    },
                    "imageResponseCard": {
                      "title": "string",
                      "subtitle": "string",
                      "imageUrl": "string",
                      "buttons": [
                        {
                          "text": "string",
                          "value": "string"
                        }
                        ...
                      ]
                    }
                  }
                  ...
                ]
              }
              ...
            ],
            "allowInterrupt": true|false
          }
        }
      },
      "timeoutResponse": {
        "messageGroups": [
          {
            "message": {
              "plainTextMessage": {
                "value": "string"
              },
              "customPayload": {
                "value": "string"
              },
              "ssmlMessage": {
                "value": "string"
              },
              "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [
                  {
                    "text": "string",
                    "value": "string"
                  }
                  ...
                ]
              }
            },
            "variations": [
              {
                "plainTextMessage": {
                  "value": "string"
                },
                "customPayload": {
                  "value": "string"
                },
                "ssmlMessage": {
                  "value": "string"
                },
                "imageResponseCard": {
                  "title": "string",
                  "subtitle": "string",
                  "imageUrl": "string",
                  "buttons": [
                    {
                      "text": "string",
                      "value": "string"
                    }
                    ...
                  ]
                }
              }
              ...
            ]
          }
          ...
        ],
        "allowInterrupt": true|false
      },
      "timeoutNextStep": {
        "dialogAction": {
          "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
          "slotToElicit": "string",
          "suppressNextMessage": true|false
        },
        "intent": {
          "name": "string",
          "slots": {"string": {
                "shape": "Scalar"|"List",
                "value": {
                  "interpretedValue": "string"
                },
                "values": [
                  {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      { ... recursive ... }
                      ...
                    ]
                  }
                  ...
                ]
              }
            ...}
        },
        "sessionAttributes": {"string": "string"
          ...}
      },
      "timeoutConditional": {
        "active": true|false,
        "conditionalBranches": [
          {
            "name": "string",
            "condition": {
              "expressionString": "string"
            },
            "nextStep": {
              "dialogAction": {
                "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
                "slotToElicit": "string",
                "suppressNextMessage": true|false
              },
              "intent": {
                "name": "string",
                "slots": {"string": {
                      "shape": "Scalar"|"List",
                      "value": {
                        "interpretedValue": "string"
                      },
                      "values": [
                        {
                          "shape": "Scalar"|"List",
                          "value": {
                            "interpretedValue": "string"
                          },
                          "values": [
                            { ... recursive ... }
                            ...
                          ]
                        }
                        ...
                      ]
                    }
                  ...}
              },
              "sessionAttributes": {"string": "string"
                ...}
            },
            "response": {
              "messageGroups": [
                {
                  "message": {
                    "plainTextMessage": {
                      "value": "string"
                    },
                    "customPayload": {
                      "value": "string"
                    },
                    "ssmlMessage": {
                      "value": "string"
                    },
                    "imageResponseCard": {
                      "title": "string",
                      "subtitle": "string",
                      "imageUrl": "string",
                      "buttons": [
                        {
                          "text": "string",
                          "value": "string"
                        }
                        ...
                      ]
                    }
                  },
                  "variations": [
                    {
                      "plainTextMessage": {
                        "value": "string"
                      },
                      "customPayload": {
                        "value": "string"
                      },
                      "ssmlMessage": {
                        "value": "string"
                      },
                      "imageResponseCard": {
                        "title": "string",
                        "subtitle": "string",
                        "imageUrl": "string",
                        "buttons": [
                          {
                            "text": "string",
                            "value": "string"
                          }
                          ...
                        ]
                      }
                    }
                    ...
                  ]
                }
                ...
              ],
              "allowInterrupt": true|false
            }
          }
          ...
        ],
        "defaultBranch": {
          "nextStep": {
            "dialogAction": {
              "type": "ElicitIntent"|"StartIntent"|"ElicitSlot"|"EvaluateConditional"|"InvokeDialogCodeHook"|"ConfirmIntent"|"FulfillIntent"|"CloseIntent"|"EndConversation",
              "slotToElicit": "string",
              "suppressNextMessage": true|false
            },
            "intent": {
              "name": "string",
              "slots": {"string": {
                    "shape": "Scalar"|"List",
                    "value": {
                      "interpretedValue": "string"
                    },
                    "values": [
                      {
                        "shape": "Scalar"|"List",
                        "value": {
                          "interpretedValue": "string"
                        },
                        "values": [
                          { ... recursive ... }
                          ...
                        ]
                      }
                      ...
                    ]
                  }
                ...}
            },
            "sessionAttributes": {"string": "string"
              ...}
          },
          "response": {
            "messageGroups": [
              {
                "message": {
                  "plainTextMessage": {
                    "value": "string"
                  },
                  "customPayload": {
                    "value": "string"
                  },
                  "ssmlMessage": {
                    "value": "string"
                  },
                  "imageResponseCard": {
                    "title": "string",
                    "subtitle": "string",
                    "imageUrl": "string",
                    "buttons": [
                      {
                        "text": "string",
                        "value": "string"
                      }
                      ...
                    ]
                  }
                },
                "variations": [
                  {
                    "plainTextMessage": {
                      "value": "string"
                    },
                    "customPayload": {
                      "value": "string"
                    },
                    "ssmlMessage": {
                      "value": "string"
                    },
                    "imageResponseCard": {
                      "title": "string",
                      "subtitle": "string",
                      "imageUrl": "string",
                      "buttons": [
                        {
                          "text": "string",
                          "value": "string"
                        }
                        ...
                      ]
                    }
                  }
                  ...
                ]
              }
              ...
            ],
            "allowInterrupt": true|false
          }
        }
      }
    }
  }
}
```

`--qn-a-intent-configuration` (structure)

Specifies the configuration of the built-in `Amazon.QnAIntent` . The `AMAZON.QnAIntent` intent is called when Amazon Lex canât determine another intent to invoke. If you specify this field, you canât specify the `kendraConfiguration` field.

dataSourceConfiguration -> (structure)

Contains details about the configuration of the data source used for the `AMAZON.QnAIntent` .

opensearchConfiguration -> (structure)

Contains details about the configuration of the Amazon OpenSearch Service database used for the `AMAZON.QnAIntent` . To create a domain, follow the steps at [Creating and managing Amazon OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html) .

domainEndpoint -> (string)

The endpoint of the Amazon OpenSearch Service domain.

indexName -> (string)

The name of the Amazon OpenSearch Service index.

exactResponse -> (boolean)

Specifies whether to return an exact response or to return an answer generated by the model using the fields you specify from the database.

exactResponseFields -> (structure)

Contains the names of the fields used for an exact response to the user.

questionField -> (string)

The name of the field that contains the query made to the OpenSearch Service database.

answerField -> (string)

The name of the field that contains the answer to the query made to the OpenSearch Service database.

includeFields -> (list)

Contains a list of fields from the Amazon OpenSearch Service that the model can use to generate the answer to the query.

(string)

kendraConfiguration -> (structure)

Contains details about the configuration of the Amazon Kendra index used for the `AMAZON.QnAIntent` . To create a Amazon Kendra index, follow the steps at [Creating an index](https://docs.aws.amazon.com/kendra/latest/dg/create-index.html) .

kendraIndex -> (string)

The ARN of the Amazon Kendra index to use.

queryFilterStringEnabled -> (boolean)

Specifies whether to enable an Amazon Kendra filter string or not.

queryFilterString -> (string)

Contains the Amazon Kendra filter string to use if enabled. For more information on the Amazon Kendra search filter JSON format, see [Using document attributes to filter search results](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html#search-filtering) .

exactResponse -> (boolean)

Specifies whether to return an exact response from the Amazon Kendra index or to let the Amazon Bedrock model you select generate a response based on the results. To use this feature, you must first add FAQ questions to your index by following the steps at [Adding frequently asked questions (FAQs) to an index](https://docs.aws.amazon.com/kendra/latest/dg/in-creating-faq.html) .

bedrockKnowledgeStoreConfiguration -> (structure)

Contains details about the configuration of the Amazon Bedrock knowledge base used for the `AMAZON.QnAIntent` . To set up a knowledge base, follow the steps at [Building a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) .

bedrockKnowledgeBaseArn -> (string)

The base ARN of the knowledge base used.

exactResponse -> (boolean)

Specifies whether to return an exact response, or to return an answer generated by the model, using the fields you specify from the database.

exactResponseFields -> (structure)

Contains the names of the fields used for an exact response to the user.

answerField -> (string)

The answer field used for an exact response from Bedrock Knowledge Store.

bedrockModelConfiguration -> (structure)

Contains information about the Amazon Bedrock model used to interpret the prompt used in descriptive bot building.

modelArn -> (string)

The ARN of the foundation model used in descriptive bot building.

guardrail -> (structure)

The guardrail configuration in the Bedrock model specification details.

identifier -> (string)

The unique guardrail id for the Bedrock guardrail configuration.

version -> (string)

The guardrail version for the Bedrock guardrail configuration.

traceStatus -> (string)

The Bedrock trace status in the Bedrock model specification details.

customPrompt -> (string)

The custom prompt used in the Bedrock model specification details.

JSON Syntax:

```
{
  "dataSourceConfiguration": {
    "opensearchConfiguration": {
      "domainEndpoint": "string",
      "indexName": "string",
      "exactResponse": true|false,
      "exactResponseFields": {
        "questionField": "string",
        "answerField": "string"
      },
      "includeFields": ["string", ...]
    },
    "kendraConfiguration": {
      "kendraIndex": "string",
      "queryFilterStringEnabled": true|false,
      "queryFilterString": "string",
      "exactResponse": true|false
    },
    "bedrockKnowledgeStoreConfiguration": {
      "bedrockKnowledgeBaseArn": "string",
      "exactResponse": true|false,
      "exactResponseFields": {
        "answerField": "string"
      }
    }
  },
  "bedrockModelConfiguration": {
    "modelArn": "string",
    "guardrail": {
      "identifier": "string",
      "version": "string"
    },
    "traceStatus": "ENABLED"|"DISABLED",
    "customPrompt": "string"
  }
}
```

`--q-in-connect-intent-configuration` (structure)

Qinconnect intent configuration details for the update intent request.

qInConnectAssistantConfiguration -> (structure)

The Qinconnect assistant configuration details of the Qinconnect intent.

assistantArn -> (string)

The assistant Arn details of the Qinconnect assistant configuration.

Shorthand Syntax:

```
qInConnectAssistantConfiguration={assistantArn=string}
```

JSON Syntax:

```
{
  "qInConnectAssistantConfiguration": {
    "assistantArn": "string"
  }
}
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

intentId -> (string)

The identifier of the intent that was updated.

intentName -> (string)

The updated name of the intent.

description -> (string)

The updated description of the intent.

parentIntentSignature -> (string)

The updated built-in intent that is the parent of this intent.

sampleUtterances -> (list)

The updated list of sample utterances for the intent.

(structure)

A sample utterance that invokes an intent or respond to a slot elicitation prompt.

utterance -> (string)

The sample utterance that Amazon Lex uses to build its machine-learning model to recognize intents.

dialogCodeHook -> (structure)

The updated Lambda function called during each turn of the conversation with the user.

enabled -> (boolean)

Enables the dialog code hook so that it processes user requests.

fulfillmentCodeHook -> (structure)

The updated Lambda function called when the intent is ready for fulfillment.

enabled -> (boolean)

Indicates whether a Lambda function should be invoked to fulfill a specific intent.

postFulfillmentStatusSpecification -> (structure)

Provides settings for messages sent to the user for after the Lambda fulfillment function completes. Post-fulfillment messages can be sent for both streaming and non-streaming conversations.

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

successNextStep -> (structure)

Specifies the next step in the conversation that Amazon Lex invokes when the fulfillment code hook completes successfully.

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

A list of conditional branches to evaluate after the fulfillment code hook finishes successfully.

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

failureNextStep -> (structure)

Specifies the next step the bot runs after the fulfillment code hook throws an exception or returns with the `State` field of the `Intent` object set to `Failed` .

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

A list of conditional branches to evaluate after the fulfillment code hook throws an exception or returns with the `State` field of the `Intent` object set to `Failed` .

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

timeoutNextStep -> (structure)

Specifies the next step that the bot runs when the fulfillment code hook times out.

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

A list of conditional branches to evaluate if the fulfillment code hook times out.

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

fulfillmentUpdatesSpecification -> (structure)

Provides settings for update messages sent to the user for long-running Lambda fulfillment functions. Fulfillment updates can be used only with streaming conversations.

active -> (boolean)

Determines whether fulfillment updates are sent to the user. When this field is true, updates are sent.

If the `active` field is set to true, the `startResponse` , `updateResponse` , and `timeoutInSeconds` fields are required.

startResponse -> (structure)

Provides configuration information for the message sent to users when the fulfillment Lambda functions starts running.

delayInSeconds -> (integer)

The delay between when the Lambda fulfillment function starts running and the start message is played. If the Lambda function returns before the delay is over, the start message isnât played.

messageGroups -> (list)

1 - 5 message groups that contain start messages. Amazon Lex chooses one of the messages to play to the user.

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

Determines whether the user can interrupt the start message while it is playing.

updateResponse -> (structure)

Provides configuration information for messages sent periodically to the user while the fulfillment Lambda function is running.

frequencyInSeconds -> (integer)

The frequency that a message is sent to the user. When the period ends, Amazon Lex chooses a message from the message groups and plays it to the user. If the fulfillment Lambda returns before the first period ends, an update message is not played to the user.

messageGroups -> (list)

1 - 5 message groups that contain update messages. Amazon Lex chooses one of the messages to play to the user.

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

Determines whether the user can interrupt an update message while it is playing.

timeoutInSeconds -> (integer)

The length of time that the fulfillment Lambda function should run before it times out.

active -> (boolean)

Determines whether the fulfillment code hook is used. When `active` is false, the code hook doesnât run.

slotPriorities -> (list)

The updated list of slots and their priorities that are elicited from the user for the intent.

(structure)

Sets the priority that Amazon Lex should use when eliciting slot values from a user.

priority -> (integer)

The priority that Amazon Lex should apply to the slot.

slotId -> (string)

The unique identifier of the slot.

intentConfirmationSetting -> (structure)

The updated prompts that Amazon Lex sends to the user to confirm the completion of an intent.

promptSpecification -> (structure)

Prompts the user to confirm the intent. This question should have a yes or no answer.

Amazon Lex uses this prompt to ensure that the user acknowledges that the intent is ready for fulfillment. For example, with the `OrderPizza` intent, you might want to confirm that the order is correct before placing it. For other intents, such as intents that simply respond to user questions, you might not need to ask the user for confirmation before providing the information.

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

declinationResponse -> (structure)

When the user answers ânoâ to the question defined in `promptSpecification` , Amazon Lex responds with this response to acknowledge that the intent was canceled.

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

active -> (boolean)

Specifies whether the intentâs confirmation is sent to the user. When this field is false, confirmation and declination responses arenât sent. If the `active` field isnât specified, the default is true.

confirmationResponse -> (structure)

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

confirmationNextStep -> (structure)

Specifies the next step that the bot executes when the customer confirms the intent.

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

confirmationConditional -> (structure)

A list of conditional branches to evaluate after the intent is closed.

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

declinationNextStep -> (structure)

Specifies the next step that the bot executes when the customer declines the intent.

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

declinationConditional -> (structure)

A list of conditional branches to evaluate after the intent is declined.

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

The next step to take in the conversation if the confirmation step fails.

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

Provides a list of conditional branches. Branches are evaluated in the order that they are entered in the list. The first branch with a condition that evaluates to true is executed. The last branch in the list is the default branch. The default branch should not have any condition expression. The default branch is executed if no other branch has a matching condition.

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

The `DialogCodeHookInvocationSetting` object associated with intentâs confirmation step. The dialog code hook is triggered based on these invocation settings when the confirmation next step or declination next step or failure next step is `InvokeDialogCodeHook` .

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

The `DialogCodeHookInvocationSetting` used when the code hook is invoked during confirmation prompt retries.

enableCodeHookInvocation -> (boolean)

Indicates whether a Lambda function should be invoked for the dialog.

invocationLabel -> (string)

A label that indicates the dialog step from which the dialog code hook is happening.

intentClosingSetting -> (structure)

The updated response that Amazon Lex sends the user when the intent is closed.

closingResponse -> (structure)

The response that Amazon Lex sends to the user when the intent is complete.

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

active -> (boolean)

Specifies whether an intentâs closing response is used. When this field is false, the closing response isnât sent to the user. If the `active` field isnât specified, the default is true.

nextStep -> (structure)

Specifies the next step that the bot executes after playing the intentâs closing response.

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

conditional -> (structure)

A list of conditional branches associated with the intentâs closing response. These branches are executed when the `nextStep` attribute is set to `EvalutateConditional` .

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

inputContexts -> (list)

The updated list of contexts that must be active for the intent to be considered by Amazon Lex.

(structure)

A context that must be active for an intent to be selected by Amazon Lex.

name -> (string)

The name of the context.

outputContexts -> (list)

The updated list of contexts that Amazon Lex activates when the intent is fulfilled.

(structure)

Describes a session context that is activated when an intent is fulfilled.

name -> (string)

The name of the output context.

timeToLiveInSeconds -> (integer)

The amount of time, in seconds, that the output context should remain active. The time is figured from the first time the context is sent to the user.

turnsToLive -> (integer)

The number of conversation turns that the output context should remain active. The number of turns is counted from the first time that the context is sent to the user.

kendraConfiguration -> (structure)

The updated configuration for connecting to an Amazon Kendra index with the `AMAZON.KendraSearchIntent` intent.

kendraIndex -> (string)

The Amazon Resource Name (ARN) of the Amazon Kendra index that you want the `AMAZON.KendraSearchIntent` intent to search. The index must be in the same account and Region as the Amazon Lex bot.

queryFilterStringEnabled -> (boolean)

Determines whether the `AMAZON.KendraSearchIntent` intent uses a custom query string to query the Amazon Kendra index.

queryFilterString -> (string)

A query filter that Amazon Lex sends to Amazon Kendra to filter the response from a query. The filter is in the format defined by Amazon Kendra. For more information, see [Filtering queries](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html) .

botId -> (string)

The identifier of the bot that contains the intent.

botVersion -> (string)

The version of the bot that contains the intent. Will always be `DRAFT` .

localeId -> (string)

The updated language and locale of the intent.

creationDateTime -> (timestamp)

A timestamp of when the intent was created.

lastUpdatedDateTime -> (timestamp)

A timestamp of the last time that the intent was modified.

initialResponseSetting -> (structure)

Configuration settings for a response sent to the user before Amazon Lex starts eliciting slots.

initialResponse -> (structure)

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

conditional -> (structure)

Provides a list of conditional branches. Branches are evaluated in the order that they are entered in the list. The first branch with a condition that evaluates to true is executed. The last branch in the list is the default branch. The default branch should not have any condition expression. The default branch is executed if no other branch has a matching condition.

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

Settings that specify the dialog code hook that is called by Amazon Lex at a step of the conversation.

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

qnAIntentConfiguration -> (structure)

Details about the configuration of the built-in `Amazon.QnAIntent` .

dataSourceConfiguration -> (structure)

Contains details about the configuration of the data source used for the `AMAZON.QnAIntent` .

opensearchConfiguration -> (structure)

Contains details about the configuration of the Amazon OpenSearch Service database used for the `AMAZON.QnAIntent` . To create a domain, follow the steps at [Creating and managing Amazon OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html) .

domainEndpoint -> (string)

The endpoint of the Amazon OpenSearch Service domain.

indexName -> (string)

The name of the Amazon OpenSearch Service index.

exactResponse -> (boolean)

Specifies whether to return an exact response or to return an answer generated by the model using the fields you specify from the database.

exactResponseFields -> (structure)

Contains the names of the fields used for an exact response to the user.

questionField -> (string)

The name of the field that contains the query made to the OpenSearch Service database.

answerField -> (string)

The name of the field that contains the answer to the query made to the OpenSearch Service database.

includeFields -> (list)

Contains a list of fields from the Amazon OpenSearch Service that the model can use to generate the answer to the query.

(string)

kendraConfiguration -> (structure)

Contains details about the configuration of the Amazon Kendra index used for the `AMAZON.QnAIntent` . To create a Amazon Kendra index, follow the steps at [Creating an index](https://docs.aws.amazon.com/kendra/latest/dg/create-index.html) .

kendraIndex -> (string)

The ARN of the Amazon Kendra index to use.

queryFilterStringEnabled -> (boolean)

Specifies whether to enable an Amazon Kendra filter string or not.

queryFilterString -> (string)

Contains the Amazon Kendra filter string to use if enabled. For more information on the Amazon Kendra search filter JSON format, see [Using document attributes to filter search results](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html#search-filtering) .

exactResponse -> (boolean)

Specifies whether to return an exact response from the Amazon Kendra index or to let the Amazon Bedrock model you select generate a response based on the results. To use this feature, you must first add FAQ questions to your index by following the steps at [Adding frequently asked questions (FAQs) to an index](https://docs.aws.amazon.com/kendra/latest/dg/in-creating-faq.html) .

bedrockKnowledgeStoreConfiguration -> (structure)

Contains details about the configuration of the Amazon Bedrock knowledge base used for the `AMAZON.QnAIntent` . To set up a knowledge base, follow the steps at [Building a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) .

bedrockKnowledgeBaseArn -> (string)

The base ARN of the knowledge base used.

exactResponse -> (boolean)

Specifies whether to return an exact response, or to return an answer generated by the model, using the fields you specify from the database.

exactResponseFields -> (structure)

Contains the names of the fields used for an exact response to the user.

answerField -> (string)

The answer field used for an exact response from Bedrock Knowledge Store.

bedrockModelConfiguration -> (structure)

Contains information about the Amazon Bedrock model used to interpret the prompt used in descriptive bot building.

modelArn -> (string)

The ARN of the foundation model used in descriptive bot building.

guardrail -> (structure)

The guardrail configuration in the Bedrock model specification details.

identifier -> (string)

The unique guardrail id for the Bedrock guardrail configuration.

version -> (string)

The guardrail version for the Bedrock guardrail configuration.

traceStatus -> (string)

The Bedrock trace status in the Bedrock model specification details.

customPrompt -> (string)

The custom prompt used in the Bedrock model specification details.

qInConnectIntentConfiguration -> (structure)

Qinconnect intent configuration details for the update intent response.

qInConnectAssistantConfiguration -> (structure)

The Qinconnect assistant configuration details of the Qinconnect intent.

assistantArn -> (string)

The assistant Arn details of the Qinconnect assistant configuration.