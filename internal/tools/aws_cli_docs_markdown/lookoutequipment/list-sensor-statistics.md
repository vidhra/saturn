# list-sensor-statisticsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/list-sensor-statistics.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/list-sensor-statistics.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutequipment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/index.html#cli-aws-lookoutequipment) ]

# list-sensor-statistics

## Description

Lists statistics about the data collected for each of the sensors that have been successfully ingested in the particular dataset. Can also be used to retreive Sensor Statistics for a previous ingestion job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutequipment-2020-12-15/ListSensorStatistics)

## Synopsis

```
list-sensor-statistics
--dataset-name <value>
[--ingestion-job-id <value>]
[--max-results <value>]
[--next-token <value>]
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

`--dataset-name` (string)

The name of the dataset associated with the list of Sensor Statistics.

`--ingestion-job-id` (string)

The ingestion job id associated with the list of Sensor Statistics. To get sensor statistics for a particular ingestion job id, both dataset name and ingestion job id must be submitted as inputs.

`--max-results` (integer)

Specifies the maximum number of sensors for which to retrieve statistics.

`--next-token` (string)

An opaque pagination token indicating where to continue the listing of sensor statistics.

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

SensorStatisticsSummaries -> (list)

Provides ingestion-based statistics regarding the specified sensor with respect to various validation types, such as whether data exists, the number and percentage of missing values, and the number and percentage of duplicate timestamps.

(structure)

Summary of ingestion statistics like whether data exists, number of missing values, number of invalid values and so on related to the particular sensor.

ComponentName -> (string)

Name of the component to which the particular sensor belongs for which the statistics belong to.

SensorName -> (string)

Name of the sensor that the statistics belong to.

DataExists -> (boolean)

Parameter that indicates whether data exists for the sensor that the statistics belong to.

MissingValues -> (structure)

Parameter that describes the total number of, and percentage of, values that are missing for the sensor that the statistics belong to.

Count -> (integer)

Indicates the count of occurences of the given statistic.

Percentage -> (float)

Indicates the percentage of occurances of the given statistic.

InvalidValues -> (structure)

Parameter that describes the total number of, and percentage of, values that are invalid for the sensor that the statistics belong to.

Count -> (integer)

Indicates the count of occurences of the given statistic.

Percentage -> (float)

Indicates the percentage of occurances of the given statistic.

InvalidDateEntries -> (structure)

Parameter that describes the total number of invalid date entries associated with the sensor that the statistics belong to.

Count -> (integer)

Indicates the count of occurences of the given statistic.

Percentage -> (float)

Indicates the percentage of occurances of the given statistic.

DuplicateTimestamps -> (structure)

Parameter that describes the total number of duplicate timestamp records associated with the sensor that the statistics belong to.

Count -> (integer)

Indicates the count of occurences of the given statistic.

Percentage -> (float)

Indicates the percentage of occurances of the given statistic.

CategoricalValues -> (structure)

Parameter that describes potential risk about whether data associated with the sensor is categorical.

Status -> (string)

Indicates whether there is a potential data issue related to categorical values.

NumberOfCategory -> (integer)

Indicates the number of categories in the data.

MultipleOperatingModes -> (structure)

Parameter that describes potential risk about whether data associated with the sensor has more than one operating mode.

Status -> (string)

Indicates whether there is a potential data issue related to having multiple operating modes.

LargeTimestampGaps -> (structure)

Parameter that describes potential risk about whether data associated with the sensor contains one or more large gaps between consecutive timestamps.

Status -> (string)

Indicates whether there is a potential data issue related to large gaps in timestamps.

NumberOfLargeTimestampGaps -> (integer)

Indicates the number of large timestamp gaps, if there are any.

MaxTimestampGapInDays -> (integer)

Indicates the size of the largest timestamp gap, in days.

MonotonicValues -> (structure)

Parameter that describes potential risk about whether data associated with the sensor is mostly monotonic.

Status -> (string)

Indicates whether there is a potential data issue related to having monotonic values.

Monotonicity -> (string)

Indicates the monotonicity of values. Can be INCREASING, DECREASING, or STATIC.

DataStartTime -> (timestamp)

Indicates the time reference to indicate the beginning of valid data associated with the sensor that the statistics belong to.

DataEndTime -> (timestamp)

Indicates the time reference to indicate the end of valid data associated with the sensor that the statistics belong to.

NextToken -> (string)

An opaque pagination token indicating where to continue the listing of sensor statistics.