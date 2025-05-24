# write-recordsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/write-records.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/write-records.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [timestream-write](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/index.html#cli-aws-timestream-write) ]

# write-records

## Description

Enables you to write your time-series data into Timestream. You can specify a single data point or a batch of data points to be inserted into the system. Timestream offers you a flexible schema that auto detects the column names and data types for your Timestream tables based on the dimension names and data types of the data points you specify when invoking writes into the database.

Timestream supports eventual consistency read semantics. This means that when you query data immediately after writing a batch of data into Timestream, the query results might not reflect the results of a recently completed write operation. The results may also include some stale data. If you repeat the query request after a short time, the results should return the latest data. [Service quotas apply](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html) .

See [code sample](https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.write.html) for details.

**Upserts**

You can use the `Version` parameter in a `WriteRecords` request to update data points. Timestream tracks a version number with each record. `Version` defaults to `1` when itâs not specified for the record in the request. Timestream updates an existing recordâs measure value along with its `Version` when it receives a write request with a higher `Version` number for that record. When it receives an update request where the measure value is the same as that of the existing record, Timestream still updates `Version` , if it is greater than the existing value of `Version` . You can update a data point as many times as desired, as long as the value of `Version` continuously increases.

For example, suppose you write a new record without indicating `Version` in the request. Timestream stores this record, and set `Version` to `1` . Now, suppose you try to update this record with a `WriteRecords` request of the same record with a different measure value but, like before, do not provide `Version` . In this case, Timestream will reject this update with a `RejectedRecordsException` since the updated recordâs version is not greater than the existing value of Version.

However, if you were to resend the update request with `Version` set to `2` , Timestream would then succeed in updating the recordâs value, and the `Version` would be set to `2` . Next, suppose you sent a `WriteRecords` request with this same record and an identical measure value, but with `Version` set to `3` . In this case, Timestream would only update `Version` to `3` . Any further updates would need to send a version number greater than `3` , or the update requests would receive a `RejectedRecordsException` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/timestream-write-2018-11-01/WriteRecords)

## Synopsis

```
write-records
--database-name <value>
--table-name <value>
[--common-attributes <value>]
--records <value>
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

`--database-name` (string)

The name of the Timestream database.

`--table-name` (string)

The name of the Timestream table.

`--common-attributes` (structure)

A record that contains the common measure, dimension, time, and version attributes shared across all the records in the request. The measure and dimension attributes specified will be merged with the measure and dimension attributes in the records object when the data is written into Timestream. Dimensions may not overlap, or a `ValidationException` will be thrown. In other words, a record must contain dimensions with unique names.

Dimensions -> (list)

Contains the list of dimensions for time-series data points.

(structure)

Represents the metadata attributes of the time series. For example, the name and Availability Zone of an EC2 instance or the name of the manufacturer of a wind turbine are dimensions.

Name -> (string)

Dimension represents the metadata attributes of the time series. For example, the name and Availability Zone of an EC2 instance or the name of the manufacturer of a wind turbine are dimensions.

For constraints on dimension names, see [Naming Constraints](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html#limits.naming) .

Value -> (string)

The value of the dimension.

DimensionValueType -> (string)

The data type of the dimension for the time-series data point.

MeasureName -> (string)

Measure represents the data attribute of the time series. For example, the CPU utilization of an EC2 instance or the RPM of a wind turbine are measures.

MeasureValue -> (string)

Contains the measure value for the time-series data point.

MeasureValueType -> (string)

Contains the data type of the measure value for the time-series data point. Default type is `DOUBLE` . For more information, see [Data types](https://docs.aws.amazon.com/timestream/latest/developerguide/writes.html#writes.data-types) .

Time -> (string)

Contains the time at which the measure value for the data point was collected. The time value plus the unit provides the time elapsed since the epoch. For example, if the time value is `12345` and the unit is `ms` , then `12345 ms` have elapsed since the epoch.

TimeUnit -> (string)

The granularity of the timestamp unit. It indicates if the time value is in seconds, milliseconds, nanoseconds, or other supported values. Default is `MILLISECONDS` .

Version -> (long)

64-bit attribute used for record updates. Write requests for duplicate data with a higher version number will update the existing measure value and version. In cases where the measure value is the same, `Version` will still be updated. Default value is `1` .

### Note

`Version` must be `1` or greater, or you will receive a `ValidationException` error.

MeasureValues -> (list)

Contains the list of MeasureValue for time-series data points.

This is only allowed for type `MULTI` . For scalar values, use `MeasureValue` attribute of the record directly.

(structure)

Represents the data attribute of the time series. For example, the CPU utilization of an EC2 instance or the RPM of a wind turbine are measures. MeasureValue has both name and value.

MeasureValue is only allowed for type `MULTI` . Using `MULTI` type, you can pass multiple data attributes associated with the same time series in a single record

Name -> (string)

The name of the MeasureValue.

For constraints on MeasureValue names, see [Naming Constraints](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html#limits.naming) in the Amazon Timestream Developer Guide.

Value -> (string)

The value for the MeasureValue. For information, see [Data types](https://docs.aws.amazon.com/timestream/latest/developerguide/writes.html#writes.data-types) .

Type -> (string)

Contains the data type of the MeasureValue for the time-series data point.

Shorthand Syntax:

```
Dimensions=[{Name=string,Value=string,DimensionValueType=string},{Name=string,Value=string,DimensionValueType=string}],MeasureName=string,MeasureValue=string,MeasureValueType=string,Time=string,TimeUnit=string,Version=long,MeasureValues=[{Name=string,Value=string,Type=string},{Name=string,Value=string,Type=string}]
```

JSON Syntax:

```
{
  "Dimensions": [
    {
      "Name": "string",
      "Value": "string",
      "DimensionValueType": "VARCHAR"
    }
    ...
  ],
  "MeasureName": "string",
  "MeasureValue": "string",
  "MeasureValueType": "DOUBLE"|"BIGINT"|"VARCHAR"|"BOOLEAN"|"TIMESTAMP"|"MULTI",
  "Time": "string",
  "TimeUnit": "MILLISECONDS"|"SECONDS"|"MICROSECONDS"|"NANOSECONDS",
  "Version": long,
  "MeasureValues": [
    {
      "Name": "string",
      "Value": "string",
      "Type": "DOUBLE"|"BIGINT"|"VARCHAR"|"BOOLEAN"|"TIMESTAMP"|"MULTI"
    }
    ...
  ]
}
```

`--records` (list)

An array of records that contain the unique measure, dimension, time, and version attributes for each time-series data point.

(structure)

Represents a time-series data point being written into Timestream. Each record contains an array of dimensions. Dimensions represent the metadata attributes of a time-series data point, such as the instance name or Availability Zone of an EC2 instance. A record also contains the measure name, which is the name of the measure being collected (for example, the CPU utilization of an EC2 instance). Additionally, a record contains the measure value and the value type, which is the data type of the measure value. Also, the record contains the timestamp of when the measure was collected and the timestamp unit, which represents the granularity of the timestamp.

Records have a `Version` field, which is a 64-bit `long` that you can use for updating data points. Writes of a duplicate record with the same dimension, timestamp, and measure name but different measure value will only succeed if the `Version` attribute of the record in the write request is higher than that of the existing record. Timestream defaults to a `Version` of `1` for records without the `Version` field.

Dimensions -> (list)

Contains the list of dimensions for time-series data points.

(structure)

Represents the metadata attributes of the time series. For example, the name and Availability Zone of an EC2 instance or the name of the manufacturer of a wind turbine are dimensions.

Name -> (string)

Dimension represents the metadata attributes of the time series. For example, the name and Availability Zone of an EC2 instance or the name of the manufacturer of a wind turbine are dimensions.

For constraints on dimension names, see [Naming Constraints](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html#limits.naming) .

Value -> (string)

The value of the dimension.

DimensionValueType -> (string)

The data type of the dimension for the time-series data point.

MeasureName -> (string)

Measure represents the data attribute of the time series. For example, the CPU utilization of an EC2 instance or the RPM of a wind turbine are measures.

MeasureValue -> (string)

Contains the measure value for the time-series data point.

MeasureValueType -> (string)

Contains the data type of the measure value for the time-series data point. Default type is `DOUBLE` . For more information, see [Data types](https://docs.aws.amazon.com/timestream/latest/developerguide/writes.html#writes.data-types) .

Time -> (string)

Contains the time at which the measure value for the data point was collected. The time value plus the unit provides the time elapsed since the epoch. For example, if the time value is `12345` and the unit is `ms` , then `12345 ms` have elapsed since the epoch.

TimeUnit -> (string)

The granularity of the timestamp unit. It indicates if the time value is in seconds, milliseconds, nanoseconds, or other supported values. Default is `MILLISECONDS` .

Version -> (long)

64-bit attribute used for record updates. Write requests for duplicate data with a higher version number will update the existing measure value and version. In cases where the measure value is the same, `Version` will still be updated. Default value is `1` .

### Note

`Version` must be `1` or greater, or you will receive a `ValidationException` error.

MeasureValues -> (list)

Contains the list of MeasureValue for time-series data points.

This is only allowed for type `MULTI` . For scalar values, use `MeasureValue` attribute of the record directly.

(structure)

Represents the data attribute of the time series. For example, the CPU utilization of an EC2 instance or the RPM of a wind turbine are measures. MeasureValue has both name and value.

MeasureValue is only allowed for type `MULTI` . Using `MULTI` type, you can pass multiple data attributes associated with the same time series in a single record

Name -> (string)

The name of the MeasureValue.

For constraints on MeasureValue names, see [Naming Constraints](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html#limits.naming) in the Amazon Timestream Developer Guide.

Value -> (string)

The value for the MeasureValue. For information, see [Data types](https://docs.aws.amazon.com/timestream/latest/developerguide/writes.html#writes.data-types) .

Type -> (string)

Contains the data type of the MeasureValue for the time-series data point.

Shorthand Syntax:

```
Dimensions=[{Name=string,Value=string,DimensionValueType=string},{Name=string,Value=string,DimensionValueType=string}],MeasureName=string,MeasureValue=string,MeasureValueType=string,Time=string,TimeUnit=string,Version=long,MeasureValues=[{Name=string,Value=string,Type=string},{Name=string,Value=string,Type=string}] ...
```

JSON Syntax:

```
[
  {
    "Dimensions": [
      {
        "Name": "string",
        "Value": "string",
        "DimensionValueType": "VARCHAR"
      }
      ...
    ],
    "MeasureName": "string",
    "MeasureValue": "string",
    "MeasureValueType": "DOUBLE"|"BIGINT"|"VARCHAR"|"BOOLEAN"|"TIMESTAMP"|"MULTI",
    "Time": "string",
    "TimeUnit": "MILLISECONDS"|"SECONDS"|"MICROSECONDS"|"NANOSECONDS",
    "Version": long,
    "MeasureValues": [
      {
        "Name": "string",
        "Value": "string",
        "Type": "DOUBLE"|"BIGINT"|"VARCHAR"|"BOOLEAN"|"TIMESTAMP"|"MULTI"
      }
      ...
    ]
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

RecordsIngested -> (structure)

Information on the records ingested by this request.

Total -> (integer)

Total count of successfully ingested records.

MemoryStore -> (integer)

Count of records ingested into the memory store.

MagneticStore -> (integer)

Count of records ingested into the magnetic store.