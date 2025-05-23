# update-column-statistics-for-tableÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-column-statistics-for-table.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-column-statistics-for-table.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# update-column-statistics-for-table

## Description

Creates or updates table statistics of columns.

The Identity and Access Management (IAM) permission required for this operation is `UpdateTable` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateColumnStatisticsForTable)

## Synopsis

```
update-column-statistics-for-table
[--catalog-id <value>]
--database-name <value>
--table-name <value>
--column-statistics-list <value>
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

`--catalog-id` (string)

The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default.

`--database-name` (string)

The name of the catalog database where the partitions reside.

`--table-name` (string)

The name of the partitionsâ table.

`--column-statistics-list` (list)

A list of the column statistics.

(structure)

Represents the generated column-level statistics for a table or partition.

ColumnName -> (string)

Name of column which statistics belong to.

ColumnType -> (string)

The data type of the column.

AnalyzedTime -> (timestamp)

The timestamp of when column statistics were generated.

StatisticsData -> (structure)

A `ColumnStatisticData` object that contains the statistics data values.

Type -> (string)

The type of column statistics data.

BooleanColumnStatisticsData -> (structure)

Boolean column statistics data.

NumberOfTrues -> (long)

The number of true values in the column.

NumberOfFalses -> (long)

The number of false values in the column.

NumberOfNulls -> (long)

The number of null values in the column.

DateColumnStatisticsData -> (structure)

Date column statistics data.

MinimumValue -> (timestamp)

The lowest value in the column.

MaximumValue -> (timestamp)

The highest value in the column.

NumberOfNulls -> (long)

The number of null values in the column.

NumberOfDistinctValues -> (long)

The number of distinct values in a column.

DecimalColumnStatisticsData -> (structure)

Decimal column statistics data. UnscaledValues within are Base64-encoded binary objects storing big-endian, twoâs complement representations of the decimalâs unscaled value.

MinimumValue -> (structure)

The lowest value in the column.

UnscaledValue -> (blob)

The unscaled numeric value.

Scale -> (integer)

The scale that determines where the decimal point falls in the unscaled value.

MaximumValue -> (structure)

The highest value in the column.

UnscaledValue -> (blob)

The unscaled numeric value.

Scale -> (integer)

The scale that determines where the decimal point falls in the unscaled value.

NumberOfNulls -> (long)

The number of null values in the column.

NumberOfDistinctValues -> (long)

The number of distinct values in a column.

DoubleColumnStatisticsData -> (structure)

Double column statistics data.

MinimumValue -> (double)

The lowest value in the column.

MaximumValue -> (double)

The highest value in the column.

NumberOfNulls -> (long)

The number of null values in the column.

NumberOfDistinctValues -> (long)

The number of distinct values in a column.

LongColumnStatisticsData -> (structure)

Long column statistics data.

MinimumValue -> (long)

The lowest value in the column.

MaximumValue -> (long)

The highest value in the column.

NumberOfNulls -> (long)

The number of null values in the column.

NumberOfDistinctValues -> (long)

The number of distinct values in a column.

StringColumnStatisticsData -> (structure)

String column statistics data.

MaximumLength -> (long)

The size of the longest string in the column.

AverageLength -> (double)

The average string length in the column.

NumberOfNulls -> (long)

The number of null values in the column.

NumberOfDistinctValues -> (long)

The number of distinct values in a column.

BinaryColumnStatisticsData -> (structure)

Binary column statistics data.

MaximumLength -> (long)

The size of the longest bit sequence in the column.

AverageLength -> (double)

The average bit sequence length in the column.

NumberOfNulls -> (long)

The number of null values in the column.

JSON Syntax:

```
[
  {
    "ColumnName": "string",
    "ColumnType": "string",
    "AnalyzedTime": timestamp,
    "StatisticsData": {
      "Type": "BOOLEAN"|"DATE"|"DECIMAL"|"DOUBLE"|"LONG"|"STRING"|"BINARY",
      "BooleanColumnStatisticsData": {
        "NumberOfTrues": long,
        "NumberOfFalses": long,
        "NumberOfNulls": long
      },
      "DateColumnStatisticsData": {
        "MinimumValue": timestamp,
        "MaximumValue": timestamp,
        "NumberOfNulls": long,
        "NumberOfDistinctValues": long
      },
      "DecimalColumnStatisticsData": {
        "MinimumValue": {
          "UnscaledValue": blob,
          "Scale": integer
        },
        "MaximumValue": {
          "UnscaledValue": blob,
          "Scale": integer
        },
        "NumberOfNulls": long,
        "NumberOfDistinctValues": long
      },
      "DoubleColumnStatisticsData": {
        "MinimumValue": double,
        "MaximumValue": double,
        "NumberOfNulls": long,
        "NumberOfDistinctValues": long
      },
      "LongColumnStatisticsData": {
        "MinimumValue": long,
        "MaximumValue": long,
        "NumberOfNulls": long,
        "NumberOfDistinctValues": long
      },
      "StringColumnStatisticsData": {
        "MaximumLength": long,
        "AverageLength": double,
        "NumberOfNulls": long,
        "NumberOfDistinctValues": long
      },
      "BinaryColumnStatisticsData": {
        "MaximumLength": long,
        "AverageLength": double,
        "NumberOfNulls": long
      }
    }
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

Errors -> (list)

List of ColumnStatisticsErrors.

(structure)

Encapsulates a `ColumnStatistics` object that failed and the reason for failure.

ColumnStatistics -> (structure)

The `ColumnStatistics` of the column.

ColumnName -> (string)

Name of column which statistics belong to.

ColumnType -> (string)

The data type of the column.

AnalyzedTime -> (timestamp)

The timestamp of when column statistics were generated.

StatisticsData -> (structure)

A `ColumnStatisticData` object that contains the statistics data values.

Type -> (string)

The type of column statistics data.

BooleanColumnStatisticsData -> (structure)

Boolean column statistics data.

NumberOfTrues -> (long)

The number of true values in the column.

NumberOfFalses -> (long)

The number of false values in the column.

NumberOfNulls -> (long)

The number of null values in the column.

DateColumnStatisticsData -> (structure)

Date column statistics data.

MinimumValue -> (timestamp)

The lowest value in the column.

MaximumValue -> (timestamp)

The highest value in the column.

NumberOfNulls -> (long)

The number of null values in the column.

NumberOfDistinctValues -> (long)

The number of distinct values in a column.

DecimalColumnStatisticsData -> (structure)

Decimal column statistics data. UnscaledValues within are Base64-encoded binary objects storing big-endian, twoâs complement representations of the decimalâs unscaled value.

MinimumValue -> (structure)

The lowest value in the column.

UnscaledValue -> (blob)

The unscaled numeric value.

Scale -> (integer)

The scale that determines where the decimal point falls in the unscaled value.

MaximumValue -> (structure)

The highest value in the column.

UnscaledValue -> (blob)

The unscaled numeric value.

Scale -> (integer)

The scale that determines where the decimal point falls in the unscaled value.

NumberOfNulls -> (long)

The number of null values in the column.

NumberOfDistinctValues -> (long)

The number of distinct values in a column.

DoubleColumnStatisticsData -> (structure)

Double column statistics data.

MinimumValue -> (double)

The lowest value in the column.

MaximumValue -> (double)

The highest value in the column.

NumberOfNulls -> (long)

The number of null values in the column.

NumberOfDistinctValues -> (long)

The number of distinct values in a column.

LongColumnStatisticsData -> (structure)

Long column statistics data.

MinimumValue -> (long)

The lowest value in the column.

MaximumValue -> (long)

The highest value in the column.

NumberOfNulls -> (long)

The number of null values in the column.

NumberOfDistinctValues -> (long)

The number of distinct values in a column.

StringColumnStatisticsData -> (structure)

String column statistics data.

MaximumLength -> (long)

The size of the longest string in the column.

AverageLength -> (double)

The average string length in the column.

NumberOfNulls -> (long)

The number of null values in the column.

NumberOfDistinctValues -> (long)

The number of distinct values in a column.

BinaryColumnStatisticsData -> (structure)

Binary column statistics data.

MaximumLength -> (long)

The size of the longest bit sequence in the column.

AverageLength -> (double)

The average bit sequence length in the column.

NumberOfNulls -> (long)

The number of null values in the column.

Error -> (structure)

An error message with the reason for the failure of an operation.

ErrorCode -> (string)

The code associated with this error.

ErrorMessage -> (string)

A message describing the error.