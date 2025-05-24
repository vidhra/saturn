# get-media-pipelineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-media-pipelines/get-media-pipeline.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-media-pipelines/get-media-pipeline.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [chime-sdk-media-pipelines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-media-pipelines/index.html#cli-aws-chime-sdk-media-pipelines) ]

# get-media-pipeline

## Description

Gets an existing media pipeline.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/chime-sdk-media-pipelines-2021-07-15/GetMediaPipeline)

## Synopsis

```
get-media-pipeline
--media-pipeline-id <value>
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

`--media-pipeline-id` (string)

The ID of the pipeline that you want to get.

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

MediaPipeline -> (structure)

The media pipeline object.

MediaCapturePipeline -> (structure)

A pipeline that enables users to capture audio and video.

MediaPipelineId -> (string)

The ID of a media pipeline.

MediaPipelineArn -> (string)

The ARN of the media capture pipeline

SourceType -> (string)

Source type from which media artifacts are saved. You must use `ChimeMeeting` .

SourceArn -> (string)

ARN of the source from which the media artifacts are saved.

Status -> (string)

The status of the media pipeline.

SinkType -> (string)

Destination type to which the media artifacts are saved. You must use an S3 Bucket.

SinkArn -> (string)

ARN of the destination to which the media artifacts are saved.

CreatedTimestamp -> (timestamp)

The time at which the pipeline was created, in ISO 8601 format.

UpdatedTimestamp -> (timestamp)

The time at which the pipeline was updated, in ISO 8601 format.

ChimeSdkMeetingConfiguration -> (structure)

The configuration for a specified media pipeline. `SourceType` must be `ChimeSdkMeeting` .

SourceConfiguration -> (structure)

The source configuration for a specified media pipeline.

SelectedVideoStreams -> (structure)

The selected video streams for a specified media pipeline. The number of video streams canât exceed 25.

AttendeeIds -> (list)

The attendee IDs of the streams selected for a media pipeline.

(string)

ExternalUserIds -> (list)

The external user IDs of the streams selected for a media pipeline.

(string)

ArtifactsConfiguration -> (structure)

The configuration for the artifacts in an Amazon Chime SDK meeting.

Audio -> (structure)

The configuration for the audio artifacts.

MuxType -> (string)

The MUX type of the audio artifact configuration object.

Video -> (structure)

The configuration for the video artifacts.

State -> (string)

Indicates whether the video artifact is enabled or disabled.

MuxType -> (string)

The MUX type of the video artifact configuration object.

Content -> (structure)

The configuration for the content artifacts.

State -> (string)

Indicates whether the content artifact is enabled or disabled.

MuxType -> (string)

The MUX type of the artifact configuration.

CompositedVideo -> (structure)

Enables video compositing.

Layout -> (string)

The layout setting, such as `GridView` in the configuration object.

Resolution -> (string)

The video resolution setting in the configuration object. Default: HD at 1280 x 720. FHD resolution: 1920 x 1080.

GridViewConfiguration -> (structure)

The `GridView` configuration setting.

ContentShareLayout -> (string)

Defines the layout of the video tiles when content sharing is enabled.

PresenterOnlyConfiguration -> (structure)

Defines the configuration options for a presenter only video tile.

PresenterPosition -> (string)

Defines the position of the presenter video tile. Default: `TopRight` .

ActiveSpeakerOnlyConfiguration -> (structure)

The configuration settings for an `ActiveSpeakerOnly` video tile.

ActiveSpeakerPosition -> (string)

The position of the `ActiveSpeakerOnly` video tile.

HorizontalLayoutConfiguration -> (structure)

The configuration settings for a horizontal layout.

TileOrder -> (string)

Sets the automatic ordering of the video tiles.

TilePosition -> (string)

Sets the position of horizontal tiles.

TileCount -> (integer)

The maximum number of video tiles to display.

TileAspectRatio -> (string)

Specifies the aspect ratio of all video tiles.

VerticalLayoutConfiguration -> (structure)

The configuration settings for a vertical layout.

TileOrder -> (string)

Sets the automatic ordering of the video tiles.

TilePosition -> (string)

Sets the position of vertical tiles.

TileCount -> (integer)

The maximum number of tiles to display.

TileAspectRatio -> (string)

Sets the aspect ratio of the video tiles, such as 16:9.

VideoAttribute -> (structure)

The attribute settings for the video tiles.

CornerRadius -> (integer)

Sets the corner radius of all video tiles.

BorderColor -> (string)

Defines the border color of all video tiles.

HighlightColor -> (string)

Defines the highlight color for the active video tile.

BorderThickness -> (integer)

Defines the border thickness for all video tiles.

CanvasOrientation -> (string)

The orientation setting, horizontal or vertical.

SseAwsKeyManagementParams -> (structure)

An object that contains server side encryption parameters to be used by media capture pipeline. The parameters can also be used by media concatenation pipeline taking media capture pipeline as a media source.

AwsKmsKeyId -> (string)

The KMS key you want to use to encrypt your media pipeline output. Decryption is required for concatenation pipeline. If using a key located in the current Amazon Web Services account, you can specify your KMS key in one of four ways:

- Use the KMS key ID itself. For example, `1234abcd-12ab-34cd-56ef-1234567890ab` .
- Use an alias for the KMS key ID. For example, `alias/ExampleAlias` .
- Use the Amazon Resource Name (ARN) for the KMS key ID. For example, `arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab` .
- Use the ARN for the KMS key alias. For example, `arn:aws:kms:region:account-ID:alias/ExampleAlias` .

If using a key located in a different Amazon Web Services account than the current Amazon Web Services account, you can specify your KMS key in one of two ways:

- Use the ARN for the KMS key ID. For example, `arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab` .
- Use the ARN for the KMS key alias. For example, `arn:aws:kms:region:account-ID:alias/ExampleAlias` .

If you donât specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).

Note that the role specified in the `SinkIamRoleArn` request parameter must have permission to use the specified KMS key.

AwsKmsEncryptionContext -> (string)

Base64-encoded string of a UTF-8 encoded JSON, which contains the encryption context as non-secret key-value pair known as encryption context pairs, that provides an added layer of security for your data. For more information, see [KMS encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) and [Asymmetric keys in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *Key Management Service Developer Guide* .

SinkIamRoleArn -> (string)

The Amazon Resource Name (ARN) of the sink role to be used with `AwsKmsKeyId` in `SseAwsKeyManagementParams` .

MediaLiveConnectorPipeline -> (structure)

The connector pipeline of the media pipeline.

Sources -> (list)

The connector pipelineâs data sources.

(structure)

The data source configuration object of a streaming media pipeline.

SourceType -> (string)

The source configurationâs media source type.

ChimeSdkMeetingLiveConnectorConfiguration -> (structure)

The configuration settings of the connector pipeline.

Arn -> (string)

The configuration objectâs Chime SDK meeting ARN.

MuxType -> (string)

The configuration objectâs multiplex type.

CompositedVideo -> (structure)

The media pipelineâs composited video.

Layout -> (string)

The layout setting, such as `GridView` in the configuration object.

Resolution -> (string)

The video resolution setting in the configuration object. Default: HD at 1280 x 720. FHD resolution: 1920 x 1080.

GridViewConfiguration -> (structure)

The `GridView` configuration setting.

ContentShareLayout -> (string)

Defines the layout of the video tiles when content sharing is enabled.

PresenterOnlyConfiguration -> (structure)

Defines the configuration options for a presenter only video tile.

PresenterPosition -> (string)

Defines the position of the presenter video tile. Default: `TopRight` .

ActiveSpeakerOnlyConfiguration -> (structure)

The configuration settings for an `ActiveSpeakerOnly` video tile.

ActiveSpeakerPosition -> (string)

The position of the `ActiveSpeakerOnly` video tile.

HorizontalLayoutConfiguration -> (structure)

The configuration settings for a horizontal layout.

TileOrder -> (string)

Sets the automatic ordering of the video tiles.

TilePosition -> (string)

Sets the position of horizontal tiles.

TileCount -> (integer)

The maximum number of video tiles to display.

TileAspectRatio -> (string)

Specifies the aspect ratio of all video tiles.

VerticalLayoutConfiguration -> (structure)

The configuration settings for a vertical layout.

TileOrder -> (string)

Sets the automatic ordering of the video tiles.

TilePosition -> (string)

Sets the position of vertical tiles.

TileCount -> (integer)

The maximum number of tiles to display.

TileAspectRatio -> (string)

Sets the aspect ratio of the video tiles, such as 16:9.

VideoAttribute -> (structure)

The attribute settings for the video tiles.

CornerRadius -> (integer)

Sets the corner radius of all video tiles.

BorderColor -> (string)

Defines the border color of all video tiles.

HighlightColor -> (string)

Defines the highlight color for the active video tile.

BorderThickness -> (integer)

Defines the border thickness for all video tiles.

CanvasOrientation -> (string)

The orientation setting, horizontal or vertical.

SourceConfiguration -> (structure)

The source configuration settings of the media pipelineâs configuration object.

SelectedVideoStreams -> (structure)

The selected video streams for a specified media pipeline. The number of video streams canât exceed 25.

AttendeeIds -> (list)

The attendee IDs of the streams selected for a media pipeline.

(string)

ExternalUserIds -> (list)

The external user IDs of the streams selected for a media pipeline.

(string)

Sinks -> (list)

The connector pipelineâs data sinks.

(structure)

The media pipelineâs sink configuration settings.

SinkType -> (string)

The sink configurationâs sink type.

RTMPConfiguration -> (structure)

The sink configurationâs RTMP configuration settings.

Url -> (string)

The URL of the RTMP configuration.

AudioChannels -> (string)

The audio channels set for the RTMP configuration

AudioSampleRate -> (string)

The audio sample rate set for the RTMP configuration. Default: 48000.

MediaPipelineId -> (string)

The connector pipelineâs ID.

MediaPipelineArn -> (string)

The connector pipelineâs ARN.

Status -> (string)

The connector pipelineâs status.

CreatedTimestamp -> (timestamp)

The time at which the connector pipeline was created.

UpdatedTimestamp -> (timestamp)

The time at which the connector pipeline was last updated.

MediaConcatenationPipeline -> (structure)

The media concatenation pipeline in a media pipeline.

MediaPipelineId -> (string)

The ID of the media pipeline being concatenated.

MediaPipelineArn -> (string)

The ARN of the media pipeline that you specify in the `SourceConfiguration` object.

Sources -> (list)

The data sources being concatenated.

(structure)

The source type and media pipeline configuration settings in a configuration object.

Type -> (string)

The type of concatenation source in a configuration object.

MediaCapturePipelineSourceConfiguration -> (structure)

The concatenation settings for the media pipeline in a configuration object.

MediaPipelineArn -> (string)

The media pipeline ARN in the configuration object of a media capture pipeline.

ChimeSdkMeetingConfiguration -> (structure)

The meeting configuration settings in a media capture pipeline configuration object.

ArtifactsConfiguration -> (structure)

The configuration for the artifacts in an Amazon Chime SDK meeting concatenation.

Audio -> (structure)

The configuration for the audio artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

Video -> (structure)

The configuration for the video artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

Content -> (structure)

The configuration for the content artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

DataChannel -> (structure)

The configuration for the data channel artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

TranscriptionMessages -> (structure)

The configuration for the transcription messages artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

MeetingEvents -> (structure)

The configuration for the meeting events artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

CompositedVideo -> (structure)

The configuration for the composited video artifacts concatenation.

State -> (string)

Enables or disables the configuration object.

Sinks -> (list)

The data sinks of the concatenation pipeline.

(structure)

The data sink of the configuration object.

Type -> (string)

The type of data sink in the configuration object.

S3BucketSinkConfiguration -> (structure)

The configuration settings for an Amazon S3 bucket sink.

Destination -> (string)

The destination URL of the S3 bucket.

Status -> (string)

The status of the concatenation pipeline.

CreatedTimestamp -> (timestamp)

The time at which the concatenation pipeline was created.

UpdatedTimestamp -> (timestamp)

The time at which the concatenation pipeline was last updated.

MediaInsightsPipeline -> (structure)

The media insights pipeline of a media pipeline.

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

MediaStreamPipeline -> (structure)

Designates a media pipeline as a media stream pipeline.

MediaPipelineId -> (string)

The ID of the media stream pipeline

MediaPipelineArn -> (string)

The ARN of the media stream pipeline.

CreatedTimestamp -> (timestamp)

The time at which the media stream pipeline was created.

UpdatedTimestamp -> (timestamp)

The time at which the media stream pipeline was updated.

Status -> (string)

The status of the media stream pipeline.

Sources -> (list)

The media stream pipelineâs data sources.

(structure)

Structure that contains the settings for media stream sources.

SourceType -> (string)

The type of media stream source.

SourceArn -> (string)

The ARN of the meeting.

Sinks -> (list)

The media stream pipelineâs data sinks.

(structure)

Structure that contains the settings for a media stream sink.

SinkArn -> (string)

The ARN of the Kinesis Video Stream pool returned by the  CreateMediaPipelineKinesisVideoStreamPool API.

SinkType -> (string)

The media stream sinkâs type.

ReservedStreamCapacity -> (integer)

Specifies the number of streams that the sink can accept.

MediaStreamType -> (string)

The media stream sinkâs media stream type.