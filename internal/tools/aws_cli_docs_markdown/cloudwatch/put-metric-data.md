# put-metric-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudwatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/index.html#cli-aws-cloudwatch) ]

# put-metric-data

## Description

Publishes metric data to Amazon CloudWatch. CloudWatch associates the data with the specified metric. If the specified metric does not exist, CloudWatch creates the metric. When CloudWatch creates a metric, it can take up to fifteen minutes for the metric to appear in calls to [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html) .

You can publish metrics with associated entity data (so that related telemetry can be found and viewed together), or publish metric data by itself. To send entity data with your metrics, use the `EntityMetricData` parameter. To send metrics without entity data, use the `MetricData` parameter. The `EntityMetricData` structure includes `MetricData` structures for the metric data.

You can publish either individual values in the `Value` field, or arrays of values and the number of times each value occurred during the period by using the `Values` and `Counts` fields in the `MetricData` structure. Using the `Values` and `Counts` method enables you to publish up to 150 values per metric with one `PutMetricData` request, and supports retrieving percentile statistics on this data.

Each `PutMetricData` request is limited to 1 MB in size for HTTP POST requests. You can send a payload compressed by gzip. Each request is also limited to no more than 1000 different metrics (across both the `MetricData` and `EntityMetricData` properties).

Although the `Value` parameter accepts numbers of type `Double` , CloudWatch rejects values that are either too small or too large. Values must be in the range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.

You can use up to 30 dimensions per metric to further clarify what data the metric collects. Each dimension consists of a Name and Value pair. For more information about specifying dimensions, see [Publishing Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) in the *Amazon CloudWatch User Guide* .

You specify the time stamp to be associated with each data point. You can specify time stamps that are as much as two weeks before the current date, and as much as 2 hours after the current day and time.

Data points with time stamps from 24 hours ago or longer can take at least 48 hours to become available for [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) or [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) from the time they are submitted. Data points with time stamps between 3 and 24 hours ago can take as much as 2 hours to become available for [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) or [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) .

CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:

- The `SampleCount` value of the statistic set is 1 and `Min` , `Max` , and `Sum` are all equal.
- The `Min` and `Max` are equal, and `Sum` is equal to `Min` multiplied by `SampleCount` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutMetricData)

## Synopsis

```
put-metric-data
--namespace <value>
[--metric-data <value>]
[--entity-metric-data <value>]
[--strict-entity-validation | --no-strict-entity-validation]
[--metric-name <value>]
[--timestamp <value>]
[--unit <value>]
[--value <value>]
[--dimensions <value>]
[--statistic-values <value>]
[--storage-resolution <value>]
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

`--namespace` (string)

The namespace for the metric data. You can use ASCII characters for the namespace, except for control characters which are not supported.

To avoid conflicts with Amazon Web Services service namespaces, you should not specify a namespace that begins with `AWS/`

`--metric-data` (list)

The data for the metrics. Use this parameter if your metrics do not contain associated entities. The array can include no more than 1000 metrics per call.

The limit of metrics allowed, 1000, is the sum of both `EntityMetricData` and `MetricData` metrics.

(structure)

Encapsulates the information sent to either create a metric or add new values to be aggregated into an existing metric.

MetricName -> (string)

The name of the metric.

Dimensions -> (list)

The dimensions associated with the metric.

(structure)

A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish `InstanceId` as a dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

Name -> (string)

The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (`:` ). ASCII control characters are not supported as part of dimension names.

Value -> (string)

The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

Timestamp -> (timestamp)

The time the metric data was received, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.

Value -> (double)

The value for the metric.

Although the parameter accepts numbers of type Double, CloudWatch rejects values that are either too small or too large. Values must be in the range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.

StatisticValues -> (structure)

The statistical values for the metric.

SampleCount -> (double)

The number of samples used for the statistic set.

Sum -> (double)

The sum of values for the sample set.

Minimum -> (double)

The minimum value of the sample set.

Maximum -> (double)

The maximum value of the sample set.

Values -> (list)

Array of numbers representing the values for the metric during the period. Each unique value is listed just once in this array, and the corresponding number in the `Counts` array specifies the number of times that value occurred during the period. You can include up to 150 unique values in each `PutMetricData` action that specifies a `Values` array.

Although the `Values` array accepts numbers of type `Double` , CloudWatch rejects values that are either too small or too large. Values must be in the range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.

(double)

Counts -> (list)

Array of numbers that is used along with the `Values` array. Each number in the `Count` array is the number of times the corresponding value in the `Values` array occurred during the period.

If you omit the `Counts` array, the default of 1 is used as the value for each count. If you include a `Counts` array, it must include the same amount of values as the `Values` array.

(double)

Unit -> (string)

When you are using a `Put` operation, this defines what unit you want to use when storing the metric.

In a `Get` operation, this displays the unit that is used for the metric.

StorageResolution -> (integer)

Valid values are 1 and 60. Setting this to 1 specifies this metric as a high-resolution metric, so that CloudWatch stores the metric with sub-minute resolution down to one second. Setting this to 60 specifies this metric as a regular-resolution metric, which CloudWatch stores at 1-minute resolution. Currently, high resolution is available only for custom metrics. For more information about high-resolution metrics, see [High-Resolution Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html#high-resolution-metrics) in the *Amazon CloudWatch User Guide* .

This field is optional, if you do not specify it the default of 60 is used.

Shorthand Syntax:

```
MetricName=string,Dimensions=[{Name=string,Value=string},{Name=string,Value=string}],Timestamp=timestamp,Value=double,StatisticValues={SampleCount=double,Sum=double,Minimum=double,Maximum=double},Values=double,double,Counts=double,double,Unit=string,StorageResolution=integer ...
```

JSON Syntax:

```
[
  {
    "MetricName": "string",
    "Dimensions": [
      {
        "Name": "string",
        "Value": "string"
      }
      ...
    ],
    "Timestamp": timestamp,
    "Value": double,
    "StatisticValues": {
      "SampleCount": double,
      "Sum": double,
      "Minimum": double,
      "Maximum": double
    },
    "Values": [double, ...],
    "Counts": [double, ...],
    "Unit": "Seconds"|"Microseconds"|"Milliseconds"|"Bytes"|"Kilobytes"|"Megabytes"|"Gigabytes"|"Terabytes"|"Bits"|"Kilobits"|"Megabits"|"Gigabits"|"Terabits"|"Percent"|"Count"|"Bytes/Second"|"Kilobytes/Second"|"Megabytes/Second"|"Gigabytes/Second"|"Terabytes/Second"|"Bits/Second"|"Kilobits/Second"|"Megabits/Second"|"Gigabits/Second"|"Terabits/Second"|"Count/Second"|"None",
    "StorageResolution": integer
  }
  ...
]
```

`--entity-metric-data` (list)

Data for metrics that contain associated entity information. You can include up to two `EntityMetricData` objects, each of which can contain a single `Entity` and associated metrics.

The limit of metrics allowed, 1000, is the sum of both `EntityMetricData` and `MetricData` metrics.

(structure)

A set of metrics that are associated with an entity, such as a specific service or resource. Contains the entity and the list of metric data associated with it.

Entity -> (structure)

The entity associated with the metrics.

KeyAttributes -> (map)

The attributes of the entity which identify the specific entity, as a list of key-value pairs. Entities with the same `KeyAttributes` are considered to be the same entity. For an entity to be valid, the `KeyAttributes` must exist and be formatted correctly.

There are five allowed attributes (key names): `Type` , `ResourceType` , `Identifier` , `Name` , and `Environment` .

For details about how to use the key attributes to specify an entity, see [How to add related information to telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/adding-your-own-related-telemetry.html) in the *CloudWatch User Guide* .

key -> (string)

value -> (string)

Attributes -> (map)

Additional attributes of the entity that are not used to specify the identity of the entity. A list of key-value pairs.

For details about how to use the attributes, see [How to add related information to telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/adding-your-own-related-telemetry.html) in the *CloudWatch User Guide* .

key -> (string)

value -> (string)

MetricData -> (list)

The metric data.

(structure)

Encapsulates the information sent to either create a metric or add new values to be aggregated into an existing metric.

MetricName -> (string)

The name of the metric.

Dimensions -> (list)

The dimensions associated with the metric.

(structure)

A dimension is a name/value pair that is part of the identity of a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish `InstanceId` as a dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

Name -> (string)

The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (`:` ). ASCII control characters are not supported as part of dimension names.

Value -> (string)

The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

Timestamp -> (timestamp)

The time the metric data was received, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.

Value -> (double)

The value for the metric.

Although the parameter accepts numbers of type Double, CloudWatch rejects values that are either too small or too large. Values must be in the range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.

StatisticValues -> (structure)

The statistical values for the metric.

SampleCount -> (double)

The number of samples used for the statistic set.

Sum -> (double)

The sum of values for the sample set.

Minimum -> (double)

The minimum value of the sample set.

Maximum -> (double)

The maximum value of the sample set.

Values -> (list)

Array of numbers representing the values for the metric during the period. Each unique value is listed just once in this array, and the corresponding number in the `Counts` array specifies the number of times that value occurred during the period. You can include up to 150 unique values in each `PutMetricData` action that specifies a `Values` array.

Although the `Values` array accepts numbers of type `Double` , CloudWatch rejects values that are either too small or too large. Values must be in the range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.

(double)

Counts -> (list)

Array of numbers that is used along with the `Values` array. Each number in the `Count` array is the number of times the corresponding value in the `Values` array occurred during the period.

If you omit the `Counts` array, the default of 1 is used as the value for each count. If you include a `Counts` array, it must include the same amount of values as the `Values` array.

(double)

Unit -> (string)

When you are using a `Put` operation, this defines what unit you want to use when storing the metric.

In a `Get` operation, this displays the unit that is used for the metric.

StorageResolution -> (integer)

Valid values are 1 and 60. Setting this to 1 specifies this metric as a high-resolution metric, so that CloudWatch stores the metric with sub-minute resolution down to one second. Setting this to 60 specifies this metric as a regular-resolution metric, which CloudWatch stores at 1-minute resolution. Currently, high resolution is available only for custom metrics. For more information about high-resolution metrics, see [High-Resolution Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html#high-resolution-metrics) in the *Amazon CloudWatch User Guide* .

This field is optional, if you do not specify it the default of 60 is used.

JSON Syntax:

```
[
  {
    "Entity": {
      "KeyAttributes": {"string": "string"
        ...},
      "Attributes": {"string": "string"
        ...}
    },
    "MetricData": [
      {
        "MetricName": "string",
        "Dimensions": [
          {
            "Name": "string",
            "Value": "string"
          }
          ...
        ],
        "Timestamp": timestamp,
        "Value": double,
        "StatisticValues": {
          "SampleCount": double,
          "Sum": double,
          "Minimum": double,
          "Maximum": double
        },
        "Values": [double, ...],
        "Counts": [double, ...],
        "Unit": "Seconds"|"Microseconds"|"Milliseconds"|"Bytes"|"Kilobytes"|"Megabytes"|"Gigabytes"|"Terabytes"|"Bits"|"Kilobits"|"Megabits"|"Gigabits"|"Terabits"|"Percent"|"Count"|"Bytes/Second"|"Kilobytes/Second"|"Megabytes/Second"|"Gigabytes/Second"|"Terabytes/Second"|"Bits/Second"|"Kilobits/Second"|"Megabits/Second"|"Gigabits/Second"|"Terabits/Second"|"Count/Second"|"None",
        "StorageResolution": integer
      }
      ...
    ]
  }
  ...
]
```

`--strict-entity-validation` | `--no-strict-entity-validation` (boolean)

Whether to accept valid metric data when an invalid entity is sent.

- When set to `true` : Any validation error (for entity or metric data) will fail the entire request, and no data will be ingested. The failed operation will return a 400 result with the error.
- When set to `false` : Validation errors in the entity will not associate the metric with the entity, but the metric data will still be accepted and ingested. Validation errors in the metric data will fail the entire request, and no data will be ingested. In the case of an invalid entity, the operation will return a `200` status, but an additional response header will contain information about the validation errors. The new header, `X-Amzn-Failure-Message` is an enumeration of the following values:
- `InvalidEntity` - The provided entity is invalid.
- `InvalidKeyAttributes` - The provided `KeyAttributes` of an entity is invalid.
- `InvalidAttributes` - The provided `Attributes` of an entity is invalid.
- `InvalidTypeValue` - The provided `Type` in the `KeyAttributes` of an entity is invalid.
- `EntitySizeTooLarge` - The number of `EntityMetricData` objects allowed is 2.
- `MissingRequiredFields` - There are missing required fields in the `KeyAttributes` for the provided `Type` .

For details of the requirements for specifying an entity, see [How to add related information to telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/adding-your-own-related-telemetry.html) in the *CloudWatch User Guide* .

This parameter is *required* when `EntityMetricData` is included.

`--metric-name` (string)
The name of the metric.

`--timestamp` (string)
The time stamp used for the metric. If not specified, the default value is set to the time the metric data was received.

`--unit` (string)
The unit of metric.

`--value` (string)
The value for the metric. Although the âvalue parameter accepts numbers of type Double, Amazon CloudWatch truncates values with very large exponents. Values with base-10 exponents greater than 126 (1 x 10^126) are truncated. Likewise, values with base-10 exponents less than -130 (1 x 10^-130) are also truncated.

`--dimensions` (string)
The âdimensions argument further expands on the identity of a metric using a Name=Value pair, separated by commas, for example: `--dimensions InstanceID=1-23456789,InstanceType=m1.small` . Note that the `--dimensions` argument has a different format when used in `get-metric-data` , where for the same example you would use the format `--dimensions Name=InstanceID,Value=i-aaba32d4 Name=InstanceType,value=m1.small` .

`--statistic-values` (string)
A set of statistical values describing the metric.

`--storage-resolution` (string)

Valid values are 1 and 60. Setting this to 1 specifies this metric as a high-resolution metric, so that CloudWatch stores the metric with sub-minute resolution down to one second. Setting this to 60 specifies this metric as a regular-resolution metric, which CloudWatch stores at 1-minute resolution. Currently, high resolution is available only for custom metrics. For more information about high-resolution metrics, see [High-Resolution Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html#high-resolution-metrics) in the *Amazon CloudWatch User Guide* .

This field is optional, if you do not specify it the default of 60 is used.

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

**To publish a custom metric to Amazon CloudWatch**

The following example uses the `put-metric-data` command to publish a custom metric to Amazon CloudWatch:

```
aws cloudwatch put-metric-data --namespace "Usage Metrics" --metric-data file://metric.json
```

The values for the metric itself are stored in the JSON file, `metric.json`.

Here are the contents of that file:

```
[
  {
    "MetricName": "New Posts",
    "Timestamp": "Wednesday, June 12, 2013 8:28:20 PM",
    "Value": 0.50,
    "Unit": "Count"
  }
]
```

For more information, see [Publishing Custom Metrics](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html) in the *Amazon CloudWatch Developer Guide*.

**To specify multiple dimensions**

The following example illustrates how to specify multiple dimensions. Each dimension is specified as a Name=Value pair. Multiple dimensions are separated by a comma.:

```
aws cloudwatch put-metric-data --metric-name Buffers --namespace MyNameSpace --unit Bytes --value 231434333 --dimensions InstanceID=1-23456789,InstanceType=m1.small
```

## Output

None