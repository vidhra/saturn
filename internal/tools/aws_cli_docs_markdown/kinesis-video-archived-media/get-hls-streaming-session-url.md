# get-hls-streaming-session-urlÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis-video-archived-media/get-hls-streaming-session-url.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis-video-archived-media/get-hls-streaming-session-url.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kinesis-video-archived-media](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis-video-archived-media/index.html#cli-aws-kinesis-video-archived-media) ]

# get-hls-streaming-session-url

## Description

Retrieves an HTTP Live Streaming (HLS) URL for the stream. You can then open the URL in a browser or media player to view the stream contents.

Both the `StreamName` and the `StreamARN` parameters are optional, but you must specify either the `StreamName` or the `StreamARN` when invoking this API operation.

An Amazon Kinesis video stream has the following requirements for providing data through HLS:

- For streaming video, the media must contain H.264 or H.265 encoded video and, optionally, AAC encoded audio. Specifically, the codec ID of track 1 should be `V_MPEG/ISO/AVC` (for H.264) or `V_MPEG/ISO/HEVC` (for H.265). Optionally, the codec ID of track 2 should be `A_AAC` . For audio only streaming, the codec ID of track 1 should be `A_AAC` .
- Data retention must be greater than 0.
- The video track of each fragment must contain codec private data in the Advanced Video Coding (AVC) for H.264 format or HEVC for H.265 format ([MPEG-4 specification ISO/IEC 14496-15](https://www.iso.org/standard/55980.html) ). For information about adapting stream data to a given format, see [NAL Adaptation Flags](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-reference-nal.html) .
- The audio track (if present) of each fragment must contain codec private data in the AAC format ([AAC specification ISO/IEC 13818-7](https://www.iso.org/standard/43345.html) ).

Kinesis Video Streams HLS sessions contain fragments in the fragmented MPEG-4 form (also called fMP4 or CMAF) or the MPEG-2 form (also called TS chunks, which the HLS specification also supports). For more information about HLS fragment types, see the [HLS specification](https://tools.ietf.org/html/draft-pantos-http-live-streaming-23) .

The following procedure shows how to use HLS with Kinesis Video Streams:

- Get an endpoint using [GetDataEndpoint](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_GetDataEndpoint.html) , specifying `GET_HLS_STREAMING_SESSION_URL` for the `APIName` parameter.
- Retrieve the HLS URL using `GetHLSStreamingSessionURL` . Kinesis Video Streams creates an HLS streaming session to be used for accessing content in a stream using the HLS protocol. `GetHLSStreamingSessionURL` returns an authenticated URL (that includes an encrypted session token) for the sessionâs HLS *master playlist* (the root resource needed for streaming with HLS).

### Note

Donât share or store this token where an unauthorized entity could access it. The token provides access to the content of the stream. Safeguard the token with the same measures that you would use with your Amazon Web Services credentials.

The media that is made available through the playlist consists only of the requested stream, time range, and format. No other media data (such as frames outside the requested window or alternate bitrates) is made available.

- Provide the URL (containing the encrypted session token) for the HLS master playlist to a media player that supports the HLS protocol. Kinesis Video Streams makes the HLS media playlist, initialization fragment, and media fragments available through the master playlist URL. The initialization fragment contains the codec private data for the stream, and other data needed to set up the video or audio decoder and renderer. The media fragments contain H.264-encoded video frames or AAC-encoded audio samples.
- The media player receives the authenticated URL and requests stream metadata and media data normally. When the media player requests data, it calls the following actions:

- **GetHLSMasterPlaylist:** Retrieves an HLS master playlist, which contains a URL for the `GetHLSMediaPlaylist` action for each track, and additional metadata for the media player, including estimated bitrate and resolution.
- **GetHLSMediaPlaylist:** Retrieves an HLS media playlist, which contains a URL to access the MP4 initialization fragment with the `GetMP4InitFragment` action, and URLs to access the MP4 media fragments with the `GetMP4MediaFragment` actions. The HLS media playlist also contains metadata about the stream that the player needs to play it, such as whether the `PlaybackMode` is `LIVE` or `ON_DEMAND` . The HLS media playlist is typically static for sessions with a `PlaybackType` of `ON_DEMAND` . The HLS media playlist is continually updated with new fragments for sessions with a `PlaybackType` of `LIVE` . There is a distinct HLS media playlist for the video track and the audio track (if applicable) that contains MP4 media URLs for the specific track.
- **GetMP4InitFragment:** Retrieves the MP4 initialization fragment. The media player typically loads the initialization fragment before loading any media fragments. This fragment contains the â`fytp` â and â`moov` â MP4 atoms, and the child atoms that are needed to initialize the media player decoder. The initialization fragment does not correspond to a fragment in a Kinesis video stream. It contains only the codec private data for the stream and respective track, which the media player needs to decode the media frames.
- **GetMP4MediaFragment:** Retrieves MP4 media fragments. These fragments contain the â`moof` â and â`mdat` â MP4 atoms and their child atoms, containing the encoded fragmentâs media frames and their timestamps.

### Note

For the HLS streaming session, in-track codec private data (CPD) changes are supported. After the first media fragment is made available in a streaming session, fragments can contain CPD changes for each track. Therefore, the fragments in a session can have a different resolution, bit rate, or other information in the CPD without interrupting playback. However, any change made in the track number or track codec format can return an error when those different media fragments are loaded. For example, streaming will fail if the fragments in the stream change from having only video to having both audio and video, or if an AAC audio track is changed to an ALAW audio track. For each streaming session, only 500 CPD changes are allowed.

Data retrieved with this action is billable. For information, see [Pricing](https://aws.amazon.com/kinesis/video-streams/pricing/) .

- **GetTSFragment:** Retrieves MPEG TS fragments containing both initialization and media data for all tracks in the stream.

### Note

If the `ContainerFormat` is `MPEG_TS` , this API is used instead of `GetMP4InitFragment` and `GetMP4MediaFragment` to retrieve stream media.

Data retrieved with this action is billable. For more information, see [Kinesis Video Streams pricing](https://aws.amazon.com/kinesis/video-streams/pricing/) .

A streaming session URL must not be shared between players. The service might throttle a session if multiple media players are sharing it. For connection limits, see [Kinesis Video Streams Limits](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html) .

You can monitor the amount of data that the media player consumes by monitoring the `GetMP4MediaFragment.OutgoingBytes` Amazon CloudWatch metric. For information about using CloudWatch to monitor Kinesis Video Streams, see [Monitoring Kinesis Video Streams](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/monitoring.html) . For pricing information, see [Amazon Kinesis Video Streams Pricing](https://aws.amazon.com/kinesis/video-streams/pricing/) and [Amazon Web Services Pricing](https://aws.amazon.com/pricing/) . Charges for both HLS sessions and outgoing Amazon Web Services data apply.

For more information about HLS, see [HTTP Live Streaming](https://developer.apple.com/streaming/) on the [Apple Developer site](https://developer.apple.com) .

### Warning

If an error is thrown after invoking a Kinesis Video Streams archived media API, in addition to the HTTP status code and the response body, it includes the following pieces of information:

- `x-amz-ErrorType` HTTP header â contains a more specific error type in addition to what the HTTP status code provides.
- `x-amz-RequestId` HTTP header â if you want to report an issue to Amazon Web Services, the support team can better diagnose the problem if given the Request Id.

Both the HTTP status code and the ErrorType header can be utilized to make programmatic decisions about whether errors are retry-able and under what conditions, as well as provide information on what actions the client programmer might need to take in order to successfully try again.

For more information, see the **Errors** section at the bottom of this topic, as well as [Common Errors](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonErrors.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kinesis-video-archived-media-2017-09-30/GetHLSStreamingSessionURL)

## Synopsis

```
get-hls-streaming-session-url
[--stream-name <value>]
[--stream-arn <value>]
[--playback-mode <value>]
[--hls-fragment-selector <value>]
[--container-format <value>]
[--discontinuity-mode <value>]
[--display-fragment-timestamp <value>]
[--expires <value>]
[--max-media-playlist-fragment-results <value>]
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

`--stream-name` (string)

The name of the stream for which to retrieve the HLS master playlist URL.

You must specify either the `StreamName` or the `StreamARN` .

`--stream-arn` (string)

The Amazon Resource Name (ARN) of the stream for which to retrieve the HLS master playlist URL.

You must specify either the `StreamName` or the `StreamARN` .

`--playback-mode` (string)

Whether to retrieve live, live replay, or archived, on-demand data.

Features of the three types of sessions include the following:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis-video-archived-media/get-hls-streaming-session-url.html#id1)`LIVE` ** : For sessions of this type, the HLS media playlist is continually updated with the latest fragments as they become available. We recommend that the media player retrieve a new playlist on a one-second interval. When this type of session is played in a media player, the user interface typically displays a âliveâ notification, with no scrubber control for choosing the position in the playback window to display.

### Note

In `LIVE` mode, the newest available fragments are included in an HLS media playlist, even if there is a gap between fragments (that is, if a fragment is missing). A gap like this might cause a media player to halt or cause a jump in playback. In this mode, fragments are not added to the HLS media playlist if they are older than the newest fragment in the playlist. If the missing fragment becomes available after a subsequent fragment is added to the playlist, the older fragment is not added, and the gap is not filled.

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis-video-archived-media/get-hls-streaming-session-url.html#id3)`LIVE_REPLAY` ** : For sessions of this type, the HLS media playlist is updated similarly to how it is updated for `LIVE` mode except that it starts by including fragments from a given start time. Instead of fragments being added as they are ingested, fragments are added as the duration of the next fragment elapses. For example, if the fragments in the session are two seconds long, then a new fragment is added to the media playlist every two seconds. This mode is useful to be able to start playback from when an event is detected and continue live streaming media that has not yet been ingested as of the time of the session creation. This mode is also useful to stream previously archived media without being limited by the 1,000 fragment limit in the `ON_DEMAND` mode.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis-video-archived-media/get-hls-streaming-session-url.html#id5)`ON_DEMAND` ** : For sessions of this type, the HLS media playlist contains all the fragments for the session, up to the number that is specified in `MaxMediaPlaylistFragmentResults` . The playlist must be retrieved only once for each session. When this type of session is played in a media player, the user interface typically displays a scrubber control for choosing the position in the playback window to display.

In all playback modes, if `FragmentSelectorType` is `PRODUCER_TIMESTAMP` , and if there are multiple fragments with the same start timestamp, the fragment that has the largest fragment number (that is, the newest fragment) is included in the HLS media playlist. The other fragments are not included. Fragments that have different timestamps but have overlapping durations are still included in the HLS media playlist. This can lead to unexpected behavior in the media player.

The default is `LIVE` .

Possible values:

- `LIVE`
- `LIVE_REPLAY`
- `ON_DEMAND`

`--hls-fragment-selector` (structure)

The time range of the requested fragment and the source of the timestamps.

This parameter is required if `PlaybackMode` is `ON_DEMAND` or `LIVE_REPLAY` . This parameter is optional if PlaybackMode is `LIVE` . If `PlaybackMode` is `LIVE` , the `FragmentSelectorType` can be set, but the `TimestampRange` should not be set. If `PlaybackMode` is `ON_DEMAND` or `LIVE_REPLAY` , both `FragmentSelectorType` and `TimestampRange` must be set.

FragmentSelectorType -> (string)

The source of the timestamps for the requested media.

When `FragmentSelectorType` is set to `PRODUCER_TIMESTAMP` and  GetHLSStreamingSessionURLInput$PlaybackMode is `ON_DEMAND` or `LIVE_REPLAY` , the first fragment ingested with a producer timestamp within the specified  FragmentSelector$TimestampRange is included in the media playlist. In addition, the fragments with producer timestamps within the `TimestampRange` ingested immediately following the first fragment (up to the  GetHLSStreamingSessionURLInput$MaxMediaPlaylistFragmentResults value) are included.

Fragments that have duplicate producer timestamps are deduplicated. This means that if producers are producing a stream of fragments with producer timestamps that are approximately equal to the true clock time, the HLS media playlists will contain all of the fragments within the requested timestamp range. If some fragments are ingested within the same time range and very different points in time, only the oldest ingested collection of fragments are returned.

When `FragmentSelectorType` is set to `PRODUCER_TIMESTAMP` and  GetHLSStreamingSessionURLInput$PlaybackMode is `LIVE` , the producer timestamps are used in the MP4 fragments and for deduplication. But the most recently ingested fragments based on server timestamps are included in the HLS media playlist. This means that even if fragments ingested in the past have producer timestamps with values now, they are not included in the HLS media playlist.

The default is `SERVER_TIMESTAMP` .

TimestampRange -> (structure)

The start and end of the timestamp range for the requested media.

This value should not be present if `PlaybackType` is `LIVE` .

StartTimestamp -> (timestamp)

The start of the timestamp range for the requested media.

If the `HLSTimestampRange` value is specified, the `StartTimestamp` value is required.

Only fragments that start exactly at or after `StartTimestamp` are included in the session. Fragments that start before `StartTimestamp` and continue past it arenât included in the session. If `FragmentSelectorType` is `SERVER_TIMESTAMP` , the `StartTimestamp` must be later than the stream head.

EndTimestamp -> (timestamp)

The end of the timestamp range for the requested media. This value must be within 24 hours of the specified `StartTimestamp` , and it must be later than the `StartTimestamp` value.

If `FragmentSelectorType` for the request is `SERVER_TIMESTAMP` , this value must be in the past.

The `EndTimestamp` value is required for `ON_DEMAND` mode, but optional for `LIVE_REPLAY` mode. If the `EndTimestamp` is not set for `LIVE_REPLAY` mode then the session will continue to include newly ingested fragments until the session expires.

### Note

This value is inclusive. The `EndTimestamp` is compared to the (starting) timestamp of the fragment. Fragments that start before the `EndTimestamp` value and continue past it are included in the session.

Shorthand Syntax:

```
FragmentSelectorType=string,TimestampRange={StartTimestamp=timestamp,EndTimestamp=timestamp}
```

JSON Syntax:

```
{
  "FragmentSelectorType": "PRODUCER_TIMESTAMP"|"SERVER_TIMESTAMP",
  "TimestampRange": {
    "StartTimestamp": timestamp,
    "EndTimestamp": timestamp
  }
}
```

`--container-format` (string)

Specifies which format should be used for packaging the media. Specifying the `FRAGMENTED_MP4` container format packages the media into MP4 fragments (fMP4 or CMAF). This is the recommended packaging because there is minimal packaging overhead. The other container format option is `MPEG_TS` . HLS has supported MPEG TS chunks since it was released and is sometimes the only supported packaging on older HLS players. MPEG TS typically has a 5-25 percent packaging overhead. This means MPEG TS typically requires 5-25 percent more bandwidth and cost than fMP4.

The default is `FRAGMENTED_MP4` .

Possible values:

- `FRAGMENTED_MP4`
- `MPEG_TS`

`--discontinuity-mode` (string)

Specifies when flags marking discontinuities between fragments are added to the media playlists.

Media players typically build a timeline of media content to play, based on the timestamps of each fragment. This means that if there is any overlap or gap between fragments (as is typical if  HLSFragmentSelector is set to `SERVER_TIMESTAMP` ), the media player timeline will also have small gaps between fragments in some places, and will overwrite frames in other places. Gaps in the media player timeline can cause playback to stall and overlaps can cause playback to be jittery. When there are discontinuity flags between fragments, the media player is expected to reset the timeline, resulting in the next fragment being played immediately after the previous fragment.

The following modes are supported:

- `ALWAYS` : a discontinuity marker is placed between every fragment in the HLS media playlist. It is recommended to use a value of `ALWAYS` if the fragment timestamps are not accurate.
- `NEVER` : no discontinuity markers are placed anywhere. It is recommended to use a value of `NEVER` to ensure the media player timeline most accurately maps to the producer timestamps.
- `ON_DISCONTINUITY` : a discontinuity marker is placed between fragments that have a gap or overlap of more than 50 milliseconds. For most playback scenarios, it is recommended to use a value of `ON_DISCONTINUITY` so that the media player timeline is only reset when there is a significant issue with the media timeline (e.g. a missing fragment).

The default is `ALWAYS` when  HLSFragmentSelector is set to `SERVER_TIMESTAMP` , and `NEVER` when it is set to `PRODUCER_TIMESTAMP` .

Possible values:

- `ALWAYS`
- `NEVER`
- `ON_DISCONTINUITY`

`--display-fragment-timestamp` (string)

Specifies when the fragment start timestamps should be included in the HLS media playlist. Typically, media players report the playhead position as a time relative to the start of the first fragment in the playback session. However, when the start timestamps are included in the HLS media playlist, some media players might report the current playhead as an absolute time based on the fragment timestamps. This can be useful for creating a playback experience that shows viewers the wall-clock time of the media.

The default is `NEVER` . When  HLSFragmentSelector is `SERVER_TIMESTAMP` , the timestamps will be the server start timestamps. Similarly, when  HLSFragmentSelector is `PRODUCER_TIMESTAMP` , the timestamps will be the producer start timestamps.

Possible values:

- `ALWAYS`
- `NEVER`

`--expires` (integer)

The time in seconds until the requested session expires. This value can be between 300 (5 minutes) and 43200 (12 hours).

When a session expires, no new calls to `GetHLSMasterPlaylist` , `GetHLSMediaPlaylist` , `GetMP4InitFragment` , `GetMP4MediaFragment` , or `GetTSFragment` can be made for that session.

The default is 300 (5 minutes).

`--max-media-playlist-fragment-results` (long)

The maximum number of fragments that are returned in the HLS media playlists.

When the `PlaybackMode` is `LIVE` , the most recent fragments are returned up to this value. When the `PlaybackMode` is `ON_DEMAND` , the oldest fragments are returned, up to this maximum number.

When there are a higher number of fragments available in a live HLS media playlist, video players often buffer content before starting playback. Increasing the buffer size increases the playback latency, but it decreases the likelihood that rebuffering will occur during playback. We recommend that a live HLS media playlist have a minimum of 3 fragments and a maximum of 10 fragments.

The default is 5 fragments if `PlaybackMode` is `LIVE` or `LIVE_REPLAY` , and 1,000 if `PlaybackMode` is `ON_DEMAND` .

The maximum value of 5,000 fragments corresponds to more than 80 minutes of video on streams with 1-second fragments, and more than 13 hours of video on streams with 10-second fragments.

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

HLSStreamingSessionURL -> (string)

The URL (containing the session token) that a media player can use to retrieve the HLS master playlist.