# add-application-outputÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/add-application-output.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/add-application-output.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kinesisanalyticsv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/index.html#cli-aws-kinesisanalyticsv2) ]

# add-application-output

## Description

Adds an external destination to your SQL-based Kinesis Data Analytics application.

If you want Kinesis Data Analytics to deliver data from an in-application stream within your application to an external destination (such as an Kinesis data stream, a Kinesis Data Firehose delivery stream, or an Amazon Lambda function), you add the relevant configuration to your application using this operation. You can configure one or more outputs for your application. Each output configuration maps an in-application stream and an external destination.

You can use one of the output configurations to deliver data from your in-application error stream to an external destination so that you can analyze the errors.

Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the  DescribeApplication operation to find the current application version.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/AddApplicationOutput)

## Synopsis

```
add-application-output
--application-name <value>
--current-application-version-id <value>
--application-output <value>
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

The name of the application to which you want to add the output configuration.

`--current-application-version-id` (long)

The version of the application to which you want to add the output configuration. You can use the  DescribeApplication operation to get the current application version. If the version specified is not the current version, the `ConcurrentModificationException` is returned.

`--application-output` (structure)

An array of objects, each describing one output configuration. In the output configuration, you specify the name of an in-application stream, a destination (that is, a Kinesis data stream, a Kinesis Data Firehose delivery stream, or an Amazon Lambda function), and record the formation to use when writing to the destination.

Name -> (string)

The name of the in-application stream.

KinesisStreamsOutput -> (structure)

Identifies a Kinesis data stream as the destination.

ResourceARN -> (string)

The ARN of the destination Kinesis data stream to write to.

KinesisFirehoseOutput -> (structure)

Identifies a Kinesis Data Firehose delivery stream as the destination.

ResourceARN -> (string)

The ARN of the destination delivery stream to write to.

LambdaOutput -> (structure)

Identifies an Amazon Lambda function as the destination.

ResourceARN -> (string)

The Amazon Resource Name (ARN) of the destination Lambda function to write to.

### Note

To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see [Example ARNs: Amazon Lambda](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda)

DestinationSchema -> (structure)

Describes the data format when records are written to the destination.

RecordFormatType -> (string)

Specifies the format of the records on the output stream.

Shorthand Syntax:

```
Name=string,KinesisStreamsOutput={ResourceARN=string},KinesisFirehoseOutput={ResourceARN=string},LambdaOutput={ResourceARN=string},DestinationSchema={RecordFormatType=string}
```

JSON Syntax:

```
{
  "Name": "string",
  "KinesisStreamsOutput": {
    "ResourceARN": "string"
  },
  "KinesisFirehoseOutput": {
    "ResourceARN": "string"
  },
  "LambdaOutput": {
    "ResourceARN": "string"
  },
  "DestinationSchema": {
    "RecordFormatType": "JSON"|"CSV"
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

OutputDescriptions -> (list)

Describes the application output configuration. For more information, see [Configuring Application Output](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html) .

(structure)

For a SQL-based Kinesis Data Analytics application, describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

OutputId -> (string)

A unique identifier for the output configuration.

Name -> (string)

The name of the in-application stream that is configured as output.

KinesisStreamsOutputDescription -> (structure)

Describes the Kinesis data stream that is configured as the destination where output is written.

ResourceARN -> (string)

The Amazon Resource Name (ARN) of the Kinesis data stream.

RoleARN -> (string)

The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

### Note

Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.

KinesisFirehoseOutputDescription -> (structure)

Describes the Kinesis Data Firehose delivery stream that is configured as the destination where output is written.

ResourceARN -> (string)

The Amazon Resource Name (ARN) of the delivery stream.

RoleARN -> (string)

The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

### Note

Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.

LambdaOutputDescription -> (structure)

Describes the Lambda function that is configured as the destination where output is written.

ResourceARN -> (string)

The Amazon Resource Name (ARN) of the destination Lambda function.

RoleARN -> (string)

The ARN of the IAM role that Kinesis Data Analytics can assume to write to the destination function.

### Note

Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.

DestinationSchema -> (structure)

The data format used for writing data to the destination.

RecordFormatType -> (string)

Specifies the format of the records on the output stream.