# start-stream-processorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-stream-processor.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-stream-processor.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# start-stream-processor

## Description

Starts processing a stream processor. You create a stream processor by calling  CreateStreamProcessor . To tell `StartStreamProcessor` which stream processor to start, use the value of the `Name` field specified in the call to `CreateStreamProcessor` .

If you are using a label detection stream processor to detect labels, you need to provide a `Start selector` and a `Stop selector` to determine the length of the stream processing time.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartStreamProcessor)

## Synopsis

```
start-stream-processor
--name <value>
[--start-selector <value>]
[--stop-selector <value>]
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

`--name` (string)

The name of the stream processor to start processing.

`--start-selector` (structure)

Specifies the starting point in the Kinesis stream to start processing. You can use the producer timestamp or the fragment number. If you use the producer timestamp, you must put the time in milliseconds. For more information about fragment numbers, see [Fragment](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_Fragment.html) .

This is a required parameter for label detection stream processors and should not be used to start a face search stream processor.

KVSStreamStartSelector -> (structure)

Specifies the starting point in the stream to start processing. This can be done with a producer timestamp or a fragment number in a Kinesis stream.

ProducerTimestamp -> (long)

The timestamp from the producer corresponding to the fragment, in milliseconds, expressed in unix time format.

FragmentNumber -> (string)

The unique identifier of the fragment. This value monotonically increases based on the ingestion order.

Shorthand Syntax:

```
KVSStreamStartSelector={ProducerTimestamp=long,FragmentNumber=string}
```

JSON Syntax:

```
{
  "KVSStreamStartSelector": {
    "ProducerTimestamp": long,
    "FragmentNumber": "string"
  }
}
```

`--stop-selector` (structure)

Specifies when to stop processing the stream. You can specify a maximum amount of time to process the video.

This is a required parameter for label detection stream processors and should not be used to start a face search stream processor.

MaxDurationInSeconds -> (long)

Specifies the maximum amount of time in seconds that you want the stream to be processed. The largest amount of time is 2 minutes. The default is 10 seconds.

Shorthand Syntax:

```
MaxDurationInSeconds=long
```

JSON Syntax:

```
{
  "MaxDurationInSeconds": long
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To start a stream processor**

The following `start-stream-processor` command starts the specified video stream processor.

```
aws rekognition start-stream-processor \
    --name my-stream-processor
```

This command produces no output.

For more information, see [Working with Streaming Videos](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video.html) in the *Amazon Rekognition Developer Guide*.

## Output

SessionId -> (string)

A unique identifier for the stream processing session.