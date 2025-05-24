# describe-alarmsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/describe-alarms.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/describe-alarms.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudwatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/index.html#cli-aws-cloudwatch) ]

# describe-alarms

## Description

Retrieves the specified alarms. You can filter the results by specifying a prefix for the alarm name, the alarm state, or a prefix for any action.

To use this operation and return information about composite alarms, you must be signed on with the `cloudwatch:DescribeAlarms` permission that is scoped to `*` . You canât return information about composite alarms if your `cloudwatch:DescribeAlarms` permission has a narrower scope.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms)

`describe-alarms` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `MetricAlarms`, `CompositeAlarms`

## Synopsis

```
describe-alarms
[--alarm-names <value>]
[--alarm-name-prefix <value>]
[--alarm-types <value>]
[--children-of-alarm-name <value>]
[--parents-of-alarm-name <value>]
[--state-value <value>]
[--action-prefix <value>]
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

`--alarm-names` (list)

The names of the alarms to retrieve information about.

(string)

Syntax:

```
"string" "string" ...
```

`--alarm-name-prefix` (string)

An alarm name prefix. If you specify this parameter, you receive information about all alarms that have names that start with this prefix.

If this parameter is specified, you cannot specify `AlarmNames` .

`--alarm-types` (list)

Use this parameter to specify whether you want the operation to return metric alarms or composite alarms. If you omit this parameter, only metric alarms are returned, even if composite alarms exist in the account.

For example, if you omit this parameter or specify `MetricAlarms` , the operation returns only a list of metric alarms. It does not return any composite alarms, even if composite alarms exist in the account.

If you specify `CompositeAlarms` , the operation returns only a list of composite alarms, and does not return any metric alarms.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  CompositeAlarm
  MetricAlarm
```

`--children-of-alarm-name` (string)

If you use this parameter and specify the name of a composite alarm, the operation returns information about the âchildrenâ alarms of the alarm you specify. These are the metric alarms and composite alarms referenced in the `AlarmRule` field of the composite alarm that you specify in `ChildrenOfAlarmName` . Information about the composite alarm that you name in `ChildrenOfAlarmName` is not returned.

If you specify `ChildrenOfAlarmName` , you cannot specify any other parameters in the request except for `MaxRecords` and `NextToken` . If you do so, you receive a validation error.

### Note

Only the `Alarm Name` , `ARN` , `StateValue` (OK/ALARM/INSUFFICIENT_DATA), and `StateUpdatedTimestamp` information are returned by this operation when you use this parameter. To get complete information about these alarms, perform another `DescribeAlarms` operation and specify the parent alarm names in the `AlarmNames` parameter.

`--parents-of-alarm-name` (string)

If you use this parameter and specify the name of a metric or composite alarm, the operation returns information about the âparentâ alarms of the alarm you specify. These are the composite alarms that have `AlarmRule` parameters that reference the alarm named in `ParentsOfAlarmName` . Information about the alarm that you specify in `ParentsOfAlarmName` is not returned.

If you specify `ParentsOfAlarmName` , you cannot specify any other parameters in the request except for `MaxRecords` and `NextToken` . If you do so, you receive a validation error.

### Note

Only the Alarm Name and ARN are returned by this operation when you use this parameter. To get complete information about these alarms, perform another `DescribeAlarms` operation and specify the parent alarm names in the `AlarmNames` parameter.

`--state-value` (string)

Specify this parameter to receive information only about alarms that are currently in the state that you specify.

Possible values:

- `OK`
- `ALARM`
- `INSUFFICIENT_DATA`

`--action-prefix` (string)

Use this parameter to filter the results of the operation to only those alarms that use a certain alarm action. For example, you could specify the ARN of an SNS topic to find all alarms that send notifications to that topic.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To list information about an alarm**

The following example uses the `describe-alarms` command to provide information about the alarm named âmyalarmâ:

```
aws cloudwatch describe-alarms --alarm-names "myalarm"
```

Output:

```
{
    "MetricAlarms": [
        {
            "EvaluationPeriods": 2,
            "AlarmArn": "arn:aws:cloudwatch:us-east-1:123456789012:alarm:myalarm",
            "StateUpdatedTimestamp": "2014-04-09T18:59:06.442Z",
            "AlarmConfigurationUpdatedTimestamp": "2012-12-27T00:49:54.032Z",
            "ComparisonOperator": "GreaterThanThreshold",
            "AlarmActions": [
                "arn:aws:sns:us-east-1:123456789012:myHighCpuAlarm"
            ],
            "Namespace": "AWS/EC2",
            "AlarmDescription": "CPU usage exceeds 70 percent",
            "StateReasonData": "{\"version\":\"1.0\",\"queryDate\":\"2014-04-09T18:59:06.419+0000\",\"startDate\":\"2014-04-09T18:44:00.000+0000\",\"statistic\":\"Average\",\"period\":300,\"recentDatapoints\":[38.958,40.292],\"threshold\":70.0}",
            "Period": 300,
            "StateValue": "OK",
            "Threshold": 70.0,
            "AlarmName": "myalarm",
            "Dimensions": [
                {
                    "Name": "InstanceId",
                    "Value": "i-0c986c72"
                }
            ],
            "Statistic": "Average",
            "StateReason": "Threshold Crossed: 2 datapoints were not greater than the threshold (70.0). The most recent datapoints: [38.958, 40.292].",
            "InsufficientDataActions": [],
            "OKActions": [],
            "ActionsEnabled": true,
            "MetricName": "CPUUtilization"
        }
    ]
}
```

## Output

CompositeAlarms -> (list)

The information about any composite alarms returned by the operation.

(structure)

The details about a composite alarm.

ActionsEnabled -> (boolean)

Indicates whether actions should be executed during any changes to the alarm state.

AlarmActions -> (list)

The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).

(string)

AlarmArn -> (string)

The Amazon Resource Name (ARN) of the alarm.

AlarmConfigurationUpdatedTimestamp -> (timestamp)

The time stamp of the last update to the alarm configuration.

AlarmDescription -> (string)

The description of the alarm.

AlarmName -> (string)

The name of the alarm.

AlarmRule -> (string)

The rule that this alarm uses to evaluate its alarm state.

InsufficientDataActions -> (list)

The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).

(string)

OKActions -> (list)

The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).

(string)

StateReason -> (string)

An explanation for the alarm state, in text format.

StateReasonData -> (string)

An explanation for the alarm state, in JSON format.

StateUpdatedTimestamp -> (timestamp)

Tracks the timestamp of any state update, even if `StateValue` doesnât change.

StateValue -> (string)

The state value for the alarm.

StateTransitionedTimestamp -> (timestamp)

The timestamp of the last change to the alarmâs `StateValue` .

ActionsSuppressedBy -> (string)

When the value is `ALARM` , it means that the actions are suppressed because the suppressor alarm is in `ALARM` When the value is `WaitPeriod` , it means that the actions are suppressed because the composite alarm is waiting for the suppressor alarm to go into into the `ALARM` state. The maximum waiting time is as specified in `ActionsSuppressorWaitPeriod` . After this time, the composite alarm performs its actions. When the value is `ExtensionPeriod` , it means that the actions are suppressed because the composite alarm is waiting after the suppressor alarm went out of the `ALARM` state. The maximum waiting time is as specified in `ActionsSuppressorExtensionPeriod` . After this time, the composite alarm performs its actions.

ActionsSuppressedReason -> (string)

Captures the reason for action suppression.

ActionsSuppressor -> (string)

Actions will be suppressed if the suppressor alarm is in the `ALARM` state. `ActionsSuppressor` can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm.

ActionsSuppressorWaitPeriod -> (integer)

The maximum time in seconds that the composite alarm waits for the suppressor alarm to go into the `ALARM` state. After this time, the composite alarm performs its actions.

### Warning

`WaitPeriod` is required only when `ActionsSuppressor` is specified.

ActionsSuppressorExtensionPeriod -> (integer)

The maximum time in seconds that the composite alarm waits after suppressor alarm goes out of the `ALARM` state. After this time, the composite alarm performs its actions.

### Warning

`ExtensionPeriod` is required only when `ActionsSuppressor` is specified.

MetricAlarms -> (list)

The information about any metric alarms returned by the operation.

(structure)

The details about a metric alarm.

AlarmName -> (string)

The name of the alarm.

AlarmArn -> (string)

The Amazon Resource Name (ARN) of the alarm.

AlarmDescription -> (string)

The description of the alarm.

AlarmConfigurationUpdatedTimestamp -> (timestamp)

The time stamp of the last update to the alarm configuration.

ActionsEnabled -> (boolean)

Indicates whether actions should be executed during any changes to the alarm state.

OKActions -> (list)

The actions to execute when this alarm transitions to the `OK` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

(string)

AlarmActions -> (list)

The actions to execute when this alarm transitions to the `ALARM` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

(string)

InsufficientDataActions -> (list)

The actions to execute when this alarm transitions to the `INSUFFICIENT_DATA` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

(string)

StateValue -> (string)

The state value for the alarm.

StateReason -> (string)

An explanation for the alarm state, in text format.

StateReasonData -> (string)

An explanation for the alarm state, in JSON format.

StateUpdatedTimestamp -> (timestamp)

The time stamp of the last update to the value of either the `StateValue` or `EvaluationState` parameters.

MetricName -> (string)

The name of the metric associated with the alarm, if this is an alarm based on a single metric.

Namespace -> (string)

The namespace of the metric associated with the alarm.

Statistic -> (string)

The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use `ExtendedStatistic` .

ExtendedStatistic -> (string)

The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

Dimensions -> (list)

The dimensions for the metric associated with the alarm.

(structure)

A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish `InstanceId` as a dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

Name -> (string)

The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (`:` ). ASCII control characters are not supported as part of dimension names.

Value -> (string)

The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

Period -> (integer)

The period, in seconds, over which the statistic is applied.

Unit -> (string)

The unit of the metric associated with the alarm.

EvaluationPeriods -> (integer)

The number of periods over which data is compared to the specified threshold.

DatapointsToAlarm -> (integer)

The number of data points that must be breaching to trigger the alarm.

Threshold -> (double)

The value to compare with the specified statistic.

ComparisonOperator -> (string)

The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.

TreatMissingData -> (string)

Sets how this alarm is to handle missing data points. The valid values are `breaching` , `notBreaching` , `ignore` , and `missing` . For more information, see [Configuring how CloudWatch alarms treat missing data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data) .

If this parameter is omitted, the default behavior of `missing` is used.

EvaluateLowSampleCountPercentile -> (string)

Used only for alarms based on percentiles. If `ignore` , the alarm state does not change during periods with too few data points to be statistically significant. If `evaluate` or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.

Metrics -> (list)

An array of MetricDataQuery structures, used in an alarm based on a metric math expression. Each structure either retrieves a metric or performs a math expression. One item in the Metrics array is the math expression that the alarm watches. This expression by designated by having `ReturnData` set to true.

(structure)

This structure is used in both `GetMetricData` and `PutMetricAlarm` . The supported use of this structure is different for those two operations.

When used in `GetMetricData` , it indicates the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a Metrics Insights query or a math expression. A single `GetMetricData` call can include up to 500 `MetricDataQuery` structures.

When used in `PutMetricAlarm` , it enables you to create an alarm based on a metric math expression. Each `MetricDataQuery` in the array specifies either a metric to retrieve, or a math expression to be performed on retrieved metrics. A single `PutMetricAlarm` call can include up to 20 `MetricDataQuery` structures in the array. The 20 structures can include as many as 10 structures that contain a `MetricStat` parameter to retrieve a metric, and as many as 10 structures that contain the `Expression` parameter to perform a math expression. Of those `Expression` structures, one must have `true` as the value for `ReturnData` . The result of this expression is the value the alarm watches.

Any expression used in a `PutMetricAlarm` operation must return a single time series. For more information, see [Metric Math Syntax and Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User Guide* .

Some of the parameters of this structure also have different uses whether you are using this structure in a `GetMetricData` operation or a `PutMetricAlarm` operation. These differences are explained in the following parameter list.

Id -> (string)

A short name used to tie this object to the results in the response. This name must be unique within a single call to `GetMetricData` . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

MetricStat -> (structure)

The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.

Within one MetricDataQuery object, you must specify either `Expression` or `MetricStat` but not both.

Metric -> (structure)

The metric to return, including the metric name, namespace, and dimensions.

Namespace -> (string)

The namespace of the metric.

MetricName -> (string)

The name of the metric. This is a required field.

Dimensions -> (list)

The dimensions for the metric.

(structure)

A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish `InstanceId` as a dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

Name -> (string)

The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (`:` ). ASCII control characters are not supported as part of dimension names.

Value -> (string)

The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

Period -> (integer)

The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 20, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

If the `StartTime` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

- Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
- Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
- Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

Stat -> (string)

The statistic to return. It can include any CloudWatch statistic or extended statistic.

Unit -> (string)

When you are using a `Put` operation, this defines what unit you want to use when storing the metric.

In a `Get` operation, if you omit `Unit` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

Expression -> (string)

This field can contain either a Metrics Insights query, or a metric math expression to be performed on the returned data. For more information about Metrics Insights queries, see [Metrics Insights query components and syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-querylanguage) in the *Amazon CloudWatch User Guide* .

A math expression can use the `Id` of the other metrics or queries to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions. For more information about metric math expressions, see [Metric Math Syntax and Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User Guide* .

Within each MetricDataQuery object, you must specify either `Expression` or `MetricStat` but not both.

Label -> (string)

A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default.

You can put dynamic expressions into a label, so that it is more descriptive. For more information, see [Using Dynamic Labels](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html) .

ReturnData -> (boolean)

When used in `GetMetricData` , this option indicates whether to return the timestamps and raw data values of this metric. If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify `false` . If you omit this, the default of `true` is used.

When used in `PutMetricAlarm` , specify `true` for the one expression result to use as the alarm. For all other metrics and expressions in the same `PutMetricAlarm` operation, specify `ReturnData` as False.

Period -> (integer)

The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 20, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` operation that includes a `StorageResolution of 1 second` .

AccountId -> (string)

The ID of the account where the metrics are located.

If you are performing a `GetMetricData` operation in a monitoring account, use this to specify which account to retrieve this metric from.

If you are performing a `PutMetricAlarm` operation, use this to specify which account contains the metric that the alarm is watching.

ThresholdMetricId -> (string)

In an alarm based on an anomaly detection model, this is the ID of the `ANOMALY_DETECTION_BAND` function used as the threshold for the alarm.

EvaluationState -> (string)

If the value of this field is `PARTIAL_DATA` , the alarm is being evaluated based on only partial data. This happens if the query used for the alarm returns more than 10,000 metrics. For more information, see [Create alarms on Metrics Insights queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Metrics_Insights_Alarm.html) .

StateTransitionedTimestamp -> (timestamp)

The date and time that the alarmâs `StateValue` most recently changed.

NextToken -> (string)

The token that marks the start of the next batch of returned results.