# describe-flow-source-metadataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/describe-flow-source-metadata.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/describe-flow-source-metadata.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediaconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/index.html#cli-aws-mediaconnect) ]

# describe-flow-source-metadata

## Description

The `DescribeFlowSourceMetadata` API is used to view information about the flowâs source transport stream and programs. This API displays status messages about the flowâs source as well as details about the programâs video, audio, and other data.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/DescribeFlowSourceMetadata)

## Synopsis

```
describe-flow-source-metadata
--flow-arn <value>
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

`--flow-arn` (string)

The Amazon Resource Name (ARN) of the flow.

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

FlowArn -> (string)

The ARN of the flow that DescribeFlowSourceMetadata was performed on.

Messages -> (list)

Provides a status code and message regarding issues found with the flow source metadata.

(structure)

The details of an error message.

Code -> (string)

The error code.

Message -> (string)

The specific error message that MediaConnect returns to help you understand the reason that the request did not succeed.

ResourceName -> (string)

The name of the resource.

Timestamp -> (timestamp)

The timestamp of the most recent change in metadata for this flowâs source.

TransportMediaInfo -> (structure)

Information about the flowâs transport media.

Programs -> (list)

The list of transport stream programs in the current flowâs source.

(structure)

The metadata of a single transport stream program.

PcrPid -> (integer)

The Program Clock Reference (PCR) Packet ID (PID) as it is reported in the Program Association Table.

ProgramName -> (string)

The program name as it is reported in the Program Association Table.

ProgramNumber -> (integer)

The program number as it is reported in the Program Association Table.

ProgramPid -> (integer)

The program Packet ID (PID) as it is reported in the Program Association Table.

Streams -> (list)

The list of elementary transport streams in the program. The list includes video, audio, and data streams.

(structure)

The metadata of an elementary transport stream.

Channels -> (integer)

The number of channels in the audio stream.

Codec -> (string)

The codec used by the stream.

FrameRate -> (string)

The frame rate used by the video stream.

FrameResolution -> (structure)

The frame resolution used by the video stream.

FrameHeight -> (integer)

The number of pixels in the height of the video frame.

FrameWidth -> (integer)

The number of pixels in the width of the video frame.

Pid -> (integer)

The Packet ID (PID) as it is reported in the Program Map Table.

SampleRate -> (integer)

The sample rate used by the audio stream.

SampleSize -> (integer)

The sample bit size used by the audio stream.

StreamType -> (string)

The Stream Type as it is reported in the Program Map Table.