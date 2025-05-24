# describe-applicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/describe-application.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/describe-application.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kinesisanalytics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/index.html#cli-aws-kinesisanalytics) ]

# describe-application

## Description

### Note

This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see [Amazon Kinesis Data Analytics API V2 Documentation](https://awscli.amazonaws.com/kinesisanalytics/latest/apiv2/Welcome.html) .

Returns information about a specific Amazon Kinesis Analytics application.

If you want to retrieve a list of all applications in your account, use the [ListApplications](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_ListApplications.html) operation.

This operation requires permissions to perform the `kinesisanalytics:DescribeApplication` action. You can use `DescribeApplication` to get the current application versionId, which you need to call other operations such as `Update` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/DescribeApplication)

## Synopsis

```
describe-application
--application-name <value>
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

Name of the application.

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

ApplicationDetail -> (structure)

Provides a description of the application, such as the application Amazon Resource Name (ARN), status, latest version, and input and output configuration details.

ApplicationName -> (string)

Name of the application.

ApplicationDescription -> (string)

Description of the application.

ApplicationARN -> (string)

ARN of the application.

ApplicationStatus -> (string)

Status of the application.

CreateTimestamp -> (timestamp)

Time stamp when the application version was created.

LastUpdateTimestamp -> (timestamp)

Time stamp when the application was last updated.

InputDescriptions -> (list)

Describes the application input configuration. For more information, see [Configuring Application Input](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html) .

(structure)

Describes the application input configuration. For more information, see [Configuring Application Input](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html) .

InputId -> (string)

Input ID associated with the application input. This is the ID that Amazon Kinesis Analytics assigns to each input configuration you add to your application.

NamePrefix -> (string)

In-application name prefix.

InAppStreamNames -> (list)

Returns the in-application stream names that are mapped to the stream source.

(string)

InputProcessingConfigurationDescription -> (structure)

The description of the preprocessor that executes on records in this input before the applicationâs code is run.

InputLambdaProcessorDescription -> (structure)

Provides configuration information about the associated [InputLambdaProcessorDescription](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessorDescription.html) .

ResourceARN -> (string)

The ARN of the [AWS Lambda](https://docs.aws.amazon.com/lambda/) function that is used to preprocess the records in the stream.

RoleARN -> (string)

The ARN of the IAM role that is used to access the AWS Lambda function.

KinesisStreamsInputDescription -> (structure)

If an Amazon Kinesis stream is configured as streaming source, provides Amazon Kinesis streamâs Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.

ResourceARN -> (string)

Amazon Resource Name (ARN) of the Amazon Kinesis stream.

RoleARN -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.

KinesisFirehoseInputDescription -> (structure)

If an Amazon Kinesis Firehose delivery stream is configured as a streaming source, provides the delivery streamâs ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.

ResourceARN -> (string)

Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.

RoleARN -> (string)

ARN of the IAM role that Amazon Kinesis Analytics assumes to access the stream.

InputSchema -> (structure)

Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.

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

InputParallelism -> (structure)

Describes the configured parallelism (number of in-application streams mapped to the streaming source).

Count -> (integer)

Number of in-application streams to create. For more information, see [Limits](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html) .

InputStartingPositionConfiguration -> (structure)

Point at which the application is configured to read from the input stream.

InputStartingPosition -> (string)

The starting position on the stream.

- `NOW` - Start reading just after the most recent record in the stream, start at the request time stamp that the customer issued.
- `TRIM_HORIZON` - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Firehose delivery stream.
- `LAST_STOPPED_POINT` - Resume reading from where the application last stopped reading.

OutputDescriptions -> (list)

Describes the application output configuration. For more information, see [Configuring Application Output](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html) .

(structure)

Describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be an Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream.

OutputId -> (string)

A unique identifier for the output configuration.

Name -> (string)

Name of the in-application stream configured as output.

KinesisStreamsOutputDescription -> (structure)

Describes Amazon Kinesis stream configured as the destination where output is written.

ResourceARN -> (string)

Amazon Resource Name (ARN) of the Amazon Kinesis stream.

RoleARN -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.

KinesisFirehoseOutputDescription -> (structure)

Describes the Amazon Kinesis Firehose delivery stream configured as the destination where output is written.

ResourceARN -> (string)

Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.

RoleARN -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.

LambdaOutputDescription -> (structure)

Describes the AWS Lambda function configured as the destination where output is written.

ResourceARN -> (string)

Amazon Resource Name (ARN) of the destination Lambda function.

RoleARN -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination function.

DestinationSchema -> (structure)

Data format used for writing data to the destination.

RecordFormatType -> (string)

Specifies the format of the records on the output stream.

ReferenceDataSourceDescriptions -> (list)

Describes reference data sources configured for the application. For more information, see [Configuring Application Input](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html) .

(structure)

Describes the reference data source configured for an application.

ReferenceId -> (string)

ID of the reference data source. This is the ID that Amazon Kinesis Analytics assigns when you add the reference data source to your application using the [AddApplicationReferenceDataSource](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationReferenceDataSource.html) operation.

TableName -> (string)

The in-application table name created by the specific reference data source configuration.

S3ReferenceDataSourceDescription -> (structure)

Provides the S3 bucket name, the object key name that contains the reference data. It also provides the Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object and populate the in-application reference table.

BucketARN -> (string)

Amazon Resource Name (ARN) of the S3 bucket.

FileKey -> (string)

Amazon S3 object key name.

ReferenceRoleARN -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object on your behalf to populate the in-application reference table.

ReferenceSchema -> (structure)

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

CloudWatchLoggingOptionDescriptions -> (list)

Describes the CloudWatch log streams that are configured to receive application messages. For more information about using CloudWatch log streams with Amazon Kinesis Analytics applications, see [Working with Amazon CloudWatch Logs](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html) .

(structure)

Description of the CloudWatch logging option.

CloudWatchLoggingOptionId -> (string)

ID of the CloudWatch logging option description.

LogStreamARN -> (string)

ARN of the CloudWatch log to receive application messages.

RoleARN -> (string)

IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role used must have the `PutLogEvents` policy action enabled.

ApplicationCode -> (string)

Returns the application code that you provided to perform data analysis on any of the in-application streams in your application.

ApplicationVersionId -> (long)

Provides the current application version.