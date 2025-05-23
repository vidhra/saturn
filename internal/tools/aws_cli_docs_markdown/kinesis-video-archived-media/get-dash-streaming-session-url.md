# get-dash-streaming-session-urlÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis-video-archived-media/get-dash-streaming-session-url.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis-video-archived-media/get-dash-streaming-session-url.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kinesis-video-archived-media](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis-video-archived-media/index.html#cli-aws-kinesis-video-archived-media) ]

# get-dash-streaming-session-url

## Description

Retrieves an MPEG Dynamic Adaptive Streaming over HTTP (DASH) URL for the stream. You can then open the URL in a media player to view the stream contents.

Both the `StreamName` and the `StreamARN` parameters are optional, but you must specify either the `StreamName` or the `StreamARN` when invoking this API operation.

An Amazon Kinesis video stream has the following requirements for providing data through MPEG-DASH:

- The media must contain h.264 or h.265 encoded video and, optionally, AAC or G.711 encoded audio. Specifically, the codec ID of track 1 should be `V_MPEG/ISO/AVC` (for h.264) or V_MPEGH/ISO/HEVC (for H.265). Optionally, the codec ID of track 2 should be `A_AAC` (for AAC) or A_MS/ACM (for G.711).
- Data retention must be greater than 0.
- The video track of each fragment must contain codec private data in the Advanced Video Coding (AVC) for H.264 format and HEVC for H.265 format. For more information, see [MPEG-4 specification ISO/IEC 14496-15](https://www.iso.org/standard/55980.html) . For information about adapting stream data to a given format, see [NAL Adaptation Flags](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-reference-nal.html) .
- The audio track (if present) of each fragment must contain codec private data in the AAC format ([AAC specification ISO/IEC 13818-7](https://www.iso.org/standard/43345.html) ) or the [MS Wave format](http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/WAVE.html) .

The following procedure shows how to use MPEG-DASH with Kinesis Video Streams:

- Get an endpoint using [GetDataEndpoint](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_GetDataEndpoint.html) , specifying `GET_DASH_STREAMING_SESSION_URL` for the `APIName` parameter.
- Retrieve the MPEG-DASH URL using `GetDASHStreamingSessionURL` . Kinesis Video Streams creates an MPEG-DASH streaming session to be used for accessing content in a stream using the MPEG-DASH protocol. `GetDASHStreamingSessionURL` returns an authenticated URL (that includes an encrypted session token) for the sessionâs MPEG-DASH *manifest* (the root resource needed for streaming with MPEG-DASH).

### Note

Donât share or store this token where an unauthorized entity can access it. The token provides access to the content of the stream. Safeguard the token with the same measures that you use with your Amazon Web Services credentials.

The media that is made available through the manifest consists only of the requested stream, time range, and format. No other media data (such as frames outside the requested window or alternate bitrates) is made available.

- Provide the URL (containing the encrypted session token) for the MPEG-DASH manifest to a media player that supports the MPEG-DASH protocol. Kinesis Video Streams makes the initialization fragment and media fragments available through the manifest URL. The initialization fragment contains the codec private data for the stream, and other data needed to set up the video or audio decoder and renderer. The media fragments contain encoded video frames or encoded audio samples.
- The media player receives the authenticated URL and requests stream metadata and media data normally. When the media player requests data, it calls the following actions:

- **GetDASHManifest:** Retrieves an MPEG DASH manifest, which contains the metadata for the media that you want to playback.
- **GetMP4InitFragment:** Retrieves the MP4 initialization fragment. The media player typically loads the initialization fragment before loading any media fragments. This fragment contains the â`fytp` â and â`moov` â MP4 atoms, and the child atoms that are needed to initialize the media player decoder. The initialization fragment does not correspond to a fragment in a Kinesis video stream. It contains only the codec private data for the stream and respective track, which the media player needs to decode the media frames.
- **GetMP4MediaFragment:** Retrieves MP4 media fragments. These fragments contain the â`moof` â and â`mdat` â MP4 atoms and their child atoms, containing the encoded fragmentâs media frames and their timestamps.

### Note

After the first media fragment is made available in a streaming session, any fragments that donât contain the same codec private data cause an error to be returned when those different media fragments are loaded. Therefore, the codec private data should not change between fragments in a session. This also means that the session fails if the fragments in a stream change from having only video to having both audio and video.

Data retrieved with this action is billable. See [Pricing](https://aws.amazon.com/kinesis/video-streams/pricing/) for details.

### Note

For restrictions that apply to MPEG-DASH sessions, see [Kinesis Video Streams Limits](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html) .

You can monitor the amount of data that the media player consumes by monitoring the `GetMP4MediaFragment.OutgoingBytes` Amazon CloudWatch metric. For information about using CloudWatch to monitor Kinesis Video Streams, see [Monitoring Kinesis Video Streams](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/monitoring.html) . For pricing information, see [Amazon Kinesis Video Streams Pricing](https://aws.amazon.com/kinesis/video-streams/pricing/) and [Amazon Web Services Pricing](https://aws.amazon.com/pricing/) . Charges for both HLS sessions and outgoing Amazon Web Services data apply.

For more information about HLS, see [HTTP Live Streaming](https://developer.apple.com/streaming/) on the [Apple Developer site](https://developer.apple.com) .

### Warning

If an error is thrown after invoking a Kinesis Video Streams archived media API, in addition to the HTTP status code and the response body, it includes the following pieces of information:

- `x-amz-ErrorType` HTTP header â contains a more specific error type in addition to what the HTTP status code provides.
- `x-amz-RequestId` HTTP header â if you want to report an issue to Amazon Web Services the support team can better diagnose the problem if given the Request Id.

Both the HTTP status code and the ErrorType header can be utilized to make programmatic decisions about whether errors are retry-able and under what conditions, as well as provide information on what actions the client programmer might need to take in order to successfully try again.

For more information, see the **Errors** section at the bottom of this topic, as well as [Common Errors](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonErrors.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kinesis-video-archived-media-2017-09-30/GetDASHStreamingSessionURL)

## Synopsis

```
get-dash-streaming-session-url
[--stream-name <value>]
[--stream-arn <value>]
[--playback-mode <value>]
[--display-fragment-timestamp <value>]
[--display-fragment-number <value>]
[--dash-fragment-selector <value>]
[--expires <value>]
[--max-manifest-fragment-results <value>]
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

The name of the stream for which to retrieve the MPEG-DASH manifest URL.

You must specify either the `StreamName` or the `StreamARN` .

`--stream-arn` (string)

The Amazon Resource Name (ARN) of the stream for which to retrieve the MPEG-DASH manifest URL.

You must specify either the `StreamName` or the `StreamARN` .

`--playback-mode` (string)

Whether to retrieve live, live replay, or archived, on-demand data.

Features of the three types of sessions include the following:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis-video-archived-media/get-dash-streaming-session-url.html#id1)`LIVE` ** : For sessions of this type, the MPEG-DASH manifest is continually updated with the latest fragments as they become available. We recommend that the media player retrieve a new manifest on a one-second interval. When this type of session is played in a media player, the user interface typically displays a âliveâ notification, with no scrubber control for choosing the position in the playback window to display.

### Note

In `LIVE` mode, the newest available fragments are included in an MPEG-DASH manifest, even if there is a gap between fragments (that is, if a fragment is missing). A gap like this might cause a media player to halt or cause a jump in playback. In this mode, fragments are not added to the MPEG-DASH manifest if they are older than the newest fragment in the playlist. If the missing fragment becomes available after a subsequent fragment is added to the manifest, the older fragment is not added, and the gap is not filled.

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis-video-archived-media/get-dash-streaming-session-url.html#id3)`LIVE_REPLAY` ** : For sessions of this type, the MPEG-DASH manifest is updated similarly to how it is updated for `LIVE` mode except that it starts by including fragments from a given start time. Instead of fragments being added as they are ingested, fragments are added as the duration of the next fragment elapses. For example, if the fragments in the session are two seconds long, then a new fragment is added to the manifest every two seconds. This mode is useful to be able to start playback from when an event is detected and continue live streaming media that has not yet been ingested as of the time of the session creation. This mode is also useful to stream previously archived media without being limited by the 1,000 fragment limit in the `ON_DEMAND` mode.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis-video-archived-media/get-dash-streaming-session-url.html#id5)`ON_DEMAND` ** : For sessions of this type, the MPEG-DASH manifest contains all the fragments for the session, up to the number that is specified in `MaxManifestFragmentResults` . The manifest must be retrieved only once for each session. When this type of session is played in a media player, the user interface typically displays a scrubber control for choosing the position in the playback window to display.

In all playback modes, if `FragmentSelectorType` is `PRODUCER_TIMESTAMP` , and if there are multiple fragments with the same start timestamp, the fragment that has the larger fragment number (that is, the newer fragment) is included in the MPEG-DASH manifest. The other fragments are not included. Fragments that have different timestamps but have overlapping durations are still included in the MPEG-DASH manifest. This can lead to unexpected behavior in the media player.

The default is `LIVE` .

Possible values:

- `LIVE`
- `LIVE_REPLAY`
- `ON_DEMAND`

`--display-fragment-timestamp` (string)

Per the MPEG-DASH specification, the wall-clock time of fragments in the manifest file can be derived using attributes in the manifest itself. However, typically, MPEG-DASH compatible media players do not properly handle gaps in the media timeline. Kinesis Video Streams adjusts the media timeline in the manifest file to enable playback of media with discontinuities. Therefore, the wall-clock time derived from the manifest file may be inaccurate. If DisplayFragmentTimestamp is set to `ALWAYS` , the accurate fragment timestamp is added to each S element in the manifest file with the attribute name âkvs:tsâ. A custom MPEG-DASH media player is necessary to leverage this custom attribute.

The default value is `NEVER` . When  DASHFragmentSelector is `SERVER_TIMESTAMP` , the timestamps will be the server start timestamps. Similarly, when  DASHFragmentSelector is `PRODUCER_TIMESTAMP` , the timestamps will be the producer start timestamps.

Possible values:

- `ALWAYS`
- `NEVER`

`--display-fragment-number` (string)

Fragments are identified in the manifest file based on their sequence number in the session. If DisplayFragmentNumber is set to `ALWAYS` , the Kinesis Video Streams fragment number is added to each S element in the manifest file with the attribute name âkvs:fnâ. These fragment numbers can be used for logging or for use with other APIs (e.g. `GetMedia` and `GetMediaForFragmentList` ). A custom MPEG-DASH media player is necessary to leverage these this custom attribute.

The default value is `NEVER` .

Possible values:

- `ALWAYS`
- `NEVER`

`--dash-fragment-selector` (structure)

The time range of the requested fragment and the source of the timestamps.

This parameter is required if `PlaybackMode` is `ON_DEMAND` or `LIVE_REPLAY` . This parameter is optional if PlaybackMode is `LIVE` . If `PlaybackMode` is `LIVE` , the `FragmentSelectorType` can be set, but the `TimestampRange` should not be set. If `PlaybackMode` is `ON_DEMAND` or `LIVE_REPLAY` , both `FragmentSelectorType` and `TimestampRange` must be set.

FragmentSelectorType -> (string)

The source of the timestamps for the requested media.

When `FragmentSelectorType` is set to `PRODUCER_TIMESTAMP` and  GetDASHStreamingSessionURLInput$PlaybackMode is `ON_DEMAND` or `LIVE_REPLAY` , the first fragment ingested with a producer timestamp within the specified  FragmentSelector$TimestampRange is included in the media playlist. In addition, the fragments with producer timestamps within the `TimestampRange` ingested immediately following the first fragment (up to the  GetDASHStreamingSessionURLInput$MaxManifestFragmentResults value) are included.

Fragments that have duplicate producer timestamps are deduplicated. This means that if producers are producing a stream of fragments with producer timestamps that are approximately equal to the true clock time, the MPEG-DASH manifest will contain all of the fragments within the requested timestamp range. If some fragments are ingested within the same time range and very different points in time, only the oldest ingested collection of fragments are returned.

When `FragmentSelectorType` is set to `PRODUCER_TIMESTAMP` and  GetDASHStreamingSessionURLInput$PlaybackMode is `LIVE` , the producer timestamps are used in the MP4 fragments and for deduplication. But the most recently ingested fragments based on server timestamps are included in the MPEG-DASH manifest. This means that even if fragments ingested in the past have producer timestamps with values now, they are not included in the HLS media playlist.

The default is `SERVER_TIMESTAMP` .

TimestampRange -> (structure)

The start and end of the timestamp range for the requested media.

This value should not be present if `PlaybackType` is `LIVE` .

StartTimestamp -> (timestamp)

The start of the timestamp range for the requested media.

If the `DASHTimestampRange` value is specified, the `StartTimestamp` value is required.

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

`--expires` (integer)

The time in seconds until the requested session expires. This value can be between 300 (5 minutes) and 43200 (12 hours).

When a session expires, no new calls to `GetDashManifest` , `GetMP4InitFragment` , or `GetMP4MediaFragment` can be made for that session.

The default is 300 (5 minutes).

`--max-manifest-fragment-results` (long)

The maximum number of fragments that are returned in the MPEG-DASH manifest.

When the `PlaybackMode` is `LIVE` , the most recent fragments are returned up to this value. When the `PlaybackMode` is `ON_DEMAND` , the oldest fragments are returned, up to this maximum number.

When there are a higher number of fragments available in a live MPEG-DASH manifest, video players often buffer content before starting playback. Increasing the buffer size increases the playback latency, but it decreases the likelihood that rebuffering will occur during playback. We recommend that a live MPEG-DASH manifest have a minimum of 3 fragments and a maximum of 10 fragments.

The default is 5 fragments if `PlaybackMode` is `LIVE` or `LIVE_REPLAY` , and 1,000 if `PlaybackMode` is `ON_DEMAND` .

The maximum value of 1,000 fragments corresponds to more than 16 minutes of video on streams with 1-second fragments, and more than 2 1/2 hours of video on streams with 10-second fragments.

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

DASHStreamingSessionURL -> (string)

The URL (containing the session token) that a media player can use to retrieve the MPEG-DASH manifest.