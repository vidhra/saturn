# get-current-metric-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/get-current-metric-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/get-current-metric-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# get-current-metric-data

## Description

Gets the real-time metric data from the specified Amazon Connect instance.

For a description of each metric, see [Metrics definitions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) in the *Amazon Connect Administrator Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/GetCurrentMetricData)

## Synopsis

```
get-current-metric-data
--instance-id <value>
--filters <value>
[--groupings <value>]
--current-metrics <value>
[--next-token <value>]
[--max-results <value>]
[--sort-criteria <value>]
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

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

`--filters` (structure)

The filters to apply to returned metrics. You can filter up to the following limits:

- Queues: 100
- Routing profiles: 100
- Channels: 3 (VOICE, CHAT, and TASK channels are supported.)
- RoutingStepExpressions: 50

Metric data is retrieved only for the resources associated with the queues or routing profiles, and by any channels included in the filter. (You cannot filter by both queue AND routing profile.) You can include both resource IDs and resource ARNs in the same request.

When using the `RoutingStepExpression` filter, you need to pass exactly one `QueueId` . The filter is also case sensitive so when using the `RoutingStepExpression` filter, grouping by `ROUTING_STEP_EXPRESSION` is required.

Currently tagging is only supported on the resources that are passed in the filter.

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

The grouping applied to the metrics returned. For example, when grouped by `QUEUE` , the metrics returned apply to each queue rather than aggregated for all queues.

- If you group by `CHANNEL` , you should include a Channels filter. VOICE, CHAT, and TASK channels are supported.
- If you group by `ROUTING_PROFILE` , you must include either a queue or routing profile filter. In addition, a routing profile filter is required for metrics `CONTACTS_SCHEDULED` , `CONTACTS_IN_QUEUE` , and `OLDEST_CONTACT_AGE` .
- If no `Grouping` is included in the request, a summary of metrics is returned.
- When using the `RoutingStepExpression` filter, group by `ROUTING_STEP_EXPRESSION` is required.

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

`--current-metrics` (list)

The metrics to retrieve. Specify the name and unit for each metric. The following metrics are available. For a description of all the metrics, see [Metrics definitions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) in the *Amazon Connect Administrator Guide* .

AGENTS_AFTER_CONTACT_WORK

Unit: COUNT

Name in real-time metrics report: [ACW](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#aftercallwork-real-time)

AGENTS_AVAILABLE

Unit: COUNT

Name in real-time metrics report: [Available](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#available-real-time)

AGENTS_ERROR

Unit: COUNT

Name in real-time metrics report: [Error](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#error-real-time)

AGENTS_NON_PRODUCTIVE

Unit: COUNT

Name in real-time metrics report: [NPT (Non-Productive Time)](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#non-productive-time-real-time)

AGENTS_ON_CALL

Unit: COUNT

Name in real-time metrics report: [On contact](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#on-call-real-time)

AGENTS_ON_CONTACT

Unit: COUNT

Name in real-time metrics report: [On contact](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#on-call-real-time)

AGENTS_ONLINE

Unit: COUNT

Name in real-time metrics report: [Online](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#online-real-time)

AGENTS_STAFFED

Unit: COUNT

Name in real-time metrics report: [Staffed](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#staffed-real-time)

CONTACTS_IN_QUEUE

Unit: COUNT

Name in real-time metrics report: [In queue](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#in-queue-real-time)

CONTACTS_SCHEDULED

Unit: COUNT

Name in real-time metrics report: [Scheduled](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#scheduled-real-time)

OLDEST_CONTACT_AGE

Unit: SECONDS

When you use groupings, Unit says SECONDS and the Value is returned in SECONDS.

When you do not use groupings, Unit says SECONDS but the Value is returned in MILLISECONDS. For example, if you get a response like this:

`{ "Metric": { "Name": "OLDEST_CONTACT_AGE", "Unit": "SECONDS" }, "Value": 24113.0` }

The actual OLDEST_CONTACT_AGE is 24 seconds.

When the filter `RoutingStepExpression` is used, this metric is still calculated from enqueue time. For example, if a contact that has been queued under `<Expression 1>` for 10 seconds has expired and `<Expression 2>` becomes active, then `OLDEST_CONTACT_AGE` for this queue will be counted starting from 10, not 0.

Name in real-time metrics report: [Oldest](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#oldest-real-time)

SLOTS_ACTIVE

Unit: COUNT

Name in real-time metrics report: [Active](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#active-real-time)

SLOTS_AVAILABLE

Unit: COUNT

Name in real-time metrics report: [Availability](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#availability-real-time)

(structure)

Contains information about a real-time metric. For a description of each metric, see [Metrics definitions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) in the *Amazon Connect Administrator Guide* .

Name -> (string)

The name of the metric.

Unit -> (string)

The unit for the metric.

Shorthand Syntax:

```
Name=string,Unit=string ...
```

JSON Syntax:

```
[
  {
    "Name": "AGENTS_ONLINE"|"AGENTS_AVAILABLE"|"AGENTS_ON_CALL"|"AGENTS_NON_PRODUCTIVE"|"AGENTS_AFTER_CONTACT_WORK"|"AGENTS_ERROR"|"AGENTS_STAFFED"|"CONTACTS_IN_QUEUE"|"OLDEST_CONTACT_AGE"|"CONTACTS_SCHEDULED"|"AGENTS_ON_CONTACT"|"SLOTS_ACTIVE"|"SLOTS_AVAILABLE",
    "Unit": "SECONDS"|"COUNT"|"PERCENT"
  }
  ...
]
```

`--next-token` (string)

The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

The token expires after 5 minutes from the time it is created. Subsequent requests that use the token must use the same request parameters as the request that generated the token.

`--max-results` (integer)

The maximum number of results to return per page.

`--sort-criteria` (list)

The way to sort the resulting response based on metrics. You can enter one sort criteria. By default resources are sorted based on `AGENTS_ONLINE` , `DESCENDING` . The metric collection is sorted based on the input metrics.

Note the following:

- Sorting on `SLOTS_ACTIVE` and `SLOTS_AVAILABLE` is not supported.

(structure)

The way to sort the resulting response based on metrics. By default resources are sorted based on `AGENTS_ONLINE` , `DESCENDING` . The metric collection is sorted based on the input metrics.

SortByMetric -> (string)

The current metric names.

SortOrder -> (string)

The way to sort.

Shorthand Syntax:

```
SortByMetric=string,SortOrder=string ...
```

JSON Syntax:

```
[
  {
    "SortByMetric": "AGENTS_ONLINE"|"AGENTS_AVAILABLE"|"AGENTS_ON_CALL"|"AGENTS_NON_PRODUCTIVE"|"AGENTS_AFTER_CONTACT_WORK"|"AGENTS_ERROR"|"AGENTS_STAFFED"|"CONTACTS_IN_QUEUE"|"OLDEST_CONTACT_AGE"|"CONTACTS_SCHEDULED"|"AGENTS_ON_CONTACT"|"SLOTS_ACTIVE"|"SLOTS_AVAILABLE",
    "SortOrder": "ASCENDING"|"DESCENDING"
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

NextToken -> (string)

If there are additional results, this is the token for the next set of results.

The token expires after 5 minutes from the time it is created. Subsequent requests that use the token must use the same request parameters as the request that generated the token.

MetricResults -> (list)

Information about the real-time metrics.

(structure)

Contains information about a set of real-time metrics.

Dimensions -> (structure)

The dimensions for the metrics.

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

Contains the data for a real-time metric.

Metric -> (structure)

Information about the metric.

Name -> (string)

The name of the metric.

Unit -> (string)

The unit for the metric.

Value -> (double)

The value of the metric.

DataSnapshotTime -> (timestamp)

The time at which the metrics were retrieved and cached for pagination.

ApproximateTotalCount -> (long)

The total count of the result, regardless of the current page size.