# list-session-analytics-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-session-analytics-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-session-analytics-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# list-session-analytics-data

## Description

Retrieves a list of metadata for individual user sessions with your bot. The `startDateTime` and `endDateTime` fields are required. These fields define a time range for which you want to retrieve results. Of the optional fields, you can organize the results in the following ways:

- Use the `filters` field to filter the results and the `sortBy` field to specify the values by which to sort the results.
- Use the `maxResults` field to limit the number of results to return in a single response and the `nextToken` field to return the next batch of results if the response does not return the full set of results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/ListSessionAnalyticsData)

## Synopsis

```
list-session-analytics-data
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

The identifier for the bot for which you want to retrieve session analytics.

`--start-date-time` (timestamp)

The date and time that marks the beginning of the range of time for which you want to see session analytics.

`--end-date-time` (timestamp)

The date and time that marks the end of the range of time for which you want to see session analytics.

`--sort-by` (structure)

An object specifying the measure and method by which to sort the session analytics data.

name -> (string)

The measure by which to sort the session analytics data.

- `conversationStartTime` â The date and time when the conversation began. A conversation is defined as a unique combination of a `sessionId` and an `originatingRequestId` .
- `numberOfTurns` â The number of turns that the session took.
- `conversationDurationSeconds` â The duration of the conversation in seconds.

order -> (string)

Specifies whether to sort the results in ascending or descending order.

Shorthand Syntax:

```
name=string,order=string
```

JSON Syntax:

```
{
  "name": "ConversationStartTime"|"NumberOfTurns"|"Duration",
  "order": "Ascending"|"Descending"
}
```

`--filters` (list)

A list of objects, each of which describes a condition by which you want to filter the results.

(structure)

Contains fields describing a condition by which to filter the sessions. The expression may be understood as `name` `operator` `values` . For example:

- `LocaleId EQ en` â The locale is âenâ.
- `Duration GT 200` â The duration is greater than 200 seconds.

The operators that each filter supports are listed below:

- `BotAlias` â `EQ` .
- `BotVersion` â `EQ` .
- `LocaleId` â `EQ` .
- `Modality` â `EQ` .
- `Channel` â `EQ` .
- `Duration` â `EQ` , `GT` , `LT` .
- `conversationEndState` â `EQ` , `CO` .
- `SessionId` â `EQ` .
- `OriginatingRequestId` â `EQ` .
- `IntentPath` â `EQ` .

name -> (string)

The category by which to filter the sessions. The descriptions for each option are as follows:

- `BotAlias` â The name of the bot alias.
- `BotVersion` â The version of the bot.
- `LocaleId` â The locale of the bot.
- `Modality` â The modality of the session with the bot (audio, DTMF, or text).
- `Channel` â The channel that the bot is integrated with.
- `Duration` â The duration of the session.
- `conversationEndState` â The final state of the session.
- `SessionId` â The identifier of the session with the bot.
- `OriginatingRequestId` â The identifier of the first request in a session.
- `IntentPath` â The order of intents taken in a session.

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
- `Duration` â `EQ` , `GT` , `LT` .
- `conversationEndState` â `EQ` , `CO` .
- `SessionId` â `EQ` .
- `OriginatingRequestId` â `EQ` .
- `IntentPath` â `EQ` .

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
    "name": "BotAliasId"|"BotVersion"|"LocaleId"|"Modality"|"Channel"|"Duration"|"ConversationEndState"|"SessionId"|"OriginatingRequestId"|"IntentPath",
    "operator": "EQ"|"GT"|"LT",
    "values": ["string", ...]
  }
  ...
]
```

`--max-results` (integer)

The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.

`--next-token` (string)

If the response from the ListSessionAnalyticsData operation contains more results than specified in the maxResults parameter, a token is returned in the response.

Use the returned token in the nextToken parameter of a ListSessionAnalyticsData request to return the next page of results. For a complete set of results, call the ListSessionAnalyticsData operation until the nextToken returned in the response is null.

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

The unique identifier of the bot that the sessions belong to.

nextToken -> (string)

If the response from the ListSessionAnalyticsData operation contains more results than specified in the maxResults parameter, a token is returned in the response.

Use the returned token in the nextToken parameter of a ListSessionAnalyticsData request to return the next page of results. For a complete set of results, call the ListSessionAnalyticsData operation until the nextToken returned in the response is null.

sessions -> (list)

A list of objects, each of which contains information about a session with the bot.

(structure)

An object containing information about a specific session.

botAliasId -> (string)

The identifier of the alias of the bot that the session was held with.

botVersion -> (string)

The version of the bot that the session was held with.

localeId -> (string)

The locale of the bot that the session was held with.

channel -> (string)

The channel that is integrated with the bot that the session was held with.

sessionId -> (string)

The identifier of the session.

conversationStartTime -> (timestamp)

The date and time when the conversation began. A conversation is defined as a unique combination of a `sessionId` and an `originatingRequestId` .

conversationEndTime -> (timestamp)

The date and time when the conversation ended. A conversation is defined as a unique combination of a `sessionId` and an `originatingRequestId` .

conversationDurationSeconds -> (long)

The duration of the conversation in seconds. A conversation is defined as a unique combination of a `sessionId` and an `originatingRequestId` .

conversationEndState -> (string)

The final state of the conversation. A conversation is defined as a unique combination of a `sessionId` and an `originatingRequestId` .

mode -> (string)

The mode of the session. The possible values are as follows:

- `Speech` â The session was spoken.
- `Text` â The session was written.
- `DTMF` â The session used a touch-tone keypad (Dual Tone Multi-Frequency).
- `MultiMode` â The session used multiple modes.

numberOfTurns -> (long)

The number of turns that the session took.

invokedIntentSamples -> (list)

A list of objects containing the name of an intent that was invoked.

(structure)

An object containing the name of an intent that was invoked.

intentName -> (string)

The name of an intent that was invoked.

originatingRequestId -> (string)

The identifier of the first request in a session.