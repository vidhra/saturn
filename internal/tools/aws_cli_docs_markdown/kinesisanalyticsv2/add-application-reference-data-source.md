# add-application-reference-data-sourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/add-application-reference-data-source.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/add-application-reference-data-source.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kinesisanalyticsv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/index.html#cli-aws-kinesisanalyticsv2) ]

# add-application-reference-data-source

## Description

Adds a reference data source to an existing SQL-based Kinesis Data Analytics application.

Kinesis Data Analytics reads reference data (that is, an Amazon S3 object) and creates an in-application table within your application. In the request, you provide the source (S3 bucket name and object key name), name of the in-application table to create, and the necessary mapping information that describes how data in an Amazon S3 object maps to columns in the resulting in-application table.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/AddApplicationReferenceDataSource)

## Synopsis

```
add-application-reference-data-source
--application-name <value>
--current-application-version-id <value>
--reference-data-source <value>
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

`--application-name` (string)

The name of an existing application.

`--current-application-version-id` (long)

The version of the application for which you are adding the reference data source. You can use the  DescribeApplication operation to get the current application version. If the version specified is not the current version, the `ConcurrentModificationException` is returned.

`--reference-data-source` (structure)

The reference data source can be an object in your Amazon S3 bucket. Kinesis Data Analytics reads the object and copies the data into the in-application table that is created. You provide an S3 bucket, object key name, and the resulting in-application table that is created.

TableName -> (string)

The name of the in-application table to create.

S3ReferenceDataSource -> (structure)

Identifies the S3 bucket and object that contains the reference data. A SQL-based Kinesis Data Analytics application loads reference data only once. If the data changes, you call the  UpdateApplication operation to trigger reloading of data into your application.

BucketARN -> (string)

The Amazon Resource Name (ARN) of the S3 bucket.

FileKey -> (string)

The object key name containing the reference data.

ReferenceSchema -> (structure)

Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

RecordFormat -> (structure)

Specifies the format of the records on the streaming source.

RecordFormatType -> (string)

The type of record format.

MappingParameters -> (structure)

When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters -> (structure)

Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath -> (string)

The path to the top-level parent that contains the records.

CSVMappingParameters -> (structure)

Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter -> (string)

The row delimiter. For example, in a CSV format, *ânâ* is the typical row delimiter.

RecordColumnDelimiter -> (string)

The column delimiter. For example, in a CSV format, a comma (â,â) is the typical column delimiter.

RecordEncoding -> (string)

Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns -> (list)

A list of `RecordColumn` objects.

(structure)

For a SQL-based Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

Also used to describe the format of the reference data source.

Name -> (string)

The name of the column that is created in the in-application input stream or reference table.

Mapping -> (string)

A reference to the data element in the streaming input or the reference data source.

SqlType -> (string)

The type of column created in the in-application input stream or reference table.

JSON Syntax:

```
{
  "TableName": "string",
  "S3ReferenceDataSource": {
    "BucketARN": "string",
    "FileKey": "string"
  },
  "ReferenceSchema": {
    "RecordFormat": {
      "RecordFormatType": "JSON"|"CSV",
      "MappingParameters": {
        "JSONMappingParameters": {
          "RecordRowPath": "string"
        },
        "CSVMappingParameters": {
          "RecordRowDelimiter": "string",
          "RecordColumnDelimiter": "string"
        }
      }
    },
    "RecordEncoding": "string",
    "RecordColumns": [
      {
        "Name": "string",
        "Mapping": "string",
        "SqlType": "string"
      }
      ...
    ]
  }
}
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

ApplicationARN -> (string)

The application Amazon Resource Name (ARN).

ApplicationVersionId -> (long)

The updated application version ID. Kinesis Data Analytics increments this ID when the application is updated.

ReferenceDataSourceDescriptions -> (list)

Describes reference data sources configured for the application.

(structure)

For a SQL-based Kinesis Data Analytics application, describes the reference data source configured for an application.

ReferenceId -> (string)

The ID of the reference data source. This is the ID that Kinesis Data Analytics assigns when you add the reference data source to your application using the  CreateApplication or  UpdateApplication operation.

TableName -> (string)

The in-application table name created by the specific reference data source configuration.

S3ReferenceDataSourceDescription -> (structure)

Provides the Amazon S3 bucket name, the object key name that contains the reference data.

BucketARN -> (string)

The Amazon Resource Name (ARN) of the S3 bucket.

FileKey -> (string)

Amazon S3 object key name.

ReferenceRoleARN -> (string)

The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon S3 object on your behalf to populate the in-application reference table.

### Note

Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.

ReferenceSchema -> (structure)

Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

RecordFormat -> (structure)

Specifies the format of the records on the streaming source.

RecordFormatType -> (string)

The type of record format.

MappingParameters -> (structure)

When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters -> (structure)

Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath -> (string)

The path to the top-level parent that contains the records.

CSVMappingParameters -> (structure)

Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter -> (string)

The row delimiter. For example, in a CSV format, *ânâ* is the typical row delimiter.

RecordColumnDelimiter -> (string)

The column delimiter. For example, in a CSV format, a comma (â,â) is the typical column delimiter.

RecordEncoding -> (string)

Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns -> (list)

A list of `RecordColumn` objects.

(structure)

For a SQL-based Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

Also used to describe the format of the reference data source.

Name -> (string)

The name of the column that is created in the in-application input stream or reference table.

Mapping -> (string)

A reference to the data element in the streaming input or the reference data source.

SqlType -> (string)

The type of column created in the in-application input stream or reference table.