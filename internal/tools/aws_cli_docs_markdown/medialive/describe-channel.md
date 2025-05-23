# describe-channelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-channel.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-channel.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [medialive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/index.html#cli-aws-medialive) ]

# describe-channel

## Description

Gets details about a channel

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DescribeChannel)

## Synopsis

```
describe-channel
--channel-id <value>
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

`--channel-id` (string)
channel ID

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

The unique arn of the channel.

CdiInputSpecification -> (structure)

Specification of CDI inputs for this channel

Resolution -> (string)

Maximum CDI input resolution

ChannelClass -> (string)

The class for this channel. STANDARD for a channel with two pipelines or SINGLE_PIPELINE for a channel with one pipeline.

Destinations -> (list)

A list of destinations of the channel. For UDP outputs, there is one destination per output. For other types (HLS, for example), there is one destination per packager.

(structure)

Placeholder documentation for OutputDestination

Id -> (string)

User-specified id. This is used in an output group or an output.

MediaPackageSettings -> (list)

Destination settings for a MediaPackage output; one destination for both encoders.

(structure)

MediaPackage Output Destination Settings

ChannelId -> (string)

ID of the channel in MediaPackage that is the destination for this output group. You do not need to specify the individual inputs in MediaPackage; MediaLive will handle the connection of the two MediaLive pipelines to the two MediaPackage inputs. The MediaPackage channel and MediaLive channel must be in the same region.

ChannelGroup -> (string)

Name of the channel group in MediaPackageV2. Only use if you are sending CMAF Ingest output to a CMAF ingest endpoint on a MediaPackage channel that uses MediaPackage v2.

ChannelName -> (string)

Name of the channel in MediaPackageV2. Only use if you are sending CMAF Ingest output to a CMAF ingest endpoint on a MediaPackage channel that uses MediaPackage v2.

MultiplexSettings -> (structure)

Destination settings for a Multiplex output; one destination for both encoders.

MultiplexId -> (string)

The ID of the Multiplex that the encoder is providing output to. You do not need to specify the individual inputs to the Multiplex; MediaLive will handle the connection of the two MediaLive pipelines to the two Multiplex instances. The Multiplex must be in the same region as the Channel.

ProgramName -> (string)

The program name of the Multiplex program that the encoder is providing output to.

Settings -> (list)

Destination settings for a standard output; one destination for each redundant encoder.

(structure)

Placeholder documentation for OutputDestinationSettings

PasswordParam -> (string)

key used to extract the password from EC2 Parameter store

StreamName -> (string)

Stream name for RTMP destinations (URLs of type rtmp://)

Url -> (string)

A URL specifying a destination

Username -> (string)

username for destination

SrtSettings -> (list)

SRT settings for an SRT output; one destination for each redundant encoder.

(structure)

Placeholder documentation for SrtOutputDestinationSettings

EncryptionPassphraseSecretArn -> (string)

Arn used to extract the password from Secrets Manager

StreamId -> (string)

Stream id for SRT destinations (URLs of type srt://)

Url -> (string)

A URL specifying a destination

LogicalInterfaceNames -> (list)

Optional assignment of an output to a logical interface on the Node. Only applies to on premises channels.

(string)

Placeholder documentation for __string

EgressEndpoints -> (list)

The endpoints where outgoing connections initiate from

(structure)

Placeholder documentation for ChannelEgressEndpoint

SourceIp -> (string)

Public IP of where a channelâs output comes from

EncoderSettings -> (structure)

Encoder Settings

AudioDescriptions -> (list)

Placeholder documentation for __listOfAudioDescription

(structure)

Audio Description

AudioNormalizationSettings -> (structure)

Advanced audio normalization settings.

Algorithm -> (string)

Audio normalization algorithm to use. itu17701 conforms to the CALM Act specification, itu17702 conforms to the EBU R-128 specification.

AlgorithmControl -> (string)

When set to correctAudio the output audio is corrected using the chosen algorithm. If set to measureOnly, the audio will be measured but not adjusted.

TargetLkfs -> (double)

Target LKFS(loudness) to adjust volume to. If no value is entered, a default value will be used according to the chosen algorithm. The CALM Act (1770-1) recommends a target of -24 LKFS. The EBU R-128 specification (1770-2) recommends a target of -23 LKFS.

AudioSelectorName -> (string)

The name of the AudioSelector used as the source for this AudioDescription.

AudioType -> (string)

Applies only if audioTypeControl is useConfigured. The values for audioType are defined in ISO-IEC 13818-1.

AudioTypeControl -> (string)

Determines how audio type is determined. followInput: If the input contains an ISO 639 audioType, then that value is passed through to the output. If the input contains no ISO 639 audioType, the value in Audio Type is included in the output. useConfigured: The value in Audio Type is included in the output. Note that this field and audioType are both ignored if inputType is broadcasterMixedAd.

AudioWatermarkingSettings -> (structure)

Settings to configure one or more solutions that insert audio watermarks in the audio encode

NielsenWatermarksSettings -> (structure)

Settings to configure Nielsen Watermarks in the audio encode

NielsenCbetSettings -> (structure)

Complete these fields only if you want to insert watermarks of type Nielsen CBET

CbetCheckDigitString -> (string)

Enter the CBET check digits to use in the watermark.

CbetStepaside -> (string)

Determines the method of CBET insertion mode when prior encoding is detected on the same layer.

Csid -> (string)

Enter the CBET Source ID (CSID) to use in the watermark

NielsenDistributionType -> (string)

Choose the distribution types that you want to assign to the watermarks: - PROGRAM_CONTENT - FINAL_DISTRIBUTOR

NielsenNaesIiNwSettings -> (structure)

Complete these fields only if you want to insert watermarks of type Nielsen NAES II (N2) and Nielsen NAES VI (NW).

CheckDigitString -> (string)

Enter the check digit string for the watermark

Sid -> (double)

Enter the Nielsen Source ID (SID) to include in the watermark

Timezone -> (string)

Choose the timezone for the time stamps in the watermark. If not provided, the timestamps will be in Coordinated Universal Time (UTC)

CodecSettings -> (structure)

Audio codec settings.

AacSettings -> (structure)

Aac Settings

Bitrate -> (double)

Average bitrate in bits/second. Valid values depend on rate control mode and profile.

CodingMode -> (string)

Mono, Stereo, or 5.1 channel layout. Valid values depend on rate control mode and profile. The adReceiverMix setting receives a stereo description plus control track and emits a mono AAC encode of the description track, with control data emitted in the PES header as per ETSI TS 101 154 Annex E.

InputType -> (string)

Set to âbroadcasterMixedAdâ when input contains pre-mixed main audio + AD (narration) as a stereo pair. The Audio Type field (audioType) will be set to 3, which signals to downstream systems that this stream contains âbroadcaster mixed ADâ. Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. The values in audioTypeControl and audioType (in AudioDescription) are ignored when set to broadcasterMixedAd. Leave set to ânormalâ when input does not contain pre-mixed audio + AD.

Profile -> (string)

AAC Profile.

RateControlMode -> (string)

Rate Control Mode.

RawFormat -> (string)

Sets LATM / LOAS AAC output for raw containers.

SampleRate -> (double)

Sample rate in Hz. Valid values depend on rate control mode and profile.

Spec -> (string)

Use MPEG-2 AAC audio instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers.

VbrQuality -> (string)

VBR Quality Level - Only used if rateControlMode is VBR.

Ac3Settings -> (structure)

Ac3 Settings

Bitrate -> (double)

Average bitrate in bits/second. Valid bitrates depend on the coding mode.

BitstreamMode -> (string)

Specifies the bitstream mode (bsmod) for the emitted AC-3 stream. See ATSC A/52-2012 for background on these values.

CodingMode -> (string)

Dolby Digital coding mode. Determines number of channels.

Dialnorm -> (integer)

Sets the dialnorm for the output. If excluded and input audio is Dolby Digital, dialnorm will be passed through.

DrcProfile -> (string)

If set to filmStandard, adds dynamic range compression signaling to the output bitstream as defined in the Dolby Digital specification.

LfeFilter -> (string)

When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid in codingMode32Lfe mode.

MetadataControl -> (string)

When set to âfollowInputâ, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.

AttenuationControl -> (string)

Applies a 3 dB attenuation to the surround channels. Applies only when the coding mode parameter is CODING_MODE_3_2_LFE.

Eac3AtmosSettings -> (structure)

Eac3 Atmos Settings

Bitrate -> (double)

Average bitrate in bits/second. Valid bitrates depend on the coding mode.

CodingMode -> (string)

Dolby Digital Plus with Dolby Atmos coding mode. Determines number of channels.

Dialnorm -> (integer)

Sets the dialnorm for the output. Default 23.

DrcLine -> (string)

Sets the Dolby dynamic range compression profile.

DrcRf -> (string)

Sets the profile for heavy Dolby dynamic range compression, ensures that the instantaneous signal peaks do not exceed specified levels.

HeightTrim -> (double)

Height dimensional trim. Sets the maximum amount to attenuate the height channels when the downstream player isn??t configured to handle Dolby Digital Plus with Dolby Atmos and must remix the channels.

SurroundTrim -> (double)

Surround dimensional trim. Sets the maximum amount to attenuate the surround channels when the downstream player isnât configured to handle Dolby Digital Plus with Dolby Atmos and must remix the channels.

Eac3Settings -> (structure)

Eac3 Settings

AttenuationControl -> (string)

When set to attenuate3Db, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode.

Bitrate -> (double)

Average bitrate in bits/second. Valid bitrates depend on the coding mode.

BitstreamMode -> (string)

Specifies the bitstream mode (bsmod) for the emitted E-AC-3 stream. See ATSC A/52-2012 (Annex E) for background on these values.

CodingMode -> (string)

Dolby Digital Plus coding mode. Determines number of channels.

DcFilter -> (string)

When set to enabled, activates a DC highpass filter for all input channels.

Dialnorm -> (integer)

Sets the dialnorm for the output. If blank and input audio is Dolby Digital Plus, dialnorm will be passed through.

DrcLine -> (string)

Sets the Dolby dynamic range compression profile.

DrcRf -> (string)

Sets the profile for heavy Dolby dynamic range compression, ensures that the instantaneous signal peaks do not exceed specified levels.

LfeControl -> (string)

When encoding 3/2 audio, setting to lfe enables the LFE channel

LfeFilter -> (string)

When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with codingMode32 coding mode.

LoRoCenterMixLevel -> (double)

Left only/Right only center mix level. Only used for 3/2 coding mode.

LoRoSurroundMixLevel -> (double)

Left only/Right only surround mix level. Only used for 3/2 coding mode.

LtRtCenterMixLevel -> (double)

Left total/Right total center mix level. Only used for 3/2 coding mode.

LtRtSurroundMixLevel -> (double)

Left total/Right total surround mix level. Only used for 3/2 coding mode.

MetadataControl -> (string)

When set to followInput, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.

PassthroughControl -> (string)

When set to whenPossible, input DD+ audio will be passed through if it is present on the input. This detection is dynamic over the life of the transcode. Inputs that alternate between DD+ and non-DD+ content will have a consistent DD+ output as the system alternates between passthrough and encoding.

PhaseControl -> (string)

When set to shift90Degrees, applies a 90-degree phase shift to the surround channels. Only used for 3/2 coding mode.

StereoDownmix -> (string)

Stereo downmix preference. Only used for 3/2 coding mode.

SurroundExMode -> (string)

When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels.

SurroundMode -> (string)

When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels.

Mp2Settings -> (structure)

Mp2 Settings

Bitrate -> (double)

Average bitrate in bits/second.

CodingMode -> (string)

The MPEG2 Audio coding mode. Valid values are codingMode10 (for mono) or codingMode20 (for stereo).

SampleRate -> (double)

Sample rate in Hz.

PassThroughSettings -> (structure)

Pass Through Settings

WavSettings -> (structure)

Wav Settings

BitDepth -> (double)

Bits per sample.

CodingMode -> (string)

The audio coding mode for the WAV audio. The mode determines the number of channels in the audio.

SampleRate -> (double)

Sample rate in Hz.

LanguageCode -> (string)

RFC 5646 language code representing the language of the audio output track. Only used if languageControlMode is useConfigured, or there is no ISO 639 language code specified in the input.

LanguageCodeControl -> (string)

Choosing followInput will cause the ISO 639 language code of the output to follow the ISO 639 language code of the input. The languageCode will be used when useConfigured is set, or when followInput is selected but there is no ISO 639 language code specified by the input.

Name -> (string)

The name of this AudioDescription. Outputs will use this name to uniquely identify this AudioDescription. Description names should be unique within this Live Event.

RemixSettings -> (structure)

Settings that control how input audio channels are remixed into the output audio channels.

ChannelMappings -> (list)

Mapping of input channels to output channels, with appropriate gain adjustments.

(structure)

Audio Channel Mapping

InputChannelLevels -> (list)

Indices and gain values for each input channel that should be remixed into this output channel.

(structure)

Input Channel Level

Gain -> (integer)

Remixing value. Units are in dB and acceptable values are within the range from -60 (mute) and 6 dB.

InputChannel -> (integer)

The index of the input channel used as a source.

OutputChannel -> (integer)

The index of the output channel being produced.

ChannelsIn -> (integer)

Number of input channels to be used.

ChannelsOut -> (integer)

Number of output channels to be produced. Valid values: 1, 2, 4, 6, 8

StreamName -> (string)

Used for MS Smooth and Apple HLS outputs. Indicates the name displayed by the player (eg. English, or Director Commentary).

AudioDashRoles -> (list)

Identifies the DASH roles to assign to this audio output. Applies only when the audio output is configured for DVB DASH accessibility signaling.

(string)

Dash Role Audio

DvbDashAccessibility -> (string)

Identifies DVB DASH accessibility signaling in this audio output. Used in Microsoft Smooth Streaming outputs to signal accessibility information to packagers.

AvailBlanking -> (structure)

Settings for ad avail blanking.

AvailBlankingImage -> (structure)

Blanking image to be used. Leave empty for solid black. Only bmp and png images are supported.

PasswordParam -> (string)

key used to extract the password from EC2 Parameter store

Uri -> (string)

Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a [http://](http://) URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: ârtmp://fmsserver/liveâ.

Username -> (string)

Documentation update needed

State -> (string)

When set to enabled, causes video, audio and captions to be blanked when insertion metadata is added.

AvailConfiguration -> (structure)

Event-wide configuration settings for ad avail insertion.

AvailSettings -> (structure)

Controls how SCTE-35 messages create cues. Splice Insert mode treats all segmentation signals traditionally. With Time Signal APOS mode only Time Signal Placement Opportunity and Break messages create segment breaks. With ESAM mode, signals are forwarded to an ESAM server for possible update.

Esam -> (structure)

Esam

AcquisitionPointId -> (string)

Sent as acquisitionPointIdentity to identify the MediaLive channel to the POIS.

AdAvailOffset -> (integer)

When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages.

PasswordParam -> (string)

Documentation update needed

PoisEndpoint -> (string)

The URL of the signal conditioner endpoint on the Placement Opportunity Information System (POIS). MediaLive sends SignalProcessingEvents here when SCTE-35 messages are read.

Username -> (string)

Documentation update needed

ZoneIdentity -> (string)

Optional data sent as zoneIdentity to identify the MediaLive channel to the POIS.

Scte35SpliceInsert -> (structure)

Typical configuration that applies breaks on splice inserts in addition to time signal placement opportunities, breaks, and advertisements.

AdAvailOffset -> (integer)

When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages.

NoRegionalBlackoutFlag -> (string)

When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to 0 will no longer trigger blackouts or Ad Avail slates

WebDeliveryAllowedFlag -> (string)

When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to 0 will no longer trigger blackouts or Ad Avail slates

Scte35TimeSignalApos -> (structure)

Atypical configuration that applies segment breaks only on SCTE-35 time signal placement opportunities and breaks.

AdAvailOffset -> (integer)

When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages.

NoRegionalBlackoutFlag -> (string)

When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to 0 will no longer trigger blackouts or Ad Avail slates

WebDeliveryAllowedFlag -> (string)

When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to 0 will no longer trigger blackouts or Ad Avail slates

Scte35SegmentationScope -> (string)

Configures whether SCTE 35 passthrough triggers segment breaks in all output groups that use segmented outputs. Insertion of a SCTE 35 message typically results in a segment break, in addition to the regular cadence of breaks. The segment breaks appear in video outputs, audio outputs, and captions outputs (if any). ALL_OUTPUT_GROUPS: Default. Insert the segment break in in all output groups that have segmented outputs. This is the legacy behavior. SCTE35_ENABLED_OUTPUT_GROUPS: Insert the segment break only in output groups that have SCTE 35 passthrough enabled. This is the recommended value, because it reduces unnecessary segment breaks.

BlackoutSlate -> (structure)

Settings for blackout slate.

BlackoutSlateImage -> (structure)

Blackout slate image to be used. Leave empty for solid black. Only bmp and png images are supported.

PasswordParam -> (string)

key used to extract the password from EC2 Parameter store

Uri -> (string)

Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a [http://](http://) URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: ârtmp://fmsserver/liveâ.

Username -> (string)

Documentation update needed

NetworkEndBlackout -> (string)

Setting to enabled causes the encoder to blackout the video, audio, and captions, and raise the âNetwork Blackout Imageâ slate when an SCTE104/35 Network End Segmentation Descriptor is encountered. The blackout will be lifted when the Network Start Segmentation Descriptor is encountered. The Network End and Network Start descriptors must contain a network ID that matches the value entered in âNetwork IDâ.

NetworkEndBlackoutImage -> (structure)

Path to local file to use as Network End Blackout image. Image will be scaled to fill the entire output raster.

PasswordParam -> (string)

key used to extract the password from EC2 Parameter store

Uri -> (string)

Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a [http://](http://) URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: ârtmp://fmsserver/liveâ.

Username -> (string)

Documentation update needed

NetworkId -> (string)

Provides Network ID that matches EIDR ID format (e.g., â10.XXXX/XXXX-XXXX-XXXX-XXXX-XXXX-Câ).

State -> (string)

When set to enabled, causes video, audio and captions to be blanked when indicated by program metadata.

CaptionDescriptions -> (list)

Settings for caption decriptions

(structure)

Caption Description

Accessibility -> (string)

Indicates whether the caption track implements accessibility features such as written descriptions of spoken dialog, music, and sounds. This signaling is added to HLS output group and MediaPackage output group.

CaptionSelectorName -> (string)

Specifies which input caption selector to use as a caption source when generating output captions. This field should match a captionSelector name.

DestinationSettings -> (structure)

Additional settings for captions destination that depend on the destination type.

AribDestinationSettings -> (structure)

Arib Destination Settings

BurnInDestinationSettings -> (structure)

Burn In Destination Settings

Alignment -> (string)

If no explicit xPosition or yPosition is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Selecting âsmartâ justification will left-justify live subtitles and center-justify pre-recorded subtitles. All burn-in and DVB-Sub font settings must match.

BackgroundColor -> (string)

Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.

BackgroundOpacity -> (integer)

Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.

Font -> (structure)

External font file used for caption burn-in. File extension must be âttfâ or âtteâ. Although the user can select output fonts for many different types of input captions, embedded, STL and teletext sources use a strict grid system. Using external fonts with these caption sources could cause unexpected display of proportional fonts. All burn-in and DVB-Sub font settings must match.

PasswordParam -> (string)

key used to extract the password from EC2 Parameter store

Uri -> (string)

Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a [http://](http://) URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: ârtmp://fmsserver/liveâ.

Username -> (string)

Documentation update needed

FontColor -> (string)

Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.

FontOpacity -> (integer)

Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.

FontResolution -> (integer)

Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.

FontSize -> (string)

When set to âautoâ fontSize will scale depending on the size of the output. Giving a positive integer will specify the exact font size in points. All burn-in and DVB-Sub font settings must match.

OutlineColor -> (string)

Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.

OutlineSize -> (integer)

Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.

ShadowColor -> (string)

Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.

ShadowOpacity -> (integer)

Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.

ShadowXOffset -> (integer)

Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.

ShadowYOffset -> (integer)

Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.

TeletextGridControl -> (string)

Controls whether a fixed grid size will be used to generate the output subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in outputs.

XPosition -> (integer)

Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit xPosition is provided, the horizontal caption position will be determined by the alignment parameter. All burn-in and DVB-Sub font settings must match.

YPosition -> (integer)

Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit yPosition is provided, the caption will be positioned towards the bottom of the output. All burn-in and DVB-Sub font settings must match.

DvbSubDestinationSettings -> (structure)

Dvb Sub Destination Settings

Alignment -> (string)

If no explicit xPosition or yPosition is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Selecting âsmartâ justification will left-justify live subtitles and center-justify pre-recorded subtitles. This option is not valid for source captions that are STL or 608/embedded. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.

BackgroundColor -> (string)

Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.

BackgroundOpacity -> (integer)

Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.

Font -> (structure)

External font file used for caption burn-in. File extension must be âttfâ or âtteâ. Although the user can select output fonts for many different types of input captions, embedded, STL and teletext sources use a strict grid system. Using external fonts with these caption sources could cause unexpected display of proportional fonts. All burn-in and DVB-Sub font settings must match.

PasswordParam -> (string)

key used to extract the password from EC2 Parameter store

Uri -> (string)

Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a [http://](http://) URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: ârtmp://fmsserver/liveâ.

Username -> (string)

Documentation update needed

FontColor -> (string)

Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.

FontOpacity -> (integer)

Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.

FontResolution -> (integer)

Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.

FontSize -> (string)

When set to auto fontSize will scale depending on the size of the output. Giving a positive integer will specify the exact font size in points. All burn-in and DVB-Sub font settings must match.

OutlineColor -> (string)

Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.

OutlineSize -> (integer)

Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.

ShadowColor -> (string)

Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.

ShadowOpacity -> (integer)

Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.

ShadowXOffset -> (integer)

Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.

ShadowYOffset -> (integer)

Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.

TeletextGridControl -> (string)

Controls whether a fixed grid size will be used to generate the output subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in outputs.

XPosition -> (integer)

Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit xPosition is provided, the horizontal caption position will be determined by the alignment parameter. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.

YPosition -> (integer)

Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit yPosition is provided, the caption will be positioned towards the bottom of the output. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.

EbuTtDDestinationSettings -> (structure)

Ebu Tt DDestination Settings

CopyrightHolder -> (string)

Complete this field if you want to include the name of the copyright holder in the copyright tag in the captions metadata.

FillLineGap -> (string)

Specifies how to handle the gap between the lines (in multi-line captions). ENABLED: Fill with the captions background color (as specified in the input captions). DISABLED: Leave the gap unfilled

FontFamily -> (string)

Specifies the font family to include in the font data attached to the EBU-TT captions. Valid only if style_control is set to include. (If style_control is set to exclude, the font family is always set to monospaced.) Enter a list of font families, as a comma-separated list of font names, in order of preference. The name can be a font family (such as Arial), or a generic font family (such as serif), or default (to let the downstream player choose the font). Or leave blank to set the family to monospace. Note that you can specify only the font family. All other style information (color, bold, position and so on) is copied from the input captions. The size is always set to 100% to allow the downstream player to choose the size.

StyleControl -> (string)

Specifies the style information to include in the font data that is attached to the EBU-TT captions. INCLUDE: Take the style information from the source captions and include that information in the font data attached to the EBU-TT captions. This option is valid only if the source captions are Embedded or Teletext. EXCLUDE: Set the font family to monospaced. Do not include any other style information.

DefaultFontSize -> (integer)

Specifies the default font size as a percentage of the computed cell size. Valid only if the defaultLineHeight is also set. If you leave this field empty, the default font size is 80% of the cell size.

DefaultLineHeight -> (integer)

Documentation update needed

EmbeddedDestinationSettings -> (structure)

Embedded Destination Settings

EmbeddedPlusScte20DestinationSettings -> (structure)

Embedded Plus Scte20 Destination Settings

RtmpCaptionInfoDestinationSettings -> (structure)

Rtmp Caption Info Destination Settings

Scte20PlusEmbeddedDestinationSettings -> (structure)

Scte20 Plus Embedded Destination Settings

Scte27DestinationSettings -> (structure)

Scte27 Destination Settings

SmpteTtDestinationSettings -> (structure)

Smpte Tt Destination Settings

TeletextDestinationSettings -> (structure)

Teletext Destination Settings

TtmlDestinationSettings -> (structure)

Ttml Destination Settings

StyleControl -> (string)

This field is not currently supported and will not affect the output styling. Leave the default value.

WebvttDestinationSettings -> (structure)

Webvtt Destination Settings

StyleControl -> (string)

Controls whether the color and position of the source captions is passed through to the WebVTT output captions. PASSTHROUGH - Valid only if the source captions are EMBEDDED or TELETEXT. NO_STYLE_DATA - Donât pass through the style. The output captions will not contain any font styling information.

LanguageCode -> (string)

ISO 639-2 three-digit code: [http://www.loc.gov/standards/iso639-2/](http://www.loc.gov/standards/iso639-2/)

LanguageDescription -> (string)

Human readable information to indicate captions available for players (eg. English, or Spanish).

Name -> (string)

Name of the caption description. Used to associate a caption description with an output. Names must be unique within an event.

CaptionDashRoles -> (list)

Identifies the DASH roles to assign to this captions output. Applies only when the captions output is configured for DVB DASH accessibility signaling.

(string)

Dash Role Caption

DvbDashAccessibility -> (string)

Identifies DVB DASH accessibility signaling in this captions output. Used in Microsoft Smooth Streaming outputs to signal accessibility information to packagers.

FeatureActivations -> (structure)

Feature Activations

InputPrepareScheduleActions -> (string)

Enables the Input Prepare feature. You can create Input Prepare actions in the schedule only if this feature is enabled. If you disable the feature on an existing schedule, make sure that you first delete all input prepare actions from the schedule.

OutputStaticImageOverlayScheduleActions -> (string)

Enables the output static image overlay feature. Enabling this feature allows you to send channel schedule updates to display/clear/modify image overlays on an output-by-output bases.

GlobalConfiguration -> (structure)

Configuration settings that apply to the event as a whole.

InitialAudioGain -> (integer)

Value to set the initial audio gain for the Live Event.

InputEndAction -> (string)

Indicates the action to take when the current input completes (e.g. end-of-file). When switchAndLoopInputs is configured the encoder will restart at the beginning of the first input. When ânoneâ is configured the encoder will transcode either black, a solid color, or a user specified slate images per the âInput Loss Behaviorâ configuration until the next input switch occurs (which is controlled through the Channel Schedule API).

InputLossBehavior -> (structure)

Settings for system actions when input is lost.

BlackFrameMsec -> (integer)

Documentation update needed

InputLossImageColor -> (string)

When input loss image type is âcolorâ this field specifies the color to use. Value: 6 hex characters representing the values of RGB.

InputLossImageSlate -> (structure)

When input loss image type is âslateâ these fields specify the parameters for accessing the slate.

PasswordParam -> (string)

key used to extract the password from EC2 Parameter store

Uri -> (string)

Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a [http://](http://) URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: ârtmp://fmsserver/liveâ.

Username -> (string)

Documentation update needed

InputLossImageType -> (string)

Indicates whether to substitute a solid color or a slate into the output after input loss exceeds blackFrameMsec.

RepeatFrameMsec -> (integer)

Documentation update needed

OutputLockingMode -> (string)

Indicates how MediaLive pipelines are synchronized. PIPELINE_LOCKING - MediaLive will attempt to synchronize the output of each pipeline to the other. EPOCH_LOCKING - MediaLive will attempt to synchronize the output of each pipeline to the Unix epoch. DISABLED - MediaLive will not attempt to synchronize the output of pipelines. We advise against disabling output locking because it has negative side effects in most workflows. For more information, see the section about output locking (pipeline locking) in the Medialive user guide.

OutputTimingSource -> (string)

Indicates whether the rate of frames emitted by the Live encoder should be paced by its system clock (which optionally may be locked to another source via NTP) or should be locked to the clock of the source that is providing the input stream.

SupportLowFramerateInputs -> (string)

Adjusts video input buffer for streams with very low video framerates. This is commonly set to enabled for music channels with less than one video frame per second.

OutputLockingSettings -> (structure)

Advanced output locking settings

EpochLockingSettings -> (structure)

Epoch Locking Settings

CustomEpoch -> (string)

Optional. Enter a value here to use a custom epoch, instead of the standard epoch (which started at 1970-01-01T00:00:00 UTC). Specify the start time of the custom epoch, in YYYY-MM-DDTHH:MM:SS in UTC. The time must be 2000-01-01T00:00:00 or later. Always set the MM:SS portion to 00:00.

JamSyncTime -> (string)

Optional. Enter a time for the jam sync. The default is midnight UTC. When epoch locking is enabled, MediaLive performs a daily jam sync on every output encode to ensure timecodes donât diverge from the wall clock. The jam sync applies only to encodes with frame rate of 29.97 or 59.94 FPS. To override, enter a time in HH:MM:SS in UTC. Always set the MM:SS portion to 00:00.

PipelineLockingSettings -> (structure)

Pipeline Locking Settings

MotionGraphicsConfiguration -> (structure)

Settings for motion graphics.

MotionGraphicsInsertion -> (string)

Motion Graphics Insertion

MotionGraphicsSettings -> (structure)

Motion Graphics Settings

HtmlMotionGraphicsSettings -> (structure)

Html Motion Graphics Settings

NielsenConfiguration -> (structure)

Nielsen configuration settings.

DistributorId -> (string)

Enter the Distributor ID assigned to your organization by Nielsen.

NielsenPcmToId3Tagging -> (string)

Enables Nielsen PCM to ID3 tagging

OutputGroups -> (list)

Placeholder documentation for __listOfOutputGroup

(structure)

Output groups for this Live Event. Output groups contain information about where streams should be distributed.

Name -> (string)

Custom output group name optionally defined by the user.

OutputGroupSettings -> (structure)

Settings associated with the output group.

ArchiveGroupSettings -> (structure)

Archive Group Settings

ArchiveCdnSettings -> (structure)

Parameters that control interactions with the CDN.

ArchiveS3Settings -> (structure)

Archive S3 Settings

CannedAcl -> (string)

Specify the canned ACL to apply to each S3 request. Defaults to none.

Destination -> (structure)

A directory and base filename where archive files should be written.

DestinationRefId -> (string)

Placeholder documentation for __string

RolloverInterval -> (integer)

Number of seconds to write to archive file before closing and starting a new one.

FrameCaptureGroupSettings -> (structure)

Frame Capture Group Settings

Destination -> (structure)

The destination for the frame capture files. Either the URI for an Amazon S3 bucket and object, plus a file name prefix (for example, s3ssl://sportsDelivery/highlights/20180820/curling-) or the URI for a MediaStore container, plus a file name prefix (for example, mediastoressl://sportsDelivery/20180820/curling-). The final file names consist of the prefix from the destination field (for example, âcurling-â) + name modifier + the counter (5 digits, starting from 00001) + extension (which is always .jpg). For example, curling-low.00001.jpg

DestinationRefId -> (string)

Placeholder documentation for __string

FrameCaptureCdnSettings -> (structure)

Parameters that control interactions with the CDN.

FrameCaptureS3Settings -> (structure)

Frame Capture S3 Settings

CannedAcl -> (string)

Specify the canned ACL to apply to each S3 request. Defaults to none.

HlsGroupSettings -> (structure)

Hls Group Settings

AdMarkers -> (list)

Choose one or more ad marker types to pass SCTE35 signals through to this group of Apple HLS outputs.

(string)

Hls Ad Markers

BaseUrlContent -> (string)

A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file.

BaseUrlContent1 -> (string)

Optional. One value per output group. This field is required only if you are completing Base URL content A, and the downstream system has notified you that the media files for pipeline 1 of all outputs are in a location different from the media files for pipeline 0.

BaseUrlManifest -> (string)

A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file.

BaseUrlManifest1 -> (string)

Optional. One value per output group. Complete this field only if you are completing Base URL manifest A, and the downstream system has notified you that the child manifest files for pipeline 1 of all outputs are in a location different from the child manifest files for pipeline 0.

CaptionLanguageMappings -> (list)

Mapping of up to 4 caption channels to caption languages. Is only meaningful if captionLanguageSetting is set to âinsertâ.

(structure)

Maps a caption channel to an ISO 693-2 language code ([http://www.loc.gov/standards/iso639-2](http://www.loc.gov/standards/iso639-2)), with an optional description.

CaptionChannel -> (integer)

The closed caption channel being described by this CaptionLanguageMapping. Each channel mapping must have a unique channel number (maximum of 4)

LanguageCode -> (string)

Three character ISO 639-2 language code (see [http://www.loc.gov/standards/iso639-2](http://www.loc.gov/standards/iso639-2))

LanguageDescription -> (string)

Textual description of language

CaptionLanguageSetting -> (string)

Applies only to 608 Embedded output captions. insert: Include CLOSED-CAPTIONS lines in the manifest. Specify at least one language in the CC1 Language Code field. One CLOSED-CAPTION line is added for each Language Code you specify. Make sure to specify the languages in the order in which they appear in the original source (if the source is embedded format) or the order of the caption selectors (if the source is other than embedded). Otherwise, languages in the manifest will not match up properly with the output captions. none: Include CLOSED-CAPTIONS=NONE line in the manifest. omit: Omit any CLOSED-CAPTIONS line from the manifest.

ClientCache -> (string)

When set to âdisabledâ, sets the #EXT-X-ALLOW-CACHE:no tag in the manifest, which prevents clients from saving media segments for later replay.

CodecSpecification -> (string)

Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation.

ConstantIv -> (string)

For use with encryptionType. This is a 128-bit, 16-byte hex value represented by a 32-character text string. If ivSource is set to âexplicitâ then this parameter is required and is used as the IV for encryption.

Destination -> (structure)

A directory or HTTP destination for the HLS segments, manifest files, and encryption keys (if enabled).

DestinationRefId -> (string)

Placeholder documentation for __string

DirectoryStructure -> (string)

Place segments in subdirectories.

DiscontinuityTags -> (string)

Specifies whether to insert EXT-X-DISCONTINUITY tags in the HLS child manifests for this output group. Typically, choose Insert because these tags are required in the manifest (according to the HLS specification) and serve an important purpose. Choose Never Insert only if the downstream system is doing real-time failover (without using the MediaLive automatic failover feature) and only if that downstream system has advised you to exclude the tags.

EncryptionType -> (string)

Encrypts the segments with the given encryption scheme. Exclude this parameter if no encryption is desired.

HlsCdnSettings -> (structure)

Parameters that control interactions with the CDN.

HlsAkamaiSettings -> (structure)

Hls Akamai Settings

ConnectionRetryInterval -> (integer)

Number of seconds to wait before retrying connection to the CDN if the connection is lost.

FilecacheDuration -> (integer)

Size in seconds of file cache for streaming outputs.

HttpTransferMode -> (string)

Specify whether or not to use chunked transfer encoding to Akamai. User should contact Akamai to enable this feature.

NumRetries -> (integer)

Number of retry attempts that will be made before the Live Event is put into an error state. Applies only if the CDN destination URI begins with âs3â or âmediastoreâ. For other URIs, the value is always 3.

RestartDelay -> (integer)

If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.

Salt -> (string)

Salt for authenticated Akamai.

Token -> (string)

Token parameter for authenticated akamai. If not specified, _gda_ is used.

HlsBasicPutSettings -> (structure)

Hls Basic Put Settings

ConnectionRetryInterval -> (integer)

Number of seconds to wait before retrying connection to the CDN if the connection is lost.

FilecacheDuration -> (integer)

Size in seconds of file cache for streaming outputs.

NumRetries -> (integer)

Number of retry attempts that will be made before the Live Event is put into an error state. Applies only if the CDN destination URI begins with âs3â or âmediastoreâ. For other URIs, the value is always 3.

RestartDelay -> (integer)

If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.

HlsMediaStoreSettings -> (structure)

Hls Media Store Settings

ConnectionRetryInterval -> (integer)

Number of seconds to wait before retrying connection to the CDN if the connection is lost.

FilecacheDuration -> (integer)

Size in seconds of file cache for streaming outputs.

MediaStoreStorageClass -> (string)

When set to temporal, output files are stored in non-persistent memory for faster reading and writing.

NumRetries -> (integer)

Number of retry attempts that will be made before the Live Event is put into an error state. Applies only if the CDN destination URI begins with âs3â or âmediastoreâ. For other URIs, the value is always 3.

RestartDelay -> (integer)

If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.

HlsS3Settings -> (structure)

Hls S3 Settings

CannedAcl -> (string)

Specify the canned ACL to apply to each S3 request. Defaults to none.

HlsWebdavSettings -> (structure)

Hls Webdav Settings

ConnectionRetryInterval -> (integer)

Number of seconds to wait before retrying connection to the CDN if the connection is lost.

FilecacheDuration -> (integer)

Size in seconds of file cache for streaming outputs.

HttpTransferMode -> (string)

Specify whether or not to use chunked transfer encoding to WebDAV.

NumRetries -> (integer)

Number of retry attempts that will be made before the Live Event is put into an error state. Applies only if the CDN destination URI begins with âs3â or âmediastoreâ. For other URIs, the value is always 3.

RestartDelay -> (integer)

If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.

HlsId3SegmentTagging -> (string)

State of HLS ID3 Segment Tagging

IFrameOnlyPlaylists -> (string)

DISABLED: Do not create an I-frame-only manifest, but do create the master and media manifests (according to the Output Selection field). STANDARD: Create an I-frame-only manifest for each output that contains video, as well as the other manifests (according to the Output Selection field). The I-frame manifest contains a #EXT-X-I-FRAMES-ONLY tag to indicate it is I-frame only, and one or more #EXT-X-BYTERANGE entries identifying the I-frame position. For example, #EXT-X-BYTERANGE:160364@1461888â

IncompleteSegmentBehavior -> (string)

Specifies whether to include the final (incomplete) segment in the media output when the pipeline stops producing output because of a channel stop, a channel pause or a loss of input to the pipeline. Auto means that MediaLive decides whether to include the final segment, depending on the channel class and the types of output groups. Suppress means to never include the incomplete segment. We recommend you choose Auto and let MediaLive control the behavior.

IndexNSegments -> (integer)

Applies only if Mode field is LIVE. Specifies the maximum number of segments in the media manifest file. After this maximum, older segments are removed from the media manifest. This number must be smaller than the number in the Keep Segments field.

InputLossAction -> (string)

Parameter that control output group behavior on input loss.

IvInManifest -> (string)

For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If set to âincludeâ, IV is listed in the manifest, otherwise the IV is not in the manifest.

IvSource -> (string)

For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If this setting is âfollowsSegmentNumberâ, it will cause the IV to change every segment (to match the segment number). If this is set to âexplicitâ, you must enter a constantIv value.

KeepSegments -> (integer)

Applies only if Mode field is LIVE. Specifies the number of media segments to retain in the destination directory. This number should be bigger than indexNSegments (Num segments). We recommend (value = (2 x indexNsegments) + 1). If this âkeep segmentsâ number is too low, the following might happen: the player is still reading a media manifest file that lists this segment, but that segment has been removed from the destination directory (as directed by indexNSegments). This situation would result in a 404 HTTP error on the player.

KeyFormat -> (string)

The value specifies how the key is represented in the resource identified by the URI. If parameter is absent, an implicit value of âidentityâ is used. A reverse DNS string can also be given.

KeyFormatVersions -> (string)

Either a single positive integer version value or a slash delimited list of version values (1/2/3).

KeyProviderSettings -> (structure)

The key provider settings.

StaticKeySettings -> (structure)

Static Key Settings

KeyProviderServer -> (structure)

The URL of the license server used for protecting content.

PasswordParam -> (string)

key used to extract the password from EC2 Parameter store

Uri -> (string)

Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a [http://](http://) URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: ârtmp://fmsserver/liveâ.

Username -> (string)

Documentation update needed

StaticKeyValue -> (string)

Static key value as a 32 character hexadecimal string.

ManifestCompression -> (string)

When set to gzip, compresses HLS playlist.

ManifestDurationFormat -> (string)

Indicates whether the output manifest should use floating point or integer values for segment duration.

MinSegmentLength -> (integer)

Minimum length of MPEG-2 Transport Stream segments in seconds. When set, minimum segment length is enforced by looking ahead and back within the specified range for a nearby avail and extending the segment size if needed.

Mode -> (string)

If âvodâ, all segments are indexed and kept permanently in the destination and manifest. If âliveâ, only the number segments specified in keepSegments and indexNSegments are kept; newer segments replace older segments, which may prevent players from rewinding all the way to the beginning of the event. VOD mode uses HLS EXT-X-PLAYLIST-TYPE of EVENT while the channel is running, converting it to a âVODâ type manifest on completion of the stream.

OutputSelection -> (string)

MANIFESTS_AND_SEGMENTS: Generates manifests (master manifest, if applicable, and media manifests) for this output group. VARIANT_MANIFESTS_AND_SEGMENTS: Generates media manifests for this output group, but not a master manifest. SEGMENTS_ONLY: Does not generate any manifests for this output group.

ProgramDateTime -> (string)

Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is calculated using the program date time clock.

ProgramDateTimeClock -> (string)

Specifies the algorithm used to drive the HLS EXT-X-PROGRAM-DATE-TIME clock. Options include: INITIALIZE_FROM_OUTPUT_TIMECODE: The PDT clock is initialized as a function of the first output timecode, then incremented by the EXTINF duration of each encoded segment. SYSTEM_CLOCK: The PDT clock is initialized as a function of the UTC wall clock, then incremented by the EXTINF duration of each encoded segment. If the PDT clock diverges from the wall clock by more than 500ms, it is resynchronized to the wall clock.

ProgramDateTimePeriod -> (integer)

Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds.

RedundantManifest -> (string)

ENABLED: The master manifest (.m3u8 file) for each pipeline includes information about both pipelines: first its own media files, then the media files of the other pipeline. This feature allows playout device that support stale manifest detection to switch from one manifest to the other, when the current manifest seems to be stale. There are still two destinations and two master manifests, but both master manifests reference the media files from both pipelines. DISABLED: The master manifest (.m3u8 file) for each pipeline includes information about its own pipeline only. For an HLS output group with MediaPackage as the destination, the DISABLED behavior is always followed. MediaPackage regenerates the manifests it serves to players so a redundant manifest from MediaLive is irrelevant.

SegmentLength -> (integer)

Length of MPEG-2 Transport Stream segments to create in seconds. Note that segments will end on the next keyframe after this duration, so actual segment length may be longer.

SegmentationMode -> (string)

useInputSegmentation has been deprecated. The configured segment size is always used.

SegmentsPerSubdirectory -> (integer)

Number of segments to write to a subdirectory before starting a new one. directoryStructure must be subdirectoryPerStream for this setting to have an effect.

StreamInfResolution -> (string)

Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest.

TimedMetadataId3Frame -> (string)

Indicates ID3 frame that has the timecode.

TimedMetadataId3Period -> (integer)

Timed Metadata interval in seconds.

TimestampDeltaMilliseconds -> (integer)

Provides an extra millisecond delta offset to fine tune the timestamps.

TsFileMode -> (string)

SEGMENTED_FILES: Emit the program as segments - multiple .ts media files. SINGLE_FILE: Applies only if Mode field is VOD. Emit the program as a single .ts media file. The media manifest includes #EXT-X-BYTERANGE tags to index segments for playback. A typical use for this value is when sending the output to AWS Elemental MediaConvert, which can accept only a single media file. Playback while the channel is running is not guaranteed due to HTTP server caching.

MediaPackageGroupSettings -> (structure)

Media Package Group Settings

Destination -> (structure)

MediaPackage channel destination.

DestinationRefId -> (string)

Placeholder documentation for __string

MsSmoothGroupSettings -> (structure)

Ms Smooth Group Settings

AcquisitionPointId -> (string)

The ID to include in each message in the sparse track. Ignored if sparseTrackType is NONE.

AudioOnlyTimecodeControl -> (string)

If set to passthrough for an audio-only MS Smooth output, the fragment absolute time will be set to the current timecode. This option does not write timecodes to the audio elementary stream.

CertificateMode -> (string)

If set to verifyAuthenticity, verify the https certificate chain to a trusted Certificate Authority (CA). This will cause https outputs to self-signed certificates to fail.

ConnectionRetryInterval -> (integer)

Number of seconds to wait before retrying connection to the IIS server if the connection is lost. Content will be cached during this time and the cache will be be delivered to the IIS server once the connection is re-established.

Destination -> (structure)

Smooth Streaming publish point on an IIS server. Elemental Live acts as a âPushâ encoder to IIS.

DestinationRefId -> (string)

Placeholder documentation for __string

EventId -> (string)

MS Smooth event ID to be sent to the IIS server. Should only be specified if eventIdMode is set to useConfigured.

EventIdMode -> (string)

Specifies whether or not to send an event ID to the IIS server. If no event ID is sent and the same Live Event is used without changing the publishing point, clients might see cached video from the previous run. Options: - âuseConfiguredâ - use the value provided in eventId - âuseTimestampâ - generate and send an event ID based on the current timestamp - ânoEventIdâ - do not send an event ID to the IIS server.

EventStopBehavior -> (string)

When set to sendEos, send EOS signal to IIS server when stopping the event

FilecacheDuration -> (integer)

Size in seconds of file cache for streaming outputs.

FragmentLength -> (integer)

Length of mp4 fragments to generate (in seconds). Fragment length must be compatible with GOP size and framerate.

InputLossAction -> (string)

Parameter that control output group behavior on input loss.

NumRetries -> (integer)

Number of retry attempts.

RestartDelay -> (integer)

Number of seconds before initiating a restart due to output failure, due to exhausting the numRetries on one segment, or exceeding filecacheDuration.

SegmentationMode -> (string)

useInputSegmentation has been deprecated. The configured segment size is always used.

SendDelayMs -> (integer)

Number of milliseconds to delay the output from the second pipeline.

SparseTrackType -> (string)

Identifies the type of data to place in the sparse track: - SCTE35: Insert SCTE-35 messages from the source content. With each message, insert an IDR frame to start a new segment. - SCTE35_WITHOUT_SEGMENTATION: Insert SCTE-35 messages from the source content. With each message, insert an IDR frame but donât start a new segment. - NONE: Donât generate a sparse track for any outputs in this output group.

StreamManifestBehavior -> (string)

When set to send, send stream manifest so publishing point doesnât start until all streams start.

TimestampOffset -> (string)

Timestamp offset for the event. Only used if timestampOffsetMode is set to useConfiguredOffset.

TimestampOffsetMode -> (string)

Type of timestamp date offset to use. - useEventStartDate: Use the date the event was started as the offset - useConfiguredOffset: Use an explicitly configured date as the offset

MultiplexGroupSettings -> (structure)

Multiplex Group Settings

RtmpGroupSettings -> (structure)

Rtmp Group Settings

AdMarkers -> (list)

Choose the ad marker type for this output group. MediaLive will create a message based on the content of each SCTE-35 message, format it for that marker type, and insert it in the datastream.

(string)

Rtmp Ad Markers

AuthenticationScheme -> (string)

Authentication scheme to use when connecting with CDN

CacheFullBehavior -> (string)

Controls behavior when content cache fills up. If remote origin server stalls the RTMP connection and does not accept content fast enough the âMedia Cacheâ will fill up. When the cache reaches the duration specified by cacheLength the cache will stop accepting new content. If set to disconnectImmediately, the RTMP output will force a disconnect. Clear the media cache, and reconnect after restartDelay seconds. If set to waitForServer, the RTMP output will wait up to 5 minutes to allow the origin server to begin accepting data again.

CacheLength -> (integer)

Cache length, in seconds, is used to calculate buffer size.

CaptionData -> (string)

Controls the types of data that passes to onCaptionInfo outputs. If set to âallâ then 608 and 708 carried DTVCC data will be passed. If set to âfield1AndField2608â then DTVCC data will be stripped out, but 608 data from both fields will be passed. If set to âfield1608â then only the data carried in 608 from field 1 video will be passed.

InputLossAction -> (string)

Controls the behavior of this RTMP group if input becomes unavailable. - emitOutput: Emit a slate until input returns. - pauseOutput: Stop transmitting data until input returns. This does not close the underlying RTMP connection.

RestartDelay -> (integer)

If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.

IncludeFillerNalUnits -> (string)

Applies only when the rate control mode (in the codec settings) is CBR (constant bit rate). Controls whether the RTMP output stream is padded (with FILL NAL units) in order to achieve a constant bit rate that is truly constant. When there is no padding, the bandwidth varies (up to the bitrate value in the codec settings). We recommend that you choose Auto.

UdpGroupSettings -> (structure)

Udp Group Settings

InputLossAction -> (string)

Specifies behavior of last resort when input video is lost, and no more backup inputs are available. When dropTs is selected the entire transport stream will stop being emitted. When dropProgram is selected the program can be dropped from the transport stream (and replaced with null packets to meet the TS bitrate requirement). Or, when emitProgram is chosen the transport stream will continue to be produced normally with repeat frames, black frames, or slate frames substituted for the absent input video.

TimedMetadataId3Frame -> (string)

Indicates ID3 frame that has the timecode.

TimedMetadataId3Period -> (integer)

Timed Metadata interval in seconds.

CmafIngestGroupSettings -> (structure)

Cmaf Ingest Group Settings

Destination -> (structure)

A HTTP destination for the tracks

DestinationRefId -> (string)

Placeholder documentation for __string

NielsenId3Behavior -> (string)

If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.

Scte35Type -> (string)

Type of scte35 track to add. none or scte35WithoutSegmentation

SegmentLength -> (integer)

The nominal duration of segments. The units are specified in SegmentLengthUnits. The segments will end on the next keyframe after the specified duration, so the actual segment length might be longer, and it might be a fraction of the units.

SegmentLengthUnits -> (string)

Time unit for segment length parameter.

SendDelayMs -> (integer)

Number of milliseconds to delay the output from the second pipeline.

KlvBehavior -> (string)

If set to passthrough, passes any KLV data from the input source to this output.

KlvNameModifier -> (string)

Change the modifier that MediaLive automatically adds to the Streams() name that identifies a KLV track. The default is âklvâ, which means the default name will be Streams(klv.cmfm). Any string you enter here will replace the âklvâ string.nThe modifier can only contain: numbers, letters, plus (+), minus (-), underscore (_) and period (.) and has a maximum length of 100 characters.

NielsenId3NameModifier -> (string)

Change the modifier that MediaLive automatically adds to the Streams() name that identifies a Nielsen ID3 track. The default is ânid3â, which means the default name will be Streams(nid3.cmfm). Any string you enter here will replace the ânid3â string.nThe modifier can only contain: numbers, letters, plus (+), minus (-), underscore (_) and period (.) and has a maximum length of 100 characters.

Scte35NameModifier -> (string)

Change the modifier that MediaLive automatically adds to the Streams() name for a SCTE 35 track. The default is âscteâ, which means the default name will be Streams(scte.cmfm). Any string you enter here will replace the âscteâ string.nThe modifier can only contain: numbers, letters, plus (+), minus (-), underscore (_) and period (.) and has a maximum length of 100 characters.

Id3Behavior -> (string)

Set to ENABLED to enable ID3 metadata insertion. To include metadata, you configure other parameters in the output group, or you add an ID3 action to the channel schedule.

Id3NameModifier -> (string)

Change the modifier that MediaLive automatically adds to the Streams() name that identifies an ID3 track. The default is âid3â, which means the default name will be Streams(id3.cmfm). Any string you enter here will replace the âid3â string.nThe modifier can only contain: numbers, letters, plus (+), minus (-), underscore (_) and period (.) and has a maximum length of 100 characters.

CaptionLanguageMappings -> (list)

An array that identifies the languages in the four caption channels in the embedded captions.

(structure)

Add an array item for each language. Follow the order of the caption descriptions. For example, if the first caption description is for German, then the first array item must be for German, and its caption channel must be set to 1. The second array item must be 2, and so on.

CaptionChannel -> (integer)

A number for the channel for this caption, 1 to 4.

LanguageCode -> (string)

Language code for the language of the caption in this channel. For example, ger/deu. See [http://www.loc.gov/standards/iso639-2](http://www.loc.gov/standards/iso639-2)

TimedMetadataId3Frame -> (string)

Set to none if you donât want to insert a timecode in the output. Otherwise choose the frame type for the timecode.

TimedMetadataId3Period -> (integer)

If you set up to insert a timecode in the output, specify the frequency for the frame, in seconds.

TimedMetadataPassthrough -> (string)

Set to enabled to pass through ID3 metadata from the input sources.

SrtGroupSettings -> (structure)

Srt Group Settings

InputLossAction -> (string)

Specifies behavior of last resort when input video is lost, and no more backup inputs are available. When dropTs is selected the entire transport stream will stop being emitted. When dropProgram is selected the program can be dropped from the transport stream (and replaced with null packets to meet the TS bitrate requirement). Or, when emitProgram is chosen the transport stream will continue to be produced normally with repeat frames, black frames, or slate frames substituted for the absent input video.

Outputs -> (list)

Placeholder documentation for __listOfOutput

(structure)

Output settings. There can be multiple outputs within a group.

AudioDescriptionNames -> (list)

The names of the AudioDescriptions used as audio sources for this output.

(string)

Placeholder documentation for __string

CaptionDescriptionNames -> (list)

The names of the CaptionDescriptions used as caption sources for this output.

(string)

Placeholder documentation for __string

OutputName -> (string)

The name used to identify an output.

OutputSettings -> (structure)

Output type-specific settings.

ArchiveOutputSettings -> (structure)

Archive Output Settings

ContainerSettings -> (structure)

Settings specific to the container type of the file.

M2tsSettings -> (structure)

M2ts Settings

AbsentInputAudioBehavior -> (string)

When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream.

Arib -> (string)

When set to enabled, uses ARIB-compliant field muxing and removes video descriptor.

AribCaptionsPid -> (string)

Packet Identifier (PID) for ARIB Captions in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

AribCaptionsPidControl -> (string)

If set to auto, pid number used for ARIB Captions will be auto-selected from unused pids. If set to useConfigured, ARIB Captions will be on the configured pid number.

AudioBufferModel -> (string)

When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used.

AudioFramesPerPes -> (integer)

The number of audio frames to insert for each PES packet.

AudioPids -> (string)

Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).

AudioStreamType -> (string)

When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06.

Bitrate -> (integer)

The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate.

BufferModel -> (string)

Controls the timing accuracy for output network traffic. Leave as MULTIPLEX to ensure accurate network packet timing. Or set to NONE, which might result in lower latency but will result in more variability in output network packet timing. This variability might cause interruptions, jitter, or bursty behavior in your playback or receiving devices.

CcDescriptor -> (string)

When set to enabled, generates captionServiceDescriptor in PMT.

DvbNitSettings -> (structure)

Inserts DVB Network Information Table (NIT) at the specified table repetition interval.

NetworkId -> (integer)

The numeric value placed in the Network Information Table (NIT).

NetworkName -> (string)

The network name text placed in the networkNameDescriptor inside the Network Information Table. Maximum length is 256 characters.

RepInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream.

DvbSdtSettings -> (structure)

Inserts DVB Service Description Table (SDT) at the specified table repetition interval.

OutputSdt -> (string)

Selects method of inserting SDT information into output stream. The sdtFollow setting copies SDT information from input stream to output stream. The sdtFollowIfPresent setting copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. The sdtManual setting means user will enter the SDT information. The sdtNone setting means output stream will not contain SDT information.

RepInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream.

ServiceName -> (string)

The service name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.

ServiceProviderName -> (string)

The service provider name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.

DvbSubPids -> (string)

Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).

DvbTdtSettings -> (structure)

Inserts DVB Time and Date Table (TDT) at the specified table repetition interval.

RepInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream.

DvbTeletextPid -> (string)

Packet Identifier (PID) for input source DVB Teletext data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

Ebif -> (string)

If set to passthrough, passes any EBIF data from the input source to this output.

EbpAudioInterval -> (string)

When videoAndFixedIntervals is selected, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. Only available when EBP Cablelabs segmentation markers are selected. Partitions 1 and 2 will always follow the video interval.

EbpLookaheadMs -> (integer)

When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is âstretchedâ to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate.

EbpPlacement -> (string)

Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP markers will be placed on the video PID and all audio PIDs. If set to videoPid, EBP markers will be placed on only the video PID.

EcmPid -> (string)

This field is unused and deprecated.

EsRateInPes -> (string)

Include or exclude the ES Rate field in the PES header.

EtvPlatformPid -> (string)

Packet Identifier (PID) for input source ETV Platform data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

EtvSignalPid -> (string)

Packet Identifier (PID) for input source ETV Signal data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

FragmentTime -> (double)

The length in seconds of each fragment. Only used with EBP markers.

Klv -> (string)

If set to passthrough, passes any KLV data from the input source to this output.

KlvDataPids -> (string)

Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).

NielsenId3Behavior -> (string)

If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.

NullPacketBitrate -> (double)

Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets.

PatInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.

PcrControl -> (string)

When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.

PcrPeriod -> (integer)

Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream.

PcrPid -> (string)

Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

PmtInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.

PmtPid -> (string)

Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

ProgramNum -> (integer)

The value of the program number field in the Program Map Table.

RateMode -> (string)

When vbr, does not insert null packets into transport stream to fill specified bitrate. The bitrate setting acts as the maximum bitrate when vbr is set.

Scte27Pids -> (string)

Packet Identifier (PID) for input source SCTE-27 data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).

Scte35Control -> (string)

Optionally pass SCTE-35 signals from the input source to this output.

Scte35Pid -> (string)

Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

SegmentationMarkers -> (string)

Inserts segmentation markers at each segmentationTime period. raiSegstart sets the Random Access Indicator bit in the adaptation field. raiAdapt sets the RAI bit and adds the current timecode in the private data bytes. psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.

SegmentationStyle -> (string)

The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of âresetCadenceâ is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of $segmentationTime seconds. When a segmentation style of âmaintainCadenceâ is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentationTime seconds. Note that EBP lookahead is a slight exception to this rule.

SegmentationTime -> (double)

The length in seconds of each segment. Required unless markers is set to _none_.

TimedMetadataBehavior -> (string)

When set to passthrough, timed metadata will be passed through from input to output.

TimedMetadataPid -> (string)

Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

TransportStreamId -> (integer)

The value of the transport stream ID field in the Program Map Table.

VideoPid -> (string)

Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

Scte35PrerollPullupMilliseconds -> (double)

Defines the amount SCTE-35 preroll will be increased (in milliseconds) on the output. Preroll is the amount of time between the presence of a SCTE-35 indication in a transport stream and the PTS of the video frame it references. Zero means donât add pullup (it doesnât mean set the preroll to zero). Negative pullup is not supported, which means that you canât make the preroll shorter. Be aware that latency in the output will increase by the pullup amount.

RawSettings -> (structure)

Raw Settings

Extension -> (string)

Output file extension. If excluded, this will be auto-selected from the container type.

NameModifier -> (string)

String concatenated to the end of the destination filename. Required for multiple outputs of the same type.

FrameCaptureOutputSettings -> (structure)

Frame Capture Output Settings

NameModifier -> (string)

Required if the output group contains more than one output. This modifier forms part of the output file name.

HlsOutputSettings -> (structure)

Hls Output Settings

H265PackagingType -> (string)

Only applicable when this output is referencing an H.265 video description. Specifies whether MP4 segments should be packaged as HEV1 or HVC1.

HlsSettings -> (structure)

Settings regarding the underlying stream. These settings are different for audio-only outputs.

AudioOnlyHlsSettings -> (structure)

Audio Only Hls Settings

AudioGroupId -> (string)

Specifies the group to which the audio Rendition belongs.

AudioOnlyImage -> (structure)

Optional. Specifies the .jpg or .png image to use as the cover art for an audio-only output. We recommend a low bit-size file because the image increases the output audio bandwidth. The image is attached to the audio as an ID3 tag, frame type APIC, picture type 0x10, as per the âID3 tag version 2.4.0 - Native Framesâ standard.

PasswordParam -> (string)

key used to extract the password from EC2 Parameter store

Uri -> (string)

Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a [http://](http://) URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: ârtmp://fmsserver/liveâ.

Username -> (string)

Documentation update needed

AudioTrackType -> (string)

Four types of audio-only tracks are supported: Audio-Only Variant Stream The client can play back this audio-only stream instead of video in low-bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate Audio, Auto Select, Default Alternate rendition that the client should try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio, Auto Select, Not Default Alternate rendition that the client may try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate rendition that the client will not try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO

SegmentType -> (string)

Specifies the segment type.

Fmp4HlsSettings -> (structure)

Fmp4 Hls Settings

AudioRenditionSets -> (string)

List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by â,â.

NielsenId3Behavior -> (string)

If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.

TimedMetadataBehavior -> (string)

Set to PASSTHROUGH to enable ID3 metadata insertion. To include metadata, you configure other parameters in the output group or individual outputs, or you add an ID3 action to the channel schedule.

FrameCaptureHlsSettings -> (structure)

Frame Capture Hls Settings

StandardHlsSettings -> (structure)

Standard Hls Settings

AudioRenditionSets -> (string)

List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by â,â.

M3u8Settings -> (structure)

Settings information for the .m3u8 container

AudioFramesPerPes -> (integer)

The number of audio frames to insert for each PES packet.

AudioPids -> (string)

Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values.

EcmPid -> (string)

This parameter is unused and deprecated.

NielsenId3Behavior -> (string)

If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.

PatInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream. A value of "0" writes out the PMT once per segment file.

PcrControl -> (string)

When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.

PcrPeriod -> (integer)

Maximum time in milliseconds between Program Clock References (PCRs) inserted into the transport stream.

PcrPid -> (string)

Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value.

PmtInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream. A value of "0" writes out the PMT once per segment file.

PmtPid -> (string)

Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value.

ProgramNum -> (integer)

The value of the program number field in the Program Map Table.

Scte35Behavior -> (string)

If set to passthrough, passes any SCTE-35 signals from the input source to this output.

Scte35Pid -> (string)

Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value.

TimedMetadataBehavior -> (string)

Set to PASSTHROUGH to enable ID3 metadata insertion. To include metadata, you configure other parameters in the output group or individual outputs, or you add an ID3 action to the channel schedule.

TimedMetadataPid -> (string)

Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

TransportStreamId -> (integer)

The value of the transport stream ID field in the Program Map Table.

VideoPid -> (string)

Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value.

KlvBehavior -> (string)

If set to passthrough, passes any KLV data from the input source to this output.

KlvDataPids -> (string)

Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).

NameModifier -> (string)

String concatenated to the end of the destination filename. Accepts "Format Identifiers":#formatIdentifierParameters.

SegmentModifier -> (string)

String concatenated to end of segment filenames.

MediaPackageOutputSettings -> (structure)

Media Package Output Settings

MsSmoothOutputSettings -> (structure)

Ms Smooth Output Settings

H265PackagingType -> (string)

Only applicable when this output is referencing an H.265 video description. Specifies whether MP4 segments should be packaged as HEV1 or HVC1.

NameModifier -> (string)

String concatenated to the end of the destination filename. Required for multiple outputs of the same type.

MultiplexOutputSettings -> (structure)

Multiplex Output Settings

Destination -> (structure)

Destination is a Multiplex.

DestinationRefId -> (string)

Placeholder documentation for __string

ContainerSettings -> (structure)

Multiplex Container Settings

MultiplexM2tsSettings -> (structure)

Multiplex M2ts Settings

AbsentInputAudioBehavior -> (string)

When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream.

Arib -> (string)

When set to enabled, uses ARIB-compliant field muxing and removes video descriptor.

AudioBufferModel -> (string)

When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used.

AudioFramesPerPes -> (integer)

The number of audio frames to insert for each PES packet.

AudioStreamType -> (string)

When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06.

CcDescriptor -> (string)

When set to enabled, generates captionServiceDescriptor in PMT.

Ebif -> (string)

If set to passthrough, passes any EBIF data from the input source to this output.

EsRateInPes -> (string)

Include or exclude the ES Rate field in the PES header.

Klv -> (string)

If set to passthrough, passes any KLV data from the input source to this output.

NielsenId3Behavior -> (string)

If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.

PcrControl -> (string)

When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.

PcrPeriod -> (integer)

Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream.

Scte35Control -> (string)

Optionally pass SCTE-35 signals from the input source to this output.

Scte35PrerollPullupMilliseconds -> (double)

Defines the amount SCTE-35 preroll will be increased (in milliseconds) on the output. Preroll is the amount of time between the presence of a SCTE-35 indication in a transport stream and the PTS of the video frame it references. Zero means donât add pullup (it doesnât mean set the preroll to zero). Negative pullup is not supported, which means that you canât make the preroll shorter. Be aware that latency in the output will increase by the pullup amount.

RtmpOutputSettings -> (structure)

Rtmp Output Settings

CertificateMode -> (string)

If set to verifyAuthenticity, verify the tls certificate chain to a trusted Certificate Authority (CA). This will cause rtmps outputs with self-signed certificates to fail.

ConnectionRetryInterval -> (integer)

Number of seconds to wait before retrying a connection to the Flash Media server if the connection is lost.

Destination -> (structure)

The RTMP endpoint excluding the stream name (eg. rtmp://host/appname). For connection to Akamai, a username and password must be supplied. URI fields accept format identifiers.

DestinationRefId -> (string)

Placeholder documentation for __string

NumRetries -> (integer)

Number of retry attempts.

UdpOutputSettings -> (structure)

Udp Output Settings

BufferMsec -> (integer)

UDP output buffering in milliseconds. Larger values increase latency through the transcoder but simultaneously assist the transcoder in maintaining a constant, low-jitter UDP/RTP output while accommodating clock recovery, input switching, input disruptions, picture reordering, etc.

ContainerSettings -> (structure)

Udp Container Settings

M2tsSettings -> (structure)

M2ts Settings

AbsentInputAudioBehavior -> (string)

When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream.

Arib -> (string)

When set to enabled, uses ARIB-compliant field muxing and removes video descriptor.

AribCaptionsPid -> (string)

Packet Identifier (PID) for ARIB Captions in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

AribCaptionsPidControl -> (string)

If set to auto, pid number used for ARIB Captions will be auto-selected from unused pids. If set to useConfigured, ARIB Captions will be on the configured pid number.

AudioBufferModel -> (string)

When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used.

AudioFramesPerPes -> (integer)

The number of audio frames to insert for each PES packet.

AudioPids -> (string)

Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).

AudioStreamType -> (string)

When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06.

Bitrate -> (integer)

The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate.

BufferModel -> (string)

Controls the timing accuracy for output network traffic. Leave as MULTIPLEX to ensure accurate network packet timing. Or set to NONE, which might result in lower latency but will result in more variability in output network packet timing. This variability might cause interruptions, jitter, or bursty behavior in your playback or receiving devices.

CcDescriptor -> (string)

When set to enabled, generates captionServiceDescriptor in PMT.

DvbNitSettings -> (structure)

Inserts DVB Network Information Table (NIT) at the specified table repetition interval.

NetworkId -> (integer)

The numeric value placed in the Network Information Table (NIT).

NetworkName -> (string)

The network name text placed in the networkNameDescriptor inside the Network Information Table. Maximum length is 256 characters.

RepInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream.

DvbSdtSettings -> (structure)

Inserts DVB Service Description Table (SDT) at the specified table repetition interval.

OutputSdt -> (string)

Selects method of inserting SDT information into output stream. The sdtFollow setting copies SDT information from input stream to output stream. The sdtFollowIfPresent setting copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. The sdtManual setting means user will enter the SDT information. The sdtNone setting means output stream will not contain SDT information.

RepInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream.

ServiceName -> (string)

The service name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.

ServiceProviderName -> (string)

The service provider name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.

DvbSubPids -> (string)

Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).

DvbTdtSettings -> (structure)

Inserts DVB Time and Date Table (TDT) at the specified table repetition interval.

RepInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream.

DvbTeletextPid -> (string)

Packet Identifier (PID) for input source DVB Teletext data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

Ebif -> (string)

If set to passthrough, passes any EBIF data from the input source to this output.

EbpAudioInterval -> (string)

When videoAndFixedIntervals is selected, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. Only available when EBP Cablelabs segmentation markers are selected. Partitions 1 and 2 will always follow the video interval.

EbpLookaheadMs -> (integer)

When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is âstretchedâ to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate.

EbpPlacement -> (string)

Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP markers will be placed on the video PID and all audio PIDs. If set to videoPid, EBP markers will be placed on only the video PID.

EcmPid -> (string)

This field is unused and deprecated.

EsRateInPes -> (string)

Include or exclude the ES Rate field in the PES header.

EtvPlatformPid -> (string)

Packet Identifier (PID) for input source ETV Platform data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

EtvSignalPid -> (string)

Packet Identifier (PID) for input source ETV Signal data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

FragmentTime -> (double)

The length in seconds of each fragment. Only used with EBP markers.

Klv -> (string)

If set to passthrough, passes any KLV data from the input source to this output.

KlvDataPids -> (string)

Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).

NielsenId3Behavior -> (string)

If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.

NullPacketBitrate -> (double)

Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets.

PatInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.

PcrControl -> (string)

When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.

PcrPeriod -> (integer)

Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream.

PcrPid -> (string)

Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

PmtInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.

PmtPid -> (string)

Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

ProgramNum -> (integer)

The value of the program number field in the Program Map Table.

RateMode -> (string)

When vbr, does not insert null packets into transport stream to fill specified bitrate. The bitrate setting acts as the maximum bitrate when vbr is set.

Scte27Pids -> (string)

Packet Identifier (PID) for input source SCTE-27 data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).

Scte35Control -> (string)

Optionally pass SCTE-35 signals from the input source to this output.

Scte35Pid -> (string)

Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

SegmentationMarkers -> (string)

Inserts segmentation markers at each segmentationTime period. raiSegstart sets the Random Access Indicator bit in the adaptation field. raiAdapt sets the RAI bit and adds the current timecode in the private data bytes. psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.

SegmentationStyle -> (string)

The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of âresetCadenceâ is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of $segmentationTime seconds. When a segmentation style of âmaintainCadenceâ is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentationTime seconds. Note that EBP lookahead is a slight exception to this rule.

SegmentationTime -> (double)

The length in seconds of each segment. Required unless markers is set to _none_.

TimedMetadataBehavior -> (string)

When set to passthrough, timed metadata will be passed through from input to output.

TimedMetadataPid -> (string)

Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

TransportStreamId -> (integer)

The value of the transport stream ID field in the Program Map Table.

VideoPid -> (string)

Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

Scte35PrerollPullupMilliseconds -> (double)

Defines the amount SCTE-35 preroll will be increased (in milliseconds) on the output. Preroll is the amount of time between the presence of a SCTE-35 indication in a transport stream and the PTS of the video frame it references. Zero means donât add pullup (it doesnât mean set the preroll to zero). Negative pullup is not supported, which means that you canât make the preroll shorter. Be aware that latency in the output will increase by the pullup amount.

Destination -> (structure)

Destination address and port number for RTP or UDP packets. Can be unicast or multicast RTP or UDP (eg. rtp://239.10.10.10:5001 or udp://10.100.100.100:5002).

DestinationRefId -> (string)

Placeholder documentation for __string

FecOutputSettings -> (structure)

Settings for enabling and adjusting Forward Error Correction on UDP outputs.

ColumnDepth -> (integer)

Parameter D from SMPTE 2022-1. The height of the FEC protection matrix. The number of transport stream packets per column error correction packet. Must be between 4 and 20, inclusive.

IncludeFec -> (string)

Enables column only or column and row based FEC

RowLength -> (integer)

Parameter L from SMPTE 2022-1. The width of the FEC protection matrix. Must be between 1 and 20, inclusive. If only Column FEC is used, then larger values increase robustness. If Row FEC is used, then this is the number of transport stream packets per row error correction packet, and the value must be between 4 and 20, inclusive, if includeFec is columnAndRow. If includeFec is column, this value must be 1 to 20, inclusive.

CmafIngestOutputSettings -> (structure)

Cmaf Ingest Output Settings

NameModifier -> (string)

String concatenated to the end of the destination filename. Required for multiple outputs of the same type.

SrtOutputSettings -> (structure)

Srt Output Settings

BufferMsec -> (integer)

SRT output buffering in milliseconds. A higher value increases latency through the encoder. But the benefits are that it helps to maintain a constant, low-jitter SRT output, and it accommodates clock recovery, input switching, input disruptions, picture reordering, and so on. Range: 0-10000 milliseconds.

ContainerSettings -> (structure)

Udp Container Settings

M2tsSettings -> (structure)

M2ts Settings

AbsentInputAudioBehavior -> (string)

When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream.

Arib -> (string)

When set to enabled, uses ARIB-compliant field muxing and removes video descriptor.

AribCaptionsPid -> (string)

Packet Identifier (PID) for ARIB Captions in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

AribCaptionsPidControl -> (string)

If set to auto, pid number used for ARIB Captions will be auto-selected from unused pids. If set to useConfigured, ARIB Captions will be on the configured pid number.

AudioBufferModel -> (string)

When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used.

AudioFramesPerPes -> (integer)

The number of audio frames to insert for each PES packet.

AudioPids -> (string)

Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).

AudioStreamType -> (string)

When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06.

Bitrate -> (integer)

The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate.

BufferModel -> (string)

Controls the timing accuracy for output network traffic. Leave as MULTIPLEX to ensure accurate network packet timing. Or set to NONE, which might result in lower latency but will result in more variability in output network packet timing. This variability might cause interruptions, jitter, or bursty behavior in your playback or receiving devices.

CcDescriptor -> (string)

When set to enabled, generates captionServiceDescriptor in PMT.

DvbNitSettings -> (structure)

Inserts DVB Network Information Table (NIT) at the specified table repetition interval.

NetworkId -> (integer)

The numeric value placed in the Network Information Table (NIT).

NetworkName -> (string)

The network name text placed in the networkNameDescriptor inside the Network Information Table. Maximum length is 256 characters.

RepInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream.

DvbSdtSettings -> (structure)

Inserts DVB Service Description Table (SDT) at the specified table repetition interval.

OutputSdt -> (string)

Selects method of inserting SDT information into output stream. The sdtFollow setting copies SDT information from input stream to output stream. The sdtFollowIfPresent setting copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. The sdtManual setting means user will enter the SDT information. The sdtNone setting means output stream will not contain SDT information.

RepInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream.

ServiceName -> (string)

The service name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.

ServiceProviderName -> (string)

The service provider name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.

DvbSubPids -> (string)

Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).

DvbTdtSettings -> (structure)

Inserts DVB Time and Date Table (TDT) at the specified table repetition interval.

RepInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream.

DvbTeletextPid -> (string)

Packet Identifier (PID) for input source DVB Teletext data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

Ebif -> (string)

If set to passthrough, passes any EBIF data from the input source to this output.

EbpAudioInterval -> (string)

When videoAndFixedIntervals is selected, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. Only available when EBP Cablelabs segmentation markers are selected. Partitions 1 and 2 will always follow the video interval.

EbpLookaheadMs -> (integer)

When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is âstretchedâ to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate.

EbpPlacement -> (string)

Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP markers will be placed on the video PID and all audio PIDs. If set to videoPid, EBP markers will be placed on only the video PID.

EcmPid -> (string)

This field is unused and deprecated.

EsRateInPes -> (string)

Include or exclude the ES Rate field in the PES header.

EtvPlatformPid -> (string)

Packet Identifier (PID) for input source ETV Platform data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

EtvSignalPid -> (string)

Packet Identifier (PID) for input source ETV Signal data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

FragmentTime -> (double)

The length in seconds of each fragment. Only used with EBP markers.

Klv -> (string)

If set to passthrough, passes any KLV data from the input source to this output.

KlvDataPids -> (string)

Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).

NielsenId3Behavior -> (string)

If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.

NullPacketBitrate -> (double)

Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets.

PatInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.

PcrControl -> (string)

When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.

PcrPeriod -> (integer)

Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream.

PcrPid -> (string)

Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

PmtInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.

PmtPid -> (string)

Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

ProgramNum -> (integer)

The value of the program number field in the Program Map Table.

RateMode -> (string)

When vbr, does not insert null packets into transport stream to fill specified bitrate. The bitrate setting acts as the maximum bitrate when vbr is set.

Scte27Pids -> (string)

Packet Identifier (PID) for input source SCTE-27 data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).

Scte35Control -> (string)

Optionally pass SCTE-35 signals from the input source to this output.

Scte35Pid -> (string)

Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

SegmentationMarkers -> (string)

Inserts segmentation markers at each segmentationTime period. raiSegstart sets the Random Access Indicator bit in the adaptation field. raiAdapt sets the RAI bit and adds the current timecode in the private data bytes. psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.

SegmentationStyle -> (string)

The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of âresetCadenceâ is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of $segmentationTime seconds. When a segmentation style of âmaintainCadenceâ is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentationTime seconds. Note that EBP lookahead is a slight exception to this rule.

SegmentationTime -> (double)

The length in seconds of each segment. Required unless markers is set to _none_.

TimedMetadataBehavior -> (string)

When set to passthrough, timed metadata will be passed through from input to output.

TimedMetadataPid -> (string)

Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

TransportStreamId -> (integer)

The value of the transport stream ID field in the Program Map Table.

VideoPid -> (string)

Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).

Scte35PrerollPullupMilliseconds -> (double)

Defines the amount SCTE-35 preroll will be increased (in milliseconds) on the output. Preroll is the amount of time between the presence of a SCTE-35 indication in a transport stream and the PTS of the video frame it references. Zero means donât add pullup (it doesnât mean set the preroll to zero). Negative pullup is not supported, which means that you canât make the preroll shorter. Be aware that latency in the output will increase by the pullup amount.

Destination -> (structure)

Reference to an OutputDestination ID defined in the channel

DestinationRefId -> (string)

Placeholder documentation for __string

EncryptionType -> (string)

The encryption level for the content. Valid values are AES128, AES192, AES256. You and the downstream system should plan how to set this field because the values must not conflict with each other.

Latency -> (integer)

The latency value, in milliseconds, that is proposed during the SRT connection handshake. SRT will choose the maximum of the values proposed by the sender and receiver. On the sender side, latency is the amount of time a packet is held to give it a chance to be delivered successfully. On the receiver side, latency is the amount of time the packet is held before delivering to the application, aiding in packet recovery and matching as closely as possible the packet timing of the sender. Range: 40-16000 milliseconds.

VideoDescriptionName -> (string)

The name of the VideoDescription used as the source for this output.

TimecodeConfig -> (structure)

Contains settings used to acquire and adjust timecode information from inputs.

Source -> (string)

Identifies the source for the timecode that will be associated with the events outputs. -Embedded (embedded): Initialize the output timecode with timecode from the the source. If no embedded timecode is detected in the source, the system falls back to using âStart at 0â (zerobased). -System Clock (systemclock): Use the UTC time. -Start at 0 (zerobased): The time of the first frame of the event will be 00:00:00:00.

SyncThreshold -> (integer)

Threshold in frames beyond which output timecode is resynchronized to the input timecode. Discrepancies below this threshold are permitted to avoid unnecessary discontinuities in the output timecode. No timecode sync when this is not specified.

VideoDescriptions -> (list)

Placeholder documentation for __listOfVideoDescription

(structure)

Video settings for this stream.

CodecSettings -> (structure)

Video codec settings.

FrameCaptureSettings -> (structure)

Frame Capture Settings

CaptureInterval -> (integer)

The frequency at which to capture frames for inclusion in the output. May be specified in either seconds or milliseconds, as specified by captureIntervalUnits.

CaptureIntervalUnits -> (string)

Unit for the frame capture interval.

TimecodeBurninSettings -> (structure)

Timecode burn-in settings

FontSize -> (string)

Choose a timecode burn-in font size

Position -> (string)

Choose a timecode burn-in output position

Prefix -> (string)

Create a timecode burn-in prefix (optional)

H264Settings -> (structure)

H264 Settings

AdaptiveQuantization -> (string)

Enables or disables adaptive quantization, which is a technique MediaLive can apply to video on a frame-by-frame basis to produce more compression without losing quality. There are three types of adaptive quantization: flicker, spatial, and temporal. Set the field in one of these ways: Set to Auto. Recommended. For each type of AQ, MediaLive will determine if AQ is needed, and if so, the appropriate strength. Set a strength (a value other than Auto or Disable). This strength will apply to any of the AQ fields that you choose to enable. Set to Disabled to disable all types of adaptive quantization.

AfdSignaling -> (string)

Indicates that AFD values will be written into the output stream. If afdSignaling is âautoâ, the system will try to preserve the input AFD value (in cases where multiple AFD values are valid). If set to âfixedâ, the AFD value will be the value configured in the fixedAfd parameter.

Bitrate -> (integer)

Average bitrate in bits/second. Required when the rate control mode is VBR or CBR. Not used for QVBR. In an MS Smooth output group, each output must have a unique value when its bitrate is rounded down to the nearest multiple of 1000.

BufFillPct -> (integer)

Percentage of the buffer that should initially be filled (HRD buffer model).

BufSize -> (integer)

Size of buffer (HRD buffer model) in bits.

ColorMetadata -> (string)

Includes colorspace metadata in the output.

ColorSpaceSettings -> (structure)

Color Space settings

ColorSpacePassthroughSettings -> (structure)

Passthrough applies no color space conversion to the output

Rec601Settings -> (structure)

Rec601 Settings

Rec709Settings -> (structure)

Rec709 Settings

EntropyEncoding -> (string)

Entropy encoding mode. Use cabac (must be in Main or High profile) or cavlc.

FilterSettings -> (structure)

Optional. Both filters reduce bandwidth by removing imperceptible details. You can enable one of the filters. We recommend that you try both filters and observe the results to decide which one to use. The Temporal Filter reduces bandwidth by removing imperceptible details in the content. It combines perceptual filtering and motion compensated temporal filtering (MCTF). It operates independently of the compression level. The Bandwidth Reduction filter is a perceptual filter located within the encoding loop. It adapts to the current compression level to filter imperceptible signals. This filter works only when the resolution is 1080p or lower.

TemporalFilterSettings -> (structure)

Temporal Filter Settings

PostFilterSharpening -> (string)

If you enable this filter, the results are the following: - If the source content is noisy (it contains excessive digital artifacts), the filter cleans up the source. - If the source content is already clean, the filter tends to decrease the bitrate, especially when the rate control mode is QVBR.

Strength -> (string)

Choose a filter strength. We recommend a strength of 1 or 2. A higher strength might take out good information, resulting in an image that is overly soft.

BandwidthReductionFilterSettings -> (structure)

Bandwidth Reduction Filter Settings

PostFilterSharpening -> (string)

Configures the sharpening control, which is available when the bandwidth reduction filter is enabled. This control sharpens edges and contours, which produces a specific artistic effect that you might want. We recommend that you test each of the values (including DISABLED) to observe the sharpening effect on the content.

Strength -> (string)

Enables the bandwidth reduction filter. The filter strengths range from 1 to 4. We recommend that you always enable this filter and use AUTO, to let MediaLive apply the optimum filtering for the context.

FixedAfd -> (string)

Four bit AFD value to write on all frames of video in the output stream. Only valid when afdSignaling is set to âFixedâ.

FlickerAq -> (string)

Flicker AQ makes adjustments within each frame to reduce flicker or âpopâ on I-frames. The value to enter in this field depends on the value in the Adaptive quantization field: If you have set the Adaptive quantization field to Auto, MediaLive ignores any value in this field. MediaLive will determine if flicker AQ is appropriate and will apply the appropriate strength. If you have set the Adaptive quantization field to a strength, you can set this field to Enabled or Disabled. Enabled: MediaLive will apply flicker AQ using the specified strength. Disabled: MediaLive wonât apply flicker AQ. If you have set the Adaptive quantization to Disabled, MediaLive ignores any value in this field and doesnât apply flicker AQ.

ForceFieldPictures -> (string)

This setting applies only when scan type is âinterlaced.â It controls whether coding is performed on a field basis or on a frame basis. (When the video is progressive, the coding is always performed on a frame basis.) enabled: Force MediaLive to code on a field basis, so that odd and even sets of fields are coded separately. disabled: Code the two sets of fields separately (on a field basis) or together (on a frame basis using PAFF), depending on what is most appropriate for the content.

FramerateControl -> (string)

This field indicates how the output video frame rate is specified. If âspecifiedâ is selected then the output video frame rate is determined by framerateNumerator and framerateDenominator, else if âinitializeFromSourceâ is selected then the output video frame rate will be set equal to the input video frame rate of the first input.

FramerateDenominator -> (integer)

Framerate denominator.

FramerateNumerator -> (integer)

Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.

GopBReference -> (string)

Documentation update needed

GopClosedCadence -> (integer)

Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.

GopNumBFrames -> (integer)

Number of B-frames between reference frames.

GopSize -> (double)

GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits. If gopSizeUnits is frames, gopSize must be an integer and must be greater than or equal to 1. If gopSizeUnits is seconds, gopSize must be greater than 0, but need not be an integer.

GopSizeUnits -> (string)

Indicates if the gopSize is specified in frames or seconds. If seconds the system will convert the gopSize into a frame count at run time.

Level -> (string)

H.264 Level.

LookAheadRateControl -> (string)

Amount of lookahead. A value of low can decrease latency and memory usage, while high can produce better quality for certain content.

MaxBitrate -> (integer)

For QVBR: See the tooltip for Quality level For VBR: Set the maximum bitrate in order to accommodate expected spikes in the complexity of the video.

MinIInterval -> (integer)

Only meaningful if sceneChangeDetect is set to enabled. Defaults to 5 if multiplex rate control is used. Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1

NumRefFrames -> (integer)

Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding.

ParControl -> (string)

This field indicates how the output pixel aspect ratio is specified. If âspecifiedâ is selected then the output video pixel aspect ratio is determined by parNumerator and parDenominator, else if âinitializeFromSourceâ is selected then the output pixsel aspect ratio will be set equal to the input video pixel aspect ratio of the first input.

ParDenominator -> (integer)

Pixel Aspect Ratio denominator.

ParNumerator -> (integer)

Pixel Aspect Ratio numerator.

Profile -> (string)

H.264 Profile.

QualityLevel -> (string)

Leave as STANDARD_QUALITY or choose a different value (which might result in additional costs to run the channel). - ENHANCED_QUALITY: Produces a slightly better video quality without an increase in the bitrate. Has an effect only when the Rate control mode is QVBR or CBR. If this channel is in a MediaLive multiplex, the value must be ENHANCED_QUALITY. - STANDARD_QUALITY: Valid for any Rate control mode.

QvbrQualityLevel -> (integer)

Controls the target quality for the video encode. Applies only when the rate control mode is QVBR. You can set a target quality or you can let MediaLive determine the best quality. To set a target quality, enter values in the QVBR quality level field and the Max bitrate field. Enter values that suit your most important viewing devices. Recommended values are: - Primary screen: Quality level: 8 to 10. Max bitrate: 4M - PC or tablet: Quality level: 7. Max bitrate: 1.5M to 3M - Smartphone: Quality level: 6. Max bitrate: 1M to 1.5M To let MediaLive decide, leave the QVBR quality level field empty, and in Max bitrate enter the maximum rate you want in the video. For more information, see the section called âVideo - rate control modeâ in the MediaLive user guide

RateControlMode -> (string)

Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. VBR: Quality and bitrate vary, depending on the video complexity. Recommended instead of QVBR if you want to maintain a specific average bitrate over the duration of the channel. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates. Multiplex: This rate control mode is only supported (and is required) when the video is being delivered to a MediaLive Multiplex in which case the rate control configuration is controlled by the properties within the Multiplex Program.

ScanType -> (string)

Sets the scan type of the output to progressive or top-field-first interlaced.

SceneChangeDetect -> (string)

Scene change detection. - On: inserts I-frames when scene change is detected. - Off: does not force an I-frame when scene change is detected.

Slices -> (integer)

Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. This field is optional; when no value is specified the encoder will choose the number of slices based on encode resolution.

Softness -> (integer)

Softness. Selects quantizer matrix, larger values reduce high-frequency content in the encoded image. If not set to zero, must be greater than 15.

SpatialAq -> (string)

Spatial AQ makes adjustments within each frame based on spatial variation of content complexity. The value to enter in this field depends on the value in the Adaptive quantization field: If you have set the Adaptive quantization field to Auto, MediaLive ignores any value in this field. MediaLive will determine if spatial AQ is appropriate and will apply the appropriate strength. If you have set the Adaptive quantization field to a strength, you can set this field to Enabled or Disabled. Enabled: MediaLive will apply spatial AQ using the specified strength. Disabled: MediaLive wonât apply spatial AQ. If you have set the Adaptive quantization to Disabled, MediaLive ignores any value in this field and doesnât apply spatial AQ.

SubgopLength -> (string)

If set to fixed, use gopNumBFrames B-frames per sub-GOP. If set to dynamic, optimize the number of B-frames used for each sub-GOP to improve visual quality.

Syntax -> (string)

Produces a bitstream compliant with SMPTE RP-2027.

TemporalAq -> (string)

Temporal makes adjustments within each frame based on temporal variation of content complexity. The value to enter in this field depends on the value in the Adaptive quantization field: If you have set the Adaptive quantization field to Auto, MediaLive ignores any value in this field. MediaLive will determine if temporal AQ is appropriate and will apply the appropriate strength. If you have set the Adaptive quantization field to a strength, you can set this field to Enabled or Disabled. Enabled: MediaLive will apply temporal AQ using the specified strength. Disabled: MediaLive wonât apply temporal AQ. If you have set the Adaptive quantization to Disabled, MediaLive ignores any value in this field and doesnât apply temporal AQ.

TimecodeInsertion -> (string)

Determines how timecodes should be inserted into the video elementary stream. - âdisabledâ: Do not include timecodes - âpicTimingSeiâ: Pass through picture timing SEI messages from the source specified in Timecode Config

TimecodeBurninSettings -> (structure)

Timecode burn-in settings

FontSize -> (string)

Choose a timecode burn-in font size

Position -> (string)

Choose a timecode burn-in output position

Prefix -> (string)

Create a timecode burn-in prefix (optional)

MinQp -> (integer)

Sets the minimum QP. If you arenât familiar with quantization adjustment, leave the field empty. MediaLive will apply an appropriate value.

H265Settings -> (structure)

H265 Settings

AdaptiveQuantization -> (string)

Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality.

AfdSignaling -> (string)

Indicates that AFD values will be written into the output stream. If afdSignaling is âautoâ, the system will try to preserve the input AFD value (in cases where multiple AFD values are valid). If set to âfixedâ, the AFD value will be the value configured in the fixedAfd parameter.

AlternativeTransferFunction -> (string)

Whether or not EML should insert an Alternative Transfer Function SEI message to support backwards compatibility with non-HDR decoders and displays.

Bitrate -> (integer)

Average bitrate in bits/second. Required when the rate control mode is VBR or CBR. Not used for QVBR. In an MS Smooth output group, each output must have a unique value when its bitrate is rounded down to the nearest multiple of 1000.

BufSize -> (integer)

Size of buffer (HRD buffer model) in bits.

ColorMetadata -> (string)

Includes colorspace metadata in the output.

ColorSpaceSettings -> (structure)

Color Space settings

ColorSpacePassthroughSettings -> (structure)

Passthrough applies no color space conversion to the output

DolbyVision81Settings -> (structure)

Dolby Vision81 Settings

Hdr10Settings -> (structure)

Hdr10 Settings

MaxCll -> (integer)

Maximum Content Light Level An integer metadata value defining the maximum light level, in nits, of any single pixel within an encoded HDR video stream or file.

MaxFall -> (integer)

Maximum Frame Average Light Level An integer metadata value defining the maximum average light level, in nits, for any single frame within an encoded HDR video stream or file.

Rec601Settings -> (structure)

Rec601 Settings

Rec709Settings -> (structure)

Rec709 Settings

FilterSettings -> (structure)

Optional. Both filters reduce bandwidth by removing imperceptible details. You can enable one of the filters. We recommend that you try both filters and observe the results to decide which one to use. The Temporal Filter reduces bandwidth by removing imperceptible details in the content. It combines perceptual filtering and motion compensated temporal filtering (MCTF). It operates independently of the compression level. The Bandwidth Reduction filter is a perceptual filter located within the encoding loop. It adapts to the current compression level to filter imperceptible signals. This filter works only when the resolution is 1080p or lower.

TemporalFilterSettings -> (structure)

Temporal Filter Settings

PostFilterSharpening -> (string)

If you enable this filter, the results are the following: - If the source content is noisy (it contains excessive digital artifacts), the filter cleans up the source. - If the source content is already clean, the filter tends to decrease the bitrate, especially when the rate control mode is QVBR.

Strength -> (string)

Choose a filter strength. We recommend a strength of 1 or 2. A higher strength might take out good information, resulting in an image that is overly soft.

BandwidthReductionFilterSettings -> (structure)

Bandwidth Reduction Filter Settings

PostFilterSharpening -> (string)

Configures the sharpening control, which is available when the bandwidth reduction filter is enabled. This control sharpens edges and contours, which produces a specific artistic effect that you might want. We recommend that you test each of the values (including DISABLED) to observe the sharpening effect on the content.

Strength -> (string)

Enables the bandwidth reduction filter. The filter strengths range from 1 to 4. We recommend that you always enable this filter and use AUTO, to let MediaLive apply the optimum filtering for the context.

FixedAfd -> (string)

Four bit AFD value to write on all frames of video in the output stream. Only valid when afdSignaling is set to âFixedâ.

FlickerAq -> (string)

If set to enabled, adjust quantization within each frame to reduce flicker or âpopâ on I-frames.

FramerateDenominator -> (integer)

Framerate denominator.

FramerateNumerator -> (integer)

Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.

GopClosedCadence -> (integer)

Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.

GopSize -> (double)

GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits. If gopSizeUnits is frames, gopSize must be an integer and must be greater than or equal to 1. If gopSizeUnits is seconds, gopSize must be greater than 0, but need not be an integer.

GopSizeUnits -> (string)

Indicates if the gopSize is specified in frames or seconds. If seconds the system will convert the gopSize into a frame count at run time.

Level -> (string)

H.265 Level.

LookAheadRateControl -> (string)

Amount of lookahead. A value of low can decrease latency and memory usage, while high can produce better quality for certain content.

MaxBitrate -> (integer)

For QVBR: See the tooltip for Quality level

MinIInterval -> (integer)

Only meaningful if sceneChangeDetect is set to enabled. Defaults to 5 if multiplex rate control is used. Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1

ParDenominator -> (integer)

Pixel Aspect Ratio denominator.

ParNumerator -> (integer)

Pixel Aspect Ratio numerator.

Profile -> (string)

H.265 Profile.

QvbrQualityLevel -> (integer)

Controls the target quality for the video encode. Applies only when the rate control mode is QVBR. Set values for the QVBR quality level field and Max bitrate field that suit your most important viewing devices. Recommended values are: - Primary screen: Quality level: 8 to 10. Max bitrate: 4M - PC or tablet: Quality level: 7. Max bitrate: 1.5M to 3M - Smartphone: Quality level: 6. Max bitrate: 1M to 1.5M

RateControlMode -> (string)

Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates. Multiplex: This rate control mode is only supported (and is required) when the video is being delivered to a MediaLive Multiplex in which case the rate control configuration is controlled by the properties within the Multiplex Program.

ScanType -> (string)

Sets the scan type of the output to progressive or top-field-first interlaced.

SceneChangeDetect -> (string)

Scene change detection.

Slices -> (integer)

Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. This field is optional; when no value is specified the encoder will choose the number of slices based on encode resolution.

Tier -> (string)

H.265 Tier.

TimecodeInsertion -> (string)

Determines how timecodes should be inserted into the video elementary stream. - âdisabledâ: Do not include timecodes - âpicTimingSeiâ: Pass through picture timing SEI messages from the source specified in Timecode Config

TimecodeBurninSettings -> (structure)

Timecode burn-in settings

FontSize -> (string)

Choose a timecode burn-in font size

Position -> (string)

Choose a timecode burn-in output position

Prefix -> (string)

Create a timecode burn-in prefix (optional)

MvOverPictureBoundaries -> (string)

If you are setting up the picture as a tile, you must set this to âdisabledâ. In all other configurations, you typically enter âenabledâ.

MvTemporalPredictor -> (string)

If you are setting up the picture as a tile, you must set this to âdisabledâ. In other configurations, you typically enter âenabledâ.

TileHeight -> (integer)

Set this field to set up the picture as a tile. You must also set tileWidth. The tile height must result in 22 or fewer rows in the frame. The tile width must result in 20 or fewer columns in the frame. And finally, the product of the column count and row count must be 64 of less. If the tile width and height are specified, MediaLive will override the video codec slices field with a value that MediaLive calculates

TilePadding -> (string)

Set to âpaddedâ to force MediaLive to add padding to the frame, to obtain a frame that is a whole multiple of the tile size. If you are setting up the picture as a tile, you must enter âpaddedâ. In all other configurations, you typically enter ânoneâ.

TileWidth -> (integer)

Set this field to set up the picture as a tile. See tileHeight for more information.

TreeblockSize -> (string)

Select the tree block size used for encoding. If you enter âautoâ, the encoder will pick the best size. If you are setting up the picture as a tile, you must set this to 32x32. In all other configurations, you typically enter âautoâ.

MinQp -> (integer)

Sets the minimum QP. If you arenât familiar with quantization adjustment, leave the field empty. MediaLive will apply an appropriate value.

Deblocking -> (string)

Enable or disable the deblocking filter for this codec. The filter reduces blocking artifacts at block boundaries, which improves overall video quality. If the filter is disabled, visible block edges might appear in the output, especially at lower bitrates.

Mpeg2Settings -> (structure)

Mpeg2 Settings

AdaptiveQuantization -> (string)

Choose Off to disable adaptive quantization. Or choose another value to enable the quantizer and set its strength. The strengths are: Auto, Off, Low, Medium, High. When you enable this field, MediaLive allows intra-frame quantizers to vary, which might improve visual quality.

AfdSignaling -> (string)

Indicates the AFD values that MediaLive will write into the video encode. If you do not know what AFD signaling is, or if your downstream system has not given you guidance, choose AUTO. AUTO: MediaLive will try to preserve the input AFD value (in cases where multiple AFD values are valid). FIXED: MediaLive will use the value you specify in fixedAFD.

ColorMetadata -> (string)

Specifies whether to include the color space metadata. The metadata describes the color space that applies to the video (the colorSpace field). We recommend that you insert the metadata.

ColorSpace -> (string)

Choose the type of color space conversion to apply to the output. For detailed information on setting up both the input and the output to obtain the desired color space in the output, see the section on "MediaLive Features - Video - color space" in the MediaLive User Guide. PASSTHROUGH: Keep the color space of the input content - do not convert it. AUTO:Convert all content that is SD to rec 601, and convert all content that is HD to rec 709.

DisplayAspectRatio -> (string)

Sets the pixel aspect ratio for the encode.

FilterSettings -> (structure)

Optionally specify a noise reduction filter, which can improve quality of compressed content. If you do not choose a filter, no filter will be applied. TEMPORAL: This filter is useful for both source content that is noisy (when it has excessive digital artifacts) and source content that is clean. When the content is noisy, the filter cleans up the source content before the encoding phase, with these two effects: First, it improves the output video quality because the content has been cleaned up. Secondly, it decreases the bandwidth because MediaLive does not waste bits on encoding noise. When the content is reasonably clean, the filter tends to decrease the bitrate.

TemporalFilterSettings -> (structure)

Temporal Filter Settings

PostFilterSharpening -> (string)

If you enable this filter, the results are the following: - If the source content is noisy (it contains excessive digital artifacts), the filter cleans up the source. - If the source content is already clean, the filter tends to decrease the bitrate, especially when the rate control mode is QVBR.

Strength -> (string)

Choose a filter strength. We recommend a strength of 1 or 2. A higher strength might take out good information, resulting in an image that is overly soft.

FixedAfd -> (string)

Complete this field only when afdSignaling is set to FIXED. Enter the AFD value (4 bits) to write on all frames of the video encode.

FramerateDenominator -> (integer)

descriptionâ: âThe framerate denominator. For example, 1001. The framerate is the numerator divided by the denominator. For example, 24000 / 1001 = 23.976 FPS.

FramerateNumerator -> (integer)

The framerate numerator. For example, 24000. The framerate is the numerator divided by the denominator. For example, 24000 / 1001 = 23.976 FPS.

GopClosedCadence -> (integer)

MPEG2: default is open GOP.

GopNumBFrames -> (integer)

Relates to the GOP structure. The number of B-frames between reference frames. If you do not know what a B-frame is, use the default.

GopSize -> (double)

Relates to the GOP structure. The GOP size (keyframe interval) in the units specified in gopSizeUnits. If you do not know what GOP is, use the default. If gopSizeUnits is frames, then the gopSize must be an integer and must be greater than or equal to 1. If gopSizeUnits is seconds, the gopSize must be greater than 0, but does not need to be an integer.

GopSizeUnits -> (string)

Relates to the GOP structure. Specifies whether the gopSize is specified in frames or seconds. If you do not plan to change the default gopSize, leave the default. If you specify SECONDS, MediaLive will internally convert the gop size to a frame count.

ScanType -> (string)

Set the scan type of the output to PROGRESSIVE or INTERLACED (top field first).

SubgopLength -> (string)

Relates to the GOP structure. If you do not know what GOP is, use the default. FIXED: Set the number of B-frames in each sub-GOP to the value in gopNumBFrames. DYNAMIC: Let MediaLive optimize the number of B-frames in each sub-GOP, to improve visual quality.

TimecodeInsertion -> (string)

Determines how MediaLive inserts timecodes in the output video. For detailed information about setting up the input and the output for a timecode, see the section on "MediaLive Features - Timecode configuration" in the MediaLive User Guide. DISABLED: do not include timecodes. GOP_TIMECODE: Include timecode metadata in the GOP header.

TimecodeBurninSettings -> (structure)

Timecode burn-in settings

FontSize -> (string)

Choose a timecode burn-in font size

Position -> (string)

Choose a timecode burn-in output position

Prefix -> (string)

Create a timecode burn-in prefix (optional)

Av1Settings -> (structure)

Av1 Settings

AfdSignaling -> (string)

Configures whether MediaLive will write AFD values into the video. AUTO: MediaLive will try to preserve the input AFD value (in cases where multiple AFD values are valid). FIXED: the AFD value will be the value configured in the fixedAfd parameter. NONE: MediaLive wonât write AFD into the video

BufSize -> (integer)

The size of the buffer (HRD buffer model) in bits.

ColorSpaceSettings -> (structure)

Color Space settings

ColorSpacePassthroughSettings -> (structure)

Passthrough applies no color space conversion to the output

Hdr10Settings -> (structure)

Hdr10 Settings

MaxCll -> (integer)

Maximum Content Light Level An integer metadata value defining the maximum light level, in nits, of any single pixel within an encoded HDR video stream or file.

MaxFall -> (integer)

Maximum Frame Average Light Level An integer metadata value defining the maximum average light level, in nits, for any single frame within an encoded HDR video stream or file.

Rec601Settings -> (structure)

Rec601 Settings

Rec709Settings -> (structure)

Rec709 Settings

FixedAfd -> (string)

Complete this property only if you set the afdSignaling property to FIXED. Choose the AFD value (4 bits) to write on all frames of the video encode.

FramerateDenominator -> (integer)

The denominator for the framerate. Framerate is a fraction, for example, 24000 / 1001.

FramerateNumerator -> (integer)

The numerator for the framerate. Framerate is a fraction, for example, 24000 / 1001.

GopSize -> (double)

The GOP size (keyframe interval). If GopSizeUnits is frames, GopSize must be a whole number and must be greater than or equal to 1. If GopSizeUnits is seconds, GopSize must be greater than 0, but it can be a decimal.

GopSizeUnits -> (string)

Choose the units for the GOP size: FRAMES or SECONDS. For SECONDS, MediaLive converts the size into a frame count at run time.

Level -> (string)

Sets the level. This parameter is one of the properties of the encoding scheme for AV1.

LookAheadRateControl -> (string)

Sets the amount of lookahead. A value of LOW can decrease latency and memory usage. A value of HIGH can produce better quality for certain content.

MaxBitrate -> (integer)

The maximum bitrate to assign. For recommendations, see the description for qvbrQualityLevel.

MinIInterval -> (integer)

Applies only if you enable SceneChangeDetect. Sets the interval between frames. This property ensures a minimum separation between repeated (cadence) I-frames and any I-frames inserted by scene change detection (SCD frames). Enter a number for the interval, measured in number of frames. If an SCD frame and a cadence frame are closer than the specified number of frames, MediaLive shrinks or stretches the GOP to include the SCD frame. Then normal cadence resumes in the next GOP. For GOP stretch to succeed, you must enable LookAheadRateControl. Note that the maximum GOP stretch = (GOP size) + (Minimum I-interval) - 1

ParDenominator -> (integer)

The denominator for the output pixel aspect ratio (PAR).

ParNumerator -> (integer)

The numerator for the output pixel aspect ratio (PAR).

QvbrQualityLevel -> (integer)

Controls the target quality for the video encode. With QVBR rate control mode, the final quality is the target quality, constrained by the maxBitrate. Set values for the qvbrQualityLevel property and maxBitrate property that suit your most important viewing devices. To let MediaLive set the quality level (AUTO mode), leave the qvbrQualityLevel field empty. In this case, MediaLive uses the maximum bitrate, and the quality follows from that: more complex content might have a lower quality. Or set a target quality level and a maximum bitrate. With more complex content, MediaLive will try to achieve the target quality, but it wonât exceed the maximum bitrate. With less complex content, This option will use only the bitrate needed to reach the target quality. Recommended values are: Primary screen: qvbrQualityLevel: Leave empty. maxBitrate: 4,000,000 PC or tablet: qvbrQualityLevel: Leave empty. maxBitrate: 1,500,000 to 3,000,000 Smartphone: qvbrQualityLevel: Leave empty. maxBitrate: 1,000,000 to 1,500,000

SceneChangeDetect -> (string)

Controls whether MediaLive inserts I-frames when it detects a scene change. ENABLED or DISABLED.

TimecodeBurninSettings -> (structure)

Configures the timecode burn-in feature. If you enable this feature, the timecode will become part of the video.

FontSize -> (string)

Choose a timecode burn-in font size

Position -> (string)

Choose a timecode burn-in output position

Prefix -> (string)

Create a timecode burn-in prefix (optional)

Bitrate -> (integer)

Average bitrate in bits/second. Required when the rate control mode is CBR. Not used for QVBR.

RateControlMode -> (string)

Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates.

Height -> (integer)

Output video height, in pixels. Must be an even number. For most codecs, you can leave this field and width blank in order to use the height and width (resolution) from the source. Note, however, that leaving blank is not recommended. For the Frame Capture codec, height and width are required.

Name -> (string)

The name of this VideoDescription. Outputs will use this name to uniquely identify this Description. Description names should be unique within this Live Event.

RespondToAfd -> (string)

Indicates how MediaLive will respond to the AFD values that might be in the input video. If you do not know what AFD signaling is, or if your downstream system has not given you guidance, choose PASSTHROUGH. RESPOND: MediaLive clips the input video using a formula that uses the AFD values (configured in afdSignaling ), the input display aspect ratio, and the output display aspect ratio. MediaLive also includes the AFD values in the output, unless the codec for this encode is FRAME_CAPTURE. PASSTHROUGH: MediaLive ignores the AFD values and does not clip the video. But MediaLive does include the values in the output. NONE: MediaLive does not clip the input video and does not include the AFD values in the output

ScalingBehavior -> (string)

STRETCH_TO_OUTPUT configures the output position to stretch the video to the specified output resolution (height and width). This option will override any position value. DEFAULT may insert black boxes (pillar boxes or letter boxes) around the video to provide the specified output resolution.

Sharpness -> (integer)

Changes the strength of the anti-alias filter used for scaling. 0 is the softest setting, 100 is the sharpest. A setting of 50 is recommended for most content.

Width -> (integer)

Output video width, in pixels. Must be an even number. For most codecs, you can leave this field and height blank in order to use the height and width (resolution) from the source. Note, however, that leaving blank is not recommended. For the Frame Capture codec, height and width are required.

ThumbnailConfiguration -> (structure)

Thumbnail configuration settings.

State -> (string)

Enables the thumbnail feature. The feature generates thumbnails of the incoming video in each pipeline in the channel. AUTO turns the feature on, DISABLE turns the feature off.

ColorCorrectionSettings -> (structure)

Color Correction Settings

GlobalColorCorrections -> (list)

An array of colorCorrections that applies when you are using 3D LUT files to perform color conversion on video. Each colorCorrection contains one 3D LUT file (that defines the color mapping for converting an input color space to an output color space), and the input/output combination that this 3D LUT file applies to. MediaLive reads the color space in the input metadata, determines the color space that you have specified for the output, and finds and uses the LUT file that applies to this combination.

(structure)

Property of ColorCorrectionSettings. Used for custom color space conversion. The object identifies one 3D LUT file and specifies the input/output color space combination that the file will be used for.

InputColorSpace -> (string)

The color space of the input.

OutputColorSpace -> (string)

The color space of the output.

Uri -> (string)

The URI of the 3D LUT file. The protocol must be âs3:â or âs3ssl:â:.

Id -> (string)

The unique id of the channel.

InputAttachments -> (list)

List of input attachments for channel.

(structure)

Placeholder documentation for InputAttachment

AutomaticInputFailoverSettings -> (structure)

User-specified settings for defining what the conditions are for declaring the input unhealthy and failing over to a different input.

ErrorClearTimeMsec -> (integer)

This clear time defines the requirement a recovered input must meet to be considered healthy. The input must have no failover conditions for this length of time. Enter a time in milliseconds. This value is particularly important if the input_preference for the failover pair is set to PRIMARY_INPUT_PREFERRED, because after this time, MediaLive will switch back to the primary input.

FailoverConditions -> (list)

A list of failover conditions. If any of these conditions occur, MediaLive will perform a failover to the other input.

(structure)

Failover Condition settings. There can be multiple failover conditions inside AutomaticInputFailoverSettings.

FailoverConditionSettings -> (structure)

Failover condition type-specific settings.

AudioSilenceSettings -> (structure)

MediaLive will perform a failover if the specified audio selector is silent for the specified period.

AudioSelectorName -> (string)

The name of the audio selector in the input that MediaLive should monitor to detect silence. Select your most important rendition. If you didnât create an audio selector in this input, leave blank.

AudioSilenceThresholdMsec -> (integer)

The amount of time (in milliseconds) that the active input must be silent before automatic input failover occurs. Silence is defined as audio loss or audio quieter than -50 dBFS.

InputLossSettings -> (structure)

MediaLive will perform a failover if content is not detected in this input for the specified period.

InputLossThresholdMsec -> (integer)

The amount of time (in milliseconds) that no input is detected. After that time, an input failover will occur.

VideoBlackSettings -> (structure)

MediaLive will perform a failover if content is considered black for the specified period.

BlackDetectThreshold -> (double)

A value used in calculating the threshold below which MediaLive considers a pixel to be âblackâ. For the input to be considered black, every pixel in a frame must be below this threshold. The threshold is calculated as a percentage (expressed as a decimal) of white. Therefore .1 means 10% white (or 90% black). Note how the formula works for any color depth. For example, if you set this field to 0.1 in 10-bit color depth: (1023*0.1=102.3), which means a pixel value of 102 or less is âblackâ. If you set this field to .1 in an 8-bit color depth: (255*0.1=25.5), which means a pixel value of 25 or less is âblackâ. The range is 0.0 to 1.0, with any number of decimal places.

VideoBlackThresholdMsec -> (integer)

The amount of time (in milliseconds) that the active input must be black before automatic input failover occurs.

InputPreference -> (string)

Input preference when deciding which input to make active when a previously failed input has recovered.

SecondaryInputId -> (string)

The input ID of the secondary input in the automatic input failover pair.

InputAttachmentName -> (string)

User-specified name for the attachment. This is required if the user wants to use this input in an input switch action.

InputId -> (string)

The ID of the input

InputSettings -> (structure)

Settings of an input (caption selector, etc.)

AudioSelectors -> (list)

Used to select the audio stream to decode for inputs that have multiple available.

(structure)

Audio Selector

Name -> (string)

The name of this AudioSelector. AudioDescriptions will use this name to uniquely identify this Selector. Selector names should be unique per input.

SelectorSettings -> (structure)

The audio selector settings.

AudioHlsRenditionSelection -> (structure)

Audio Hls Rendition Selection

GroupId -> (string)

Specifies the GROUP-ID in the #EXT-X-MEDIA tag of the target HLS audio rendition.

Name -> (string)

Specifies the NAME in the #EXT-X-MEDIA tag of the target HLS audio rendition.

AudioLanguageSelection -> (structure)

Audio Language Selection

LanguageCode -> (string)

Selects a specific three-letter language code from within an audio source.

LanguageSelectionPolicy -> (string)

When set to âstrictâ, the transport stream demux strictly identifies audio streams by their language descriptor. If a PMT update occurs such that an audio stream matching the initially selected language is no longer present then mute will be encoded until the language returns. If âlooseâ, then on a PMT update the demux will choose another audio stream in the program with the same stream type if it canât find one with the same language.

AudioPidSelection -> (structure)

Audio Pid Selection

Pid -> (integer)

Selects a specific PID from within a source.

AudioTrackSelection -> (structure)

Audio Track Selection

Tracks -> (list)

Selects one or more unique audio tracks from within a source.

(structure)

Audio Track

Track -> (integer)

1-based integer value that maps to a specific audio track

DolbyEDecode -> (structure)

Configure decoding options for Dolby E streams - these should be Dolby E frames carried in PCM streams tagged with SMPTE-337

ProgramSelection -> (string)

Applies only to Dolby E. Enter the program ID (according to the metadata in the audio) of the Dolby E program to extract from the specified track. One program extracted per audio selector. To select multiple programs, create multiple selectors with the same Track and different Program numbers. âAll channelsâ means to ignore the program IDs and include all the channels in this selector; useful if metadata is known to be incorrect.

CaptionSelectors -> (list)

Used to select the caption input to use for inputs that have multiple available.

(structure)

Caption Selector

LanguageCode -> (string)

When specified this field indicates the three letter language code of the caption track to extract from the source.

Name -> (string)

Name identifier for a caption selector. This name is used to associate this caption selector with one or more caption descriptions. Names must be unique within an event.

SelectorSettings -> (structure)

Caption selector settings.

AncillarySourceSettings -> (structure)

Ancillary Source Settings

SourceAncillaryChannelNumber -> (integer)

Specifies the number (1 to 4) of the captions channel you want to extract from the ancillary captions. If you plan to convert the ancillary captions to another format, complete this field. If you plan to choose Embedded as the captions destination in the output (to pass through all the channels in the ancillary captions), leave this field blank because MediaLive ignores the field.

AribSourceSettings -> (structure)

Arib Source Settings

DvbSubSourceSettings -> (structure)

Dvb Sub Source Settings

OcrLanguage -> (string)

If you will configure a WebVTT caption description that references this caption selector, use this field to provide the language to consider when translating the image-based source to text.

Pid -> (integer)

When using DVB-Sub with Burn-In or SMPTE-TT, use this PID for the source content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors.

EmbeddedSourceSettings -> (structure)

Embedded Source Settings

Convert608To708 -> (string)

If upconvert, 608 data is both passed through via the â608 compatibility bytesâ fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.

Scte20Detection -> (string)

Set to âautoâ to handle streams with intermittent and/or non-aligned SCTE-20 and Embedded captions.

Source608ChannelNumber -> (integer)

Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.

Source608TrackNumber -> (integer)

This field is unused and deprecated.

Scte20SourceSettings -> (structure)

Scte20 Source Settings

Convert608To708 -> (string)

If upconvert, 608 data is both passed through via the â608 compatibility bytesâ fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.

Source608ChannelNumber -> (integer)

Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.

Scte27SourceSettings -> (structure)

Scte27 Source Settings

OcrLanguage -> (string)

If you will configure a WebVTT caption description that references this caption selector, use this field to provide the language to consider when translating the image-based source to text.

Pid -> (integer)

The pid field is used in conjunction with the caption selector languageCode field as follows: - Specify PID and Language: Extracts captions from that PID; the language is âinformationalâ. - Specify PID and omit Language: Extracts the specified PID. - Omit PID and specify Language: Extracts the specified language, whichever PID that happens to be. - Omit PID and omit Language: Valid only if source is DVB-Sub that is being passed through; all languages will be passed through.

TeletextSourceSettings -> (structure)

Teletext Source Settings

OutputRectangle -> (structure)

Optionally defines a region where TTML style captions will be displayed

Height -> (double)

See the description in leftOffset. For height, specify the entire height of the rectangle as a percentage of the underlying frame height. For example, "80" means the rectangle height is 80% of the underlying frame height. The topOffset and rectangleHeight must add up to 100% or less. This field corresponds to tts:extent - Y in the TTML standard.

LeftOffset -> (double)

Applies only if you plan to convert these source captions to EBU-TT-D or TTML in an output. (Make sure to leave the default if you donât have either of these formats in the output.) You can define a display rectangle for the captions that is smaller than the underlying video frame. You define the rectangle by specifying the position of the left edge, top edge, bottom edge, and right edge of the rectangle, all within the underlying video frame. The units for the measurements are percentages. If you specify a value for one of these fields, you must specify a value for all of them. For leftOffset, specify the position of the left edge of the rectangle, as a percentage of the underlying frame width, and relative to the left edge of the frame. For example, "10" means the measurement is 10% of the underlying frame width. The rectangle left edge starts at that position from the left edge of the frame. This field corresponds to tts:origin - X in the TTML standard.

TopOffset -> (double)

See the description in leftOffset. For topOffset, specify the position of the top edge of the rectangle, as a percentage of the underlying frame height, and relative to the top edge of the frame. For example, "10" means the measurement is 10% of the underlying frame height. The rectangle top edge starts at that position from the top edge of the frame. This field corresponds to tts:origin - Y in the TTML standard.

Width -> (double)

See the description in leftOffset. For width, specify the entire width of the rectangle as a percentage of the underlying frame width. For example, "80" means the rectangle width is 80% of the underlying frame width. The leftOffset and rectangleWidth must add up to 100% or less. This field corresponds to tts:extent - X in the TTML standard.

PageNumber -> (string)

Specifies the teletext page number within the data stream from which to extract captions. Range of 0x100 (256) to 0x8FF (2303). Unused for passthrough. Should be specified as a hexadecimal string with no â0xâ prefix.

DeblockFilter -> (string)

Enable or disable the deblock filter when filtering.

DenoiseFilter -> (string)

Enable or disable the denoise filter when filtering.

FilterStrength -> (integer)

Adjusts the magnitude of filtering from 1 (minimal) to 5 (strongest).

InputFilter -> (string)

Turns on the filter for this input. MPEG-2 inputs have the deblocking filter enabled by default. 1) auto - filtering will be applied depending on input type/quality 2) disabled - no filtering will be applied to the input 3) forced - filtering will be applied regardless of input type

NetworkInputSettings -> (structure)

Input settings.

HlsInputSettings -> (structure)

Specifies HLS input settings when the uri is for a HLS manifest.

Bandwidth -> (integer)

When specified the HLS stream with the m3u8 BANDWIDTH that most closely matches this value will be chosen, otherwise the highest bandwidth stream in the m3u8 will be chosen. The bitrate is specified in bits per second, as in an HLS manifest.

BufferSegments -> (integer)

When specified, reading of the HLS input will begin this many buffer segments from the end (most recently written segment). When not specified, the HLS input will begin with the first segment specified in the m3u8.

Retries -> (integer)

The number of consecutive times that attempts to read a manifest or segment must fail before the input is considered unavailable.

RetryInterval -> (integer)

The number of seconds between retries when an attempt to read a manifest or segment fails.

Scte35Source -> (string)

Identifies the source for the SCTE-35 messages that MediaLive will ingest. Messages can be ingested from the content segments (in the stream) or from tags in the playlist (the HLS manifest). MediaLive ignores SCTE-35 information in the source that is not selected.

ServerValidation -> (string)

Check HTTPS server certificates. When set to checkCryptographyOnly, cryptography in the certificate will be checked, but not the serverâs name. Certain subdomains (notably S3 buckets that use dots in the bucket name) do not strictly match the corresponding certificateâs wildcard pattern and would otherwise cause the event to error. This setting is ignored for protocols that do not use https.

MulticastInputSettings -> (structure)

Specifies multicast input settings when the uri is for a multicast event.

SourceIpAddress -> (string)

Optionally, a source ip address to filter by for Source-specific Multicast (SSM)

Scte35Pid -> (integer)

PID from which to read SCTE-35 messages. If left undefined, EML will select the first SCTE-35 PID found in the input.

Smpte2038DataPreference -> (string)

Specifies whether to extract applicable ancillary data from a SMPTE-2038 source in this input. Applicable data types are captions, timecode, AFD, and SCTE-104 messages. - PREFER: Extract from SMPTE-2038 if present in this input, otherwise extract from another source (if any). - IGNORE: Never extract any ancillary data from SMPTE-2038.

SourceEndBehavior -> (string)

Loop input if it is a file. This allows a file input to be streamed indefinitely.

VideoSelector -> (structure)

Informs which video elementary stream to decode for input types that have multiple available.

ColorSpace -> (string)

Specifies the color space of an input. This setting works in tandem with colorSpaceUsage and a video descriptionâs colorSpaceSettingsChoice to determine if any conversion will be performed.

ColorSpaceSettings -> (structure)

Color space settings

Hdr10Settings -> (structure)

Hdr10 Settings

MaxCll -> (integer)

Maximum Content Light Level An integer metadata value defining the maximum light level, in nits, of any single pixel within an encoded HDR video stream or file.

MaxFall -> (integer)

Maximum Frame Average Light Level An integer metadata value defining the maximum average light level, in nits, for any single frame within an encoded HDR video stream or file.

ColorSpaceUsage -> (string)

Applies only if colorSpace is a value other than follow. This field controls how the value in the colorSpace field will be used. fallback means that when the input does include color space data, that data will be used, but when the input has no color space data, the value in colorSpace will be used. Choose fallback if your input is sometimes missing color space data, but when it does have color space data, that data is correct. force means to always use the value in colorSpace. Choose force if your input usually has no color space data or might have unreliable color space data.

SelectorSettings -> (structure)

The video selector settings.

VideoSelectorPid -> (structure)

Video Selector Pid

Pid -> (integer)

Selects a specific PID from within a video source.

VideoSelectorProgramId -> (structure)

Video Selector Program Id

ProgramId -> (integer)

Selects a specific program from within a multi-program transport stream. If the program doesnât exist, the first program within the transport stream will be selected by default.

LogicalInterfaceNames -> (list)

Optional assignment of an input to a logical interface on the Node. Only applies to on premises channels.

(string)

Placeholder documentation for __string

InputSpecification -> (structure)

Specification of network and file inputs for this channel

Codec -> (string)

Input codec

MaximumBitrate -> (string)

Maximum input bitrate, categorized coarsely

Resolution -> (string)

Input resolution, categorized coarsely

LogLevel -> (string)

The log level being written to CloudWatch Logs.

Maintenance -> (structure)

Maintenance settings for this channel.

MaintenanceDay -> (string)

The currently selected maintenance day.

MaintenanceDeadline -> (string)

Maintenance is required by the displayed date and time. Date and time is in ISO.

MaintenanceScheduledDate -> (string)

The currently scheduled maintenance date and time. Date and time is in ISO.

MaintenanceStartTime -> (string)

The currently selected maintenance start time. Time is in UTC.

Name -> (string)

The name of the channel. (user-mutable)

PipelineDetails -> (list)

Runtime details for the pipelines of a running channel.

(structure)

Runtime details of a pipeline when a channel is running.

ActiveInputAttachmentName -> (string)

The name of the active input attachment currently being ingested by this pipeline.

ActiveInputSwitchActionName -> (string)

The name of the input switch schedule action that occurred most recently and that resulted in the switch to the current input attachment for this pipeline.

ActiveMotionGraphicsActionName -> (string)

The name of the motion graphics activate action that occurred most recently and that resulted in the current graphics URI for this pipeline.

ActiveMotionGraphicsUri -> (string)

The current URI being used for HTML5 motion graphics for this pipeline.

PipelineId -> (string)

Pipeline ID

ChannelEngineVersion -> (structure)

Current engine version of the encoder for this pipeline.

ExpirationDate -> (timestamp)

The UTC time when the version expires.

Version -> (string)

The build identifier for this version of the channel version.

PipelinesRunningCount -> (integer)

The number of currently healthy pipelines.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the role assumed when running the Channel.

State -> (string)

Placeholder documentation for ChannelState

Tags -> (map)

A collection of key-value pairs.

key -> (string)

Placeholder documentation for __string

value -> (string)

Placeholder documentation for __string

Vpc -> (structure)

Settings for VPC output

AvailabilityZones -> (list)

The Availability Zones where the vpc subnets are located. The first Availability Zone applies to the first subnet in the list of subnets. The second Availability Zone applies to the second subnet.

(string)

Placeholder documentation for __string

NetworkInterfaceIds -> (list)

A list of Elastic Network Interfaces created by MediaLive in the customerâs VPC

(string)

Placeholder documentation for __string

SecurityGroupIds -> (list)

A list of up EC2 VPC security group IDs attached to the Output VPC network interfaces.

(string)

Placeholder documentation for __string

SubnetIds -> (list)

A list of VPC subnet IDs from the same VPC. If STANDARD channel, subnet IDs must be mapped to two unique availability zones (AZ).

(string)

Placeholder documentation for __string

AnywhereSettings -> (structure)

Anywhere settings for this channel.

ChannelPlacementGroupId -> (string)

The ID of the channel placement group for the channel.

ClusterId -> (string)

The ID of the cluster for the channel.

ChannelEngineVersion -> (structure)

Requested engine version for this channel.

ExpirationDate -> (timestamp)

The UTC time when the version expires.

Version -> (string)

The build identifier for this version of the channel version.