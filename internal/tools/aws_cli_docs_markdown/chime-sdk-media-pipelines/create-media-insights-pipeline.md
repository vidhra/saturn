# create-media-insights-pipelineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-media-pipelines/create-media-insights-pipeline.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-media-pipelines/create-media-insights-pipeline.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [chime-sdk-media-pipelines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-media-pipelines/index.html#cli-aws-chime-sdk-media-pipelines) ]

# create-media-insights-pipeline

## Description

Creates a media insights pipeline.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/chime-sdk-media-pipelines-2021-07-15/CreateMediaInsightsPipeline)

## Synopsis

```
create-media-insights-pipeline
--media-insights-pipeline-configuration-arn <value>
[--kinesis-video-stream-source-runtime-configuration <value>]
[--media-insights-runtime-metadata <value>]
[--kinesis-video-stream-recording-source-runtime-configuration <value>]
[--s3-recording-sink-runtime-configuration <value>]
[--tags <value>]
[--client-request-token <value>]
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

`--media-insights-pipeline-configuration-arn` (string)

The ARN of the pipelineâs configuration.

`--kinesis-video-stream-source-runtime-configuration` (structure)

The runtime configuration for the Kinesis video stream source of the media insights pipeline.

Streams -> (list)

The streams in the source runtime configuration of a Kinesis video stream.

(structure)

The configuration settings for a stream.

StreamArn -> (string)

The ARN of the stream.

FragmentNumber -> (string)

The unique identifier of the fragment to begin processing.

StreamChannelDefinition -> (structure)

The streaming channel definition in the stream configuration.

NumberOfChannels -> (integer)

The number of channels in a streaming channel.

ChannelDefinitions -> (list)

The definitions of the channels in a streaming channel.

(structure)

Defines an audio channel in a Kinesis video stream.

ChannelId -> (integer)

The channel ID.

ParticipantRole -> (string)

Specifies whether the audio in a channel belongs to the `AGENT` or `CUSTOMER` .

MediaEncoding -> (string)

Specifies the encoding of your input audio. Supported format: PCM (only signed 16-bit little-endian audio formats, which does not include WAV)

For more information, see [Media formats](https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio) in the *Amazon Transcribe Developer Guide* .

MediaSampleRate -> (integer)

The sample rate of the input audio (in hertz). Low-quality audio, such as telephone audio, is typically around 8,000 Hz. High-quality audio typically ranges from 16,000 Hz to 48,000 Hz. Note that the sample rate you specify must match that of your audio.

Valid Range: Minimum value of 8000. Maximum value of 48000.

JSON Syntax:

```
{
  "Streams": [
    {
      "StreamArn": "string",
      "FragmentNumber": "string",
      "StreamChannelDefinition": {
        "NumberOfChannels": integer,
        "ChannelDefinitions": [
          {
            "ChannelId": integer,
            "ParticipantRole": "AGENT"|"CUSTOMER"
          }
          ...
        ]
      }
    }
    ...
  ],
  "MediaEncoding": "pcm",
  "MediaSampleRate": integer
}
```

`--media-insights-runtime-metadata` (map)

The runtime metadata for the media insights pipeline. Consists of a key-value map of strings.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--kinesis-video-stream-recording-source-runtime-configuration` (structure)

The runtime configuration for the Kinesis video recording stream source.

Streams -> (list)

The stream or streams to be recorded.

(structure)

A structure that holds the settings for recording media.

StreamArn -> (string)

The ARN of the recording stream.

FragmentSelector -> (structure)

Describes the timestamp range and timestamp origin of a range of fragments in the Kinesis video stream.

FragmentSelectorType -> (string)

The origin of the timestamps to use, `Server` or `Producer` . For more information, see [StartSelectorType](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_StartSelector.html) in the *Amazon Kinesis Video Streams Developer Guide* .

TimestampRange -> (structure)

The range of timestamps to return.

StartTimestamp -> (timestamp)

The starting timestamp for the specified range.

EndTimestamp -> (timestamp)

The ending timestamp for the specified range.

Shorthand Syntax:

```
Streams=[{StreamArn=string},{StreamArn=string}],FragmentSelector={FragmentSelectorType=string,TimestampRange={StartTimestamp=timestamp,EndTimestamp=timestamp}}
```

JSON Syntax:

```
{
  "Streams": [
    {
      "StreamArn": "string"
    }
    ...
  ],
  "FragmentSelector": {
    "FragmentSelectorType": "ProducerTimestamp"|"ServerTimestamp",
    "TimestampRange": {
      "StartTimestamp": timestamp,
      "EndTimestamp": timestamp
    }
  }
}
```

`--s3-recording-sink-runtime-configuration` (structure)

The runtime configuration for the S3 recording sink. If specified, the settings in this structure override any settings in `S3RecordingSinkConfiguration` .

Destination -> (string)

The URI of the S3 bucket used as the sink.

RecordingFileFormat -> (string)

The file format for the media files sent to the Amazon S3 bucket.

Shorthand Syntax:

```
Destination=string,RecordingFileFormat=string
```

JSON Syntax:

```
{
  "Destination": "string",
  "RecordingFileFormat": "Wav"|"Opus"
}
```

`--tags` (list)

The tags assigned to the media insights pipeline.

(structure)

A key/value pair that grants users access to meeting resources.

Key -> (string)

The key half of a tag.

Value -> (string)

The value half of a tag.

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

`--client-request-token` (string)

The unique identifier for the media insights pipeline request.

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

MediaInsightsPipeline -> (structure)

The media insights pipeline object.

MediaPipelineId -> (string)

The ID of a media insights pipeline.

MediaPipelineArn -> (string)

The ARN of a media insights pipeline.

MediaInsightsPipelineConfigurationArn -> (string)

The ARN of a media insight pipelineâs configuration settings.

Status -> (string)

The status of a media insights pipeline.

KinesisVideoStreamSourceRuntimeConfiguration -> (structure)

The configuration settings for a Kinesis runtime video stream in a media insights pipeline.

Streams -> (list)

The streams in the source runtime configuration of a Kinesis video stream.

(structure)

The configuration settings for a stream.

StreamArn -> (string)

The ARN of the stream.

FragmentNumber -> (string)

The unique identifier of the fragment to begin processing.

StreamChannelDefinition -> (structure)

The streaming channel definition in the stream configuration.

NumberOfChannels -> (integer)

The number of channels in a streaming channel.

ChannelDefinitions -> (list)

The definitions of the channels in a streaming channel.

(structure)

Defines an audio channel in a Kinesis video stream.

ChannelId -> (integer)

The channel ID.

ParticipantRole -> (string)

Specifies whether the audio in a channel belongs to the `AGENT` or `CUSTOMER` .

MediaEncoding -> (string)

Specifies the encoding of your input audio. Supported format: PCM (only signed 16-bit little-endian audio formats, which does not include WAV)

For more information, see [Media formats](https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio) in the *Amazon Transcribe Developer Guide* .

MediaSampleRate -> (integer)

The sample rate of the input audio (in hertz). Low-quality audio, such as telephone audio, is typically around 8,000 Hz. High-quality audio typically ranges from 16,000 Hz to 48,000 Hz. Note that the sample rate you specify must match that of your audio.

Valid Range: Minimum value of 8000. Maximum value of 48000.

MediaInsightsRuntimeMetadata -> (map)

The runtime metadata of a media insights pipeline.

key -> (string)

value -> (string)

KinesisVideoStreamRecordingSourceRuntimeConfiguration -> (structure)

The runtime configuration settings for a Kinesis recording video stream in a media insights pipeline.

Streams -> (list)

The stream or streams to be recorded.

(structure)

A structure that holds the settings for recording media.

StreamArn -> (string)

The ARN of the recording stream.

FragmentSelector -> (structure)

Describes the timestamp range and timestamp origin of a range of fragments in the Kinesis video stream.

FragmentSelectorType -> (string)

The origin of the timestamps to use, `Server` or `Producer` . For more information, see [StartSelectorType](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_StartSelector.html) in the *Amazon Kinesis Video Streams Developer Guide* .

TimestampRange -> (structure)

The range of timestamps to return.

StartTimestamp -> (timestamp)

The starting timestamp for the specified range.

EndTimestamp -> (timestamp)

The ending timestamp for the specified range.

S3RecordingSinkRuntimeConfiguration -> (structure)

The runtime configuration of the Amazon S3 bucket that stores recordings in a media insights pipeline.

Destination -> (string)

The URI of the S3 bucket used as the sink.

RecordingFileFormat -> (string)

The file format for the media files sent to the Amazon S3 bucket.

CreatedTimestamp -> (timestamp)

The time at which the media insights pipeline was created.

ElementStatuses -> (list)

The statuses that the elements in a media insights pipeline can have during data processing.

(structure)

The status of the pipeline element.

Type -> (string)

The type of status.

Status -> (string)

The elementâs status.