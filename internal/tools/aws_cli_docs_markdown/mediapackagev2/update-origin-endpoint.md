# update-origin-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/update-origin-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/update-origin-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediapackagev2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/index.html#cli-aws-mediapackagev2) ]

# update-origin-endpoint

## Description

Update the specified origin endpoint. Edit the packaging preferences on an endpoint to optimize the viewing experience. You canât edit the name of the endpoint.

Any edits you make that impact the video output may not be reflected for a few minutes.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediapackagev2-2022-12-25/UpdateOriginEndpoint)

## Synopsis

```
update-origin-endpoint
--channel-group-name <value>
--channel-name <value>
--origin-endpoint-name <value>
--container-type <value>
[--segment <value>]
[--description <value>]
[--startover-window-seconds <value>]
[--hls-manifests <value>]
[--low-latency-hls-manifests <value>]
[--dash-manifests <value>]
[--force-endpoint-error-configuration <value>]
[--e-tag <value>]
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

`--channel-group-name` (string)

The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.

`--channel-name` (string)

The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.

`--origin-endpoint-name` (string)

The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.

`--container-type` (string)

The type of container attached to this origin endpoint. A container type is a file format that encapsulates one or more media streams, such as audio and video, into a single file.

Possible values:

- `TS`
- `CMAF`

`--segment` (structure)

The segment configuration, including the segment name, duration, and other configuration values.

SegmentDurationSeconds -> (integer)

The duration (in seconds) of each segment. Enter a value equal to, or a multiple of, the input segment duration. If the value that you enter is different from the input segment duration, MediaPackage rounds segments to the nearest multiple of the input segment duration.

SegmentName -> (string)

The name that describes the segment. The name is the base name of the segment used in all content manifests inside of the endpoint. You canât use spaces in the name.

TsUseAudioRenditionGroup -> (boolean)

When selected, MediaPackage bundles all audio tracks in a rendition group. All other tracks in the stream can be used with any audio rendition from the group.

IncludeIframeOnlyStreams -> (boolean)

When selected, the stream set includes an additional I-frame only stream, along with the other tracks. If false, this extra stream is not included. MediaPackage generates an I-frame only stream from the first rendition in the manifest. The service inserts EXT-I-FRAMES-ONLY tags in the output manifest, and then generates and includes an I-frames only playlist in the stream. This playlist permits player functionality like fast forward and rewind.

TsIncludeDvbSubtitles -> (boolean)

By default, MediaPackage excludes all digital video broadcasting (DVB) subtitles from the output. When selected, MediaPackage passes through DVB subtitles into the output.

Scte -> (structure)

The SCTE configuration options in the segment settings.

ScteFilter -> (list)

The SCTE-35 message types that you want to be treated as ad markers in the output.

(string)

Encryption -> (structure)

The parameters for encrypting content.

ConstantInitializationVector -> (string)

A 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting content. If you donât specify a value, then MediaPackage creates the constant initialization vector (IV).

EncryptionMethod -> (structure)

The encryption method to use.

TsEncryptionMethod -> (string)

The encryption method to use.

CmafEncryptionMethod -> (string)

The encryption method to use.

KeyRotationIntervalSeconds -> (integer)

The frequency (in seconds) of key changes for live workflows, in which content is streamed real time. The service retrieves content keys before the live content begins streaming, and then retrieves them as needed over the lifetime of the workflow. By default, key rotation is set to 300 seconds (5 minutes), the minimum rotation interval, which is equivalent to setting it to 300. If you donât enter an interval, content keys arenât rotated.

The following example setting causes the service to rotate keys every thirty minutes: `1800`

SpekeKeyProvider -> (structure)

The parameters for the SPEKE key provider.

EncryptionContractConfiguration -> (structure)

Configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use.

PresetSpeke20Audio -> (string)

A collection of audio encryption presets.

Value description:

- PRESET-AUDIO-1 - Use one content key to encrypt all of the audio tracks in your stream.
- PRESET-AUDIO-2 - Use one content key to encrypt all of the stereo audio tracks and one content key to encrypt all of the multichannel audio tracks.
- PRESET-AUDIO-3 - Use one content key to encrypt all of the stereo audio tracks, one content key to encrypt all of the multichannel audio tracks with 3 to 6 channels, and one content key to encrypt all of the multichannel audio tracks with more than 6 channels.
- SHARED - Use the same content key for all of the audio and video tracks in your stream.
- UNENCRYPTED - Donât encrypt any of the audio tracks in your stream.

PresetSpeke20Video -> (string)

A collection of video encryption presets.

Value description:

- PRESET-VIDEO-1 - Use one content key to encrypt all of the video tracks in your stream.
- PRESET-VIDEO-2 - Use one content key to encrypt all of the SD video tracks and one content key for all HD and higher resolutions video tracks.
- PRESET-VIDEO-3 - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks and one content key for all UHD video tracks.
- PRESET-VIDEO-4 - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
- PRESET-VIDEO-5 - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
- PRESET-VIDEO-6 - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks.
- PRESET-VIDEO-7 - Use one content key to encrypt all of the SD+HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks.
- PRESET-VIDEO-8 - Use one content key to encrypt all of the SD+HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
- SHARED - Use the same content key for all of the video and audio tracks in your stream.
- UNENCRYPTED - Donât encrypt any of the video tracks in your stream.

ResourceId -> (string)

The unique identifier for the content. The service sends this to the key server to identify the current endpoint. How unique you make this depends on how fine-grained you want access controls to be. The service does not permit you to use the same ID for two simultaneous encryption processes. The resource ID is also known as the content ID.

The following example shows a resource ID: `MovieNight20171126093045`

DrmSystems -> (list)

The DRM solution provider youâre using to protect your content during distribution.

(string)

RoleArn -> (string)

The ARN for the IAM role granted by the key provider that provides access to the key provider API. This role must have a trust policy that allows MediaPackage to assume the role, and it must have a sufficient permissions policy to allow access to the specific key retrieval URL. Get this from your DRM solution provider.

Valid format: `arn:aws:iam::{accountID}:role/{name}` . The following example shows a role ARN: `arn:aws:iam::444455556666:role/SpekeAccess`

Url -> (string)

The URL of the API Gateway proxy that you set up to talk to your key server. The API Gateway proxy must reside in the same AWS Region as MediaPackage and must start with [https://](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/update-origin-endpoint.html).

The following example shows a URL: `https://1wm2dx1f33.execute-api.us-west-2.amazonaws.com/SpekeSample/copyProtection`

JSON Syntax:

```
{
  "SegmentDurationSeconds": integer,
  "SegmentName": "string",
  "TsUseAudioRenditionGroup": true|false,
  "IncludeIframeOnlyStreams": true|false,
  "TsIncludeDvbSubtitles": true|false,
  "Scte": {
    "ScteFilter": ["SPLICE_INSERT"|"BREAK"|"PROVIDER_ADVERTISEMENT"|"DISTRIBUTOR_ADVERTISEMENT"|"PROVIDER_PLACEMENT_OPPORTUNITY"|"DISTRIBUTOR_PLACEMENT_OPPORTUNITY"|"PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY"|"DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY"|"PROGRAM", ...]
  },
  "Encryption": {
    "ConstantInitializationVector": "string",
    "EncryptionMethod": {
      "TsEncryptionMethod": "AES_128"|"SAMPLE_AES",
      "CmafEncryptionMethod": "CENC"|"CBCS"
    },
    "KeyRotationIntervalSeconds": integer,
    "SpekeKeyProvider": {
      "EncryptionContractConfiguration": {
        "PresetSpeke20Audio": "PRESET_AUDIO_1"|"PRESET_AUDIO_2"|"PRESET_AUDIO_3"|"SHARED"|"UNENCRYPTED",
        "PresetSpeke20Video": "PRESET_VIDEO_1"|"PRESET_VIDEO_2"|"PRESET_VIDEO_3"|"PRESET_VIDEO_4"|"PRESET_VIDEO_5"|"PRESET_VIDEO_6"|"PRESET_VIDEO_7"|"PRESET_VIDEO_8"|"SHARED"|"UNENCRYPTED"
      },
      "ResourceId": "string",
      "DrmSystems": ["CLEAR_KEY_AES_128"|"FAIRPLAY"|"PLAYREADY"|"WIDEVINE"|"IRDETO", ...],
      "RoleArn": "string",
      "Url": "string"
    }
  }
}
```

`--description` (string)

Any descriptive information that you want to add to the origin endpoint for future identification purposes.

`--startover-window-seconds` (integer)

The size of the window (in seconds) to create a window of the live stream thatâs available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days).

`--hls-manifests` (list)

An HTTP live streaming (HLS) manifest configuration.

(structure)

Create an HTTP live streaming (HLS) manifest configuration.

ManifestName -> (string)

A short short string thatâs appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you donât enter a value, MediaPackage uses the default manifest name, index. MediaPackage automatically inserts the format extension, such as .m3u8. You canât use the same manifest name if you use HLS manifest and low-latency HLS manifest. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.

ChildManifestName -> (string)

A short string thatâs appended to the endpoint URL. The child manifest name creates a unique path to this endpoint. If you donât enter a value, MediaPackage uses the default manifest name, index, with an added suffix to distinguish it from the manifest name. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.

ScteHls -> (structure)

The SCTE configuration.

AdMarkerHls -> (string)

Ad markers indicate when ads should be inserted during playback. If you include ad markers in the content stream in your upstream encoders, then you need to inform MediaPackage what to do with the ad markers in the output. Choose what you want MediaPackage to do with the ad markers.

Value description:

- DATERANGE - Insert EXT-X-DATERANGE tags to signal ad and program transition events in TS and CMAF manifests. If you use DATERANGE, you must set a programDateTimeIntervalSeconds value of 1 or higher. To learn more about DATERANGE, see [SCTE-35 Ad Marker EXT-X-DATERANGE](http://docs.aws.amazon.com/mediapackage/latest/ug/scte-35-ad-marker-ext-x-daterange.html) .

StartTag -> (structure)

To insert an EXT-X-START tag in your HLS playlist, specify a StartTag configuration object with a valid TimeOffset. When you do, you can also optionally specify whether to include a PRECISE value in the EXT-X-START tag.

TimeOffset -> (float)

Specify the value for TIME-OFFSET within your EXT-X-START tag. Enter a signed floating point value which, if positive, must be less than the configured manifest duration minus three times the configured segment target duration. If negative, the absolute value must be larger than three times the configured segment target duration, and the absolute value must be smaller than the configured manifest duration.

Precise -> (boolean)

Specify the value for PRECISE within your EXT-X-START tag. Leave blank, or choose false, to use the default value NO. Choose yes to use the value YES.

ManifestWindowSeconds -> (integer)

The total duration (in seconds) of the manifestâs content.

ProgramDateTimeIntervalSeconds -> (integer)

Inserts EXT-X-PROGRAM-DATE-TIME tags in the output manifest at the interval that you specify. If you donât enter an interval, EXT-X-PROGRAM-DATE-TIME tags arenât included in the manifest. The tags sync the stream to the wall clock so that viewers can seek to a specific time in the playback timeline on the player.

Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it is passed through to the HLS output.

FilterConfiguration -> (structure)

Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.

ManifestFilter -> (string)

Optionally specify one or more manifest filters for all of your manifest egress requests. When you include a manifest filter, note that you cannot use an identical manifest filter query parameter for this manifestâs endpoint URL.

Start -> (timestamp)

Optionally specify the start time for all of your manifest egress requests. When you include start time, note that you cannot use start time query parameters for this manifestâs endpoint URL.

End -> (timestamp)

Optionally specify the end time for all of your manifest egress requests. When you include end time, note that you cannot use end time query parameters for this manifestâs endpoint URL.

TimeDelaySeconds -> (integer)

Optionally specify the time delay for all of your manifest egress requests. Enter a value that is smaller than your endpointâs startover window. When you include time delay, note that you cannot use time delay query parameters for this manifestâs endpoint URL.

ClipStartTime -> (timestamp)

Optionally specify the clip start time for all of your manifest egress requests. When you include clip start time, note that you cannot use clip start time query parameters for this manifestâs endpoint URL.

UrlEncodeChildManifest -> (boolean)

When enabled, MediaPackage URL-encodes the query string for API requests for HLS child manifests to comply with Amazon Web Services Signature Version 4 (SigV4) signature signing protocol. For more information, see [Amazon Web Services Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in *Identity and Access Management User Guide* .

Shorthand Syntax:

```
ManifestName=string,ChildManifestName=string,ScteHls={AdMarkerHls=string},StartTag={TimeOffset=float,Precise=boolean},ManifestWindowSeconds=integer,ProgramDateTimeIntervalSeconds=integer,FilterConfiguration={ManifestFilter=string,Start=timestamp,End=timestamp,TimeDelaySeconds=integer,ClipStartTime=timestamp},UrlEncodeChildManifest=boolean ...
```

JSON Syntax:

```
[
  {
    "ManifestName": "string",
    "ChildManifestName": "string",
    "ScteHls": {
      "AdMarkerHls": "DATERANGE"
    },
    "StartTag": {
      "TimeOffset": float,
      "Precise": true|false
    },
    "ManifestWindowSeconds": integer,
    "ProgramDateTimeIntervalSeconds": integer,
    "FilterConfiguration": {
      "ManifestFilter": "string",
      "Start": timestamp,
      "End": timestamp,
      "TimeDelaySeconds": integer,
      "ClipStartTime": timestamp
    },
    "UrlEncodeChildManifest": true|false
  }
  ...
]
```

`--low-latency-hls-manifests` (list)

A low-latency HLS manifest configuration.

(structure)

Create a low-latency HTTP live streaming (HLS) manifest configuration.

ManifestName -> (string)

A short short string thatâs appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you donât enter a value, MediaPackage uses the default manifest name, index. MediaPackage automatically inserts the format extension, such as .m3u8. You canât use the same manifest name if you use HLS manifest and low-latency HLS manifest. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.

ChildManifestName -> (string)

A short string thatâs appended to the endpoint URL. The child manifest name creates a unique path to this endpoint. If you donât enter a value, MediaPackage uses the default manifest name, index, with an added suffix to distinguish it from the manifest name. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.

ScteHls -> (structure)

The SCTE configuration.

AdMarkerHls -> (string)

Ad markers indicate when ads should be inserted during playback. If you include ad markers in the content stream in your upstream encoders, then you need to inform MediaPackage what to do with the ad markers in the output. Choose what you want MediaPackage to do with the ad markers.

Value description:

- DATERANGE - Insert EXT-X-DATERANGE tags to signal ad and program transition events in TS and CMAF manifests. If you use DATERANGE, you must set a programDateTimeIntervalSeconds value of 1 or higher. To learn more about DATERANGE, see [SCTE-35 Ad Marker EXT-X-DATERANGE](http://docs.aws.amazon.com/mediapackage/latest/ug/scte-35-ad-marker-ext-x-daterange.html) .

StartTag -> (structure)

To insert an EXT-X-START tag in your HLS playlist, specify a StartTag configuration object with a valid TimeOffset. When you do, you can also optionally specify whether to include a PRECISE value in the EXT-X-START tag.

TimeOffset -> (float)

Specify the value for TIME-OFFSET within your EXT-X-START tag. Enter a signed floating point value which, if positive, must be less than the configured manifest duration minus three times the configured segment target duration. If negative, the absolute value must be larger than three times the configured segment target duration, and the absolute value must be smaller than the configured manifest duration.

Precise -> (boolean)

Specify the value for PRECISE within your EXT-X-START tag. Leave blank, or choose false, to use the default value NO. Choose yes to use the value YES.

ManifestWindowSeconds -> (integer)

The total duration (in seconds) of the manifestâs content.

ProgramDateTimeIntervalSeconds -> (integer)

Inserts EXT-X-PROGRAM-DATE-TIME tags in the output manifest at the interval that you specify. If you donât enter an interval, EXT-X-PROGRAM-DATE-TIME tags arenât included in the manifest. The tags sync the stream to the wall clock so that viewers can seek to a specific time in the playback timeline on the player.

Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it is passed through to the HLS output.

FilterConfiguration -> (structure)

Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.

ManifestFilter -> (string)

Optionally specify one or more manifest filters for all of your manifest egress requests. When you include a manifest filter, note that you cannot use an identical manifest filter query parameter for this manifestâs endpoint URL.

Start -> (timestamp)

Optionally specify the start time for all of your manifest egress requests. When you include start time, note that you cannot use start time query parameters for this manifestâs endpoint URL.

End -> (timestamp)

Optionally specify the end time for all of your manifest egress requests. When you include end time, note that you cannot use end time query parameters for this manifestâs endpoint URL.

TimeDelaySeconds -> (integer)

Optionally specify the time delay for all of your manifest egress requests. Enter a value that is smaller than your endpointâs startover window. When you include time delay, note that you cannot use time delay query parameters for this manifestâs endpoint URL.

ClipStartTime -> (timestamp)

Optionally specify the clip start time for all of your manifest egress requests. When you include clip start time, note that you cannot use clip start time query parameters for this manifestâs endpoint URL.

UrlEncodeChildManifest -> (boolean)

When enabled, MediaPackage URL-encodes the query string for API requests for LL-HLS child manifests to comply with Amazon Web Services Signature Version 4 (SigV4) signature signing protocol. For more information, see [Amazon Web Services Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in *Identity and Access Management User Guide* .

Shorthand Syntax:

```
ManifestName=string,ChildManifestName=string,ScteHls={AdMarkerHls=string},StartTag={TimeOffset=float,Precise=boolean},ManifestWindowSeconds=integer,ProgramDateTimeIntervalSeconds=integer,FilterConfiguration={ManifestFilter=string,Start=timestamp,End=timestamp,TimeDelaySeconds=integer,ClipStartTime=timestamp},UrlEncodeChildManifest=boolean ...
```

JSON Syntax:

```
[
  {
    "ManifestName": "string",
    "ChildManifestName": "string",
    "ScteHls": {
      "AdMarkerHls": "DATERANGE"
    },
    "StartTag": {
      "TimeOffset": float,
      "Precise": true|false
    },
    "ManifestWindowSeconds": integer,
    "ProgramDateTimeIntervalSeconds": integer,
    "FilterConfiguration": {
      "ManifestFilter": "string",
      "Start": timestamp,
      "End": timestamp,
      "TimeDelaySeconds": integer,
      "ClipStartTime": timestamp
    },
    "UrlEncodeChildManifest": true|false
  }
  ...
]
```

`--dash-manifests` (list)

A DASH manifest configuration.

(structure)

Create a DASH manifest configuration.

ManifestName -> (string)

A short string thatâs appended to the endpoint URL. The child manifest name creates a unique path to this endpoint.

ManifestWindowSeconds -> (integer)

The total duration (in seconds) of the manifestâs content.

FilterConfiguration -> (structure)

Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.

ManifestFilter -> (string)

Optionally specify one or more manifest filters for all of your manifest egress requests. When you include a manifest filter, note that you cannot use an identical manifest filter query parameter for this manifestâs endpoint URL.

Start -> (timestamp)

Optionally specify the start time for all of your manifest egress requests. When you include start time, note that you cannot use start time query parameters for this manifestâs endpoint URL.

End -> (timestamp)

Optionally specify the end time for all of your manifest egress requests. When you include end time, note that you cannot use end time query parameters for this manifestâs endpoint URL.

TimeDelaySeconds -> (integer)

Optionally specify the time delay for all of your manifest egress requests. Enter a value that is smaller than your endpointâs startover window. When you include time delay, note that you cannot use time delay query parameters for this manifestâs endpoint URL.

ClipStartTime -> (timestamp)

Optionally specify the clip start time for all of your manifest egress requests. When you include clip start time, note that you cannot use clip start time query parameters for this manifestâs endpoint URL.

MinUpdatePeriodSeconds -> (integer)

Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest.

MinBufferTimeSeconds -> (integer)

Minimum amount of content (in seconds) that a player must keep available in the buffer.

SuggestedPresentationDelaySeconds -> (integer)

The amount of time (in seconds) that the player should be from the end of the manifest.

SegmentTemplateFormat -> (string)

Determines the type of variable used in the `media` URL of the `SegmentTemplate` tag in the manifest. Also specifies if segment timeline information is included in `SegmentTimeline` or `SegmentTemplate` .

Value description:

- `NUMBER_WITH_TIMELINE` - The `$Number$` variable is used in the `media` URL. The value of this variable is the sequential number of the segment. A full `SegmentTimeline` object is presented in each `SegmentTemplate` .

PeriodTriggers -> (list)

A list of triggers that controls when AWS Elemental MediaPackage separates the MPEG-DASH manifest into multiple periods. Type `ADS` to indicate that AWS Elemental MediaPackage must create periods in the output manifest that correspond to SCTE-35 ad markers in the input source. Leave this value empty to indicate that the manifest is contained all in one period. For more information about periods in the DASH manifest, see [Multi-period DASH in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/userguide/multi-period.html) .

(string)

ScteDash -> (structure)

The SCTE configuration.

AdMarkerDash -> (string)

Choose how ad markers are included in the packaged content. If you include ad markers in the content stream in your upstream encoders, then you need to inform MediaPackage what to do with the ad markers in the output.

Value description:

- `Binary` - The SCTE-35 marker is expressed as a hex-string (Base64 string) rather than full XML.
- `XML` - The SCTE marker is expressed fully in XML.

DrmSignaling -> (string)

Determines how the DASH manifest signals the DRM content.

UtcTiming -> (structure)

Determines the type of UTC timing included in the DASH Media Presentation Description (MPD).

TimingMode -> (string)

The UTC timing mode.

TimingSource -> (string)

The the method that the player uses to synchronize to coordinated universal time (UTC) wall clock time.

Profiles -> (list)

The profile that the output is compliant with.

(string)

BaseUrls -> (list)

The base URLs to use for retrieving segments.

(structure)

The base URLs to use for retrieving segments. You can specify multiple locations and indicate the priority and weight for when each should be used, for use in mutli-CDN workflows.

Url -> (string)

A source location for segments.

ServiceLocation -> (string)

The name of the source location.

DvbPriority -> (integer)

For use with DVB-DASH profiles only. The priority of this location for servings segments. The lower the number, the higher the priority.

DvbWeight -> (integer)

For use with DVB-DASH profiles only. The weighting for source locations that have the same priority.

ProgramInformation -> (structure)

Details about the content that you want MediaPackage to pass through in the manifest to the playback device.

Title -> (string)

The title for the manifest.

Source -> (string)

Information about the content provider.

Copyright -> (string)

A copyright statement about the content.

LanguageCode -> (string)

The language code for this manifest.

MoreInformationUrl -> (string)

An absolute URL that contains more information about this content.

DvbSettings -> (structure)

For endpoints that use the DVB-DASH profile only. The font download and error reporting information that you want MediaPackage to pass through to the manifest.

FontDownload -> (structure)

Subtitle font settings.

Url -> (string)

The URL for downloading fonts for subtitles.

MimeType -> (string)

The `mimeType` of the resource thatâs at the font download URL.

For information about font MIME types, see the [MPEG-DASH Profile for Transport of ISO BMFF Based DVB Services over IP Based Networks](https://dvb.org/wp-content/uploads/2021/06/A168r4_MPEG-DASH-Profile-for-Transport-of-ISO-BMFF-Based-DVB-Services_Draft-ts_103-285-v140_November_2021.pdf) document.

FontFamily -> (string)

The `fontFamily` name for subtitles, as described in [EBU-TT-D Subtitling Distribution Format](https://tech.ebu.ch/publications/tech3380) .

ErrorMetrics -> (list)

Playback device error reporting settings.

(structure)

For use with DVB-DASH profiles only. The settings for error reporting from the playback device that you want Elemental MediaPackage to pass through to the manifest.

ReportingUrl -> (string)

The URL where playback devices send error reports.

Probability -> (integer)

The number of playback devices per 1000 that will send error reports to the reporting URL. This represents the probability that a playback device will be a reporting player for this session.

Compactness -> (string)

The layout of the DASH manifest that MediaPackage produces. `STANDARD` indicates a default manifest, which is compacted. `NONE` indicates a full manifest.

For information about compactness, see [DASH manifest compactness](https://docs.aws.amazon.com/mediapackage/latest/userguide/compacted.html) in the *Elemental MediaPackage v2 User Guide* .

SubtitleConfiguration -> (structure)

The configuration for DASH subtitles.

TtmlConfiguration -> (structure)

Settings for TTML subtitles.

TtmlProfile -> (string)

The profile that MediaPackage uses when signaling subtitles in the manifest. `IMSC` is the default profile. `EBU-TT-D` produces subtitles that are compliant with the EBU-TT-D TTML profile. MediaPackage passes through subtitle styles to the manifest. For more information about EBU-TT-D subtitles, see [EBU-TT-D Subtitling Distribution Format](https://tech.ebu.ch/publications/tech3380) .

JSON Syntax:

```
[
  {
    "ManifestName": "string",
    "ManifestWindowSeconds": integer,
    "FilterConfiguration": {
      "ManifestFilter": "string",
      "Start": timestamp,
      "End": timestamp,
      "TimeDelaySeconds": integer,
      "ClipStartTime": timestamp
    },
    "MinUpdatePeriodSeconds": integer,
    "MinBufferTimeSeconds": integer,
    "SuggestedPresentationDelaySeconds": integer,
    "SegmentTemplateFormat": "NUMBER_WITH_TIMELINE",
    "PeriodTriggers": ["AVAILS"|"DRM_KEY_ROTATION"|"SOURCE_CHANGES"|"SOURCE_DISRUPTIONS"|"NONE", ...],
    "ScteDash": {
      "AdMarkerDash": "BINARY"|"XML"
    },
    "DrmSignaling": "INDIVIDUAL"|"REFERENCED",
    "UtcTiming": {
      "TimingMode": "HTTP_HEAD"|"HTTP_ISO"|"HTTP_XSDATE"|"UTC_DIRECT",
      "TimingSource": "string"
    },
    "Profiles": ["DVB_DASH", ...],
    "BaseUrls": [
      {
        "Url": "string",
        "ServiceLocation": "string",
        "DvbPriority": integer,
        "DvbWeight": integer
      }
      ...
    ],
    "ProgramInformation": {
      "Title": "string",
      "Source": "string",
      "Copyright": "string",
      "LanguageCode": "string",
      "MoreInformationUrl": "string"
    },
    "DvbSettings": {
      "FontDownload": {
        "Url": "string",
        "MimeType": "string",
        "FontFamily": "string"
      },
      "ErrorMetrics": [
        {
          "ReportingUrl": "string",
          "Probability": integer
        }
        ...
      ]
    },
    "Compactness": "STANDARD"|"NONE",
    "SubtitleConfiguration": {
      "TtmlConfiguration": {
        "TtmlProfile": "IMSC_1"|"EBU_TT_D_101"
      }
    }
  }
  ...
]
```

`--force-endpoint-error-configuration` (structure)

The failover settings for the endpoint.

EndpointErrorConditions -> (list)

The failover conditions for the endpoint. The options are:

- `STALE_MANIFEST` - The manifest stalled and there are no new segments or parts.
- `INCOMPLETE_MANIFEST` - There is a gap in the manifest.
- `MISSING_DRM_KEY` - Key rotation is enabled but weâre unable to fetch the key for the current key period.
- `SLATE_INPUT` - The segments which contain slate content are considered to be missing content.

(string)

Shorthand Syntax:

```
EndpointErrorConditions=string,string
```

JSON Syntax:

```
{
  "EndpointErrorConditions": ["STALE_MANIFEST"|"INCOMPLETE_MANIFEST"|"MISSING_DRM_KEY"|"SLATE_INPUT", ...]
}
```

`--e-tag` (string)

The expected current Entity Tag (ETag) for the resource. If the specified ETag does not match the resourceâs current entity tag, the update request will be rejected.

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

Arn -> (string)

The ARN associated with the resource.

ChannelGroupName -> (string)

The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.

ChannelName -> (string)

The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.

OriginEndpointName -> (string)

The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.

ContainerType -> (string)

The type of container attached to this origin endpoint.

Segment -> (structure)

The segment configuration, including the segment name, duration, and other configuration values.

SegmentDurationSeconds -> (integer)

The duration (in seconds) of each segment. Enter a value equal to, or a multiple of, the input segment duration. If the value that you enter is different from the input segment duration, MediaPackage rounds segments to the nearest multiple of the input segment duration.

SegmentName -> (string)

The name that describes the segment. The name is the base name of the segment used in all content manifests inside of the endpoint. You canât use spaces in the name.

TsUseAudioRenditionGroup -> (boolean)

When selected, MediaPackage bundles all audio tracks in a rendition group. All other tracks in the stream can be used with any audio rendition from the group.

IncludeIframeOnlyStreams -> (boolean)

When selected, the stream set includes an additional I-frame only stream, along with the other tracks. If false, this extra stream is not included. MediaPackage generates an I-frame only stream from the first rendition in the manifest. The service inserts EXT-I-FRAMES-ONLY tags in the output manifest, and then generates and includes an I-frames only playlist in the stream. This playlist permits player functionality like fast forward and rewind.

TsIncludeDvbSubtitles -> (boolean)

By default, MediaPackage excludes all digital video broadcasting (DVB) subtitles from the output. When selected, MediaPackage passes through DVB subtitles into the output.

Scte -> (structure)

The SCTE configuration options in the segment settings.

ScteFilter -> (list)

The SCTE-35 message types that you want to be treated as ad markers in the output.

(string)

Encryption -> (structure)

The parameters for encrypting content.

ConstantInitializationVector -> (string)

A 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting content. If you donât specify a value, then MediaPackage creates the constant initialization vector (IV).

EncryptionMethod -> (structure)

The encryption method to use.

TsEncryptionMethod -> (string)

The encryption method to use.

CmafEncryptionMethod -> (string)

The encryption method to use.

KeyRotationIntervalSeconds -> (integer)

The frequency (in seconds) of key changes for live workflows, in which content is streamed real time. The service retrieves content keys before the live content begins streaming, and then retrieves them as needed over the lifetime of the workflow. By default, key rotation is set to 300 seconds (5 minutes), the minimum rotation interval, which is equivalent to setting it to 300. If you donât enter an interval, content keys arenât rotated.

The following example setting causes the service to rotate keys every thirty minutes: `1800`

SpekeKeyProvider -> (structure)

The parameters for the SPEKE key provider.

EncryptionContractConfiguration -> (structure)

Configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use.

PresetSpeke20Audio -> (string)

A collection of audio encryption presets.

Value description:

- PRESET-AUDIO-1 - Use one content key to encrypt all of the audio tracks in your stream.
- PRESET-AUDIO-2 - Use one content key to encrypt all of the stereo audio tracks and one content key to encrypt all of the multichannel audio tracks.
- PRESET-AUDIO-3 - Use one content key to encrypt all of the stereo audio tracks, one content key to encrypt all of the multichannel audio tracks with 3 to 6 channels, and one content key to encrypt all of the multichannel audio tracks with more than 6 channels.
- SHARED - Use the same content key for all of the audio and video tracks in your stream.
- UNENCRYPTED - Donât encrypt any of the audio tracks in your stream.

PresetSpeke20Video -> (string)

A collection of video encryption presets.

Value description:

- PRESET-VIDEO-1 - Use one content key to encrypt all of the video tracks in your stream.
- PRESET-VIDEO-2 - Use one content key to encrypt all of the SD video tracks and one content key for all HD and higher resolutions video tracks.
- PRESET-VIDEO-3 - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks and one content key for all UHD video tracks.
- PRESET-VIDEO-4 - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
- PRESET-VIDEO-5 - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
- PRESET-VIDEO-6 - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks.
- PRESET-VIDEO-7 - Use one content key to encrypt all of the SD+HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks.
- PRESET-VIDEO-8 - Use one content key to encrypt all of the SD+HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
- SHARED - Use the same content key for all of the video and audio tracks in your stream.
- UNENCRYPTED - Donât encrypt any of the video tracks in your stream.

ResourceId -> (string)

The unique identifier for the content. The service sends this to the key server to identify the current endpoint. How unique you make this depends on how fine-grained you want access controls to be. The service does not permit you to use the same ID for two simultaneous encryption processes. The resource ID is also known as the content ID.

The following example shows a resource ID: `MovieNight20171126093045`

DrmSystems -> (list)

The DRM solution provider youâre using to protect your content during distribution.

(string)

RoleArn -> (string)

The ARN for the IAM role granted by the key provider that provides access to the key provider API. This role must have a trust policy that allows MediaPackage to assume the role, and it must have a sufficient permissions policy to allow access to the specific key retrieval URL. Get this from your DRM solution provider.

Valid format: `arn:aws:iam::{accountID}:role/{name}` . The following example shows a role ARN: `arn:aws:iam::444455556666:role/SpekeAccess`

Url -> (string)

The URL of the API Gateway proxy that you set up to talk to your key server. The API Gateway proxy must reside in the same AWS Region as MediaPackage and must start with [https://](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/update-origin-endpoint.html).

The following example shows a URL: `https://1wm2dx1f33.execute-api.us-west-2.amazonaws.com/SpekeSample/copyProtection`

CreatedAt -> (timestamp)

The date and time the origin endpoint was created.

ModifiedAt -> (timestamp)

The date and time the origin endpoint was modified.

Description -> (string)

The description of the origin endpoint.

StartoverWindowSeconds -> (integer)

The size of the window (in seconds) to create a window of the live stream thatâs available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window.

HlsManifests -> (list)

An HTTP live streaming (HLS) manifest configuration.

(structure)

Retrieve the HTTP live streaming (HLS) manifest configuration.

ManifestName -> (string)

A short short string thatâs appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you donât enter a value, MediaPackage uses the default manifest name, index. MediaPackage automatically inserts the format extension, such as .m3u8. You canât use the same manifest name if you use HLS manifest and low-latency HLS manifest. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.

Url -> (string)

The egress domain URL for stream delivery from MediaPackage.

ChildManifestName -> (string)

A short string thatâs appended to the endpoint URL. The child manifest name creates a unique path to this endpoint. If you donât enter a value, MediaPackage uses the default child manifest name, index_1. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.

ManifestWindowSeconds -> (integer)

The total duration (in seconds) of the manifestâs content.

ProgramDateTimeIntervalSeconds -> (integer)

Inserts EXT-X-PROGRAM-DATE-TIME tags in the output manifest at the interval that you specify. If you donât enter an interval, EXT-X-PROGRAM-DATE-TIME tags arenât included in the manifest. The tags sync the stream to the wall clock so that viewers can seek to a specific time in the playback timeline on the player.

Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it is passed through to the HLS output.

ScteHls -> (structure)

The SCTE configuration.

AdMarkerHls -> (string)

Ad markers indicate when ads should be inserted during playback. If you include ad markers in the content stream in your upstream encoders, then you need to inform MediaPackage what to do with the ad markers in the output. Choose what you want MediaPackage to do with the ad markers.

Value description:

- DATERANGE - Insert EXT-X-DATERANGE tags to signal ad and program transition events in TS and CMAF manifests. If you use DATERANGE, you must set a programDateTimeIntervalSeconds value of 1 or higher. To learn more about DATERANGE, see [SCTE-35 Ad Marker EXT-X-DATERANGE](http://docs.aws.amazon.com/mediapackage/latest/ug/scte-35-ad-marker-ext-x-daterange.html) .

FilterConfiguration -> (structure)

Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.

ManifestFilter -> (string)

Optionally specify one or more manifest filters for all of your manifest egress requests. When you include a manifest filter, note that you cannot use an identical manifest filter query parameter for this manifestâs endpoint URL.

Start -> (timestamp)

Optionally specify the start time for all of your manifest egress requests. When you include start time, note that you cannot use start time query parameters for this manifestâs endpoint URL.

End -> (timestamp)

Optionally specify the end time for all of your manifest egress requests. When you include end time, note that you cannot use end time query parameters for this manifestâs endpoint URL.

TimeDelaySeconds -> (integer)

Optionally specify the time delay for all of your manifest egress requests. Enter a value that is smaller than your endpointâs startover window. When you include time delay, note that you cannot use time delay query parameters for this manifestâs endpoint URL.

ClipStartTime -> (timestamp)

Optionally specify the clip start time for all of your manifest egress requests. When you include clip start time, note that you cannot use clip start time query parameters for this manifestâs endpoint URL.

StartTag -> (structure)

To insert an EXT-X-START tag in your HLS playlist, specify a StartTag configuration object with a valid TimeOffset. When you do, you can also optionally specify whether to include a PRECISE value in the EXT-X-START tag.

TimeOffset -> (float)

Specify the value for TIME-OFFSET within your EXT-X-START tag. Enter a signed floating point value which, if positive, must be less than the configured manifest duration minus three times the configured segment target duration. If negative, the absolute value must be larger than three times the configured segment target duration, and the absolute value must be smaller than the configured manifest duration.

Precise -> (boolean)

Specify the value for PRECISE within your EXT-X-START tag. Leave blank, or choose false, to use the default value NO. Choose yes to use the value YES.

UrlEncodeChildManifest -> (boolean)

When enabled, MediaPackage URL-encodes the query string for API requests for HLS child manifests to comply with Amazon Web Services Signature Version 4 (SigV4) signature signing protocol. For more information, see [Amazon Web Services Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in *Identity and Access Management User Guide* .

LowLatencyHlsManifests -> (list)

A low-latency HLS manifest configuration.

(structure)

Retrieve the low-latency HTTP live streaming (HLS) manifest configuration.

ManifestName -> (string)

A short short string thatâs appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you donât enter a value, MediaPackage uses the default manifest name, index. MediaPackage automatically inserts the format extension, such as .m3u8. You canât use the same manifest name if you use HLS manifest and low-latency HLS manifest. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.

Url -> (string)

The egress domain URL for stream delivery from MediaPackage.

ChildManifestName -> (string)

A short string thatâs appended to the endpoint URL. The child manifest name creates a unique path to this endpoint. If you donât enter a value, MediaPackage uses the default child manifest name, index_1. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.

ManifestWindowSeconds -> (integer)

The total duration (in seconds) of the manifestâs content.

ProgramDateTimeIntervalSeconds -> (integer)

Inserts EXT-X-PROGRAM-DATE-TIME tags in the output manifest at the interval that you specify. If you donât enter an interval, EXT-X-PROGRAM-DATE-TIME tags arenât included in the manifest. The tags sync the stream to the wall clock so that viewers can seek to a specific time in the playback timeline on the player.

Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it is passed through to the HLS output.

ScteHls -> (structure)

The SCTE configuration.

AdMarkerHls -> (string)

Ad markers indicate when ads should be inserted during playback. If you include ad markers in the content stream in your upstream encoders, then you need to inform MediaPackage what to do with the ad markers in the output. Choose what you want MediaPackage to do with the ad markers.

Value description:

- DATERANGE - Insert EXT-X-DATERANGE tags to signal ad and program transition events in TS and CMAF manifests. If you use DATERANGE, you must set a programDateTimeIntervalSeconds value of 1 or higher. To learn more about DATERANGE, see [SCTE-35 Ad Marker EXT-X-DATERANGE](http://docs.aws.amazon.com/mediapackage/latest/ug/scte-35-ad-marker-ext-x-daterange.html) .

FilterConfiguration -> (structure)

Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.

ManifestFilter -> (string)

Optionally specify one or more manifest filters for all of your manifest egress requests. When you include a manifest filter, note that you cannot use an identical manifest filter query parameter for this manifestâs endpoint URL.

Start -> (timestamp)

Optionally specify the start time for all of your manifest egress requests. When you include start time, note that you cannot use start time query parameters for this manifestâs endpoint URL.

End -> (timestamp)

Optionally specify the end time for all of your manifest egress requests. When you include end time, note that you cannot use end time query parameters for this manifestâs endpoint URL.

TimeDelaySeconds -> (integer)

Optionally specify the time delay for all of your manifest egress requests. Enter a value that is smaller than your endpointâs startover window. When you include time delay, note that you cannot use time delay query parameters for this manifestâs endpoint URL.

ClipStartTime -> (timestamp)

Optionally specify the clip start time for all of your manifest egress requests. When you include clip start time, note that you cannot use clip start time query parameters for this manifestâs endpoint URL.

StartTag -> (structure)

To insert an EXT-X-START tag in your HLS playlist, specify a StartTag configuration object with a valid TimeOffset. When you do, you can also optionally specify whether to include a PRECISE value in the EXT-X-START tag.

TimeOffset -> (float)

Specify the value for TIME-OFFSET within your EXT-X-START tag. Enter a signed floating point value which, if positive, must be less than the configured manifest duration minus three times the configured segment target duration. If negative, the absolute value must be larger than three times the configured segment target duration, and the absolute value must be smaller than the configured manifest duration.

Precise -> (boolean)

Specify the value for PRECISE within your EXT-X-START tag. Leave blank, or choose false, to use the default value NO. Choose yes to use the value YES.

UrlEncodeChildManifest -> (boolean)

When enabled, MediaPackage URL-encodes the query string for API requests for LL-HLS child manifests to comply with Amazon Web Services Signature Version 4 (SigV4) signature signing protocol. For more information, see [Amazon Web Services Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in *Identity and Access Management User Guide* .

ForceEndpointErrorConfiguration -> (structure)

The failover settings for the endpoint.

EndpointErrorConditions -> (list)

The failover conditions for the endpoint. The options are:

- `STALE_MANIFEST` - The manifest stalled and there are no new segments or parts.
- `INCOMPLETE_MANIFEST` - There is a gap in the manifest.
- `MISSING_DRM_KEY` - Key rotation is enabled but weâre unable to fetch the key for the current key period.
- `SLATE_INPUT` - The segments which contain slate content are considered to be missing content.

(string)

ETag -> (string)

The current Entity Tag (ETag) associated with this resource. The entity tag can be used to safely make concurrent updates to the resource.

Tags -> (map)

The comma-separated list of tag key:value pairs assigned to the origin endpoint.

key -> (string)

value -> (string)

DashManifests -> (list)

A DASH manifest configuration.

(structure)

Retrieve the DASH manifest configuration.

ManifestName -> (string)

A short string thatâs appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you donât enter a value, MediaPackage uses the default manifest name, index.

Url -> (string)

The egress domain URL for stream delivery from MediaPackage.

ManifestWindowSeconds -> (integer)

The total duration (in seconds) of the manifestâs content.

FilterConfiguration -> (structure)

Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.

ManifestFilter -> (string)

Optionally specify one or more manifest filters for all of your manifest egress requests. When you include a manifest filter, note that you cannot use an identical manifest filter query parameter for this manifestâs endpoint URL.

Start -> (timestamp)

Optionally specify the start time for all of your manifest egress requests. When you include start time, note that you cannot use start time query parameters for this manifestâs endpoint URL.

End -> (timestamp)

Optionally specify the end time for all of your manifest egress requests. When you include end time, note that you cannot use end time query parameters for this manifestâs endpoint URL.

TimeDelaySeconds -> (integer)

Optionally specify the time delay for all of your manifest egress requests. Enter a value that is smaller than your endpointâs startover window. When you include time delay, note that you cannot use time delay query parameters for this manifestâs endpoint URL.

ClipStartTime -> (timestamp)

Optionally specify the clip start time for all of your manifest egress requests. When you include clip start time, note that you cannot use clip start time query parameters for this manifestâs endpoint URL.

MinUpdatePeriodSeconds -> (integer)

Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest.

MinBufferTimeSeconds -> (integer)

Minimum amount of content (in seconds) that a player must keep available in the buffer.

SuggestedPresentationDelaySeconds -> (integer)

The amount of time (in seconds) that the player should be from the end of the manifest.

SegmentTemplateFormat -> (string)

Determines the type of variable used in the `media` URL of the `SegmentTemplate` tag in the manifest. Also specifies if segment timeline information is included in `SegmentTimeline` or `SegmentTemplate` .

Value description:

- `NUMBER_WITH_TIMELINE` - The `$Number$` variable is used in the `media` URL. The value of this variable is the sequential number of the segment. A full `SegmentTimeline` object is presented in each `SegmentTemplate` .

PeriodTriggers -> (list)

A list of triggers that controls when AWS Elemental MediaPackage separates the MPEG-DASH manifest into multiple periods. Leave this value empty to indicate that the manifest is contained all in one period. For more information about periods in the DASH manifest, see [Multi-period DASH in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/userguide/multi-period.html) .

(string)

ScteDash -> (structure)

The SCTE configuration.

AdMarkerDash -> (string)

Choose how ad markers are included in the packaged content. If you include ad markers in the content stream in your upstream encoders, then you need to inform MediaPackage what to do with the ad markers in the output.

Value description:

- `Binary` - The SCTE-35 marker is expressed as a hex-string (Base64 string) rather than full XML.
- `XML` - The SCTE marker is expressed fully in XML.

DrmSignaling -> (string)

Determines how the DASH manifest signals the DRM content.

UtcTiming -> (structure)

Determines the type of UTC timing included in the DASH Media Presentation Description (MPD).

TimingMode -> (string)

The UTC timing mode.

TimingSource -> (string)

The the method that the player uses to synchronize to coordinated universal time (UTC) wall clock time.

Profiles -> (list)

The profile that the output is compliant with.

(string)

BaseUrls -> (list)

The base URL to use for retrieving segments.

(structure)

The base URLs to use for retrieving segments. You can specify multiple locations and indicate the priority and weight for when each should be used, for use in mutli-CDN workflows.

Url -> (string)

A source location for segments.

ServiceLocation -> (string)

The name of the source location.

DvbPriority -> (integer)

For use with DVB-DASH profiles only. The priority of this location for servings segments. The lower the number, the higher the priority.

DvbWeight -> (integer)

For use with DVB-DASH profiles only. The weighting for source locations that have the same priority.

ProgramInformation -> (structure)

Details about the content that you want MediaPackage to pass through in the manifest to the playback device.

Title -> (string)

The title for the manifest.

Source -> (string)

Information about the content provider.

Copyright -> (string)

A copyright statement about the content.

LanguageCode -> (string)

The language code for this manifest.

MoreInformationUrl -> (string)

An absolute URL that contains more information about this content.

DvbSettings -> (structure)

For endpoints that use the DVB-DASH profile only. The font download and error reporting information that you want MediaPackage to pass through to the manifest.

FontDownload -> (structure)

Subtitle font settings.

Url -> (string)

The URL for downloading fonts for subtitles.

MimeType -> (string)

The `mimeType` of the resource thatâs at the font download URL.

For information about font MIME types, see the [MPEG-DASH Profile for Transport of ISO BMFF Based DVB Services over IP Based Networks](https://dvb.org/wp-content/uploads/2021/06/A168r4_MPEG-DASH-Profile-for-Transport-of-ISO-BMFF-Based-DVB-Services_Draft-ts_103-285-v140_November_2021.pdf) document.

FontFamily -> (string)

The `fontFamily` name for subtitles, as described in [EBU-TT-D Subtitling Distribution Format](https://tech.ebu.ch/publications/tech3380) .

ErrorMetrics -> (list)

Playback device error reporting settings.

(structure)

For use with DVB-DASH profiles only. The settings for error reporting from the playback device that you want Elemental MediaPackage to pass through to the manifest.

ReportingUrl -> (string)

The URL where playback devices send error reports.

Probability -> (integer)

The number of playback devices per 1000 that will send error reports to the reporting URL. This represents the probability that a playback device will be a reporting player for this session.

Compactness -> (string)

The layout of the DASH manifest that MediaPackage produces. `STANDARD` indicates a default manifest, which is compacted. `NONE` indicates a full manifest.

SubtitleConfiguration -> (structure)

The configuration for DASH subtitles.

TtmlConfiguration -> (structure)

Settings for TTML subtitles.

TtmlProfile -> (string)

The profile that MediaPackage uses when signaling subtitles in the manifest. `IMSC` is the default profile. `EBU-TT-D` produces subtitles that are compliant with the EBU-TT-D TTML profile. MediaPackage passes through subtitle styles to the manifest. For more information about EBU-TT-D subtitles, see [EBU-TT-D Subtitling Distribution Format](https://tech.ebu.ch/publications/tech3380) .