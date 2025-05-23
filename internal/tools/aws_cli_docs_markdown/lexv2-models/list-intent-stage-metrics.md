# list-intent-stage-metricsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-intent-stage-metrics.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-intent-stage-metrics.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# list-intent-stage-metrics

## Description

Retrieves summary metrics for the stages within intents in your bot. The following fields are required:

- `metrics` â A list of [AnalyticsIntentStageMetric](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsIntentStageMetric.html) objects. In each object, use the `name` field to specify the metric to calculate, the `statistic` field to specify whether to calculate the `Sum` , `Average` , or `Max` number, and the `order` field to specify whether to sort the results in `Ascending` or `Descending` order.
- `startDateTime` and `endDateTime` â Define a time range for which you want to retrieve results.

Of the optional fields, you can organize the results in the following ways:

- Use the `filters` field to filter the results, the `groupBy` field to specify categories by which to group the results, and the `binBy` field to specify time intervals by which to group the results.
- Use the `maxResults` field to limit the number of results to return in a single response and the `nextToken` field to return the next batch of results if the response does not return the full set of results.

Note that an `order` field exists in both `binBy` and `metrics` . You can only specify one `order` in a given request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/ListIntentStageMetrics)

## Synopsis

```
list-intent-stage-metrics
--bot-id <value>
--start-date-time <value>
--end-date-time <value>
--metrics <value>
[--bin-by <value>]
[--group-by <value>]
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

The identifier for the bot for which you want to retrieve intent stage metrics.

`--start-date-time` (timestamp)

The date and time that marks the beginning of the range of time for which you want to see intent stage metrics.

`--end-date-time` (timestamp)

The date and time that marks the end of the range of time for which you want to see intent stage metrics.

`--metrics` (list)

A list of objects, each of which contains a metric you want to list, the statistic for the metric you want to return, and the method by which to organize the results.

(structure)

Contains the metric and the summary statistic you want to calculate, and the order in which to sort the results, for the intent stages across the user sessions with the bot.

name -> (string)

The metric for which you want to get intent stage summary statistics. See [Key definitions](https://docs.aws.amazon.com/lexv2/latest/dg/analytics-key-definitions.html) for more details about these metrics.

- `Count` â The number of times the intent stage occurred.
- `Success` â The number of times the intent stage succeeded.
- `Failure` â The number of times the intent stage failed.
- `Dropped` â The number of times the user dropped the intent stage.
- `Retry` â The number of times the bot tried to elicit a response from the user at this stage.

statistic -> (string)

The summary statistic to calculate.

- `Sum` â The total count for the category you provide in `name` .
- `Average` â The total count divided by the number of intent stages in the category you provide in `name` .
- `Max` â The highest count in the category you provide in `name` .

order -> (string)

Specifies whether to sort the results in ascending or descending order of the summary statistic (`value` in the response).

Shorthand Syntax:

```
name=string,statistic=string,order=string ...
```

JSON Syntax:

```
[
  {
    "name": "Count"|"Success"|"Failed"|"Dropped"|"Retry",
    "statistic": "Sum"|"Avg"|"Max",
    "order": "Ascending"|"Descending"
  }
  ...
]
```

`--bin-by` (list)

A list of objects, each of which contains specifications for organizing the results by time.

(structure)

Contains the time metric, interval, and method by which to bin the analytics data.

name -> (string)

Specifies the time metric by which to bin the analytics data.

interval -> (string)

Specifies the interval of time by which to bin the analytics data.

order -> (string)

Specifies whether to bin the analytics data in ascending or descending order. If this field is left blank, the default order is by the key of the bin in descending order.

Shorthand Syntax:

```
name=string,interval=string,order=string ...
```

JSON Syntax:

```
[
  {
    "name": "ConversationStartTime"|"UtteranceTimestamp",
    "interval": "OneHour"|"OneDay",
    "order": "Ascending"|"Descending"
  }
  ...
]
```

`--group-by` (list)

A list of objects, each of which specifies how to group the results. You can group by the following criteria:

- `IntentStageName` â The name of the intent stage.
- `SwitchedToIntent` â The intent to which the conversation was switched (if any).

(structure)

Contains the category by which to group the intent stages.

name -> (string)

Specifies whether to group the intent stages by their name or the intent to which the session was switched.

Shorthand Syntax:

```
name=string ...
```

JSON Syntax:

```
[
  {
    "name": "IntentStageName"|"SwitchedToIntent"
  }
  ...
]
```

`--filters` (list)

A list of objects, each of which describes a condition by which you want to filter the results.

(structure)

Contains fields describing a condition by which to filter the intent stages. The expression may be understood as `name` `operator` `values` . For example:

- `IntentName CO Book` â The intent name contains the string âBook.â
- `BotVersion EQ 2` â The bot version is equal to two.

The operators that each filter supports are listed below:

- `BotAlias` â `EQ` .
- `BotVersion` â `EQ` .
- `LocaleId` â `EQ` .
- `Modality` â `EQ` .
- `Channel` â `EQ` .
- `SessionId` â `EQ` .
- `OriginatingRequestId` â `EQ` .
- `IntentName` â `EQ` , `CO` .
- `IntentStageName` â `EQ` , `CO` .

name -> (string)

The category by which to filter the intent stages. The descriptions for each option are as follows:

- `BotAlias` â The name of the bot alias.
- `BotVersion` â The version of the bot.
- `LocaleId` â The locale of the bot.
- `Modality` â The modality of the session with the bot (audio, DTMF, or text).
- `Channel` â The channel that the bot is integrated with.
- `SessionId` â The identifier of the session with the bot.
- `OriginatingRequestId` â The identifier of the first request in a session.
- `IntentName` â The name of the intent.
- `IntentStageName` â The stage in the intent.

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
- `IntentName` â `EQ` , `CO` .
- `IntentStageName` â `EQ` , `CO` .

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
    "name": "BotAliasId"|"BotVersion"|"LocaleId"|"Modality"|"Channel"|"SessionId"|"OriginatingRequestId"|"IntentName"|"IntentStageName",
    "operator": "EQ"|"GT"|"LT",
    "values": ["string", ...]
  }
  ...
]
```

`--max-results` (integer)

The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.

`--next-token` (string)

If the response from the ListIntentStageMetrics operation contains more results than specified in the maxResults parameter, a token is returned in the response.

Use the returned token in the nextToken parameter of a ListIntentStageMetrics request to return the next page of results. For a complete set of results, call the ListIntentStageMetrics operation until the nextToken returned in the response is null.

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

The identifier for the bot for which you retrieved intent stage metrics.

results -> (list)

The results for the intent stage metrics.

(structure)

An object containing the results for the intent stage metrics you requested and the bin and/or group they refer to, if applicable.

binKeys -> (list)

A list of objects containing the criteria you requested for binning results and the values of the bins.

(structure)

An object containing the criterion by which to bin the results and the value that defines that bin.

name -> (string)

The criterion by which to bin the results.

value -> (long)

The value of the criterion that defines the bin.

groupByKeys -> (list)

A list of objects containing the criteria you requested for grouping results and the values of the bins.

(structure)

Contains the category by which the intent stage analytics and the values for that category were grouped.

name -> (string)

A category by which the intent stage analytics were grouped.

value -> (string)

A member of the category by which the intent stage analytics were grouped.

metricsResults -> (list)

A list of objects, each of which contains a metric you want to list, the statistic for the metric you want to return, and the method by which to organize the results.

(structure)

An object containing the results for an intent stage metric you requested.

name -> (string)

The metric that you requested.

- `Count` â The number of times the intent stage occurred.
- `Success` â The number of times the intent stage succeeded.
- `Failure` â The number of times the intent stage failed.
- `Dropped` â The number of times the user dropped the intent stage.
- `Retry` â The number of times the bot tried to elicit a response from the user at this stage.

statistic -> (string)

The summary statistic that you requested to calculate.

- `Sum` â The total count for the category you provide in `name` .
- `Average` â The total count divided by the number of intent stages in the category you provide in `name` .
- `Max` â The highest count in the category you provide in `name` .

value -> (double)

The value of the summary statistic for the metric that you requested.

nextToken -> (string)

If the response from the ListIntentStageMetrics operation contains more results than specified in the maxResults parameter, a token is returned in the response.

Use the returned token in the nextToken parameter of a ListIntentStageMetrics request to return the next page of results. For a complete set of results, call the ListIntentStageMetrics operation until the nextToken returned in the response is null.