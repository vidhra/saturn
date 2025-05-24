# create-service-level-objectiveÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-signals/create-service-level-objective.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-signals/create-service-level-objective.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [application-signals](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-signals/index.html#cli-aws-application-signals) ]

# create-service-level-objective

## Description

Creates a service level objective (SLO), which can help you ensure that your critical business operations are meeting customer expectations. Use SLOs to set and track specific target levels for the reliability and availability of your applications and services. SLOs use service level indicators (SLIs) to calculate whether the application is performing at the level that you want.

Create an SLO to set a target for a service or operationâs availability or latency. CloudWatch measures this target frequently you can find whether it has been breached.

The target performance quality that is defined for an SLO is the *attainment goal* .

You can set SLO targets for your applications that are discovered by Application Signals, using critical metrics such as latency and availability. You can also set SLOs against any CloudWatch metric or math expression that produces a time series.

### Note

You canât create an SLO for a service operation that was discovered by Application Signals until after that operation has reported standard metrics to Application Signals.

When you create an SLO, you specify whether it is a *period-based SLO* or a *request-based SLO* . Each type of SLO has a different way of evaluating your applicationâs performance against its attainment goal.

- A *period-based SLO* uses defined *periods* of time within a specified total time interval. For each period of time, Application Signals determines whether the application met its goal. The attainment rate is calculated as the `number of good periods/number of total periods` . For example, for a period-based SLO, meeting an attainment goal of 99.9% means that within your interval, your application must meet its performance goal during at least 99.9% of the time periods.
- A *request-based SLO* doesnât use pre-defined periods of time. Instead, the SLO measures `number of good requests/number of total requests` during the interval. At any time, you can find the ratio of good requests to total requests for the interval up to the time stamp that you specify, and measure that ratio against the goal set in your SLO.

After you have created an SLO, you can retrieve error budget reports for it. An *error budget* is the amount of time or amount of requests that your application can be non-compliant with the SLOâs goal, and still have your application meet the goal.

- For a period-based SLO, the error budget starts at a number defined by the highest number of periods that can fail to meet the threshold, while still meeting the overall goal. The *remaining error budget* decreases with every failed period that is recorded. The error budget within one interval can never increase. For example, an SLO with a threshold that 99.95% of requests must be completed under 2000ms every month translates to an error budget of 21.9 minutes of downtime per month.
- For a request-based SLO, the remaining error budget is dynamic and can increase or decrease, depending on the ratio of good requests to total requests.

For more information about SLOs, see [Service level objectives (SLOs)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) .

When you perform a `CreateServiceLevelObjective` operation, Application Signals creates the *AWSServiceRoleForCloudWatchApplicationSignals* service-linked role, if it doesnât already exist in your account. This service- linked role has the following permissions:

- `xray:GetServiceGraph`
- `logs:StartQuery`
- `logs:GetQueryResults`
- `cloudwatch:GetMetricData`
- `cloudwatch:ListMetrics`
- `tag:GetResources`
- `autoscaling:DescribeAutoScalingGroups`

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/application-signals-2024-04-15/CreateServiceLevelObjective)

## Synopsis

```
create-service-level-objective
--name <value>
[--description <value>]
[--sli-config <value>]
[--request-based-sli-config <value>]
[--goal <value>]
[--tags <value>]
[--burn-rate-configurations <value>]
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

`--name` (string)

A name for this SLO.

`--description` (string)

An optional description for this SLO.

`--sli-config` (structure)

If this SLO is a period-based SLO, this structure defines the information about what performance metric this SLO will monitor.

You canât specify both `RequestBasedSliConfig` and `SliConfig` in the same operation.

SliMetricConfig -> (structure)

Use this structure to specify the metric to be used for the SLO.

KeyAttributes -> (map)

If this SLO is related to a metric collected by Application Signals, you must use this field to specify which service the SLO metric is related to. To do so, you must specify at least the `Type` , `Name` , and `Environment` attributes.

This is a string-to-string map. It can include the following fields.

- `Type` designates the type of object this is.
- `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service` , `RemoteService` , or `AWS::Service` .
- `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Environment` specifies the location where this object is hosted, or what it belongs to.

key -> (string)

value -> (string)

OperationName -> (string)

If the SLO is to monitor a specific operation of the service, use this field to specify the name of that operation.

MetricType -> (string)

If the SLO is to monitor either the `LATENCY` or `AVAILABILITY` metric that Application Signals collects, use this field to specify which of those metrics is used.

Statistic -> (string)

The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html) .

PeriodSeconds -> (integer)

The number of seconds to use as the period for SLO evaluation. Your applicationâs performance is compared to the SLI during each period. For each period, the application is determined to have either achieved or not achieved the necessary performance.

MetricDataQueries -> (list)

If this SLO monitors a CloudWatch metric or the result of a CloudWatch metric math expression, use this structure to specify that metric or expression.

(structure)

Use this structure to define a metric or metric math expression that you want to use as for a service level objective.

Each `MetricDataQuery` in the `MetricDataQueries` array specifies either a metric to retrieve, or a metric math expression to be performed on retrieved metrics. A single `MetricDataQueries` array can include as many as 20 `MetricDataQuery` structures in the array. The 20 structures can include as many as 10 structures that contain a `MetricStat` parameter to retrieve a metric, and as many as 10 structures that contain the `Expression` parameter to perform a math expression. Of those `Expression` structures, exactly one must have true as the value for `ReturnData` . The result of this expression used for the SLO.

For more information about metric math expressions, see [CloudWatchUse metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Id -> (string)

A short name used to tie this object to the results in the response. This `Id` must be unique within a `MetricDataQueries` array. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the metric math expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

MetricStat -> (structure)

A metric to be used directly for the SLO, or to be used in the math expression that will be used for the SLO.

Within one `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Metric -> (structure)

The metric to use as the service level indicator, including the metric name, namespace, and dimensions.

Namespace -> (string)

The namespace of the metric. For more information, see [Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace) .

MetricName -> (string)

The name of the metric to use.

Dimensions -> (list)

An array of one or more dimensions to use to define the metric that you want to use. For more information, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) .

(structure)

A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish `InstanceId` as a dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

Name -> (string)

The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (`:` ). ASCII control characters are not supported as part of dimension names.

Value -> (string)

The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

Period -> (integer)

The granularity, in seconds, to be used for the metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

Stat -> (string)

The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html) .

Unit -> (string)

If you omit `Unit` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

Expression -> (string)

This field can contain a metric math expression to be performed on the other metrics that you are retrieving within this `MetricDataQueries` structure.

A math expression can use the `Id` of the other metrics or queries to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions. For more information about metric math expressions, see [Metric Math Syntax and Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User Guide* .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Label -> (string)

A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If `Label` is omitted, CloudWatch generates a default.

You can put dynamic expressions into a label, so that it is more descriptive. For more information, see [Using Dynamic Labels](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html) .

ReturnData -> (boolean)

Use this only if you are using a metric math expression for the SLO. Specify `true` for `ReturnData` for only the one expression result to use as the alarm. For all other metrics and expressions in the same `CreateServiceLevelObjective` operation, specify `ReturnData` as `false` .

Period -> (integer)

The granularity, in seconds, of the returned data points for this metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

If the `StartTime` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

- Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
- Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
- Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

AccountId -> (string)

The ID of the account where this metric is located. If you are performing this operation in a monitoring account, use this to specify which source account to retrieve this metric from.

DependencyConfig -> (structure)

Identifies the dependency using the `DependencyKeyAttributes` and `DependencyOperationName` .

DependencyKeyAttributes -> (map)

This is a string-to-string map. It can include the following fields.

- `Type` designates the type of object this is.
- `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service` , `RemoteService` , or `AWS::Service` .
- `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Environment` specifies the location where this object is hosted, or what it belongs to.

key -> (string)

value -> (string)

DependencyOperationName -> (string)

The name of the called operation in the dependency.

MetricThreshold -> (double)

This parameter is used only when a request-based SLO tracks the `Latency` metric. Specify the threshold value that the observed `Latency` metric values are to be compared to.

ComparisonOperator -> (string)

The arithmetic operation to use when comparing the specified metric to the threshold.

JSON Syntax:

```
{
  "SliMetricConfig": {
    "KeyAttributes": {"string": "string"
      ...},
    "OperationName": "string",
    "MetricType": "LATENCY"|"AVAILABILITY",
    "Statistic": "string",
    "PeriodSeconds": integer,
    "MetricDataQueries": [
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
          "Unit": "Microseconds"|"Milliseconds"|"Seconds"|"Bytes"|"Kilobytes"|"Megabytes"|"Gigabytes"|"Terabytes"|"Bits"|"Kilobits"|"Megabits"|"Gigabits"|"Terabits"|"Percent"|"Count"|"Bytes/Second"|"Kilobytes/Second"|"Megabytes/Second"|"Gigabytes/Second"|"Terabytes/Second"|"Bits/Second"|"Kilobits/Second"|"Megabits/Second"|"Gigabits/Second"|"Terabits/Second"|"Count/Second"|"None"
        },
        "Expression": "string",
        "Label": "string",
        "ReturnData": true|false,
        "Period": integer,
        "AccountId": "string"
      }
      ...
    ],
    "DependencyConfig": {
      "DependencyKeyAttributes": {"string": "string"
        ...},
      "DependencyOperationName": "string"
    }
  },
  "MetricThreshold": double,
  "ComparisonOperator": "GreaterThanOrEqualTo"|"GreaterThan"|"LessThan"|"LessThanOrEqualTo"
}
```

`--request-based-sli-config` (structure)

If this SLO is a request-based SLO, this structure defines the information about what performance metric this SLO will monitor.

You canât specify both `RequestBasedSliConfig` and `SliConfig` in the same operation.

RequestBasedSliMetricConfig -> (structure)

Use this structure to specify the metric to be used for the SLO.

KeyAttributes -> (map)

If this SLO is related to a metric collected by Application Signals, you must use this field to specify which service the SLO metric is related to. To do so, you must specify at least the `Type` , `Name` , and `Environment` attributes.

This is a string-to-string map. It can include the following fields.

- `Type` designates the type of object this is.
- `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service` , `RemoteService` , or `AWS::Service` .
- `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Environment` specifies the location where this object is hosted, or what it belongs to.

key -> (string)

value -> (string)

OperationName -> (string)

If the SLO is to monitor a specific operation of the service, use this field to specify the name of that operation.

MetricType -> (string)

If the SLO is to monitor either the `LATENCY` or `AVAILABILITY` metric that Application Signals collects, use this field to specify which of those metrics is used.

TotalRequestCountMetric -> (list)

Use this structure to define the metric that you want to use as the âtotal requestsâ number for a request-based SLO. This result will be divided by the âgood requestâ or âbad requestâ value defined in `MonitoredRequestCountMetric` .

(structure)

Use this structure to define a metric or metric math expression that you want to use as for a service level objective.

Each `MetricDataQuery` in the `MetricDataQueries` array specifies either a metric to retrieve, or a metric math expression to be performed on retrieved metrics. A single `MetricDataQueries` array can include as many as 20 `MetricDataQuery` structures in the array. The 20 structures can include as many as 10 structures that contain a `MetricStat` parameter to retrieve a metric, and as many as 10 structures that contain the `Expression` parameter to perform a math expression. Of those `Expression` structures, exactly one must have true as the value for `ReturnData` . The result of this expression used for the SLO.

For more information about metric math expressions, see [CloudWatchUse metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Id -> (string)

A short name used to tie this object to the results in the response. This `Id` must be unique within a `MetricDataQueries` array. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the metric math expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

MetricStat -> (structure)

A metric to be used directly for the SLO, or to be used in the math expression that will be used for the SLO.

Within one `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Metric -> (structure)

The metric to use as the service level indicator, including the metric name, namespace, and dimensions.

Namespace -> (string)

The namespace of the metric. For more information, see [Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace) .

MetricName -> (string)

The name of the metric to use.

Dimensions -> (list)

An array of one or more dimensions to use to define the metric that you want to use. For more information, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) .

(structure)

A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish `InstanceId` as a dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

Name -> (string)

The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (`:` ). ASCII control characters are not supported as part of dimension names.

Value -> (string)

The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

Period -> (integer)

The granularity, in seconds, to be used for the metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

Stat -> (string)

The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html) .

Unit -> (string)

If you omit `Unit` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

Expression -> (string)

This field can contain a metric math expression to be performed on the other metrics that you are retrieving within this `MetricDataQueries` structure.

A math expression can use the `Id` of the other metrics or queries to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions. For more information about metric math expressions, see [Metric Math Syntax and Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User Guide* .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Label -> (string)

A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If `Label` is omitted, CloudWatch generates a default.

You can put dynamic expressions into a label, so that it is more descriptive. For more information, see [Using Dynamic Labels](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html) .

ReturnData -> (boolean)

Use this only if you are using a metric math expression for the SLO. Specify `true` for `ReturnData` for only the one expression result to use as the alarm. For all other metrics and expressions in the same `CreateServiceLevelObjective` operation, specify `ReturnData` as `false` .

Period -> (integer)

The granularity, in seconds, of the returned data points for this metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

If the `StartTime` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

- Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
- Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
- Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

AccountId -> (string)

The ID of the account where this metric is located. If you are performing this operation in a monitoring account, use this to specify which source account to retrieve this metric from.

MonitoredRequestCountMetric -> (tagged union structure)

Use this structure to define the metric that you want to use as the âgood requestâ or âbad requestâ value for a request-based SLO. This value observed for the metric defined in `TotalRequestCountMetric` will be divided by the number found for `MonitoredRequestCountMetric` to determine the percentage of successful requests that this SLO tracks.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `GoodCountMetric`, `BadCountMetric`.

GoodCountMetric -> (list)

If you want to count âgood requestsâ to determine the percentage of successful requests for this request-based SLO, specify the metric to use as âgood requestsâ in this structure.

(structure)

Use this structure to define a metric or metric math expression that you want to use as for a service level objective.

Each `MetricDataQuery` in the `MetricDataQueries` array specifies either a metric to retrieve, or a metric math expression to be performed on retrieved metrics. A single `MetricDataQueries` array can include as many as 20 `MetricDataQuery` structures in the array. The 20 structures can include as many as 10 structures that contain a `MetricStat` parameter to retrieve a metric, and as many as 10 structures that contain the `Expression` parameter to perform a math expression. Of those `Expression` structures, exactly one must have true as the value for `ReturnData` . The result of this expression used for the SLO.

For more information about metric math expressions, see [CloudWatchUse metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Id -> (string)

A short name used to tie this object to the results in the response. This `Id` must be unique within a `MetricDataQueries` array. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the metric math expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

MetricStat -> (structure)

A metric to be used directly for the SLO, or to be used in the math expression that will be used for the SLO.

Within one `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Metric -> (structure)

The metric to use as the service level indicator, including the metric name, namespace, and dimensions.

Namespace -> (string)

The namespace of the metric. For more information, see [Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace) .

MetricName -> (string)

The name of the metric to use.

Dimensions -> (list)

An array of one or more dimensions to use to define the metric that you want to use. For more information, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) .

(structure)

A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish `InstanceId` as a dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

Name -> (string)

The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (`:` ). ASCII control characters are not supported as part of dimension names.

Value -> (string)

The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

Period -> (integer)

The granularity, in seconds, to be used for the metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

Stat -> (string)

The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html) .

Unit -> (string)

If you omit `Unit` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

Expression -> (string)

This field can contain a metric math expression to be performed on the other metrics that you are retrieving within this `MetricDataQueries` structure.

A math expression can use the `Id` of the other metrics or queries to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions. For more information about metric math expressions, see [Metric Math Syntax and Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User Guide* .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Label -> (string)

A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If `Label` is omitted, CloudWatch generates a default.

You can put dynamic expressions into a label, so that it is more descriptive. For more information, see [Using Dynamic Labels](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html) .

ReturnData -> (boolean)

Use this only if you are using a metric math expression for the SLO. Specify `true` for `ReturnData` for only the one expression result to use as the alarm. For all other metrics and expressions in the same `CreateServiceLevelObjective` operation, specify `ReturnData` as `false` .

Period -> (integer)

The granularity, in seconds, of the returned data points for this metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

If the `StartTime` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

- Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
- Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
- Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

AccountId -> (string)

The ID of the account where this metric is located. If you are performing this operation in a monitoring account, use this to specify which source account to retrieve this metric from.

BadCountMetric -> (list)

If you want to count âbad requestsâ to determine the percentage of successful requests for this request-based SLO, specify the metric to use as âbad requestsâ in this structure.

(structure)

Use this structure to define a metric or metric math expression that you want to use as for a service level objective.

Each `MetricDataQuery` in the `MetricDataQueries` array specifies either a metric to retrieve, or a metric math expression to be performed on retrieved metrics. A single `MetricDataQueries` array can include as many as 20 `MetricDataQuery` structures in the array. The 20 structures can include as many as 10 structures that contain a `MetricStat` parameter to retrieve a metric, and as many as 10 structures that contain the `Expression` parameter to perform a math expression. Of those `Expression` structures, exactly one must have true as the value for `ReturnData` . The result of this expression used for the SLO.

For more information about metric math expressions, see [CloudWatchUse metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Id -> (string)

A short name used to tie this object to the results in the response. This `Id` must be unique within a `MetricDataQueries` array. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the metric math expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

MetricStat -> (structure)

A metric to be used directly for the SLO, or to be used in the math expression that will be used for the SLO.

Within one `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Metric -> (structure)

The metric to use as the service level indicator, including the metric name, namespace, and dimensions.

Namespace -> (string)

The namespace of the metric. For more information, see [Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace) .

MetricName -> (string)

The name of the metric to use.

Dimensions -> (list)

An array of one or more dimensions to use to define the metric that you want to use. For more information, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) .

(structure)

A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish `InstanceId` as a dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

Name -> (string)

The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (`:` ). ASCII control characters are not supported as part of dimension names.

Value -> (string)

The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

Period -> (integer)

The granularity, in seconds, to be used for the metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

Stat -> (string)

The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html) .

Unit -> (string)

If you omit `Unit` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

Expression -> (string)

This field can contain a metric math expression to be performed on the other metrics that you are retrieving within this `MetricDataQueries` structure.

A math expression can use the `Id` of the other metrics or queries to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions. For more information about metric math expressions, see [Metric Math Syntax and Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User Guide* .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Label -> (string)

A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If `Label` is omitted, CloudWatch generates a default.

You can put dynamic expressions into a label, so that it is more descriptive. For more information, see [Using Dynamic Labels](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html) .

ReturnData -> (boolean)

Use this only if you are using a metric math expression for the SLO. Specify `true` for `ReturnData` for only the one expression result to use as the alarm. For all other metrics and expressions in the same `CreateServiceLevelObjective` operation, specify `ReturnData` as `false` .

Period -> (integer)

The granularity, in seconds, of the returned data points for this metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

If the `StartTime` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

- Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
- Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
- Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

AccountId -> (string)

The ID of the account where this metric is located. If you are performing this operation in a monitoring account, use this to specify which source account to retrieve this metric from.

DependencyConfig -> (structure)

Identifies the dependency using the `DependencyKeyAttributes` and `DependencyOperationName` .

DependencyKeyAttributes -> (map)

This is a string-to-string map. It can include the following fields.

- `Type` designates the type of object this is.
- `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service` , `RemoteService` , or `AWS::Service` .
- `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Environment` specifies the location where this object is hosted, or what it belongs to.

key -> (string)

value -> (string)

DependencyOperationName -> (string)

The name of the called operation in the dependency.

MetricThreshold -> (double)

The value that the SLI metric is compared to. This parameter is required if this SLO is tracking the `Latency` metric.

ComparisonOperator -> (string)

The arithmetic operation to use when comparing the specified metric to the threshold. This parameter is required if this SLO is tracking the `Latency` metric.

JSON Syntax:

```
{
  "RequestBasedSliMetricConfig": {
    "KeyAttributes": {"string": "string"
      ...},
    "OperationName": "string",
    "MetricType": "LATENCY"|"AVAILABILITY",
    "TotalRequestCountMetric": [
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
          "Unit": "Microseconds"|"Milliseconds"|"Seconds"|"Bytes"|"Kilobytes"|"Megabytes"|"Gigabytes"|"Terabytes"|"Bits"|"Kilobits"|"Megabits"|"Gigabits"|"Terabits"|"Percent"|"Count"|"Bytes/Second"|"Kilobytes/Second"|"Megabytes/Second"|"Gigabytes/Second"|"Terabytes/Second"|"Bits/Second"|"Kilobits/Second"|"Megabits/Second"|"Gigabits/Second"|"Terabits/Second"|"Count/Second"|"None"
        },
        "Expression": "string",
        "Label": "string",
        "ReturnData": true|false,
        "Period": integer,
        "AccountId": "string"
      }
      ...
    ],
    "MonitoredRequestCountMetric": {
      "GoodCountMetric": [
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
            "Unit": "Microseconds"|"Milliseconds"|"Seconds"|"Bytes"|"Kilobytes"|"Megabytes"|"Gigabytes"|"Terabytes"|"Bits"|"Kilobits"|"Megabits"|"Gigabits"|"Terabits"|"Percent"|"Count"|"Bytes/Second"|"Kilobytes/Second"|"Megabytes/Second"|"Gigabytes/Second"|"Terabytes/Second"|"Bits/Second"|"Kilobits/Second"|"Megabits/Second"|"Gigabits/Second"|"Terabits/Second"|"Count/Second"|"None"
          },
          "Expression": "string",
          "Label": "string",
          "ReturnData": true|false,
          "Period": integer,
          "AccountId": "string"
        }
        ...
      ],
      "BadCountMetric": [
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
            "Unit": "Microseconds"|"Milliseconds"|"Seconds"|"Bytes"|"Kilobytes"|"Megabytes"|"Gigabytes"|"Terabytes"|"Bits"|"Kilobits"|"Megabits"|"Gigabits"|"Terabits"|"Percent"|"Count"|"Bytes/Second"|"Kilobytes/Second"|"Megabytes/Second"|"Gigabytes/Second"|"Terabytes/Second"|"Bits/Second"|"Kilobits/Second"|"Megabits/Second"|"Gigabits/Second"|"Terabits/Second"|"Count/Second"|"None"
          },
          "Expression": "string",
          "Label": "string",
          "ReturnData": true|false,
          "Period": integer,
          "AccountId": "string"
        }
        ...
      ]
    },
    "DependencyConfig": {
      "DependencyKeyAttributes": {"string": "string"
        ...},
      "DependencyOperationName": "string"
    }
  },
  "MetricThreshold": double,
  "ComparisonOperator": "GreaterThanOrEqualTo"|"GreaterThan"|"LessThan"|"LessThanOrEqualTo"
}
```

`--goal` (structure)

This structure contains the attributes that determine the goal of the SLO.

Interval -> (tagged union structure)

The time period used to evaluate the SLO. It can be either a calendar interval or rolling interval.

If you omit this parameter, a rolling interval of 7 days is used.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `RollingInterval`, `CalendarInterval`.

RollingInterval -> (structure)

If the interval is a rolling interval, this structure contains the interval specifications.

DurationUnit -> (string)

Specifies the rolling interval unit.

Duration -> (integer)

Specifies the duration of each rolling interval. For example, if `Duration` is `7` and `DurationUnit` is `DAY` , each rolling interval is seven days.

CalendarInterval -> (structure)

If the interval is a calendar interval, this structure contains the interval specifications.

StartTime -> (timestamp)

The date and time when you want the first interval to start. Be sure to choose a time that configures the intervals the way that you want. For example, if you want weekly intervals starting on Mondays at 6 a.m., be sure to specify a start time that is a Monday at 6 a.m.

When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`

As soon as one calendar interval ends, another automatically begins.

DurationUnit -> (string)

Specifies the calendar interval unit.

Duration -> (integer)

Specifies the duration of each calendar interval. For example, if `Duration` is `1` and `DurationUnit` is `MONTH` , each interval is one month, aligned with the calendar.

AttainmentGoal -> (double)

The threshold that determines if the goal is being met.

If this is a period-based SLO, the attainment goal is the percentage of good periods that meet the threshold requirements to the total periods within the interval. For example, an attainment goal of 99.9% means that within your interval, you are targeting 99.9% of the periods to be in healthy state.

If this is a request-based SLO, the attainment goal is the percentage of requests that must be successful to meet the attainment goal.

If you omit this parameter, 99 is used to represent 99% as the attainment goal.

WarningThreshold -> (double)

The percentage of remaining budget over total budget that you want to get warnings for. If you omit this parameter, the default of 50.0 is used.

Shorthand Syntax:

```
Interval={RollingInterval={DurationUnit=string,Duration=integer},CalendarInterval={StartTime=timestamp,DurationUnit=string,Duration=integer}},AttainmentGoal=double,WarningThreshold=double
```

JSON Syntax:

```
{
  "Interval": {
    "RollingInterval": {
      "DurationUnit": "MINUTE"|"HOUR"|"DAY"|"MONTH",
      "Duration": integer
    },
    "CalendarInterval": {
      "StartTime": timestamp,
      "DurationUnit": "MINUTE"|"HOUR"|"DAY"|"MONTH",
      "Duration": integer
    }
  },
  "AttainmentGoal": double,
  "WarningThreshold": double
}
```

`--tags` (list)

A list of key-value pairs to associate with the SLO. You can associate as many as 50 tags with an SLO. To be able to associate tags with the SLO when you create the SLO, you must have the `cloudwatch:TagResource` permission.

Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

(structure)

A key-value pair associated with a resource. Tags can help you organize and categorize your resources.

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

`--burn-rate-configurations` (list)

Use this array to create *burn rates* for this SLO. Each burn rate is a metric that indicates how fast the service is consuming the error budget, relative to the attainment goal of the SLO.

(structure)

This object defines the length of the look-back window used to calculate one burn rate metric for this SLO. The burn rate measures how fast the service is consuming the error budget, relative to the attainment goal of the SLO. A burn rate of exactly 1 indicates that the SLO goal will be met exactly.

For example, if you specify 60 as the number of minutes in the look-back window, the burn rate is calculated as the following:

*burn rate = error rate over the look-back window / (100% - attainment goal percentage)*

For more information about burn rates, see [Calculate burn rates](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html#CloudWatch-ServiceLevelObjectives-burn) .

LookBackWindowMinutes -> (integer)

The number of minutes to use as the look-back window.

Shorthand Syntax:

```
LookBackWindowMinutes=integer ...
```

JSON Syntax:

```
[
  {
    "LookBackWindowMinutes": integer
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

Slo -> (structure)

A structure that contains information about the SLO that you just created.

Arn -> (string)

The ARN of this SLO.

Name -> (string)

The name of this SLO.

Description -> (string)

The description that you created for this SLO.

CreatedTime -> (timestamp)

The date and time that this SLO was created. When used in a raw HTTP Query API, it is formatted as `yyyy-MM-dd'T'HH:mm:ss` . For example, `2019-07-01T23:59:59` .

LastUpdatedTime -> (timestamp)

The time that this SLO was most recently updated. When used in a raw HTTP Query API, it is formatted as `yyyy-MM-dd'T'HH:mm:ss` . For example, `2019-07-01T23:59:59` .

Sli -> (structure)

A structure containing information about the performance metric that this SLO monitors, if this is a period-based SLO.

SliMetric -> (structure)

A structure that contains information about the metric that the SLO monitors.

KeyAttributes -> (map)

This is a string-to-string map that contains information about the type of object that this SLO is related to. It can include the following fields.

- `Type` designates the type of object that this SLO is related to.
- `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service` , `RemoteService` , or `AWS::Service` .
- `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Environment` specifies the location where this object is hosted, or what it belongs to.

key -> (string)

value -> (string)

OperationName -> (string)

If the SLO monitors a specific operation of the service, this field displays that operation name.

MetricType -> (string)

If the SLO monitors either the `LATENCY` or `AVAILABILITY` metric that Application Signals collects, this field displays which of those metrics is used.

MetricDataQueries -> (list)

If this SLO monitors a CloudWatch metric or the result of a CloudWatch metric math expression, this structure includes the information about that metric or expression.

(structure)

Use this structure to define a metric or metric math expression that you want to use as for a service level objective.

Each `MetricDataQuery` in the `MetricDataQueries` array specifies either a metric to retrieve, or a metric math expression to be performed on retrieved metrics. A single `MetricDataQueries` array can include as many as 20 `MetricDataQuery` structures in the array. The 20 structures can include as many as 10 structures that contain a `MetricStat` parameter to retrieve a metric, and as many as 10 structures that contain the `Expression` parameter to perform a math expression. Of those `Expression` structures, exactly one must have true as the value for `ReturnData` . The result of this expression used for the SLO.

For more information about metric math expressions, see [CloudWatchUse metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Id -> (string)

A short name used to tie this object to the results in the response. This `Id` must be unique within a `MetricDataQueries` array. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the metric math expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

MetricStat -> (structure)

A metric to be used directly for the SLO, or to be used in the math expression that will be used for the SLO.

Within one `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Metric -> (structure)

The metric to use as the service level indicator, including the metric name, namespace, and dimensions.

Namespace -> (string)

The namespace of the metric. For more information, see [Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace) .

MetricName -> (string)

The name of the metric to use.

Dimensions -> (list)

An array of one or more dimensions to use to define the metric that you want to use. For more information, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) .

(structure)

A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish `InstanceId` as a dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

Name -> (string)

The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (`:` ). ASCII control characters are not supported as part of dimension names.

Value -> (string)

The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

Period -> (integer)

The granularity, in seconds, to be used for the metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

Stat -> (string)

The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html) .

Unit -> (string)

If you omit `Unit` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

Expression -> (string)

This field can contain a metric math expression to be performed on the other metrics that you are retrieving within this `MetricDataQueries` structure.

A math expression can use the `Id` of the other metrics or queries to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions. For more information about metric math expressions, see [Metric Math Syntax and Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User Guide* .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Label -> (string)

A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If `Label` is omitted, CloudWatch generates a default.

You can put dynamic expressions into a label, so that it is more descriptive. For more information, see [Using Dynamic Labels](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html) .

ReturnData -> (boolean)

Use this only if you are using a metric math expression for the SLO. Specify `true` for `ReturnData` for only the one expression result to use as the alarm. For all other metrics and expressions in the same `CreateServiceLevelObjective` operation, specify `ReturnData` as `false` .

Period -> (integer)

The granularity, in seconds, of the returned data points for this metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

If the `StartTime` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

- Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
- Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
- Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

AccountId -> (string)

The ID of the account where this metric is located. If you are performing this operation in a monitoring account, use this to specify which source account to retrieve this metric from.

DependencyConfig -> (structure)

Identifies the dependency using the `DependencyKeyAttributes` and `DependencyOperationName` .

DependencyKeyAttributes -> (map)

This is a string-to-string map. It can include the following fields.

- `Type` designates the type of object this is.
- `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service` , `RemoteService` , or `AWS::Service` .
- `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Environment` specifies the location where this object is hosted, or what it belongs to.

key -> (string)

value -> (string)

DependencyOperationName -> (string)

The name of the called operation in the dependency.

MetricThreshold -> (double)

The value that the SLI metric is compared to.

ComparisonOperator -> (string)

The arithmetic operation used when comparing the specified metric to the threshold.

RequestBasedSli -> (structure)

A structure containing information about the performance metric that this SLO monitors, if this is a request-based SLO.

RequestBasedSliMetric -> (structure)

A structure that contains information about the metric that the SLO monitors.

KeyAttributes -> (map)

This is a string-to-string map that contains information about the type of object that this SLO is related to. It can include the following fields.

- `Type` designates the type of object that this SLO is related to.
- `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service` , `RemoteService` , or `AWS::Service` .
- `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Environment` specifies the location where this object is hosted, or what it belongs to.

key -> (string)

value -> (string)

OperationName -> (string)

If the SLO monitors a specific operation of the service, this field displays that operation name.

MetricType -> (string)

If the SLO monitors either the `LATENCY` or `AVAILABILITY` metric that Application Signals collects, this field displays which of those metrics is used.

TotalRequestCountMetric -> (list)

This structure defines the metric that is used as the âtotal requestsâ number for a request-based SLO. The number observed for this metric is divided by the number of âgood requestsâ or âbad requestsâ that is observed for the metric defined in `MonitoredRequestCountMetric` .

(structure)

Use this structure to define a metric or metric math expression that you want to use as for a service level objective.

Each `MetricDataQuery` in the `MetricDataQueries` array specifies either a metric to retrieve, or a metric math expression to be performed on retrieved metrics. A single `MetricDataQueries` array can include as many as 20 `MetricDataQuery` structures in the array. The 20 structures can include as many as 10 structures that contain a `MetricStat` parameter to retrieve a metric, and as many as 10 structures that contain the `Expression` parameter to perform a math expression. Of those `Expression` structures, exactly one must have true as the value for `ReturnData` . The result of this expression used for the SLO.

For more information about metric math expressions, see [CloudWatchUse metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Id -> (string)

A short name used to tie this object to the results in the response. This `Id` must be unique within a `MetricDataQueries` array. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the metric math expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

MetricStat -> (structure)

A metric to be used directly for the SLO, or to be used in the math expression that will be used for the SLO.

Within one `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Metric -> (structure)

The metric to use as the service level indicator, including the metric name, namespace, and dimensions.

Namespace -> (string)

The namespace of the metric. For more information, see [Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace) .

MetricName -> (string)

The name of the metric to use.

Dimensions -> (list)

An array of one or more dimensions to use to define the metric that you want to use. For more information, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) .

(structure)

A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish `InstanceId` as a dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

Name -> (string)

The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (`:` ). ASCII control characters are not supported as part of dimension names.

Value -> (string)

The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

Period -> (integer)

The granularity, in seconds, to be used for the metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

Stat -> (string)

The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html) .

Unit -> (string)

If you omit `Unit` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

Expression -> (string)

This field can contain a metric math expression to be performed on the other metrics that you are retrieving within this `MetricDataQueries` structure.

A math expression can use the `Id` of the other metrics or queries to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions. For more information about metric math expressions, see [Metric Math Syntax and Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User Guide* .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Label -> (string)

A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If `Label` is omitted, CloudWatch generates a default.

You can put dynamic expressions into a label, so that it is more descriptive. For more information, see [Using Dynamic Labels](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html) .

ReturnData -> (boolean)

Use this only if you are using a metric math expression for the SLO. Specify `true` for `ReturnData` for only the one expression result to use as the alarm. For all other metrics and expressions in the same `CreateServiceLevelObjective` operation, specify `ReturnData` as `false` .

Period -> (integer)

The granularity, in seconds, of the returned data points for this metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

If the `StartTime` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

- Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
- Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
- Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

AccountId -> (string)

The ID of the account where this metric is located. If you are performing this operation in a monitoring account, use this to specify which source account to retrieve this metric from.

MonitoredRequestCountMetric -> (tagged union structure)

This structure defines the metric that is used as the âgood requestâ or âbad requestâ value for a request-based SLO. This value observed for the metric defined in `TotalRequestCountMetric` is divided by the number found for `MonitoredRequestCountMetric` to determine the percentage of successful requests that this SLO tracks.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `GoodCountMetric`, `BadCountMetric`.

GoodCountMetric -> (list)

If you want to count âgood requestsâ to determine the percentage of successful requests for this request-based SLO, specify the metric to use as âgood requestsâ in this structure.

(structure)

Use this structure to define a metric or metric math expression that you want to use as for a service level objective.

Each `MetricDataQuery` in the `MetricDataQueries` array specifies either a metric to retrieve, or a metric math expression to be performed on retrieved metrics. A single `MetricDataQueries` array can include as many as 20 `MetricDataQuery` structures in the array. The 20 structures can include as many as 10 structures that contain a `MetricStat` parameter to retrieve a metric, and as many as 10 structures that contain the `Expression` parameter to perform a math expression. Of those `Expression` structures, exactly one must have true as the value for `ReturnData` . The result of this expression used for the SLO.

For more information about metric math expressions, see [CloudWatchUse metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Id -> (string)

A short name used to tie this object to the results in the response. This `Id` must be unique within a `MetricDataQueries` array. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the metric math expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

MetricStat -> (structure)

A metric to be used directly for the SLO, or to be used in the math expression that will be used for the SLO.

Within one `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Metric -> (structure)

The metric to use as the service level indicator, including the metric name, namespace, and dimensions.

Namespace -> (string)

The namespace of the metric. For more information, see [Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace) .

MetricName -> (string)

The name of the metric to use.

Dimensions -> (list)

An array of one or more dimensions to use to define the metric that you want to use. For more information, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) .

(structure)

A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish `InstanceId` as a dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

Name -> (string)

The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (`:` ). ASCII control characters are not supported as part of dimension names.

Value -> (string)

The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

Period -> (integer)

The granularity, in seconds, to be used for the metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

Stat -> (string)

The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html) .

Unit -> (string)

If you omit `Unit` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

Expression -> (string)

This field can contain a metric math expression to be performed on the other metrics that you are retrieving within this `MetricDataQueries` structure.

A math expression can use the `Id` of the other metrics or queries to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions. For more information about metric math expressions, see [Metric Math Syntax and Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User Guide* .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Label -> (string)

A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If `Label` is omitted, CloudWatch generates a default.

You can put dynamic expressions into a label, so that it is more descriptive. For more information, see [Using Dynamic Labels](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html) .

ReturnData -> (boolean)

Use this only if you are using a metric math expression for the SLO. Specify `true` for `ReturnData` for only the one expression result to use as the alarm. For all other metrics and expressions in the same `CreateServiceLevelObjective` operation, specify `ReturnData` as `false` .

Period -> (integer)

The granularity, in seconds, of the returned data points for this metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

If the `StartTime` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

- Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
- Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
- Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

AccountId -> (string)

The ID of the account where this metric is located. If you are performing this operation in a monitoring account, use this to specify which source account to retrieve this metric from.

BadCountMetric -> (list)

If you want to count âbad requestsâ to determine the percentage of successful requests for this request-based SLO, specify the metric to use as âbad requestsâ in this structure.

(structure)

Use this structure to define a metric or metric math expression that you want to use as for a service level objective.

Each `MetricDataQuery` in the `MetricDataQueries` array specifies either a metric to retrieve, or a metric math expression to be performed on retrieved metrics. A single `MetricDataQueries` array can include as many as 20 `MetricDataQuery` structures in the array. The 20 structures can include as many as 10 structures that contain a `MetricStat` parameter to retrieve a metric, and as many as 10 structures that contain the `Expression` parameter to perform a math expression. Of those `Expression` structures, exactly one must have true as the value for `ReturnData` . The result of this expression used for the SLO.

For more information about metric math expressions, see [CloudWatchUse metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Id -> (string)

A short name used to tie this object to the results in the response. This `Id` must be unique within a `MetricDataQueries` array. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the metric math expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

MetricStat -> (structure)

A metric to be used directly for the SLO, or to be used in the math expression that will be used for the SLO.

Within one `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Metric -> (structure)

The metric to use as the service level indicator, including the metric name, namespace, and dimensions.

Namespace -> (string)

The namespace of the metric. For more information, see [Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace) .

MetricName -> (string)

The name of the metric to use.

Dimensions -> (list)

An array of one or more dimensions to use to define the metric that you want to use. For more information, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) .

(structure)

A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish `InstanceId` as a dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

Name -> (string)

The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (`:` ). ASCII control characters are not supported as part of dimension names.

Value -> (string)

The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

Period -> (integer)

The granularity, in seconds, to be used for the metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

Stat -> (string)

The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html) .

Unit -> (string)

If you omit `Unit` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

Expression -> (string)

This field can contain a metric math expression to be performed on the other metrics that you are retrieving within this `MetricDataQueries` structure.

A math expression can use the `Id` of the other metrics or queries to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions. For more information about metric math expressions, see [Metric Math Syntax and Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User Guide* .

Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` but not both.

Label -> (string)

A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If `Label` is omitted, CloudWatch generates a default.

You can put dynamic expressions into a label, so that it is more descriptive. For more information, see [Using Dynamic Labels](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html) .

ReturnData -> (boolean)

Use this only if you are using a metric math expression for the SLO. Specify `true` for `ReturnData` for only the one expression result to use as the alarm. For all other metrics and expressions in the same `CreateServiceLevelObjective` operation, specify `ReturnData` as `false` .

Period -> (integer)

The granularity, in seconds, of the returned data points for this metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.

If the `StartTime` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

- Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
- Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
- Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

AccountId -> (string)

The ID of the account where this metric is located. If you are performing this operation in a monitoring account, use this to specify which source account to retrieve this metric from.

DependencyConfig -> (structure)

Identifies the dependency using the `DependencyKeyAttributes` and `DependencyOperationName` .

DependencyKeyAttributes -> (map)

This is a string-to-string map. It can include the following fields.

- `Type` designates the type of object this is.
- `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service` , `RemoteService` , or `AWS::Service` .
- `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Environment` specifies the location where this object is hosted, or what it belongs to.

key -> (string)

value -> (string)

DependencyOperationName -> (string)

The name of the called operation in the dependency.

MetricThreshold -> (double)

This value is the threshold that the observed metric values of the SLI metric are compared to.

ComparisonOperator -> (string)

The arithmetic operation used when comparing the specified metric to the threshold.

EvaluationType -> (string)

Displays whether this is a period-based SLO or a request-based SLO.

Goal -> (structure)

This structure contains the attributes that determine the goal of an SLO. This includes the time period for evaluation and the attainment threshold.

Interval -> (tagged union structure)

The time period used to evaluate the SLO. It can be either a calendar interval or rolling interval.

If you omit this parameter, a rolling interval of 7 days is used.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `RollingInterval`, `CalendarInterval`.

RollingInterval -> (structure)

If the interval is a rolling interval, this structure contains the interval specifications.

DurationUnit -> (string)

Specifies the rolling interval unit.

Duration -> (integer)

Specifies the duration of each rolling interval. For example, if `Duration` is `7` and `DurationUnit` is `DAY` , each rolling interval is seven days.

CalendarInterval -> (structure)

If the interval is a calendar interval, this structure contains the interval specifications.

StartTime -> (timestamp)

The date and time when you want the first interval to start. Be sure to choose a time that configures the intervals the way that you want. For example, if you want weekly intervals starting on Mondays at 6 a.m., be sure to specify a start time that is a Monday at 6 a.m.

When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`

As soon as one calendar interval ends, another automatically begins.

DurationUnit -> (string)

Specifies the calendar interval unit.

Duration -> (integer)

Specifies the duration of each calendar interval. For example, if `Duration` is `1` and `DurationUnit` is `MONTH` , each interval is one month, aligned with the calendar.

AttainmentGoal -> (double)

The threshold that determines if the goal is being met.

If this is a period-based SLO, the attainment goal is the percentage of good periods that meet the threshold requirements to the total periods within the interval. For example, an attainment goal of 99.9% means that within your interval, you are targeting 99.9% of the periods to be in healthy state.

If this is a request-based SLO, the attainment goal is the percentage of requests that must be successful to meet the attainment goal.

If you omit this parameter, 99 is used to represent 99% as the attainment goal.

WarningThreshold -> (double)

The percentage of remaining budget over total budget that you want to get warnings for. If you omit this parameter, the default of 50.0 is used.

BurnRateConfigurations -> (list)

Each object in this array defines the length of the look-back window used to calculate one burn rate metric for this SLO. The burn rate measures how fast the service is consuming the error budget, relative to the attainment goal of the SLO.

(structure)

This object defines the length of the look-back window used to calculate one burn rate metric for this SLO. The burn rate measures how fast the service is consuming the error budget, relative to the attainment goal of the SLO. A burn rate of exactly 1 indicates that the SLO goal will be met exactly.

For example, if you specify 60 as the number of minutes in the look-back window, the burn rate is calculated as the following:

*burn rate = error rate over the look-back window / (100% - attainment goal percentage)*

For more information about burn rates, see [Calculate burn rates](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html#CloudWatch-ServiceLevelObjectives-burn) .

LookBackWindowMinutes -> (integer)

The number of minutes to use as the look-back window.

MetricSourceType -> (string)

Displays the SLI metric source type for this SLO. Supported types are:

- Service operation
- Service dependency
- CloudWatch metric