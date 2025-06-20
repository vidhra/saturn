# list-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediaconvert](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/index.html#cli-aws-mediaconvert) ]

# list-jobs

## Description

Retrieve a JSON array of up to twenty of your most recently created jobs. This array includes in-process, completed, and errored jobs. This will return the jobs themselves, not just a list of the jobs. To retrieve the twenty next most recent jobs, use the nextToken string returned with the array.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconvert-2017-08-29/ListJobs)

`list-jobs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Jobs`

## Synopsis

```
list-jobs
[--order <value>]
[--queue <value>]
[--status <value>]
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

`--order` (string)
Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.

Possible values:

- `ASCENDING`
- `DESCENDING`

`--queue` (string)
Optional. Provide a queue name to get back only jobs from that queue.

`--status` (string)
Optional. A jobâs status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR.

Possible values:

- `SUBMITTED`
- `PROGRESSING`
- `COMPLETE`
- `CANCELED`
- `ERROR`

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To get details for all jobs in a region**

The following example requests the information for all of your jobs in the specified region.

```
aws mediaconvert list-jobs \
    --endpoint-url https://abcd1234.mediaconvert.region-name-1.amazonaws.com \
    --region region-name-1
```

To get your account-specific endpoint, use `describe-endpoints`, or send the command without the endpoint. The service returns an error and your endpoint.

For more information, see [Working with AWS Elemental MediaConvert Jobs](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-jobs.html) in the *AWS Elemental MediaConvert User Guide*.

## Output

Jobs -> (list)

List of jobs

(structure)

Each job converts an input file into an output file or files. For more information, see the User Guide at [https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html)

AccelerationSettings -> (structure)

Accelerated transcoding can significantly speed up jobs with long, visually complex content.

Mode -> (string)

Specify the conditions when the service will run your job with accelerated transcoding.

AccelerationStatus -> (string)

Describes whether the current job is running with accelerated transcoding. For jobs that have Acceleration (AccelerationMode) set to DISABLED, AccelerationStatus is always NOT_APPLICABLE. For jobs that have Acceleration (AccelerationMode) set to ENABLED or PREFERRED, AccelerationStatus is one of the other states. AccelerationStatus is IN_PROGRESS initially, while the service determines whether the input files and job settings are compatible with accelerated transcoding. If they are, AcclerationStatus is ACCELERATED. If your input files and job settings arenât compatible with accelerated transcoding, the service either fails your job or runs it without accelerated transcoding, depending on how you set Acceleration (AccelerationMode). When the service runs your job without accelerated transcoding, AccelerationStatus is NOT_ACCELERATED.

Arn -> (string)

An identifier for this resource that is unique within all of AWS.

BillingTagsSource -> (string)

The tag type that AWS Billing and Cost Management will use to sort your AWS Elemental MediaConvert costs on any billing report that you set up.

ClientRequestToken -> (string)

Prevent duplicate jobs from being created and ensure idempotency for your requests. A client request token can be any string that includes up to 64 ASCII characters. If you reuse a client request token within one minute of a successful request, the API returns the job details of the original request instead. For more information see [https://docs.aws.amazon.com/mediaconvert/latest/apireference/idempotency.html](https://docs.aws.amazon.com/mediaconvert/latest/apireference/idempotency.html).

CreatedAt -> (timestamp)

The time, in Unix epoch format in seconds, when the job got created.

CurrentPhase -> (string)

A jobâs phase can be PROBING, TRANSCODING OR UPLOADING

ErrorCode -> (integer)

Error code for the job

ErrorMessage -> (string)

Error message of Job

HopDestinations -> (list)

Optional list of hop destinations.

(structure)

Optional. Configuration for a destination queue to which the job can hop once a customer-defined minimum wait time has passed.

Priority -> (integer)

Optional. When you set up a job to use queue hopping, you can specify a different relative priority for the job in the destination queue. If you donât specify, the relative priority will remain the same as in the previous queue.

Queue -> (string)

Optional unless the job is submitted on the default queue. When you set up a job to use queue hopping, you can specify a destination queue. This queue cannot be the original queue to which the job is submitted. If the original queue isnât the default queue and you donât specify the destination queue, the job will move to the default queue.

WaitMinutes -> (integer)

Required for setting up a job to use queue hopping. Minimum wait time in minutes until the job can hop to the destination queue. Valid range is 1 to 4320 minutes, inclusive.

Id -> (string)

A portion of the jobâs ARN, unique within your AWS Elemental MediaConvert resources

JobEngineVersionRequested -> (string)

The Job engine version that you requested for your job. Valid versions are in a YYYY-MM-DD format.

JobEngineVersionUsed -> (string)

The Job engine version that your job used. Job engine versions are in a YYYY-MM-DD format. When you request an expired version, the response for this property will be empty. Requests to create jobs with an expired version result in a regular job, as if no specific Job engine version was requested. When you request an invalid version, the response for this property will be empty. Requests to create jobs with an invalid version result in a 400 error message, and no job is created.

JobPercentComplete -> (integer)

An estimate of how far your job has progressed. This estimate is shown as a percentage of the total time from when your job leaves its queue to when your output files appear in your output Amazon S3 bucket. AWS Elemental MediaConvert provides jobPercentComplete in CloudWatch STATUS_UPDATE events and in the response to GetJob and ListJobs requests. The jobPercentComplete estimate is reliable for the following input containers: Quicktime, Transport Stream, MP4, and MXF. For some jobs, the service canât provide information about job progress. In those cases, jobPercentComplete returns a null value.

JobTemplate -> (string)

The job template that the job is created from, if it is created from a job template.

Messages -> (structure)

Provides messages from the service about jobs that you have already successfully submitted.

Info -> (list)

List of messages that are informational only and donât indicate a problem with your job.

(string)

Warning -> (list)

List of messages that warn about conditions that might cause your job not to run or to fail.

(string)

OutputGroupDetails -> (list)

List of output group details

(structure)

Contains details about the output groups specified in the job settings.

OutputDetails -> (list)

Details about the output

(structure)

Details regarding output

DurationInMs -> (integer)

Duration in milliseconds

VideoDetails -> (structure)

Contains details about the outputâs video stream

HeightInPx -> (integer)

Height in pixels for the output

WidthInPx -> (integer)

Width in pixels for the output

Priority -> (integer)

Relative priority on the job.

Queue -> (string)

When you create a job, you can specify a queue to send it to. If you donât specify, the job will go to the default queue. For more about queues, see the User Guide topic at [https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html)

QueueTransitions -> (list)

The jobâs queue hopping history.

(structure)

Description of the source and destination queues between which the job has moved, along with the timestamp of the move

DestinationQueue -> (string)

The queue that the job was on after the transition.

SourceQueue -> (string)

The queue that the job was on before the transition.

Timestamp -> (timestamp)

The time, in Unix epoch format, that the job moved from the source queue to the destination queue.

RetryCount -> (integer)

The number of times that the service automatically attempted to process your job after encountering an error.

Role -> (string)

The IAM role you use for creating this job. For details about permissions, see the User Guide topic at the User Guide at [https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html)

Settings -> (structure)

JobSettings contains all the transcode settings for a job.

AdAvailOffset -> (integer)

When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time.

AvailBlanking -> (structure)

Settings for ad avail blanking. Video can be blanked or overlaid with an image, and audio muted during SCTE-35 triggered ad avails.

AvailBlankingImage -> (string)

Blanking image to be used. Leave empty for solid black. Only bmp and png images are supported.

ColorConversion3DLUTSettings -> (list)

Use 3D LUTs to specify custom color mapping behavior when you convert from one color space into another. You can include up to 8 different 3D LUTs. For more information, see: [https://docs.aws.amazon.com/mediaconvert/latest/ug/3d-luts.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/3d-luts.html)

(structure)

Custom 3D lut settings

FileInput -> (string)

Specify the input file S3, HTTP, or HTTPS URL for your 3D LUT .cube file. Note that MediaConvert accepts 3D LUT files up to 8MB in size.

InputColorSpace -> (string)

Specify which inputs use this 3D LUT, according to their color space.

InputMasteringLuminance -> (integer)

Specify which inputs use this 3D LUT, according to their luminance. To apply this 3D LUT to HDR10 or P3D65 (HDR) inputs with a specific mastering luminance: Enter an integer from 0 to 2147483647, corresponding to the inputâs Maximum luminance value. To apply this 3D LUT to any input regardless of its luminance: Leave blank, or enter 0.

OutputColorSpace -> (string)

Specify which outputs use this 3D LUT, according to their color space.

OutputMasteringLuminance -> (integer)

Specify which outputs use this 3D LUT, according to their luminance. To apply this 3D LUT to HDR10 or P3D65 (HDR) outputs with a specific luminance: Enter an integer from 0 to 2147483647, corresponding to the outputâs luminance. To apply this 3D LUT to any output regardless of its luminance: Leave blank, or enter 0.

Esam -> (structure)

Settings for Event Signaling And Messaging (ESAM). If you donât do ad insertion, you can ignore these settings.

ManifestConfirmConditionNotification -> (structure)

Specifies an ESAM ManifestConfirmConditionNotification XML as per OC-SP-ESAM-API-I03-131025. The transcoder uses the manifest conditioning instructions that you provide in the setting MCC XML.

MccXml -> (string)

Provide your ESAM ManifestConfirmConditionNotification XML document inside your JSON job settings. Form the XML document as per OC-SP-ESAM-API-I03-131025. The transcoder will use the Manifest Conditioning instructions in the message that you supply.

ResponseSignalPreroll -> (integer)

Specifies the stream distance, in milliseconds, between the SCTE 35 messages that the transcoder places and the splice points that they refer to. If the time between the start of the asset and the SCTE-35 message is less than this value, then the transcoder places the SCTE-35 marker at the beginning of the stream.

SignalProcessingNotification -> (structure)

Specifies an ESAM SignalProcessingNotification XML as per OC-SP-ESAM-API-I03-131025. The transcoder uses the signal processing instructions that you provide in the setting SCC XML.

SccXml -> (string)

Provide your ESAM SignalProcessingNotification XML document inside your JSON job settings. Form the XML document as per OC-SP-ESAM-API-I03-131025. The transcoder will use the signal processing instructions in the message that you supply. For your MPEG2-TS file outputs, if you want the service to place SCTE-35 markers at the insertion points you specify in the XML document, you must also enable SCTE-35 ESAM. Note that you can either specify an ESAM XML document or enable SCTE-35 passthrough. You canât do both.

ExtendedDataServices -> (structure)

If your source content has EIA-608 Line 21 Data Services, enable this feature to specify what MediaConvert does with the Extended Data Services (XDS) packets. You can choose to pass through XDS packets, or remove them from the output. For more information about XDS, see EIA-608 Line Data Services, section 9.5.1.5 05h Content Advisory.

CopyProtectionAction -> (string)

The action to take on copy and redistribution control XDS packets. If you select PASSTHROUGH, packets will not be changed. If you select STRIP, any packets will be removed in output captions.

VchipAction -> (string)

The action to take on content advisory XDS packets. If you select PASSTHROUGH, packets will not be changed. If you select STRIP, any packets will be removed in output captions.

FollowSource -> (integer)

Specify the input that MediaConvert references for your default output settings. MediaConvert uses this inputâs Resolution, Frame rate, and Pixel aspect ratio for all outputs that you donât manually specify different output settings for. Enabling this setting will disable âFollow sourceâ for all other inputs. If MediaConvert cannot follow your source, for example if you specify an audio-only input, MediaConvert uses the first followable input instead. In your JSON job specification, enter an integer from 1 to 150 corresponding to the order of your inputs.

Inputs -> (list)

Use Inputs to define source file used in the transcode job. There can be multiple inputs add in a job. These inputs will be concantenated together to create the output.

(structure)

Use inputs to define the source files used in your transcoding job. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/specify-input-settings.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/specify-input-settings.html). You can use multiple video inputs to do input stitching. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/assembling-multiple-inputs-and-input-clips.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/assembling-multiple-inputs-and-input-clips.html)

AdvancedInputFilter -> (string)

Use to remove noise, blocking, blurriness, or ringing from your input as a pre-filter step before encoding. The Advanced input filter removes more types of compression artifacts and is an improvement when compared to basic Deblock and Denoise filters. To remove video compression artifacts from your input and improve the video quality: Choose Enabled. Additionally, this filter can help increase the video quality of your output relative to its bitrate, since noisy inputs are more complex and require more bits to encode. To help restore loss of detail after applying the filter, you can optionally add texture or sharpening as an additional step. Jobs that use this feature incur pro-tier pricing. To not apply advanced input filtering: Choose Disabled. Note that you can still apply basic filtering with Deblock and Denoise.

AdvancedInputFilterSettings -> (structure)

Optional settings for Advanced input filter when you set Advanced input filter to Enabled.

AddTexture -> (string)

Add texture and detail to areas of your input video content that were lost after applying the Advanced input filter. To adaptively add texture and reduce softness: Choose Enabled. To not add any texture: Keep the default value, Disabled. We recommend that you choose Disabled for input video content that doesnât have texture, including screen recordings, computer graphics, or cartoons.

Sharpening -> (string)

Optionally specify the amount of sharpening to apply when you use the Advanced input filter. Sharpening adds contrast to the edges of your video content and can reduce softness. To apply no sharpening: Keep the default value, Off. To apply a minimal amount of sharpening choose Low, or for the maximum choose High.

AudioSelectorGroups -> (map)

Use audio selector groups to combine multiple sidecar audio inputs so that you can assign them to a single output audio tab. Note that, if youâre working with embedded audio, itâs simpler to assign multiple input tracks into a single audio selector rather than use an audio selector group.

key -> (string)

value -> (structure)

Use audio selector groups to combine multiple sidecar audio inputs so that you can assign them to a single output audio tab. Note that, if youâre working with embedded audio, itâs simpler to assign multiple input tracks into a single audio selector rather than use an audio selector group.

AudioSelectorNames -> (list)

Name of an Audio Selector within the same input to include in the group. Audio selector names are standardized, based on their order within the input (e.g., âAudio Selector 1â). The audio selector name parameter can be repeated to add any number of audio selectors to the group.

(string)

AudioSelectors -> (map)

Use Audio selectors to specify a track or set of tracks from the input that you will use in your outputs. You can use multiple Audio selectors per input.

key -> (string)

value -> (structure)

Use Audio selectors to specify a track or set of tracks from the input that you will use in your outputs. You can use multiple Audio selectors per input.

AudioDurationCorrection -> (string)

Apply audio timing corrections to help synchronize audio and video in your output. To apply timing corrections, your input must meet the following requirements: * Container: MP4, or MOV, with an accurate time-to-sample (STTS) table. * Audio track: AAC. Choose from the following audio timing correction settings: * Disabled (Default): Apply no correction. * Auto: Recommended for most inputs. MediaConvert analyzes the audio timing in your input and determines which correction setting to use, if needed. * Track: Adjust the duration of each audio frame by a constant amount to align the audio track length with STTS duration. Track-level correction does not affect pitch, and is recommended for tonal audio content such as music. * Frame: Adjust the duration of each audio frame by a variable amount to align audio frames with STTS timestamps. No corrections are made to already-aligned frames. Frame-level correction may affect the pitch of corrected frames, and is recommended for atonal audio content such as speech or percussion. * Force: Apply audio duration correction, either Track or Frame depending on your input, regardless of the accuracy of your inputâs STTS table. Your output audio and video may not be aligned or it may contain audio artifacts.

CustomLanguageCode -> (string)

Selects a specific language code from within an audio source, using the ISO 639-2 or ISO 639-3 three-letter language code

DefaultSelection -> (string)

Enable this setting on one audio selector to set it as the default for the job. The service uses this default for outputs where it canât find the specified input audio. If you donât set a default, those outputs have no audio.

ExternalAudioFileInput -> (string)

Specify the S3, HTTP, or HTTPS URL for your external audio file input.

HlsRenditionGroupSettings -> (structure)

Settings specific to audio sources in an HLS alternate rendition group. Specify the properties (renditionGroupId, renditionName or renditionLanguageCode) to identify the unique audio track among the alternative rendition groups present in the HLS manifest. If no unique track is found, or multiple tracks match the properties provided, the job fails. If no properties in hlsRenditionGroupSettings are specified, the default audio track within the video segment is chosen. If there is no audio within video segment, the alternative audio with DEFAULT=YES is chosen instead.

RenditionGroupId -> (string)

Optional. Specify alternative group ID

RenditionLanguageCode -> (string)

Optional. Specify ISO 639-2 or ISO 639-3 code in the language property

RenditionName -> (string)

Optional. Specify media name

LanguageCode -> (string)

Specify the language to select from your audio input. In the MediaConvert console choose from a list of languages. In your JSON job settings choose from an ISO 639-2 three-letter code listed at [https://www.loc.gov/standards/iso639-2/php/code_list.php](https://www.loc.gov/standards/iso639-2/php/code_list.php)

Offset -> (integer)

Specify a time delta, in milliseconds, to offset the audio from the input video. To specify no offset: Keep the default value, 0. To specify an offset: Enter an integer from -2147483648 to 2147483647

Pids -> (list)

Selects a specific PID from within an audio source (e.g. 257 selects PID 0x101).

(integer)

ProgramSelection -> (integer)

Use this setting for input streams that contain Dolby E, to have the service extract specific program data from the track. To select multiple programs, create multiple selectors with the same Track and different Program numbers. In the console, this setting is visible when you set Selector type to Track. Choose the program number from the dropdown list. If your input file has incorrect metadata, you can choose All channels instead of a program number to have the service ignore the program IDs and include all the programs in the track.

RemixSettings -> (structure)

Use these settings to reorder the audio channels of one input to match those of another input. This allows you to combine the two files into a single output, one after the other.

AudioDescriptionAudioChannel -> (integer)

Optionally specify the channel in your input that contains your audio description audio signal. MediaConvert mixes your audio signal across all output channels, while reducing their volume according to your data stream. When you specify an audio description audio channel, you must also specify an audio description data channel. For more information about audio description signals, see the BBC WHP 198 and 051 white papers.

AudioDescriptionDataChannel -> (integer)

Optionally specify the channel in your input that contains your audio description data stream. MediaConvert mixes your audio signal across all output channels, while reducing their volume according to your data stream. When you specify an audio description data channel, you must also specify an audio description audio channel. For more information about audio description signals, see the BBC WHP 198 and 051 white papers.

ChannelMapping -> (structure)

Channel mapping contains the group of fields that hold the remixing value for each channel, in dB. Specify remix values to indicate how much of the content from your input audio channel you want in your output audio channels. Each instance of the InputChannels or InputChannelsFineTune array specifies these values for one output channel. Use one instance of this array for each output channel. In the console, each array corresponds to a column in the graphical depiction of the mapping matrix. The rows of the graphical matrix correspond to input channels. Valid values are within the range from -60 (mute) through 6. A setting of 0 passes the input channel unchanged to the output channel (no attenuation or amplification). Use InputChannels or InputChannelsFineTune to specify your remix values. Donât use both.

OutputChannels -> (list)

In your JSON job specification, include one child of OutputChannels for each audio channel that you want in your output. Each child should contain one instance of InputChannels or InputChannelsFineTune.

(structure)

OutputChannel mapping settings.

InputChannels -> (list)

Use this setting to specify your remix values when they are integers, such as -10, 0, or 4.

(integer)

InputChannelsFineTune -> (list)

Use this setting to specify your remix values when they have a decimal component, such as -10.312, 0.08, or 4.9. MediaConvert rounds your remixing values to the nearest thousandth.

(double)

ChannelsIn -> (integer)

Specify the number of audio channels from your input that you want to use in your output. With remixing, you might combine or split the data in these channels, so the number of channels in your final output might be different. If you are doing both input channel mapping and output channel mapping, the number of output channels in your input mapping must be the same as the number of input channels in your output mapping.

ChannelsOut -> (integer)

Specify the number of channels in this output after remixing. Valid values: 1, 2, 4, 6, 8â¦ 64. (1 and even numbers to 64.) If you are doing both input channel mapping and output channel mapping, the number of output channels in your input mapping must be the same as the number of input channels in your output mapping.

SelectorType -> (string)

Specifies the type of the audio selector.

Tracks -> (list)

Identify a track from the input audio to include in this selector by entering the track index number. To include several tracks in a single audio selector, specify multiple tracks as follows. Using the console, enter a comma-separated list. For example, type â1,2,3â to include tracks 1 through 3.

(integer)

CaptionSelectors -> (map)

Use captions selectors to specify the captions data from your input that you use in your outputs. You can use up to 100 captions selectors per input.

key -> (string)

value -> (structure)

Use captions selectors to specify the captions data from your input that you use in your outputs. You can use up to 100 captions selectors per input.

CustomLanguageCode -> (string)

The specific language to extract from source, using the ISO 639-2 or ISO 639-3 three-letter language code. If input is SCTE-27, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub and output is Burn-in, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub that is being passed through, omit this field (and PID field); there is no way to extract a specific language with pass-through captions.

LanguageCode -> (string)

The specific language to extract from source. If input is SCTE-27, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub and output is Burn-in, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub that is being passed through, omit this field (and PID field); there is no way to extract a specific language with pass-through captions.

SourceSettings -> (structure)

If your input captions are SCC, TTML, STL, SMI, SRT, or IMSC in an xml file, specify the URI of the input captions source file. If your input captions are IMSC in an IMF package, use TrackSourceSettings instead of FileSoureSettings.

AncillarySourceSettings -> (structure)

Settings for ancillary captions source.

Convert608To708 -> (string)

Specify whether this set of input captions appears in your outputs in both 608 and 708 format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the 608 data through using the 608 compatibility bytes fields of the 708 wrapper, and it also translates the 608 data into 708.

SourceAncillaryChannelNumber -> (integer)

Specifies the 608 channel number in the ancillary data track from which to extract captions. Unused for passthrough.

TerminateCaptions -> (string)

By default, the service terminates any unterminated captions at the end of each input. If you want the caption to continue onto your next input, disable this setting.

DvbSubSourceSettings -> (structure)

DVB Sub Source Settings

Pid -> (integer)

When using DVB-Sub with Burn-in, use this PID for the source content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors.

EmbeddedSourceSettings -> (structure)

Settings for embedded captions Source

Convert608To708 -> (string)

Specify whether this set of input captions appears in your outputs in both 608 and 708 format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the 608 data through using the 608 compatibility bytes fields of the 708 wrapper, and it also translates the 608 data into 708.

Source608ChannelNumber -> (integer)

Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.

Source608TrackNumber -> (integer)

Specifies the video track index used for extracting captions. The system only supports one input video track, so this should always be set to â1â.

TerminateCaptions -> (string)

By default, the service terminates any unterminated captions at the end of each input. If you want the caption to continue onto your next input, disable this setting.

FileSourceSettings -> (structure)

If your input captions are SCC, SMI, SRT, STL, TTML, WebVTT, or IMSC 1.1 in an xml file, specify the URI of the input caption source file. If your caption source is IMSC in an IMF package, use TrackSourceSettings instead of FileSoureSettings.

ByteRateLimit -> (string)

Choose whether to limit the byte rate at which your SCC input captions are inserted into your output. To not limit the caption rate: We recommend that you keep the default value, Disabled. MediaConvert inserts captions in your output according to the byte rates listed in the EIA-608 specification, typically 2 or 3 caption bytes per frame depending on your output frame rate. To limit your output caption rate: Choose Enabled. Choose this option if your downstream systems require a maximum of 2 caption bytes per frame. Note that this setting has no effect when your output frame rate is 30 or 60.

Convert608To708 -> (string)

Specify whether this set of input captions appears in your outputs in both 608 and 708 format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the 608 data through using the 608 compatibility bytes fields of the 708 wrapper, and it also translates the 608 data into 708.

ConvertPaintToPop -> (string)

Choose the presentation style of your input SCC captions. To use the same presentation style as your input: Keep the default value, Disabled. To convert paint-on captions to pop-on: Choose Enabled. We also recommend that you choose Enabled if you notice additional repeated lines in your output captions.

Framerate -> (structure)

Ignore this setting unless your input captions format is SCC. To have the service compensate for differing frame rates between your input captions and input video, specify the frame rate of the captions file. Specify this value as a fraction. For example, you might specify 24 / 1 for 24 fps, 25 / 1 for 25 fps, 24000 / 1001 for 23.976 fps, or 30000 / 1001 for 29.97 fps.

FramerateDenominator -> (integer)

Specify the denominator of the fraction that represents the frame rate for the setting Caption source frame rate. Use this setting along with the setting Framerate numerator.

FramerateNumerator -> (integer)

Specify the numerator of the fraction that represents the frame rate for the setting Caption source frame rate. Use this setting along with the setting Framerate denominator.

SourceFile -> (string)

External caption file used for loading captions. Accepted file extensions are âsccâ, âttmlâ, âdfxpâ, âstlâ, âsrtâ, âxmlâ, âsmiâ, âwebvttâ, and âvttâ.

TimeDelta -> (integer)

Optional. Use this setting when you need to adjust the sync between your sidecar captions and your video. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/time-delta-use-cases.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/time-delta-use-cases.html). Enter a positive or negative number to modify the times in the captions file. For example, type 15 to add 15 seconds to all the times in the captions file. Type -5 to subtract 5 seconds from the times in the captions file. You can optionally specify your time delta in milliseconds instead of seconds. When you do so, set the related setting, Time delta units to Milliseconds. Note that, when you specify a time delta for timecode-based caption sources, such as SCC and STL, and your time delta isnât a multiple of the input frame rate, MediaConvert snaps the captions to the nearest frame. For example, when your input video frame rate is 25 fps and you specify 1010ms for time delta, MediaConvert delays your captions by 1000 ms.

TimeDeltaUnits -> (string)

When you use the setting Time delta to adjust the sync between your sidecar captions and your video, use this setting to specify the units for the delta that you specify. When you donât specify a value for Time delta units, MediaConvert uses seconds by default.

UpconvertSTLToTeletext -> (string)

Specify whether this set of input captions appears in your outputs in both STL and Teletext format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the STL data through using the Teletext compatibility bytes fields of the Teletext wrapper, and it also translates the STL data into Teletext.

SourceType -> (string)

Use Source to identify the format of your input captions. The service cannot auto-detect caption format.

TeletextSourceSettings -> (structure)

Settings specific to Teletext caption sources, including Page number.

PageNumber -> (string)

Use Page Number to specify the three-digit hexadecimal page number that will be used for Teletext captions. Do not use this setting if you are passing through teletext from the input source to output.

TrackSourceSettings -> (structure)

Settings specific to caption sources that are specified by track number. Currently, this is only IMSC captions in an IMF package. If your caption source is IMSC 1.1 in a separate xml file, use FileSourceSettings instead of TrackSourceSettings.

TrackNumber -> (integer)

Use this setting to select a single captions track from a source. Track numbers correspond to the order in the captions source file. For IMF sources, track numbering is based on the order that the captions appear in the CPL. For example, use 1 to select the captions asset that is listed first in the CPL. To include more than one captions track in your job outputs, create multiple input captions selectors. Specify one track per selector.

WebvttHlsSourceSettings -> (structure)

Settings specific to WebVTT sources in HLS alternative rendition group. Specify the properties (renditionGroupId, renditionName or renditionLanguageCode) to identify the unique subtitle track among the alternative rendition groups present in the HLS manifest. If no unique track is found, or multiple tracks match the specified properties, the job fails. If there is only one subtitle track in the rendition group, the settings can be left empty and the default subtitle track will be chosen. If your caption source is a sidecar file, use FileSourceSettings instead of WebvttHlsSourceSettings.

RenditionGroupId -> (string)

Optional. Specify alternative group ID

RenditionLanguageCode -> (string)

Optional. Specify ISO 639-2 or ISO 639-3 code in the language property

RenditionName -> (string)

Optional. Specify media name

Crop -> (structure)

Use Cropping selection to specify the video area that the service will include in the output video frame. If you specify a value here, it will override any value that you specify in the output setting Cropping selection.

Height -> (integer)

Height of rectangle in pixels. Specify only even numbers.

Width -> (integer)

Width of rectangle in pixels. Specify only even numbers.

X -> (integer)

The distance, in pixels, between the rectangle and the left edge of the video frame. Specify only even numbers.

Y -> (integer)

The distance, in pixels, between the rectangle and the top edge of the video frame. Specify only even numbers.

DeblockFilter -> (string)

Enable Deblock to produce smoother motion in the output. Default is disabled. Only manually controllable for MPEG2 and uncompressed video inputs.

DecryptionSettings -> (structure)

Settings for decrypting any input files that you encrypt before you upload them to Amazon S3. MediaConvert can decrypt files only when you use AWS Key Management Service (KMS) to encrypt the data key that you use to encrypt your content.

DecryptionMode -> (string)

Specify the encryption mode that you used to encrypt your input files.

EncryptedDecryptionKey -> (string)

Warning! Donât provide your encryption key in plaintext. Your job settings could be intercepted, making your encrypted content vulnerable. Specify the encrypted version of the data key that you used to encrypt your content. The data key must be encrypted by AWS Key Management Service (KMS). The key can be 128, 192, or 256 bits.

InitializationVector -> (string)

Specify the initialization vector that you used when you encrypted your content before uploading it to Amazon S3. You can use a 16-byte initialization vector with any encryption mode. Or, you can use a 12-byte initialization vector with GCM or CTR. MediaConvert accepts only initialization vectors that are base64-encoded.

KmsKeyRegion -> (string)

Specify the AWS Region for AWS Key Management Service (KMS) that you used to encrypt your data key, if that Region is different from the one you are using for AWS Elemental MediaConvert.

DenoiseFilter -> (string)

Enable Denoise to filter noise from the input. Default is disabled. Only applicable to MPEG2, H.264, H.265, and uncompressed video inputs.

DolbyVisionMetadataXml -> (string)

Use this setting only when your video source has Dolby Vision studio mastering metadata that is carried in a separate XML file. Specify the Amazon S3 location for the metadata XML file. MediaConvert uses this file to provide global and frame-level metadata for Dolby Vision preprocessing. When you specify a file here and your input also has interleaved global and frame level metadata, MediaConvert ignores the interleaved metadata and uses only the the metadata from this external XML file. Note that your IAM service role must grant MediaConvert read permissions to this file. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html).

DynamicAudioSelectors -> (map)

Use Dynamic audio selectors when you do not know the track layout of your source when you submit your job, but want to select multiple audio tracks. When you include an audio track in your output and specify this Dynamic audio selector as the Audio source, MediaConvert creates an output audio track for each dynamically selected track. Note that when you include a Dynamic audio selector for two or more inputs, each input must have the same number of audio tracks and audio channels.

key -> (string)

value -> (structure)

Use Dynamic audio selectors when you do not know the track layout of your source when you submit your job, but want to select multiple audio tracks. When you include an audio track in your output and specify this Dynamic audio selector as the Audio source, MediaConvert creates an audio track within that output for each dynamically selected track. Note that when you include a Dynamic audio selector for two or more inputs, each input must have the same number of audio tracks and audio channels.

AudioDurationCorrection -> (string)

Apply audio timing corrections to help synchronize audio and video in your output. To apply timing corrections, your input must meet the following requirements: * Container: MP4, or MOV, with an accurate time-to-sample (STTS) table. * Audio track: AAC. Choose from the following audio timing correction settings: * Disabled (Default): Apply no correction. * Auto: Recommended for most inputs. MediaConvert analyzes the audio timing in your input and determines which correction setting to use, if needed. * Track: Adjust the duration of each audio frame by a constant amount to align the audio track length with STTS duration. Track-level correction does not affect pitch, and is recommended for tonal audio content such as music. * Frame: Adjust the duration of each audio frame by a variable amount to align audio frames with STTS timestamps. No corrections are made to already-aligned frames. Frame-level correction may affect the pitch of corrected frames, and is recommended for atonal audio content such as speech or percussion. * Force: Apply audio duration correction, either Track or Frame depending on your input, regardless of the accuracy of your inputâs STTS table. Your output audio and video may not be aligned or it may contain audio artifacts.

ExternalAudioFileInput -> (string)

Specify the S3, HTTP, or HTTPS URL for your external audio file input.

LanguageCode -> (string)

Specify the language to select from your audio input. In the MediaConvert console choose from a list of languages. In your JSON job settings choose from an ISO 639-2 three-letter code listed at [https://www.loc.gov/standards/iso639-2/php/code_list.php](https://www.loc.gov/standards/iso639-2/php/code_list.php)

Offset -> (integer)

Specify a time delta, in milliseconds, to offset the audio from the input video. To specify no offset: Keep the default value, 0. To specify an offset: Enter an integer from -2147483648 to 2147483647

SelectorType -> (string)

Specify which audio tracks to dynamically select from your source. To select all audio tracks: Keep the default value, All tracks. To select all audio tracks with a specific language code: Choose Language code. When you do, you must also specify a language code under the Language code setting. If there is no matching Language code in your source, then no track will be selected.

FileInput -> (string)

Specify the source file for your transcoding job. You can use multiple inputs in a single job. The service concatenates these inputs, in the order that you specify them in the job, to create the outputs. If your input format is IMF, specify your input by providing the path to your CPL. For example, âs3://bucket/vf/cpl.xmlâ. If the CPL is in an incomplete IMP, make sure to use *Supplemental IMPs* to specify any supplemental IMPs that contain assets referenced by the CPL.

FilterEnable -> (string)

Specify whether to apply input filtering to improve the video quality of your input. To apply filtering depending on your input type and quality: Choose Auto. To apply no filtering: Choose Disable. To apply filtering regardless of your input type and quality: Choose Force. When you do, you must also specify a value for Filter strength.

FilterStrength -> (integer)

Specify the strength of the input filter. To apply an automatic amount of filtering based the compression artifacts measured in your input: We recommend that you leave Filter strength blank and set Filter enable to Auto. To manually apply filtering: Enter a value from 1 to 5, where 1 is the least amount of filtering and 5 is the most. The value that you enter applies to the strength of the Deblock or Denoise filters, or to the strength of the Advanced input filter.

ImageInserter -> (structure)

Enable the image inserter feature to include a graphic overlay on your video. Enable or disable this feature for each input individually. This setting is disabled by default.

InsertableImages -> (list)

Specify the images that you want to overlay on your video. The images must be PNG or TGA files.

(structure)

These settings apply to a specific graphic overlay. You can include multiple overlays in your job.

Duration -> (integer)

Specify the time, in milliseconds, for the image to remain on the output video. This duration includes fade-in time but not fade-out time.

FadeIn -> (integer)

Specify the length of time, in milliseconds, between the Start time that you specify for the image insertion and the time that the image appears at full opacity. Full opacity is the level that you specify for the opacity setting. If you donât specify a value for Fade-in, the image will appear abruptly at the overlay start time.

FadeOut -> (integer)

Specify the length of time, in milliseconds, between the end of the time that you have specified for the image overlay Duration and when the overlaid image has faded to total transparency. If you donât specify a value for Fade-out, the image will disappear abruptly at the end of the inserted image duration.

Height -> (integer)

Specify the height of the inserted image in pixels. If you specify a value thatâs larger than the video resolution height, the service will crop your overlaid image to fit. To use the native height of the image, keep this setting blank.

ImageInserterInput -> (string)

Specify the HTTP, HTTPS, or Amazon S3 location of the image that you want to overlay on the video. Use a PNG or TGA file.

ImageX -> (integer)

Specify the distance, in pixels, between the inserted image and the left edge of the video frame. Required for any image overlay that you specify.

ImageY -> (integer)

Specify the distance, in pixels, between the overlaid image and the top edge of the video frame. Required for any image overlay that you specify.

Layer -> (integer)

Specify how overlapping inserted images appear. Images with higher values for Layer appear on top of images with lower values for Layer.

Opacity -> (integer)

Use Opacity to specify how much of the underlying video shows through the inserted image. 0 is transparent and 100 is fully opaque. Default is 50.

StartTime -> (string)

Specify the timecode of the frame that you want the overlay to first appear on. This must be in timecode (HH:MM:SS:FF or HH:MM:SS;FF) format. Remember to take into account your timecode source settings.

Width -> (integer)

Specify the width of the inserted image in pixels. If you specify a value thatâs larger than the video resolution width, the service will crop your overlaid image to fit. To use the native width of the image, keep this setting blank.

SdrReferenceWhiteLevel -> (integer)

Specify the reference white level, in nits, for all of your image inserter images. Use to correct brightness levels within HDR10 outputs. For 1,000 nit peak brightness displays, we recommend that you set SDR reference white level to 203 (according to ITU-R BT.2408). Leave blank to use the default value of 100, or specify an integer from 100 to 1000.

InputClippings -> (list)

Contains sets of start and end times that together specify a portion of the input to be used in the outputs. If you provide only a start time, the clip will be the entire input from that point to the end. If you provide only an end time, it will be the entire input up to that point. When you specify more than one input clip, the transcoding service creates the job outputs by stringing the clips together in the order you specify them.

(structure)

To transcode only portions of your input, include one input clip for each part of your input that you want in your output. All input clips that you specify will be included in every output of the job. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/assembling-multiple-inputs-and-input-clips.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/assembling-multiple-inputs-and-input-clips.html).

EndTimecode -> (string)

Set End timecode to the end of the portion of the input you are clipping. The frame corresponding to the End timecode value is included in the clip. Start timecode or End timecode may be left blank, but not both. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When choosing this value, take into account your setting for timecode source under input settings. For example, if you have embedded timecodes that start at 01:00:00:00 and you want your clip to end six minutes into the video, use 01:06:00:00.

StartTimecode -> (string)

Set Start timecode to the beginning of the portion of the input you are clipping. The frame corresponding to the Start timecode value is included in the clip. Start timecode or End timecode may be left blank, but not both. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When choosing this value, take into account your setting for Input timecode source. For example, if you have embedded timecodes that start at 01:00:00:00 and you want your clip to begin five minutes into the video, use 01:05:00:00.

InputScanType -> (string)

When you have a progressive segmented frame (PsF) input, use this setting to flag the input as PsF. MediaConvert doesnât automatically detect PsF. Therefore, flagging your input as PsF results in better preservation of video quality when you do deinterlacing and frame rate conversion. If you donât specify, the default value is Auto. Auto is the correct setting for all inputs that are not PsF. Donât set this value to PsF when your input is interlaced. Doing so creates horizontal interlacing artifacts.

Position -> (structure)

Use Selection placement to define the video area in your output frame. The area outside of the rectangle that you specify here is black. If you specify a value here, it will override any value that you specify in the output setting Selection placement. If you specify a value here, this will override any AFD values in your input, even if you set Respond to AFD to Respond. If you specify a value here, this will ignore anything that you specify for the setting Scaling Behavior.

Height -> (integer)

Height of rectangle in pixels. Specify only even numbers.

Width -> (integer)

Width of rectangle in pixels. Specify only even numbers.

X -> (integer)

The distance, in pixels, between the rectangle and the left edge of the video frame. Specify only even numbers.

Y -> (integer)

The distance, in pixels, between the rectangle and the top edge of the video frame. Specify only even numbers.

ProgramNumber -> (integer)

Use Program to select a specific program from within a multi-program transport stream. Note that Quad 4K is not currently supported. Default is the first program within the transport stream. If the program you specify doesnât exist, the transcoding service will use this default.

PsiControl -> (string)

Set PSI control for transport stream inputs to specify which data the demux process to scans. * Ignore PSI - Scan all PIDs for audio and video. * Use PSI - Scan only PSI data.

SupplementalImps -> (list)

Provide a list of any necessary supplemental IMPs. You need supplemental IMPs if the CPL that youâre using for your input is in an incomplete IMP. Specify either the supplemental IMP directories with a trailing slash or the ASSETMAP.xml files. For example [âs3://bucket/ov/â, âs3://bucket/vf2/ASSETMAP.xmlâ]. You donât need to specify the IMP that contains your input CPL, because the service automatically detects it.

(string)

TimecodeSource -> (string)

Use this Timecode source setting, located under the input settings, to specify how the service counts input video frames. This input frame count affects only the behavior of features that apply to a single input at a time, such as input clipping and synchronizing some captions formats. Choose Embedded to use the timecodes in your input video. Choose Start at zero to start the first frame at zero. Choose Specified start to start the first frame at the timecode that you specify in the setting Start timecode. If you donât specify a value for Timecode source, the service will use Embedded by default. For more information about timecodes, see [https://docs.aws.amazon.com/console/mediaconvert/timecode](https://docs.aws.amazon.com/console/mediaconvert/timecode).

TimecodeStart -> (string)

Specify the timecode that you want the service to use for this inputâs initial frame. To use this setting, you must set the Timecode source setting, located under the input settings, to Specified start. For more information about timecodes, see [https://docs.aws.amazon.com/console/mediaconvert/timecode](https://docs.aws.amazon.com/console/mediaconvert/timecode).

VideoGenerator -> (structure)

When you include Video generator, MediaConvert creates a video input with black frames. Use this setting if you do not have a video input or if you want to add black video frames before, or after, other inputs. You can specify Video generator, or you can specify an Input file, but you cannot specify both. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/video-generator.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/video-generator.html)

Channels -> (integer)

Specify the number of audio channels to include in your video generator input. MediaConvert creates these audio channels as silent audio within a single audio track. Enter an integer from 1 to 32.

Duration -> (integer)

Specify the duration, in milliseconds, for your video generator input. Enter an integer from 50 to 86400000.

FramerateDenominator -> (integer)

Specify the denominator of the fraction that represents the frame rate for your video generator input. When you do, you must also specify a value for Frame rate numerator. MediaConvert uses a default frame rate of 29.97 when you leave Frame rate numerator and Frame rate denominator blank.

FramerateNumerator -> (integer)

Specify the numerator of the fraction that represents the frame rate for your video generator input. When you do, you must also specify a value for Frame rate denominator. MediaConvert uses a default frame rate of 29.97 when you leave Frame rate numerator and Frame rate denominator blank.

SampleRate -> (integer)

Specify the audio sample rate, in Hz, for the silent audio in your video generator input. Enter an integer from 32000 to 48000.

VideoOverlays -> (list)

Contains an array of video overlays.

(structure)

Overlay one or more videos on top of your input video. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/video-overlays.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/video-overlays.html)

Crop -> (structure)

Specify a rectangle of content to crop and use from your video overlayâs input video. When you do, MediaConvert uses the cropped dimensions that you specify under X offset, Y offset, Width, and Height.

Height -> (integer)

Specify the height of the video overlay cropping rectangle. To use the same height as your overlay input video: Keep blank, or enter 0. To specify a different height for the cropping rectangle: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 100 and choose Pixels, the cropping rectangle will 100 pixels high. When you enter 10, choose Percentage, and your overlay input video is 1920x1080, the cropping rectangle will be 108 pixels high.

Unit -> (string)

Specify the Unit type to use when you enter a value for X position, Y position, Width, or Height. You can choose Pixels or Percentage. Leave blank to use the default value, Pixels.

Width -> (integer)

Specify the width of the video overlay cropping rectangle. To use the same width as your overlay input video: Keep blank, or enter 0. To specify a different width for the cropping rectangle: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 100 and choose Pixels, the cropping rectangle will 100 pixels wide. When you enter 10, choose Percentage, and your overlay input video is 1920x1080, the cropping rectangle will be 192 pixels wide.

X -> (integer)

Specify the distance between the cropping rectangle and the left edge of your overlay videoâs frame. To position the cropping rectangle along the left edge: Keep blank, or enter 0. To position the cropping rectangle to the right, relative to the left edge of your overlay videoâs frame: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 10 and choose Pixels, the cropping rectangle will be positioned 10 pixels from the left edge of the overlay videoâs frame. When you enter 10, choose Percentage, and your overlay input video is 1920x1080, the cropping rectangle will be positioned 192 pixels from the left edge of the overlay videoâs frame.

Y -> (integer)

Specify the distance between the cropping rectangle and the top edge of your overlay videoâs frame. To position the cropping rectangle along the top edge: Keep blank, or enter 0. To position the cropping rectangle down, relative to the top edge of your overlay videoâs frame: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 10 and choose Pixels, the cropping rectangle will be positioned 10 pixels from the top edge of the overlay videoâs frame. When you enter 10, choose Percentage, and your overlay input video is 1920x1080, the cropping rectangle will be positioned 108 pixels from the top edge of the overlay videoâs frame.

EndTimecode -> (string)

Enter the end timecode in the base input video for this overlay. Your overlay will be active through this frame. To display your video overlay for the duration of the base input video: Leave blank. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS isthe second, and FF is the frame number. When entering this value, take into account your choice for the base input videoâs timecode source. For example, if you have embedded timecodes that start at 01:00:00:00 and you want your overlay to end ten minutes into the video, enter 01:10:00:00.

InitialPosition -> (structure)

Specify the Initial position of your video overlay. To specify the Initial position of your video overlay, including distance from the left or top edge of the base input videoâs frame, or size: Enter a value for X position, Y position, Width, or Height. To use the full frame of the base input video: Leave blank.

Height -> (integer)

To scale your video overlay to the same height as the base input video: Leave blank. To scale the height of your video overlay to a different height: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 360 and choose Pixels, your video overlay will be rendered with a height of 360. When you enter 50, choose Percentage, and your overlayâs source has a height of 1080, your video overlay will be rendered with a height of 540. To scale your overlay to a specific height while automatically maintaining its original aspect ratio, enter a value for Height and leave Width blank.

Unit -> (string)

Specify the Unit type to use when you enter a value for X position, Y position, Width, or Height. You can choose Pixels or Percentage. Leave blank to use the default value, Pixels.

Width -> (integer)

To scale your video overlay to the same width as the base input video: Leave blank. To scale the width of your video overlay to a different width: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 640 and choose Pixels, your video overlay will scale to a height of 640 pixels. When you enter 50, choose Percentage, and your overlayâs source has a width of 1920, your video overlay will scale to a width of 960. To scale your overlay to a specific width while automatically maintaining its original aspect ratio, enter a value for Width and leave Height blank.

XPosition -> (integer)

To position the left edge of your video overlay along the left edge of the base input videoâs frame: Keep blank, or enter 0. To position the left edge of your video overlay to the right, relative to the left edge of the base input videoâs frame: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 10 and choose Pixels, your video overlay will be positioned 10 pixels from the left edge of the base input videoâs frame. When you enter 10, choose Percentage, and your base input video is 1920x1080, your video overlay will be positioned 192 pixels from the left edge of the base input videoâs frame.

YPosition -> (integer)

To position the top edge of your video overlay along the top edge of the base input videoâs frame: Keep blank, or enter 0. To position the top edge of your video overlay down, relative to the top edge of the base input videoâs frame: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 10 and choose Pixels, your video overlay will be positioned 10 pixels from the top edge of the base input videoâs frame. When you enter 10, choose Percentage, and your underlying video is 1920x1080, your video overlay will be positioned 108 pixels from the top edge of the base input videoâs frame.

Input -> (structure)

Input settings for Video overlay. You can include one or more video overlays in sequence at different times that you specify.

FileInput -> (string)

Specify the input file S3, HTTP, or HTTPS URL for your video overlay. To specify one or more Transitions for your base input video instead: Leave blank.

InputClippings -> (list)

Specify one or more clips to use from your video overlay. When you include an input clip, you must also specify its start timecode, end timecode, or both start and end timecode.

(structure)

To transcode only portions of your video overlay, include one input clip for each part of your video overlay that you want in your output.

EndTimecode -> (string)

Specify the timecode of the last frame to include in your video overlayâs clip. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When entering this value, take into account your choice for Timecode source.

StartTimecode -> (string)

Specify the timecode of the first frame to include in your video overlayâs clip. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When entering this value, take into account your choice for Timecode source.

TimecodeSource -> (string)

Specify the timecode source for your video overlay input clips. To use the timecode present in your video overlay: Choose Embedded. To use a zerobased timecode: Choose Start at 0. To choose a timecode: Choose Specified start. When you do, enter the starting timecode in Start timecode. If you donât specify a value for Timecode source, MediaConvert uses Embedded by default.

TimecodeStart -> (string)

Specify the starting timecode for this video overlay. To use this setting, you must set Timecode source to Specified start.

Playback -> (string)

Specify whether your video overlay repeats or plays only once. To repeat your video overlay on a loop: Keep the default value, Repeat. Your overlay will repeat for the duration of the base input video. To playback your video overlay only once: Choose Once. With either option, you can end playback at a time that you specify by entering a value for End timecode.

StartTimecode -> (string)

Enter the start timecode in the base input video for this overlay. Your overlay will be active starting with this frame. To display your video overlay starting at the beginning of the base input video: Leave blank. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When entering this value, take into account your choice for the base input videoâs timecode source. For example, if you have embedded timecodes that start at 01:00:00:00 and you want your overlay to begin five minutes into the video, enter 01:05:00:00.

Transitions -> (list)

Specify one or more transitions for your video overlay. Use Transitions to reposition or resize your overlay over time. To use the same position and size for the duration of your video overlay: Leave blank. To specify a Transition: Enter a value for Start timecode, End Timecode, X Position, Y Position, Width, or Height.

(structure)

Specify one or more Transitions for your video overlay. Use Transitions to reposition or resize your overlay over time. To use the same position and size for the duration of your video overlay: Leave blank. To specify a Transition: Enter a value for Start timecode, End Timecode, X Position, Y Position, Width, or Height.

EndPosition -> (structure)

Specify the ending position for this transition, relative to the base input videoâs frame. Your video overlay will move smoothly to this position, beginning at this transitionâs Start timecode and ending at this transitionâs End timecode.

Height -> (integer)

To scale your video overlay to the same height as the base input video: Leave blank. To scale the height of your video overlay to a different height: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 360 and choose Pixels, your video overlay will be rendered with a height of 360. When you enter 50, choose Percentage, and your overlayâs source has a height of 1080, your video overlay will be rendered with a height of 540. To scale your overlay to a specific height while automatically maintaining its original aspect ratio, enter a value for Height and leave Width blank.

Unit -> (string)

Specify the Unit type to use when you enter a value for X position, Y position, Width, or Height. You can choose Pixels or Percentage. Leave blank to use the default value, Pixels.

Width -> (integer)

To scale your video overlay to the same width as the base input video: Leave blank. To scale the width of your video overlay to a different width: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 640 and choose Pixels, your video overlay will scale to a height of 640 pixels. When you enter 50, choose Percentage, and your overlayâs source has a width of 1920, your video overlay will scale to a width of 960. To scale your overlay to a specific width while automatically maintaining its original aspect ratio, enter a value for Width and leave Height blank.

XPosition -> (integer)

To position the left edge of your video overlay along the left edge of the base input videoâs frame: Keep blank, or enter 0. To position the left edge of your video overlay to the right, relative to the left edge of the base input videoâs frame: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 10 and choose Pixels, your video overlay will be positioned 10 pixels from the left edge of the base input videoâs frame. When you enter 10, choose Percentage, and your base input video is 1920x1080, your video overlay will be positioned 192 pixels from the left edge of the base input videoâs frame.

YPosition -> (integer)

To position the top edge of your video overlay along the top edge of the base input videoâs frame: Keep blank, or enter 0. To position the top edge of your video overlay down, relative to the top edge of the base input videoâs frame: Enter an integer representing the Unit type that you choose, either Pixels or Percentage. For example, when you enter 10 and choose Pixels, your video overlay will be positioned 10 pixels from the top edge of the base input videoâs frame. When you enter 10, choose Percentage, and your underlying video is 1920x1080, your video overlay will be positioned 108 pixels from the top edge of the base input videoâs frame.

EndTimecode -> (string)

Specify the timecode for when this transition ends. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When entering this value, take into account your choice for Timecode source.

StartTimecode -> (string)

Specify the timecode for when this transition begins. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When entering this value, take into account your choice for Timecode source.

VideoSelector -> (structure)

Input video selectors contain the video settings for the input. Each of your inputs can have up to one video selector.

AlphaBehavior -> (string)

Ignore this setting unless this input is a QuickTime animation with an alpha channel. Use this setting to create separate Key and Fill outputs. In each output, specify which part of the input MediaConvert uses. Leave this setting at the default value DISCARD to delete the alpha channel and preserve the video. Set it to REMAP_TO_LUMA to delete the video and map the alpha channel to the luma channel of your outputs.

ColorSpace -> (string)

If your input video has accurate color space metadata, or if you donât know about color space: Keep the default value, Follow. MediaConvert will automatically detect your input color space. If your input video has metadata indicating the wrong color space, or has missing metadata: Specify the accurate color space here. If your input video is HDR 10 and the SMPTE ST 2086 Mastering Display Color Volume static metadata isnât present in your video stream, or if that metadata is present but not accurate: Choose Force HDR 10. Specify correct values in the input HDR 10 metadata settings. For more information about HDR jobs, see [https://docs.aws.amazon.com/console/mediaconvert/hdr](https://docs.aws.amazon.com/console/mediaconvert/hdr). When you specify an input color space, MediaConvert uses the following color space metadata, which includes color primaries, transfer characteristics, and matrix coefficients: * HDR 10: BT.2020, PQ, BT.2020 non-constant * HLG 2020: BT.2020, HLG, BT.2020 non-constant * P3DCI (Theater): DCIP3, SMPTE 428M, BT.709 * P3D65 (SDR): Display P3, sRGB, BT.709 * P3D65 (HDR): Display P3, PQ, BT.709

ColorSpaceUsage -> (string)

There are two sources for color metadata, the input file and the job input settings Color space and HDR master display information settings. The Color space usage setting determines which takes precedence. Choose Force to use color metadata from the input job settings. If you donât specify values for those settings, the service defaults to using metadata from your input. FALLBACK - Choose Fallback to use color metadata from the source when it is present. If thereâs no color metadata in your input file, the service defaults to using values you specify in the input settings.

EmbeddedTimecodeOverride -> (string)

Set Embedded timecode override to Use MDPM when your AVCHD input contains timecode tag data in the Modified Digital Video Pack Metadata. When you do, we recommend you also set Timecode source to Embedded. Leave Embedded timecode override blank, or set to None, when your input does not contain MDPM timecode.

Hdr10Metadata -> (structure)

Use these settings to provide HDR 10 metadata that is missing or inaccurate in your input video. Appropriate values vary depending on the input video and must be provided by a color grader. The color grader generates these values during the HDR 10 mastering process. The valid range for each of these settings is 0 to 50,000. Each increment represents 0.00002 in CIE1931 color coordinate. Related settings - When you specify these values, you must also set Color space to HDR 10. To specify whether the the values you specify here take precedence over the values in the metadata of your input file, set Color space usage. To specify whether color metadata is included in an output, set Color metadata. For more information about MediaConvert HDR jobs, see [https://docs.aws.amazon.com/console/mediaconvert/hdr](https://docs.aws.amazon.com/console/mediaconvert/hdr).

BluePrimaryX -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

BluePrimaryY -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

GreenPrimaryX -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

GreenPrimaryY -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

MaxContentLightLevel -> (integer)

Maximum light level among all samples in the coded video sequence, in units of candelas per square meter. This setting doesnât have a default value; you must specify a value that is suitable for the content.

MaxFrameAverageLightLevel -> (integer)

Maximum average light level of any frame in the coded video sequence, in units of candelas per square meter. This setting doesnât have a default value; you must specify a value that is suitable for the content.

MaxLuminance -> (integer)

Nominal maximum mastering display luminance in units of of 0.0001 candelas per square meter.

MinLuminance -> (integer)

Nominal minimum mastering display luminance in units of of 0.0001 candelas per square meter

RedPrimaryX -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

RedPrimaryY -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

WhitePointX -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

WhitePointY -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

MaxLuminance -> (integer)

Specify the maximum mastering display luminance. Enter an integer from 0 to 2147483647, in units of 0.0001 nits. For example, enter 10000000 for 1000 nits.

PadVideo -> (string)

Use this setting if your input has video and audio durations that donât align, and your output or player has strict alignment requirements. Examples: Input audio track has a delayed start. Input video track ends before audio ends. When you set Pad video to Black, MediaConvert generates black video frames so that output video and audio durations match. Black video frames are added at the beginning or end, depending on your input. To keep the default behavior and not generate black video, set Pad video to Disabled or leave blank.

Pid -> (integer)

Use PID to select specific video data from an input file. Specify this value as an integer; the system automatically converts it to the hexidecimal value. For example, 257 selects PID 0x101. A PID, or packet identifier, is an identifier for a set of data in an MPEG-2 transport stream container.

ProgramNumber -> (integer)

Selects a specific program from within a multi-program transport stream. Note that Quad 4K is not currently supported.

Rotate -> (string)

Use Rotate to specify how the service rotates your video. You can choose automatic rotation or specify a rotation. You can specify a clockwise rotation of 0, 90, 180, or 270 degrees. If your input video container is .mov or .mp4 and your input has rotation metadata, you can choose Automatic to have the service rotate your video according to the rotation specified in the metadata. The rotation must be within one degree of 90, 180, or 270 degrees. If the rotation metadata specifies any other rotation, the service will default to no rotation. By default, the service does no rotation, even if your input video has rotation metadata. The service doesnât pass through rotation metadata.

SampleRange -> (string)

If the sample range metadata in your input video is accurate, or if you donât know about sample range, keep the default value, Follow, for this setting. When you do, the service automatically detects your input sample range. If your input video has metadata indicating the wrong sample range, specify the accurate sample range here. When you do, MediaConvert ignores any sample range information in the input metadata. Regardless of whether MediaConvert uses the input sample range or the sample range that you specify, MediaConvert uses the sample range for transcoding and also writes it to the output metadata.

KantarWatermark -> (structure)

Use these settings only when you use Kantar watermarking. Specify the values that MediaConvert uses to generate and place Kantar watermarks in your output audio. These settings apply to every output in your job. In addition to specifying these values, you also need to store your Kantar credentials in AWS Secrets Manager. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/kantar-watermarking.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/kantar-watermarking.html).

ChannelName -> (string)

Provide an audio channel name from your Kantar audio license.

ContentReference -> (string)

Specify a unique identifier for Kantar to use for this piece of content.

CredentialsSecretName -> (string)

Provide the name of the AWS Secrets Manager secret where your Kantar credentials are stored. Note that your MediaConvert service role must provide access to this secret. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/granting-permissions-for-mediaconvert-to-access-secrets-manager-secret.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/granting-permissions-for-mediaconvert-to-access-secrets-manager-secret.html). For instructions on creating a secret, see [https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html), in the AWS Secrets Manager User Guide.

FileOffset -> (double)

Optional. Specify an offset, in whole seconds, from the start of your output and the beginning of the watermarking. When you donât specify an offset, Kantar defaults to zero.

KantarLicenseId -> (integer)

Provide your Kantar license ID number. You should get this number from Kantar.

KantarServerUrl -> (string)

Provide the HTTPS endpoint to the Kantar server. You should get this endpoint from Kantar.

LogDestination -> (string)

Optional. Specify the Amazon S3 bucket where you want MediaConvert to store your Kantar watermark XML logs. When you donât specify a bucket, MediaConvert doesnât save these logs. Note that your MediaConvert service role must provide access to this location. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html)

Metadata3 -> (string)

You can optionally use this field to specify the first timestamp that Kantar embeds during watermarking. Kantar suggests that you be very cautious when using this Kantar feature, and that you use it only on channels that are managed specifically for use with this feature by your Audience Measurement Operator. For more information about this feature, contact Kantar technical support.

Metadata4 -> (string)

Additional metadata that MediaConvert sends to Kantar. Maximum length is 50 characters.

Metadata5 -> (string)

Additional metadata that MediaConvert sends to Kantar. Maximum length is 50 characters.

Metadata6 -> (string)

Additional metadata that MediaConvert sends to Kantar. Maximum length is 50 characters.

Metadata7 -> (string)

Additional metadata that MediaConvert sends to Kantar. Maximum length is 50 characters.

Metadata8 -> (string)

Additional metadata that MediaConvert sends to Kantar. Maximum length is 50 characters.

MotionImageInserter -> (structure)

Overlay motion graphics on top of your video. The motion graphics that you specify here appear on all outputs in all output groups. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/motion-graphic-overlay.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/motion-graphic-overlay.html).

Framerate -> (structure)

If your motion graphic asset is a .mov file, keep this setting unspecified. If your motion graphic asset is a series of .png files, specify the frame rate of the overlay in frames per second, as a fraction. For example, specify 24 fps as 24/1. Make sure that the number of images in your series matches the frame rate and your intended overlay duration. For example, if you want a 30-second overlay at 30 fps, you should have 900 .png images. This overlay frame rate doesnât need to match the frame rate of the underlying video.

FramerateDenominator -> (integer)

The bottom of the fraction that expresses your overlay frame rate. For example, if your frame rate is 24 fps, set this value to 1.

FramerateNumerator -> (integer)

The top of the fraction that expresses your overlay frame rate. For example, if your frame rate is 24 fps, set this value to 24.

Input -> (string)

Specify the .mov file or series of .png files that you want to overlay on your video. For .png files, provide the file name of the first file in the series. Make sure that the names of the .png files end with sequential numbers that specify the order that they are played in. For example, overlay_000.png, overlay_001.png, overlay_002.png, and so on. The sequence must start at zero, and each image file name must have the same number of digits. Pad your initial file names with enough zeros to complete the sequence. For example, if the first image is overlay_0.png, there can be only 10 images in the sequence, with the last image being overlay_9.png. But if the first image is overlay_00.png, there can be 100 images in the sequence.

InsertionMode -> (string)

Choose the type of motion graphic asset that you are providing for your overlay. You can choose either a .mov file or a series of .png files.

Offset -> (structure)

Use Offset to specify the placement of your motion graphic overlay on the video frame. Specify in pixels, from the upper-left corner of the frame. If you donât specify an offset, the service scales your overlay to the full size of the frame. Otherwise, the service inserts the overlay at its native resolution and scales the size up or down with any video scaling.

ImageX -> (integer)

Set the distance, in pixels, between the overlay and the left edge of the video frame.

ImageY -> (integer)

Set the distance, in pixels, between the overlay and the top edge of the video frame.

Playback -> (string)

Specify whether your motion graphic overlay repeats on a loop or plays only once.

StartTime -> (string)

Specify when the motion overlay begins. Use timecode format (HH:MM:SS:FF or HH:MM:SS;FF). Make sure that the timecode you provide here takes into account how you have set up your timecode configuration under both job settings and input settings. The simplest way to do that is to set both to start at 0. If you need to set up your job to follow timecodes embedded in your source that donât start at zero, make sure that you specify a start time that is after the first embedded timecode. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up-timecode.html

NielsenConfiguration -> (structure)

Settings for your Nielsen configuration. If you donât do Nielsen measurement and analytics, ignore these settings. When you enable Nielsen configuration, MediaConvert enables PCM to ID3 tagging for all outputs in the job.

BreakoutCode -> (integer)

Nielsen has discontinued the use of breakout code functionality. If you must include this property, set the value to zero.

DistributorId -> (string)

Use Distributor ID to specify the distributor ID that is assigned to your organization by Nielsen.

NielsenNonLinearWatermark -> (structure)

Ignore these settings unless you are using Nielsen non-linear watermarking. Specify the values that MediaConvert uses to generate and place Nielsen watermarks in your output audio. In addition to specifying these values, you also need to set up your cloud TIC server. These settings apply to every output in your job. The MediaConvert implementation is currently with the following Nielsen versions: Nielsen Watermark SDK Version 6.0.13 Nielsen NLM Watermark Engine Version 1.3.3 Nielsen Watermark Authenticator [SID_TIC] Version [7.0.0]

ActiveWatermarkProcess -> (string)

Choose the type of Nielsen watermarks that you want in your outputs. When you choose NAES 2 and NW, you must provide a value for the setting SID. When you choose CBET, you must provide a value for the setting CSID. When you choose NAES 2, NW, and CBET, you must provide values for both of these settings.

AdiFilename -> (string)

Optional. Use this setting when you want the service to include an ADI file in the Nielsen metadata .zip file. To provide an ADI file, store it in Amazon S3 and provide a URL to it here. The URL should be in the following format: S3://bucket/path/ADI-file. For more information about the metadata .zip file, see the setting Metadata destination.

AssetId -> (string)

Use the asset ID that you provide to Nielsen to uniquely identify this asset. Required for all Nielsen non-linear watermarking.

AssetName -> (string)

Use the asset name that you provide to Nielsen for this asset. Required for all Nielsen non-linear watermarking.

CbetSourceId -> (string)

Use the CSID that Nielsen provides to you. This CBET source ID should be unique to your Nielsen account but common to all of your output assets that have CBET watermarking. Required when you choose a value for the setting Watermark types that includes CBET.

EpisodeId -> (string)

Optional. If this asset uses an episode ID with Nielsen, provide it here.

MetadataDestination -> (string)

Specify the Amazon S3 location where you want MediaConvert to save your Nielsen non-linear metadata .zip file. This Amazon S3 bucket must be in the same Region as the one where you do your MediaConvert transcoding. If you want to include an ADI file in this .zip file, use the setting ADI file to specify it. MediaConvert delivers the Nielsen metadata .zip files only to your metadata destination Amazon S3 bucket. It doesnât deliver the .zip files to Nielsen. You are responsible for delivering the metadata .zip files to Nielsen.

SourceId -> (integer)

Use the SID that Nielsen provides to you. This source ID should be unique to your Nielsen account but common to all of your output assets. Required for all Nielsen non-linear watermarking. This ID should be unique to your Nielsen account but common to all of your output assets. Required for all Nielsen non-linear watermarking.

SourceWatermarkStatus -> (string)

Required. Specify whether your source content already contains Nielsen non-linear watermarks. When you set this value to Watermarked, the service fails the job. Nielsen requires that you add non-linear watermarking to only clean content that doesnât already have non-linear Nielsen watermarks.

TicServerUrl -> (string)

Specify the endpoint for the TIC server that you have deployed and configured in the AWS Cloud. Required for all Nielsen non-linear watermarking. MediaConvert canât connect directly to a TIC server. Instead, you must use API Gateway to provide a RESTful interface between MediaConvert and a TIC server that you deploy in your AWS account. For more information on deploying a TIC server in your AWS account and the required API Gateway, contact Nielsen support.

UniqueTicPerAudioTrack -> (string)

To create assets that have the same TIC values in each audio track, keep the default value Share TICs. To create assets that have unique TIC values for each audio track, choose Use unique TICs.

OutputGroups -> (list)

Contains one group of settings for each set of outputs that share a common package type. All unpackaged files (MPEG-4, MPEG-2 TS, Quicktime, MXF, and no container) are grouped in a single output group as well. Required in is a group of settings that apply to the whole group. This required object depends on the value you set for Type. Type, settings object pairs are as follows. * FILE_GROUP_SETTINGS, FileGroupSettings * HLS_GROUP_SETTINGS, HlsGroupSettings * DASH_ISO_GROUP_SETTINGS, DashIsoGroupSettings * MS_SMOOTH_GROUP_SETTINGS, MsSmoothGroupSettings * CMAF_GROUP_SETTINGS, CmafGroupSettings

(structure)

Group of outputs

AutomatedEncodingSettings -> (structure)

Use automated encoding to have MediaConvert choose your encoding settings for you, based on characteristics of your input video.

AbrSettings -> (structure)

Use automated ABR to have MediaConvert set up the renditions in your ABR package for you automatically, based on characteristics of your input video. This feature optimizes video quality while minimizing the overall size of your ABR package.

MaxAbrBitrate -> (integer)

Specify the maximum average bitrate for MediaConvert to use in your automated ABR stack. If you donât specify a value, MediaConvert uses 8,000,000 (8 mb/s) by default. The average bitrate of your highest-quality rendition will be equal to or below this value, depending on the quality, complexity, and resolution of your content. Note that the instantaneous maximum bitrate may vary above the value that you specify.

MaxQualityLevel -> (double)

Optional. Specify the QVBR quality level to use for all renditions in your automated ABR stack. To have MediaConvert automatically determine the quality level: Leave blank. To manually specify a quality level: Enter a value from 1 to 10. MediaConvert will use a quality level up to the value that you specify, depending on your source. For more information about QVBR quality levels, see: [https://docs.aws.amazon.com/mediaconvert/latest/ug/qvbr-guidelines.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/qvbr-guidelines.html)

MaxRenditions -> (integer)

Optional. The maximum number of renditions that MediaConvert will create in your automated ABR stack. The number of renditions is determined automatically, based on analysis of each job, but will never exceed this limit. When you set this to Auto in the console, which is equivalent to excluding it from your JSON job specification, MediaConvert defaults to a limit of 15.

MinAbrBitrate -> (integer)

Specify the minimum average bitrate for MediaConvert to use in your automated ABR stack. If you donât specify a value, MediaConvert uses 600,000 (600 kb/s) by default. The average bitrate of your lowest-quality rendition will be near this value. Note that the instantaneous minimum bitrate may vary below the value that you specify.

Rules -> (list)

Optional. Use Automated ABR rules to specify restrictions for the rendition sizes MediaConvert will create in your ABR stack. You can use these rules if your ABR workflow has specific rendition size requirements, but you still want MediaConvert to optimize for video quality and overall file size.

(structure)

Specify one or more Automated ABR rule types. Note: Force include and Allowed renditions are mutually exclusive.

AllowedRenditions -> (list)

When customer adds the allowed renditions rule for auto ABR ladder, they are required to add at leat one rendition to allowedRenditions list

(structure)

Use Allowed renditions to specify a list of possible resolutions in your ABR stack. * MediaConvert will create an ABR stack exclusively from the list of resolutions that you specify. * Some resolutions in the Allowed renditions list may not be included, however you can force a resolution to be included by setting Required to ENABLED. * You must specify at least one resolution that is greater than or equal to any resolutions that you specify in Min top rendition size or Min bottom rendition size. * If you specify Allowed renditions, you must not specify a separate rule for Force include renditions.

Height -> (integer)

Use Height to define the video resolution height, in pixels, for this rule.

Required -> (string)

Set to ENABLED to force a rendition to be included.

Width -> (integer)

Use Width to define the video resolution width, in pixels, for this rule.

ForceIncludeRenditions -> (list)

When customer adds the force include renditions rule for auto ABR ladder, they are required to add at leat one rendition to forceIncludeRenditions list

(structure)

Use Force include renditions to specify one or more resolutions to include your ABR stack. * (Recommended) To optimize automated ABR, specify as few resolutions as possible. * (Required) The number of resolutions that you specify must be equal to, or less than, the Max renditions setting. * If you specify a Min top rendition size rule, specify at least one resolution that is equal to, or greater than, Min top rendition size. * If you specify a Min bottom rendition size rule, only specify resolutions that are equal to, or greater than, Min bottom rendition size. * If you specify a Force include renditions rule, do not specify a separate rule for Allowed renditions. * Note: The ABR stack may include other resolutions that you do not specify here, depending on the Max renditions setting.

Height -> (integer)

Use Height to define the video resolution height, in pixels, for this rule.

Width -> (integer)

Use Width to define the video resolution width, in pixels, for this rule.

MinBottomRenditionSize -> (structure)

Use Min bottom rendition size to specify a minimum size for the lowest resolution in your ABR stack. * The lowest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 640x360 the lowest resolution in your ABR stack will be equal to or greater than to 640x360. * If you specify a Min top rendition size rule, the value that you specify for Min bottom rendition size must be less than, or equal to, Min top rendition size.

Height -> (integer)

Use Height to define the video resolution height, in pixels, for this rule.

Width -> (integer)

Use Width to define the video resolution width, in pixels, for this rule.

MinTopRenditionSize -> (structure)

Use Min top rendition size to specify a minimum size for the highest resolution in your ABR stack. * The highest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 1280x720 the highest resolution in your ABR stack will be equal to or greater than 1280x720. * If you specify a value for Max resolution, the value that you specify for Min top rendition size must be less than, or equal to, Max resolution.

Height -> (integer)

Use Height to define the video resolution height, in pixels, for this rule.

Width -> (integer)

Use Width to define the video resolution width, in pixels, for this rule.

Type -> (string)

Use Min top rendition size to specify a minimum size for the highest resolution in your ABR stack. * The highest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 1280x720 the highest resolution in your ABR stack will be equal to or greater than 1280x720. * If you specify a value for Max resolution, the value that you specify for Min top rendition size must be less than, or equal to, Max resolution. Use Min bottom rendition size to specify a minimum size for the lowest resolution in your ABR stack. * The lowest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 640x360 the lowest resolution in your ABR stack will be equal to or greater than to 640x360. * If you specify a Min top rendition size rule, the value that you specify for Min bottom rendition size must be less than, or equal to, Min top rendition size. Use Force include renditions to specify one or more resolutions to include your ABR stack. * (Recommended) To optimize automated ABR, specify as few resolutions as possible. * (Required) The number of resolutions that you specify must be equal to, or less than, the Max renditions setting. * If you specify a Min top rendition size rule, specify at least one resolution that is equal to, or greater than, Min top rendition size. * If you specify a Min bottom rendition size rule, only specify resolutions that are equal to, or greater than, Min bottom rendition size. * If you specify a Force include renditions rule, do not specify a separate rule for Allowed renditions. * Note: The ABR stack may include other resolutions that you do not specify here, depending on the Max renditions setting. Use Allowed renditions to specify a list of possible resolutions in your ABR stack. * (Required) The number of resolutions that you specify must be equal to, or greater than, the Max renditions setting. * MediaConvert will create an ABR stack exclusively from the list of resolutions that you specify. * Some resolutions in the Allowed renditions list may not be included, however you can force a resolution to be included by setting Required to ENABLED. * You must specify at least one resolution that is greater than or equal to any resolutions that you specify in Min top rendition size or Min bottom rendition size. * If you specify Allowed renditions, you must not specify a separate rule for Force include renditions.

CustomName -> (string)

Use Custom Group Name to specify a name for the output group. This value is displayed on the console and can make your job settings JSON more human-readable. It does not affect your outputs. Use up to twelve characters that are either letters, numbers, spaces, or underscores.

Name -> (string)

Name of the output group

OutputGroupSettings -> (structure)

Output Group settings, including type

CmafGroupSettings -> (structure)

Settings related to your CMAF output package. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html).

AdditionalManifests -> (list)

By default, the service creates one top-level .m3u8 HLS manifest and one top -level .mpd DASH manifest for each CMAF output group in your job. These default manifests reference every output in the output group. To create additional top-level manifests that reference a subset of the outputs in the output group, specify a list of them here. For each additional manifest that you specify, the service creates one HLS manifest and one DASH manifest.

(structure)

Specify the details for each pair of HLS and DASH additional manifests that you want the service to generate for this CMAF output group. Each pair of manifests can reference a different subset of outputs in the group.

ManifestNameModifier -> (string)

Specify a name modifier that the service adds to the name of this manifest to make it different from the file names of the other main manifests in the output group. For example, say that the default main manifest for your HLS group is film-name.m3u8. If you enter â-no-premiumâ for this setting, then the file name the service generates for this top-level manifest is film-name-no-premium.m3u8. For HLS output groups, specify a manifestNameModifier that is different from the nameModifier of the output. The service uses the output name modifier to create unique names for the individual variant manifests.

SelectedOutputs -> (list)

Specify the outputs that you want this additional top-level manifest to reference.

(string)

BaseUrl -> (string)

A partial URI prefix that will be put in the manifest file at the top level BaseURL element. Can be used if streams are delivered from a different URL than the manifest file.

ClientCache -> (string)

Disable this setting only when your workflow requires the #EXT-X-ALLOW-CACHE:no tag. Otherwise, keep the default value Enabled and control caching in your video distribution set up. For example, use the Cache-Control http header.

CodecSpecification -> (string)

Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation.

DashIFrameTrickPlayNameModifier -> (string)

Specify whether MediaConvert generates I-frame only video segments for DASH trick play, also known as trick mode. When specified, the I-frame only video segments are included within an additional AdaptationSet in your DASH output manifest. To generate I-frame only video segments: Enter a name as a text string, up to 256 character long. This name is appended to the end of this output groupâs base filename, that you specify as part of your destination URI, and used for the I-frame only video segment files. You may also include format identifiers. For more information, see: [https://docs.aws.amazon.com/mediaconvert/latest/ug/using-variables-in-your-job-settings.html#using-settings-variables-with-streaming-outputs](https://docs.aws.amazon.com/mediaconvert/latest/ug/using-variables-in-your-job-settings.html#using-settings-variables-with-streaming-outputs) To not generate I-frame only video segments: Leave blank.

DashManifestStyle -> (string)

Specify how MediaConvert writes SegmentTimeline in your output DASH manifest. To write a SegmentTimeline in each video Representation: Keep the default value, Basic. To write a common SegmentTimeline in the video AdaptationSet: Choose Compact. Note that MediaConvert will still write a SegmentTimeline in any Representation that does not share a common timeline. To write a video AdaptationSet for each different output framerate, and a common SegmentTimeline in each AdaptationSet: Choose Distinct.

Destination -> (string)

Use Destination to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file.

DestinationSettings -> (structure)

Settings associated with the destination. Will vary based on the type of destination

S3Settings -> (structure)

Settings associated with S3 destination

AccessControl -> (structure)

Optional. Have MediaConvert automatically apply Amazon S3 access control for the outputs in this output group. When you donât use this setting, S3 automatically applies the default access control list PRIVATE.

CannedAcl -> (string)

Choose an Amazon S3 canned ACL for MediaConvert to apply to this output.

Encryption -> (structure)

Settings for how your job outputs are encrypted as they are uploaded to Amazon S3.

EncryptionType -> (string)

Specify how you want your data keys managed. AWS uses data keys to encrypt your content. AWS also encrypts the data keys themselves, using a customer master key (CMK), and then stores the encrypted data keys alongside your encrypted content. Use this setting to specify which AWS service manages the CMK. For simplest set up, choose Amazon S3. If you want your master key to be managed by AWS Key Management Service (KMS), choose AWS KMS. By default, when you choose AWS KMS, KMS uses the AWS managed customer master key (CMK) associated with Amazon S3 to encrypt your data keys. You can optionally choose to specify a different, customer managed CMK. Do so by specifying the Amazon Resource Name (ARN) of the key for the setting KMS ARN.

KmsEncryptionContext -> (string)

Optionally, specify the encryption context that you want to use alongside your KMS key. AWS KMS uses this encryption context as additional authenticated data (AAD) to support authenticated encryption. This value must be a base64-encoded UTF-8 string holding JSON which represents a string-string map. To use this setting, you must also set Server-side encryption to AWS KMS. For more information about encryption context, see: [https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context).

KmsKeyArn -> (string)

Optionally, specify the customer master key (CMK) that you want to use to encrypt the data key that AWS uses to encrypt your output content. Enter the Amazon Resource Name (ARN) of the CMK. To use this setting, you must also set Server-side encryption to AWS KMS. If you set Server-side encryption to AWS KMS but donât specify a CMK here, AWS uses the AWS managed CMK associated with Amazon S3.

StorageClass -> (string)

Specify the S3 storage class to use for this output. To use your destinationâs default storage class: Keep the default value, Not set. For more information about S3 storage classes, see [https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

Encryption -> (structure)

DRM settings.

ConstantInitializationVector -> (string)

This is a 128-bit, 16-byte hex value represented by a 32-character text string. If this parameter is not set then the Initialization Vector will follow the segment number by default.

EncryptionMethod -> (string)

Specify the encryption scheme that you want the service to use when encrypting your CMAF segments. Choose AES-CBC subsample or AES_CTR.

InitializationVectorInManifest -> (string)

When you use DRM with CMAF outputs, choose whether the service writes the 128-bit encryption initialization vector in the HLS and DASH manifests.

SpekeKeyProvider -> (structure)

If your output group type is CMAF, use these settings when doing DRM encryption with a SPEKE-compliant key provider. If your output group type is HLS, DASH, or Microsoft Smooth, use the SpekeKeyProvider settings instead.

CertificateArn -> (string)

If you want your key provider to encrypt the content keys that it provides to MediaConvert, set up a certificate with a master key using AWS Certificate Manager. Specify the certificateâs Amazon Resource Name (ARN) here.

DashSignaledSystemIds -> (list)

Specify the DRM system IDs that you want signaled in the DASH manifest that MediaConvert creates as part of this CMAF package. The DASH manifest can currently signal up to three system IDs. For more information, see [https://dashif.org/identifiers/content_protection/](https://dashif.org/identifiers/content_protection/).

(string)

EncryptionContractConfiguration -> (structure)

Specify the SPEKE version, either v1.0 or v2.0, that MediaConvert uses when encrypting your output. For more information, see: [https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html](https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html) To use SPEKE v1.0: Leave blank. To use SPEKE v2.0: Specify a SPEKE v2.0 video preset and a SPEKE v2.0 audio preset.

SpekeAudioPreset -> (string)

Specify which SPEKE version 2.0 audio preset MediaConvert uses to request content keys from your SPEKE server. For more information, see: [https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html) To encrypt to your audio outputs, choose from the following: Audio preset 1, Audio preset 2, or Audio preset 3. To encrypt your audio outputs, using the same content key for both your audio and video outputs: Choose Shared. When you do, you must also set SPEKE v2.0 video preset to Shared. To not encrypt your audio outputs: Choose Unencrypted. When you do, to encrypt your video outputs, you must also specify a SPEKE v2.0 video preset (other than Shared or Unencrypted).

SpekeVideoPreset -> (string)

Specify which SPEKE version 2.0 video preset MediaConvert uses to request content keys from your SPEKE server. For more information, see: [https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html) To encrypt to your video outputs, choose from the following: Video preset 1, Video preset 2, Video preset 3, Video preset 4, Video preset 5, Video preset 6, Video preset 7, or Video preset 8. To encrypt your video outputs, using the same content key for both your video and audio outputs: Choose Shared. When you do, you must also set SPEKE v2.0 audio preset to Shared. To not encrypt your video outputs: Choose Unencrypted. When you do, to encrypt your audio outputs, you must also specify a SPEKE v2.0 audio preset (other than Shared or Unencrypted).

HlsSignaledSystemIds -> (list)

Specify up to 3 DRM system IDs that you want signaled in the HLS manifest that MediaConvert creates as part of this CMAF package. For more information, see [https://dashif.org/identifiers/content_protection/](https://dashif.org/identifiers/content_protection/).

(string)

ResourceId -> (string)

Specify the resource ID that your SPEKE-compliant key provider uses to identify this content.

Url -> (string)

Specify the URL to the key server that your SPEKE-compliant DRM key provider uses to provide keys for encrypting your content.

StaticKeyProvider -> (structure)

Use these settings to set up encryption with a static key provider.

KeyFormat -> (string)

Relates to DRM implementation. Sets the value of the KEYFORMAT attribute. Must be âidentityâ or a reverse DNS string. May be omitted to indicate an implicit value of âidentityâ.

KeyFormatVersions -> (string)

Relates to DRM implementation. Either a single positive integer version value or a slash delimited list of version values (1/2/3).

StaticKeyValue -> (string)

Relates to DRM implementation. Use a 32-character hexidecimal string to specify Key Value.

Url -> (string)

Relates to DRM implementation. The location of the license server used for protecting content.

Type -> (string)

Specify whether your DRM encryption key is static or from a key provider that follows the SPEKE standard. For more information about SPEKE, see [https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html](https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html).

FragmentLength -> (integer)

Specify the length, in whole seconds, of the mp4 fragments. When you donât specify a value, MediaConvert defaults to 2. Related setting: Use Fragment length control to specify whether the encoder enforces this value strictly.

ImageBasedTrickPlay -> (string)

Specify whether MediaConvert generates images for trick play. Keep the default value, None, to not generate any images. Choose Thumbnail to generate tiled thumbnails. Choose Thumbnail and full frame to generate tiled thumbnails and full-resolution images of single frames. When you enable Write HLS manifest, MediaConvert creates a child manifest for each set of images that you generate and adds corresponding entries to the parent manifest. When you enable Write DASH manifest, MediaConvert adds an entry in the .mpd manifest for each set of images that you generate. A common application for these images is Roku trick mode. The thumbnails and full-frame images that MediaConvert creates with this feature are compatible with this Roku specification: [https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md](https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md)

ImageBasedTrickPlaySettings -> (structure)

Tile and thumbnail settings applicable when imageBasedTrickPlay is ADVANCED

IntervalCadence -> (string)

The cadence MediaConvert follows for generating thumbnails. If set to FOLLOW_IFRAME, MediaConvert generates thumbnails for each IDR frame in the output (matching the GOP cadence). If set to FOLLOW_CUSTOM, MediaConvert generates thumbnails according to the interval you specify in thumbnailInterval.

ThumbnailHeight -> (integer)

Height of each thumbnail within each tile image, in pixels. Leave blank to maintain aspect ratio with thumbnail width. If following the aspect ratio would lead to a total tile height greater than 4096, then the job will be rejected. Must be divisible by 2.

ThumbnailInterval -> (double)

Enter the interval, in seconds, that MediaConvert uses to generate thumbnails. If the interval you enter doesnât align with the output frame rate, MediaConvert automatically rounds the interval to align with the output frame rate. For example, if the output frame rate is 29.97 frames per second and you enter 5, MediaConvert uses a 150 frame interval to generate thumbnails.

ThumbnailWidth -> (integer)

Width of each thumbnail within each tile image, in pixels. Default is 312. Must be divisible by 8.

TileHeight -> (integer)

Number of thumbnails in each column of a tile image. Set a value between 2 and 2048. Must be divisible by 2.

TileWidth -> (integer)

Number of thumbnails in each row of a tile image. Set a value between 1 and 512.

ManifestCompression -> (string)

When set to GZIP, compresses HLS playlist.

ManifestDurationFormat -> (string)

Indicates whether the output manifest should use floating point values for segment duration.

MinBufferTime -> (integer)

Minimum time of initially buffered media that is needed to ensure smooth playout.

MinFinalSegmentLength -> (double)

Keep this setting at the default value of 0, unless you are troubleshooting a problem with how devices play back the end of your video asset. If you know that player devices are hanging on the final segment of your video because the length of your final segment is too short, use this setting to specify a minimum final segment length, in seconds. Choose a value that is greater than or equal to 1 and less than your segment length. When you specify a value for this setting, the encoder will combine any final segment that is shorter than the length that you specify with the previous segment. For example, your segment length is 3 seconds and your final segment is .5 seconds without a minimum final segment length; when you set the minimum final segment length to 1, your final segment is 3.5 seconds.

MpdManifestBandwidthType -> (string)

Specify how the value for bandwidth is determined for each video Representation in your output MPD manifest. We recommend that you choose a MPD manifest bandwidth type that is compatible with your downstream player configuration. Max: Use the same value that you specify for Max bitrate in the video output, in bits per second. Average: Use the calculated average bitrate of the encoded video output, in bits per second.

MpdProfile -> (string)

Specify whether your DASH profile is on-demand or main. When you choose Main profile, the service signals [urn:mpeg:dash:profile:isoff-main:2011](urn:mpeg:dash:profile:isoff-main:2011) in your .mpd DASH manifest. When you choose On-demand, the service signals [urn:mpeg:dash:profile:isoff-on-demand:2011](urn:mpeg:dash:profile:isoff-on-demand:2011) in your .mpd. When you choose On-demand, you must also set the output group setting Segment control to Single file.

PtsOffsetHandlingForBFrames -> (string)

Use this setting only when your output video stream has B-frames, which causes the initial presentation time stamp (PTS) to be offset from the initial decode time stamp (DTS). Specify how MediaConvert handles PTS when writing time stamps in output DASH manifests. Choose Match initial PTS when you want MediaConvert to use the initial PTS as the first time stamp in the manifest. Choose Zero-based to have MediaConvert ignore the initial PTS in the video stream and instead write the initial time stamp as zero in the manifest. For outputs that donât have B-frames, the time stamps in your DASH manifests start at zero regardless of your choice here.

SegmentControl -> (string)

When set to SINGLE_FILE, a single output file is generated, which is internally segmented using the Fragment Length and Segment Length. When set to SEGMENTED_FILES, separate segment files will be created.

SegmentLength -> (integer)

Specify the length, in whole seconds, of each segment. When you donât specify a value, MediaConvert defaults to 10. Related settings: Use Segment length control to specify whether the encoder enforces this value strictly. Use Segment control to specify whether MediaConvert creates separate segment files or one content file that has metadata to mark the segment boundaries.

SegmentLengthControl -> (string)

Specify how you want MediaConvert to determine segment lengths in this output group. To use the exact value that you specify under Segment length: Choose Exact. Note that this might result in additional I-frames in the output GOP. To create segment lengths that are a multiple of the GOP: Choose Multiple of GOP. MediaConvert will round up the segment lengths to match the next GOP boundary. To have MediaConvert automatically determine a segment duration that is a multiple of both the audio packets and the frame rates: Choose Match. When you do, also specify a target segment duration under Segment length. This is useful for some ad-insertion or segment replacement workflows. Note that Match has the following requirements: - Output containers: Include at least one video output and at least one audio output. Audio-only outputs are not supported. - Output frame rate: Follow source is not supported. - Multiple output frame rates: When you specify multiple outputs, we recommend they share a similar frame rate (as in X/3, X/2, X, or 2X). For example: 5, 15, 30 and 60. Or: 25 and 50. (Outputs must share an integer multiple.) - Output audio codec: Specify Advanced Audio Coding (AAC). - Output sample rate: Choose 48kHz.

StreamInfResolution -> (string)

Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest.

TargetDurationCompatibilityMode -> (string)

When set to LEGACY, the segment target duration is always rounded up to the nearest integer value above its current value in seconds. When set to SPEC\_COMPLIANT, the segment target duration is rounded up to the nearest integer value if fraction seconds are greater than or equal to 0.5 (>= 0.5) and rounded down if less than 0.5 (<0.5). You may need to use LEGACY if your client needs to ensure that the target duration is always longer than the actual duration of the segment. Some older players may experience interrupted playback when the actual duration of a track in a segment is longer than the target duration.

VideoCompositionOffsets -> (string)

Specify the video sample composition time offset mode in the output fMP4 TRUN box. For wider player compatibility, set Video composition offsets to Unsigned or leave blank. The earliest presentation time may be greater than zero, and sample composition time offsets will increment using unsigned integers. For strict fMP4 video and audio timing, set Video composition offsets to Signed. The earliest presentation time will be equal to zero, and sample composition time offsets will increment using signed integers.

WriteDashManifest -> (string)

When set to ENABLED, a DASH MPD manifest will be generated for this output.

WriteHlsManifest -> (string)

When set to ENABLED, an Apple HLS manifest will be generated for this output.

WriteSegmentTimelineInRepresentation -> (string)

When you enable Precise segment duration in DASH manifests, your DASH manifest shows precise segment durations. The segment duration information appears inside the SegmentTimeline element, inside SegmentTemplate at the Representation level. When this feature isnât enabled, the segment durations in your DASH manifest are approximate. The segment duration information appears in the duration attribute of the SegmentTemplate element.

DashIsoGroupSettings -> (structure)

Settings related to your DASH output package. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html).

AdditionalManifests -> (list)

By default, the service creates one .mpd DASH manifest for each DASH ISO output group in your job. This default manifest references every output in the output group. To create additional DASH manifests that reference a subset of the outputs in the output group, specify a list of them here.

(structure)

Specify the details for each additional DASH manifest that you want the service to generate for this output group. Each manifest can reference a different subset of outputs in the group.

ManifestNameModifier -> (string)

Specify a name modifier that the service adds to the name of this manifest to make it different from the file names of the other main manifests in the output group. For example, say that the default main manifest for your DASH group is film-name.mpd. If you enter â-no-premiumâ for this setting, then the file name the service generates for this top-level manifest is film-name-no-premium.mpd.

SelectedOutputs -> (list)

Specify the outputs that you want this additional top-level manifest to reference.

(string)

AudioChannelConfigSchemeIdUri -> (string)

Use this setting only when your audio codec is a Dolby one (AC3, EAC3, or Atmos) and your downstream workflow requires that your DASH manifest use the Dolby channel configuration tag, rather than the MPEG one. For example, you might need to use this to make dynamic ad insertion work. Specify which audio channel configuration scheme ID URI MediaConvert writes in your DASH manifest. Keep the default value, MPEG channel configuration, to have MediaConvert write this: [urn:mpeg:mpegB:cicp:ChannelConfiguration](urn:mpeg:mpegB:cicp:ChannelConfiguration). Choose Dolby channel configuration to have MediaConvert write this instead: [tag:dolby.com,2014:dash:audio_channel_configuration:2011](tag:dolby.com,2014:dash:audio_channel_configuration:2011).

BaseUrl -> (string)

A partial URI prefix that will be put in the manifest (.mpd) file at the top level BaseURL element. Can be used if streams are delivered from a different URL than the manifest file.

DashIFrameTrickPlayNameModifier -> (string)

Specify whether MediaConvert generates I-frame only video segments for DASH trick play, also known as trick mode. When specified, the I-frame only video segments are included within an additional AdaptationSet in your DASH output manifest. To generate I-frame only video segments: Enter a name as a text string, up to 256 character long. This name is appended to the end of this output groupâs base filename, that you specify as part of your destination URI, and used for the I-frame only video segment files. You may also include format identifiers. For more information, see: [https://docs.aws.amazon.com/mediaconvert/latest/ug/using-variables-in-your-job-settings.html#using-settings-variables-with-streaming-outputs](https://docs.aws.amazon.com/mediaconvert/latest/ug/using-variables-in-your-job-settings.html#using-settings-variables-with-streaming-outputs) To not generate I-frame only video segments: Leave blank.

DashManifestStyle -> (string)

Specify how MediaConvert writes SegmentTimeline in your output DASH manifest. To write a SegmentTimeline in each video Representation: Keep the default value, Basic. To write a common SegmentTimeline in the video AdaptationSet: Choose Compact. Note that MediaConvert will still write a SegmentTimeline in any Representation that does not share a common timeline. To write a video AdaptationSet for each different output framerate, and a common SegmentTimeline in each AdaptationSet: Choose Distinct.

Destination -> (string)

Use Destination to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file.

DestinationSettings -> (structure)

Settings associated with the destination. Will vary based on the type of destination

S3Settings -> (structure)

Settings associated with S3 destination

AccessControl -> (structure)

Optional. Have MediaConvert automatically apply Amazon S3 access control for the outputs in this output group. When you donât use this setting, S3 automatically applies the default access control list PRIVATE.

CannedAcl -> (string)

Choose an Amazon S3 canned ACL for MediaConvert to apply to this output.

Encryption -> (structure)

Settings for how your job outputs are encrypted as they are uploaded to Amazon S3.

EncryptionType -> (string)

Specify how you want your data keys managed. AWS uses data keys to encrypt your content. AWS also encrypts the data keys themselves, using a customer master key (CMK), and then stores the encrypted data keys alongside your encrypted content. Use this setting to specify which AWS service manages the CMK. For simplest set up, choose Amazon S3. If you want your master key to be managed by AWS Key Management Service (KMS), choose AWS KMS. By default, when you choose AWS KMS, KMS uses the AWS managed customer master key (CMK) associated with Amazon S3 to encrypt your data keys. You can optionally choose to specify a different, customer managed CMK. Do so by specifying the Amazon Resource Name (ARN) of the key for the setting KMS ARN.

KmsEncryptionContext -> (string)

Optionally, specify the encryption context that you want to use alongside your KMS key. AWS KMS uses this encryption context as additional authenticated data (AAD) to support authenticated encryption. This value must be a base64-encoded UTF-8 string holding JSON which represents a string-string map. To use this setting, you must also set Server-side encryption to AWS KMS. For more information about encryption context, see: [https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context).

KmsKeyArn -> (string)

Optionally, specify the customer master key (CMK) that you want to use to encrypt the data key that AWS uses to encrypt your output content. Enter the Amazon Resource Name (ARN) of the CMK. To use this setting, you must also set Server-side encryption to AWS KMS. If you set Server-side encryption to AWS KMS but donât specify a CMK here, AWS uses the AWS managed CMK associated with Amazon S3.

StorageClass -> (string)

Specify the S3 storage class to use for this output. To use your destinationâs default storage class: Keep the default value, Not set. For more information about S3 storage classes, see [https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

Encryption -> (structure)

DRM settings.

PlaybackDeviceCompatibility -> (string)

This setting can improve the compatibility of your output with video players on obsolete devices. It applies only to DASH H.264 outputs with DRM encryption. Choose Unencrypted SEI only to correct problems with playback on older devices. Otherwise, keep the default setting CENC v1. If you choose Unencrypted SEI, for that output, the service will exclude the access unit delimiter and will leave the SEI NAL units unencrypted.

SpekeKeyProvider -> (structure)

If your output group type is HLS, DASH, or Microsoft Smooth, use these settings when doing DRM encryption with a SPEKE-compliant key provider. If your output group type is CMAF, use the SpekeKeyProviderCmaf settings instead.

CertificateArn -> (string)

If you want your key provider to encrypt the content keys that it provides to MediaConvert, set up a certificate with a master key using AWS Certificate Manager. Specify the certificateâs Amazon Resource Name (ARN) here.

EncryptionContractConfiguration -> (structure)

Specify the SPEKE version, either v1.0 or v2.0, that MediaConvert uses when encrypting your output. For more information, see: [https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html](https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html) To use SPEKE v1.0: Leave blank. To use SPEKE v2.0: Specify a SPEKE v2.0 video preset and a SPEKE v2.0 audio preset.

SpekeAudioPreset -> (string)

Specify which SPEKE version 2.0 audio preset MediaConvert uses to request content keys from your SPEKE server. For more information, see: [https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html) To encrypt to your audio outputs, choose from the following: Audio preset 1, Audio preset 2, or Audio preset 3. To encrypt your audio outputs, using the same content key for both your audio and video outputs: Choose Shared. When you do, you must also set SPEKE v2.0 video preset to Shared. To not encrypt your audio outputs: Choose Unencrypted. When you do, to encrypt your video outputs, you must also specify a SPEKE v2.0 video preset (other than Shared or Unencrypted).

SpekeVideoPreset -> (string)

Specify which SPEKE version 2.0 video preset MediaConvert uses to request content keys from your SPEKE server. For more information, see: [https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html) To encrypt to your video outputs, choose from the following: Video preset 1, Video preset 2, Video preset 3, Video preset 4, Video preset 5, Video preset 6, Video preset 7, or Video preset 8. To encrypt your video outputs, using the same content key for both your video and audio outputs: Choose Shared. When you do, you must also set SPEKE v2.0 audio preset to Shared. To not encrypt your video outputs: Choose Unencrypted. When you do, to encrypt your audio outputs, you must also specify a SPEKE v2.0 audio preset (other than Shared or Unencrypted).

ResourceId -> (string)

Specify the resource ID that your SPEKE-compliant key provider uses to identify this content.

SystemIds -> (list)

Relates to SPEKE implementation. DRM system identifiers. DASH output groups support a max of two system ids. HLS output groups support a max of 3 system ids. Other group types support one system id. See [https://dashif.org/identifiers/content_protection/](https://dashif.org/identifiers/content_protection/) for more details.

(string)

Url -> (string)

Specify the URL to the key server that your SPEKE-compliant DRM key provider uses to provide keys for encrypting your content.

FragmentLength -> (integer)

Length of fragments to generate (in seconds). Fragment length must be compatible with GOP size and Framerate. Note that fragments will end on the next keyframe after this number of seconds, so actual fragment length may be longer. When Emit Single File is checked, the fragmentation is internal to a single output file and it does not cause the creation of many output files as in other output types.

HbbtvCompliance -> (string)

Supports HbbTV specification as indicated

ImageBasedTrickPlay -> (string)

Specify whether MediaConvert generates images for trick play. Keep the default value, None, to not generate any images. Choose Thumbnail to generate tiled thumbnails. Choose Thumbnail and full frame to generate tiled thumbnails and full-resolution images of single frames. MediaConvert adds an entry in the .mpd manifest for each set of images that you generate. A common application for these images is Roku trick mode. The thumbnails and full-frame images that MediaConvert creates with this feature are compatible with this Roku specification: [https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md](https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md)

ImageBasedTrickPlaySettings -> (structure)

Tile and thumbnail settings applicable when imageBasedTrickPlay is ADVANCED

IntervalCadence -> (string)

The cadence MediaConvert follows for generating thumbnails. If set to FOLLOW_IFRAME, MediaConvert generates thumbnails for each IDR frame in the output (matching the GOP cadence). If set to FOLLOW_CUSTOM, MediaConvert generates thumbnails according to the interval you specify in thumbnailInterval.

ThumbnailHeight -> (integer)

Height of each thumbnail within each tile image, in pixels. Leave blank to maintain aspect ratio with thumbnail width. If following the aspect ratio would lead to a total tile height greater than 4096, then the job will be rejected. Must be divisible by 2.

ThumbnailInterval -> (double)

Enter the interval, in seconds, that MediaConvert uses to generate thumbnails. If the interval you enter doesnât align with the output frame rate, MediaConvert automatically rounds the interval to align with the output frame rate. For example, if the output frame rate is 29.97 frames per second and you enter 5, MediaConvert uses a 150 frame interval to generate thumbnails.

ThumbnailWidth -> (integer)

Width of each thumbnail within each tile image, in pixels. Default is 312. Must be divisible by 8.

TileHeight -> (integer)

Number of thumbnails in each column of a tile image. Set a value between 2 and 2048. Must be divisible by 2.

TileWidth -> (integer)

Number of thumbnails in each row of a tile image. Set a value between 1 and 512.

MinBufferTime -> (integer)

Minimum time of initially buffered media that is needed to ensure smooth playout.

MinFinalSegmentLength -> (double)

Keep this setting at the default value of 0, unless you are troubleshooting a problem with how devices play back the end of your video asset. If you know that player devices are hanging on the final segment of your video because the length of your final segment is too short, use this setting to specify a minimum final segment length, in seconds. Choose a value that is greater than or equal to 1 and less than your segment length. When you specify a value for this setting, the encoder will combine any final segment that is shorter than the length that you specify with the previous segment. For example, your segment length is 3 seconds and your final segment is .5 seconds without a minimum final segment length; when you set the minimum final segment length to 1, your final segment is 3.5 seconds.

MpdManifestBandwidthType -> (string)

Specify how the value for bandwidth is determined for each video Representation in your output MPD manifest. We recommend that you choose a MPD manifest bandwidth type that is compatible with your downstream player configuration. Max: Use the same value that you specify for Max bitrate in the video output, in bits per second. Average: Use the calculated average bitrate of the encoded video output, in bits per second.

MpdProfile -> (string)

Specify whether your DASH profile is on-demand or main. When you choose Main profile, the service signals [urn:mpeg:dash:profile:isoff-main:2011](urn:mpeg:dash:profile:isoff-main:2011) in your .mpd DASH manifest. When you choose On-demand, the service signals [urn:mpeg:dash:profile:isoff-on-demand:2011](urn:mpeg:dash:profile:isoff-on-demand:2011) in your .mpd. When you choose On-demand, you must also set the output group setting Segment control to Single file.

PtsOffsetHandlingForBFrames -> (string)

Use this setting only when your output video stream has B-frames, which causes the initial presentation time stamp (PTS) to be offset from the initial decode time stamp (DTS). Specify how MediaConvert handles PTS when writing time stamps in output DASH manifests. Choose Match initial PTS when you want MediaConvert to use the initial PTS as the first time stamp in the manifest. Choose Zero-based to have MediaConvert ignore the initial PTS in the video stream and instead write the initial time stamp as zero in the manifest. For outputs that donât have B-frames, the time stamps in your DASH manifests start at zero regardless of your choice here.

SegmentControl -> (string)

When set to SINGLE_FILE, a single output file is generated, which is internally segmented using the Fragment Length and Segment Length. When set to SEGMENTED_FILES, separate segment files will be created.

SegmentLength -> (integer)

Specify the length, in whole seconds, of each segment. When you donât specify a value, MediaConvert defaults to 30. Related settings: Use Segment length control to specify whether the encoder enforces this value strictly. Use Segment control to specify whether MediaConvert creates separate segment files or one content file that has metadata to mark the segment boundaries.

SegmentLengthControl -> (string)

Specify how you want MediaConvert to determine segment lengths in this output group. To use the exact value that you specify under Segment length: Choose Exact. Note that this might result in additional I-frames in the output GOP. To create segment lengths that are a multiple of the GOP: Choose Multiple of GOP. MediaConvert will round up the segment lengths to match the next GOP boundary. To have MediaConvert automatically determine a segment duration that is a multiple of both the audio packets and the frame rates: Choose Match. When you do, also specify a target segment duration under Segment length. This is useful for some ad-insertion or segment replacement workflows. Note that Match has the following requirements: - Output containers: Include at least one video output and at least one audio output. Audio-only outputs are not supported. - Output frame rate: Follow source is not supported. - Multiple output frame rates: When you specify multiple outputs, we recommend they share a similar frame rate (as in X/3, X/2, X, or 2X). For example: 5, 15, 30 and 60. Or: 25 and 50. (Outputs must share an integer multiple.) - Output audio codec: Specify Advanced Audio Coding (AAC). - Output sample rate: Choose 48kHz.

VideoCompositionOffsets -> (string)

Specify the video sample composition time offset mode in the output fMP4 TRUN box. For wider player compatibility, set Video composition offsets to Unsigned or leave blank. The earliest presentation time may be greater than zero, and sample composition time offsets will increment using unsigned integers. For strict fMP4 video and audio timing, set Video composition offsets to Signed. The earliest presentation time will be equal to zero, and sample composition time offsets will increment using signed integers.

WriteSegmentTimelineInRepresentation -> (string)

If you get an HTTP error in the 400 range when you play back your DASH output, enable this setting and run your transcoding job again. When you enable this setting, the service writes precise segment durations in the DASH manifest. The segment duration information appears inside the SegmentTimeline element, inside SegmentTemplate at the Representation level. When you donât enable this setting, the service writes approximate segment durations in your DASH manifest.

FileGroupSettings -> (structure)

Settings related to your File output group. MediaConvert uses this group of settings to generate a single standalone file, rather than a streaming package.

Destination -> (string)

Use Destination to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file.

DestinationSettings -> (structure)

Settings associated with the destination. Will vary based on the type of destination

S3Settings -> (structure)

Settings associated with S3 destination

AccessControl -> (structure)

Optional. Have MediaConvert automatically apply Amazon S3 access control for the outputs in this output group. When you donât use this setting, S3 automatically applies the default access control list PRIVATE.

CannedAcl -> (string)

Choose an Amazon S3 canned ACL for MediaConvert to apply to this output.

Encryption -> (structure)

Settings for how your job outputs are encrypted as they are uploaded to Amazon S3.

EncryptionType -> (string)

Specify how you want your data keys managed. AWS uses data keys to encrypt your content. AWS also encrypts the data keys themselves, using a customer master key (CMK), and then stores the encrypted data keys alongside your encrypted content. Use this setting to specify which AWS service manages the CMK. For simplest set up, choose Amazon S3. If you want your master key to be managed by AWS Key Management Service (KMS), choose AWS KMS. By default, when you choose AWS KMS, KMS uses the AWS managed customer master key (CMK) associated with Amazon S3 to encrypt your data keys. You can optionally choose to specify a different, customer managed CMK. Do so by specifying the Amazon Resource Name (ARN) of the key for the setting KMS ARN.

KmsEncryptionContext -> (string)

Optionally, specify the encryption context that you want to use alongside your KMS key. AWS KMS uses this encryption context as additional authenticated data (AAD) to support authenticated encryption. This value must be a base64-encoded UTF-8 string holding JSON which represents a string-string map. To use this setting, you must also set Server-side encryption to AWS KMS. For more information about encryption context, see: [https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context).

KmsKeyArn -> (string)

Optionally, specify the customer master key (CMK) that you want to use to encrypt the data key that AWS uses to encrypt your output content. Enter the Amazon Resource Name (ARN) of the CMK. To use this setting, you must also set Server-side encryption to AWS KMS. If you set Server-side encryption to AWS KMS but donât specify a CMK here, AWS uses the AWS managed CMK associated with Amazon S3.

StorageClass -> (string)

Specify the S3 storage class to use for this output. To use your destinationâs default storage class: Keep the default value, Not set. For more information about S3 storage classes, see [https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

HlsGroupSettings -> (structure)

Settings related to your HLS output package. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html).

AdMarkers -> (list)

Choose one or more ad marker types to decorate your Apple HLS manifest. This setting does not determine whether SCTE-35 markers appear in the outputs themselves.

(string)

Ad marker for Apple HLS manifest.

AdditionalManifests -> (list)

By default, the service creates one top-level .m3u8 HLS manifest for each HLS output group in your job. This default manifest references every output in the output group. To create additional top-level manifests that reference a subset of the outputs in the output group, specify a list of them here.

(structure)

Specify the details for each additional HLS manifest that you want the service to generate for this output group. Each manifest can reference a different subset of outputs in the group.

ManifestNameModifier -> (string)

Specify a name modifier that the service adds to the name of this manifest to make it different from the file names of the other main manifests in the output group. For example, say that the default main manifest for your HLS group is film-name.m3u8. If you enter â-no-premiumâ for this setting, then the file name the service generates for this top-level manifest is film-name-no-premium.m3u8. For HLS output groups, specify a manifestNameModifier that is different from the nameModifier of the output. The service uses the output name modifier to create unique names for the individual variant manifests.

SelectedOutputs -> (list)

Specify the outputs that you want this additional top-level manifest to reference.

(string)

AudioOnlyHeader -> (string)

Ignore this setting unless you are using FairPlay DRM with Verimatrix and you encounter playback issues. Keep the default value, Include, to output audio-only headers. Choose Exclude to remove the audio-only headers from your audio segments.

BaseUrl -> (string)

A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file.

CaptionLanguageMappings -> (list)

Language to be used on Caption outputs

(structure)

Caption Language Mapping

CaptionChannel -> (integer)

Caption channel.

CustomLanguageCode -> (string)

Specify the language for this captions channel, using the ISO 639-2 or ISO 639-3 three-letter language code

LanguageCode -> (string)

Specify the language, using the ISO 639-2 three-letter code listed at [https://www.loc.gov/standards/iso639-2/php/code_list.php](https://www.loc.gov/standards/iso639-2/php/code_list.php).

LanguageDescription -> (string)

Caption language description.

CaptionLanguageSetting -> (string)

Applies only to 608 Embedded output captions. Insert: Include CLOSED-CAPTIONS lines in the manifest. Specify at least one language in the CC1 Language Code field. One CLOSED-CAPTION line is added for each Language Code you specify. Make sure to specify the languages in the order in which they appear in the original source (if the source is embedded format) or the order of the caption selectors (if the source is other than embedded). Otherwise, languages in the manifest will not match up properly with the output captions. None: Include CLOSED-CAPTIONS=NONE line in the manifest. Omit: Omit any CLOSED-CAPTIONS line from the manifest.

CaptionSegmentLengthControl -> (string)

Set Caption segment length control to Match video to create caption segments that align with the video segments from the first video output in this output group. For example, if the video segments are 2 seconds long, your WebVTT segments will also be 2 seconds long. Keep the default setting, Large segments to create caption segments that are 300 seconds long.

ClientCache -> (string)

Disable this setting only when your workflow requires the #EXT-X-ALLOW-CACHE:no tag. Otherwise, keep the default value Enabled and control caching in your video distribution set up. For example, use the Cache-Control http header.

CodecSpecification -> (string)

Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation.

Destination -> (string)

Use Destination to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file.

DestinationSettings -> (structure)

Settings associated with the destination. Will vary based on the type of destination

S3Settings -> (structure)

Settings associated with S3 destination

AccessControl -> (structure)

Optional. Have MediaConvert automatically apply Amazon S3 access control for the outputs in this output group. When you donât use this setting, S3 automatically applies the default access control list PRIVATE.

CannedAcl -> (string)

Choose an Amazon S3 canned ACL for MediaConvert to apply to this output.

Encryption -> (structure)

Settings for how your job outputs are encrypted as they are uploaded to Amazon S3.

EncryptionType -> (string)

Specify how you want your data keys managed. AWS uses data keys to encrypt your content. AWS also encrypts the data keys themselves, using a customer master key (CMK), and then stores the encrypted data keys alongside your encrypted content. Use this setting to specify which AWS service manages the CMK. For simplest set up, choose Amazon S3. If you want your master key to be managed by AWS Key Management Service (KMS), choose AWS KMS. By default, when you choose AWS KMS, KMS uses the AWS managed customer master key (CMK) associated with Amazon S3 to encrypt your data keys. You can optionally choose to specify a different, customer managed CMK. Do so by specifying the Amazon Resource Name (ARN) of the key for the setting KMS ARN.

KmsEncryptionContext -> (string)

Optionally, specify the encryption context that you want to use alongside your KMS key. AWS KMS uses this encryption context as additional authenticated data (AAD) to support authenticated encryption. This value must be a base64-encoded UTF-8 string holding JSON which represents a string-string map. To use this setting, you must also set Server-side encryption to AWS KMS. For more information about encryption context, see: [https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context).

KmsKeyArn -> (string)

Optionally, specify the customer master key (CMK) that you want to use to encrypt the data key that AWS uses to encrypt your output content. Enter the Amazon Resource Name (ARN) of the CMK. To use this setting, you must also set Server-side encryption to AWS KMS. If you set Server-side encryption to AWS KMS but donât specify a CMK here, AWS uses the AWS managed CMK associated with Amazon S3.

StorageClass -> (string)

Specify the S3 storage class to use for this output. To use your destinationâs default storage class: Keep the default value, Not set. For more information about S3 storage classes, see [https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

DirectoryStructure -> (string)

Indicates whether segments should be placed in subdirectories.

Encryption -> (structure)

DRM settings.

ConstantInitializationVector -> (string)

This is a 128-bit, 16-byte hex value represented by a 32-character text string. If this parameter is not set then the Initialization Vector will follow the segment number by default.

EncryptionMethod -> (string)

Encrypts the segments with the given encryption scheme. Leave blank to disable. Selecting âDisabledâ in the web interface also disables encryption.

InitializationVectorInManifest -> (string)

The Initialization Vector is a 128-bit number used in conjunction with the key for encrypting blocks. If set to INCLUDE, Initialization Vector is listed in the manifest. Otherwise Initialization Vector is not in the manifest.

OfflineEncrypted -> (string)

Enable this setting to insert the EXT-X-SESSION-KEY element into the master playlist. This allows for offline Apple HLS FairPlay content protection.

SpekeKeyProvider -> (structure)

If your output group type is HLS, DASH, or Microsoft Smooth, use these settings when doing DRM encryption with a SPEKE-compliant key provider. If your output group type is CMAF, use the SpekeKeyProviderCmaf settings instead.

CertificateArn -> (string)

If you want your key provider to encrypt the content keys that it provides to MediaConvert, set up a certificate with a master key using AWS Certificate Manager. Specify the certificateâs Amazon Resource Name (ARN) here.

EncryptionContractConfiguration -> (structure)

Specify the SPEKE version, either v1.0 or v2.0, that MediaConvert uses when encrypting your output. For more information, see: [https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html](https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html) To use SPEKE v1.0: Leave blank. To use SPEKE v2.0: Specify a SPEKE v2.0 video preset and a SPEKE v2.0 audio preset.

SpekeAudioPreset -> (string)

Specify which SPEKE version 2.0 audio preset MediaConvert uses to request content keys from your SPEKE server. For more information, see: [https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html) To encrypt to your audio outputs, choose from the following: Audio preset 1, Audio preset 2, or Audio preset 3. To encrypt your audio outputs, using the same content key for both your audio and video outputs: Choose Shared. When you do, you must also set SPEKE v2.0 video preset to Shared. To not encrypt your audio outputs: Choose Unencrypted. When you do, to encrypt your video outputs, you must also specify a SPEKE v2.0 video preset (other than Shared or Unencrypted).

SpekeVideoPreset -> (string)

Specify which SPEKE version 2.0 video preset MediaConvert uses to request content keys from your SPEKE server. For more information, see: [https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html) To encrypt to your video outputs, choose from the following: Video preset 1, Video preset 2, Video preset 3, Video preset 4, Video preset 5, Video preset 6, Video preset 7, or Video preset 8. To encrypt your video outputs, using the same content key for both your video and audio outputs: Choose Shared. When you do, you must also set SPEKE v2.0 audio preset to Shared. To not encrypt your video outputs: Choose Unencrypted. When you do, to encrypt your audio outputs, you must also specify a SPEKE v2.0 audio preset (other than Shared or Unencrypted).

ResourceId -> (string)

Specify the resource ID that your SPEKE-compliant key provider uses to identify this content.

SystemIds -> (list)

Relates to SPEKE implementation. DRM system identifiers. DASH output groups support a max of two system ids. HLS output groups support a max of 3 system ids. Other group types support one system id. See [https://dashif.org/identifiers/content_protection/](https://dashif.org/identifiers/content_protection/) for more details.

(string)

Url -> (string)

Specify the URL to the key server that your SPEKE-compliant DRM key provider uses to provide keys for encrypting your content.

StaticKeyProvider -> (structure)

Use these settings to set up encryption with a static key provider.

KeyFormat -> (string)

Relates to DRM implementation. Sets the value of the KEYFORMAT attribute. Must be âidentityâ or a reverse DNS string. May be omitted to indicate an implicit value of âidentityâ.

KeyFormatVersions -> (string)

Relates to DRM implementation. Either a single positive integer version value or a slash delimited list of version values (1/2/3).

StaticKeyValue -> (string)

Relates to DRM implementation. Use a 32-character hexidecimal string to specify Key Value.

Url -> (string)

Relates to DRM implementation. The location of the license server used for protecting content.

Type -> (string)

Specify whether your DRM encryption key is static or from a key provider that follows the SPEKE standard. For more information about SPEKE, see [https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html](https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html).

ImageBasedTrickPlay -> (string)

Specify whether MediaConvert generates images for trick play. Keep the default value, None, to not generate any images. Choose Thumbnail to generate tiled thumbnails. Choose Thumbnail and full frame to generate tiled thumbnails and full-resolution images of single frames. MediaConvert creates a child manifest for each set of images that you generate and adds corresponding entries to the parent manifest. A common application for these images is Roku trick mode. The thumbnails and full-frame images that MediaConvert creates with this feature are compatible with this Roku specification: [https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md](https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md)

ImageBasedTrickPlaySettings -> (structure)

Tile and thumbnail settings applicable when imageBasedTrickPlay is ADVANCED

IntervalCadence -> (string)

The cadence MediaConvert follows for generating thumbnails. If set to FOLLOW_IFRAME, MediaConvert generates thumbnails for each IDR frame in the output (matching the GOP cadence). If set to FOLLOW_CUSTOM, MediaConvert generates thumbnails according to the interval you specify in thumbnailInterval.

ThumbnailHeight -> (integer)

Height of each thumbnail within each tile image, in pixels. Leave blank to maintain aspect ratio with thumbnail width. If following the aspect ratio would lead to a total tile height greater than 4096, then the job will be rejected. Must be divisible by 2.

ThumbnailInterval -> (double)

Enter the interval, in seconds, that MediaConvert uses to generate thumbnails. If the interval you enter doesnât align with the output frame rate, MediaConvert automatically rounds the interval to align with the output frame rate. For example, if the output frame rate is 29.97 frames per second and you enter 5, MediaConvert uses a 150 frame interval to generate thumbnails.

ThumbnailWidth -> (integer)

Width of each thumbnail within each tile image, in pixels. Default is 312. Must be divisible by 8.

TileHeight -> (integer)

Number of thumbnails in each column of a tile image. Set a value between 2 and 2048. Must be divisible by 2.

TileWidth -> (integer)

Number of thumbnails in each row of a tile image. Set a value between 1 and 512.

ManifestCompression -> (string)

When set to GZIP, compresses HLS playlist.

ManifestDurationFormat -> (string)

Indicates whether the output manifest should use floating point values for segment duration.

MinFinalSegmentLength -> (double)

Keep this setting at the default value of 0, unless you are troubleshooting a problem with how devices play back the end of your video asset. If you know that player devices are hanging on the final segment of your video because the length of your final segment is too short, use this setting to specify a minimum final segment length, in seconds. Choose a value that is greater than or equal to 1 and less than your segment length. When you specify a value for this setting, the encoder will combine any final segment that is shorter than the length that you specify with the previous segment. For example, your segment length is 3 seconds and your final segment is .5 seconds without a minimum final segment length; when you set the minimum final segment length to 1, your final segment is 3.5 seconds.

MinSegmentLength -> (integer)

When set, Minimum Segment Size is enforced by looking ahead and back within the specified range for a nearby avail and extending the segment size if needed.

OutputSelection -> (string)

Indicates whether the .m3u8 manifest file should be generated for this HLS output group.

ProgramDateTime -> (string)

Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is calculated as follows: either the program date and time are initialized using the input timecode source, or the time is initialized using the input timecode source and the date is initialized using the timestamp_offset.

ProgramDateTimePeriod -> (integer)

Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds.

ProgressiveWriteHlsManifest -> (string)

Specify whether MediaConvert generates HLS manifests while your job is running or when your job is complete. To generate HLS manifests while your job is running: Choose Enabled. Use if you want to play back your content as soon as itâs available. MediaConvert writes the parent and child manifests after the first three media segments are written to your destination S3 bucket. It then writes new updated manifests after each additional segment is written. The parent manifest includes the latest BANDWIDTH and AVERAGE-BANDWIDTH attributes, and child manifests include the latest available media segment. When your job completes, the final child playlists include an EXT-X-ENDLIST tag. To generate HLS manifests only when your job completes: Choose Disabled.

SegmentControl -> (string)

When set to SINGLE_FILE, emits program as a single media resource (.ts) file, uses #EXT-X-BYTERANGE tags to index segment for playback.

SegmentLength -> (integer)

Specify the length, in whole seconds, of each segment. When you donât specify a value, MediaConvert defaults to 10. Related settings: Use Segment length control to specify whether the encoder enforces this value strictly. Use Segment control to specify whether MediaConvert creates separate segment files or one content file that has metadata to mark the segment boundaries.

SegmentLengthControl -> (string)

Specify how you want MediaConvert to determine segment lengths in this output group. To use the exact value that you specify under Segment length: Choose Exact. Note that this might result in additional I-frames in the output GOP. To create segment lengths that are a multiple of the GOP: Choose Multiple of GOP. MediaConvert will round up the segment lengths to match the next GOP boundary. To have MediaConvert automatically determine a segment duration that is a multiple of both the audio packets and the frame rates: Choose Match. When you do, also specify a target segment duration under Segment length. This is useful for some ad-insertion or segment replacement workflows. Note that Match has the following requirements: - Output containers: Include at least one video output and at least one audio output. Audio-only outputs are not supported. - Output frame rate: Follow source is not supported. - Multiple output frame rates: When you specify multiple outputs, we recommend they share a similar frame rate (as in X/3, X/2, X, or 2X). For example: 5, 15, 30 and 60. Or: 25 and 50. (Outputs must share an integer multiple.) - Output audio codec: Specify Advanced Audio Coding (AAC). - Output sample rate: Choose 48kHz.

SegmentsPerSubdirectory -> (integer)

Specify the number of segments to write to a subdirectory before starting a new one. You must also set Directory structure to Subdirectory per stream for this setting to have an effect.

StreamInfResolution -> (string)

Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest.

TargetDurationCompatibilityMode -> (string)

When set to LEGACY, the segment target duration is always rounded up to the nearest integer value above its current value in seconds. When set to SPEC\_COMPLIANT, the segment target duration is rounded up to the nearest integer value if fraction seconds are greater than or equal to 0.5 (>= 0.5) and rounded down if less than 0.5 (<0.5). You may need to use LEGACY if your client needs to ensure that the target duration is always longer than the actual duration of the segment. Some older players may experience interrupted playback when the actual duration of a track in a segment is longer than the target duration.

TimedMetadataId3Frame -> (string)

Specify the type of the ID3 frame to use for ID3 timestamps in your output. To include ID3 timestamps: Specify PRIV or TDRL and set ID3 metadata to Passthrough. To exclude ID3 timestamps: Set ID3 timestamp frame type to None.

TimedMetadataId3Period -> (integer)

Specify the interval in seconds to write ID3 timestamps in your output. The first timestamp starts at the output timecode and date, and increases incrementally with each ID3 timestamp. To use the default interval of 10 seconds: Leave blank. To include this metadata in your output: Set ID3 timestamp frame type to PRIV or TDRL, and set ID3 metadata to Passthrough.

TimestampDeltaMilliseconds -> (integer)

Provides an extra millisecond delta offset to fine tune the timestamps.

MsSmoothGroupSettings -> (structure)

Settings related to your Microsoft Smooth Streaming output package. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html).

AdditionalManifests -> (list)

By default, the service creates one .ism Microsoft Smooth Streaming manifest for each Microsoft Smooth Streaming output group in your job. This default manifest references every output in the output group. To create additional manifests that reference a subset of the outputs in the output group, specify a list of them here.

(structure)

Specify the details for each additional Microsoft Smooth Streaming manifest that you want the service to generate for this output group. Each manifest can reference a different subset of outputs in the group.

ManifestNameModifier -> (string)

Specify a name modifier that the service adds to the name of this manifest to make it different from the file names of the other main manifests in the output group. For example, say that the default main manifest for your Microsoft Smooth group is film-name.ismv. If you enter â-no-premiumâ for this setting, then the file name the service generates for this top-level manifest is film-name-no-premium.ismv.

SelectedOutputs -> (list)

Specify the outputs that you want this additional top-level manifest to reference.

(string)

AudioDeduplication -> (string)

COMBINE_DUPLICATE_STREAMS combines identical audio encoding settings across a Microsoft Smooth output group into a single audio stream.

Destination -> (string)

Use Destination to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file.

DestinationSettings -> (structure)

Settings associated with the destination. Will vary based on the type of destination

S3Settings -> (structure)

Settings associated with S3 destination

AccessControl -> (structure)

Optional. Have MediaConvert automatically apply Amazon S3 access control for the outputs in this output group. When you donât use this setting, S3 automatically applies the default access control list PRIVATE.

CannedAcl -> (string)

Choose an Amazon S3 canned ACL for MediaConvert to apply to this output.

Encryption -> (structure)

Settings for how your job outputs are encrypted as they are uploaded to Amazon S3.

EncryptionType -> (string)

Specify how you want your data keys managed. AWS uses data keys to encrypt your content. AWS also encrypts the data keys themselves, using a customer master key (CMK), and then stores the encrypted data keys alongside your encrypted content. Use this setting to specify which AWS service manages the CMK. For simplest set up, choose Amazon S3. If you want your master key to be managed by AWS Key Management Service (KMS), choose AWS KMS. By default, when you choose AWS KMS, KMS uses the AWS managed customer master key (CMK) associated with Amazon S3 to encrypt your data keys. You can optionally choose to specify a different, customer managed CMK. Do so by specifying the Amazon Resource Name (ARN) of the key for the setting KMS ARN.

KmsEncryptionContext -> (string)

Optionally, specify the encryption context that you want to use alongside your KMS key. AWS KMS uses this encryption context as additional authenticated data (AAD) to support authenticated encryption. This value must be a base64-encoded UTF-8 string holding JSON which represents a string-string map. To use this setting, you must also set Server-side encryption to AWS KMS. For more information about encryption context, see: [https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context).

KmsKeyArn -> (string)

Optionally, specify the customer master key (CMK) that you want to use to encrypt the data key that AWS uses to encrypt your output content. Enter the Amazon Resource Name (ARN) of the CMK. To use this setting, you must also set Server-side encryption to AWS KMS. If you set Server-side encryption to AWS KMS but donât specify a CMK here, AWS uses the AWS managed CMK associated with Amazon S3.

StorageClass -> (string)

Specify the S3 storage class to use for this output. To use your destinationâs default storage class: Keep the default value, Not set. For more information about S3 storage classes, see [https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

Encryption -> (structure)

If you are using DRM, set DRM System to specify the value SpekeKeyProvider.

SpekeKeyProvider -> (structure)

If your output group type is HLS, DASH, or Microsoft Smooth, use these settings when doing DRM encryption with a SPEKE-compliant key provider. If your output group type is CMAF, use the SpekeKeyProviderCmaf settings instead.

CertificateArn -> (string)

If you want your key provider to encrypt the content keys that it provides to MediaConvert, set up a certificate with a master key using AWS Certificate Manager. Specify the certificateâs Amazon Resource Name (ARN) here.

EncryptionContractConfiguration -> (structure)

Specify the SPEKE version, either v1.0 or v2.0, that MediaConvert uses when encrypting your output. For more information, see: [https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html](https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html) To use SPEKE v1.0: Leave blank. To use SPEKE v2.0: Specify a SPEKE v2.0 video preset and a SPEKE v2.0 audio preset.

SpekeAudioPreset -> (string)

Specify which SPEKE version 2.0 audio preset MediaConvert uses to request content keys from your SPEKE server. For more information, see: [https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html) To encrypt to your audio outputs, choose from the following: Audio preset 1, Audio preset 2, or Audio preset 3. To encrypt your audio outputs, using the same content key for both your audio and video outputs: Choose Shared. When you do, you must also set SPEKE v2.0 video preset to Shared. To not encrypt your audio outputs: Choose Unencrypted. When you do, to encrypt your video outputs, you must also specify a SPEKE v2.0 video preset (other than Shared or Unencrypted).

SpekeVideoPreset -> (string)

Specify which SPEKE version 2.0 video preset MediaConvert uses to request content keys from your SPEKE server. For more information, see: [https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html) To encrypt to your video outputs, choose from the following: Video preset 1, Video preset 2, Video preset 3, Video preset 4, Video preset 5, Video preset 6, Video preset 7, or Video preset 8. To encrypt your video outputs, using the same content key for both your video and audio outputs: Choose Shared. When you do, you must also set SPEKE v2.0 audio preset to Shared. To not encrypt your video outputs: Choose Unencrypted. When you do, to encrypt your audio outputs, you must also specify a SPEKE v2.0 audio preset (other than Shared or Unencrypted).

ResourceId -> (string)

Specify the resource ID that your SPEKE-compliant key provider uses to identify this content.

SystemIds -> (list)

Relates to SPEKE implementation. DRM system identifiers. DASH output groups support a max of two system ids. HLS output groups support a max of 3 system ids. Other group types support one system id. See [https://dashif.org/identifiers/content_protection/](https://dashif.org/identifiers/content_protection/) for more details.

(string)

Url -> (string)

Specify the URL to the key server that your SPEKE-compliant DRM key provider uses to provide keys for encrypting your content.

FragmentLength -> (integer)

Specify how you want MediaConvert to determine the fragment length. Choose Exact to have the encoder use the exact length that you specify with the setting Fragment length. This might result in extra I-frames. Choose Multiple of GOP to have the encoder round up the segment lengths to match the next GOP boundary.

FragmentLengthControl -> (string)

Specify how you want MediaConvert to determine the fragment length. Choose Exact to have the encoder use the exact length that you specify with the setting Fragment length. This might result in extra I-frames. Choose Multiple of GOP to have the encoder round up the segment lengths to match the next GOP boundary.

ManifestEncoding -> (string)

Use Manifest encoding to specify the encoding format for the server and client manifest. Valid options are utf8 and utf16.

PerFrameMetrics -> (list)

Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: * PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

(string)

- PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

Type -> (string)

Type of output group (File group, Apple HLS, DASH ISO, Microsoft Smooth Streaming, CMAF)

Outputs -> (list)

This object holds groups of encoding settings, one group of settings per output.

(structure)

Each output in your job is a collection of settings that describes how you want MediaConvert to encode a single output file or stream. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/create-outputs.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/create-outputs.html).

AudioDescriptions -> (list)

Contains groups of audio encoding settings organized by audio codec. Include one instance of per output. Can contain multiple groups of encoding settings.

(structure)

Settings related to one audio tab on the MediaConvert console. In your job JSON, an instance of AudioDescription is equivalent to one audio tab in the console. Usually, one audio tab corresponds to one output audio track. Depending on how you set up your input audio selectors and whether you use audio selector groups, one audio tab can correspond to a group of output audio tracks.

AudioChannelTaggingSettings -> (structure)

Specify the QuickTime audio channel layout tags for the audio channels in this audio track. When you donât specify a value, MediaConvert labels your track as Center (C) by default. To use Audio layout tagging, your output must be in a QuickTime (MOV) container and your audio codec must be AAC, WAV, or AIFF.

ChannelTag -> (string)

Specify the QuickTime audio channel layout tags for the audio channels in this audio track. Enter channel layout tags in the same order as your outputâs audio channel order. For example, if your output audio track has a left and a right channel, enter Left (L) for the first channel and Right (R) for the second. If your output has multiple single-channel audio tracks, enter a single channel layout tag for each track.

ChannelTags -> (list)

Specify the QuickTime audio channel layout tags for the audio channels in this audio track. Enter channel layout tags in the same order as your outputâs audio channel order. For example, if your output audio track has a left and a right channel, enter Left (L) for the first channel and Right (R) for the second. If your output has multiple single-channel audio tracks, enter a single channel layout tag for each track.

(string)

Specify the QuickTime audio channel layout tags for the audio channels in this audio track. Enter channel layout tags in the same order as your outputâs audio channel order. For example, if your output audio track has a left and a right channel, enter Left (L) for the first channel and Right (R) for the second. If your output has multiple single-channel audio tracks, enter a single channel layout tag for each track.

AudioNormalizationSettings -> (structure)

Advanced audio normalization settings. Ignore these settings unless you need to comply with a loudness standard.

Algorithm -> (string)

Choose one of the following audio normalization algorithms: ITU-R BS.1770-1: Ungated loudness. A measurement of ungated average loudness for an entire piece of content, suitable for measurement of short-form content under ATSC recommendation A/85. Supports up to 5.1 audio channels. ITU-R BS.1770-2: Gated loudness. A measurement of gated average loudness compliant with the requirements of EBU-R128. Supports up to 5.1 audio channels. ITU-R BS.1770-3: Modified peak. The same loudness measurement algorithm as 1770-2, with an updated true peak measurement. ITU-R BS.1770-4: Higher channel count. Allows for more audio channels than the other algorithms, including configurations such as 7.1.

AlgorithmControl -> (string)

When enabled the output audio is corrected using the chosen algorithm. If disabled, the audio will be measured but not adjusted.

CorrectionGateLevel -> (integer)

Content measuring above this level will be corrected to the target level. Content measuring below this level will not be corrected.

LoudnessLogging -> (string)

If set to LOG, log each outputâs audio track loudness to a CSV file.

PeakCalculation -> (string)

If set to TRUE_PEAK, calculate and log the TruePeak for each outputâs audio track loudness.

TargetLkfs -> (double)

When you use Audio normalization, optionally use this setting to specify a target loudness. If you donât specify a value here, the encoder chooses a value for you, based on the algorithm that you choose for Algorithm. If you choose algorithm 1770-1, the encoder will choose -24 LKFS; otherwise, the encoder will choose -23 LKFS.

TruePeakLimiterThreshold -> (double)

Specify the True-peak limiter threshold in decibels relative to full scale (dBFS). The peak inter-audio sample loudness in your output will be limited to the value that you specify, without affecting the overall target LKFS. Enter a value from 0 to -8. Leave blank to use the default value 0.

AudioSourceName -> (string)

Specifies which audio data to use from each input. In the simplest case, specify an âAudio Selectorâ:#inputs-audio_selector by name based on its order within each input. For example if you specify âAudio Selector 3â, then the third audio selector will be used from each input. If an input does not have an âAudio Selector 3â, then the audio selector marked as âdefaultâ in that input will be used. If there is no audio selector marked as âdefaultâ, silence will be inserted for the duration of that input. Alternatively, an âAudio Selector Groupâ:#inputs-audio_selector_group name may be specified, with similar default/silence behavior. If no audio_source_name is specified, then âAudio Selector 1â will be chosen automatically.

AudioType -> (integer)

Applies only if Follow Input Audio Type is unchecked (false). A number between 0 and 255. The following are defined in ISO-IEC 13818-1: 0 = Undefined, 1 = Clean Effects, 2 = Hearing Impaired, 3 = Visually Impaired Commentary, 4-255 = Reserved.

AudioTypeControl -> (string)

When set to FOLLOW_INPUT, if the input contains an ISO 639 audio_type, then that value is passed through to the output. If the input contains no ISO 639 audio_type, the value in Audio Type is included in the output. Otherwise the value in Audio Type is included in the output. Note that this field and audioType are both ignored if audioDescriptionBroadcasterMix is set to BROADCASTER_MIXED_AD.

CodecSettings -> (structure)

Settings related to audio encoding. The settings in this group vary depending on the value that you choose for your audio codec.

AacSettings -> (structure)

Required when you set Codec to the value AAC. The service accepts one of two mutually exclusive groups of AAC settingsâVBR and CBR. To select one of these modes, set the value of Bitrate control mode to âVBRâ or âCBRâ. In VBR mode, you control the audio quality with the setting VBR quality. In CBR mode, you use the setting Bitrate. Defaults and valid values depend on the rate control mode.

AudioDescriptionBroadcasterMix -> (string)

Choose BROADCASTER_MIXED_AD when the input contains pre-mixed main audio + audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains âbroadcaster mixed ADâ. Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER_MIXED_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NORMAL when the input does not contain pre-mixed audio + audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType.

Bitrate -> (integer)

Specify the average bitrate in bits per second. The set of valid values for this setting is: 6000, 8000, 10000, 12000, 14000, 16000, 20000, 24000, 28000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000, 224000, 256000, 288000, 320000, 384000, 448000, 512000, 576000, 640000, 768000, 896000, 1024000. The value you set is also constrained by the values that you choose for Profile, Bitrate control mode, and Sample rate. Default values depend on Bitrate control mode and Profile.

CodecProfile -> (string)

Specify the AAC profile. For the widest player compatibility and where higher bitrates are acceptable: Keep the default profile, LC (AAC-LC) For improved audio performance at lower bitrates: Choose HEV1 or HEV2. HEV1 (AAC-HE v1) adds spectral band replication to improve speech audio at low bitrates. HEV2 (AAC-HE v2) adds parametric stereo, which optimizes for encoding stereo audio at very low bitrates.

CodingMode -> (string)

The Coding mode that you specify determines the number of audio channels and the audio channel layout metadata in your AAC output. Valid coding modes depend on the Rate control mode and Profile that you select. The following list shows the number of audio channels and channel layout for each coding mode. * 1.0 Audio Description (Receiver Mix): One channel, C. Includes audio description data from your stereo input. For more information see ETSI TS 101 154 Annex E. * 1.0 Mono: One channel, C. * 2.0 Stereo: Two channels, L, R. * 5.1 Surround: Six channels, C, L, R, Ls, Rs, LFE.

RateControlMode -> (string)

Specify the AAC rate control mode. For a constant bitrate: Choose CBR. Your AAC output bitrate will be equal to the value that you choose for Bitrate. For a variable bitrate: Choose VBR. Your AAC output bitrate will vary according to your audio content and the value that you choose for Bitrate quality.

RawFormat -> (string)

Enables LATM/LOAS AAC output. Note that if you use LATM/LOAS AAC in an output, you must choose âNo containerâ for the output container.

SampleRate -> (integer)

Specify the AAC sample rate in samples per second (Hz). Valid sample rates depend on the AAC profile and Coding mode that you select. For a list of supported sample rates, see: [https://docs.aws.amazon.com/mediaconvert/latest/ug/aac-support.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/aac-support.html)

Specification -> (string)

Use MPEG-2 AAC instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers.

VbrQuality -> (string)

Specify the quality of your variable bitrate (VBR) AAC audio. For a list of approximate VBR bitrates, see: [https://docs.aws.amazon.com/mediaconvert/latest/ug/aac-support.html#aac_vbr](https://docs.aws.amazon.com/mediaconvert/latest/ug/aac-support.html#aac_vbr)

Ac3Settings -> (structure)

Required when you set Codec to the value AC3.

Bitrate -> (integer)

Specify the average bitrate in bits per second. The bitrate that you specify must be a multiple of 8000 within the allowed minimum and maximum values. Leave blank to use the default bitrate for the coding mode you select according ETSI TS 102 366. Valid bitrates for coding mode 1/0: Default: 96000. Minimum: 64000. Maximum: 128000. Valid bitrates for coding mode 1/1: Default: 192000. Minimum: 128000. Maximum: 384000. Valid bitrates for coding mode 2/0: Default: 192000. Minimum: 128000. Maximum: 384000. Valid bitrates for coding mode 3/2 with FLE: Default: 384000. Minimum: 384000. Maximum: 640000.

BitstreamMode -> (string)

Specify the bitstream mode for the AC-3 stream that the encoder emits. For more information about the AC3 bitstream mode, see ATSC A/52-2012 (Annex E).

CodingMode -> (string)

Dolby Digital coding mode. Determines number of channels.

Dialnorm -> (integer)

Sets the dialnorm for the output. If blank and input audio is Dolby Digital, dialnorm will be passed through.

DynamicRangeCompressionLine -> (string)

Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the line operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at [https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf](https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf).

DynamicRangeCompressionProfile -> (string)

When you want to add Dolby dynamic range compression (DRC) signaling to your output stream, we recommend that you use the mode-specific settings instead of Dynamic range compression profile. The mode-specific settings are Dynamic range compression profile, line mode and Dynamic range compression profile, RF mode. Note that when you specify values for all three settings, MediaConvert ignores the value of this setting in favor of the mode-specific settings. If you do use this setting instead of the mode-specific settings, choose None to leave out DRC signaling. Keep the default Film standard to set the profile to Dolbyâs film standard profile for all operating modes.

DynamicRangeCompressionRf -> (string)

Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the RF operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at [https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf](https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf).

LfeFilter -> (string)

Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3_2_LFE coding mode.

MetadataControl -> (string)

When set to FOLLOW_INPUT, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.

SampleRate -> (integer)

This value is always 48000. It represents the sample rate in Hz.

AiffSettings -> (structure)

Required when you set Codec to the value AIFF.

BitDepth -> (integer)

Specify Bit depth, in bits per sample, to choose the encoding quality for this audio track.

Channels -> (integer)

Specify the number of channels in this output audio track. Valid values are 1 and even numbers up to 64. For example, 1, 2, 4, 6, and so on, up to 64.

SampleRate -> (integer)

Sample rate in Hz.

Codec -> (string)

Choose the audio codec for this output. Note that the option Dolby Digital passthrough applies only to Dolby Digital and Dolby Digital Plus audio inputs. Make sure that you choose a codec thatâs supported with your output container: [https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html#reference-codecs-containers-output-audio](https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html#reference-codecs-containers-output-audio) For audio-only outputs, make sure that both your input audio codec and your output audio codec are supported for audio-only workflows. For more information, see: [https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers-input.html#reference-codecs-containers-input-audio-only](https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers-input.html#reference-codecs-containers-input-audio-only) and [https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html#audio-only-output](https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html#audio-only-output)

Eac3AtmosSettings -> (structure)

Required when you set Codec to the value EAC3_ATMOS.

Bitrate -> (integer)

Specify the average bitrate for this output in bits per second. Valid values: 384k, 448k, 576k, 640k, 768k, 1024k Default value: 448k Note that MediaConvert supports 384k only with channel-based immersive (CBI) 7.1.4 and 5.1.4 inputs. For CBI 9.1.6 and other input types, MediaConvert automatically increases your output bitrate to 448k.

BitstreamMode -> (string)

Specify the bitstream mode for the E-AC-3 stream that the encoder emits. For more information about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E).

CodingMode -> (string)

The coding mode for Dolby Digital Plus JOC (Atmos).

DialogueIntelligence -> (string)

Enable Dolby Dialogue Intelligence to adjust loudness based on dialogue analysis.

DownmixControl -> (string)

Specify whether MediaConvert should use any downmix metadata from your input file. Keep the default value, Custom to provide downmix values in your job settings. Choose Follow source to use the metadata from your input. Related settingsâUse these settings to specify your downmix values: Left only/Right only surround, Left total/Right total surround, Left total/Right total center, Left only/Right only center, and Stereo downmix. When you keep Custom for Downmix control and you donât specify values for the related settings, MediaConvert uses default values for those settings.

DynamicRangeCompressionLine -> (string)

Choose the Dolby dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby stream for the line operating mode. Default value: Film light Related setting: To have MediaConvert use the value you specify here, keep the default value, Custom for the setting Dynamic range control. Otherwise, MediaConvert ignores Dynamic range compression line. For information about the Dolby DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at [https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf](https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf).

DynamicRangeCompressionRf -> (string)

Choose the Dolby dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby stream for the RF operating mode. Default value: Film light Related setting: To have MediaConvert use the value you specify here, keep the default value, Custom for the setting Dynamic range control. Otherwise, MediaConvert ignores Dynamic range compression RF. For information about the Dolby DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at [https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf](https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf).

DynamicRangeControl -> (string)

Specify whether MediaConvert should use any dynamic range control metadata from your input file. Keep the default value, Custom, to provide dynamic range control values in your job settings. Choose Follow source to use the metadata from your input. Related settingsâUse these settings to specify your dynamic range control values: Dynamic range compression line and Dynamic range compression RF. When you keep the value Custom for Dynamic range control and you donât specify values for the related settings, MediaConvert uses default values for those settings.

LoRoCenterMixLevel -> (double)

Specify a value for the following Dolby Atmos setting: Left only/Right only center mix (Lo/Ro center). MediaConvert uses this value for downmixing. Default value: -3 dB. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, and -6.0. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Left only/Right only center.

LoRoSurroundMixLevel -> (double)

Specify a value for the following Dolby Atmos setting: Left only/Right only. MediaConvert uses this value for downmixing. Default value: -3 dB. Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Left only/Right only surround.

LtRtCenterMixLevel -> (double)

Specify a value for the following Dolby Atmos setting: Left total/Right total center mix (Lt/Rt center). MediaConvert uses this value for downmixing. Default value: -3 dB Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, and -6.0. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Left total/Right total center.

LtRtSurroundMixLevel -> (double)

Specify a value for the following Dolby Atmos setting: Left total/Right total surround mix (Lt/Rt surround). MediaConvert uses this value for downmixing. Default value: -3 dB Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. Related setting: How the service uses this value depends on the value that you choose for Stereo downmix. Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, the service ignores Left total/Right total surround.

MeteringMode -> (string)

Choose how the service meters the loudness of your audio.

SampleRate -> (integer)

This value is always 48000. It represents the sample rate in Hz.

SpeechThreshold -> (integer)

Specify the percentage of audio content, from 0% to 100%, that must be speech in order for the encoder to use the measured speech loudness as the overall program loudness. Default value: 15%

StereoDownmix -> (string)

Choose how the service does stereo downmixing. Default value: Not indicated Related setting: To have MediaConvert use this value, keep the default value, Custom for the setting Downmix control. Otherwise, MediaConvert ignores Stereo downmix.

SurroundExMode -> (string)

Specify whether your input audio has an additional center rear surround channel matrix encoded into your left and right surround channels.

Eac3Settings -> (structure)

Required when you set Codec to the value EAC3.

AttenuationControl -> (string)

If set to ATTENUATE_3_DB, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode.

Bitrate -> (integer)

Specify the average bitrate in bits per second. The bitrate that you specify must be a multiple of 8000 within the allowed minimum and maximum values. Leave blank to use the default bitrate for the coding mode you select according ETSI TS 102 366. Valid bitrates for coding mode 1/0: Default: 96000. Minimum: 32000. Maximum: 3024000. Valid bitrates for coding mode 2/0: Default: 192000. Minimum: 96000. Maximum: 3024000. Valid bitrates for coding mode 3/2: Default: 384000. Minimum: 192000. Maximum: 3024000.

BitstreamMode -> (string)

Specify the bitstream mode for the E-AC-3 stream that the encoder emits. For more information about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E).

CodingMode -> (string)

Dolby Digital Plus coding mode. Determines number of channels.

DcFilter -> (string)

Activates a DC highpass filter for all input channels.

Dialnorm -> (integer)

Sets the dialnorm for the output. If blank and input audio is Dolby Digital Plus, dialnorm will be passed through.

DynamicRangeCompressionLine -> (string)

Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the line operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at [https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf](https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf).

DynamicRangeCompressionRf -> (string)

Choose the Dolby Digital dynamic range control (DRC) profile that MediaConvert uses when encoding the metadata in the Dolby Digital stream for the RF operating mode. Related setting: When you use this setting, MediaConvert ignores any value you provide for Dynamic range compression profile. For information about the Dolby Digital DRC operating modes and profiles, see the Dynamic Range Control chapter of the Dolby Metadata Guide at [https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf](https://developer.dolby.com/globalassets/professional/documents/dolby-metadata-guide.pdf).

LfeControl -> (string)

When encoding 3/2 audio, controls whether the LFE channel is enabled

LfeFilter -> (string)

Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3_2_LFE coding mode.

LoRoCenterMixLevel -> (double)

Specify a value for the following Dolby Digital Plus setting: Left only/Right only center mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left only/Right only center.

LoRoSurroundMixLevel -> (double)

Specify a value for the following Dolby Digital Plus setting: Left only/Right only. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left only/Right only surround.

LtRtCenterMixLevel -> (double)

Specify a value for the following Dolby Digital Plus setting: Left total/Right total center mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left total/Right total center.

LtRtSurroundMixLevel -> (double)

Specify a value for the following Dolby Digital Plus setting: Left total/Right total surround mix. MediaConvert uses this value for downmixing. How the service uses this value depends on the value that you choose for Stereo downmix. Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel. This setting applies only if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Left total/Right total surround.

MetadataControl -> (string)

When set to FOLLOW_INPUT, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.

PassthroughControl -> (string)

When set to WHEN_POSSIBLE, input DD+ audio will be passed through if it is present on the input. this detection is dynamic over the life of the transcode. Inputs that alternate between DD+ and non-DD+ content will have a consistent DD+ output as the system alternates between passthrough and encoding.

PhaseControl -> (string)

Controls the amount of phase-shift applied to the surround channels. Only used for 3/2 coding mode.

SampleRate -> (integer)

This value is always 48000. It represents the sample rate in Hz.

StereoDownmix -> (string)

Choose how the service does stereo downmixing. This setting only applies if you keep the default value of 3/2 - L, R, C, Ls, Rs for the setting Coding mode. If you choose a different value for Coding mode, the service ignores Stereo downmix.

SurroundExMode -> (string)

When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels.

SurroundMode -> (string)

When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels.

FlacSettings -> (structure)

Required when you set Codec, under AudioDescriptions>CodecSettings, to the value FLAC.

BitDepth -> (integer)

Specify Bit depth (BitDepth), in bits per sample, to choose the encoding quality for this audio track.

Channels -> (integer)

Specify the number of channels in this output audio track. Choosing Mono on the console gives you 1 output channel; choosing Stereo gives you 2. In the API, valid values are between 1 and 8.

SampleRate -> (integer)

Sample rate in Hz.

Mp2Settings -> (structure)

Required when you set Codec to the value MP2.

Bitrate -> (integer)

Specify the average bitrate in bits per second.

Channels -> (integer)

Set Channels to specify the number of channels in this output audio track. Choosing Mono in will give you 1 output channel; choosing Stereo will give you 2. In the API, valid values are 1 and 2.

SampleRate -> (integer)

Sample rate in Hz.

Mp3Settings -> (structure)

Required when you set Codec, under AudioDescriptions>CodecSettings, to the value MP3.

Bitrate -> (integer)

Specify the average bitrate in bits per second.

Channels -> (integer)

Specify the number of channels in this output audio track. Choosing Mono gives you 1 output channel; choosing Stereo gives you 2. In the API, valid values are 1 and 2.

RateControlMode -> (string)

Specify whether the service encodes this MP3 audio output with a constant bitrate (CBR) or a variable bitrate (VBR).

SampleRate -> (integer)

Sample rate in Hz.

VbrQuality -> (integer)

Required when you set Bitrate control mode to VBR. Specify the audio quality of this MP3 output from 0 (highest quality) to 9 (lowest quality).

OpusSettings -> (structure)

Required when you set Codec, under AudioDescriptions>CodecSettings, to the value OPUS.

Bitrate -> (integer)

Optional. Specify the average bitrate in bits per second. Valid values are multiples of 8000, from 32000 through 192000. The default value is 96000, which we recommend for quality and bandwidth.

Channels -> (integer)

Specify the number of channels in this output audio track. Choosing Mono on gives you 1 output channel; choosing Stereo gives you 2. In the API, valid values are 1 and 2.

SampleRate -> (integer)

Optional. Sample rate in Hz. Valid values are 16000, 24000, and 48000. The default value is 48000.

VorbisSettings -> (structure)

Required when you set Codec, under AudioDescriptions>CodecSettings, to the value Vorbis.

Channels -> (integer)

Optional. Specify the number of channels in this output audio track. Choosing Mono on the console gives you 1 output channel; choosing Stereo gives you 2. In the API, valid values are 1 and 2. The default value is 2.

SampleRate -> (integer)

Optional. Specify the audio sample rate in Hz. Valid values are 22050, 32000, 44100, and 48000. The default value is 48000.

VbrQuality -> (integer)

Optional. Specify the variable audio quality of this Vorbis output from -1 (lowest quality, ~45 kbit/s) to 10 (highest quality, ~500 kbit/s). The default value is 4 (~128 kbit/s). Values 5 and 6 are approximately 160 and 192 kbit/s, respectively.

WavSettings -> (structure)

Required when you set Codec to the value WAV.

BitDepth -> (integer)

Specify Bit depth, in bits per sample, to choose the encoding quality for this audio track.

Channels -> (integer)

Specify the number of channels in this output audio track. Valid values are 1 and even numbers up to 64. For example, 1, 2, 4, 6, and so on, up to 64.

Format -> (string)

Specify the file format for your wave audio output. To use a RIFF wave format: Keep the default value, RIFF. If your output audio is likely to exceed 4GB in file size, or if you otherwise need the extended support of the RF64 format: Choose RF64. If your player only supports the extensible wave format: Choose Extensible.

SampleRate -> (integer)

Sample rate in Hz.

CustomLanguageCode -> (string)

Specify the language for this audio output track. The service puts this language code into your output audio track when you set Language code control to Use configured. The service also uses your specified custom language code when you set Language code control to Follow input, but your input file doesnât specify a language code. For all outputs, you can use an ISO 639-2 or ISO 639-3 code. For streaming outputs, you can also use any other code in the full RFC-5646 specification. Streaming outputs are those that are in one of the following output groups: CMAF, DASH ISO, Apple HLS, or Microsoft Smooth Streaming.

LanguageCode -> (string)

Indicates the language of the audio output track. The ISO 639 language specified in the âLanguage Codeâ drop down will be used when âFollow Input Language Codeâ is not selected or when âFollow Input Language Codeâ is selected but there is no ISO 639 language code specified by the input.

LanguageCodeControl -> (string)

Specify which source for language code takes precedence for this audio track. When you choose Follow input, the service uses the language code from the input track if itâs present. If thereâs no languge code on the input track, the service uses the code that you specify in the setting Language code. When you choose Use configured, the service uses the language code that you specify.

RemixSettings -> (structure)

Advanced audio remixing settings.

AudioDescriptionAudioChannel -> (integer)

Optionally specify the channel in your input that contains your audio description audio signal. MediaConvert mixes your audio signal across all output channels, while reducing their volume according to your data stream. When you specify an audio description audio channel, you must also specify an audio description data channel. For more information about audio description signals, see the BBC WHP 198 and 051 white papers.

AudioDescriptionDataChannel -> (integer)

Optionally specify the channel in your input that contains your audio description data stream. MediaConvert mixes your audio signal across all output channels, while reducing their volume according to your data stream. When you specify an audio description data channel, you must also specify an audio description audio channel. For more information about audio description signals, see the BBC WHP 198 and 051 white papers.

ChannelMapping -> (structure)

Channel mapping contains the group of fields that hold the remixing value for each channel, in dB. Specify remix values to indicate how much of the content from your input audio channel you want in your output audio channels. Each instance of the InputChannels or InputChannelsFineTune array specifies these values for one output channel. Use one instance of this array for each output channel. In the console, each array corresponds to a column in the graphical depiction of the mapping matrix. The rows of the graphical matrix correspond to input channels. Valid values are within the range from -60 (mute) through 6. A setting of 0 passes the input channel unchanged to the output channel (no attenuation or amplification). Use InputChannels or InputChannelsFineTune to specify your remix values. Donât use both.

OutputChannels -> (list)

In your JSON job specification, include one child of OutputChannels for each audio channel that you want in your output. Each child should contain one instance of InputChannels or InputChannelsFineTune.

(structure)

OutputChannel mapping settings.

InputChannels -> (list)

Use this setting to specify your remix values when they are integers, such as -10, 0, or 4.

(integer)

InputChannelsFineTune -> (list)

Use this setting to specify your remix values when they have a decimal component, such as -10.312, 0.08, or 4.9. MediaConvert rounds your remixing values to the nearest thousandth.

(double)

ChannelsIn -> (integer)

Specify the number of audio channels from your input that you want to use in your output. With remixing, you might combine or split the data in these channels, so the number of channels in your final output might be different. If you are doing both input channel mapping and output channel mapping, the number of output channels in your input mapping must be the same as the number of input channels in your output mapping.

ChannelsOut -> (integer)

Specify the number of channels in this output after remixing. Valid values: 1, 2, 4, 6, 8â¦ 64. (1 and even numbers to 64.) If you are doing both input channel mapping and output channel mapping, the number of output channels in your input mapping must be the same as the number of input channels in your output mapping.

StreamName -> (string)

Specify a label for this output audio stream. For example, âEnglishâ, âDirector commentaryâ, or âtrack_2â. For streaming outputs, MediaConvert passes this information into destination manifests for display on the end-viewerâs player device. For outputs in other output groups, the service ignores this setting.

CaptionDescriptions -> (list)

Contains groups of captions settings. For each output that has captions, include one instance of CaptionDescriptions. Can contain multiple groups of captions settings.

(structure)

This object holds groups of settings related to captions for one output. For each output that has captions, include one instance of CaptionDescriptions.

CaptionSelectorName -> (string)

Specifies which âCaption Selectorâ:#inputs-caption_selector to use from each input when generating captions. The name should be of the format âCaption Selector â, which denotes that the Nth Caption Selector will be used from each input.

CustomLanguageCode -> (string)

Specify the language for this captions output track. For most captions output formats, the encoder puts this language information in the output captions metadata. If your output captions format is DVB-Sub or Burn in, the encoder uses this language information when automatically selecting the font script for rendering the captions text. For all outputs, you can use an ISO 639-2 or ISO 639-3 code. For streaming outputs, you can also use any other code in the full RFC-5646 specification. Streaming outputs are those that are in one of the following output groups: CMAF, DASH ISO, Apple HLS, or Microsoft Smooth Streaming.

DestinationSettings -> (structure)

Settings related to one captions tab on the MediaConvert console. Usually, one captions tab corresponds to one output captions track. Depending on your output captions format, one tab might correspond to a set of output captions tracks. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/including-captions.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/including-captions.html).

BurninDestinationSettings -> (structure)

Burn-in is a captions delivery method, rather than a captions format. Burn-in writes the captions directly on your video frames, replacing pixels of video content with the captions. Set up burn-in captions in the same output as your video. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/burn-in-output-captions.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/burn-in-output-captions.html).

Alignment -> (string)

Specify the alignment of your captions. If no explicit x_position is provided, setting alignment to centered will placethe captions at the bottom center of the output. Similarly, setting a left alignment willalign captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates.

ApplyFontColor -> (string)

Ignore this setting unless Style passthrough is set to Enabled and Font color set to Black, Yellow, Red, Green, Blue, or Hex. Use Apply font color for additional font color controls. When you choose White text only, or leave blank, your font color setting only applies to white text in your input captions. For example, if your font color setting is Yellow, and your input captions have red and white text, your output captions will have red and yellow text. When you choose ALL_TEXT, your font color setting applies to all of your output captions text.

BackgroundColor -> (string)

Specify the color of the rectangle behind the captions. Leave background color blank and set Style passthrough to enabled to use the background color data from your input captions, if present.

BackgroundOpacity -> (integer)

Specify the opacity of the background rectangle. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to enabled, leave blank to pass through the background style information in your input captions to your output captions. If Style passthrough is set to disabled, leave blank to use a value of 0 and remove all backgrounds from your output captions.

FallbackFont -> (string)

Specify the font that you want the service to use for your burn in captions when your input captions specify a font that MediaConvert doesnât support. When you set Fallback font to best match, or leave blank, MediaConvert uses a supported font that most closely matches the font that your input captions specify. When there are multiple unsupported fonts in your input captions, MediaConvert matches each font with the supported font that matches best. When you explicitly choose a replacement font, MediaConvert uses that font to replace all unsupported fonts from your input.

FontColor -> (string)

Specify the color of the burned-in captions text. Leave Font color blank and set Style passthrough to enabled to use the font color data from your input captions, if present.

FontFileBold -> (string)

Specify a bold TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, an italic, and a bold italic font file.

FontFileBoldItalic -> (string)

Specify a bold italic TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, a bold, and an italic font file.

FontFileItalic -> (string)

Specify an italic TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, a bold, and a bold italic font file.

FontFileRegular -> (string)

Specify a regular TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a bold, an italic, and a bold italic font file.

FontOpacity -> (integer)

Specify the opacity of the burned-in captions. 255 is opaque; 0 is transparent.

FontResolution -> (integer)

Specify the Font resolution in DPI (dots per inch).

FontScript -> (string)

Set Font script to Automatically determined, or leave blank, to automatically determine the font script in your input captions. Otherwise, set to Simplified Chinese (HANS) or Traditional Chinese (HANT) if your input font script uses Simplified or Traditional Chinese.

FontSize -> (integer)

Specify the Font size in pixels. Must be a positive integer. Set to 0, or leave blank, for automatic font size.

HexFontColor -> (string)

Ignore this setting unless your Font color is set to Hex. Enter either six or eight hexidecimal digits, representing red, green, and blue, with two optional extra digits for alpha. For example a value of 1122AABB is a red value of 0x11, a green value of 0x22, a blue value of 0xAA, and an alpha value of 0xBB.

OutlineColor -> (string)

Specify font outline color. Leave Outline color blank and set Style passthrough to enabled to use the font outline color data from your input captions, if present.

OutlineSize -> (integer)

Specify the Outline size of the caption text, in pixels. Leave Outline size blank and set Style passthrough to enabled to use the outline size data from your input captions, if present.

RemoveRubyReserveAttributes -> (string)

Optionally remove any tts:rubyReserve attributes present in your input, that do not have a tts:ruby attribute in the same element, from your output. Use if your vertical Japanese output captions have alignment issues. To remove ruby reserve attributes when present: Choose Enabled. To not remove any ruby reserve attributes: Keep the default value, Disabled.

ShadowColor -> (string)

Specify the color of the shadow cast by the captions. Leave Shadow color blank and set Style passthrough to enabled to use the shadow color data from your input captions, if present.

ShadowOpacity -> (integer)

Specify the opacity of the shadow. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to Enabled, leave Shadow opacity blank to pass through the shadow style information in your input captions to your output captions. If Style passthrough is set to disabled, leave blank to use a value of 0 and remove all shadows from your output captions.

ShadowXOffset -> (integer)

Specify the horizontal offset of the shadow, relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left.

ShadowYOffset -> (integer)

Specify the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. Leave Shadow y-offset blank and set Style passthrough to enabled to use the shadow y-offset data from your input captions, if present.

StylePassthrough -> (string)

To use the available style, color, and position information from your input captions: Set Style passthrough to Enabled. Note that MediaConvert uses default settings for any missing style or position information in your input captions To ignore the style and position information from your input captions and use default settings: Leave blank or keep the default value, Disabled. Default settings include white text with black outlining, bottom-center positioning, and automatic sizing. Whether you set Style passthrough to enabled or not, you can also choose to manually override any of the individual style and position settings. You can also override any fonts by manually specifying custom font files.

TeletextSpacing -> (string)

Specify whether the text spacing in your captions is set by the captions grid, or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read for closed captions.

XPosition -> (integer)

Specify the horizontal position of the captions, relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit x_position is provided, the horizontal caption position will be determined by the alignment parameter.

YPosition -> (integer)

Specify the vertical position of the captions, relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit y_position is provided, the caption will be positioned towards the bottom of the output.

DestinationType -> (string)

Specify the format for this set of captions on this output. The default format is embedded without SCTE-20. Note that your choice of video output container constrains your choice of output captions format. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/captions-support-tables.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/captions-support-tables.html). If you are using SCTE-20 and you want to create an output that complies with the SCTE-43 spec, choose SCTE-20 plus embedded. To create a non-compliant output where the embedded captions come first, choose Embedded plus SCTE-20.

DvbSubDestinationSettings -> (structure)

Settings related to DVB-Sub captions. Set up DVB-Sub captions in the same output as your video. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/dvb-sub-output-captions.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/dvb-sub-output-captions.html).

Alignment -> (string)

Specify the alignment of your captions. If no explicit x_position is provided, setting alignment to centered will placethe captions at the bottom center of the output. Similarly, setting a left alignment willalign captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Within your job settings, all of your DVB-Sub settings must be identical.

ApplyFontColor -> (string)

Ignore this setting unless Style Passthrough is set to Enabled and Font color set to Black, Yellow, Red, Green, Blue, or Hex. Use Apply font color for additional font color controls. When you choose White text only, or leave blank, your font color setting only applies to white text in your input captions. For example, if your font color setting is Yellow, and your input captions have red and white text, your output captions will have red and yellow text. When you choose ALL_TEXT, your font color setting applies to all of your output captions text.

BackgroundColor -> (string)

Specify the color of the rectangle behind the captions. Leave background color blank and set Style passthrough to enabled to use the background color data from your input captions, if present.

BackgroundOpacity -> (integer)

Specify the opacity of the background rectangle. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to enabled, leave blank to pass through the background style information in your input captions to your output captions. If Style passthrough is set to disabled, leave blank to use a value of 0 and remove all backgrounds from your output captions. Within your job settings, all of your DVB-Sub settings must be identical.

DdsHandling -> (string)

Specify how MediaConvert handles the display definition segment (DDS). To exclude the DDS from this set of captions: Keep the default, None. To include the DDS: Choose Specified. When you do, also specify the offset coordinates of the display window with DDS x-coordinate and DDS y-coordinate. To include the DDS, but not include display window data: Choose No display window. When you do, you can write position metadata to the page composition segment (PCS) with DDS x-coordinate and DDS y-coordinate. For video resolutions with a height of 576 pixels or less, MediaConvert doesnât include the DDS, regardless of the value you choose for DDS handling. All burn-in and DVB-Sub font settings must match.

DdsXCoordinate -> (integer)

Use this setting, along with DDS y-coordinate, to specify the upper left corner of the display definition segment (DDS) display window. With this setting, specify the distance, in pixels, between the left side of the frame and the left side of the DDS display window. Keep the default value, 0, to have MediaConvert automatically choose this offset. Related setting: When you use this setting, you must set DDS handling to a value other than None. MediaConvert uses these values to determine whether to write page position data to the DDS or to the page composition segment. All burn-in and DVB-Sub font settings must match.

DdsYCoordinate -> (integer)

Use this setting, along with DDS x-coordinate, to specify the upper left corner of the display definition segment (DDS) display window. With this setting, specify the distance, in pixels, between the top of the frame and the top of the DDS display window. Keep the default value, 0, to have MediaConvert automatically choose this offset. Related setting: When you use this setting, you must set DDS handling to a value other than None. MediaConvert uses these values to determine whether to write page position data to the DDS or to the page composition segment (PCS). All burn-in and DVB-Sub font settings must match.

FallbackFont -> (string)

Specify the font that you want the service to use for your burn in captions when your input captions specify a font that MediaConvert doesnât support. When you set Fallback font to best match, or leave blank, MediaConvert uses a supported font that most closely matches the font that your input captions specify. When there are multiple unsupported fonts in your input captions, MediaConvert matches each font with the supported font that matches best. When you explicitly choose a replacement font, MediaConvert uses that font to replace all unsupported fonts from your input.

FontColor -> (string)

Specify the color of the captions text. Leave Font color blank and set Style passthrough to enabled to use the font color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical.

FontFileBold -> (string)

Specify a bold TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, an italic, and a bold italic font file.

FontFileBoldItalic -> (string)

Specify a bold italic TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, a bold, and an italic font file.

FontFileItalic -> (string)

Specify an italic TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a regular, a bold, and a bold italic font file.

FontFileRegular -> (string)

Specify a regular TrueType font file to use when rendering your output captions. Enter an S3, HTTP, or HTTPS URL. When you do, you must also separately specify a bold, an italic, and a bold italic font file.

FontOpacity -> (integer)

Specify the opacity of the burned-in captions. 255 is opaque; 0 is transparent. Within your job settings, all of your DVB-Sub settings must be identical.

FontResolution -> (integer)

Specify the Font resolution in DPI (dots per inch). Within your job settings, all of your DVB-Sub settings must be identical.

FontScript -> (string)

Set Font script to Automatically determined, or leave blank, to automatically determine the font script in your input captions. Otherwise, set to Simplified Chinese (HANS) or Traditional Chinese (HANT) if your input font script uses Simplified or Traditional Chinese. Within your job settings, all of your DVB-Sub settings must be identical.

FontSize -> (integer)

Specify the Font size in pixels. Must be a positive integer. Set to 0, or leave blank, for automatic font size. Within your job settings, all of your DVB-Sub settings must be identical.

Height -> (integer)

Specify the height, in pixels, of this set of DVB-Sub captions. The default value is 576 pixels. Related setting: When you use this setting, you must set DDS handling to a value other than None. All burn-in and DVB-Sub font settings must match.

HexFontColor -> (string)

Ignore this setting unless your Font color is set to Hex. Enter either six or eight hexidecimal digits, representing red, green, and blue, with two optional extra digits for alpha. For example a value of 1122AABB is a red value of 0x11, a green value of 0x22, a blue value of 0xAA, and an alpha value of 0xBB.

OutlineColor -> (string)

Specify font outline color. Leave Outline color blank and set Style passthrough to enabled to use the font outline color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical.

OutlineSize -> (integer)

Specify the Outline size of the caption text, in pixels. Leave Outline size blank and set Style passthrough to enabled to use the outline size data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical.

ShadowColor -> (string)

Specify the color of the shadow cast by the captions. Leave Shadow color blank and set Style passthrough to enabled to use the shadow color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical.

ShadowOpacity -> (integer)

Specify the opacity of the shadow. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to Enabled, leave Shadow opacity blank to pass through the shadow style information in your input captions to your output captions. If Style passthrough is set to disabled, leave blank to use a value of 0 and remove all shadows from your output captions. Within your job settings, all of your DVB-Sub settings must be identical.

ShadowXOffset -> (integer)

Specify the horizontal offset of the shadow, relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. Within your job settings, all of your DVB-Sub settings must be identical.

ShadowYOffset -> (integer)

Specify the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. Leave Shadow y-offset blank and set Style passthrough to enabled to use the shadow y-offset data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical.

StylePassthrough -> (string)

To use the available style, color, and position information from your input captions: Set Style passthrough to Enabled. Note that MediaConvert uses default settings for any missing style or position information in your input captions To ignore the style and position information from your input captions and use default settings: Leave blank or keep the default value, Disabled. Default settings include white text with black outlining, bottom-center positioning, and automatic sizing. Whether you set Style passthrough to enabled or not, you can also choose to manually override any of the individual style and position settings. You can also override any fonts by manually specifying custom font files.

SubtitlingType -> (string)

Specify whether your DVB subtitles are standard or for hearing impaired. Choose hearing impaired if your subtitles include audio descriptions and dialogue. Choose standard if your subtitles include only dialogue.

TeletextSpacing -> (string)

Specify whether the Text spacing in your captions is set by the captions grid, or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read for closed captions. Within your job settings, all of your DVB-Sub settings must be identical.

Width -> (integer)

Specify the width, in pixels, of this set of DVB-Sub captions. The default value is 720 pixels. Related setting: When you use this setting, you must set DDS handling to a value other than None. All burn-in and DVB-Sub font settings must match.

XPosition -> (integer)

Specify the horizontal position of the captions, relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit x_position is provided, the horizontal caption position will be determined by the alignment parameter. Within your job settings, all of your DVB-Sub settings must be identical.

YPosition -> (integer)

Specify the vertical position of the captions, relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit y_position is provided, the caption will be positioned towards the bottom of the output. Within your job settings, all of your DVB-Sub settings must be identical.

EmbeddedDestinationSettings -> (structure)

Settings related to CEA/EIA-608 and CEA/EIA-708 (also called embedded or ancillary) captions. Set up embedded captions in the same output as your video. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/embedded-output-captions.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/embedded-output-captions.html).

Destination608ChannelNumber -> (integer)

Ignore this setting unless your input captions are SCC format and your output captions are embedded in the video stream. Specify a CC number for each captions channel in this output. If you have two channels, choose CC numbers that arenât in the same field. For example, choose 1 and 3. For more information, see [https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded](https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded).

Destination708ServiceNumber -> (integer)

Ignore this setting unless your input captions are SCC format and you want both 608 and 708 captions embedded in your output stream. Optionally, specify the 708 service number for each output captions channel. Choose a different number for each channel. To use this setting, also set Force 608 to 708 upconvert to Upconvert in your input captions selector settings. If you choose to upconvert but donât specify a 708 service number, MediaConvert uses the number that you specify for CC channel number for the 708 service number. For more information, see [https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded](https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded).

ImscDestinationSettings -> (structure)

Settings related to IMSC captions. IMSC is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html).

Accessibility -> (string)

If the IMSC captions track is intended to provide accessibility for people who are deaf or hard of hearing: Set Accessibility subtitles to Enabled. When you do, MediaConvert adds accessibility attributes to your output HLS or DASH manifest. For HLS manifests, MediaConvert adds the following accessibility attributes under EXT-X-MEDIA for this track: CHARACTERISTICS=âpublic.accessibility.describes-spoken-dialog,public.accessibility.describes-music-and-soundâ and AUTOSELECT=âYESâ. For DASH manifests, MediaConvert adds the following in the adaptation set for this track: . If the captions track is not intended to provide such accessibility: Keep the default value, Disabled. When you do, for DASH manifests, MediaConvert instead adds the following in the adaptation set for this track: .

StylePassthrough -> (string)

Keep this setting enabled to have MediaConvert use the font style and position information from the captions source in the output. This option is available only when your input captions are IMSC, SMPTE-TT, or TTML. Disable this setting for simplified output captions.

SccDestinationSettings -> (structure)

Settings related to SCC captions. SCC is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/scc-srt-output-captions.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/scc-srt-output-captions.html).

Framerate -> (string)

Set Framerate to make sure that the captions and the video are synchronized in the output. Specify a frame rate that matches the frame rate of the associated video. If the video frame rate is 29.97, choose 29.97 dropframe only if the video has video_insertion=true and drop_frame_timecode=true; otherwise, choose 29.97 non-dropframe.

SrtDestinationSettings -> (structure)

Settings related to SRT captions. SRT is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video.

StylePassthrough -> (string)

Set Style passthrough to ENABLED to use the available style, color, and position information from your input captions. MediaConvert uses default settings for any missing style and position information in your input captions. Set Style passthrough to DISABLED, or leave blank, to ignore the style and position information from your input captions and use simplified output captions.

TeletextDestinationSettings -> (structure)

Settings related to teletext captions. Set up teletext captions in the same output as your video. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/teletext-output-captions.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/teletext-output-captions.html).

PageNumber -> (string)

Set pageNumber to the Teletext page number for the destination captions for this output. This value must be a three-digit hexadecimal string; strings ending in -FF are invalid. If you are passing through the entire set of Teletext data, do not use this field.

PageTypes -> (list)

Specify the page types for this Teletext page. If you donât specify a value here, the service sets the page type to the default value Subtitle. If you pass through the entire set of Teletext data, donât use this field. When you pass through a set of Teletext pages, your output has the same page types as your input.

(string)

A page type as defined in the standard ETSI EN 300 468, Table 94

TtmlDestinationSettings -> (structure)

Settings related to TTML captions. TTML is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html).

StylePassthrough -> (string)

Pass through style and position information from a TTML-like input source (TTML, IMSC, SMPTE-TT) to the TTML output.

WebvttDestinationSettings -> (structure)

Settings related to WebVTT captions. WebVTT is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html).

Accessibility -> (string)

If the WebVTT captions track is intended to provide accessibility for people who are deaf or hard of hearing: Set Accessibility subtitles to Enabled. When you do, MediaConvert adds accessibility attributes to your output HLS or DASH manifest. For HLS manifests, MediaConvert adds the following accessibility attributes under EXT-X-MEDIA for this track: CHARACTERISTICS=âpublic.accessibility.describes-spoken-dialog,public.accessibility.describes-music-and-soundâ and AUTOSELECT=âYESâ. For DASH manifests, MediaConvert adds the following in the adaptation set for this track: . If the captions track is not intended to provide such accessibility: Keep the default value, Disabled. When you do, for DASH manifests, MediaConvert instead adds the following in the adaptation set for this track: .

StylePassthrough -> (string)

Specify how MediaConvert writes style information in your output WebVTT captions. To use the available style, color, and position information from your input captions: Choose Enabled. MediaConvert uses default settings when style and position information is missing from your input captions. To recreate the input captions exactly: Choose Strict. MediaConvert automatically applies timing adjustments, including adjustments for frame rate conversion, ad avails, and input clipping. Your input captions format must be WebVTT. To ignore the style and position information from your input captions and use simplified output captions: Keep the default value, Disabled. Or leave blank. To use the available style, color, and position information from your input captions, while merging cues with identical time ranges: Choose merge. This setting can help prevent positioning overlaps for certain players that expect a single single cue for any given time range.

LanguageCode -> (string)

Specify the language of this captions output track. For most captions output formats, the encoder puts this language information in the output captions metadata. If your output captions format is DVB-Sub or Burn in, the encoder uses this language information to choose the font language for rendering the captions text.

LanguageDescription -> (string)

Specify a label for this set of output captions. For example, âEnglishâ, âDirector commentaryâ, or âtrack_2â. For streaming outputs, MediaConvert passes this information into destination manifests for display on the end-viewerâs player device. For outputs in other output groups, the service ignores this setting.

ContainerSettings -> (structure)

Container specific settings.

CmfcSettings -> (structure)

These settings relate to the fragmented MP4 container for the segments in your CMAF outputs.

AudioDuration -> (string)

Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec.

AudioGroupId -> (string)

Specify the audio rendition group for this audio rendition. Specify up to one value for each audio output in your output group. This value appears in your HLS parent manifest in the EXT-X-MEDIA tag of TYPE=AUDIO, as the value for the GROUP-ID attribute. For example, if you specify âaudio_aac_1â for Audio group ID, it appears in your manifest like this: #EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID=âaudio_aac_1â. Related setting: To associate the rendition group that this audio track belongs to with a video rendition, include the same value that you provide here for that video outputâs setting Audio rendition sets.

AudioRenditionSets -> (string)

List the audio rendition groups that you want included with this video rendition. Use a comma-separated list. For example, say you want to include the audio rendition groups that have the audio group IDs âaudio_aac_1â and âaudio_dolbyâ. Then you would specify this value: âaudio_aac_1,audio_dolbyâ. Related setting: The rendition groups that you include in your comma-separated list should all match values that you specify in the setting Audio group ID for audio renditions in the same output group as this video rendition. Default behavior: If you donât specify anything here and for Audio group ID, MediaConvert puts each audio variant in its own audio rendition group and associates it with every video variant. Each value in your list appears in your HLS parent manifest in the EXT-X-STREAM-INF tag as the value for the AUDIO attribute. To continue the previous example, say that the file name for the child manifest for your video rendition is âamazing_video_1.m3u8â. Then, in your parent manifest, each value will appear on separate lines, like this: #EXT-X-STREAM-INF:AUDIO=âaudio_aac_1ââ¦ amazing_video_1.m3u8 #EXT-X-STREAM-INF:AUDIO=âaudio_dolbyââ¦ amazing_video_1.m3u8

AudioTrackType -> (string)

Use this setting to control the values that MediaConvert puts in your HLS parent playlist to control how the client player selects which audio track to play. Choose Audio-only variant stream (AUDIO_ONLY_VARIANT_STREAM) for any variant that you want to prohibit the client from playing with video. This causes MediaConvert to represent the variant as an EXT-X-STREAM-INF in the HLS manifest. The other options for this setting determine the values that MediaConvert writes for the DEFAULT and AUTOSELECT attributes of the EXT-X-MEDIA entry for the audio variant. For more information about these attributes, see the Apple documentation article [https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/adding_alternate_media_to_a_playlist](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/adding_alternate_media_to_a_playlist). Choose Alternate audio, auto select, default to set DEFAULT=YES and AUTOSELECT=YES. Choose this value for only one variant in your output group. Choose Alternate audio, auto select, not default to set DEFAULT=NO and AUTOSELECT=YES. Choose Alternate Audio, Not Auto Select to set DEFAULT=NO and AUTOSELECT=NO. When you donât specify a value for this setting, MediaConvert defaults to Alternate audio, auto select, default. When there is more than one variant in your output group, you must explicitly choose a value for this setting.

DescriptiveVideoServiceFlag -> (string)

Specify whether to flag this audio track as descriptive video service (DVS) in your HLS parent manifest. When you choose Flag, MediaConvert includes the parameter CHARACTERISTICS=âpublic.accessibility.describes-videoâ in the EXT-X-MEDIA entry for this track. When you keep the default choice, Donât flag, MediaConvert leaves this parameter out. The DVS flag can help with accessibility on Apple devices. For more information, see the Apple documentation.

IFrameOnlyManifest -> (string)

Choose Include to have MediaConvert generate an HLS child manifest that lists only the I-frames for this rendition, in addition to your regular manifest for this rendition. You might use this manifest as part of a workflow that creates preview functions for your video. MediaConvert adds both the I-frame only child manifest and the regular child manifest to the parent manifest. When you donât need the I-frame only child manifest, keep the default value Exclude.

KlvMetadata -> (string)

To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and writes each instance to a separate event message box in the output, according to MISB ST1910.1. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank.

ManifestMetadataSignaling -> (string)

To add an InbandEventStream element in your output MPD manifest for each type of event message, set Manifest metadata signaling to Enabled. For ID3 event messages, the InbandEventStream element schemeIdUri will be same value that you specify for ID3 metadata scheme ID URI. For SCTE35 event messages, the InbandEventStream element schemeIdUri will be â[urn:scte:scte35:2013:bin](urn:scte:scte35:2013:bin)â. To leave these elements out of your output MPD manifest, set Manifest metadata signaling to Disabled. To enable Manifest metadata signaling, you must also set SCTE-35 source to Passthrough, ESAM SCTE-35 to insert, or ID3 metadata to Passthrough.

Scte35Esam -> (string)

Use this setting only when you specify SCTE-35 markers from ESAM. Choose INSERT to put SCTE-35 markers in this output at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML.

Scte35Source -> (string)

Ignore this setting unless you have SCTE-35 markers in your input video file. Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you donât want those SCTE-35 markers in this output.

TimedMetadata -> (string)

To include ID3 metadata in this output: Set ID3 metadata to Passthrough. Specify this ID3 metadata in Custom ID3 metadata inserter. MediaConvert writes each instance of ID3 metadata in a separate Event Message (eMSG) box. To exclude this ID3 metadata: Set ID3 metadata to None or leave blank.

TimedMetadataBoxVersion -> (string)

Specify the event message box (eMSG) version for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.3 Syntax. Leave blank to use the default value Version 0. When you specify Version 1, you must also set ID3 metadata to Passthrough.

TimedMetadataSchemeIdUri -> (string)

Specify the event message box (eMSG) scheme ID URI for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.4 Semantics. Leave blank to use the default value: [https://aomedia.org/emsg/ID3](https://aomedia.org/emsg/ID3) When you specify a value for ID3 metadata scheme ID URI, you must also set ID3 metadata to Passthrough.

TimedMetadataValue -> (string)

Specify the event message box (eMSG) value for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.4 Semantics. When you specify a value for ID3 Metadata Value, you must also set ID3 metadata to Passthrough.

Container -> (string)

Container for this output. Some containers require a container settings object. If not specified, the default object will be created.

F4vSettings -> (structure)

Settings for F4v container

MoovPlacement -> (string)

To place the MOOV atom at the beginning of your output, which is useful for progressive downloading: Leave blank or choose Progressive download. To place the MOOV at the end of your output: Choose Normal.

M2tsSettings -> (structure)

MPEG-2 TS container settings. These apply to outputs in a File output group when the outputâs container is MPEG-2 Transport Stream (M2TS). In these assets, data is organized by the program map table (PMT). Each transport stream program contains subsets of data, including audio, video, and metadata. Each of these subsets of data has a numerical label called a packet identifier (PID). Each transport stream program corresponds to one MediaConvert output. The PMT lists the types of data in a program along with their PID. Downstream systems and players use the program map table to look up the PID for each type of data it accesses and then uses the PIDs to locate specific data within the asset.

AudioBufferModel -> (string)

Selects between the DVB and ATSC buffer models for Dolby Digital audio.

AudioDuration -> (string)

Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec.

AudioFramesPerPes -> (integer)

The number of audio frames to insert for each PES packet.

AudioPids -> (list)

Specify the packet identifiers (PIDs) for any elementary audio streams you include in this output. Specify multiple PIDs as a JSON array. Default is the range 482-492.

(integer)

AudioPtsOffsetDelta -> (integer)

Manually specify the difference in PTS offset that will be applied to the audio track, in seconds or milliseconds, when you set PTS offset to Seconds or Milliseconds. Enter an integer from -10000 to 10000. Leave blank to keep the default value 0.

Bitrate -> (integer)

Specify the output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate. Other common values are 3750000, 7500000, and 15000000.

BufferModel -> (string)

Controls what buffer model to use for accurate interleaving. If set to MULTIPLEX, use multiplex buffer model. If set to NONE, this can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions.

DataPTSControl -> (string)

If you select ALIGN_TO_VIDEO, MediaConvert writes captions and data packets with Presentation Timestamp (PTS) values greater than or equal to the first video packet PTS (MediaConvert drops captions and data packets with lesser PTS values). Keep the default value to allow all PTS values.

DvbNitSettings -> (structure)

Use these settings to insert a DVB Network Information Table (NIT) in the transport stream of this output.

NetworkId -> (integer)

The numeric value placed in the Network Information Table (NIT).

NetworkName -> (string)

The network name text placed in the network_name_descriptor inside the Network Information Table. Maximum length is 256 characters.

NitInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream.

DvbSdtSettings -> (structure)

Use these settings to insert a DVB Service Description Table (SDT) in the transport stream of this output.

OutputSdt -> (string)

Selects method of inserting SDT information into output stream. âFollow input SDTâ copies SDT information from input stream to output stream. âFollow input SDT if presentâ copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. Enter âSDT Manuallyâ means user will enter the SDT information. âNo SDTâ means output stream will not contain SDT information.

SdtInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream.

ServiceName -> (string)

The service name placed in the service_descriptor in the Service Description Table. Maximum length is 256 characters.

ServiceProviderName -> (string)

The service provider name placed in the service_descriptor in the Service Description Table. Maximum length is 256 characters.

DvbSubPids -> (list)

Specify the packet identifiers (PIDs) for DVB subtitle data included in this output. Specify multiple PIDs as a JSON array. Default is the range 460-479.

(integer)

DvbTdtSettings -> (structure)

Use these settings to insert a DVB Time and Date Table (TDT) in the transport stream of this output.

TdtInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream.

DvbTeletextPid -> (integer)

Specify the packet identifier (PID) for DVB teletext data you include in this output. Default is 499.

EbpAudioInterval -> (string)

When set to VIDEO_AND_FIXED_INTERVALS, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. When set to VIDEO_INTERVAL, these additional markers will not be inserted. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP_LEGACY).

EbpPlacement -> (string)

Selects which PIDs to place EBP markers on. They can either be placed only on the video PID, or on both the video PID and all audio PIDs. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP_LEGACY).

EsRateInPes -> (string)

Controls whether to include the ES Rate field in the PES header.

ForceTsVideoEbpOrder -> (string)

Keep the default value unless you know that your audio EBP markers are incorrectly appearing before your video EBP markers. To correct this problem, set this value to Force.

FragmentTime -> (double)

The length, in seconds, of each fragment. Only used with EBP markers.

KlvMetadata -> (string)

To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and passes it through to the output transport stream. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank.

MaxPcrInterval -> (integer)

Specify the maximum time, in milliseconds, between Program Clock References (PCRs) inserted into the transport stream.

MinEbpInterval -> (integer)

When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is âstretchedâ to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate.

NielsenId3 -> (string)

If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.

NullPacketBitrate -> (double)

Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets.

PatInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream.

PcrControl -> (string)

When set to PCR_EVERY_PES_PACKET, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This is effective only when the PCR PID is the same as the video or audio elementary stream.

PcrPid -> (integer)

Specify the packet identifier (PID) for the program clock reference (PCR) in this output. If you do not specify a value, the service will use the value for Video PID.

PmtInterval -> (integer)

Specify the number of milliseconds between instances of the program map table (PMT) in the output transport stream.

PmtPid -> (integer)

Specify the packet identifier (PID) for the program map table (PMT) itself. Default is 480.

PreventBufferUnderflow -> (string)

Specify whether MediaConvert automatically attempts to prevent decoder buffer underflows in your transport stream output. Use if you are seeing decoder buffer underflows in your output and are unable to increase your transport streamâs bitrate. For most workflows: We recommend that you keep the default value, Disabled. To prevent decoder buffer underflows in your output, when possible: Choose Enabled. Note that if MediaConvert prevents a decoder buffer underflow in your output, output video quality is reduced and your job will take longer to complete.

PrivateMetadataPid -> (integer)

Specify the packet identifier (PID) of the private metadata stream. Default is 503.

ProgramNumber -> (integer)

Use Program number to specify the program number used in the program map table (PMT) for this output. Default is 1. Program numbers and program map tables are parts of MPEG-2 transport stream containers, used for organizing data.

PtsOffset -> (integer)

Manually specify the initial PTS offset, in seconds, when you set PTS offset to Seconds. Enter an integer from 0 to 3600. Leave blank to keep the default value 2.

PtsOffsetMode -> (string)

Specify the initial presentation timestamp (PTS) offset for your transport stream output. To let MediaConvert automatically determine the initial PTS offset: Keep the default value, Auto. We recommend that you choose Auto for the widest player compatibility. The initial PTS will be at least two seconds and vary depending on your outputâs bitrate, HRD buffer size and HRD buffer initial fill percentage. To manually specify an initial PTS offset: Choose Seconds or Milliseconds. Then specify the number of seconds or milliseconds with PTS offset.

RateMode -> (string)

When set to CBR, inserts null packets into transport stream to fill specified bitrate. When set to VBR, the bitrate setting acts as the maximum bitrate, but the output will not be padded up to that bitrate.

Scte35Esam -> (structure)

Include this in your job settings to put SCTE-35 markers in your HLS and transport stream outputs at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML.

Scte35EsamPid -> (integer)

Packet Identifier (PID) of the SCTE-35 stream in the transport stream generated by ESAM.

Scte35Pid -> (integer)

Specify the packet identifier (PID) of the SCTE-35 stream in the transport stream.

Scte35Source -> (string)

For SCTE-35 markers from your inputâ Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you donât want SCTE-35 markers in this output. For SCTE-35 markers from an ESAM XML documentâ Choose None. Also provide the ESAM XML as a string in the setting Signal processing notification XML. Also enable ESAM SCTE-35 (include the property scte35Esam).

SegmentationMarkers -> (string)

Inserts segmentation markers at each segmentation_time period. rai_segstart sets the Random Access Indicator bit in the adaptation field. rai_adapt sets the RAI bit and adds the current timecode in the private data bytes. psi_segstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebp_legacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.

SegmentationStyle -> (string)

The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of âreset_cadenceâ is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of of $segmentation_time seconds. When a segmentation style of âmaintain_cadenceâ is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentation_time seconds. Note that EBP lookahead is a slight exception to this rule.

SegmentationTime -> (double)

Specify the length, in seconds, of each segment. Required unless markers is set to _none_.

TimedMetadataPid -> (integer)

Packet Identifier (PID) of the ID3 metadata stream in the transport stream.

TransportStreamId -> (integer)

Specify the ID for the transport stream itself in the program map table for this output. Transport stream IDs and program map tables are parts of MPEG-2 transport stream containers, used for organizing data.

VideoPid -> (integer)

Specify the packet identifier (PID) of the elementary video stream in the transport stream.

M3u8Settings -> (structure)

These settings relate to the MPEG-2 transport stream (MPEG2-TS) container for the MPEG2-TS segments in your HLS outputs.

AudioDuration -> (string)

Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec.

AudioFramesPerPes -> (integer)

The number of audio frames to insert for each PES packet.

AudioPids -> (list)

Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation.

(integer)

AudioPtsOffsetDelta -> (integer)

Manually specify the difference in PTS offset that will be applied to the audio track, in seconds or milliseconds, when you set PTS offset to Seconds or Milliseconds. Enter an integer from -10000 to 10000. Leave blank to keep the default value 0.

DataPTSControl -> (string)

If you select ALIGN_TO_VIDEO, MediaConvert writes captions and data packets with Presentation Timestamp (PTS) values greater than or equal to the first video packet PTS (MediaConvert drops captions and data packets with lesser PTS values). Keep the default value AUTO to allow all PTS values.

MaxPcrInterval -> (integer)

Specify the maximum time, in milliseconds, between Program Clock References (PCRs) inserted into the transport stream.

NielsenId3 -> (string)

If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.

PatInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream.

PcrControl -> (string)

When set to PCR_EVERY_PES_PACKET a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.

PcrPid -> (integer)

Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID.

PmtInterval -> (integer)

The number of milliseconds between instances of this table in the output transport stream.

PmtPid -> (integer)

Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream.

PrivateMetadataPid -> (integer)

Packet Identifier (PID) of the private metadata stream in the transport stream.

ProgramNumber -> (integer)

The value of the program number field in the Program Map Table.

PtsOffset -> (integer)

Manually specify the initial PTS offset, in seconds, when you set PTS offset to Seconds. Enter an integer from 0 to 3600. Leave blank to keep the default value 2.

PtsOffsetMode -> (string)

Specify the initial presentation timestamp (PTS) offset for your transport stream output. To let MediaConvert automatically determine the initial PTS offset: Keep the default value, Auto. We recommend that you choose Auto for the widest player compatibility. The initial PTS will be at least two seconds and vary depending on your outputâs bitrate, HRD buffer size and HRD buffer initial fill percentage. To manually specify an initial PTS offset: Choose Seconds or Milliseconds. Then specify the number of seconds or milliseconds with PTS offset.

Scte35Pid -> (integer)

Packet Identifier (PID) of the SCTE-35 stream in the transport stream.

Scte35Source -> (string)

For SCTE-35 markers from your inputâ Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you donât want SCTE-35 markers in this output. For SCTE-35 markers from an ESAM XML documentâ Choose None if you donât want manifest conditioning. Choose Passthrough and choose Ad markers if you do want manifest conditioning. In both cases, also provide the ESAM XML as a string in the setting Signal processing notification XML.

TimedMetadata -> (string)

Set ID3 metadata to Passthrough to include ID3 metadata in this output. This includes ID3 metadata from the following features: ID3 timestamp period, and Custom ID3 metadata inserter. To exclude this ID3 metadata in this output: set ID3 metadata to None or leave blank.

TimedMetadataPid -> (integer)

Packet Identifier (PID) of the ID3 metadata stream in the transport stream.

TransportStreamId -> (integer)

The value of the transport stream ID field in the Program Map Table.

VideoPid -> (integer)

Packet Identifier (PID) of the elementary video stream in the transport stream.

MovSettings -> (structure)

These settings relate to your QuickTime MOV output container.

ClapAtom -> (string)

When enabled, include âclapâ atom if appropriate for the video output settings.

CslgAtom -> (string)

When enabled, file composition times will start at zero, composition times in the âcttsâ (composition time to sample) box for B-frames will be negative, and a âcslgâ (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools.

Mpeg2FourCCControl -> (string)

When set to XDCAM, writes MPEG2 video streams into the QuickTime file using XDCAM fourcc codes. This increases compatibility with Apple editors and players, but may decrease compatibility with other players. Only applicable when the video codec is MPEG2.

PaddingControl -> (string)

Unless you need Omneon compatibility: Keep the default value, None. To make this output compatible with Omneon: Choose Omneon. When you do, MediaConvert increases the length of the âelstâ edit list atom. Note that this might cause file rejections when a recipient of the output file doesnât expect this extra padding.

Reference -> (string)

Always keep the default value (SELF_CONTAINED) for this setting.

Mp4Settings -> (structure)

These settings relate to your MP4 output container. You can create audio only outputs with this container. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/supported-codecs-containers-audio-only.html#output-codecs-and-containers-supported-for-audio-only](https://docs.aws.amazon.com/mediaconvert/latest/ug/supported-codecs-containers-audio-only.html#output-codecs-and-containers-supported-for-audio-only).

AudioDuration -> (string)

Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec.

CslgAtom -> (string)

When enabled, file composition times will start at zero, composition times in the âcttsâ (composition time to sample) box for B-frames will be negative, and a âcslgâ (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools.

CttsVersion -> (integer)

Ignore this setting unless compliance to the CTTS box version specification matters in your workflow. Specify a value of 1 to set your CTTS box version to 1 and make your output compliant with the specification. When you specify a value of 1, you must also set CSLG atom to the value INCLUDE. Keep the default value 0 to set your CTTS box version to 0. This can provide backward compatibility for some players and packagers.

FreeSpaceBox -> (string)

Inserts a free-space box immediately after the moov box.

MoovPlacement -> (string)

To place the MOOV atom at the beginning of your output, which is useful for progressive downloading: Leave blank or choose Progressive download. To place the MOOV at the end of your output: Choose Normal.

Mp4MajorBrand -> (string)

Overrides the âMajor Brandâ field in the output file. Usually not necessary to specify.

MpdSettings -> (structure)

These settings relate to the fragmented MP4 container for the segments in your DASH outputs.

AccessibilityCaptionHints -> (string)

Optional. Choose Include to have MediaConvert mark up your DASH manifest with elements for embedded 608 captions. This markup isnât generally required, but some video players require it to discover and play embedded 608 captions. Keep the default value, Exclude, to leave these elements out. When you enable this setting, this is the markup that MediaConvert includes in your manifest:

AudioDuration -> (string)

Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec.

CaptionContainerType -> (string)

Use this setting only in DASH output groups that include sidecar TTML or IMSC captions. You specify sidecar captions in a separate output from your audio and video. Choose Raw for captions in a single XML file in a raw container. Choose Fragmented MPEG-4 for captions in XML format contained within fragmented MP4 files. This set of fragmented MP4 files is separate from your video and audio fragmented MP4 files.

KlvMetadata -> (string)

To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and writes each instance to a separate event message box in the output, according to MISB ST1910.1. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank.

ManifestMetadataSignaling -> (string)

To add an InbandEventStream element in your output MPD manifest for each type of event message, set Manifest metadata signaling to Enabled. For ID3 event messages, the InbandEventStream element schemeIdUri will be same value that you specify for ID3 metadata scheme ID URI. For SCTE35 event messages, the InbandEventStream element schemeIdUri will be â[urn:scte:scte35:2013:bin](urn:scte:scte35:2013:bin)â. To leave these elements out of your output MPD manifest, set Manifest metadata signaling to Disabled. To enable Manifest metadata signaling, you must also set SCTE-35 source to Passthrough, ESAM SCTE-35 to insert, or ID3 metadata to Passthrough.

Scte35Esam -> (string)

Use this setting only when you specify SCTE-35 markers from ESAM. Choose INSERT to put SCTE-35 markers in this output at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML.

Scte35Source -> (string)

Ignore this setting unless you have SCTE-35 markers in your input video file. Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you donât want those SCTE-35 markers in this output.

TimedMetadata -> (string)

To include ID3 metadata in this output: Set ID3 metadata to Passthrough. Specify this ID3 metadata in Custom ID3 metadata inserter. MediaConvert writes each instance of ID3 metadata in a separate Event Message (eMSG) box. To exclude this ID3 metadata: Set ID3 metadata to None or leave blank.

TimedMetadataBoxVersion -> (string)

Specify the event message box (eMSG) version for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.3 Syntax. Leave blank to use the default value Version 0. When you specify Version 1, you must also set ID3 metadata to Passthrough.

TimedMetadataSchemeIdUri -> (string)

Specify the event message box (eMSG) scheme ID URI for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.4 Semantics. Leave blank to use the default value: [https://aomedia.org/emsg/ID3](https://aomedia.org/emsg/ID3) When you specify a value for ID3 metadata scheme ID URI, you must also set ID3 metadata to Passthrough.

TimedMetadataValue -> (string)

Specify the event message box (eMSG) value for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.4 Semantics. When you specify a value for ID3 Metadata Value, you must also set ID3 metadata to Passthrough.

MxfSettings -> (structure)

These settings relate to your MXF output container.

AfdSignaling -> (string)

Optional. When you have AFD signaling set up in your output video stream, use this setting to choose whether to also include it in the MXF wrapper. Choose Donât copy to exclude AFD signaling from the MXF wrapper. Choose Copy from video stream to copy the AFD values from the video stream for this output to the MXF wrapper. Regardless of which option you choose, the AFD values remain in the video stream. Related settings: To set up your output to include or exclude AFD values, see AfdSignaling, under VideoDescription. On the console, find AFD signaling under the outputâs video encoding settings.

Profile -> (string)

Specify the MXF profile, also called shim, for this output. To automatically select a profile according to your output video codec and resolution, leave blank. For a list of codecs supported with each MXF profile, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/codecs-supported-with-each-mxf-profile.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/codecs-supported-with-each-mxf-profile.html). For more information about the automatic selection behavior, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/default-automatic-selection-of-mxf-profiles.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/default-automatic-selection-of-mxf-profiles.html).

XavcProfileSettings -> (structure)

Specify the XAVC profile settings for MXF outputs when you set your MXF profile to XAVC.

DurationMode -> (string)

To create an output that complies with the XAVC file format guidelines for interoperability, keep the default value, Drop frames for compliance. To include all frames from your input in this output, keep the default setting, Allow any duration. The number of frames that MediaConvert excludes when you set this to Drop frames for compliance depends on the output frame rate and duration.

MaxAncDataSize -> (integer)

Specify a value for this setting only for outputs that you set up with one of these two XAVC profiles: XAVC HD Intra CBG or XAVC 4K Intra CBG. Specify the amount of space in each frame that the service reserves for ancillary data, such as teletext captions. The default value for this setting is 1492 bytes per frame. This should be sufficient to prevent overflow unless you have multiple pages of teletext captions data. If you have a large amount of teletext data, specify a larger number.

Extension -> (string)

Use Extension to specify the file extension for outputs in File output groups. If you do not specify a value, the service will use default extensions by container type as follows * MPEG-2 transport stream, m2ts * Quicktime, mov * MXF container, mxf * MPEG-4 container, mp4 * WebM container, webm * Animated GIF container, gif * No Container, the service will use codec extensions (e.g. AAC, H265, H265, AC3)

NameModifier -> (string)

Use Name modifier to have the service add a string to the end of each output filename. You specify the base filename as part of your destination URI. When you create multiple outputs in the same output group, Name modifier is required. Name modifier also accepts format identifiers. For DASH ISO outputs, if you use the format identifiers $Number$ or $Time$ in one output, you must use them in the same way in all outputs of the output group.

OutputSettings -> (structure)

Specific settings for this type of output.

HlsSettings -> (structure)

Settings for HLS output groups

AudioGroupId -> (string)

Specifies the group to which the audio rendition belongs.

AudioOnlyContainer -> (string)

Use this setting only in audio-only outputs. Choose MPEG-2 Transport Stream (M2TS) to create a file in an MPEG2-TS container. Keep the default value Automatic to create an audio-only file in a raw container. Regardless of the value that you specify here, if this output has video, the service will place the output into an MPEG2-TS container.

AudioRenditionSets -> (string)

List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by â,â.

AudioTrackType -> (string)

Four types of audio-only tracks are supported: Audio-Only Variant Stream The client can play back this audio-only stream instead of video in low-bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate Audio, Auto Select, Default Alternate rendition that the client should try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio, Auto Select, Not Default Alternate rendition that the client may try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate rendition that the client will not try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO

DescriptiveVideoServiceFlag -> (string)

Specify whether to flag this audio track as descriptive video service (DVS) in your HLS parent manifest. When you choose Flag, MediaConvert includes the parameter CHARACTERISTICS=âpublic.accessibility.describes-videoâ in the EXT-X-MEDIA entry for this track. When you keep the default choice, Donât flag, MediaConvert leaves this parameter out. The DVS flag can help with accessibility on Apple devices. For more information, see the Apple documentation.

IFrameOnlyManifest -> (string)

Choose Include to have MediaConvert generate a child manifest that lists only the I-frames for this rendition, in addition to your regular manifest for this rendition. You might use this manifest as part of a workflow that creates preview functions for your video. MediaConvert adds both the I-frame only child manifest and the regular child manifest to the parent manifest. When you donât need the I-frame only child manifest, keep the default value Exclude.

SegmentModifier -> (string)

Use this setting to add an identifying string to the filename of each segment. The service adds this string between the name modifier and segment index number. You can use format identifiers in the string. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/using-variables-in-your-job-settings.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/using-variables-in-your-job-settings.html)

Preset -> (string)

Use Preset to specify a preset for your transcoding settings. Provide the system or custom preset name. You can specify either Preset or Container settings, but not both.

VideoDescription -> (structure)

VideoDescription contains a group of video encoding settings. The specific video settings depend on the video codec that you choose for the property codec. Include one instance of VideoDescription per output.

AfdSignaling -> (string)

This setting only applies to H.264, H.265, and MPEG2 outputs. Use Insert AFD signaling to specify whether the service includes AFD values in the output video data and what those values are. * Choose None to remove all AFD values from this output. * Choose Fixed to ignore input AFD values and instead encode the value specified in the job. * Choose Auto to calculate output AFD values based on the input AFD scaler data.

AntiAlias -> (string)

The anti-alias filter is automatically applied to all outputs. The service no longer accepts the value DISABLED for AntiAlias. If you specify that in your job, the service will ignore the setting.

ChromaPositionMode -> (string)

Specify the chroma sample positioning metadata for your H.264 or H.265 output. To have MediaConvert automatically determine chroma positioning: We recommend that you keep the default value, Auto. To specify center positioning: Choose Force center. To specify top left positioning: Choose Force top left.

CodecSettings -> (structure)

Video codec settings contains the group of settings related to video encoding. The settings in this group vary depending on the value that you choose for Video codec. For each codec enum that you choose, define the corresponding settings object. The following lists the codec enum, settings object pairs. * AV1, Av1Settings * AVC_INTRA, AvcIntraSettings * FRAME_CAPTURE, FrameCaptureSettings * GIF, GifSettings * H_264, H264Settings * H_265, H265Settings * MPEG2, Mpeg2Settings * PRORES, ProresSettings * UNCOMPRESSED, UncompressedSettings * VC3, Vc3Settings * VP8, Vp8Settings * VP9, Vp9Settings * XAVC, XavcSettings

Av1Settings -> (structure)

Required when you set Codec, under VideoDescription>CodecSettings to the value AV1.

AdaptiveQuantization -> (string)

Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to Spatial adaptive quantization.

BitDepth -> (string)

Specify the Bit depth. You can choose 8-bit or 10-bit.

FilmGrainSynthesis -> (string)

Film grain synthesis replaces film grain present in your content with similar quality synthesized AV1 film grain. We recommend that you choose Enabled to reduce the bandwidth of your QVBR quality level 5, 6, 7, or 8 outputs. For QVBR quality level 9 or 10 outputs we recommend that you keep the default value, Disabled. When you include Film grain synthesis, you cannot include the Noise reducer preprocessor.

FramerateControl -> (string)

Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.

FramerateConversionAlgorithm -> (string)

Choose the method that you want MediaConvert to use when increasing or decreasing your videoâs frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.

FramerateDenominator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

FramerateNumerator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

GopSize -> (double)

Specify the GOP length (keyframe interval) in frames. With AV1, MediaConvert doesnât support GOP length in seconds. This value must be greater than zero and preferably equal to 1 + ((numberBFrames + 1) * x), where x is an integer value.

MaxBitrate -> (integer)

Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR.

NumberBFramesBetweenReferenceFrames -> (integer)

Specify from the number of B-frames, in the range of 0-15. For AV1 encoding, we recommend using 7 or 15. Choose a larger number for a lower bitrate and smaller file size; choose a smaller number for better video quality.

PerFrameMetrics -> (list)

Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: * PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

(string)

- PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

QvbrSettings -> (structure)

Settings for quality-defined variable bitrate encoding with the H.265 codec. Use these settings only when you set QVBR for Rate control mode.

QvbrQualityLevel -> (integer)

Use this setting only when you set Rate control mode to QVBR. Specify the target quality level for this output. MediaConvert determines the right number of bits to use for each part of the video to maintain the video quality that you specify. When you keep the default value, AUTO, MediaConvert picks a quality level for you, based on characteristics of your input video. If you prefer to specify a quality level, specify a number from 1 through 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9. Optionally, to specify a value between whole numbers, also provide a value for the setting qvbrQualityLevelFineTune. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33.

QvbrQualityLevelFineTune -> (double)

Optional. Specify a value here to set the QVBR quality to a level that is between whole numbers. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. MediaConvert rounds your QVBR quality level to the nearest third of a whole number. For example, if you set qvbrQualityLevel to 7 and you set qvbrQualityLevelFineTune to .25, your actual QVBR quality level is 7.33.

RateControlMode -> (string)

âWith AV1 outputs, for rate control mode, MediaConvert supports only quality-defined variable bitrate (QVBR). You canâât use CBR or VBR.â

Slices -> (integer)

Specify the number of slices per picture. This value must be 1, 2, 4, 8, 16, or 32. For progressive pictures, this value must be less than or equal to the number of macroblock rows. For interlaced pictures, this value must be less than or equal to half the number of macroblock rows.

SpatialAdaptiveQuantization -> (string)

Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesnât take into account where the viewerâs attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher.

AvcIntraSettings -> (structure)

Required when you choose AVC-Intra for your output video codec. For more information about the AVC-Intra settings, see the relevant specification. For detailed information about SD and HD in AVC-Intra, see [https://ieeexplore.ieee.org/document/7290936](https://ieeexplore.ieee.org/document/7290936). For information about 4K/2K in AVC-Intra, see [https://pro-av.panasonic.net/en/avc-ultra/AVC-ULTRAoverview.pdf](https://pro-av.panasonic.net/en/avc-ultra/AVC-ULTRAoverview.pdf).

AvcIntraClass -> (string)

Specify the AVC-Intra class of your output. The AVC-Intra class selection determines the output video bit rate depending on the frame rate of the output. Outputs with higher class values have higher bitrates and improved image quality. Note that for Class 4K/2K, MediaConvert supports only 4:2:2 chroma subsampling.

AvcIntraUhdSettings -> (structure)

Optional when you set AVC-Intra class to Class 4K/2K. When you set AVC-Intra class to a different value, this object isnât allowed.

QualityTuningLevel -> (string)

Optional. Use Quality tuning level to choose how many transcoding passes MediaConvert does with your video. When you choose Multi-pass, your video quality is better and your output bitrate is more accurate. That is, the actual bitrate of your output is closer to the target bitrate defined in the specification. When you choose Single-pass, your encoding time is faster. The default behavior is Single-pass.

FramerateControl -> (string)

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.

FramerateConversionAlgorithm -> (string)

Choose the method that you want MediaConvert to use when increasing or decreasing your videoâs frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.

FramerateDenominator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

FramerateNumerator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

InterlaceMode -> (string)

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output thatâs interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.

PerFrameMetrics -> (list)

Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: * PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

(string)

- PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

ScanTypeConversionMode -> (string)

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isnât suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You canât use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.

SlowPal -> (string)

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25.

Telecine -> (string)

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.

Codec -> (string)

Specifies the video codec. This must be equal to one of the enum values defined by the object VideoCodec. To passthrough the video stream of your input JPEG2000, VC-3, AVC-INTRA or Apple ProRes video without any video encoding: Choose Passthrough. If you have multiple input videos, note that they must have identical encoding attributes. When you choose Passthrough, your output container must be MXF or QuickTime MOV.

FrameCaptureSettings -> (structure)

Required when you set Codec to the value FRAME_CAPTURE.

FramerateDenominator -> (integer)

Frame capture will encode the first frame of the output stream, then one frame every framerateDenominator/framerateNumerator seconds. For example, settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of 1/3 frame per second) will capture the first frame, then 1 frame every 3s. Files will be named as filename.n.jpg where n is the 0-based sequence number of each Capture.

FramerateNumerator -> (integer)

Frame capture will encode the first frame of the output stream, then one frame every framerateDenominator/framerateNumerator seconds. For example, settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of 1/3 frame per second) will capture the first frame, then 1 frame every 3s. Files will be named as filename.NNNNNNN.jpg where N is the 0-based frame sequence number zero padded to 7 decimal places.

MaxCaptures -> (integer)

Maximum number of captures (encoded jpg output files).

Quality -> (integer)

JPEG Quality - a higher value equals higher quality.

GifSettings -> (structure)

Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value GIF

FramerateControl -> (string)

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction. If you are creating your transcoding job specification as a JSON file without the console, use FramerateControl to specify which value the service uses for the frame rate for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to use the frame rate from the input. Choose SPECIFIED if you want the service to use the frame rate you specify in the settings FramerateNumerator and FramerateDenominator.

FramerateConversionAlgorithm -> (string)

Optional. Specify how the transcoder performs framerate conversion. The default behavior is to use Drop duplicate (DUPLICATE_DROP) conversion. When you choose Interpolate (INTERPOLATE) instead, the conversion produces smoother motion.

FramerateDenominator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

FramerateNumerator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

H264Settings -> (structure)

Required when you set Codec to the value H_264.

AdaptiveQuantization -> (string)

Keep the default value, Auto, for this setting to have MediaConvert automatically apply the best types of quantization for your video content. When you want to apply your quantization settings manually, you must set H264AdaptiveQuantization to a value other than Auto. Use this setting to specify the strength of any adaptive quantization filters that you enable. If you donât want MediaConvert to do any adaptive quantization in this transcode, set Adaptive quantization to Off. Related settings: The value that you choose here applies to the following settings: H264FlickerAdaptiveQuantization, H264SpatialAdaptiveQuantization, and H264TemporalAdaptiveQuantization.

BandwidthReductionFilter -> (structure)

The Bandwidth reduction filter increases the video quality of your output relative to its bitrate. Use to lower the bitrate of your constant quality QVBR output, with little or no perceptual decrease in quality. Or, use to increase the video quality of outputs with other rate control modes relative to the bitrate that you specify. Bandwidth reduction increases further when your input is low quality or noisy. Outputs that use this feature incur pro-tier pricing. When you include Bandwidth reduction filter, you cannot include the Noise reducer preprocessor.

Sharpening -> (string)

Optionally specify the level of sharpening to apply when you use the Bandwidth reduction filter. Sharpening adds contrast to the edges of your video content and can reduce softness. Keep the default value Off to apply no sharpening. Set Sharpening strength to Low to apply a minimal amount of sharpening, or High to apply a maximum amount of sharpening.

Strength -> (string)

Specify the strength of the Bandwidth reduction filter. For most workflows, we recommend that you choose Auto to reduce the bandwidth of your output with little to no perceptual decrease in video quality. For high quality and high bitrate outputs, choose Low. For the most bandwidth reduction, choose High. We recommend that you choose High for low bitrate outputs. Note that High may incur a slight increase in the softness of your output.

Bitrate -> (integer)

Specify the average bitrate in bits per second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000.

CodecLevel -> (string)

Specify an H.264 level that is consistent with your output video settings. If you arenât sure what level to specify, choose Auto.

CodecProfile -> (string)

H.264 Profile. High 4:2:2 and 10-bit profiles are only available with the AVC-I License.

DynamicSubGop -> (string)

Specify whether to allow the number of B-frames in your output GOP structure to vary or not depending on your input video content. To improve the subjective video quality of your output that has high-motion content: Leave blank or keep the default value Adaptive. MediaConvert will use fewer B-frames for high-motion video content than low-motion content. The maximum number of B- frames is limited by the value that you choose for B-frames between reference frames. To use the same number B-frames for all types of content: Choose Static.

EndOfStreamMarkers -> (string)

Optionally include or suppress markers at the end of your output that signal the end of the video stream. To include end of stream markers: Leave blank or keep the default value, Include. To not include end of stream markers: Choose Suppress. This is useful when your output will be inserted into another stream.

EntropyEncoding -> (string)

Entropy encoding mode. Use CABAC (must be in Main or High profile) or CAVLC.

FieldEncoding -> (string)

The video encoding method for your MPEG-4 AVC output. Keep the default value, PAFF, to have MediaConvert use PAFF encoding for interlaced outputs. Choose Force field to disable PAFF encoding and create separate interlaced fields. Choose MBAFF to disable PAFF and have MediaConvert use MBAFF encoding for interlaced outputs.

FlickerAdaptiveQuantization -> (string)

Only use this setting when you change the default value, AUTO, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264FlickerAdaptiveQuantization is Disabled. Change this value to Enabled to reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. To manually enable or disable H264FlickerAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO.

FramerateControl -> (string)

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.

FramerateConversionAlgorithm -> (string)

Choose the method that you want MediaConvert to use when increasing or decreasing your videoâs frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.

FramerateDenominator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

FramerateNumerator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

GopBReference -> (string)

Specify whether to allow B-frames to be referenced by other frame types. To use reference B-frames when your GOP structure has 1 or more B-frames: Leave blank or keep the default value Enabled. We recommend that you choose Enabled to help improve the video quality of your output relative to its bitrate. To not use reference B-frames: Choose Disabled.

GopClosedCadence -> (integer)

Specify the relative frequency of open to closed GOPs in this output. For example, if you want to allow four open GOPs and then require a closed GOP, set this value to 5. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. In the console, do this by keeping the default empty value. If you do explicitly specify a value, for segmented outputs, donât set this value to 0.

GopSize -> (double)

Use this setting only when you set GOP mode control to Specified, frames or Specified, seconds. Specify the GOP length using a whole number of frames or a decimal value of seconds. MediaConvert will interpret this value as frames or seconds depending on the value you choose for GOP mode control. If you want to allow MediaConvert to automatically determine GOP size, leave GOP size blank and set GOP mode control to Auto. If your output group specifies HLS, DASH, or CMAF, leave GOP size blank and set GOP mode control to Auto in each output in your output group.

GopSizeUnits -> (string)

Specify how the transcoder determines GOP size for this output. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, choose Auto and and leave GOP size blank. By default, if you donât specify GOP mode control, MediaConvert will use automatic behavior. If your output group specifies HLS, DASH, or CMAF, set GOP mode control to Auto and leave GOP size blank in each output in your output group. To explicitly specify the GOP length, choose Specified, frames or Specified, seconds and then provide the GOP length in the related setting GOP size.

HrdBufferFinalFillPercentage -> (integer)

If your downstream systems have strict buffer requirements: Specify the minimum percentage of the HRD buffer thatâs available at the end of each encoded video segment. For the best video quality: Set to 0 or leave blank to automatically determine the final buffer fill percentage.

HrdBufferInitialFillPercentage -> (integer)

Percentage of the buffer that should initially be filled (HRD buffer model).

HrdBufferSize -> (integer)

Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000.

InterlaceMode -> (string)

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output thatâs interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.

MaxBitrate -> (integer)

Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR.

MinIInterval -> (integer)

Specify the minimum number of frames allowed between two IDR-frames in your output. This includes frames created at the start of a GOP or a scene change. Use Min I-Interval to improve video compression by varying GOP size when two IDR-frames would be created near each other. For example, if a regular cadence-driven IDR-frame would fall within 5 frames of a scene-change IDR-frame, and you set Min I-interval to 5, then the encoder would only write an IDR-frame for the scene-change. In this way, one GOP is shortened or extended. If a cadence-driven IDR-frame would be further than 5 frames from a scene-change IDR-frame, then the encoder leaves all IDR-frames in place. To use an automatically determined interval: We recommend that you keep this value blank. This allows for MediaConvert to use an optimal setting according to the characteristics of your input video, and results in better video compression. To manually specify an interval: Enter a value from 1 to 30. Use when your downstream systems have specific GOP size requirements. To disable GOP size variance: Enter 0. MediaConvert will only create IDR-frames at the start of your outputâs cadence-driven GOP. Use when your downstream systems require a regular GOP size.

NumberBFramesBetweenReferenceFrames -> (integer)

Specify the number of B-frames between reference frames in this output. For the best video quality: Leave blank. MediaConvert automatically determines the number of B-frames to use based on the characteristics of your input video. To manually specify the number of B-frames between reference frames: Enter an integer from 0 to 7.

NumberReferenceFrames -> (integer)

Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding.

ParControl -> (string)

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.

ParDenominator -> (integer)

Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33.

ParNumerator -> (integer)

Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40.

PerFrameMetrics -> (list)

Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: * PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

(string)

- PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

QualityTuningLevel -> (string)

The Quality tuning level you choose represents a trade-off between the encoding speed of your job and the output video quality. For the fastest encoding speed at the cost of video quality: Choose Single pass. For a good balance between encoding speed and video quality: Leave blank or keep the default value Single pass HQ. For the best video quality, at the cost of encoding speed: Choose Multi pass HQ. MediaConvert performs an analysis pass on your input followed by an encoding pass. Outputs that use this feature incur pro-tier pricing.

QvbrSettings -> (structure)

Settings for quality-defined variable bitrate encoding with the H.265 codec. Use these settings only when you set QVBR for Rate control mode.

MaxAverageBitrate -> (integer)

Use this setting only when Rate control mode is QVBR and Quality tuning level is Multi-pass HQ. For Max average bitrate values suited to the complexity of your input video, the service limits the average bitrate of the video part of this output to the value that you choose. That is, the total size of the video element is less than or equal to the value you set multiplied by the number of seconds of encoded output.

QvbrQualityLevel -> (integer)

Use this setting only when you set Rate control mode to QVBR. Specify the target quality level for this output. MediaConvert determines the right number of bits to use for each part of the video to maintain the video quality that you specify. When you keep the default value, AUTO, MediaConvert picks a quality level for you, based on characteristics of your input video. If you prefer to specify a quality level, specify a number from 1 through 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9. Optionally, to specify a value between whole numbers, also provide a value for the setting qvbrQualityLevelFineTune. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33.

QvbrQualityLevelFineTune -> (double)

Optional. Specify a value here to set the QVBR quality to a level that is between whole numbers. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. MediaConvert rounds your QVBR quality level to the nearest third of a whole number. For example, if you set qvbrQualityLevel to 7 and you set qvbrQualityLevelFineTune to .25, your actual QVBR quality level is 7.33.

RateControlMode -> (string)

Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR).

RepeatPps -> (string)

Places a PPS header on each encoded picture, even if repeated.

SaliencyAwareEncoding -> (string)

Specify whether to apply Saliency aware encoding to your output. Use to improve the perceptual video quality of your output by allocating more encoding bits to the prominent or noticeable parts of your content. To apply saliency aware encoding, when possible: We recommend that you choose Preferred. The effects of Saliency aware encoding are best seen in lower bitrate outputs. When you choose Preferred, note that Saliency aware encoding will only apply to outputs that are 720p or higher in resolution. To not apply saliency aware encoding, prioritizing encoding speed over perceptual video quality: Choose Disabled.

ScanTypeConversionMode -> (string)

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isnât suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You canât use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.

SceneChangeDetect -> (string)

Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default. If this output uses QVBR, choose Transition detection for further video quality improvement. For more information about QVBR, see [https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr](https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr).

Slices -> (integer)

Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures.

SlowPal -> (string)

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25.

Softness -> (integer)

Ignore this setting unless you need to comply with a specification that requires a specific value. If you donât have a specification requirement, we recommend that you adjust the softness of your output by using a lower value for the setting Sharpness or by enabling a noise reducer filter. The Softness setting specifies the quantization matrices that the encoder uses. Keep the default value, 0, for flat quantization. Choose the value 1 or 16 to use the default JVT softening quantization matricies from the H.264 specification. Choose a value from 17 to 128 to use planar interpolation. Increasing values from 17 to 128 result in increasing reduction of high-frequency data. The value 128 results in the softest video.

SpatialAdaptiveQuantization -> (string)

Only use this setting when you change the default value, Auto, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264SpatialAdaptiveQuantization is Enabled. Keep this default value to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesnât take into account where the viewerâs attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to set H264SpatialAdaptiveQuantization to Disabled. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher. To manually enable or disable H264SpatialAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO.

Syntax -> (string)

Produces a bitstream compliant with SMPTE RP-2027.

Telecine -> (string)

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard or soft telecine to create a smoother picture. Hard telecine produces a 29.97i output. Soft telecine produces an output with a 23.976 output that signals to the video player device to do the conversion during play back. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.

TemporalAdaptiveQuantization -> (string)

Only use this setting when you change the default value, AUTO, for the setting H264AdaptiveQuantization. When you keep all defaults, excluding H264AdaptiveQuantization and all other adaptive quantization from your JSON job specification, MediaConvert automatically applies the best types of quantization for your video content. When you set H264AdaptiveQuantization to a value other than AUTO, the default value for H264TemporalAdaptiveQuantization is Enabled. Keep this default value to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that arenât moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesnât take into account where the viewerâs attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesnât have moving objects with sharp edges, such as sports athletesâ faces, you might choose to set H264TemporalAdaptiveQuantization to Disabled. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization. To manually enable or disable H264TemporalAdaptiveQuantization, you must set Adaptive quantization to a value other than AUTO.

UnregisteredSeiTimecode -> (string)

Inserts timecode for each frame as 4 bytes of an unregistered SEI message.

WriteMp4PackagingType -> (string)

Specify how SPS and PPS NAL units are written in your output MP4 container, according to ISO/IEC 14496-15. If the location of these parameters doesnât matter in your workflow: Keep the default value, AVC1. MediaConvert writes SPS and PPS NAL units in the sample description (âstsdâ) box (but not into samples directly). To write SPS and PPS NAL units directly into samples (but not in the âstsdâ box): Choose AVC3. When you do, note that your output might not play properly with some downstream systems or players.

H265Settings -> (structure)

Settings for H265 codec

AdaptiveQuantization -> (string)

When you set Adaptive Quantization to Auto, or leave blank, MediaConvert automatically applies quantization to improve the video quality of your output. Set Adaptive Quantization to Low, Medium, High, Higher, or Max to manually control the strength of the quantization filter. When you do, you can specify a value for Spatial Adaptive Quantization, Temporal Adaptive Quantization, and Flicker Adaptive Quantization, to further control the quantization filter. Set Adaptive Quantization to Off to apply no quantization to your output.

AlternateTransferFunctionSei -> (string)

Enables Alternate Transfer Function SEI message for outputs using Hybrid Log Gamma (HLG) Electro-Optical Transfer Function (EOTF).

BandwidthReductionFilter -> (structure)

The Bandwidth reduction filter increases the video quality of your output relative to its bitrate. Use to lower the bitrate of your constant quality QVBR output, with little or no perceptual decrease in quality. Or, use to increase the video quality of outputs with other rate control modes relative to the bitrate that you specify. Bandwidth reduction increases further when your input is low quality or noisy. Outputs that use this feature incur pro-tier pricing. When you include Bandwidth reduction filter, you cannot include the Noise reducer preprocessor.

Sharpening -> (string)

Optionally specify the level of sharpening to apply when you use the Bandwidth reduction filter. Sharpening adds contrast to the edges of your video content and can reduce softness. Keep the default value Off to apply no sharpening. Set Sharpening strength to Low to apply a minimal amount of sharpening, or High to apply a maximum amount of sharpening.

Strength -> (string)

Specify the strength of the Bandwidth reduction filter. For most workflows, we recommend that you choose Auto to reduce the bandwidth of your output with little to no perceptual decrease in video quality. For high quality and high bitrate outputs, choose Low. For the most bandwidth reduction, choose High. We recommend that you choose High for low bitrate outputs. Note that High may incur a slight increase in the softness of your output.

Bitrate -> (integer)

Specify the average bitrate in bits per second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000.

CodecLevel -> (string)

H.265 Level.

CodecProfile -> (string)

Represents the Profile and Tier, per the HEVC (H.265) specification. Selections are grouped as [Profile] / [Tier], so âMain/Highâ represents Main Profile with High Tier. 4:2:2 profiles are only available with the HEVC 4:2:2 License.

Deblocking -> (string)

Use Deblocking to improve the video quality of your output by smoothing the edges of macroblock artifacts created during video compression. To reduce blocking artifacts at block boundaries, and improve overall video quality: Keep the default value, Enabled. To not apply any deblocking: Choose Disabled. Visible block edge artifacts might appear in the output, especially at lower bitrates.

DynamicSubGop -> (string)

Specify whether to allow the number of B-frames in your output GOP structure to vary or not depending on your input video content. To improve the subjective video quality of your output that has high-motion content: Leave blank or keep the default value Adaptive. MediaConvert will use fewer B-frames for high-motion video content than low-motion content. The maximum number of B- frames is limited by the value that you choose for B-frames between reference frames. To use the same number B-frames for all types of content: Choose Static.

EndOfStreamMarkers -> (string)

Optionally include or suppress markers at the end of your output that signal the end of the video stream. To include end of stream markers: Leave blank or keep the default value, Include. To not include end of stream markers: Choose Suppress. This is useful when your output will be inserted into another stream.

FlickerAdaptiveQuantization -> (string)

Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set adaptiveQuantization to a value other than Off.

FramerateControl -> (string)

Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.

FramerateConversionAlgorithm -> (string)

Choose the method that you want MediaConvert to use when increasing or decreasing your videoâs frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.

FramerateDenominator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

FramerateNumerator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

GopBReference -> (string)

Specify whether to allow B-frames to be referenced by other frame types. To use reference B-frames when your GOP structure has 1 or more B-frames: Leave blank or keep the default value Enabled. We recommend that you choose Enabled to help improve the video quality of your output relative to its bitrate. To not use reference B-frames: Choose Disabled.

GopClosedCadence -> (integer)

Specify the relative frequency of open to closed GOPs in this output. For example, if you want to allow four open GOPs and then require a closed GOP, set this value to 5. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, do this by keeping the default empty value. If you do explicitly specify a value, for segmented outputs, donât set this value to 0.

GopSize -> (double)

Use this setting only when you set GOP mode control to Specified, frames or Specified, seconds. Specify the GOP length using a whole number of frames or a decimal value of seconds. MediaConvert will interpret this value as frames or seconds depending on the value you choose for GOP mode control. If you want to allow MediaConvert to automatically determine GOP size, leave GOP size blank and set GOP mode control to Auto. If your output group specifies HLS, DASH, or CMAF, leave GOP size blank and set GOP mode control to Auto in each output in your output group.

GopSizeUnits -> (string)

Specify how the transcoder determines GOP size for this output. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, choose Auto and and leave GOP size blank. By default, if you donât specify GOP mode control, MediaConvert will use automatic behavior. If your output group specifies HLS, DASH, or CMAF, set GOP mode control to Auto and leave GOP size blank in each output in your output group. To explicitly specify the GOP length, choose Specified, frames or Specified, seconds and then provide the GOP length in the related setting GOP size.

HrdBufferFinalFillPercentage -> (integer)

If your downstream systems have strict buffer requirements: Specify the minimum percentage of the HRD buffer thatâs available at the end of each encoded video segment. For the best video quality: Set to 0 or leave blank to automatically determine the final buffer fill percentage.

HrdBufferInitialFillPercentage -> (integer)

Percentage of the buffer that should initially be filled (HRD buffer model).

HrdBufferSize -> (integer)

Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000.

InterlaceMode -> (string)

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output thatâs interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.

MaxBitrate -> (integer)

Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR.

MinIInterval -> (integer)

Specify the minimum number of frames allowed between two IDR-frames in your output. This includes frames created at the start of a GOP or a scene change. Use Min I-Interval to improve video compression by varying GOP size when two IDR-frames would be created near each other. For example, if a regular cadence-driven IDR-frame would fall within 5 frames of a scene-change IDR-frame, and you set Min I-interval to 5, then the encoder would only write an IDR-frame for the scene-change. In this way, one GOP is shortened or extended. If a cadence-driven IDR-frame would be further than 5 frames from a scene-change IDR-frame, then the encoder leaves all IDR-frames in place. To use an automatically determined interval: We recommend that you keep this value blank. This allows for MediaConvert to use an optimal setting according to the characteristics of your input video, and results in better video compression. To manually specify an interval: Enter a value from 1 to 30. Use when your downstream systems have specific GOP size requirements. To disable GOP size variance: Enter 0. MediaConvert will only create IDR-frames at the start of your outputâs cadence-driven GOP. Use when your downstream systems require a regular GOP size.

NumberBFramesBetweenReferenceFrames -> (integer)

Specify the number of B-frames between reference frames in this output. For the best video quality: Leave blank. MediaConvert automatically determines the number of B-frames to use based on the characteristics of your input video. To manually specify the number of B-frames between reference frames: Enter an integer from 0 to 7.

NumberReferenceFrames -> (integer)

Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding.

ParControl -> (string)

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.

ParDenominator -> (integer)

Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33.

ParNumerator -> (integer)

Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40.

PerFrameMetrics -> (list)

Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: * PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

(string)

- PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

QualityTuningLevel -> (string)

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding.

QvbrSettings -> (structure)

Settings for quality-defined variable bitrate encoding with the H.265 codec. Use these settings only when you set QVBR for Rate control mode.

MaxAverageBitrate -> (integer)

Use this setting only when Rate control mode is QVBR and Quality tuning level is Multi-pass HQ. For Max average bitrate values suited to the complexity of your input video, the service limits the average bitrate of the video part of this output to the value that you choose. That is, the total size of the video element is less than or equal to the value you set multiplied by the number of seconds of encoded output.

QvbrQualityLevel -> (integer)

Use this setting only when you set Rate control mode to QVBR. Specify the target quality level for this output. MediaConvert determines the right number of bits to use for each part of the video to maintain the video quality that you specify. When you keep the default value, AUTO, MediaConvert picks a quality level for you, based on characteristics of your input video. If you prefer to specify a quality level, specify a number from 1 through 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9. Optionally, to specify a value between whole numbers, also provide a value for the setting qvbrQualityLevelFineTune. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33.

QvbrQualityLevelFineTune -> (double)

Optional. Specify a value here to set the QVBR quality to a level that is between whole numbers. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. MediaConvert rounds your QVBR quality level to the nearest third of a whole number. For example, if you set qvbrQualityLevel to 7 and you set qvbrQualityLevelFineTune to .25, your actual QVBR quality level is 7.33.

RateControlMode -> (string)

Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR).

SampleAdaptiveOffsetFilterMode -> (string)

Specify Sample Adaptive Offset (SAO) filter strength. Adaptive mode dynamically selects best strength based on content

ScanTypeConversionMode -> (string)

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isnât suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You canât use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.

SceneChangeDetect -> (string)

Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default. If this output uses QVBR, choose Transition detection for further video quality improvement. For more information about QVBR, see [https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr](https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr).

Slices -> (integer)

Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures.

SlowPal -> (string)

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25.

SpatialAdaptiveQuantization -> (string)

Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesnât take into account where the viewerâs attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher.

Telecine -> (string)

This field applies only if the Streams > Advanced > Framerate field is set to 29.970. This field works with the Streams > Advanced > Preprocessors > Deinterlacer field and the Streams > Advanced > Interlaced Mode field to identify the scan type for the output: Progressive, Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i output from 23.976 input. - Soft: produces 23.976; the player converts this output to 29.97i.

TemporalAdaptiveQuantization -> (string)

Keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that arenât moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesnât take into account where the viewerâs attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesnât have moving objects with sharp edges, such as sports athletesâ faces, you might choose to disable this feature. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization.

TemporalIds -> (string)

Enables temporal layer identifiers in the encoded bitstream. Up to 3 layers are supported depending on GOP structure: I- and P-frames form one layer, reference B-frames can form a second layer and non-reference b-frames can form a third layer. Decoders can optionally decode only the lower temporal layers to generate a lower frame rate output. For example, given a bitstream with temporal IDs and with b-frames = 1 (i.e. IbPbPb display order), a decoder could decode all the frames for full frame rate output or only the I and P frames (lowest temporal layer) for a half frame rate output.

Tiles -> (string)

Enable use of tiles, allowing horizontal as well as vertical subdivision of the encoded pictures.

UnregisteredSeiTimecode -> (string)

Inserts timecode for each frame as 4 bytes of an unregistered SEI message.

WriteMp4PackagingType -> (string)

If the location of parameter set NAL units doesnât matter in your workflow, ignore this setting. Use this setting only with CMAF or DASH outputs, or with standalone file outputs in an MPEG-4 container (MP4 outputs). Choose HVC1 to mark your output as HVC1. This makes your output compliant with the following specification: ISO IECJTC1 SC29 N13798 Text ISO/IEC FDIS 14496-15 3rd Edition. For these outputs, the service stores parameter set NAL units in the sample headers but not in the samples directly. For MP4 outputs, when you choose HVC1, your output video might not work properly with some downstream systems and video players. The service defaults to marking your output as HEV1. For these outputs, the service writes parameter set NAL units directly into the samples.

Mpeg2Settings -> (structure)

Required when you set Codec to the value MPEG2.

AdaptiveQuantization -> (string)

Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to the following settings: Spatial adaptive quantization, and Temporal adaptive quantization.

Bitrate -> (integer)

Specify the average bitrate in bits per second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000.

CodecLevel -> (string)

Use Level to set the MPEG-2 level for the video output.

CodecProfile -> (string)

Use Profile to set the MPEG-2 profile for the video output.

DynamicSubGop -> (string)

Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames.

FramerateControl -> (string)

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.

FramerateConversionAlgorithm -> (string)

Choose the method that you want MediaConvert to use when increasing or decreasing your videoâs frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.

FramerateDenominator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

FramerateNumerator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

GopClosedCadence -> (integer)

Specify the relative frequency of open to closed GOPs in this output. For example, if you want to allow four open GOPs and then require a closed GOP, set this value to 5. When you create a streaming output, we recommend that you keep the default value, 1, so that players starting mid-stream receive an IDR frame as quickly as possible. Donât set this value to 0; that would break output segmenting.

GopSize -> (double)

Specify the interval between keyframes, in seconds or frames, for this output. Default: 12 Related settings: When you specify the GOP size in seconds, set GOP mode control to Specified, seconds. The default value for GOP mode control is Frames.

GopSizeUnits -> (string)

Specify the units for GOP size. If you donât specify a value here, by default the encoder measures GOP size in frames.

HrdBufferFinalFillPercentage -> (integer)

If your downstream systems have strict buffer requirements: Specify the minimum percentage of the HRD buffer thatâs available at the end of each encoded video segment. For the best video quality: Set to 0 or leave blank to automatically determine the final buffer fill percentage.

HrdBufferInitialFillPercentage -> (integer)

Percentage of the buffer that should initially be filled (HRD buffer model).

HrdBufferSize -> (integer)

Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000.

InterlaceMode -> (string)

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output thatâs interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.

IntraDcPrecision -> (string)

Use Intra DC precision to set quantization precision for intra-block DC coefficients. If you choose the value auto, the service will automatically select the precision based on the per-frame compression ratio.

MaxBitrate -> (integer)

Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000.

MinIInterval -> (integer)

Specify the minimum number of frames allowed between two IDR-frames in your output. This includes frames created at the start of a GOP or a scene change. Use Min I-Interval to improve video compression by varying GOP size when two IDR-frames would be created near each other. For example, if a regular cadence-driven IDR-frame would fall within 5 frames of a scene-change IDR-frame, and you set Min I-interval to 5, then the encoder would only write an IDR-frame for the scene-change. In this way, one GOP is shortened or extended. If a cadence-driven IDR-frame would be further than 5 frames from a scene-change IDR-frame, then the encoder leaves all IDR-frames in place. To manually specify an interval: Enter a value from 1 to 30. Use when your downstream systems have specific GOP size requirements. To disable GOP size variance: Enter 0. MediaConvert will only create IDR-frames at the start of your outputâs cadence-driven GOP. Use when your downstream systems require a regular GOP size.

NumberBFramesBetweenReferenceFrames -> (integer)

Specify the number of B-frames that MediaConvert puts between reference frames in this output. Valid values are whole numbers from 0 through 7. When you donât specify a value, MediaConvert defaults to 2.

ParControl -> (string)

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.

ParDenominator -> (integer)

Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33.

ParNumerator -> (integer)

Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40.

PerFrameMetrics -> (list)

Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: * PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

(string)

- PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

QualityTuningLevel -> (string)

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding.

RateControlMode -> (string)

Use Rate control mode to specify whether the bitrate is variable (vbr) or constant (cbr).

ScanTypeConversionMode -> (string)

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isnât suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You canât use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.

SceneChangeDetect -> (string)

Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default.

SlowPal -> (string)

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25.

Softness -> (integer)

Ignore this setting unless you need to comply with a specification that requires a specific value. If you donât have a specification requirement, we recommend that you adjust the softness of your output by using a lower value for the setting Sharpness or by enabling a noise reducer filter. The Softness setting specifies the quantization matrices that the encoder uses. Keep the default value, 0, to use the AWS Elemental default matrices. Choose a value from 17 to 128 to use planar interpolation. Increasing values from 17 to 128 result in increasing reduction of high-frequency data. The value 128 results in the softest video.

SpatialAdaptiveQuantization -> (string)

Keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesnât take into account where the viewerâs attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher.

Syntax -> (string)

Specify whether this outputâs video uses the D10 syntax. Keep the default value to not use the syntax. Related settings: When you choose D10 for your MXF profile, you must also set this value to D10.

Telecine -> (string)

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard or soft telecine to create a smoother picture. Hard telecine produces a 29.97i output. Soft telecine produces an output with a 23.976 output that signals to the video player device to do the conversion during play back. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.

TemporalAdaptiveQuantization -> (string)

Keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that arenât moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesnât take into account where the viewerâs attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesnât have moving objects with sharp edges, such as sports athletesâ faces, you might choose to disable this feature. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization.

ProresSettings -> (structure)

Required when you set Codec to the value PRORES.

ChromaSampling -> (string)

This setting applies only to ProRes 4444 and ProRes 4444 XQ outputs that you create from inputs that use 4:4:4 chroma sampling. Set Preserve 4:4:4 sampling to allow outputs to also use 4:4:4 chroma sampling. You must specify a value for this setting when your output codec profile supports 4:4:4 chroma sampling. Related Settings: For Apple ProRes outputs with 4:4:4 chroma sampling: Choose Preserve 4:4:4 sampling. Use when your input has 4:4:4 chroma sampling and your output codec Profile is Apple ProRes 4444 or 4444 XQ. Note that when you choose Preserve 4:4:4 sampling, you cannot include any of the following Preprocessors: Dolby Vision, HDR10+, or Noise reducer.

CodecProfile -> (string)

Use Profile to specify the type of Apple ProRes codec to use for this output.

FramerateControl -> (string)

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.

FramerateConversionAlgorithm -> (string)

Choose the method that you want MediaConvert to use when increasing or decreasing your videoâs frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.

FramerateDenominator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

FramerateNumerator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

InterlaceMode -> (string)

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output thatâs interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.

ParControl -> (string)

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.

ParDenominator -> (integer)

Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33.

ParNumerator -> (integer)

Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40.

PerFrameMetrics -> (list)

Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: * PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

(string)

- PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

ScanTypeConversionMode -> (string)

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isnât suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You canât use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.

SlowPal -> (string)

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25.

Telecine -> (string)

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.

UncompressedSettings -> (structure)

Required when you set Codec, under VideoDescription>CodecSettings to the value UNCOMPRESSED.

Fourcc -> (string)

The four character code for the uncompressed video.

FramerateControl -> (string)

Use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.

FramerateConversionAlgorithm -> (string)

Choose the method that you want MediaConvert to use when increasing or decreasing your videoâs frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.

FramerateDenominator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

FramerateNumerator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

InterlaceMode -> (string)

Optional. Choose the scan line type for this output. If you donât specify a value, MediaConvert will create a progressive output.

ScanTypeConversionMode -> (string)

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isnât suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You canât use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.

SlowPal -> (string)

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Framerate to 25.

Telecine -> (string)

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.

Vc3Settings -> (structure)

Required when you set Codec to the value VC3

FramerateControl -> (string)

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.

FramerateConversionAlgorithm -> (string)

Choose the method that you want MediaConvert to use when increasing or decreasing your videoâs frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.

FramerateDenominator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

FramerateNumerator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

InterlaceMode -> (string)

Optional. Choose the scan line type for this output. If you donât specify a value, MediaConvert will create a progressive output.

ScanTypeConversionMode -> (string)

Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isnât suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You canât use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive.

SlowPal -> (string)

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Framerate to 25.

Telecine -> (string)

When you do frame rate conversion from 23.976 frames per second (fps) to 29.97 fps, and your output scan type is interlaced, you can optionally enable hard telecine to create a smoother picture. When you keep the default value, None, MediaConvert does a standard frame rate conversion to 29.97 without doing anything with the field polarity to create a smoother picture.

Vc3Class -> (string)

Specify the VC3 class to choose the quality characteristics for this output. VC3 class, together with the settings Framerate (framerateNumerator and framerateDenominator) and Resolution (height and width), determine your output bitrate. For example, say that your video resolution is 1920x1080 and your framerate is 29.97. Then Class 145 gives you an output with a bitrate of approximately 145 Mbps and Class 220 gives you and output with a bitrate of approximately 220 Mbps. VC3 class also specifies the color bit depth of your output.

Vp8Settings -> (structure)

Required when you set Codec to the value VP8.

Bitrate -> (integer)

Target bitrate in bits/second. For example, enter five megabits per second as 5000000.

FramerateControl -> (string)

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.

FramerateConversionAlgorithm -> (string)

Choose the method that you want MediaConvert to use when increasing or decreasing your videoâs frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.

FramerateDenominator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

FramerateNumerator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

GopSize -> (double)

GOP Length (keyframe interval) in frames. Must be greater than zero.

HrdBufferSize -> (integer)

Optional. Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000.

MaxBitrate -> (integer)

Ignore this setting unless you set qualityTuningLevel to MULTI_PASS. Optional. Specify the maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. The default behavior uses twice the target bitrate as the maximum bitrate.

ParControl -> (string)

Optional. Specify how the service determines the pixel aspect ratio (PAR) for this output. The default behavior, Follow source, uses the PAR from your input video for your output. To specify a different PAR in the console, choose any value other than Follow source. When you choose SPECIFIED for this setting, you must also specify values for the parNumerator and parDenominator settings.

ParDenominator -> (integer)

Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33.

ParNumerator -> (integer)

Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40.

QualityTuningLevel -> (string)

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, multi-pass encoding.

RateControlMode -> (string)

With the VP8 codec, you can use only the variable bitrate (VBR) rate control mode.

Vp9Settings -> (structure)

Required when you set Codec to the value VP9.

Bitrate -> (integer)

Target bitrate in bits/second. For example, enter five megabits per second as 5000000.

FramerateControl -> (string)

If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction.

FramerateConversionAlgorithm -> (string)

Choose the method that you want MediaConvert to use when increasing or decreasing your videoâs frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.

FramerateDenominator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

FramerateNumerator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

GopSize -> (double)

GOP Length (keyframe interval) in frames. Must be greater than zero.

HrdBufferSize -> (integer)

Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000.

MaxBitrate -> (integer)

Ignore this setting unless you set qualityTuningLevel to MULTI_PASS. Optional. Specify the maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. The default behavior uses twice the target bitrate as the maximum bitrate.

ParControl -> (string)

Optional. Specify how the service determines the pixel aspect ratio for this output. The default behavior is to use the same pixel aspect ratio as your input video.

ParDenominator -> (integer)

Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parDenominator is 33.

ParNumerator -> (integer)

Required when you set Pixel aspect ratio to SPECIFIED. On the console, this corresponds to any value other than Follow source. When you specify an output pixel aspect ratio (PAR) that is different from your input video PAR, provide your output PAR as a ratio. For example, for D1/DV NTSC widescreen, you would specify the ratio 40:33. In this example, the value for parNumerator is 40.

QualityTuningLevel -> (string)

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, multi-pass encoding.

RateControlMode -> (string)

With the VP9 codec, you can use only the variable bitrate (VBR) rate control mode.

XavcSettings -> (structure)

Required when you set Codec to the value XAVC.

AdaptiveQuantization -> (string)

Keep the default value, Auto, for this setting to have MediaConvert automatically apply the best types of quantization for your video content. When you want to apply your quantization settings manually, you must set Adaptive quantization to a value other than Auto. Use this setting to specify the strength of any adaptive quantization filters that you enable. If you donât want MediaConvert to do any adaptive quantization in this transcode, set Adaptive quantization to Off. Related settings: The value that you choose here applies to the following settings: Flicker adaptive quantization (flickerAdaptiveQuantization), Spatial adaptive quantization, and Temporal adaptive quantization.

EntropyEncoding -> (string)

Optional. Choose a specific entropy encoding mode only when you want to override XAVC recommendations. If you choose the value auto, MediaConvert uses the mode that the XAVC file format specifies given this outputâs operating point.

FramerateControl -> (string)

If you are using the console, use the Frame rate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list. The framerates shown in the dropdown list are decimal approximations of fractions.

FramerateConversionAlgorithm -> (string)

Choose the method that you want MediaConvert to use when increasing or decreasing your videoâs frame rate. For numerically simple conversions, such as 60 fps to 30 fps: We recommend that you keep the default value, Drop duplicate. For numerically complex conversions, to avoid stutter: Choose Interpolate. This results in a smooth picture, but might introduce undesirable video artifacts. For complex frame rate conversions, especially if your source video has already been converted from its original cadence: Choose FrameFormer to do motion-compensated interpolation. FrameFormer uses the best conversion method frame by frame. Note that using FrameFormer increases the transcoding time and incurs a significant add-on cost. When you choose FrameFormer, your input video resolution must be at least 128x96. To create an output with the same number of frames as your input: Choose Maintain frame count. When you do, MediaConvert will not drop, interpolate, add, or otherwise change the frame count from your input to your output. Note that since the frame count is maintained, the duration of your output will become shorter at higher frame rates and longer at lower frame rates.

FramerateDenominator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Frame rate. In this example, specify 23.976.

FramerateNumerator -> (integer)

When you use the API for transcode jobs that use frame rate conversion, specify the frame rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator. When you use the console for transcode jobs that use frame rate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.

PerFrameMetrics -> (list)

Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: * PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

(string)

- PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode.

Profile -> (string)

Specify the XAVC profile for this output. For more information, see the Sony documentation at [https://www.xavc-info.org/](https://www.xavc-info.org/). Note that MediaConvert doesnât support the interlaced video XAVC operating points for XAVC_HD_INTRA_CBG. To create an interlaced XAVC output, choose the profile XAVC_HD.

SlowPal -> (string)

Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Frame rate to 25.

Softness -> (integer)

Ignore this setting unless your downstream workflow requires that you specify it explicitly. Otherwise, we recommend that you adjust the softness of your output by using a lower value for the setting Sharpness or by enabling a noise reducer filter. The Softness setting specifies the quantization matrices that the encoder uses. Keep the default value, 0, for flat quantization. Choose the value 1 or 16 to use the default JVT softening quantization matricies from the H.264 specification. Choose a value from 17 to 128 to use planar interpolation. Increasing values from 17 to 128 result in increasing reduction of high-frequency data. The value 128 results in the softest video.

SpatialAdaptiveQuantization -> (string)

The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. For this setting, keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesnât take into account where the viewerâs attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher.

TemporalAdaptiveQuantization -> (string)

The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. For this setting, keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that arenât moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesnât take into account where the viewerâs attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesnât have moving objects with sharp edges, such as sports athletesâ faces, you might choose to disable this feature. Related setting: When you enable temporal adaptive quantization, adjust the strength of the filter with the setting Adaptive quantization.

Xavc4kIntraCbgProfileSettings -> (structure)

Required when you set Profile to the value XAVC_4K_INTRA_CBG.

XavcClass -> (string)

Specify the XAVC Intra 4k (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class.

Xavc4kIntraVbrProfileSettings -> (structure)

Required when you set Profile to the value XAVC_4K_INTRA_VBR.

XavcClass -> (string)

Specify the XAVC Intra 4k (VBR) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class.

Xavc4kProfileSettings -> (structure)

Required when you set Profile to the value XAVC_4K.

BitrateClass -> (string)

Specify the XAVC 4k (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class.

CodecProfile -> (string)

Specify the codec profile for this output. Choose High, 8-bit, 4:2:0 (HIGH) or High, 10-bit, 4:2:2 (HIGH_422). These profiles are specified in ITU-T H.264.

FlickerAdaptiveQuantization -> (string)

The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set Adaptive quantization to a value other than Off or Auto. Use Adaptive quantization to adjust the degree of smoothing that Flicker adaptive quantization provides.

GopBReference -> (string)

Specify whether the encoder uses B-frames as reference frames for other pictures in the same GOP. Choose Allow to allow the encoder to use B-frames as reference frames. Choose Donât allow to prevent the encoder from using B-frames as reference frames.

GopClosedCadence -> (integer)

Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.

HrdBufferSize -> (integer)

Specify the size of the buffer that MediaConvert uses in the HRD buffer model for this output. Specify this value in bits; for example, enter five megabits as 5000000. When you donât set this value, or you set it to zero, MediaConvert calculates the default by doubling the bitrate of this output point.

QualityTuningLevel -> (string)

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding.

Slices -> (integer)

Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures.

XavcHdIntraCbgProfileSettings -> (structure)

Required when you set Profile to the value XAVC_HD_INTRA_CBG.

XavcClass -> (string)

Specify the XAVC Intra HD (CBG) Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class.

XavcHdProfileSettings -> (structure)

Required when you set Profile to the value XAVC_HD.

BitrateClass -> (string)

Specify the XAVC HD (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class.

FlickerAdaptiveQuantization -> (string)

The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set Adaptive quantization to a value other than Off or Auto. Use Adaptive quantization to adjust the degree of smoothing that Flicker adaptive quantization provides.

GopBReference -> (string)

Specify whether the encoder uses B-frames as reference frames for other pictures in the same GOP. Choose Allow to allow the encoder to use B-frames as reference frames. Choose Donât allow to prevent the encoder from using B-frames as reference frames.

GopClosedCadence -> (integer)

Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.

HrdBufferSize -> (integer)

Specify the size of the buffer that MediaConvert uses in the HRD buffer model for this output. Specify this value in bits; for example, enter five megabits as 5000000. When you donât set this value, or you set it to zero, MediaConvert calculates the default by doubling the bitrate of this output point.

InterlaceMode -> (string)

Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output thatâs interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose.

QualityTuningLevel -> (string)

Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding.

Slices -> (integer)

Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures.

Telecine -> (string)

Ignore this setting unless you set Frame rate (framerateNumerator divided by framerateDenominator) to 29.970. If your input framerate is 23.976, choose Hard. Otherwise, keep the default value None. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-telecine-and-inverse-telecine.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-telecine-and-inverse-telecine.html).

ColorMetadata -> (string)

Choose Insert for this setting to include color metadata in this output. Choose Ignore to exclude color metadata from this output. If you donât specify a value, the service sets this to Insert by default.

Crop -> (structure)

Use Cropping selection to specify the video area that the service will include in the output video frame.

Height -> (integer)

Height of rectangle in pixels. Specify only even numbers.

Width -> (integer)

Width of rectangle in pixels. Specify only even numbers.

X -> (integer)

The distance, in pixels, between the rectangle and the left edge of the video frame. Specify only even numbers.

Y -> (integer)

The distance, in pixels, between the rectangle and the top edge of the video frame. Specify only even numbers.

DropFrameTimecode -> (string)

Applies only to 29.97 fps outputs. When this feature is enabled, the service will use drop-frame timecode on outputs. If it is not possible to use drop-frame timecode, the system will fall back to non-drop-frame. This setting is enabled by default when Timecode insertion or Timecode track is enabled.

FixedAfd -> (integer)

Applies only if you set AFD Signaling to Fixed. Use Fixed to specify a four-bit AFD value which the service will write on all frames of this video output.

Height -> (integer)

Use Height to define the video resolution height, in pixels, for this output. To use the same resolution as your input: Leave both Width and Height blank. To evenly scale from your input resolution: Leave Height blank and enter a value for Width. For example, if your input is 1920x1080 and you set Width to 1280, your output will be 1280x720.

Position -> (structure)

Use Selection placement to define the video area in your output frame. The area outside of the rectangle that you specify here is black.

Height -> (integer)

Height of rectangle in pixels. Specify only even numbers.

Width -> (integer)

Width of rectangle in pixels. Specify only even numbers.

X -> (integer)

The distance, in pixels, between the rectangle and the left edge of the video frame. Specify only even numbers.

Y -> (integer)

The distance, in pixels, between the rectangle and the top edge of the video frame. Specify only even numbers.

RespondToAfd -> (string)

Use Respond to AFD to specify how the service changes the video itself in response to AFD values in the input. * Choose Respond to clip the input video frame according to the AFD value, input display aspect ratio, and output display aspect ratio. * Choose Passthrough to include the input AFD values. Do not choose this when AfdSignaling is set to NONE. A preferred implementation of this workflow is to set RespondToAfd to and set AfdSignaling to AUTO. * Choose None to remove all input AFD values from this output.

ScalingBehavior -> (string)

Specify the video Scaling behavior when your output has a different resolution than your input. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/video-scaling.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/video-scaling.html)

Sharpness -> (integer)

Use Sharpness setting to specify the strength of anti-aliasing. This setting changes the width of the anti-alias filter kernel used for scaling. Sharpness only applies if your output resolution is different from your input resolution. 0 is the softest setting, 100 the sharpest, and 50 recommended for most content.

TimecodeInsertion -> (string)

Applies only to H.264, H.265, MPEG2, and ProRes outputs. Only enable Timecode insertion when the input frame rate is identical to the output frame rate. To include timecodes in this output, set Timecode insertion to PIC_TIMING_SEI. To leave them out, set it to DISABLED. Default is DISABLED. When the service inserts timecodes in an output, by default, it uses any embedded timecodes from the input. If none are present, the service will set the timecode for the first output frame to zero. To change this default behavior, adjust the settings under Timecode configuration. In the console, these settings are located under Job > Job settings > Timecode configuration. Note - Timecode source under input settings does not affect the timecodes that are inserted in the output. Source under Job settings > Timecode configuration does.

TimecodeTrack -> (string)

To include a timecode track in your MP4 output: Choose Enabled. MediaConvert writes the timecode track in the Null Media Header box (NMHD), without any timecode text formatting information. You can also specify dropframe or non-dropframe timecode under the Drop Frame Timecode setting. To not include a timecode track: Keep the default value, Disabled.

VideoPreprocessors -> (structure)

Find additional transcoding features under Preprocessors. Enable the features at each output individually. These features are disabled by default.

ColorCorrector -> (structure)

Use these settings to convert the color space or to modify properties such as hue and contrast for this output. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/converting-the-color-space.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/converting-the-color-space.html).

Brightness -> (integer)

Brightness level.

ClipLimits -> (structure)

Specify YUV limits and RGB tolerances when you set Sample range conversion to Limited range clip.

MaximumRGBTolerance -> (integer)

Specify the Maximum RGB color sample range tolerance for your output. MediaConvert corrects any YUV values that, when converted to RGB, would be outside the upper tolerance that you specify. Enter an integer from 90 to 105 as an offset percentage to the maximum possible value. Leave blank to use the default value 100. When you specify a value for Maximum RGB tolerance, you must set Sample range conversion to Limited range clip.

MaximumYUV -> (integer)

Specify the Maximum YUV color sample limit. MediaConvert conforms any pixels in your input above the value that you specify to typical limited range bounds. Enter an integer from 920 to 1023. Leave blank to use the default value 940. The value that you enter applies to 10-bit ranges. For 8-bit ranges, MediaConvert automatically scales this value down. When you specify a value for Maximum YUV, you must set Sample range conversion to Limited range clip.

MinimumRGBTolerance -> (integer)

Specify the Minimum RGB color sample range tolerance for your output. MediaConvert corrects any YUV values that, when converted to RGB, would be outside the lower tolerance that you specify. Enter an integer from -5 to 10 as an offset percentage to the minimum possible value. Leave blank to use the default value 0. When you specify a value for Minimum RGB tolerance, you must set Sample range conversion to Limited range clip.

MinimumYUV -> (integer)

Specify the Minimum YUV color sample limit. MediaConvert conforms any pixels in your input below the value that you specify to typical limited range bounds. Enter an integer from 0 to 128. Leave blank to use the default value 64. The value that you enter applies to 10-bit ranges. For 8-bit ranges, MediaConvert automatically scales this value down. When you specify a value for Minumum YUV, you must set Sample range conversion to Limited range clip.

ColorSpaceConversion -> (string)

Specify the color space you want for this output. The service supports conversion between HDR formats, between SDR formats, from SDR to HDR, and from HDR to SDR. SDR to HDR conversion doesnât upgrade the dynamic range. The converted video has an HDR format, but visually appears the same as an unconverted output. HDR to SDR conversion uses tone mapping to approximate the outcome of manually regrading from HDR to SDR. When you specify an output color space, MediaConvert uses the following color space metadata, which includes color primaries, transfer characteristics, and matrix coefficients: * HDR 10: BT.2020, PQ, BT.2020 non-constant * HLG 2020: BT.2020, HLG, BT.2020 non-constant * P3DCI (Theater): DCIP3, SMPTE 428M, BT.709 * P3D65 (SDR): Display P3, sRGB, BT.709 * P3D65 (HDR): Display P3, PQ, BT.709

Contrast -> (integer)

Contrast level.

Hdr10Metadata -> (structure)

Use these settings when you convert to the HDR 10 color space. Specify the SMPTE ST 2086 Mastering Display Color Volume static metadata that you want signaled in the output. These values donât affect the pixel values that are encoded in the video stream. They are intended to help the downstream video player display content in a way that reflects the intentions of the the content creator. When you set Color space conversion to HDR 10, these settings are required. You must set values for Max frame average light level and Max content light level; these settings donât have a default value. The default values for the other HDR 10 metadata settings are defined by the P3D65 color space. For more information about MediaConvert HDR jobs, see [https://docs.aws.amazon.com/console/mediaconvert/hdr](https://docs.aws.amazon.com/console/mediaconvert/hdr).

BluePrimaryX -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

BluePrimaryY -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

GreenPrimaryX -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

GreenPrimaryY -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

MaxContentLightLevel -> (integer)

Maximum light level among all samples in the coded video sequence, in units of candelas per square meter. This setting doesnât have a default value; you must specify a value that is suitable for the content.

MaxFrameAverageLightLevel -> (integer)

Maximum average light level of any frame in the coded video sequence, in units of candelas per square meter. This setting doesnât have a default value; you must specify a value that is suitable for the content.

MaxLuminance -> (integer)

Nominal maximum mastering display luminance in units of of 0.0001 candelas per square meter.

MinLuminance -> (integer)

Nominal minimum mastering display luminance in units of of 0.0001 candelas per square meter

RedPrimaryX -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

RedPrimaryY -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

WhitePointX -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

WhitePointY -> (integer)

HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.

HdrToSdrToneMapper -> (string)

Specify how MediaConvert maps brightness and colors from your HDR input to your SDR output. The mode that you select represents a creative choice, with different tradeoffs in the details and tones of your output. To maintain details in bright or saturated areas of your output: Choose Preserve details. For some sources, your SDR output may look less bright and less saturated when compared to your HDR source. MediaConvert automatically applies this mode for HLG sources, regardless of your choice. For a bright and saturated output: Choose Vibrant. We recommend that you choose this mode when any of your source content is HDR10, and for the best results when it is mastered for 1000 nits. You may notice loss of details in bright or saturated areas of your output. HDR to SDR tone mapping has no effect when your input is SDR.

Hue -> (integer)

Hue in degrees.

MaxLuminance -> (integer)

Specify the maximum mastering display luminance. Enter an integer from 0 to 2147483647, in units of 0.0001 nits. For example, enter 10000000 for 1000 nits.

SampleRangeConversion -> (string)

Specify how MediaConvert limits the color sample range for this output. To create a limited range output from a full range input: Choose Limited range squeeze. For full range inputs, MediaConvert performs a linear offset to color samples equally across all pixels and frames. Color samples in 10-bit outputs are limited to 64 through 940, and 8-bit outputs are limited to 16 through 235. Note: For limited range inputs, values for color samples are passed through to your output unchanged. MediaConvert does not limit the sample range. To correct pixels in your input that are out of range or out of gamut: Choose Limited range clip. Use for broadcast applications. MediaConvert conforms any pixels outside of the values that you specify under Minimum YUV and Maximum YUV to limited range bounds. MediaConvert also corrects any YUV values that, when converted to RGB, would be outside the bounds you specify under Minimum RGB tolerance and Maximum RGB tolerance. With either limited range conversion, MediaConvert writes the sample range metadata in the output.

Saturation -> (integer)

Saturation level.

SdrReferenceWhiteLevel -> (integer)

Specify the reference white level, in nits, for all of your SDR inputs. Use to correct brightness levels within HDR10 outputs. The following color metadata must be present in your SDR input: color primaries, transfer characteristics, and matrix coefficients. If your SDR input has missing color metadata, or if you want to correct input color metadata, manually specify a color space in the input video selector. For 1,000 nit peak brightness displays, we recommend that you set SDR reference white level to 203 (according to ITU-R BT.2408). Leave blank to use the default value of 100, or specify an integer from 100 to 1000.

Deinterlacer -> (structure)

Use the deinterlacer to produce smoother motion and a clearer picture. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-scan-type.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-scan-type.html).

Algorithm -> (string)

Only applies when you set Deinterlace mode to Deinterlace or Adaptive. Interpolate produces sharper pictures, while blend produces smoother motion. If your source file includes a ticker, such as a scrolling headline at the bottom of the frame: Choose Interpolate ticker or Blend ticker. To apply field doubling: Choose Linear interpolation. Note that Linear interpolation may introduce video artifacts into your output.

Control -> (string)

- When set to NORMAL (default), the deinterlacer does not convert frames that are tagged in metadata as progressive. It will only convert those that are tagged as some other type. - When set to FORCE_ALL_FRAMES, the deinterlacer converts every frame to progressive - even those that are already tagged as progressive. Turn Force mode on only if there is a good chance that the metadata has tagged frames as progressive when they are not progressive. Do not turn on otherwise; processing frames that are already progressive into progressive will probably result in lower quality video.

Mode -> (string)

Use Deinterlacer to choose how the service will do deinterlacing. Default is Deinterlace. - Deinterlace converts interlaced to progressive. - Inverse telecine converts Hard Telecine 29.97i to progressive 23.976p. - Adaptive auto-detects and converts to progressive.

DolbyVision -> (structure)

Enable Dolby Vision feature to produce Dolby Vision compatible video output.

L6Metadata -> (structure)

Use these settings when you set DolbyVisionLevel6Mode to SPECIFY to override the MaxCLL and MaxFALL values in your input with new values.

MaxCll -> (integer)

Maximum Content Light Level. Static HDR metadata that corresponds to the brightest pixel in the entire stream. Measured in nits.

MaxFall -> (integer)

Maximum Frame-Average Light Level. Static HDR metadata that corresponds to the highest frame-average brightness in the entire stream. Measured in nits.

L6Mode -> (string)

Use Dolby Vision Mode to choose how the service will handle Dolby Vision MaxCLL and MaxFALL properies.

Mapping -> (string)

Required when you set Dolby Vision Profile to Profile 8.1. When you set Content mapping to None, content mapping is not applied to the HDR10-compatible signal. Depending on the source peak nit level, clipping might occur on HDR devices without Dolby Vision. When you set Content mapping to HDR10 1000, the transcoder creates a 1,000 nits peak HDR10-compatible signal by applying static content mapping to the source. This mode is speed-optimized for PQ10 sources with metadata that is created from analysis. For graded Dolby Vision content, be aware that creative intent might not be guaranteed with extreme 1,000 nits trims.

Profile -> (string)

Required when you enable Dolby Vision. Use Profile 5 to include frame-interleaved Dolby Vision metadata in your output. Your input must include Dolby Vision metadata or an HDR10 YUV color space. Use Profile 8.1 to include frame-interleaved Dolby Vision metadata and HDR10 metadata in your output. Your input must include Dolby Vision metadata.

Hdr10Plus -> (structure)

Enable HDR10+ analysis and metadata injection. Compatible with HEVC only.

MasteringMonitorNits -> (integer)

Specify the HDR10+ mastering display normalized peak luminance, in nits. This is the normalized actual peak luminance of the mastering display, as defined by ST 2094-40.

TargetMonitorNits -> (integer)

Specify the HDR10+ target display nominal peak luminance, in nits. This is the nominal maximum luminance of the target display as defined by ST 2094-40.

ImageInserter -> (structure)

Enable the Image inserter feature to include a graphic overlay on your video. Enable or disable this feature for each output individually. This setting is disabled by default.

InsertableImages -> (list)

Specify the images that you want to overlay on your video. The images must be PNG or TGA files.

(structure)

These settings apply to a specific graphic overlay. You can include multiple overlays in your job.

Duration -> (integer)

Specify the time, in milliseconds, for the image to remain on the output video. This duration includes fade-in time but not fade-out time.

FadeIn -> (integer)

Specify the length of time, in milliseconds, between the Start time that you specify for the image insertion and the time that the image appears at full opacity. Full opacity is the level that you specify for the opacity setting. If you donât specify a value for Fade-in, the image will appear abruptly at the overlay start time.

FadeOut -> (integer)

Specify the length of time, in milliseconds, between the end of the time that you have specified for the image overlay Duration and when the overlaid image has faded to total transparency. If you donât specify a value for Fade-out, the image will disappear abruptly at the end of the inserted image duration.

Height -> (integer)

Specify the height of the inserted image in pixels. If you specify a value thatâs larger than the video resolution height, the service will crop your overlaid image to fit. To use the native height of the image, keep this setting blank.

ImageInserterInput -> (string)

Specify the HTTP, HTTPS, or Amazon S3 location of the image that you want to overlay on the video. Use a PNG or TGA file.

ImageX -> (integer)

Specify the distance, in pixels, between the inserted image and the left edge of the video frame. Required for any image overlay that you specify.

ImageY -> (integer)

Specify the distance, in pixels, between the overlaid image and the top edge of the video frame. Required for any image overlay that you specify.

Layer -> (integer)

Specify how overlapping inserted images appear. Images with higher values for Layer appear on top of images with lower values for Layer.

Opacity -> (integer)

Use Opacity to specify how much of the underlying video shows through the inserted image. 0 is transparent and 100 is fully opaque. Default is 50.

StartTime -> (string)

Specify the timecode of the frame that you want the overlay to first appear on. This must be in timecode (HH:MM:SS:FF or HH:MM:SS;FF) format. Remember to take into account your timecode source settings.

Width -> (integer)

Specify the width of the inserted image in pixels. If you specify a value thatâs larger than the video resolution width, the service will crop your overlaid image to fit. To use the native width of the image, keep this setting blank.

SdrReferenceWhiteLevel -> (integer)

Specify the reference white level, in nits, for all of your image inserter images. Use to correct brightness levels within HDR10 outputs. For 1,000 nit peak brightness displays, we recommend that you set SDR reference white level to 203 (according to ITU-R BT.2408). Leave blank to use the default value of 100, or specify an integer from 100 to 1000.

NoiseReducer -> (structure)

Enable the Noise reducer feature to remove noise from your video output if necessary. Enable or disable this feature for each output individually. This setting is disabled by default. When you enable Noise reducer, you must also select a value for Noise reducer filter. For AVC outputs, when you include Noise reducer, you cannot include the Bandwidth reduction filter.

Filter -> (string)

Use Noise reducer filter to select one of the following spatial image filtering functions. To use this setting, you must also enable Noise reducer. * Bilateral preserves edges while reducing noise. * Mean (softest), Gaussian, Lanczos, and Sharpen (sharpest) do convolution filtering. * Conserve does min/max noise reduction. * Spatial does frequency-domain filtering based on JND principles. * Temporal optimizes video quality for complex motion.

FilterSettings -> (structure)

Settings for a noise reducer filter

Strength -> (integer)

Relative strength of noise reducing filter. Higher values produce stronger filtering.

SpatialFilterSettings -> (structure)

Noise reducer filter settings for spatial filter.

PostFilterSharpenStrength -> (integer)

Specify strength of post noise reduction sharpening filter, with 0 disabling the filter and 3 enabling it at maximum strength.

Speed -> (integer)

The speed of the filter, from -2 (lower speed) to 3 (higher speed), with 0 being the nominal value.

Strength -> (integer)

Relative strength of noise reducing filter. Higher values produce stronger filtering.

TemporalFilterSettings -> (structure)

Noise reducer filter settings for temporal filter.

AggressiveMode -> (integer)

Use Aggressive mode for content that has complex motion. Higher values produce stronger temporal filtering. This filters highly complex scenes more aggressively and creates better VQ for low bitrate outputs.

PostTemporalSharpening -> (string)

When you set Noise reducer to Temporal, the bandwidth and sharpness of your output is reduced. You can optionally use Post temporal sharpening to apply sharpening to the edges of your output. Note that Post temporal sharpening will also make the bandwidth reduction from the Noise reducer smaller. The default behavior, Auto, allows the transcoder to determine whether to apply sharpening, depending on your input type and quality. When you set Post temporal sharpening to Enabled, specify how much sharpening is applied using Post temporal sharpening strength. Set Post temporal sharpening to Disabled to not apply sharpening.

PostTemporalSharpeningStrength -> (string)

Use Post temporal sharpening strength to define the amount of sharpening the transcoder applies to your output. Set Post temporal sharpening strength to Low, Medium, or High to indicate the amount of sharpening.

Speed -> (integer)

The speed of the filter (higher number is faster). Low setting reduces bit rate at the cost of transcode time, high setting improves transcode time at the cost of bit rate.

Strength -> (integer)

Specify the strength of the noise reducing filter on this output. Higher values produce stronger filtering. We recommend the following value ranges, depending on the result that you want: * 0-2 for complexity reduction with minimal sharpness loss * 2-8 for complexity reduction with image preservation * 8-16 for a high level of complexity reduction

PartnerWatermarking -> (structure)

If you work with a third party video watermarking partner, use the group of settings that correspond with your watermarking partner to include watermarks in your output.

NexguardFileMarkerSettings -> (structure)

For forensic video watermarking, MediaConvert supports Nagra NexGuard File Marker watermarking. MediaConvert supports both PreRelease Content (NGPR/G2) and OTT Streaming workflows.

License -> (string)

Use the base64 license string that Nagra provides you. Enter it directly in your JSON job specification or in the console. Required when you include Nagra NexGuard File Marker watermarking in your job.

Payload -> (integer)

Specify the payload ID that you want associated with this output. Valid values vary depending on your Nagra NexGuard forensic watermarking workflow. Required when you include Nagra NexGuard File Marker watermarking in your job. For PreRelease Content (NGPR/G2), specify an integer from 1 through 4,194,303. You must generate a unique ID for each asset you watermark, and keep a record of which ID you have assigned to each asset. Neither Nagra nor MediaConvert keep track of the relationship between output files and your IDs. For OTT Streaming, create two adaptive bitrate (ABR) stacks for each asset. Do this by setting up two output groups. For one output group, set the value of Payload ID to 0 in every output. For the other output group, set Payload ID to 1 in every output.

Preset -> (string)

Enter one of the watermarking preset strings that Nagra provides you. Required when you include Nagra NexGuard File Marker watermarking in your job.

Strength -> (string)

Optional. Ignore this setting unless Nagra support directs you to specify a value. When you donât specify a value here, the Nagra NexGuard library uses its default value.

TimecodeBurnin -> (structure)

Settings for burning the output timecode and specified prefix into the output.

FontSize -> (integer)

Use Font size to set the font size of any burned-in timecode. Valid values are 10, 16, 32, 48.

Position -> (string)

Use Position under Timecode burn-in to specify the location the burned-in timecode on output video.

Prefix -> (string)

Use Prefix to place ASCII characters before any burned-in timecode. For example, a prefix of âEZ-â will result in the timecode âEZ-00:00:00:00â. Provide either the characters themselves or the ASCII code equivalents. The supported range of characters is 0x20 through 0x7e. This includes letters, numbers, and all special characters represented on a standard English keyboard.

Width -> (integer)

Use Width to define the video resolution width, in pixels, for this output. To use the same resolution as your input: Leave both Width and Height blank. To evenly scale from your input resolution: Leave Width blank and enter a value for Height. For example, if your input is 1920x1080 and you set Height to 720, your output will be 1280x720.

TimecodeConfig -> (structure)

These settings control how the service handles timecodes throughout the job. These settings donât affect input clipping.

Anchor -> (string)

If you use an editing platform that relies on an anchor timecode, use Anchor Timecode to specify a timecode that will match the input video frame to the output video frame. Use 24-hour format with frame number, (HH:MM:SS:FF) or (HH:MM:SS;FF). This setting ignores frame rate conversion. System behavior for Anchor Timecode varies depending on your setting for Source. * If Source is set to Specified Start, the first input frame is the specified value in Start Timecode. Anchor Timecode and Start Timecode are used calculate output timecode. * If Source is set to Start at 0 the first frame is 00:00:00:00. * If Source is set to Embedded, the first frame is the timecode value on the first input frame of the input.

Source -> (string)

Use Source to set how timecodes are handled within this job. To make sure that your video, audio, captions, and markers are synchronized and that time-based features, such as image inserter, work correctly, choose the Timecode source option that matches your assets. All timecodes are in a 24-hour format with frame number (HH:MM:SS:FF). * Embedded - Use the timecode that is in the input video. If no embedded timecode is in the source, the service will use Start at 0 instead. * Start at 0 - Set the timecode of the initial frame to 00:00:00:00. * Specified Start - Set the timecode of the initial frame to a value other than zero. You use Start timecode to provide this value.

Start -> (string)

Only use when you set Source to Specified start. Use Start timecode to specify the timecode for the initial frame. Use 24-hour format with frame number, (HH:MM:SS:FF) or (HH:MM:SS;FF).

TimestampOffset -> (string)

Only applies to outputs that support program-date-time stamp. Use Timestamp offset to overwrite the timecode date without affecting the time and frame number. Provide the new date as a string in the format âyyyy-mm-ddâ. To use Timestamp offset, you must also enable Insert program-date-time in the output settings. For example, if the date part of your timecodes is 2002-1-25 and you want to change it to one year later, set Timestamp offset to 2003-1-25.

TimedMetadataInsertion -> (structure)

Insert user-defined custom ID3 metadata at timecodes that you specify. In each output that you want to include this metadata, you must set ID3 metadata to Passthrough.

Id3Insertions -> (list)

Id3Insertions contains the array of Id3Insertion instances.

(structure)

To insert ID3 tags in your output, specify two values. Use ID3 tag to specify the base 64 encoded string and use Timecode to specify the time when the tag should be inserted. To insert multiple ID3 tags in your output, create multiple instances of ID3 insertion.

Id3 -> (string)

Use ID3 tag to provide a fully formed ID3 tag in base64-encode format.

Timecode -> (string)

Provide a Timecode in HH:MM:SS:FF or HH:MM:SS;FF format.

SimulateReservedQueue -> (string)

Enable this setting when you run a test job to estimate how many reserved transcoding slots (RTS) you need. When this is enabled, MediaConvert runs your job from an on-demand queue with similar performance to what you will see with one RTS in a reserved queue. This setting is disabled by default.

Status -> (string)

A jobâs status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR.

StatusUpdateInterval -> (string)

Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error.

Timing -> (structure)

Information about when jobs are submitted, started, and finished is specified in Unix epoch format in seconds.

FinishTime -> (timestamp)

The time, in Unix epoch format, that the transcoding job finished

StartTime -> (timestamp)

The time, in Unix epoch format, that transcoding for the job began.

SubmitTime -> (timestamp)

The time, in Unix epoch format, that you submitted the job.

UserMetadata -> (map)

User-defined metadata that you want to associate with an MediaConvert job. You specify metadata in key/value pairs.

key -> (string)

value -> (string)

Warnings -> (list)

Contains any warning messages for the job. Use to help identify potential issues with your input, output, or job. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/warning_codes.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/warning_codes.html)

(structure)

Contains any warning codes and their count for the job.

Code -> (integer)

Warning code that identifies a specific warning in the job. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/warning_codes.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/warning_codes.html)

Count -> (integer)

The number of times this warning occurred in the job.

NextToken -> (string)

Use this string to request the next batch of jobs.