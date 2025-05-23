# list-slotsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-slots.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-slots.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# list-slots

## Description

Gets a list of slots that match the specified criteria.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/ListSlots)

## Synopsis

```
list-slots
--bot-id <value>
--bot-version <value>
--locale-id <value>
--intent-id <value>
[--sort-by <value>]
[--filters <value>]
[--max-results <value>]
[--next-token <value>]
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

`--bot-id` (string)

The identifier of the bot that contains the slot.

`--bot-version` (string)

The version of the bot that contains the slot.

`--locale-id` (string)

The identifier of the language and locale of the slots to list. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html) .

`--intent-id` (string)

The unique identifier of the intent that contains the slot.

`--sort-by` (structure)

Determines the sort order for the response from the `ListSlots` operation. You can choose to sort by the slot name or last updated date in either ascending or descending order.

attribute -> (string)

The attribute to use to sort the list.

order -> (string)

The order to sort the list. You can choose ascending or descending.

Shorthand Syntax:

```
attribute=string,order=string
```

JSON Syntax:

```
{
  "attribute": "SlotName"|"LastUpdatedDateTime",
  "order": "Ascending"|"Descending"
}
```

`--filters` (list)

Provides the specification of a filter used to limit the slots in the response to only those that match the filter specification. You can only specify one filter and only one string to filter on.

(structure)

Filters the response from the `ListSlots` operation.

name -> (string)

The name of the field to use for filtering.

values -> (list)

The value to use to filter the response.

(string)

operator -> (string)

The operator to use for the filter. Specify `EQ` when the `ListSlots` operation should return only aliases that equal the specified value. Specify `CO` when the `ListSlots` operation should return aliases that contain the specified value.

Shorthand Syntax:

```
name=string,values=string,string,operator=string ...
```

JSON Syntax:

```
[
  {
    "name": "SlotName",
    "values": ["string", ...],
    "operator": "CO"|"EQ"
  }
  ...
]
```

`--max-results` (integer)

The maximum number of slots to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.

`--next-token` (string)

If the response from the `ListSlots` operation contains more results than specified in the `maxResults` parameter, a token is returned in the response. Use that token in the `nextToken` parameter to return the next page of results.

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

botId -> (string)

The identifier of the bot that contains the slots.

botVersion -> (string)

The version of the bot that contains the slots.

localeId -> (string)

The language and locale of the slots in the list.

intentId -> (string)

The identifier of the intent that contains the slots.

slotSummaries -> (list)

Summary information for the slots that meet the filter criteria specified in the request. The length of the list is specified in the `maxResults` parameter of the request. If there are more slots available, the `nextToken` field contains a token to get the next page of results.

(structure)

Summary information about a slot, a value that the bot elicits from the user.

slotId -> (string)

The unique identifier of the slot.

slotName -> (string)

The name given to the slot.

description -> (string)

The description of the slot.

slotConstraint -> (string)

Whether the slot is required or optional. An intent is complete when all required slots are filled.

slotTypeId -> (string)

The unique identifier for the slot type that defines the values for the slot.

valueElicitationPromptSpecification -> (structure)

Prompts that are sent to the user to elicit a value for the slot.

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

lastUpdatedDateTime -> (timestamp)

The timestamp of the last date and time that the slot was updated.

nextToken -> (string)

A token that indicates whether there are more results to return in a response to the `ListSlots` operation. If the `nextToken` field is present, you send the contents as the `nextToken` parameter of a `ListSlots` operation request to get the next page of results.