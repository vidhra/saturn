# get-metric-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/get-metric-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/get-metric-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# get-metric-data

## Description

Gets historical metric data from the specified Amazon Connect instance.

For a description of each historical metric, see [Metrics definitions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) in the *Amazon Connect Administrator Guide* .

### Note

We recommend using the [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html) API. It provides more flexibility, features, and the ability to query longer time ranges than `GetMetricData` . Use it to retrieve historical agent and contact metrics for the last 3 months, at varying intervals. You can also use it to build custom dashboards to measure historical queue and agent performance. For example, you can track the number of incoming contacts for the last 7 days, with data split by day, to see how contact volume changed per day of the week.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/GetMetricData)

`get-metric-data` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `MetricResults`

## Synopsis

```
get-metric-data
--instance-id <value>
--start-time <value>
--end-time <value>
--filters <value>
[--groupings <value>]
--historical-metrics <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

`--start-time` (timestamp)

The timestamp, in UNIX Epoch time format, at which to start the reporting interval for the retrieval of historical metrics data. The time must be specified using a multiple of 5 minutes, such as 10:05, 10:10, 10:15.

The start time cannot be earlier than 24 hours before the time of the request. Historical metrics are available only for 24 hours.

`--end-time` (timestamp)

The timestamp, in UNIX Epoch time format, at which to end the reporting interval for the retrieval of historical metrics data. The time must be specified using an interval of 5 minutes, such as 11:00, 11:05, 11:10, and must be later than the start time timestamp.

The time range between the start and end time must be less than 24 hours.

`--filters` (structure)

The queues, up to 100, or channels, to use to filter the metrics returned. Metric data is retrieved only for the resources associated with the queues or channels included in the filter. You can include both queue IDs and queue ARNs in the same request. VOICE, CHAT, and TASK channels are supported.

RoutingStepExpression is not a valid filter for GetMetricData and we recommend switching to GetMetricDataV2 for more up-to-date features.

### Note

To filter by `Queues` , enter the queue ID/ARN, not the name of the queue.

Queues -> (list)

The queues to use to filter the metrics. You should specify at least one queue, and can specify up to 100 queues per request. The `GetCurrentMetricsData` API in particular requires a queue when you include a `Filter` in your request.

(string)

Channels -> (list)

The channel to use to filter the metrics.

(string)

RoutingProfiles -> (list)

A list of up to 100 routing profile IDs or ARNs.

(string)

RoutingStepExpressions -> (list)

A list of expressions as a filter, in which an expression is an object of a step in a routing criteria.

(string)

Shorthand Syntax:

```
Queues=string,string,Channels=string,string,RoutingProfiles=string,string,RoutingStepExpressions=string,string
```

JSON Syntax:

```
{
  "Queues": ["string", ...],
  "Channels": ["VOICE"|"CHAT"|"TASK"|"EMAIL", ...],
  "RoutingProfiles": ["string", ...],
  "RoutingStepExpressions": ["string", ...]
}
```

`--groupings` (list)

The grouping applied to the metrics returned. For example, when results are grouped by queue, the metrics returned are grouped by queue. The values returned apply to the metrics for each queue rather than aggregated for all queues.

If no grouping is specified, a summary of metrics for all queues is returned.

RoutingStepExpression is not a valid filter for GetMetricData and we recommend switching to GetMetricDataV2 for more up-to-date features.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  QUEUE
  CHANNEL
  ROUTING_PROFILE
  ROUTING_STEP_EXPRESSION
```

`--historical-metrics` (list)

The metrics to retrieve. Specify the name, unit, and statistic for each metric. The following historical metrics are available. For a description of each metric, see [Metrics definition](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) in the *Amazon Connect Administrator Guide* .

### Note

This API does not support a contacts incoming metric (thereâs no CONTACTS_INCOMING metric missing from the documented list).

ABANDON_TIME

Unit: SECONDS

Statistic: AVG

AFTER_CONTACT_WORK_TIME

Unit: SECONDS

Statistic: AVG

API_CONTACTS_HANDLED

Unit: COUNT

Statistic: SUM

CALLBACK_CONTACTS_HANDLED

Unit: COUNT

Statistic: SUM

CONTACTS_ABANDONED

Unit: COUNT

Statistic: SUM

CONTACTS_AGENT_HUNG_UP_FIRST

Unit: COUNT

Statistic: SUM

CONTACTS_CONSULTED

Unit: COUNT

Statistic: SUM

CONTACTS_HANDLED

Unit: COUNT

Statistic: SUM

CONTACTS_HANDLED_INCOMING

Unit: COUNT

Statistic: SUM

CONTACTS_HANDLED_OUTBOUND

Unit: COUNT

Statistic: SUM

CONTACTS_HOLD_ABANDONS

Unit: COUNT

Statistic: SUM

CONTACTS_MISSED

Unit: COUNT

Statistic: SUM

CONTACTS_QUEUED

Unit: COUNT

Statistic: SUM

CONTACTS_TRANSFERRED_IN

Unit: COUNT

Statistic: SUM

CONTACTS_TRANSFERRED_IN_FROM_QUEUE

Unit: COUNT

Statistic: SUM

CONTACTS_TRANSFERRED_OUT

Unit: COUNT

Statistic: SUM

CONTACTS_TRANSFERRED_OUT_FROM_QUEUE

Unit: COUNT

Statistic: SUM

HANDLE_TIME

Unit: SECONDS

Statistic: AVG

HOLD_TIME

Unit: SECONDS

Statistic: AVG

INTERACTION_AND_HOLD_TIME

Unit: SECONDS

Statistic: AVG

INTERACTION_TIME

Unit: SECONDS

Statistic: AVG

OCCUPANCY

Unit: PERCENT

Statistic: AVG

QUEUE_ANSWER_TIME

Unit: SECONDS

Statistic: AVG

QUEUED_TIME

Unit: SECONDS

Statistic: MAX

SERVICE_LEVEL

You can include up to 20 SERVICE_LEVEL metrics in a request.

Unit: PERCENT

Statistic: AVG

Threshold: For `ThresholdValue` , enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison` , you must enter `LT` (for âLess thanâ).

(structure)

Contains information about a historical metric. For a description of each metric, see [Metrics definitions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) in the *Amazon Connect Administrator Guide* .

Name -> (string)

The name of the metric.

Threshold -> (structure)

The threshold for the metric, used with service level metrics.

Comparison -> (string)

The type of comparison. Only âless thanâ (LT) comparisons are supported.

ThresholdValue -> (double)

The threshold value to compare.

Statistic -> (string)

The statistic for the metric.

Unit -> (string)

The unit for the metric.

Shorthand Syntax:

```
Name=string,Threshold={Comparison=string,ThresholdValue=double},Statistic=string,Unit=string ...
```

JSON Syntax:

```
[
  {
    "Name": "CONTACTS_QUEUED"|"CONTACTS_HANDLED"|"CONTACTS_ABANDONED"|"CONTACTS_CONSULTED"|"CONTACTS_AGENT_HUNG_UP_FIRST"|"CONTACTS_HANDLED_INCOMING"|"CONTACTS_HANDLED_OUTBOUND"|"CONTACTS_HOLD_ABANDONS"|"CONTACTS_TRANSFERRED_IN"|"CONTACTS_TRANSFERRED_OUT"|"CONTACTS_TRANSFERRED_IN_FROM_QUEUE"|"CONTACTS_TRANSFERRED_OUT_FROM_QUEUE"|"CONTACTS_MISSED"|"CALLBACK_CONTACTS_HANDLED"|"API_CONTACTS_HANDLED"|"OCCUPANCY"|"HANDLE_TIME"|"AFTER_CONTACT_WORK_TIME"|"QUEUED_TIME"|"ABANDON_TIME"|"QUEUE_ANSWER_TIME"|"HOLD_TIME"|"INTERACTION_TIME"|"INTERACTION_AND_HOLD_TIME"|"SERVICE_LEVEL",
    "Threshold": {
      "Comparison": "LT",
      "ThresholdValue": double
    },
    "Statistic": "SUM"|"MAX"|"AVG",
    "Unit": "SECONDS"|"COUNT"|"PERCENT"
  }
  ...
]
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

NextToken -> (string)

If there are additional results, this is the token for the next set of results.

The token expires after 5 minutes from the time it is created. Subsequent requests that use the token must use the same request parameters as the request that generated the token.

MetricResults -> (list)

Information about the historical metrics.

If no grouping is specified, a summary of metric data is returned.

(structure)

Contains information about the historical metrics retrieved.

Dimensions -> (structure)

The dimension for the metrics.

Queue -> (structure)

Information about the queue for which metrics are returned.

Id -> (string)

The identifier of the queue.

Arn -> (string)

The Amazon Resource Name (ARN) of the queue.

Channel -> (string)

The channel used for grouping and filters.

RoutingProfile -> (structure)

Information about the routing profile assigned to the user.

Id -> (string)

The identifier of the routing profile.

Arn -> (string)

The Amazon Resource Name (ARN) of the routing profile.

RoutingStepExpression -> (string)

The expression of a step in a routing criteria.

Collections -> (list)

The set of metrics.

(structure)

Contains the data for a historical metric.

Metric -> (structure)

Information about the metric.

Name -> (string)

The name of the metric.

Threshold -> (structure)

The threshold for the metric, used with service level metrics.

Comparison -> (string)

The type of comparison. Only âless thanâ (LT) comparisons are supported.

ThresholdValue -> (double)

The threshold value to compare.

Statistic -> (string)

The statistic for the metric.

Unit -> (string)

The unit for the metric.

Value -> (double)

The value of the metric.