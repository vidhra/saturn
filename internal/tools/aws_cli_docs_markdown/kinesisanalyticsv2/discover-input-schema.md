# discover-input-schemaÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/discover-input-schema.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/discover-input-schema.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kinesisanalyticsv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/index.html#cli-aws-kinesisanalyticsv2) ]

# discover-input-schema

## Description

Infers a schema for a SQL-based Kinesis Data Analytics application by evaluating sample records on the specified streaming source (Kinesis data stream or Kinesis Data Firehose delivery stream) or Amazon S3 object. In the response, the operation returns the inferred schema and also the sample records that the operation used to infer the schema.

You can use the inferred schema when configuring a streaming source for your application. When you create an application using the Kinesis Data Analytics console, the console uses this operation to infer a schema and show it in the console user interface.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/DiscoverInputSchema)

## Synopsis

```
discover-input-schema
[--resource-arn <value>]
--service-execution-role <value>
[--input-starting-position-configuration <value>]
[--s3-configuration <value>]
[--input-processing-configuration <value>]
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

`--resource-arn` (string)

The Amazon Resource Name (ARN) of the streaming source.

`--service-execution-role` (string)

The ARN of the role that is used to access the streaming source.

`--input-starting-position-configuration` (structure)

The point at which you want Kinesis Data Analytics to start reading records from the specified streaming source for discovery purposes.

InputStartingPosition -> (string)

The starting position on the stream.

- `NOW` - Start reading just after the most recent record in the stream, and start at the request timestamp that the customer issued.
- `TRIM_HORIZON` - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Data Firehose delivery stream.
- `LAST_STOPPED_POINT` - Resume reading from where the application last stopped reading.

Shorthand Syntax:

```
InputStartingPosition=string
```

JSON Syntax:

```
{
  "InputStartingPosition": "NOW"|"TRIM_HORIZON"|"LAST_STOPPED_POINT"
}
```

`--s3-configuration` (structure)

Specify this parameter to discover a schema from data in an Amazon S3 object.

BucketARN -> (string)

The ARN of the S3 bucket that contains the data.

FileKey -> (string)

The name of the object that contains the data.

Shorthand Syntax:

```
BucketARN=string,FileKey=string
```

JSON Syntax:

```
{
  "BucketARN": "string",
  "FileKey": "string"
}
```

`--input-processing-configuration` (structure)

The  InputProcessingConfiguration to use to preprocess the records before discovering the schema of the records.

InputLambdaProcessor -> (structure)

The  InputLambdaProcessor that is used to preprocess the records in the stream before being processed by your application code.

ResourceARN -> (string)

The ARN of the Amazon Lambda function that operates on records in the stream.

### Note

To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see [Example ARNs: Amazon Lambda](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda)

Shorthand Syntax:

```
InputLambdaProcessor={ResourceARN=string}
```

JSON Syntax:

```
{
  "InputLambdaProcessor": {
    "ResourceARN": "string"
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

InputSchema -> (structure)

The schema inferred from the streaming source. It identifies the format of the data in the streaming source and how each data element maps to corresponding columns in the in-application stream that you can create.

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

ParsedInputRecords -> (list)

An array of elements, where each element corresponds to a row in a stream record (a stream record can have more than one row).

(list)

(string)

ProcessedInputRecords -> (list)

The stream data that was modified by the processor specified in the `InputProcessingConfiguration` parameter.

(string)

RawInputRecords -> (list)

The raw stream data that was sampled to infer the schema.

(string)