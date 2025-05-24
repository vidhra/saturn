# put-sessionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-runtime/put-session.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-runtime/put-session.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-runtime/index.html#cli-aws-lexv2-runtime) ]

# put-session

## Description

Creates a new session or modifies an existing session with an Amazon Lex V2 bot. Use this operation to enable your application to set the state of the bot.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/runtime.lex.v2-2020-08-07/PutSession)

## Synopsis

```
put-session
--bot-id <value>
--bot-alias-id <value>
--locale-id <value>
--session-id <value>
[--messages <value>]
--session-state <value>
[--request-attributes <value>]
[--response-content-type <value>]
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

The identifier of the bot that receives the session data.

`--bot-alias-id` (string)

The alias identifier of the bot that receives the session data.

`--locale-id` (string)

The locale where the session is in use.

`--session-id` (string)

The identifier of the session that receives the session data.

`--messages` (list)

A list of messages to send to the user. Messages are sent in the order that they are defined in the list.

(structure)

Container for text that is returned to the customer..

content -> (string)

The text of the message.

contentType -> (string)

Indicates the type of response.

imageResponseCard -> (structure)

A card that is shown to the user by a messaging platform. You define the contents of the card, the card is displayed by the platform.

When you use a response card, the response from the user is constrained to the text associated with a button on the card.

title -> (string)

The title to display on the response card. The format of the title is determined by the platform displaying the response card.

subtitle -> (string)

The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

imageUrl -> (string)

The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.

buttons -> (list)

A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.

(structure)

A button that appears on a response card show to the user.

text -> (string)

The text that is displayed on the button.

value -> (string)

The value returned to Amazon Lex V2 when a user chooses the button.

JSON Syntax:

```
[
  {
    "content": "string",
    "contentType": "CustomPayload"|"ImageResponseCard"|"PlainText"|"SSML",
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
```

`--session-state` (structure)

Sets the state of the session with the user. You can use this to set the current intent, attributes, context, and dialog action. Use the dialog action to determine the next step that Amazon Lex V2 should use in the conversation with the user.

dialogAction -> (structure)

The next step that Amazon Lex V2 should take in the conversation with a user.

type -> (string)

The next action that the bot should take in its interaction with the user. The following values are possible:

- `Close` â Indicates that there will not be a response from the user. For example, the statement âYour order has been placedâ does not require a response.
- `ConfirmIntent` â The next action is asking the user if the intent is complete and ready to be fulfilled. This is a yes/no question such as âPlace the order?â
- `Delegate` â The next action is determined by Amazon Lex V2.
- `ElicitIntent` â The next action is to elicit an intent from the user.
- `ElicitSlot` â The next action is to elicit a slot value from the user.

slotToElicit -> (string)

The name of the slot that should be elicited from the user.

slotElicitationStyle -> (string)

Configures the slot to use spell-by-letter or spell-by-word style. When you use a style on a slot, users can spell out their input to make it clear to your bot.

- Spell by letter - âbâ âoâ âbâ
- Spell by word - âb as in boyâ âo as in oscarâ âb as in boyâ

For more information, see [Using spelling to enter slot values](https://docs.aws.amazon.com/lexv2/latest/dg/spelling-styles.html) .

subSlotToElicit -> (structure)

The name of the constituent sub slot of the composite slot specified in slotToElicit that should be elicited from the user.

name -> (string)

The name of the slot that should be elicited from the user.

subSlotToElicit -> (structure)

The field is not supported.

name -> (string)

The name of the slot that should be elicited from the user.

( â¦ recursive â¦ )

intent -> (structure)

The active intent that Amazon Lex V2 is processing.

name -> (string)

The name of the intent.

slots -> (map)

A map of all of the slots for the intent. The name of the slot maps to the value of the slot. If a slot has not been filled, the value is null.

key -> (string)

value -> (structure)

A value that Amazon Lex V2 uses to fulfill an intent.

value -> (structure)

The current value of the slot.

originalValue -> (string)

The part of the userâs response to the slot elicitation that Amazon Lex V2 determines is relevant to the slot value.

interpretedValue -> (string)

The value that Amazon Lex V2 determines for the slot, given the user input. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex V2 choose the first value in the `resolvedValues` list.

resolvedValues -> (list)

A list of values that Amazon Lex V2 determines are possible resolutions for the user input. The first value matches the `interpretedValue` .

(string)

shape -> (string)

When the `shape` value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

values -> (list)

A list of one or more values that the user provided for the slot. For example, if a for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

(structure)

A value that Amazon Lex V2 uses to fulfill an intent.

value -> (structure)

The current value of the slot.

originalValue -> (string)

The part of the userâs response to the slot elicitation that Amazon Lex V2 determines is relevant to the slot value.

interpretedValue -> (string)

The value that Amazon Lex V2 determines for the slot, given the user input. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex V2 choose the first value in the `resolvedValues` list.

resolvedValues -> (list)

A list of values that Amazon Lex V2 determines are possible resolutions for the user input. The first value matches the `interpretedValue` .

(string)

shape -> (string)

When the `shape` value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

values -> (list)

A list of one or more values that the user provided for the slot. For example, if a for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

subSlots -> (map)

The constituent sub slots of a composite slot.

key -> (string)

( â¦ recursive â¦ )

subSlots -> (map)

The constituent sub slots of a composite slot.

key -> (string)

value -> (structure)

A value that Amazon Lex V2 uses to fulfill an intent.

value -> (structure)

The current value of the slot.

originalValue -> (string)

The part of the userâs response to the slot elicitation that Amazon Lex V2 determines is relevant to the slot value.

interpretedValue -> (string)

The value that Amazon Lex V2 determines for the slot, given the user input. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex V2 choose the first value in the `resolvedValues` list.

resolvedValues -> (list)

A list of values that Amazon Lex V2 determines are possible resolutions for the user input. The first value matches the `interpretedValue` .

(string)

shape -> (string)

When the `shape` value is `List` , it indicates that the `values` field contains a list of slot values. When the value is `Scalar` , it indicates that the `value` field contains a single value.

values -> (list)

A list of one or more values that the user provided for the slot. For example, if a for a slot that elicits pizza toppings, the values might be âpepperoniâ and âpineapple.â

( â¦ recursive â¦ )

state -> (string)

Indicates the fulfillment state for the intent. The meanings of each value are as follows:

- `Failed` â The bot failed to fulfill the intent.
- `Fulfilled` â The bot has completed fulfillment of the intent.
- `FulfillmentInProgress` â The bot is in the middle of fulfilling the intent.
- `InProgress` â The bot is in the middle of eliciting the slot values that are necessary to fulfill the intent.
- `ReadyForFulfillment` â The bot has elicited all the slot values for the intent and is ready to fulfill the intent.
- `Waiting` â The bot is waiting for a response from the user (limited to streaming conversations).

confirmationState -> (string)

Indicates whether the intent has been `Confirmed` , `Denied` , or `None` if the confirmation stage has not yet been reached.

activeContexts -> (list)

One or more contexts that indicate to Amazon Lex V2 the context of a request. When a context is active, Amazon Lex V2 considers intents with the matching context as a trigger as the next intent in a session.

(structure)

Contains information about the contexts that a user is using in a session. You can configure Amazon Lex V2 to set a context when an intent is fulfilled, or you can set a context using the , , or operations.

Use a context to indicate to Amazon Lex V2 intents that should be used as follow-up intents. For example, if the active context is `order-fulfilled` , only intents that have `order-fulfilled` configured as a trigger are considered for follow up.

name -> (string)

The name of the context.

timeToLive -> (structure)

Indicates the number of turns or seconds that the context is active. Once the time to live expires, the context is no longer returned in a response.

timeToLiveInSeconds -> (integer)

The number of seconds that the context is active. You can specify between 5 and 86400 seconds (24 hours).

turnsToLive -> (integer)

The number of turns that the context is active. You can specify up to 20 turns. Each request and response from the bot is a turn.

contextAttributes -> (map)

A list of contexts active for the request. A context can be activated when a previous intent is fulfilled, or by including the context in the request.

If you donât specify a list of contexts, Amazon Lex V2 will use the current list of contexts for the session. If you specify an empty list, all contexts for the session are cleared.

key -> (string)

value -> (string)

sessionAttributes -> (map)

Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex V2 and a client application.

key -> (string)

value -> (string)

originatingRequestId -> (string)

A unique identifier for a specific request.

runtimeHints -> (structure)

Hints for phrases that a customer is likely to use for a slot. Amazon Lex V2 uses the hints to help determine the correct value of a slot.

slotHints -> (map)

A list of the slots in the intent that should have runtime hints added, and the phrases that should be added for each slot.

The first level of the `slotHints` map is the name of the intent. The second level is the name of the slot within the intent. For more information, see [Using hints to improve accuracy](https://docs.aws.amazon.com/lexv2/latest/dg/using-hints.html) .

The intent name and slot name must exist.

key -> (string)

value -> (map)

key -> (string)

value -> (structure)

Provides an array of phrases that should be given preference when resolving values for a slot.

runtimeHintValues -> (list)

One or more strings that Amazon Lex V2 should look for in the input to the bot. Each phrase is given preference when deciding on slot values.

(structure)

Provides the phrase that Amazon Lex V2 should look for in the userâs input to the bot.

phrase -> (string)

The phrase that Amazon Lex V2 should look for in the userâs input to the bot.

subSlotHints -> (map)

A map of constituent sub slot names inside a composite slot in the intent and the phrases that should be added for each sub slot. Inside each composite slot hints, this structure provides a mechanism to add granular sub slot phrases. Only sub slot hints are supported for composite slots. The intent name, composite slot name and the constituent sub slot names must exist.

key -> (string)

value -> (structure)

Provides an array of phrases that should be given preference when resolving values for a slot.

runtimeHintValues -> (list)

One or more strings that Amazon Lex V2 should look for in the input to the bot. Each phrase is given preference when deciding on slot values.

(structure)

Provides the phrase that Amazon Lex V2 should look for in the userâs input to the bot.

phrase -> (string)

The phrase that Amazon Lex V2 should look for in the userâs input to the bot.

JSON Syntax:

```
{
  "dialogAction": {
    "type": "Close"|"ConfirmIntent"|"Delegate"|"ElicitIntent"|"ElicitSlot"|"None",
    "slotToElicit": "string",
    "slotElicitationStyle": "Default"|"SpellByLetter"|"SpellByWord",
    "subSlotToElicit": {
      "name": "string",
      "subSlotToElicit": {
        "name": "string",
        "subSlotToElicit": { ... recursive ... }
      }
    }
  },
  "intent": {
    "name": "string",
    "slots": {"string": {
          "value": {
            "originalValue": "string",
            "interpretedValue": "string",
            "resolvedValues": ["string", ...]
          },
          "shape": "Scalar"|"List"|"Composite",
          "values": [
            {
              "value": {
                "originalValue": "string",
                "interpretedValue": "string",
                "resolvedValues": ["string", ...]
              },
              "shape": "Scalar"|"List"|"Composite",
              "values": [
                { ... recursive ... }
                ...
              ],
              "subSlots": {"string": { ... recursive ... }
                ...}
            }
            ...
          ],
          "subSlots": {"string": {
                "value": {
                  "originalValue": "string",
                  "interpretedValue": "string",
                  "resolvedValues": ["string", ...]
                },
                "shape": "Scalar"|"List"|"Composite",
                "values": [
                  { ... recursive ... }
                  ...
                ],
                "subSlots":
              }
            ...}
        }
      ...},
    "state": "Failed"|"Fulfilled"|"InProgress"|"ReadyForFulfillment"|"Waiting"|"FulfillmentInProgress",
    "confirmationState": "Confirmed"|"Denied"|"None"
  },
  "activeContexts": [
    {
      "name": "string",
      "timeToLive": {
        "timeToLiveInSeconds": integer,
        "turnsToLive": integer
      },
      "contextAttributes": {"string": "string"
        ...}
    }
    ...
  ],
  "sessionAttributes": {"string": "string"
    ...},
  "originatingRequestId": "string",
  "runtimeHints": {
    "slotHints": {"string": {"string": {
              "runtimeHintValues": [
                {
                  "phrase": "string"
                }
                ...
              ],
              "subSlotHints": {"string": {
                    "runtimeHintValues": [
                      {
                        "phrase": "string"
                      }
                      ...
                    ],
                    "subSlotHints":
                  }
                ...}
            }
          ...}
      ...}
  }
}
```

`--request-attributes` (map)

Request-specific information passed between Amazon Lex V2 and the client application.

The namespace `x-amz-lex:` is reserved for special attributes. Donât create any request attributes with the prefix `x-amz-lex:` .

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

`--response-content-type` (string)

The message that Amazon Lex V2 returns in the response can be either text or speech depending on the value of this parameter.

- If the value is `text/plain; charset=utf-8` , Amazon Lex V2 returns text in the response.

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

The type of response. Same as the type specified in the `responseContentType` field in the request.

messages -> (string)

A list of messages that were last sent to the user. The messages are ordered based on how you return the messages from you Lambda function or the order that the messages are defined in the bot.

sessionState -> (string)

A base-64-encoded gzipped field that represents the current state of the dialog between the user and the bot. Use this to determine the progress of the conversation and what the next action may be.

requestAttributes -> (string)

A base-64-encoded gzipped field that provides request-specific information passed between the client application and Amazon Lex V2. These are the same as the `requestAttribute` parameter in the call to the `PutSession` operation.

sessionId -> (string)

The identifier of the session that received the data.

audioStream -> (streaming blob)

If the requested content type was audio, the audio version of the message to convey to the user.