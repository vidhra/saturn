# get-predictive-scaling-forecastÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/get-predictive-scaling-forecast.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/get-predictive-scaling-forecast.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [application-autoscaling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/index.html#cli-aws-application-autoscaling) ]

# get-predictive-scaling-forecast

## Description

Retrieves the forecast data for a predictive scaling policy.

Load forecasts are predictions of the hourly load values using historical load data from CloudWatch and an analysis of historical trends. Capacity forecasts are represented as predicted values for the minimum capacity that is needed on an hourly basis, based on the hourly load forecast.

A minimum of 24 hours of data is required to create the initial forecasts. However, having a full 14 days of historical data results in more accurate forecasts.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/application-autoscaling-2016-02-06/GetPredictiveScalingForecast)

## Synopsis

```
get-predictive-scaling-forecast
--service-namespace <value>
--resource-id <value>
--scalable-dimension <value>
--policy-name <value>
--start-time <value>
--end-time <value>
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

`--service-namespace` (string)

The namespace of the Amazon Web Services service that provides the resource. For a resource provided by your own application or service, use `custom-resource` instead.

Possible values:

- `ecs`
- `elasticmapreduce`
- `ec2`
- `appstream`
- `dynamodb`
- `rds`
- `sagemaker`
- `custom-resource`
- `comprehend`
- `lambda`
- `cassandra`
- `kafka`
- `elasticache`
- `neptune`
- `workspaces`

`--resource-id` (string)

The identifier of the resource.

`--scalable-dimension` (string)

The scalable dimension.

Possible values:

- `ecs:service:DesiredCount`
- `ec2:spot-fleet-request:TargetCapacity`
- `elasticmapreduce:instancegroup:InstanceCount`
- `appstream:fleet:DesiredCapacity`
- `dynamodb:table:ReadCapacityUnits`
- `dynamodb:table:WriteCapacityUnits`
- `dynamodb:index:ReadCapacityUnits`
- `dynamodb:index:WriteCapacityUnits`
- `rds:cluster:ReadReplicaCount`
- `sagemaker:variant:DesiredInstanceCount`
- `custom-resource:ResourceType:Property`
- `comprehend:document-classifier-endpoint:DesiredInferenceUnits`
- `comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`
- `lambda:function:ProvisionedConcurrency`
- `cassandra:table:ReadCapacityUnits`
- `cassandra:table:WriteCapacityUnits`
- `kafka:broker-storage:VolumeSize`
- `elasticache:cache-cluster:Nodes`
- `elasticache:replication-group:NodeGroups`
- `elasticache:replication-group:Replicas`
- `neptune:cluster:ReadReplicaCount`
- `sagemaker:variant:DesiredProvisionedConcurrency`
- `sagemaker:inference-component:DesiredCopyCount`
- `workspaces:workspacespool:DesiredUserSessions`

`--policy-name` (string)

The name of the policy.

`--start-time` (timestamp)

The inclusive start time of the time range for the forecast data to get. At most, the date and time can be one year before the current date and time

`--end-time` (timestamp)

The exclusive end time of the time range for the forecast data to get. The maximum time duration between the start and end time is 30 days.

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

LoadForecast -> (list)

The load forecast.

(structure)

A `GetPredictiveScalingForecast` call returns the load forecast for a predictive scaling policy. This structure includes the data points for that load forecast, along with the timestamps of those data points and the metric specification.

Timestamps -> (list)

The timestamps for the data points, in UTC format.

(timestamp)

Values -> (list)

The values of the data points.

(double)

MetricSpecification -> (structure)

The metric specification for the load forecast.

TargetValue -> (double)

Specifies the target utilization.

PredefinedMetricPairSpecification -> (structure)

The predefined metric pair specification that determines the appropriate scaling metric and load metric to use.

PredefinedMetricType -> (string)

Indicates which metrics to use. There are two different types of metrics for each metric type: one is a load metric and one is a scaling metric.

ResourceLabel -> (string)

A label that uniquely identifies a specific target group from which to determine the total and average request count.

PredefinedScalingMetricSpecification -> (structure)

The predefined scaling metric specification.

PredefinedMetricType -> (string)

The metric type.

ResourceLabel -> (string)

A label that uniquely identifies a specific target group from which to determine the average request count.

PredefinedLoadMetricSpecification -> (structure)

The predefined load metric specification.

PredefinedMetricType -> (string)

The metric type.

ResourceLabel -> (string)

A label that uniquely identifies a target group.

CustomizedScalingMetricSpecification -> (structure)

The customized scaling metric specification.

MetricDataQueries -> (list)

One or more metric data queries to provide data points for a metric specification.

(structure)

The metric data to return. Also defines whether this call is returning data for one metric only, or whether it is performing a math expression on the values of returned metric statistics to create a new time series. A time series is a series of data points, each of which is associated with a timestamp.

Id -> (string)

A short name that identifies the objectâs results in the response. This name must be unique among all `MetricDataQuery` objects specified for a single scaling policy. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscores. The first character must be a lowercase letter.

Expression -> (string)

The math expression to perform on the returned data, if this object is performing a math expression. This expression can use the `Id` of the other metrics to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions.

Conditional: Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` , but not both.

MetricStat -> (structure)

Information about the metric data to return.

Conditional: Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` , but not both.

Metric -> (structure)

The CloudWatch metric to return, including the metric name, namespace, and dimensions. To get the exact metric name, namespace, and dimensions, inspect the [Metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html) object that is returned by a call to [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html) .

Dimensions -> (list)

Describes the dimensions of the metric.

(structure)

Describes the dimension of a metric.

Name -> (string)

The name of the dimension.

Value -> (string)

The value of the dimension.

MetricName -> (string)

The name of the metric.

Namespace -> (string)

The namespace of the metric.

Stat -> (string)

The statistic to return. It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in [Statistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic) in the *Amazon CloudWatch User Guide* .

The most commonly used metrics for predictive scaling are `Average` and `Sum` .

Unit -> (string)

The unit to use for the returned data points. For a complete list of the units that CloudWatch supports, see the [MetricDatum](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html) data type in the *Amazon CloudWatch API Reference* .

Label -> (string)

A human-readable label for this metric or expression. This is especially useful if this is a math expression, so that you know what the value represents.

ReturnData -> (boolean)

Indicates whether to return the timestamps and raw data values of this metric.

If you use any math expressions, specify `true` for this value for only the final math expression that the metric specification is based on. You must specify `false` for `ReturnData` for all the other metrics and expressions used in the metric specification.

If you are only retrieving metrics and not performing any math expressions, do not specify anything for `ReturnData` . This sets it to its default (`true` ).

CustomizedLoadMetricSpecification -> (structure)

The customized load metric specification.

MetricDataQueries -> (list)

One or more metric data queries to provide data points for a metric specification.

(structure)

The metric data to return. Also defines whether this call is returning data for one metric only, or whether it is performing a math expression on the values of returned metric statistics to create a new time series. A time series is a series of data points, each of which is associated with a timestamp.

Id -> (string)

A short name that identifies the objectâs results in the response. This name must be unique among all `MetricDataQuery` objects specified for a single scaling policy. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscores. The first character must be a lowercase letter.

Expression -> (string)

The math expression to perform on the returned data, if this object is performing a math expression. This expression can use the `Id` of the other metrics to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions.

Conditional: Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` , but not both.

MetricStat -> (structure)

Information about the metric data to return.

Conditional: Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` , but not both.

Metric -> (structure)

The CloudWatch metric to return, including the metric name, namespace, and dimensions. To get the exact metric name, namespace, and dimensions, inspect the [Metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html) object that is returned by a call to [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html) .

Dimensions -> (list)

Describes the dimensions of the metric.

(structure)

Describes the dimension of a metric.

Name -> (string)

The name of the dimension.

Value -> (string)

The value of the dimension.

MetricName -> (string)

The name of the metric.

Namespace -> (string)

The namespace of the metric.

Stat -> (string)

The statistic to return. It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in [Statistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic) in the *Amazon CloudWatch User Guide* .

The most commonly used metrics for predictive scaling are `Average` and `Sum` .

Unit -> (string)

The unit to use for the returned data points. For a complete list of the units that CloudWatch supports, see the [MetricDatum](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html) data type in the *Amazon CloudWatch API Reference* .

Label -> (string)

A human-readable label for this metric or expression. This is especially useful if this is a math expression, so that you know what the value represents.

ReturnData -> (boolean)

Indicates whether to return the timestamps and raw data values of this metric.

If you use any math expressions, specify `true` for this value for only the final math expression that the metric specification is based on. You must specify `false` for `ReturnData` for all the other metrics and expressions used in the metric specification.

If you are only retrieving metrics and not performing any math expressions, do not specify anything for `ReturnData` . This sets it to its default (`true` ).

CustomizedCapacityMetricSpecification -> (structure)

The customized capacity metric specification.

MetricDataQueries -> (list)

One or more metric data queries to provide data points for a metric specification.

(structure)

The metric data to return. Also defines whether this call is returning data for one metric only, or whether it is performing a math expression on the values of returned metric statistics to create a new time series. A time series is a series of data points, each of which is associated with a timestamp.

Id -> (string)

A short name that identifies the objectâs results in the response. This name must be unique among all `MetricDataQuery` objects specified for a single scaling policy. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscores. The first character must be a lowercase letter.

Expression -> (string)

The math expression to perform on the returned data, if this object is performing a math expression. This expression can use the `Id` of the other metrics to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions.

Conditional: Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` , but not both.

MetricStat -> (structure)

Information about the metric data to return.

Conditional: Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat` , but not both.

Metric -> (structure)

The CloudWatch metric to return, including the metric name, namespace, and dimensions. To get the exact metric name, namespace, and dimensions, inspect the [Metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html) object that is returned by a call to [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html) .

Dimensions -> (list)

Describes the dimensions of the metric.

(structure)

Describes the dimension of a metric.

Name -> (string)

The name of the dimension.

Value -> (string)

The value of the dimension.

MetricName -> (string)

The name of the metric.

Namespace -> (string)

The namespace of the metric.

Stat -> (string)

The statistic to return. It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in [Statistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic) in the *Amazon CloudWatch User Guide* .

The most commonly used metrics for predictive scaling are `Average` and `Sum` .

Unit -> (string)

The unit to use for the returned data points. For a complete list of the units that CloudWatch supports, see the [MetricDatum](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html) data type in the *Amazon CloudWatch API Reference* .

Label -> (string)

A human-readable label for this metric or expression. This is especially useful if this is a math expression, so that you know what the value represents.

ReturnData -> (boolean)

Indicates whether to return the timestamps and raw data values of this metric.

If you use any math expressions, specify `true` for this value for only the final math expression that the metric specification is based on. You must specify `false` for `ReturnData` for all the other metrics and expressions used in the metric specification.

If you are only retrieving metrics and not performing any math expressions, do not specify anything for `ReturnData` . This sets it to its default (`true` ).

CapacityForecast -> (structure)

The capacity forecast.

Timestamps -> (list)

The timestamps for the data points, in UTC format.

(timestamp)

Values -> (list)

The values of the data points.

(double)

UpdateTime -> (timestamp)

The time the forecast was made.