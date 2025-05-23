# list-channelsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-channels.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-channels.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [medialive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/index.html#cli-aws-medialive) ]

# list-channels

## Description

Produces list of channels that have been created

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/ListChannels)

`list-channels` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Channels`

## Synopsis

```
list-channels
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

Channels -> (list)

Placeholder documentation for __listOfChannelSummary

(structure)

Placeholder documentation for ChannelSummary

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

Settings for any VPC outputs.

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

AnywhereSettings settings for this channel.

ChannelPlacementGroupId -> (string)

The ID of the channel placement group for the channel.

ClusterId -> (string)

The ID of the cluster for the channel.

ChannelEngineVersion -> (structure)

The engine version that you requested for this channel.

ExpirationDate -> (timestamp)

The UTC time when the version expires.

Version -> (string)

The build identifier for this version of the channel version.

UsedChannelEngineVersions -> (list)

The engine version that the running pipelines are using.

(structure)

Placeholder documentation for ChannelEngineVersionResponse

ExpirationDate -> (timestamp)

The UTC time when the version expires.

Version -> (string)

The build identifier for this version of the channel version.

NextToken -> (string)

Placeholder documentation for __string