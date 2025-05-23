# put-intentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-intent.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-intent.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lex-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/index.html#cli-aws-lex-models) ]

# put-intent

## Description

Creates an intent or replaces an existing intent.

To define the interaction between the user and your bot, you use one or more intents. For a pizza ordering bot, for example, you would create an `OrderPizza` intent.

To create an intent or replace an existing intent, you must provide the following:

- Intent name. For example, `OrderPizza` .
- Sample utterances. For example, âCan I order a pizza, please.â and âI want to order a pizza.â
- Information to be gathered. You specify slot types for the information that your bot will request from the user. You can specify standard slot types, such as a date or a time, or custom slot types such as the size and crust of a pizza.
- How the intent will be fulfilled. You can provide a Lambda function or configure the intent to return the intent information to the client application. If you use a Lambda function, when all of the intent information is available, Amazon Lex invokes your Lambda function. If you configure your intent to return the intent information to the client application.

You can specify other optional information in the request, such as:

- A confirmation prompt to ask the user to confirm an intent. For example, âShall I order your pizza?â
- A conclusion statement to send to the user after the intent has been fulfilled. For example, âI placed your pizza order.â
- A follow-up prompt that asks the user for additional activity. For example, asking âDo you want to order a drink with your pizza?â

If you specify an existing intent name to update the intent, Amazon Lex replaces the values in the `$LATEST` version of the intent with the values in the request. Amazon Lex removes fields that you donât provide in the request. If you donât specify the required fields, Amazon Lex throws an exception. When you update the `$LATEST` version of an intent, the `status` field of any bot that uses the `$LATEST` version of the intent is set to `NOT_BUILT` .

For more information, see  how-it-works .

This operation requires permissions for the `lex:PutIntent` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/PutIntent)

## Synopsis

```
put-intent
--name <value>
[--description <value>]
[--slots <value>]
[--sample-utterances <value>]
[--confirmation-prompt <value>]
[--rejection-statement <value>]
[--follow-up-prompt <value>]
[--conclusion-statement <value>]
[--dialog-code-hook <value>]
[--fulfillment-activity <value>]
[--parent-intent-signature <value>]
[--checksum <value>]
[--create-version | --no-create-version]
[--kendra-configuration <value>]
[--input-contexts <value>]
[--output-contexts <value>]
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

The name of the intent. The name is *not* case sensitive.

The name canât match a built-in intent name, or a built-in intent name with âAMAZON.â removed. For example, because there is a built-in intent called `AMAZON.HelpIntent` , you canât create a custom intent called `HelpIntent` .

For a list of built-in intents, see [Standard Built-in Intents](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents) in the *Alexa Skills Kit* .

`--description` (string)

A description of the intent.

`--slots` (list)

An array of intent slots. At runtime, Amazon Lex elicits required slot values from the user using prompts defined in the slots. For more information, see  how-it-works .

(structure)

Identifies the version of a specific slot.

name -> (string)

The name of the slot.

description -> (string)

A description of the slot.

slotConstraint -> (string)

Specifies whether the slot is required or optional.

slotType -> (string)

The type of the slot, either a custom slot type that you defined or one of the built-in slot types.

slotTypeVersion -> (string)

The version of the slot type.

valueElicitationPrompt -> (structure)

The prompt that Amazon Lex uses to elicit the slot value from the user.

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

priority -> (integer)

Directs Amazon Lex the order in which to elicit this slot value from the user. For example, if the intent has two slots with priorities 1 and 2, AWS Amazon Lex first elicits a value for the slot with priority 1.

If multiple slots share the same priority, the order in which Amazon Lex elicits values is arbitrary.

sampleUtterances -> (list)

If you know a specific pattern with which users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances.

(string)

responseCard -> (string)

A set of possible responses for the slot type used by text-based clients. A user chooses an option from the response card, instead of using text to reply.

obfuscationSetting -> (string)

Determines whether a slot is obfuscated in conversation logs and stored utterances. When you obfuscate a slot, the value is replaced by the slot name in curly braces ({}). For example, if the slot name is âfull_nameâ, obfuscated values are replaced with â{full_name}â. For more information, see [Slot Obfuscation](https://docs.aws.amazon.com/lex/latest/dg/how-obfuscate.html) .

defaultValueSpec -> (structure)

A list of default values for the slot. Default values are used when Amazon Lex hasnât determined a value for a slot. You can specify default values from context variables, session attributes, and defined values.

defaultValueList -> (list)

The default values for a slot. You can specify more than one default. For example, you can specify a default value to use from a matching context variable, a session attribute, or a fixed value.

The default value chosen is selected based on the order that you specify them in the list. For example, if you specify a context variable and a fixed value in that order, Amazon Lex uses the context variable if it is available, else it uses the fixed value.

(structure)

A default value for a slot.

defaultValue -> (string)

The default value for the slot. You can specify one of the following:

- `#context-name.slot-name` - The slot value âslot-nameâ in the context âcontext-name.â
- `{attribute}` - The slot value of the session attribute âattribute.â
- `'value'` - The discrete value âvalue.â

JSON Syntax:

```
[
  {
    "name": "string",
    "description": "string",
    "slotConstraint": "Required"|"Optional",
    "slotType": "string",
    "slotTypeVersion": "string",
    "valueElicitationPrompt": {
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
    },
    "priority": integer,
    "sampleUtterances": ["string", ...],
    "responseCard": "string",
    "obfuscationSetting": "NONE"|"DEFAULT_OBFUSCATION",
    "defaultValueSpec": {
      "defaultValueList": [
        {
          "defaultValue": "string"
        }
        ...
      ]
    }
  }
  ...
]
```

`--sample-utterances` (list)

An array of utterances (strings) that a user might say to signal the intent. For example, âI want {PizzaSize} pizzaâ, âOrder {Quantity} {PizzaSize} pizzasâ.

In each utterance, a slot name is enclosed in curly braces.

(string)

Syntax:

```
"string" "string" ...
```

`--confirmation-prompt` (structure)

Prompts the user to confirm the intent. This question should have a yes or no answer.

Amazon Lex uses this prompt to ensure that the user acknowledges that the intent is ready for fulfillment. For example, with the `OrderPizza` intent, you might want to confirm that the order is correct before placing it. For other intents, such as intents that simply respond to user questions, you might not need to ask the user for confirmation before providing the information.

### Note

You you must provide both the `rejectionStatement` and the `confirmationPrompt` , or neither.

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

`--rejection-statement` (structure)

When the user answers ânoâ to the question defined in `confirmationPrompt` , Amazon Lex responds with this statement to acknowledge that the intent was canceled.

### Note

You must provide both the `rejectionStatement` and the `confirmationPrompt` , or neither.

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

`--follow-up-prompt` (structure)

Amazon Lex uses this prompt to solicit additional activity after fulfilling an intent. For example, after the `OrderPizza` intent is fulfilled, you might prompt the user to order a drink.

The action that Amazon Lex takes depends on the userâs response, as follows:

- If the user says âYesâ it responds with the clarification prompt that is configured for the bot.
- if the user says âYesâ and continues with an utterance that triggers an intent it starts a conversation for the intent.
- If the user says âNoâ it responds with the rejection statement configured for the the follow-up prompt.
- If it doesnât recognize the utterance it repeats the follow-up prompt again.

The `followUpPrompt` field and the `conclusionStatement` field are mutually exclusive. You can specify only one.

prompt -> (structure)

Prompts for information from the user.

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

rejectionStatement -> (structure)

If the user answers ânoâ to the question defined in the `prompt` field, Amazon Lex responds with this statement to acknowledge that the intent was canceled.

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

JSON Syntax:

```
{
  "prompt": {
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
  },
  "rejectionStatement": {
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
}
```

`--conclusion-statement` (structure)

The statement that you want Amazon Lex to convey to the user after the intent is successfully fulfilled by the Lambda function.

This element is relevant only if you provide a Lambda function in the `fulfillmentActivity` . If you return the intent to the client application, you canât specify this element.

### Note

The `followUpPrompt` and `conclusionStatement` are mutually exclusive. You can specify only one.

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

`--dialog-code-hook` (structure)

Specifies a Lambda function to invoke for each user input. You can invoke this Lambda function to personalize user interaction.

For example, suppose your bot determines that the user is John. Your Lambda function might retrieve Johnâs information from a backend database and prepopulate some of the values. For example, if you find that John is gluten intolerant, you might set the corresponding intent slot, `GlutenIntolerant` , to true. You might find Johnâs phone number and set the corresponding session attribute.

uri -> (string)

The Amazon Resource Name (ARN) of the Lambda function.

messageVersion -> (string)

The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .

Shorthand Syntax:

```
uri=string,messageVersion=string
```

JSON Syntax:

```
{
  "uri": "string",
  "messageVersion": "string"
}
```

`--fulfillment-activity` (structure)

Required. Describes how the intent is fulfilled. For example, after a user provides all of the information for a pizza order, `fulfillmentActivity` defines how the bot places an order with a local pizza store.

You might configure Amazon Lex to return all of the intent information to the client application, or direct it to invoke a Lambda function that can process the intent (for example, place an order with a pizzeria).

type -> (string)

How the intent should be fulfilled, either by running a Lambda function or by returning the slot data to the client application.

codeHook -> (structure)

A description of the Lambda function that is run to fulfill the intent.

uri -> (string)

The Amazon Resource Name (ARN) of the Lambda function.

messageVersion -> (string)

The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .

Shorthand Syntax:

```
type=string,codeHook={uri=string,messageVersion=string}
```

JSON Syntax:

```
{
  "type": "ReturnIntent"|"CodeHook",
  "codeHook": {
    "uri": "string",
    "messageVersion": "string"
  }
}
```

`--parent-intent-signature` (string)

A unique identifier for the built-in intent to base this intent on. To find the signature for an intent, see [Standard Built-in Intents](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents) in the *Alexa Skills Kit* .

`--checksum` (string)

Identifies a specific revision of the `$LATEST` version.

When you create a new intent, leave the `checksum` field blank. If you specify a checksum you get a `BadRequestException` exception.

When you want to update a intent, set the `checksum` field to the checksum of the most recent revision of the `$LATEST` version. If you donât specify the `checksum` field, or if the checksum does not match the `$LATEST` version, you get a `PreconditionFailedException` exception.

`--create-version` | `--no-create-version` (boolean)

When set to `true` a new numbered version of the intent is created. This is the same as calling the `CreateIntentVersion` operation. If you do not specify `createVersion` , the default is `false` .

`--kendra-configuration` (structure)

Configuration information required to use the `AMAZON.KendraSearchIntent` intent to connect to an Amazon Kendra index. For more information, see [AMAZON.KendraSearchIntent](http://docs.aws.amazon.com/lex/latest/dg/built-in-intent-kendra-search.html) .

kendraIndex -> (string)

The Amazon Resource Name (ARN) of the Amazon Kendra index that you want the AMAZON.KendraSearchIntent intent to search. The index must be in the same account and Region as the Amazon Lex bot. If the Amazon Kendra index does not exist, you get an exception when you call the `PutIntent` operation.

queryFilterString -> (string)

A query filter that Amazon Lex sends to Amazon Kendra to filter the response from the query. The filter is in the format defined by Amazon Kendra. For more information, see [Filtering queries](http://docs.aws.amazon.com/kendra/latest/dg/filtering.html) .

You can override this filter string with a new filter string at runtime.

role -> (string)

The Amazon Resource Name (ARN) of an IAM role that has permission to search the Amazon Kendra index. The role must be in the same account and Region as the Amazon Lex bot. If the role does not exist, you get an exception when you call the `PutIntent` operation.

Shorthand Syntax:

```
kendraIndex=string,queryFilterString=string,role=string
```

JSON Syntax:

```
{
  "kendraIndex": "string",
  "queryFilterString": "string",
  "role": "string"
}
```

`--input-contexts` (list)

An array of `InputContext` objects that lists the contexts that must be active for Amazon Lex to choose the intent in a conversation with the user.

(structure)

The name of a context that must be active for an intent to be selected by Amazon Lex.

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

An array of `OutputContext` objects that lists the contexts that the intent activates when the intent is fulfilled.

(structure)

The specification of an output context that is set when an intent is fulfilled.

name -> (string)

The name of the context.

timeToLiveInSeconds -> (integer)

The number of seconds that the context should be active after it is first sent in a `PostContent` or `PostText` response. You can set the value between 5 and 86,400 seconds (24 hours).

turnsToLive -> (integer)

The number of conversation turns that the context should be active. A conversation turn is one `PostContent` or `PostText` request and the corresponding response from Amazon Lex.

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

The name of the intent.

description -> (string)

A description of the intent.

slots -> (list)

An array of intent slots that are configured for the intent.

(structure)

Identifies the version of a specific slot.

name -> (string)

The name of the slot.

description -> (string)

A description of the slot.

slotConstraint -> (string)

Specifies whether the slot is required or optional.

slotType -> (string)

The type of the slot, either a custom slot type that you defined or one of the built-in slot types.

slotTypeVersion -> (string)

The version of the slot type.

valueElicitationPrompt -> (structure)

The prompt that Amazon Lex uses to elicit the slot value from the user.

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

priority -> (integer)

Directs Amazon Lex the order in which to elicit this slot value from the user. For example, if the intent has two slots with priorities 1 and 2, AWS Amazon Lex first elicits a value for the slot with priority 1.

If multiple slots share the same priority, the order in which Amazon Lex elicits values is arbitrary.

sampleUtterances -> (list)

If you know a specific pattern with which users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances.

(string)

responseCard -> (string)

A set of possible responses for the slot type used by text-based clients. A user chooses an option from the response card, instead of using text to reply.

obfuscationSetting -> (string)

Determines whether a slot is obfuscated in conversation logs and stored utterances. When you obfuscate a slot, the value is replaced by the slot name in curly braces ({}). For example, if the slot name is âfull_nameâ, obfuscated values are replaced with â{full_name}â. For more information, see [Slot Obfuscation](https://docs.aws.amazon.com/lex/latest/dg/how-obfuscate.html) .

defaultValueSpec -> (structure)

A list of default values for the slot. Default values are used when Amazon Lex hasnât determined a value for a slot. You can specify default values from context variables, session attributes, and defined values.

defaultValueList -> (list)

The default values for a slot. You can specify more than one default. For example, you can specify a default value to use from a matching context variable, a session attribute, or a fixed value.

The default value chosen is selected based on the order that you specify them in the list. For example, if you specify a context variable and a fixed value in that order, Amazon Lex uses the context variable if it is available, else it uses the fixed value.

(structure)

A default value for a slot.

defaultValue -> (string)

The default value for the slot. You can specify one of the following:

- `#context-name.slot-name` - The slot value âslot-nameâ in the context âcontext-name.â
- `{attribute}` - The slot value of the session attribute âattribute.â
- `'value'` - The discrete value âvalue.â

sampleUtterances -> (list)

An array of sample utterances that are configured for the intent.

(string)

confirmationPrompt -> (structure)

If defined in the intent, Amazon Lex prompts the user to confirm the intent before fulfilling it.

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

rejectionStatement -> (structure)

If the user answers ânoâ to the question defined in `confirmationPrompt` Amazon Lex responds with this statement to acknowledge that the intent was canceled.

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

followUpPrompt -> (structure)

If defined in the intent, Amazon Lex uses this prompt to solicit additional user activity after the intent is fulfilled.

prompt -> (structure)

Prompts for information from the user.

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

rejectionStatement -> (structure)

If the user answers ânoâ to the question defined in the `prompt` field, Amazon Lex responds with this statement to acknowledge that the intent was canceled.

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

conclusionStatement -> (structure)

After the Lambda function specified in the``fulfillmentActivity`` intent fulfills the intent, Amazon Lex conveys this statement to the user.

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

dialogCodeHook -> (structure)

If defined in the intent, Amazon Lex invokes this Lambda function for each user input.

uri -> (string)

The Amazon Resource Name (ARN) of the Lambda function.

messageVersion -> (string)

The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .

fulfillmentActivity -> (structure)

If defined in the intent, Amazon Lex invokes this Lambda function to fulfill the intent after the user provides all of the information required by the intent.

type -> (string)

How the intent should be fulfilled, either by running a Lambda function or by returning the slot data to the client application.

codeHook -> (structure)

A description of the Lambda function that is run to fulfill the intent.

uri -> (string)

The Amazon Resource Name (ARN) of the Lambda function.

messageVersion -> (string)

The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .

parentIntentSignature -> (string)

A unique identifier for the built-in intent that this intent is based on.

lastUpdatedDate -> (timestamp)

The date that the intent was updated. When you create a resource, the creation date and last update dates are the same.

createdDate -> (timestamp)

The date that the intent was created.

version -> (string)

The version of the intent. For a new intent, the version is always `$LATEST` .

checksum -> (string)

Checksum of the `$LATEST` version of the intent created or updated.

createVersion -> (boolean)

`True` if a new version of the intent was created. If the `createVersion` field was not specified in the request, the `createVersion` field is set to false in the response.

kendraConfiguration -> (structure)

Configuration information, if any, required to connect to an Amazon Kendra index and use the `AMAZON.KendraSearchIntent` intent.

kendraIndex -> (string)

The Amazon Resource Name (ARN) of the Amazon Kendra index that you want the AMAZON.KendraSearchIntent intent to search. The index must be in the same account and Region as the Amazon Lex bot. If the Amazon Kendra index does not exist, you get an exception when you call the `PutIntent` operation.

queryFilterString -> (string)

A query filter that Amazon Lex sends to Amazon Kendra to filter the response from the query. The filter is in the format defined by Amazon Kendra. For more information, see [Filtering queries](http://docs.aws.amazon.com/kendra/latest/dg/filtering.html) .

You can override this filter string with a new filter string at runtime.

role -> (string)

The Amazon Resource Name (ARN) of an IAM role that has permission to search the Amazon Kendra index. The role must be in the same account and Region as the Amazon Lex bot. If the role does not exist, you get an exception when you call the `PutIntent` operation.

inputContexts -> (list)

An array of `InputContext` objects that lists the contexts that must be active for Amazon Lex to choose the intent in a conversation with the user.

(structure)

The name of a context that must be active for an intent to be selected by Amazon Lex.

name -> (string)

The name of the context.

outputContexts -> (list)

An array of `OutputContext` objects that lists the contexts that the intent activates when the intent is fulfilled.

(structure)

The specification of an output context that is set when an intent is fulfilled.

name -> (string)

The name of the context.

timeToLiveInSeconds -> (integer)

The number of seconds that the context should be active after it is first sent in a `PostContent` or `PostText` response. You can set the value between 5 and 86,400 seconds (24 hours).

turnsToLive -> (integer)

The number of conversation turns that the context should be active. A conversation turn is one `PostContent` or `PostText` request and the corresponding response from Amazon Lex.