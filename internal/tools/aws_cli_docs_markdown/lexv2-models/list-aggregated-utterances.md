# list-aggregated-utterancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-aggregated-utterances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-aggregated-utterances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# list-aggregated-utterances

## Description

Provides a list of utterances that users have sent to the bot.

Utterances are aggregated by the text of the utterance. For example, all instances where customers used the phrase âI want to order pizzaâ are aggregated into the same line in the response.

You can see both detected utterances and missed utterances. A detected utterance is where the bot properly recognized the utterance and activated the associated intent. A missed utterance was not recognized by the bot and didnât activate an intent.

Utterances can be aggregated for a bot alias or for a bot version, but not both at the same time.

Utterances statistics are not generated under the following conditions:

- The `childDirected` field was set to true when the bot was created.
- You are using slot obfuscation with one or more slots.
- You opted out of participating in improving Amazon Lex.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/ListAggregatedUtterances)

## Synopsis

```
list-aggregated-utterances
--bot-id <value>
[--bot-alias-id <value>]
[--bot-version <value>]
--locale-id <value>
--aggregation-duration <value>
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

The unique identifier of the bot associated with this request.

`--bot-alias-id` (string)

The identifier of the bot alias associated with this request. If you specify the bot alias, you canât specify the bot version.

`--bot-version` (string)

The identifier of the bot version associated with this request. If you specify the bot version, you canât specify the bot alias.

`--locale-id` (string)

The identifier of the language and locale where the utterances were collected. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html) .

`--aggregation-duration` (structure)

The time window for aggregating the utterance information. You can specify a time between one hour and two weeks.

relativeAggregationDuration -> (structure)

The desired time window for aggregating utterances.

timeDimension -> (string)

The type of time period that the `timeValue` field represents.

timeValue -> (integer)

The period of the time window to gather statistics for. The valid value depends on the setting of the `timeDimension` field.

- `Hours` - 1/3/6/12/24
- `Days` - 3
- `Weeks` - 1/2

Shorthand Syntax:

```
relativeAggregationDuration={timeDimension=string,timeValue=integer}
```

JSON Syntax:

```
{
  "relativeAggregationDuration": {
    "timeDimension": "Hours"|"Days"|"Weeks",
    "timeValue": integer
  }
}
```

`--sort-by` (structure)

Specifies sorting parameters for the list of utterances. You can sort by the hit count, the missed count, or the number of distinct sessions the utterance appeared in.

attribute -> (string)

The utterance attribute to sort by.

order -> (string)

Specifies whether to sort the aggregated utterances in ascending or descending order.

Shorthand Syntax:

```
attribute=string,order=string
```

JSON Syntax:

```
{
  "attribute": "HitCount"|"MissedCount",
  "order": "Ascending"|"Descending"
}
```

`--filters` (list)

Provides the specification of a filter used to limit the utterances in the response to only those that match the filter specification. You can only specify one filter and one string to filter on.

(structure)

Filters responses returned by the `ListAggregatedUtterances` operation.

name -> (string)

The name of the field to filter the utterance list.

values -> (list)

The value to use for filtering the list of bots.

(string)

operator -> (string)

The operator to use for the filter. Specify `EQ` when the `ListAggregatedUtterances` operation should return only utterances that equal the specified value. Specify `CO` when the `ListAggregatedUtterances` operation should return utterances that contain the specified value.

Shorthand Syntax:

```
name=string,values=string,string,operator=string ...
```

JSON Syntax:

```
[
  {
    "name": "Utterance",
    "values": ["string", ...],
    "operator": "CO"|"EQ"
  }
  ...
]
```

`--max-results` (integer)

The maximum number of utterances to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned. If you donât specify the `maxResults` parameter, 1,000 results are returned.

`--next-token` (string)

If the response from the `ListAggregatedUtterances` operation contains more results that specified in the `maxResults` parameter, a token is returned in the response. Use that token in the `nextToken` parameter to return the next page of results.

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

The identifier of the bot that contains the utterances.

botAliasId -> (string)

The identifier of the bot alias that contains the utterances. If you specified the bot version, the bot alias ID isnât returned.

botVersion -> (string)

The identifier of the bot version that contains the utterances. If you specified the bot alias, the bot version isnât returned.

localeId -> (string)

The identifier of the language and locale that the utterances are in.

aggregationDuration -> (structure)

The time period used to aggregate the utterance data.

relativeAggregationDuration -> (structure)

The desired time window for aggregating utterances.

timeDimension -> (string)

The type of time period that the `timeValue` field represents.

timeValue -> (integer)

The period of the time window to gather statistics for. The valid value depends on the setting of the `timeDimension` field.

- `Hours` - 1/3/6/12/24
- `Days` - 3
- `Weeks` - 1/2

aggregationWindowStartTime -> (timestamp)

The date and time that the aggregation window begins. Only data collected after this time is returned in the results.

aggregationWindowEndTime -> (timestamp)

The date and time that the aggregation window ends. Only data collected between the start time and the end time are returned in the results.

aggregationLastRefreshedDateTime -> (timestamp)

The last date and time that the aggregated data was collected. The time period depends on the length of the aggregation window.

- **Hours** - for 1 hour time window, every half hour; otherwise every hour.
- **Days** - every 6 hours
- **Weeks** - for a one week time window, every 12 hours; otherwise, every day

aggregatedUtterancesSummaries -> (list)

Summaries of the aggregated utterance data. Each response contains information about the number of times that the utterance was seen during the time period, whether it was detected or missed, and when it was seen during the time period.

(structure)

Provides summary information for aggregated utterances. The `ListAggregatedUtterances` operations combines all instances of the same utterance into a single aggregated summary.

utterance -> (string)

The text of the utterance. If the utterance was used with the `RecognizeUtterance` operation, the text is the transcription of the audio utterance.

hitCount -> (integer)

The number of times that the utterance was detected by Amazon Lex during the time period. When an utterance is detected, it activates an intent or a slot.

missedCount -> (integer)

The number of times that the utterance was missed by Amazon Lex An utterance is missed when it doesnât activate an intent or slot.

utteranceFirstRecordedInAggregationDuration -> (timestamp)

The date and time that the utterance was first recorded in the time window for aggregation. An utterance may have been sent to Amazon Lex before that time, but only utterances within the time window are counted.

utteranceLastRecordedInAggregationDuration -> (timestamp)

The last date and time that an utterance was recorded in the time window for aggregation. An utterance may be sent to Amazon Lex after that time, but only utterances within the time window are counted.

containsDataFromDeletedResources -> (boolean)

Aggregated utterance data may contain utterances from versions of your bot that have since been deleted. When the aggregated contains this kind of data, this field is set to true.

nextToken -> (string)

A token that indicates whether there are more results to return in a response to the `ListAggregatedUtterances` operation. If the `nextToken` field is present, you send the contents as the `nextToken` parameter of a `ListAggregatedUtterances` operation request to get the next page of results.