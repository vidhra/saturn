# get-insight-rule-reportÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-insight-rule-report.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-insight-rule-report.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudwatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/index.html#cli-aws-cloudwatch) ]

# get-insight-rule-report

## Description

This operation returns the time series data collected by a Contributor Insights rule. The data includes the identity and number of contributors to the log group.

You can also optionally return one or more statistics about each data point in the time series. These statistics can include the following:

- `UniqueContributors` â the number of unique contributors for each data point.
- `MaxContributorValue` â the value of the top contributor for each data point. The identity of the contributor might change for each data point in the graph. If this rule aggregates by COUNT, the top contributor for each data point is the contributor with the most occurrences in that period. If the rule aggregates by SUM, the top contributor is the contributor with the highest sum in the log field specified by the ruleâs `Value` , during that period.
- `SampleCount` â the number of data points matched by the rule.
- `Sum` â the sum of the values from all contributors during the time period represented by that data point.
- `Minimum` â the minimum value from a single observation during the time period represented by that data point.
- `Maximum` â the maximum value from a single observation during the time period represented by that data point.
- `Average` â the average value from all contributors during the time period represented by that data point.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/GetInsightRuleReport)

## Synopsis

```
get-insight-rule-report
--rule-name <value>
--start-time <value>
--end-time <value>
--period <value>
[--max-contributor-count <value>]
[--metrics <value>]
[--order-by <value>]
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

`--rule-name` (string)

The name of the rule that you want to see data from.

`--start-time` (timestamp)

The start time of the data to use in the report. When used in a raw HTTP Query API, it is formatted as `yyyy-MM-dd'T'HH:mm:ss` . For example, `2019-07-01T23:59:59` .

`--end-time` (timestamp)

The end time of the data to use in the report. When used in a raw HTTP Query API, it is formatted as `yyyy-MM-dd'T'HH:mm:ss` . For example, `2019-07-01T23:59:59` .

`--period` (integer)

The period, in seconds, to use for the statistics in the `InsightRuleMetricDatapoint` results.

`--max-contributor-count` (integer)

The maximum number of contributors to include in the report. The range is 1 to 100. If you omit this, the default of 10 is used.

`--metrics` (list)

Specifies which metrics to use for aggregation of contributor values for the report. You can specify one or more of the following metrics:

- `UniqueContributors` â the number of unique contributors for each data point.
- `MaxContributorValue` â the value of the top contributor for each data point. The identity of the contributor might change for each data point in the graph. If this rule aggregates by COUNT, the top contributor for each data point is the contributor with the most occurrences in that period. If the rule aggregates by SUM, the top contributor is the contributor with the highest sum in the log field specified by the ruleâs `Value` , during that period.
- `SampleCount` â the number of data points matched by the rule.
- `Sum` â the sum of the values from all contributors during the time period represented by that data point.
- `Minimum` â the minimum value from a single observation during the time period represented by that data point.
- `Maximum` â the maximum value from a single observation during the time period represented by that data point.
- `Average` â the average value from all contributors during the time period represented by that data point.

(string)

Syntax:

```
"string" "string" ...
```

`--order-by` (string)

Determines what statistic to use to rank the contributors. Valid values are `Sum` and `Maximum` .

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To retrieve the time series data collected by a Contributor Insights rule**

The following `get-insight-rule-report` example returns the time series data collected by a Contributor Insights rule.

```
aws cloudwatch get-insight-rule-report \
    --rule-name Rule-A \
    --start-time 2024-10-13T20:15:00Z \
    --end-time 2024-10-13T20:30:00Z \
    --period 300
```

Output:

```
{
    "KeyLabels": [
        "PartitionKey"
    ],
    "AggregationStatistic": "Sum",
    "AggregateValue": 0.5,
    "ApproximateUniqueCount": 1,
    "Contributors": [
        {
            "Keys": [
                "RequestID"
            ],
            "ApproximateAggregateValue": 0.5,
            "Datapoints": [
                {
                    "Timestamp": "2024-10-13T21:00:00+00:00",
                    "ApproximateValue": 0.5
                }
            ]
        }
    ],
    "RuleAttributes": []
}
```

For more information, see [Use Contributor Insights to analyze high-cardinality data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) in the *Amazon CloudWatch User Guide*.

## Output

KeyLabels -> (list)

An array of the strings used as the keys for this rule. The keys are the dimensions used to classify contributors. If the rule contains more than one key, then each unique combination of values for the keys is counted as a unique contributor.

(string)

AggregationStatistic -> (string)

Specifies whether this rule aggregates contributor data by COUNT or SUM.

AggregateValue -> (double)

The sum of the values from all individual contributors that match the rule.

ApproximateUniqueCount -> (long)

An approximate count of the unique contributors found by this rule in this time period.

Contributors -> (list)

An array of the unique contributors found by this rule in this time period. If the rule contains multiple keys, each combination of values for the keys counts as a unique contributor.

(structure)

One of the unique contributors found by a Contributor Insights rule. If the rule contains multiple keys, then a unique contributor is a unique combination of values from all the keys in the rule.

If the rule contains a single key, then each unique contributor is each unique value for this key.

For more information, see [GetInsightRuleReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetInsightRuleReport.html) .

Keys -> (list)

One of the log entry field keywords that is used to define contributors for this rule.

(string)

ApproximateAggregateValue -> (double)

An approximation of the aggregate value that comes from this contributor.

Datapoints -> (list)

An array of the data points where this contributor is present. Only the data points when this contributor appeared are included in the array.

(structure)

One data point related to one contributor.

For more information, see [GetInsightRuleReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetInsightRuleReport.html) and [InsightRuleContributor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_InsightRuleContributor.html) .

Timestamp -> (timestamp)

The timestamp of the data point.

ApproximateValue -> (double)

The approximate value that this contributor added during this timestamp.

MetricDatapoints -> (list)

A time series of metric data points that matches the time period in the rule request.

(structure)

One data point from the metric time series returned in a Contributor Insights rule report.

For more information, see [GetInsightRuleReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetInsightRuleReport.html) .

Timestamp -> (timestamp)

The timestamp of the data point.

UniqueContributors -> (double)

The number of unique contributors who published data during this timestamp.

This statistic is returned only if you included it in the `Metrics` array in your request.

MaxContributorValue -> (double)

The maximum value provided by one contributor during this timestamp. Each timestamp is evaluated separately, so the identity of the max contributor could be different for each timestamp.

This statistic is returned only if you included it in the `Metrics` array in your request.

SampleCount -> (double)

The number of occurrences that matched the rule during this data point.

This statistic is returned only if you included it in the `Metrics` array in your request.

Average -> (double)

The average value from all contributors during the time period represented by that data point.

This statistic is returned only if you included it in the `Metrics` array in your request.

Sum -> (double)

The sum of the values from all contributors during the time period represented by that data point.

This statistic is returned only if you included it in the `Metrics` array in your request.

Minimum -> (double)

The minimum value from a single contributor during the time period represented by that data point.

This statistic is returned only if you included it in the `Metrics` array in your request.

Maximum -> (double)

The maximum value from a single occurence from a single contributor during the time period represented by that data point.

This statistic is returned only if you included it in the `Metrics` array in your request.