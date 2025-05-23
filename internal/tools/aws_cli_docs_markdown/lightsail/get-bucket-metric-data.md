# get-bucket-metric-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-bucket-metric-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-bucket-metric-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# get-bucket-metric-data

## Description

Returns the data points of a specific metric for an Amazon Lightsail bucket.

Metrics report the utilization of a bucket. View and collect metric data regularly to monitor the number of objects stored in a bucket (including object versions) and the storage space used by those objects.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetBucketMetricData)

## Synopsis

```
get-bucket-metric-data
--bucket-name <value>
--metric-name <value>
--start-time <value>
--end-time <value>
--period <value>
--statistics <value>
--unit <value>
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

`--bucket-name` (string)

The name of the bucket for which to get metric data.

`--metric-name` (string)

The metric for which you want to return information.

Valid bucket metric names are listed below, along with the most useful statistics to include in your request, and the published unit value.

### Note

These bucket metrics are reported once per day.

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-bucket-metric-data.html#id1)`BucketSizeBytes` ** - The amount of data in bytes stored in a bucket. This value is calculated by summing the size of all objects in the bucket (including object versions), including the size of all parts for all incomplete multipart uploads to the bucket. Statistics: The most useful statistic is `Maximum` . Unit: The published unit is `Bytes` .
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-bucket-metric-data.html#id3)`NumberOfObjects` ** - The total number of objects stored in a bucket. This value is calculated by counting all objects in the bucket (including object versions) and the total number of parts for all incomplete multipart uploads to the bucket. Statistics: The most useful statistic is `Average` . Unit: The published unit is `Count` .

Possible values:

- `BucketSizeBytes`
- `NumberOfObjects`

`--start-time` (timestamp)

The timestamp indicating the earliest data to be returned.

`--end-time` (timestamp)

The timestamp indicating the latest data to be returned.

`--period` (integer)

The granularity, in seconds, of the returned data points.

### Note

Bucket storage metrics are reported once per day. Therefore, you should specify a period of 86400 seconds, which is the number of seconds in a day.

`--statistics` (list)

The statistic for the metric.

The following statistics are available:

- `Minimum` - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.
- `Maximum` - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.
- `Sum` - The sum of all values submitted for the matching metric. You can use this statistic to determine the total volume of a metric.
- `Average` - The value of `Sum` / `SampleCount` during the specified period. By comparing this statistic with the `Minimum` and `Maximum` values, you can determine the full scope of a metric and how close the average use is to the `Minimum` and `Maximum` values. This comparison helps you to know when to increase or decrease your resources.
- `SampleCount` - The count, or number, of data points used for the statistical calculation.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  Minimum
  Maximum
  Sum
  Average
  SampleCount
```

`--unit` (string)

The unit for the metric data request.

Valid units depend on the metric data being requested. For the valid units with each available metric, see the `metricName` parameter.

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

metricName -> (string)

The name of the metric returned.

metricData -> (list)

An array of objects that describe the metric data returned.

(structure)

Describes the metric data point.

average -> (double)

The average.

maximum -> (double)

The maximum.

minimum -> (double)

The minimum.

sampleCount -> (double)

The sample count.

sum -> (double)

The sum.

timestamp -> (timestamp)

The timestamp (`1479816991.349` ).

unit -> (string)

The unit.