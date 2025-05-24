# batch-get-frame-metric-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/batch-get-frame-metric-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/batch-get-frame-metric-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeguruprofiler](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/index.html#cli-aws-codeguruprofiler) ]

# batch-get-frame-metric-data

## Description

Returns the time series of values for a requested list of frame metrics from a time period.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeguruprofiler-2019-07-18/BatchGetFrameMetricData)

## Synopsis

```
batch-get-frame-metric-data
[--end-time <value>]
[--frame-metrics <value>]
[--period <value>]
--profiling-group-name <value>
[--start-time <value>]
[--target-resolution <value>]
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

`--end-time` (timestamp)

The end time of the time period for the returned time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

`--frame-metrics` (list)

The details of the metrics that are used to request a time series of values. The metric includes the name of the frame, the aggregation type to calculate the metric value for the frame, and the thread states to use to get the count for the metric value of the frame.

(structure)

The frame name, metric type, and thread states. These are used to derive the value of the metric for the frame.

frameName -> (string)

Name of the method common across the multiple occurrences of a frame in an application profile.

threadStates -> (list)

List of application runtime thread states used to get the counts for a frame a derive a metric value.

(string)

type -> (string)

A type of aggregation that specifies how a metric for a frame is analyzed. The supported value `AggregatedRelativeTotalTime` is an aggregation of the metric value for one frame that is calculated across the occurrences of all frames in a profile.

Shorthand Syntax:

```
frameName=string,threadStates=string,string,type=string ...
```

JSON Syntax:

```
[
  {
    "frameName": "string",
    "threadStates": ["string", ...],
    "type": "AggregatedRelativeTotalTime"
  }
  ...
]
```

`--period` (string)

The duration of the frame metrics used to return the time series values. Specify using the ISO 8601 format. The maximum period duration is one day (`PT24H` or `P1D` ).

`--profiling-group-name` (string)

The name of the profiling group associated with the the frame metrics used to return the time series values.

`--start-time` (timestamp)

The start time of the time period for the frame metrics used to return the time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

`--target-resolution` (string)

The requested resolution of time steps for the returned time series of values. If the requested target resolution is not available due to data not being retained we provide a best effort result by falling back to the most granular available resolution after the target resolution. There are 3 valid values.

- `P1D` â 1 day
- `PT1H` â 1 hour
- `PT5M` â 5 minutes

Possible values:

- `PT5M`
- `PT1H`
- `P1D`

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

endTime -> (timestamp)

The end time of the time period for the returned time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

endTimes -> (list)

List of instances, or time steps, in the time series. For example, if the `period` is one day (`PT24H)` ), and the `resolution` is five minutes (`PT5M` ), then there are 288 `endTimes` in the list that are each five minutes appart.

(structure)

A data type that contains a `Timestamp` object. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

value -> (timestamp)

A `Timestamp` . This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

frameMetricData -> (list)

Details of the metrics to request a time series of values. The metric includes the name of the frame, the aggregation type to calculate the metric value for the frame, and the thread states to use to get the count for the metric value of the frame.

(structure)

Information about a frame metric and its values.

frameMetric -> (structure)

The frame name, metric type, and thread states. These are used to derive the value of the metric for the frame.

frameName -> (string)

Name of the method common across the multiple occurrences of a frame in an application profile.

threadStates -> (list)

List of application runtime thread states used to get the counts for a frame a derive a metric value.

(string)

type -> (string)

A type of aggregation that specifies how a metric for a frame is analyzed. The supported value `AggregatedRelativeTotalTime` is an aggregation of the metric value for one frame that is calculated across the occurrences of all frames in a profile.

values -> (list)

A list of values that are associated with a frame metric.

(double)

resolution -> (string)

Resolution or granularity of the profile data used to generate the time series. This is the value used to jump through time steps in a time series. There are 3 valid values.

- `P1D` â 1 day
- `PT1H` â 1 hour
- `PT5M` â 5 minutes

startTime -> (timestamp)

The start time of the time period for the returned time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

unprocessedEndTimes -> (map)

List of instances which remained unprocessed. This will create a missing time step in the list of end times.

key -> (string)

value -> (list)

(structure)

A data type that contains a `Timestamp` object. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

value -> (timestamp)

A `Timestamp` . This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.