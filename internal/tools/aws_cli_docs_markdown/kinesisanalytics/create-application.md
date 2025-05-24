# create-applicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/create-application.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/create-application.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kinesisanalytics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/index.html#cli-aws-kinesisanalytics) ]

# create-application

## Description

### Note

This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see [Amazon Kinesis Data Analytics API V2 Documentation](https://awscli.amazonaws.com/kinesisanalytics/latest/apiv2/Welcome.html) .

Creates an Amazon Kinesis Analytics application. You can configure each application with one streaming source as input, application code to process the input, and up to three destinations where you want Amazon Kinesis Analytics to write the output data from your application. For an overview, see [How it Works](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works.html) .

In the input configuration, you map the streaming source to an in-application stream, which you can think of as a constantly updating table. In the mapping, you must provide a schema for the in-application stream and map each data column in the in-application stream to a data element in the streaming source.

Your application code is one or more SQL statements that read input data, transform it, and generate output. Your application code can create one or more SQL artifacts like SQL streams or pumps.

In the output configuration, you can configure the application to write data from in-application streams created in your applications to up to three destinations.

To read data from your source stream or write data to destination streams, Amazon Kinesis Analytics needs your permissions. You grant these permissions by creating IAM roles. This operation requires permissions to perform the `kinesisanalytics:CreateApplication` action.

For introductory exercises to create an Amazon Kinesis Analytics application, see [Getting Started](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/getting-started.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kinesisanalytics-2015-08-14/CreateApplication)

## Synopsis

```
create-application
--application-name <value>
[--application-description <value>]
[--inputs <value>]
[--outputs <value>]
[--cloud-watch-logging-options <value>]
[--application-code <value>]
[--tags <value>]
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

Name of your Amazon Kinesis Analytics application (for example, `sample-app` ).

`--application-description` (string)

Summary description of the application.

`--inputs` (list)

Use this parameter to configure the application input.

You can configure your application to receive input from a single streaming source. In this configuration, you map this streaming source to an in-application stream that is created. Your application code can then query the in-application stream like a table (you can think of it as a constantly updating table).

For the streaming source, you provide its Amazon Resource Name (ARN) and format of data on the stream (for example, JSON, CSV, etc.). You also must provide an IAM role that Amazon Kinesis Analytics can assume to read this stream on your behalf.

To create the in-application stream, you need to specify a schema to transform your data into a schematized version used in SQL. In the schema, you provide the necessary mapping of the data elements in the streaming source to record columns in the in-app stream.

(structure)

When you configure the application input, you specify the streaming source, the in-application stream name that is created, and the mapping between the two. For more information, see [Configuring Application Input](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html) .

NamePrefix -> (string)

Name prefix to use when creating an in-application stream. Suppose that you specify a prefix âMyInApplicationStream.â Amazon Kinesis Analytics then creates one or more (as per the `InputParallelism` count you specified) in-application streams with names âMyInApplicationStream_001,â âMyInApplicationStream_002,â and so on.

InputProcessingConfiguration -> (structure)

The [InputProcessingConfiguration](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html) for the input. An input processor transforms records as they are received from the stream, before the applicationâs SQL code executes. Currently, the only input processing configuration available is [InputLambdaProcessor](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html) .

InputLambdaProcessor -> (structure)

The [InputLambdaProcessor](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html) that is used to preprocess the records in the stream before being processed by your application code.

ResourceARN -> (string)

The ARN of the [AWS Lambda](https://docs.aws.amazon.com/lambda/) function that operates on records in the stream.

### Note

To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see [Example ARNs: AWS Lambda](https://awscli.amazonaws.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda)

RoleARN -> (string)

The ARN of the IAM role that is used to access the AWS Lambda function.

KinesisStreamsInput -> (structure)

If the streaming source is an Amazon Kinesis stream, identifies the streamâs Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.

Note: Either `KinesisStreamsInput` or `KinesisFirehoseInput` is required.

ResourceARN -> (string)

ARN of the input Amazon Kinesis stream to read.

RoleARN -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.

KinesisFirehoseInput -> (structure)

If the streaming source is an Amazon Kinesis Firehose delivery stream, identifies the delivery streamâs ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.

Note: Either `KinesisStreamsInput` or `KinesisFirehoseInput` is required.

ResourceARN -> (string)

ARN of the input delivery stream.

RoleARN -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to make sure that the role has the necessary permissions to access the stream.

InputParallelism -> (structure)

Describes the number of in-application streams to create.

Data from your source is routed to these in-application input streams.

(see [Configuring Application Input](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html) .

Count -> (integer)

Number of in-application streams to create. For more information, see [Limits](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html) .

InputSchema -> (structure)

Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.

Also used to describe the format of the reference data source.

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

JSON Syntax:

```
[
  {
    "NamePrefix": "string",
    "InputProcessingConfiguration": {
      "InputLambdaProcessor": {
        "ResourceARN": "string",
        "RoleARN": "string"
      }
    },
    "KinesisStreamsInput": {
      "ResourceARN": "string",
      "RoleARN": "string"
    },
    "KinesisFirehoseInput": {
      "ResourceARN": "string",
      "RoleARN": "string"
    },
    "InputParallelism": {
      "Count": integer
    },
    "InputSchema": {
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
]
```

`--outputs` (list)

You can configure application output to write data from any of the in-application streams to up to three destinations.

These destinations can be Amazon Kinesis streams, Amazon Kinesis Firehose delivery streams, AWS Lambda destinations, or any combination of the three.

In the configuration, you specify the in-application stream name, the destination stream or Lambda function Amazon Resource Name (ARN), and the format to use when writing data. You must also provide an IAM role that Amazon Kinesis Analytics can assume to write to the destination stream or Lambda function on your behalf.

In the output configuration, you also provide the output stream or Lambda function ARN. For stream destinations, you provide the format of data in the stream (for example, JSON, CSV). You also must provide an IAM role that Amazon Kinesis Analytics can assume to write to the stream or Lambda function on your behalf.

(structure)

Describes application output configuration in which you identify an in-application stream and a destination where you want the in-application stream data to be written. The destination can be an Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream.

For limits on how many destinations an application can write and other limitations, see [Limits](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html) .

Name -> (string)

Name of the in-application stream.

KinesisStreamsOutput -> (structure)

Identifies an Amazon Kinesis stream as the destination.

ResourceARN -> (string)

ARN of the destination Amazon Kinesis stream to write to.

RoleARN -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.

KinesisFirehoseOutput -> (structure)

Identifies an Amazon Kinesis Firehose delivery stream as the destination.

ResourceARN -> (string)

ARN of the destination Amazon Kinesis Firehose delivery stream to write to.

RoleARN -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.

LambdaOutput -> (structure)

Identifies an AWS Lambda function as the destination.

ResourceARN -> (string)

Amazon Resource Name (ARN) of the destination Lambda function to write to.

### Note

To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see [Example ARNs: AWS Lambda](https://awscli.amazonaws.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda)

RoleARN -> (string)

ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination function on your behalf. You need to grant the necessary permissions to this role.

DestinationSchema -> (structure)

Describes the data format when records are written to the destination. For more information, see [Configuring Application Output](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html) .

RecordFormatType -> (string)

Specifies the format of the records on the output stream.

Shorthand Syntax:

```
Name=string,KinesisStreamsOutput={ResourceARN=string,RoleARN=string},KinesisFirehoseOutput={ResourceARN=string,RoleARN=string},LambdaOutput={ResourceARN=string,RoleARN=string},DestinationSchema={RecordFormatType=string} ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "KinesisStreamsOutput": {
      "ResourceARN": "string",
      "RoleARN": "string"
    },
    "KinesisFirehoseOutput": {
      "ResourceARN": "string",
      "RoleARN": "string"
    },
    "LambdaOutput": {
      "ResourceARN": "string",
      "RoleARN": "string"
    },
    "DestinationSchema": {
      "RecordFormatType": "JSON"|"CSV"
    }
  }
  ...
]
```

`--cloud-watch-logging-options` (list)

Use this parameter to configure a CloudWatch log stream to monitor application configuration errors. For more information, see [Working with Amazon CloudWatch Logs](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html) .

(structure)

Provides a description of CloudWatch logging options, including the log stream Amazon Resource Name (ARN) and the role ARN.

LogStreamARN -> (string)

ARN of the CloudWatch log to receive application messages.

RoleARN -> (string)

IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role that is used must have the `PutLogEvents` policy action enabled.

Shorthand Syntax:

```
LogStreamARN=string,RoleARN=string ...
```

JSON Syntax:

```
[
  {
    "LogStreamARN": "string",
    "RoleARN": "string"
  }
  ...
]
```

`--application-code` (string)

One or more SQL statements that read input data, transform it, and generate output. For example, you can write a SQL statement that reads data from one in-application stream, generates a running average of the number of advertisement clicks by vendor, and insert resulting rows in another in-application stream using pumps. For more information about the typical pattern, see [Application Code](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-app-code.html) .

You can provide such series of SQL statements, where output of one statement can be used as the input for the next statement. You store intermediate results by creating in-application streams and pumps.

Note that the application code must create the streams with names specified in the `Outputs` . For example, if your `Outputs` defines output streams named `ExampleOutputStream1` and `ExampleOutputStream2` , then your application code must create these streams.

`--tags` (list)

A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see [Using Tagging](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html) .

(structure)

A key-value pair (the value is optional) that you can define and assign to AWS resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see [Using Tagging](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html) .

Key -> (string)

The key of the key-value tag.

Value -> (string)

The value of the key-value tag. The value is optional.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
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

ApplicationSummary -> (structure)

In response to your `CreateApplication` request, Amazon Kinesis Analytics returns a response with a summary of the application it created, including the application Amazon Resource Name (ARN), name, and status.

ApplicationName -> (string)

Name of the application.

ApplicationARN -> (string)

ARN of the application.

ApplicationStatus -> (string)

Status of the application.