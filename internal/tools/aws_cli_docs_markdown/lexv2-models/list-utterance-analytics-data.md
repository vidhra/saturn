# list-utterance-analytics-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-utterance-analytics-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-utterance-analytics-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# list-utterance-analytics-data

## Description

### Note

To use this API operation, your IAM role must have permissions to perform the [ListAggregatedUtterances](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html) operation, which provides access to utterance-related analytics. See [Viewing utterance statistics](https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-utterances.html) for the IAM policy to apply to the IAM role.

Retrieves a list of metadata for individual user utterances to your bot. The following fields are required:

- `startDateTime` and `endDateTime` â Define a time range for which you want to retrieve results.

Of the optional fields, you can organize the results in the following ways:

- Use the `filters` field to filter the results and the `sortBy` field to specify the values by which to sort the results.
- Use the `maxResults` field to limit the number of results to return in a single response and the `nextToken` field to return the next batch of results if the response does not return the full set of results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/ListUtteranceAnalyticsData)

## Synopsis

```
list-utterance-analytics-data
--bot-id <value>
--start-date-time <value>
--end-date-time <value>
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

The identifier for the bot for which you want to retrieve utterance analytics.

`--start-date-time` (timestamp)

The date and time that marks the beginning of the range of time for which you want to see utterance analytics.

`--end-date-time` (timestamp)

The date and time that marks the end of the range of time for which you want to see utterance analytics.

`--sort-by` (structure)

An object specifying the measure and method by which to sort the utterance analytics data.

name -> (string)

The measure by which to sort the utterance analytics data.

- `Count` â The number of utterances.
- `UtteranceTimestamp` â The date and time of the utterance.

order -> (string)

Specifies whether to sort the results in ascending or descending order.

Shorthand Syntax:

```
name=string,order=string
```

JSON Syntax:

```
{
  "name": "UtteranceTimestamp",
  "order": "Ascending"|"Descending"
}
```

`--filters` (list)

A list of objects, each of which describes a condition by which you want to filter the results.

(structure)

Contains fields describing a condition by which to filter the utterances. The expression may be understood as `name` `operator` `values` . For example:

- `LocaleId EQ Book` â The locale is the string âenâ.
- `UtteranceText CO help` â The text of the utterance contains the string âhelpâ.

The operators that each filter supports are listed below:

- `BotAlias` â `EQ` .
- `BotVersion` â `EQ` .
- `LocaleId` â `EQ` .
- `Modality` â `EQ` .
- `Channel` â `EQ` .
- `SessionId` â `EQ` .
- `OriginatingRequestId` â `EQ` .
- `UtteranceState` â `EQ` .
- `UtteranceText` â `EQ` , `CO` .

name -> (string)

The category by which to filter the utterances. The descriptions for each option are as follows:

- `BotAlias` â The name of the bot alias.
- `BotVersion` â The version of the bot.
- `LocaleId` â The locale of the bot.
- `Modality` â The modality of the session with the bot (audio, DTMF, or text).
- `Channel` â The channel that the bot is integrated with.
- `SessionId` â The identifier of the session with the bot.
- `OriginatingRequestId` â The identifier of the first request in a session.
- `UtteranceState` â The state of the utterance.
- `UtteranceText` â The text in the utterance.

operator -> (string)

The operation by which to filter the category. The following operations are possible:

- `CO` â Contains
- `EQ` â Equals
- `GT` â Greater than
- `LT` â Less than

The operators that each filter supports are listed below:

- `BotAlias` â `EQ` .
- `BotVersion` â `EQ` .
- `LocaleId` â `EQ` .
- `Modality` â `EQ` .
- `Channel` â `EQ` .
- `SessionId` â `EQ` .
- `OriginatingRequestId` â `EQ` .
- `UtteranceState` â `EQ` .
- `UtteranceText` â `EQ` , `CO` .

values -> (list)

An array containing the values of the category by which to apply the operator to filter the results. You can provide multiple values if the operator is `EQ` or `CO` . If you provide multiple values, you filter for results that equal/contain any of the values. For example, if the `name` , `operator` , and `values` fields are `Modality` , `EQ` , and `[Speech, Text]` , the operation filters for results where the modality was either `Speech` or `Text` .

(string)

Shorthand Syntax:

```
name=string,operator=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "BotAliasId"|"BotVersion"|"LocaleId"|"Modality"|"Channel"|"SessionId"|"OriginatingRequestId"|"UtteranceState"|"UtteranceText",
    "operator": "EQ"|"GT"|"LT",
    "values": ["string", ...]
  }
  ...
]
```

`--max-results` (integer)

The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.

`--next-token` (string)

If the response from the ListUtteranceAnalyticsData operation contains more results than specified in the maxResults parameter, a token is returned in the response.

Use the returned token in the nextToken parameter of a ListUtteranceAnalyticsData request to return the next page of results. For a complete set of results, call the ListUtteranceAnalyticsData operation until the nextToken returned in the response is null.

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

The unique identifier of the bot that the utterances belong to.

nextToken -> (string)

If the response from the ListUtteranceAnalyticsData operation contains more results than specified in the maxResults parameter, a token is returned in the response.

Use the returned token in the nextToken parameter of a ListUtteranceAnalyticsData request to return the next page of results. For a complete set of results, call the ListUtteranceAnalyticsData operation until the nextToken returned in the response is null.

utterances -> (list)

A list of objects, each of which contains information about an utterance in a user session with your bot.

(structure)

An object containing information about a specific utterance.

botAliasId -> (string)

The identifier of the alias of the bot that the utterance was made to.

botVersion -> (string)

The version of the bot that the utterance was made to.

localeId -> (string)

The locale of the bot that the utterance was made to.

sessionId -> (string)

The identifier of the session that the utterance was made in.

channel -> (string)

The channel that is integrated with the bot that the utterance was made to.

mode -> (string)

The mode of the session. The possible values are as follows:

- `Speech` â The session consisted of spoken dialogue.
- `Text` â The session consisted of written dialogue.
- `DTMF` â The session consisted of touch-tone keypad (Dual Tone Multi-Frequency) key presses.
- `MultiMode` â The session consisted of multiple modes.

conversationStartTime -> (timestamp)

The date and time when the conversation in which the utterance took place began. A conversation is defined as a unique combination of a `sessionId` and an `originatingRequestId` .

conversationEndTime -> (timestamp)

The date and time when the conversation in which the utterance took place ended. A conversation is defined as a unique combination of a `sessionId` and an `originatingRequestId` .

utterance -> (string)

The text of the utterance.

utteranceTimestamp -> (timestamp)

The date and time when the utterance took place.

audioVoiceDurationMillis -> (long)

The duration in milliseconds of the audio associated with the utterance.

utteranceUnderstood -> (boolean)

Specifies whether the bot understood the utterance or not.

inputType -> (string)

The input type of the utterance. The possible values are as follows:

- PCM format: audio data must be in little-endian byte order.
- `audio/l16; rate=16000; channels=1`
- `audio/x-l16; sample-rate=16000; channel-count=1`
- `audio/lpcm; sample-rate=8000; sample-size-bits=16; channel-count=1; is-big-endian=false`
- Opus format
- `audio/x-cbr-opus-with-preamble;preamble-size=0;bit-rate=256000;frame-size-milliseconds=4`
- Text format
- `text/plain; charset=utf-8`

outputType -> (string)

The output type of the utterance. The possible values are as follows:

- `audio/mpeg`
- `audio/ogg`
- `audio/pcm (16 KHz)`
- `audio/` (defaults to `mpeg` )
- `text/plain; charset=utf-8`

associatedIntentName -> (string)

The name of the intent that the utterance is associated to.

associatedSlotName -> (string)

The name of the slot that the utterance is associated to.

intentState -> (string)

The state of the intent that the utterance is associated to.

dialogActionType -> (string)

The type of dialog action that the utterance is associated to. See the `type` field in [DialogAction](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_DialogAction.html) for more information.

botResponseAudioVoiceId -> (string)

The identifier for the audio of the bot response.

slotsFilledInSession -> (string)

The slots that have been filled in the session by the time of the utterance.

utteranceRequestId -> (string)

The identifier of the request associated with the utterance.

botResponses -> (list)

A list of objects containing information about the bot response to the utterance.

(structure)

An object that contains a response to the utterance from the bot.

content -> (string)

The text of the response to the utterance from the bot.

contentType -> (string)

The type of the response. The following values are possible:

- `PlainText` â A plain text string.
- `CustomPayload` â A response string that you can customize to include data or metadata for your application.
- `SSML` â A string that includes Speech Synthesis Markup Language to customize the audio response.
- `ImageResponseCard` â An image with buttons that the customer can select. See [ImageResponseCard](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_ImageResponseCard.html) for more information.

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

Describes a button to use on a response card used to gather slot values from a user.

text -> (string)

The text that appears on the button. Use this to tell the user what value is returned when they choose this button.

value -> (string)

The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.