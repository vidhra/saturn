# get-stream-sessionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-stream-session.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-stream-session.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ivs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/index.html#cli-aws-ivs) ]

# get-stream-session

## Description

Gets metadata on a specified stream.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ivs-2020-07-14/GetStreamSession)

## Synopsis

```
get-stream-session
--channel-arn <value>
[--stream-id <value>]
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

`--channel-arn` (string)

ARN of the channel resource

`--stream-id` (string)

Unique identifier for a live or previously live stream in the specified channel. If no `streamId` is provided, this returns the most recent stream session for the channel, if it exists.

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

**To get metadata for a specified stream**

The following `get-stream-session` example gets the metadata configuration for the specified channel ARN (Amazon Resource Name) and the specified stream; if `streamId` is not provided, the most recent stream for the channel is selected.

```
aws ivs get-stream-session \
    --channel-arn 'arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh' \
    --stream-id 'mystream'
```

Output:

```
{
    "streamSession": {
        "streamId": "mystream1",
        "startTime": "2023-06-26T19:09:28+00:00",
        "channel": {
            "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh",
            "name": "mychannel",
            "latencyMode": "LOW",
            "type": "STANDARD",
            "recordingConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABcdef34ghIJ",
            "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net",
            "playbackUrl": "url-string",
            "authorized": false,
            "insecureIngest": false,
            "preset": ""
        },
        "ingestConfiguration": {
            "audio": {
                "channels": 2,
                "codec": "mp4a.40.2",
                "sampleRate": 8000,
                "targetBitrate": 46875,
                "track": "Track0"
            },
            "video": {
                "avcProfile": "Baseline",
                "avcLevel": "4.2",
                "codec": "avc1.42C02A",
                "encoder": "Lavf58.45.100",
                "level": "4.2",
                "profile": "Baseline",
                "targetBitrate": 8789062,
                "targetFramerate": 60,
                "track": "Track0",
                "videoHeight": 1080,
                "videoWidth": 1920
            }
        },
        "ingestConfigurations": {
            "audioConfigurations": [
                {
                    "channels": 2,
                    "codec": "mp4a.40.2",
                    "sampleRate": 8000,
                    "targetBitrate": 46875,
                    "track": "Track0"
                }
            ],
            "videoConfigurations": [
                {
                    "codec": "avc1.42C02A",
                    "encoder": "Lavf58.45.100",
                    "level": "4.2",
                    "profile": "Baseline",
                    "targetBitrate": 8789062,
                    "targetFramerate": 60,
                    "track": "Track0",
                    "videoHeight": 1080,
                    "videoWidth": 1920
                }
            ]
        },
        "recordingConfiguration": {
            "arn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABcdef34ghIJ",
            "name": "test-recording-config",
            "destinationConfiguration": {
                "s3": {
                    "bucketName": "demo-recording-bucket"
                }
            },
            "state": "ACTIVE",
            "tags": {
                "key1": "value1",
                "key2": "value2"
            },
            "thumbnailConfiguration": {
                "recordingMode": "INTERVAL",
                "targetIntervalSeconds": 1,
                "resolution": "LOWEST_RESOLUTION",
                "storage": [
                    "LATEST"
                ]
            },
            "recordingReconnectWindowSeconds": 60,
            "renditionConfiguration": {
                "renditionSelection": "CUSTOM",
                "renditions": [
                    "HD"
                ]
            }
        },
        "truncatedEvents": [
            {
                "code": "StreamTakeoverInvalidPriority",
                "name": "Stream Takeover Failure",
                "type": "IVS Stream State Change",
                "eventTime": "2023-06-26T19:09:48+00:00"
            },
            {
                "name": "Stream Takeover",
                "type": "IVS Stream State Change",
                "eventTime": "2023-06-26T19:09:47+00:00"
            },
            {
                "name": "Recording Start",
                "type": "IVS Recording State Change",
                "eventTime": "2023-06-26T19:09:35+00:00"
            },
            {
                "name": "Stream Start",
                "type": "IVS Stream State Change",
                "eventTime": "2023-06-26T19:09:34+00:00"
            },
            {
                "name": "Session Created",
                "type": "IVS Stream State Change",
                "eventTime": "2023-06-26T19:09:28+00:00"
            }
        ]
    }
}
```

For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html) in the *IVS Low-Latency User Guide*.

## Output

streamSession -> (structure)

List of stream details.

channel -> (structure)

The properties of the channel at the time of going live.

arn -> (string)

Channel ARN.

authorized -> (boolean)

Whether the channel is private (enabled for playback authorization). Default: `false` .

containerFormat -> (string)

Indicates which content-packaging format is used (MPEG-TS or fMP4). If `multitrackInputConfiguration` is specified and `enabled` is `true` , then `containerFormat` is required and must be set to `FRAGMENTED_MP4` . Otherwise, `containerFormat` may be set to `TS` or `FRAGMENTED_MP4` . Default: `TS` .

ingestEndpoint -> (string)

Channel ingest endpoint, part of the definition of an ingest server, used when you set up streaming software.

insecureIngest -> (boolean)

Whether the channel allows insecure RTMP ingest. Default: `false` .

latencyMode -> (string)

Channel latency mode. Use `NORMAL` to broadcast and deliver live video up to Full HD. Use `LOW` for near-real-time interaction with viewers. Default: `LOW` .

multitrackInputConfiguration -> (structure)

Object specifying multitrack input configuration. Default: no multitrack input configuration is specified.

enabled -> (boolean)

Indicates whether multitrack input is enabled. Can be set to `true` only if channel type is `STANDARD` . Setting `enabled` to `true` with any other channel type will cause an exception. If `true` , then `policy` , `maximumResolution` , and `containerFormat` are required, and `containerFormat` must be set to `FRAGMENTED_MP4` . Default: `false` .

maximumResolution -> (string)

Maximum resolution for multitrack input. Required if `enabled` is `true` .

policy -> (string)

Indicates whether multitrack input is allowed or required. Required if `enabled` is `true` .

name -> (string)

Channel name.

playbackRestrictionPolicyArn -> (string)

Playback-restriction-policy ARN. A valid ARN value here both specifies the ARN and enables playback restriction. Default: ââ (empty string, no playback restriction policy is applied).

playbackUrl -> (string)

Channel playback URL.

preset -> (string)

Optional transcode preset for the channel. This is selectable only for `ADVANCED_HD` and `ADVANCED_SD` channel types. For those channel types, the default `preset` is `HIGHER_BANDWIDTH_DELIVERY` . For other channel types (`BASIC` and `STANDARD` ), `preset` is the empty string (`""` ).

recordingConfigurationArn -> (string)

Recording-configuration ARN. A valid ARN value here both specifies the ARN and enables recording. Default: ââ (empty string, recording is disabled).

srt -> (structure)

Specifies the endpoint and optional passphrase for streaming with the SRT protocol.

endpoint -> (string)

The endpoint to be used when streaming with IVS using the SRT protocol.

passphrase -> (string)

Auto-generated passphrase to enable encryption. This field is applicable only if the end user has *not* enabled the `insecureIngest` option for the channel.

tags -> (map)

Tags attached to the resource. Array of 1-50 maps, each of the form `string:string (key:value)` . See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging Amazon Web Services Resources and Tag Editor* for details, including restrictions that apply to tags and âTag naming limits and requirementsâ; Amazon IVS has no service-specific constraints beyond what is documented there.

key -> (string)

value -> (string)

type -> (string)

Channel type, which determines the allowable resolution and bitrate. *If you exceed the allowable input resolution or bitrate, the stream probably will disconnect immediately.* Default: `STANDARD` . For details, see [Channel Types](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/channel-types.html) .

endTime -> (timestamp)

Time when the channel went offline. This is an ISO 8601 timestamp; *note that this is returned as a string* . For live streams, this is `NULL` .

ingestConfiguration -> (structure)

The properties of the incoming RTMP stream.

**Note:** `ingestConfiguration` is deprecated in favor of `ingestConfigurations` but retained to ensure backward compatibility. If multitrack is not enabled, `ingestConfiguration` and `ingestConfigurations` contain the same data, namely information about track0 (the sole track). If multitrack is enabled, `ingestConfiguration` contains data for only the first track (track0) and `ingestConfigurations` contains data for all tracks.

audio -> (structure)

Encoder settings for audio.

channels -> (long)

Number of audio channels.

codec -> (string)

Codec used for the audio encoding.

sampleRate -> (long)

Number of audio samples recorded per second.

targetBitrate -> (long)

The expected ingest bitrate (bits per second). This is configured in the encoder.

track -> (string)

Name of the audio track (if the stream has an audio track). If multitrack is not enabled, this is track0 (the sole track).

video -> (structure)

Encoder settings for video.

avcLevel -> (string)

Indicates the degree of required decoder performance for a profile. Normally this is set automatically by the encoder. For details, see the H.264 specification.

avcProfile -> (string)

Indicates to the decoder the requirements for decoding the stream. For definitions of the valid values, see the H.264 specification.

codec -> (string)

Codec used for the video encoding.

encoder -> (string)

Software or hardware used to encode the video.

level -> (string)

Indicates the degree of required decoder performance for a profile. Normally this is set automatically by the encoder. When an AVC codec is used, this field has the same value as `avcLevel` .

profile -> (string)

Indicates to the decoder the requirements for decoding the stream. When an AVC codec is used, this field has the same value as `avcProfile` .

targetBitrate -> (long)

The expected ingest bitrate (bits per second). This is configured in the encoder.

targetFramerate -> (long)

The expected ingest framerate. This is configured in the encoder.

track -> (string)

Name of the video track. If multitrack is not enabled, this is track0 (the sole track).

videoHeight -> (long)

Video-resolution height in pixels.

videoWidth -> (long)

Video-resolution width in pixels.

ingestConfigurations -> (structure)

The properties of the incoming RTMP stream. If multitrack is enabled, `ingestConfigurations` contains data for all tracks; otherwise, it contains data only for track0 (the sole track).

audioConfigurations -> (list)

Encoder settings for audio.

(structure)

Object specifying a streamâs audio configuration, as set up by the broadcaster (usually in an encoder). This is part of the  IngestConfigurations object and the deprecated  IngestConfiguration object. It is used for monitoring stream health.

channels -> (long)

Number of audio channels.

codec -> (string)

Codec used for the audio encoding.

sampleRate -> (long)

Number of audio samples recorded per second.

targetBitrate -> (long)

The expected ingest bitrate (bits per second). This is configured in the encoder.

track -> (string)

Name of the audio track (if the stream has an audio track). If multitrack is not enabled, this is track0 (the sole track).

videoConfigurations -> (list)

Encoder settings for video

(structure)

Object specifying a streamâs video configuration, as set up by the broadcaster (usually in an encoder). This is part of the  IngestConfigurations object and the deprecated  IngestConfiguration object. It is used for monitoring stream health.

avcLevel -> (string)

Indicates the degree of required decoder performance for a profile. Normally this is set automatically by the encoder. For details, see the H.264 specification.

avcProfile -> (string)

Indicates to the decoder the requirements for decoding the stream. For definitions of the valid values, see the H.264 specification.

codec -> (string)

Codec used for the video encoding.

encoder -> (string)

Software or hardware used to encode the video.

level -> (string)

Indicates the degree of required decoder performance for a profile. Normally this is set automatically by the encoder. When an AVC codec is used, this field has the same value as `avcLevel` .

profile -> (string)

Indicates to the decoder the requirements for decoding the stream. When an AVC codec is used, this field has the same value as `avcProfile` .

targetBitrate -> (long)

The expected ingest bitrate (bits per second). This is configured in the encoder.

targetFramerate -> (long)

The expected ingest framerate. This is configured in the encoder.

track -> (string)

Name of the video track. If multitrack is not enabled, this is track0 (the sole track).

videoHeight -> (long)

Video-resolution height in pixels.

videoWidth -> (long)

Video-resolution width in pixels.

recordingConfiguration -> (structure)

The properties of recording the live stream.

arn -> (string)

Recording-configuration ARN.

destinationConfiguration -> (structure)

A complex type that contains information about where recorded video will be stored.

s3 -> (structure)

An S3 destination configuration where recorded videos will be stored.

bucketName -> (string)

Location (S3 bucket name) where recorded videos will be stored.

name -> (string)

Recording-configuration name. The value does not need to be unique.

recordingReconnectWindowSeconds -> (integer)

If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together. Default: 0.

renditionConfiguration -> (structure)

Object that describes which renditions should be recorded for a stream.

renditionSelection -> (string)

Indicates which set of renditions are recorded for a stream. For `BASIC` channels, the `CUSTOM` value has no effect. If `CUSTOM` is specified, a set of renditions must be specified in the `renditions` field. Default: `ALL` .

renditions -> (list)

Indicates which renditions are recorded for a stream, if `renditionSelection` is `CUSTOM` ; otherwise, this field is irrelevant. The selected renditions are recorded if they are available during the stream. If a selected rendition is unavailable, the best available rendition is recorded. For details on the resolution dimensions of each rendition, see [Auto-Record to Amazon S3](https://docs.aws.amazon.com/ivs/latest/userguide/record-to-s3.html) .

(string)

state -> (string)

Indicates the current state of the recording configuration. When the state is `ACTIVE` , the configuration is ready for recording a channel stream.

tags -> (map)

Tags attached to the resource. Array of 1-50 maps, each of the form `string:string (key:value)` . See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging Amazon Web Services Resources and Tag Editor* for details, including restrictions that apply to tags and âTag naming limits and requirementsâ; Amazon IVS has no service-specific constraints beyond what is documented there.

key -> (string)

value -> (string)

thumbnailConfiguration -> (structure)

A complex type that allows you to enable/disable the recording of thumbnails for a live session and modify the interval at which thumbnails are generated for the live session.

recordingMode -> (string)

Thumbnail recording mode. Default: `INTERVAL` .

resolution -> (string)

Indicates the desired resolution of recorded thumbnails. Thumbnails are recorded at the selected resolution if the corresponding rendition is available during the stream; otherwise, they are recorded at source resolution. For more information about resolution values and their corresponding height and width dimensions, see [Auto-Record to Amazon S3](https://docs.aws.amazon.com/ivs/latest/userguide/record-to-s3.html) . Default: Null (source resolution is returned).

storage -> (list)

Indicates the format in which thumbnails are recorded. `SEQUENTIAL` records all generated thumbnails in a serial manner, to the media/thumbnails directory. `LATEST` saves the latest thumbnail in media/latest_thumbnail/thumb.jpg and overwrites it at the interval specified by `targetIntervalSeconds` . You can enable both `SEQUENTIAL` and `LATEST` . Default: `SEQUENTIAL` .

(string)

targetIntervalSeconds -> (long)

The targeted thumbnail-generation interval in seconds. This is configurable (and required) only if `recordingMode` is `INTERVAL` . Default: 60.

**Important:** For the `BASIC` channel type, or the `STANDARD` channel type with multitrack input, setting a value for `targetIntervalSeconds` does not guarantee that thumbnails are generated at the specified interval. For thumbnails to be generated at the `targetIntervalSeconds` interval, the `IDR/Keyframe` value for the input video must be less than the `targetIntervalSeconds` value. See [Amazon IVS Streaming Configuration](https://docs.aws.amazon.com/ivs/latest/userguide/streaming-config.html) for information on setting `IDR/Keyframe` to the recommended value in video-encoder settings.

startTime -> (timestamp)

Time when the channel went live. This is an ISO 8601 timestamp; *note that this is returned as a string* .

streamId -> (string)

Unique identifier for a live or previously live stream in the specified channel.

truncatedEvents -> (list)

List of Amazon IVS events that the stream encountered. The list is sorted by most recent events and contains up to 500 events. For Amazon IVS events, see [Using Amazon EventBridge with Amazon IVS](https://docs.aws.amazon.com/ivs/latest/userguide/eventbridge.html) .

(structure)

Object specifying a streamâs events. For a list of events, see [Using Amazon EventBridge with Amazon IVS](https://docs.aws.amazon.com/ivs/latest/userguide/eventbridge.html) .

code -> (string)

Provides additional details about the stream event. There are several values; the long descriptions are provided in the IVS console but not delivered through the IVS API or EventBridge. Multitrack-related codes are used only for certain Session Ended events.

- `MultitrackInputNotAllowed` â The broadcast client attempted to connect with multitrack input, but multitrack input was not enabled on the channel. Check your broadcast software settings or set `MultitrackInputConfiguration.Policy` to `ALLOW` or `REQUIRE` .
- `MultitrackInputRequired` â The broadcast client attempted to connect with single-track video, but multitrack input is required on this channel. Enable multitrack video in your broadcast software or configure the channelâs `MultitrackInputConfiguration.Policy` to `ALLOW` .
- `InvalidGetClientConfigurationStreamKey` â The broadcast client attempted to connect with an invalid, expired, or corrupt stream key.
- `GetClientConfigurationStreamKeyRequired` â The broadcast client attempted to stream multitrack video without providing an authenticated stream key from GetClientConfiguration.
- `InvalidMultitrackInputTrackCount` â The multitrack input stream contained an invalid number of tracks.
- `InvalidMultitrackInputVideoTrackMediaProperties` â The multitrack input stream contained one or more tracks with an invalid codec, resolution, bitrate, or framerate.
- `StreamTakeoverMediaMismatch` â The broadcast client attempted to take over with different media properties (e.g., codec, resolution, or video track type) from the original stream.
- `StreamTakeoverInvalidPriority` â The broadcast client attempted a takeover with either a priority integer value equal to or lower than the original streamâs value or a value outside the allowed range of 1 to 2,147,483,647.  `StreamTakeoverLimitBreached` â The broadcast client reached the maximum allowed takeover attempts for this stream.

eventTime -> (timestamp)

Time when the event occurred. This is an ISO 8601 timestamp; *note that this is returned as a string* .

name -> (string)

Name that identifies the stream event within a `type` .

type -> (string)

Logical group for certain events.