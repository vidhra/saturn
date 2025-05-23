# put-metric-alarmÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudwatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/index.html#cli-aws-cloudwatch) ]

# put-metric-alarm

## Description

Creates or updates an alarm and associates it with the specified metric, metric math expression, anomaly detection model, or Metrics Insights query. For more information about using a Metrics Insights query for an alarm, see [Create alarms on Metrics Insights queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Metrics_Insights_Alarm.html) .

Alarms based on anomaly detection models cannot have Auto Scaling actions.

When this operation creates an alarm, the alarm state is immediately set to `INSUFFICIENT_DATA` . The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.

When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.

If you are an IAM user, you must have Amazon EC2 permissions for some alarm operations:

- The `iam:CreateServiceLinkedRole` permission for all alarms with EC2 actions
- The `iam:CreateServiceLinkedRole` permissions to create an alarm with Systems Manager OpsItem or response plan actions.

The first time you create an alarm in the Amazon Web Services Management Console, the CLI, or by using the PutMetricAlarm API, CloudWatch creates the necessary service-linked role for you. The service-linked roles are called `AWSServiceRoleForCloudWatchEvents` and `AWSServiceRoleForCloudWatchAlarms_ActionSSM` . For more information, see [Amazon Web Services service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role) .

Each `PutMetricAlarm` action has a maximum uncompressed payload of 120 KB.

**Cross-account alarms**

You can set an alarm on metrics in the current account, or in another account. To create a cross-account alarm that watches a metric in a different account, you must have completed the following pre-requisites:

- The account where the metrics are located (the *sharing account* ) must already have a sharing role named **CloudWatch-CrossAccountSharingRole** . If it does not already have this role, you must create it using the instructions in **Set up a sharing account** in [Cross-account cross-Region CloudWatch console](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html#enable-cross-account-cross-Region) . The policy for that role must grant access to the ID of the account where you are creating the alarm.
- The account where you are creating the alarm (the *monitoring account* ) must already have a service-linked role named **AWSServiceRoleForCloudWatchCrossAccount** to allow CloudWatch to assume the sharing role in the sharing account. If it does not, you must create it following the directions in **Set up a monitoring account** in [Cross-account cross-Region CloudWatch console](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html#enable-cross-account-cross-Region) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutMetricAlarm)

## Synopsis

```
put-metric-alarm
--alarm-name <value>
[--alarm-description <value>]
[--actions-enabled | --no-actions-enabled]
[--ok-actions <value>]
[--alarm-actions <value>]
[--insufficient-data-actions <value>]
[--metric-name <value>]
[--namespace <value>]
[--statistic <value>]
[--extended-statistic <value>]
[--dimensions <value>]
[--period <value>]
[--unit <value>]
--evaluation-periods <value>
[--datapoints-to-alarm <value>]
[--threshold <value>]
--comparison-operator <value>
[--treat-missing-data <value>]
[--evaluate-low-sample-count-percentile <value>]
[--metrics <value>]
[--tags <value>]
[--threshold-metric-id <value>]
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

`--alarm-name` (string)

The name for the alarm. This name must be unique within the Region.

The name must contain only UTF-8 characters, and canât contain ASCII control characters

`--alarm-description` (string)

The description for the alarm.

`--actions-enabled` | `--no-actions-enabled` (boolean)

Indicates whether actions should be executed during any changes to the alarm state. The default is `TRUE` .

`--ok-actions` (list)

The actions to execute when this alarm transitions to an `OK` state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid values:

**EC2 actions:**

- `arn:aws:automate:*region* :ec2:stop`
- `arn:aws:automate:*region* :ec2:terminate`
- `arn:aws:automate:*region* :ec2:reboot`
- `arn:aws:automate:*region* :ec2:recover`
- `arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Stop/1.0`
- `arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Terminate/1.0`
- `arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Reboot/1.0`
- `arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Recover/1.0`

**Autoscaling action:**

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id1)arn:aws:autoscaling:*region* :*account-id* :scalingPolicy:*policy-id* :autoScalingGroupName/*group-friendly-name* :policyName/*policy-friendly-name* ``

**Lambda actions:**

- Invoke the latest version of a Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id3)arn:aws:lambda:*region* :*account-id* :function:*function-name* ``
- Invoke a specific version of a Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id5)arn:aws:lambda:*region* :*account-id* :function:*function-name* :*version-number* ``
- Invoke a function by using an alias Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id7)arn:aws:lambda:*region* :*account-id* :function:*function-name* :*alias-name* ``

**SNS notification action:**

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id9)arn:aws:sns:*region* :*account-id* :*sns-topic-name* ``

**SSM integration actions:**

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id11)arn:aws:ssm:*region* :*account-id* :opsitem:*severity* #CATEGORY=*category-name* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id13)arn:aws:ssm-incidents::*account-id* :responseplan/*response-plan-name* ``

(string)

Syntax:

```
"string" "string" ...
```

`--alarm-actions` (list)

The actions to execute when this alarm transitions to the `ALARM` state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid values:

**EC2 actions:**

- `arn:aws:automate:*region* :ec2:stop`
- `arn:aws:automate:*region* :ec2:terminate`
- `arn:aws:automate:*region* :ec2:reboot`
- `arn:aws:automate:*region* :ec2:recover`
- `arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Stop/1.0`
- `arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Terminate/1.0`
- `arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Reboot/1.0`
- `arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Recover/1.0`

**Autoscaling action:**

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id15)arn:aws:autoscaling:*region* :*account-id* :scalingPolicy:*policy-id* :autoScalingGroupName/*group-friendly-name* :policyName/*policy-friendly-name* ``

**Lambda actions:**

- Invoke the latest version of a Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id17)arn:aws:lambda:*region* :*account-id* :function:*function-name* ``
- Invoke a specific version of a Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id19)arn:aws:lambda:*region* :*account-id* :function:*function-name* :*version-number* ``
- Invoke a function by using an alias Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id21)arn:aws:lambda:*region* :*account-id* :function:*function-name* :*alias-name* ``

**SNS notification action:**

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id23)arn:aws:sns:*region* :*account-id* :*sns-topic-name* ``

**SSM integration actions:**

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id25)arn:aws:ssm:*region* :*account-id* :opsitem:*severity* #CATEGORY=*category-name* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id27)arn:aws:ssm-incidents::*account-id* :responseplan/*response-plan-name* ``

**Start a Amazon Q Developer operational investigation**

[``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id29)arn:aws:aiops:*region* :*account-id* :investigation-group:*investigation-group-id* ``

(string)

Syntax:

```
"string" "string" ...
```

`--insufficient-data-actions` (list)

The actions to execute when this alarm transitions to the `INSUFFICIENT_DATA` state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid values:

**EC2 actions:**

- `arn:aws:automate:*region* :ec2:stop`
- `arn:aws:automate:*region* :ec2:terminate`
- `arn:aws:automate:*region* :ec2:reboot`
- `arn:aws:automate:*region* :ec2:recover`
- `arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Stop/1.0`
- `arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Terminate/1.0`
- `arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Reboot/1.0`
- `arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Recover/1.0`

**Autoscaling action:**

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id31)arn:aws:autoscaling:*region* :*account-id* :scalingPolicy:*policy-id* :autoScalingGroupName/*group-friendly-name* :policyName/*policy-friendly-name* ``

**Lambda actions:**

- Invoke the latest version of a Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id33)arn:aws:lambda:*region* :*account-id* :function:*function-name* ``
- Invoke a specific version of a Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id35)arn:aws:lambda:*region* :*account-id* :function:*function-name* :*version-number* ``
- Invoke a function by using an alias Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id37)arn:aws:lambda:*region* :*account-id* :function:*function-name* :*alias-name* ``

**SNS notification action:**

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id39)arn:aws:sns:*region* :*account-id* :*sns-topic-name* ``

**SSM integration actions:**

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id41)arn:aws:ssm:*region* :*account-id* :opsitem:*severity* #CATEGORY=*category-name* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html#id43)arn:aws:ssm-incidents::*account-id* :responseplan/*response-plan-name* ``

(string)

Syntax:

```
"string" "string" ...
```

`--metric-name` (string)

The name for the metric associated with the alarm. For each `PutMetricAlarm` operation, you must specify either `MetricName` or a `Metrics` array.

If you are creating an alarm based on a math expression, you cannot specify this parameter, or any of the `Namespace` , `Dimensions` , `Period` , `Unit` , `Statistic` , or `ExtendedStatistic` parameters. Instead, you specify all this information in the `Metrics` array.

`--namespace` (string)

The namespace for the metric associated specified in `MetricName` .

`--statistic` (string)

The statistic for the metric specified in `MetricName` , other than percentile. For percentile statistics, use `ExtendedStatistic` . When you call `PutMetricAlarm` and specify a `MetricName` , you must specify either `Statistic` or `ExtendedStatistic,` but not both.

Possible values:

- `SampleCount`
- `Average`
- `Sum`
- `Minimum`
- `Maximum`

`--extended-statistic` (string)

The extended statistic for the metric specified in `MetricName` . When you call `PutMetricAlarm` and specify a `MetricName` , you must specify either `Statistic` or `ExtendedStatistic` but not both.

If you specify `ExtendedStatistic` , the following are valid values:

- `p90`
- `tm90`
- `tc90`
- `ts90`
- `wm90`
- `IQM`
- `PR(*n* :*m* )` where n and m are values of the metric
- `TC(*X* %:*X* %)` where X is between 10 and 90 inclusive.
- `TM(*X* %:*X* %)` where X is between 10 and 90 inclusive.
- `TS(*X* %:*X* %)` where X is between 10 and 90 inclusive.
- `WM(*X* %:*X* %)` where X is between 10 and 90 inclusive.

For more information about these extended statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html) .

`--dimensions` (list)

The dimensions for the metric specified in `MetricName` .

(structure)

A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish `InstanceId` as a dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

Name -> (string)

The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (`:` ). ASCII control characters are not supported as part of dimension names.

Value -> (string)

The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

Shorthand Syntax:

```
Name=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Value": "string"
  }
  ...
]
```

`--period` (integer)

The length, in seconds, used each time the metric specified in `MetricName` is evaluated. Valid values are 10, 20, 30, and any multiple of 60.

`Period` is required for alarms based on static thresholds. If you are creating an alarm based on a metric math expression, you specify the period for each metric within the objects in the `Metrics` array.

Be sure to specify 10, 20, or 30 only for metrics that are stored by a `PutMetricData` call with a `StorageResolution` of 1. If you specify a period of 10, 20, or 30 for a metric that does not have sub-minute resolution, the alarm still attempts to gather data at the period rate that you specify. In this case, it does not receive data for the attempts that do not correspond to a one-minute data resolution, and the alarm might often lapse into INSUFFICENT_DATA status. Specifying 10, 20, or 30 also sets this alarm as a high-resolution alarm, which has a higher charge than other alarms. For more information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/) .

An alarmâs total current evaluation period can be no longer than seven days, so `Period` multiplied by `EvaluationPeriods` canât be more than 604,800 seconds. For alarms with a period of less than one hour (3,600 seconds), the total evaluation period canât be longer than one day (86,400 seconds).

`--unit` (string)

The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately. If you are creating an alarm based on a metric math expression, you can specify the unit for each metric (if needed) within the objects in the `Metrics` array.

If you donât specify `Unit` , CloudWatch retrieves all unit types that have been published for the metric and attempts to evaluate the alarm. Usually, metrics are published with only one unit, so the alarm works as intended.

However, if the metric is published with multiple types of units and you donât specify a unit, the alarmâs behavior is not defined and it behaves unpredictably.

We recommend omitting `Unit` so that you donât inadvertently specify an incorrect unit that is not published for this metric. Doing so causes the alarm to be stuck in the `INSUFFICIENT DATA` state.

Possible values:

- `Seconds`
- `Microseconds`
- `Milliseconds`
- `Bytes`
- `Kilobytes`
- `Megabytes`
- `Gigabytes`
- `Terabytes`
- `Bits`
- `Kilobits`
- `Megabits`
- `Gigabits`
- `Terabits`
- `Percent`
- `Count`
- `Bytes/Second`
- `Kilobytes/Second`
- `Megabytes/Second`
- `Gigabytes/Second`
- `Terabytes/Second`
- `Bits/Second`
- `Kilobits/Second`
- `Megabits/Second`
- `Gigabits/Second`
- `Terabits/Second`
- `Count/Second`
- `None`

`--evaluation-periods` (integer)

The number of periods over which data is compared to the specified threshold. If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an âM out of Nâ alarm, this value is the N.

`--datapoints-to-alarm` (integer)

The number of data points that must be breaching to trigger the alarm. This is used only if you are setting an âM out of Nâ alarm. In that case, this value is the M. For more information, see [Evaluating an Alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation) in the *Amazon CloudWatch User Guide* .

`--threshold` (double)

The value against which the specified statistic is compared.

This parameter is required for alarms based on static thresholds, but should not be used for alarms based on anomaly detection models.

`--comparison-operator` (string)

The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.

The values `LessThanLowerOrGreaterThanUpperThreshold` , `LessThanLowerThreshold` , and `GreaterThanUpperThreshold` are used only for alarms based on anomaly detection models.

Possible values:

- `GreaterThanOrEqualToThreshold`
- `GreaterThanThreshold`
- `LessThanThreshold`
- `LessThanOrEqualToThreshold`
- `LessThanLowerOrGreaterThanUpperThreshold`
- `LessThanLowerThreshold`
- `GreaterThanUpperThreshold`

`--treat-missing-data` (string)

Sets how this alarm is to handle missing data points. If `TreatMissingData` is omitted, the default behavior of `missing` is used. For more information, see [Configuring How CloudWatch Alarms Treats Missing Data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data) .

Valid Values: `breaching | notBreaching | ignore | missing`

### Note

Alarms that evaluate metrics in the `AWS/DynamoDB` namespace always `ignore` missing data even if you choose a different option for `TreatMissingData` . When an `AWS/DynamoDB` metric has missing data, alarms that evaluate that metric remain in their current state.

`--evaluate-low-sample-count-percentile` (string)

Used only for alarms based on percentiles. If you specify `ignore` , the alarm state does not change during periods with too few data points to be statistically significant. If you specify `evaluate` or omit this parameter, the alarm is always evaluated and possibly changes state no matter how many data points are available. For more information, see [Percentile-Based CloudWatch Alarms and Low Data Samples](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#percentiles-with-low-samples) .

Valid Values: `evaluate | ignore`

`--metrics` (list)

An array of `MetricDataQuery` structures that enable you to create an alarm based on the result of a metric math expression. For each `PutMetricAlarm` operation, you must specify either `MetricName` or a `Metrics` array.

Each item in the `Metrics` array either retrieves a metric or performs a math expression.

One item in the `Metrics` array is the expression that the alarm watches. You designate this expression by setting `ReturnData` to true for this object in the array. For more information, see [MetricDataQuery](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDataQuery.html) .

If you use the `Metrics` parameter, you cannot include the `Namespace` , `MetricName` , `Dimensions` , `Period` , `Unit` , `Statistic` , or `ExtendedStatistic` parameters of `PutMetricAlarm` in the same operation. Instead, you retrieve the metrics you are using in your math expression as part of the `Metrics` array.

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

JSON Syntax:

```
[
  {
    "Id": "string",
    "MetricStat": {
      "Metric": {
        "Namespace": "string",
        "MetricName": "string",
        "Dimensions": [
          {
            "Name": "string",
            "Value": "string"
          }
          ...
        ]
      },
      "Period": integer,
      "Stat": "string",
      "Unit": "Seconds"|"Microseconds"|"Milliseconds"|"Bytes"|"Kilobytes"|"Megabytes"|"Gigabytes"|"Terabytes"|"Bits"|"Kilobits"|"Megabits"|"Gigabits"|"Terabits"|"Percent"|"Count"|"Bytes/Second"|"Kilobytes/Second"|"Megabytes/Second"|"Gigabytes/Second"|"Terabytes/Second"|"Bits/Second"|"Kilobits/Second"|"Megabits/Second"|"Gigabits/Second"|"Terabits/Second"|"Count/Second"|"None"
    },
    "Expression": "string",
    "Label": "string",
    "ReturnData": true|false,
    "Period": integer,
    "AccountId": "string"
  }
  ...
]
```

`--tags` (list)

A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm. To be able to associate tags with the alarm when you create the alarm, you must have the `cloudwatch:TagResource` permission.

Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

If you are using this operation to update an existing alarm, any tags you specify in this parameter are ignored. To change the tags of an existing alarm, use [TagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html) or [UntagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html) .

To use this field to set tags for an alarm when you create it, you must be signed on with both the `cloudwatch:PutMetricAlarm` and `cloudwatch:TagResource` permissions.

(structure)

A key-value pair associated with a CloudWatch resource.

Key -> (string)

A string that you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.

Value -> (string)

The value for the specified tag key.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--threshold-metric-id` (string)

If this is an alarm based on an anomaly detection model, make this value match the ID of the `ANOMALY_DETECTION_BAND` function.

For an example of how to use this parameter, see the **Anomaly Detection Model Alarm** example on this page.

If your alarm uses this parameter, it cannot have Auto Scaling actions.

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

**To send an Amazon Simple Notification Service email message when CPU utilization exceeds 70 percent**

The following example uses the `put-metric-alarm` command to send an Amazon Simple Notification Service email message when CPU utilization exceeds 70 percent:

```
aws cloudwatch put-metric-alarm --alarm-name cpu-mon --alarm-description "Alarm when CPU exceeds 70 percent" --metric-name CPUUtilization --namespace AWS/EC2 --statistic Average --period 300 --threshold 70 --comparison-operator GreaterThanThreshold  --dimensions "Name=InstanceId,Value=i-12345678" --evaluation-periods 2 --alarm-actions arn:aws:sns:us-east-1:111122223333:MyTopic --unit Percent
```

This command returns to the prompt if successful. If an alarm with the same name already exists, it will be overwritten by the new alarm.

**To specify multiple dimensions**

The following example illustrates how to specify multiple dimensions. Each dimension is specified as a Name/Value pair, with a comma between the name and the value. Multiple dimensions are separated by a space:

```
aws cloudwatch put-metric-alarm --alarm-name "Default_Test_Alarm3" --alarm-description "The default example alarm" --namespace "CW EXAMPLE METRICS" --metric-name Default_Test --statistic Average --period 60 --evaluation-periods 3 --threshold 50 --comparison-operator GreaterThanOrEqualToThreshold --dimensions Name=key1,Value=value1 Name=key2,Value=value2
```

## Output

None