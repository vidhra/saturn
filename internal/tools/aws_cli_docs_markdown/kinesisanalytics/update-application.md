# update-applicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/update-application.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/update-application.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kinesisanalytics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/index.html#cli-aws-kinesisanalytics) ]

# update-application

## Description

### Note

This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see [Amazon Kinesis Data Analytics API V2 Documentation](https://awscli.amazonaws.com/kinesisanalytics/latest/apiv2/Welcome.html) .

Updates an existing Amazon Kinesis Analytics application. Using this API, you can update application code, input configuration, and output configuration.

Note that Amazon Kinesis Analytics updates the `CurrentApplicationVersionId` each time you update your application.

This operation requires permission for the `kinesisanalytics:UpdateApplication` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/UpdateApplication)

## Synopsis

```
update-application
--application-name <value>
--current-application-version-id <value>
--application-update <value>
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

Name of the Amazon Kinesis Analytics application to update.

`--current-application-version-id` (long)

The current application version ID. You can use the [DescribeApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html) operation to get this value.

`--application-update` (structure)

Describes application updates.

InputUpdates -> (list)

Describes application input configuration updates.

(structure)

Describes updates to a specific input configuration (identified by the `InputId` of an application).

InputId -> (string)

Input ID of the application input to be updated.

NamePrefixUpdate -> (string)

Name prefix for in-application streams that Amazon Kinesis Analytics creates for the specific streaming source.

InputProcessingConfigurationUpdate -> (structure)

Describes updates for an input processing configuration.

InputLambdaProcessorUpdate -> (structure)

Provides update information for an [InputLambdaProcessor](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html) .

ResourceARNUpdate -> (string)

The Amazon Resource Name (ARN) of the new [AWS Lambda](https://docs.aws.amazon.com/lambda/) function that is used to preprocess the records in the stream.

### Note

To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see [Example ARNs: AWS Lambda](https://awscli.amazonaws.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda)

RoleARNUpdate -> (string)

The ARN of the new IAM role that is used to access the AWS Lambda function.

KinesisStreamsInputUpdate -> (structure)

If an Amazon Kinesis stream is the streaming source to be updated, provides an updated stream Amazon Resource Name (ARN) and IAM role ARN.

ResourceARNUpdate -> (string)

Amazon Resource Name (ARN) of the input Amazon Kinesis stream to read.

RoleARNUpdate -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.

KinesisFirehoseInputUpdate -> (structure)

If an Amazon Kinesis Firehose delivery stream is the streaming source to be updated, provides an updated stream ARN and IAM role ARN.

ResourceARNUpdate -> (string)

Amazon Resource Name (ARN) of the input Amazon Kinesis Firehose delivery stream to read.

RoleARNUpdate -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.

InputSchemaUpdate -> (structure)

Describes the data format on the streaming source, and how record elements on the streaming source map to columns of the in-application stream that is created.

RecordFormatUpdate -> (structure)

Specifies the format of the records on the streaming source.

RecordFormatType -> (string)

The type of record format.

MappingParameters -> (structure)

When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters -> (structure)

Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath -> (string)

Path to the top-level parent that contains the records.

CSVMappingParameters -> (structure)

Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter -> (string)

Row delimiter. For example, in a CSV format, *ânâ* is the typical row delimiter.

RecordColumnDelimiter -> (string)

Column delimiter. For example, in a CSV format, a comma (â,â) is the typical column delimiter.

RecordEncodingUpdate -> (string)

Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumnUpdates -> (list)

A list of `RecordColumn` objects. Each object describes the mapping of the streaming source element to the corresponding column in the in-application stream.

(structure)

Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

Also used to describe the format of the reference data source.

Name -> (string)

Name of the column created in the in-application input stream or reference table.

Mapping -> (string)

Reference to the data element in the streaming input or the reference data source. This element is required if the [RecordFormatType](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel) is `JSON` .

SqlType -> (string)

Type of column created in the in-application input stream or reference table.

InputParallelismUpdate -> (structure)

Describes the parallelism updates (the number in-application streams Amazon Kinesis Analytics creates for the specific streaming source).

CountUpdate -> (integer)

Number of in-application streams to create for the specified streaming source.

ApplicationCodeUpdate -> (string)

Describes application code updates.

OutputUpdates -> (list)

Describes application output configuration updates.

(structure)

Describes updates to the output configuration identified by the `OutputId` .

OutputId -> (string)

Identifies the specific output configuration that you want to update.

NameUpdate -> (string)

If you want to specify a different in-application stream for this output configuration, use this field to specify the new in-application stream name.

KinesisStreamsOutputUpdate -> (structure)

Describes an Amazon Kinesis stream as the destination for the output.

ResourceARNUpdate -> (string)

Amazon Resource Name (ARN) of the Amazon Kinesis stream where you want to write the output.

RoleARNUpdate -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.

KinesisFirehoseOutputUpdate -> (structure)

Describes an Amazon Kinesis Firehose delivery stream as the destination for the output.

ResourceARNUpdate -> (string)

Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream to write to.

RoleARNUpdate -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.

LambdaOutputUpdate -> (structure)

Describes an AWS Lambda function as the destination for the output.

ResourceARNUpdate -> (string)

Amazon Resource Name (ARN) of the destination Lambda function.

### Note

To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see [Example ARNs: AWS Lambda](https://awscli.amazonaws.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda)

RoleARNUpdate -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination function on your behalf. You need to grant the necessary permissions to this role.

DestinationSchemaUpdate -> (structure)

Describes the data format when records are written to the destination. For more information, see [Configuring Application Output](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html) .

RecordFormatType -> (string)

Specifies the format of the records on the output stream.

ReferenceDataSourceUpdates -> (list)

Describes application reference data source updates.

(structure)

When you update a reference data source configuration for an application, this object provides all the updated values (such as the source bucket name and object key name), the in-application table name that is created, and updated mapping information that maps the data in the Amazon S3 object to the in-application reference table that is created.

ReferenceId -> (string)

ID of the reference data source being updated. You can use the [DescribeApplication](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html) operation to get this value.

TableNameUpdate -> (string)

In-application table name that is created by this update.

S3ReferenceDataSourceUpdate -> (structure)

Describes the S3 bucket name, object key name, and IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object on your behalf and populate the in-application reference table.

BucketARNUpdate -> (string)

Amazon Resource Name (ARN) of the S3 bucket.

FileKeyUpdate -> (string)

Object key name.

ReferenceRoleARNUpdate -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object and populate the in-application.

ReferenceSchemaUpdate -> (structure)

Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

RecordFormat -> (structure)

Specifies the format of the records on the streaming source.

RecordFormatType -> (string)

The type of record format.

MappingParameters -> (structure)

When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters -> (structure)

Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath -> (string)

Path to the top-level parent that contains the records.

CSVMappingParameters -> (structure)

Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter -> (string)

Row delimiter. For example, in a CSV format, *ânâ* is the typical row delimiter.

RecordColumnDelimiter -> (string)

Column delimiter. For example, in a CSV format, a comma (â,â) is the typical column delimiter.

RecordEncoding -> (string)

Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns -> (list)

A list of `RecordColumn` objects.

(structure)

Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

Also used to describe the format of the reference data source.

Name -> (string)

Name of the column created in the in-application input stream or reference table.

Mapping -> (string)

Reference to the data element in the streaming input or the reference data source. This element is required if the [RecordFormatType](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel) is `JSON` .

SqlType -> (string)

Type of column created in the in-application input stream or reference table.

CloudWatchLoggingOptionUpdates -> (list)

Describes application CloudWatch logging option updates.

(structure)

Describes CloudWatch logging option updates.

CloudWatchLoggingOptionId -> (string)

ID of the CloudWatch logging option to update

LogStreamARNUpdate -> (string)

ARN of the CloudWatch log to receive application messages.

RoleARNUpdate -> (string)

IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role used must have the `PutLogEvents` policy action enabled.

JSON Syntax:

```
{
  "InputUpdates": [
    {
      "InputId": "string",
      "NamePrefixUpdate": "string",
      "InputProcessingConfigurationUpdate": {
        "InputLambdaProcessorUpdate": {
          "ResourceARNUpdate": "string",
          "RoleARNUpdate": "string"
        }
      },
      "KinesisStreamsInputUpdate": {
        "ResourceARNUpdate": "string",
        "RoleARNUpdate": "string"
      },
      "KinesisFirehoseInputUpdate": {
        "ResourceARNUpdate": "string",
        "RoleARNUpdate": "string"
      },
      "InputSchemaUpdate": {
        "RecordFormatUpdate": {
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
        "RecordEncodingUpdate": "string",
        "RecordColumnUpdates": [
          {
            "Name": "string",
            "Mapping": "string",
            "SqlType": "string"
          }
          ...
        ]
      },
      "InputParallelismUpdate": {
        "CountUpdate": integer
      }
    }
    ...
  ],
  "ApplicationCodeUpdate": "string",
  "OutputUpdates": [
    {
      "OutputId": "string",
      "NameUpdate": "string",
      "KinesisStreamsOutputUpdate": {
        "ResourceARNUpdate": "string",
        "RoleARNUpdate": "string"
      },
      "KinesisFirehoseOutputUpdate": {
        "ResourceARNUpdate": "string",
        "RoleARNUpdate": "string"
      },
      "LambdaOutputUpdate": {
        "ResourceARNUpdate": "string",
        "RoleARNUpdate": "string"
      },
      "DestinationSchemaUpdate": {
        "RecordFormatType": "JSON"|"CSV"
      }
    }
    ...
  ],
  "ReferenceDataSourceUpdates": [
    {
      "ReferenceId": "string",
      "TableNameUpdate": "string",
      "S3ReferenceDataSourceUpdate": {
        "BucketARNUpdate": "string",
        "FileKeyUpdate": "string",
        "ReferenceRoleARNUpdate": "string"
      },
      "ReferenceSchemaUpdate": {
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
    ...
  ],
  "CloudWatchLoggingOptionUpdates": [
    {
      "CloudWatchLoggingOptionId": "string",
      "LogStreamARNUpdate": "string",
      "RoleARNUpdate": "string"
    }
    ...
  ]
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

None