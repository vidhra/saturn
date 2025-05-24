# batch-update-scheduleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/batch-update-schedule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/batch-update-schedule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [medialive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/index.html#cli-aws-medialive) ]

# batch-update-schedule

## Description

Update a channel schedule

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/BatchUpdateSchedule)

## Synopsis

```
batch-update-schedule
--channel-id <value>
[--creates <value>]
[--deletes <value>]
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
Id of the channel whose schedule is being updated.

`--creates` (structure)
Schedule actions to create in the schedule.ScheduleActions -> (list)

A list of schedule actions to create.

(structure)

Contains information on a single schedule action.

ActionName -> (string)

The name of the action, must be unique within the schedule. This name provides the main reference to an action once it is added to the schedule. A name is unique if it is no longer in the schedule. The schedule is automatically cleaned up to remove actions with a start time of more than 1 hour ago (approximately) so at that point a name can be reused.

ScheduleActionSettings -> (structure)

Settings for this schedule action.

HlsId3SegmentTaggingSettings -> (structure)

Action to insert ID3 metadata in every segment, in HLS output groups

Tag -> (string)

Complete this parameter if you want to specify only the metadata, not the entire frame. MediaLive will insert the metadata in a TXXX frame. Enter the value as plain text. You can include standard MediaLive variable data such as the current segment number.

Id3 -> (string)

Complete this parameter if you want to specify the entire ID3 metadata. Enter a base64 string that contains one or more fully formed ID3 tags, according to the ID3 specification: [http://id3.org/id3v2.4.0-structure](http://id3.org/id3v2.4.0-structure)

HlsTimedMetadataSettings -> (structure)

Action to insert ID3 metadata once, in HLS output groups

Id3 -> (string)

Enter a base64 string that contains one or more fully formed ID3 tags.See the ID3 specification: [http://id3.org/id3v2.4.0-structure](http://id3.org/id3v2.4.0-structure)

InputPrepareSettings -> (structure)

Action to prepare an input for a future immediate input switch

InputAttachmentNameReference -> (string)

The name of the input attachment that should be prepared by this action. If no name is provided, the action will stop the most recent prepare (if any) when activated.

InputClippingSettings -> (structure)

Settings to let you create a clip of the file input, in order to set up the input to ingest only a portion of the file.

InputTimecodeSource -> (string)

The source of the timecodes in the source being clipped.

StartTimecode -> (structure)

Settings to identify the start of the clip.

Timecode -> (string)

The timecode for the frame where you want to start the clip. Optional; if not specified, the clip starts at first frame in the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF.

StopTimecode -> (structure)

Settings to identify the end of the clip.

LastFrameClippingBehavior -> (string)

If you specify a StopTimecode in an input (in order to clip the file), you can specify if you want the clip to exclude (the default) or include the frame specified by the timecode.

Timecode -> (string)

The timecode for the frame where you want to stop the clip. Optional; if not specified, the clip continues to the end of the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF.

UrlPath -> (list)

The value for the variable portion of the URL for the dynamic input, for this instance of the input. Each time you use the same dynamic input in an input switch action, you can provide a different value, in order to connect the input to a different content source.

(string)

Placeholder documentation for __string

InputSwitchSettings -> (structure)

Action to switch the input

InputAttachmentNameReference -> (string)

The name of the input attachment (not the name of the input!) to switch to. The name is specified in the channel configuration.

InputClippingSettings -> (structure)

Settings to let you create a clip of the file input, in order to set up the input to ingest only a portion of the file.

InputTimecodeSource -> (string)

The source of the timecodes in the source being clipped.

StartTimecode -> (structure)

Settings to identify the start of the clip.

Timecode -> (string)

The timecode for the frame where you want to start the clip. Optional; if not specified, the clip starts at first frame in the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF.

StopTimecode -> (structure)

Settings to identify the end of the clip.

LastFrameClippingBehavior -> (string)

If you specify a StopTimecode in an input (in order to clip the file), you can specify if you want the clip to exclude (the default) or include the frame specified by the timecode.

Timecode -> (string)

The timecode for the frame where you want to stop the clip. Optional; if not specified, the clip continues to the end of the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF.

UrlPath -> (list)

The value for the variable portion of the URL for the dynamic input, for this instance of the input. Each time you use the same dynamic input in an input switch action, you can provide a different value, in order to connect the input to a different content source.

(string)

Placeholder documentation for __string

MotionGraphicsImageActivateSettings -> (structure)

Action to activate a motion graphics image overlay

Duration -> (long)

Duration (in milliseconds) that motion graphics should render on to the video stream. Leaving out this property or setting to 0 will result in rendering continuing until a deactivate action is processed.

PasswordParam -> (string)

Key used to extract the password from EC2 Parameter store

Url -> (string)

URI of the HTML5 content to be rendered into the live stream.

Username -> (string)

Documentation update needed

MotionGraphicsImageDeactivateSettings -> (structure)

Action to deactivate a motion graphics image overlay

PauseStateSettings -> (structure)

Action to pause or unpause one or both channel pipelines

Pipelines -> (list)

Placeholder documentation for __listOfPipelinePauseStateSettings

(structure)

Settings for pausing a pipeline.

PipelineId -> (string)

Pipeline ID to pause (âPIPELINE_0â or âPIPELINE_1â).

Scte35InputSettings -> (structure)

Action to specify scte35 input

InputAttachmentNameReference -> (string)

In fixed mode, enter the name of the input attachment that you want to use as a SCTE-35 input. (Donât enter the ID of the input.)â

Mode -> (string)

Whether the SCTE-35 input should be the active input or a fixed input.

Scte35ReturnToNetworkSettings -> (structure)

Action to insert SCTE-35 return_to_network message

SpliceEventId -> (long)

The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.

Scte35SpliceInsertSettings -> (structure)

Action to insert SCTE-35 splice_insert message

Duration -> (long)

Optional, the duration for the splice_insert, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. If you enter a duration, there is an expectation that the downstream system can read the duration and cue in at that time. If you do not enter a duration, the splice_insert will continue indefinitely and there is an expectation that you will enter a return_to_network to end the splice_insert at the appropriate time.

SpliceEventId -> (long)

The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.

Scte35TimeSignalSettings -> (structure)

Action to insert SCTE-35 time_signal message

Scte35Descriptors -> (list)

The list of SCTE-35 descriptors accompanying the SCTE-35 time_signal.

(structure)

Holds one set of SCTE-35 Descriptor Settings.

Scte35DescriptorSettings -> (structure)

SCTE-35 Descriptor Settings.

SegmentationDescriptorScte35DescriptorSettings -> (structure)

SCTE-35 Segmentation Descriptor.

DeliveryRestrictions -> (structure)

Holds the four SCTE-35 delivery restriction parameters.

ArchiveAllowedFlag -> (string)

Corresponds to SCTE-35 archive_allowed_flag.

DeviceRestrictions -> (string)

Corresponds to SCTE-35 device_restrictions parameter.

NoRegionalBlackoutFlag -> (string)

Corresponds to SCTE-35 no_regional_blackout_flag parameter.

WebDeliveryAllowedFlag -> (string)

Corresponds to SCTE-35 web_delivery_allowed_flag parameter.

SegmentNum -> (integer)

Corresponds to SCTE-35 segment_num. A value that is valid for the specified segmentation_type_id.

SegmentationCancelIndicator -> (string)

Corresponds to SCTE-35 segmentation_event_cancel_indicator.

SegmentationDuration -> (long)

Corresponds to SCTE-35 segmentation_duration. Optional. The duration for the time_signal, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. Enter time in 90 KHz clock ticks. If you do not enter a duration, the time_signal will continue until you insert a cancellation message.

SegmentationEventId -> (long)

Corresponds to SCTE-35 segmentation_event_id.

SegmentationTypeId -> (integer)

Corresponds to SCTE-35 segmentation_type_id. One of the segmentation_type_id values listed in the SCTE-35 specification. On the console, enter the ID in decimal (for example, â52â). In the CLI, API, or an SDK, enter the ID in hex (for example, â0x34â) or decimal (for example, â52â).

SegmentationUpid -> (string)

Corresponds to SCTE-35 segmentation_upid. Enter a string containing the hexadecimal representation of the characters that make up the SCTE-35 segmentation_upid value. Must contain an even number of hex characters. Do not include spaces between each hex pair. For example, the ASCII âADS Informationâ becomes hex â41445320496e666f726d6174696f6e.

SegmentationUpidType -> (integer)

Corresponds to SCTE-35 segmentation_upid_type. On the console, enter one of the types listed in the SCTE-35 specification, converted to a decimal. For example, â0x0Câ hex from the specification is â12â in decimal. In the CLI, API, or an SDK, enter one of the types listed in the SCTE-35 specification, in either hex (for example, â0x0Câ ) or in decimal (for example, â12â).

SegmentsExpected -> (integer)

Corresponds to SCTE-35 segments_expected. A value that is valid for the specified segmentation_type_id.

SubSegmentNum -> (integer)

Corresponds to SCTE-35 sub_segment_num. A value that is valid for the specified segmentation_type_id.

SubSegmentsExpected -> (integer)

Corresponds to SCTE-35 sub_segments_expected. A value that is valid for the specified segmentation_type_id.

StaticImageActivateSettings -> (structure)

Action to activate a static image overlay

Duration -> (integer)

The duration in milliseconds for the image to remain on the video. If omitted or set to 0 the duration is unlimited and the image will remain until it is explicitly deactivated.

FadeIn -> (integer)

The time in milliseconds for the image to fade in. The fade-in starts at the start time of the overlay. Default is 0 (no fade-in).

FadeOut -> (integer)

Applies only if a duration is specified. The time in milliseconds for the image to fade out. The fade-out starts when the duration time is hit, so it effectively extends the duration. Default is 0 (no fade-out).

Height -> (integer)

The height of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified height. Leave blank to use the native height of the overlay.

Image -> (structure)

The location and filename of the image file to overlay on the video. The file must be a 32-bit BMP, PNG, or TGA file, and must not be larger (in pixels) than the input video.

PasswordParam -> (string)

key used to extract the password from EC2 Parameter store

Uri -> (string)

Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a [http://](http://) URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: ârtmp://fmsserver/liveâ.

Username -> (string)

Documentation update needed

ImageX -> (integer)

Placement of the left edge of the overlay relative to the left edge of the video frame, in pixels. 0 (the default) is the left edge of the frame. If the placement causes the overlay to extend beyond the right edge of the underlying video, then the overlay is cropped on the right.

ImageY -> (integer)

Placement of the top edge of the overlay relative to the top edge of the video frame, in pixels. 0 (the default) is the top edge of the frame. If the placement causes the overlay to extend beyond the bottom edge of the underlying video, then the overlay is cropped on the bottom.

Layer -> (integer)

The number of the layer, 0 to 7. There are 8 layers that can be overlaid on the video, each layer with a different image. The layers are in Z order, which means that overlays with higher values of layer are inserted on top of overlays with lower values of layer. Default is 0.

Opacity -> (integer)

Opacity of image where 0 is transparent and 100 is fully opaque. Default is 100.

Width -> (integer)

The width of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified width. Leave blank to use the native width of the overlay.

StaticImageDeactivateSettings -> (structure)

Action to deactivate a static image overlay

FadeOut -> (integer)

The time in milliseconds for the image to fade out. Default is 0 (no fade-out).

Layer -> (integer)

The image overlay layer to deactivate, 0 to 7. Default is 0.

StaticImageOutputActivateSettings -> (structure)

Action to activate a static image overlay in one or more specified outputs

Duration -> (integer)

The duration in milliseconds for the image to remain on the video. If omitted or set to 0 the duration is unlimited and the image will remain until it is explicitly deactivated.

FadeIn -> (integer)

The time in milliseconds for the image to fade in. The fade-in starts at the start time of the overlay. Default is 0 (no fade-in).

FadeOut -> (integer)

Applies only if a duration is specified. The time in milliseconds for the image to fade out. The fade-out starts when the duration time is hit, so it effectively extends the duration. Default is 0 (no fade-out).

Height -> (integer)

The height of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified height. Leave blank to use the native height of the overlay.

Image -> (structure)

The location and filename of the image file to overlay on the video. The file must be a 32-bit BMP, PNG, or TGA file, and must not be larger (in pixels) than the input video.

PasswordParam -> (string)

key used to extract the password from EC2 Parameter store

Uri -> (string)

Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a [http://](http://) URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: ârtmp://fmsserver/liveâ.

Username -> (string)

Documentation update needed

ImageX -> (integer)

Placement of the left edge of the overlay relative to the left edge of the video frame, in pixels. 0 (the default) is the left edge of the frame. If the placement causes the overlay to extend beyond the right edge of the underlying video, then the overlay is cropped on the right.

ImageY -> (integer)

Placement of the top edge of the overlay relative to the top edge of the video frame, in pixels. 0 (the default) is the top edge of the frame. If the placement causes the overlay to extend beyond the bottom edge of the underlying video, then the overlay is cropped on the bottom.

Layer -> (integer)

The number of the layer, 0 to 7. There are 8 layers that can be overlaid on the video, each layer with a different image. The layers are in Z order, which means that overlays with higher values of layer are inserted on top of overlays with lower values of layer. Default is 0.

Opacity -> (integer)

Opacity of image where 0 is transparent and 100 is fully opaque. Default is 100.

OutputNames -> (list)

The name(s) of the output(s) the activation should apply to.

(string)

Placeholder documentation for __string

Width -> (integer)

The width of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified width. Leave blank to use the native width of the overlay.

StaticImageOutputDeactivateSettings -> (structure)

Action to deactivate a static image overlay in one or more specified outputs

FadeOut -> (integer)

The time in milliseconds for the image to fade out. Default is 0 (no fade-out).

Layer -> (integer)

The image overlay layer to deactivate, 0 to 7. Default is 0.

OutputNames -> (list)

The name(s) of the output(s) the deactivation should apply to.

(string)

Placeholder documentation for __string

Id3SegmentTaggingSettings -> (structure)

Action to insert ID3 metadata in every segment, in applicable output groups

Id3 -> (string)

Complete this parameter if you want to specify the entire ID3 metadata. Enter a base64 string that contains one or more fully formed ID3 tags, according to the ID3 specification: [http://id3.org/id3v2.4.0-structure](http://id3.org/id3v2.4.0-structure)

Tag -> (string)

Complete this parameter if you want to specify only the metadata, not the entire frame. MediaLive will insert the metadata in a TXXX frame. Enter the value as plain text. You can include standard MediaLive variable data such as the current segment number.

TimedMetadataSettings -> (structure)

Action to insert ID3 metadata once, in applicable output groups

Id3 -> (string)

Enter a base64 string that contains one or more fully formed ID3 tags.See the ID3 specification: [http://id3.org/id3v2.4.0-structure](http://id3.org/id3v2.4.0-structure)

ScheduleActionStartSettings -> (structure)

The time for the action to start in the channel.

FixedModeScheduleActionStartSettings -> (structure)

Option for specifying the start time for an action.

Time -> (string)

Start time for the action to start in the channel. (Not the time for the action to be added to the schedule: actions are always added to the schedule immediately.) UTC format: yyyy-mm-ddThh:mm:ss.nnnZ. All the letters are digits (for example, mm might be 01) except for the two constants âTâ for time and âZâ for âUTC formatâ.

FollowModeScheduleActionStartSettings -> (structure)

Option for specifying an action as relative to another action.

FollowPoint -> (string)

Identifies whether this action starts relative to the start or relative to the end of the reference action.

ReferenceActionName -> (string)

The action name of another action that this one refers to.

ImmediateModeScheduleActionStartSettings -> (structure)

Option for specifying an action that should be applied immediately.

JSON Syntax:

```
{
  "ScheduleActions": [
    {
      "ActionName": "string",
      "ScheduleActionSettings": {
        "HlsId3SegmentTaggingSettings": {
          "Tag": "string",
          "Id3": "string"
        },
        "HlsTimedMetadataSettings": {
          "Id3": "string"
        },
        "InputPrepareSettings": {
          "InputAttachmentNameReference": "string",
          "InputClippingSettings": {
            "InputTimecodeSource": "ZEROBASED"|"EMBEDDED",
            "StartTimecode": {
              "Timecode": "string"
            },
            "StopTimecode": {
              "LastFrameClippingBehavior": "EXCLUDE_LAST_FRAME"|"INCLUDE_LAST_FRAME",
              "Timecode": "string"
            }
          },
          "UrlPath": ["string", ...]
        },
        "InputSwitchSettings": {
          "InputAttachmentNameReference": "string",
          "InputClippingSettings": {
            "InputTimecodeSource": "ZEROBASED"|"EMBEDDED",
            "StartTimecode": {
              "Timecode": "string"
            },
            "StopTimecode": {
              "LastFrameClippingBehavior": "EXCLUDE_LAST_FRAME"|"INCLUDE_LAST_FRAME",
              "Timecode": "string"
            }
          },
          "UrlPath": ["string", ...]
        },
        "MotionGraphicsImageActivateSettings": {
          "Duration": long,
          "PasswordParam": "string",
          "Url": "string",
          "Username": "string"
        },
        "MotionGraphicsImageDeactivateSettings": {

        },
        "PauseStateSettings": {
          "Pipelines": [
            {
              "PipelineId": "PIPELINE_0"|"PIPELINE_1"
            }
            ...
          ]
        },
        "Scte35InputSettings": {
          "InputAttachmentNameReference": "string",
          "Mode": "FIXED"|"FOLLOW_ACTIVE"
        },
        "Scte35ReturnToNetworkSettings": {
          "SpliceEventId": long
        },
        "Scte35SpliceInsertSettings": {
          "Duration": long,
          "SpliceEventId": long
        },
        "Scte35TimeSignalSettings": {
          "Scte35Descriptors": [
            {
              "Scte35DescriptorSettings": {
                "SegmentationDescriptorScte35DescriptorSettings": {
                  "DeliveryRestrictions": {
                    "ArchiveAllowedFlag": "ARCHIVE_NOT_ALLOWED"|"ARCHIVE_ALLOWED",
                    "DeviceRestrictions": "NONE"|"RESTRICT_GROUP0"|"RESTRICT_GROUP1"|"RESTRICT_GROUP2",
                    "NoRegionalBlackoutFlag": "REGIONAL_BLACKOUT"|"NO_REGIONAL_BLACKOUT",
                    "WebDeliveryAllowedFlag": "WEB_DELIVERY_NOT_ALLOWED"|"WEB_DELIVERY_ALLOWED"
                  },
                  "SegmentNum": integer,
                  "SegmentationCancelIndicator": "SEGMENTATION_EVENT_NOT_CANCELED"|"SEGMENTATION_EVENT_CANCELED",
                  "SegmentationDuration": long,
                  "SegmentationEventId": long,
                  "SegmentationTypeId": integer,
                  "SegmentationUpid": "string",
                  "SegmentationUpidType": integer,
                  "SegmentsExpected": integer,
                  "SubSegmentNum": integer,
                  "SubSegmentsExpected": integer
                }
              }
            }
            ...
          ]
        },
        "StaticImageActivateSettings": {
          "Duration": integer,
          "FadeIn": integer,
          "FadeOut": integer,
          "Height": integer,
          "Image": {
            "PasswordParam": "string",
            "Uri": "string",
            "Username": "string"
          },
          "ImageX": integer,
          "ImageY": integer,
          "Layer": integer,
          "Opacity": integer,
          "Width": integer
        },
        "StaticImageDeactivateSettings": {
          "FadeOut": integer,
          "Layer": integer
        },
        "StaticImageOutputActivateSettings": {
          "Duration": integer,
          "FadeIn": integer,
          "FadeOut": integer,
          "Height": integer,
          "Image": {
            "PasswordParam": "string",
            "Uri": "string",
            "Username": "string"
          },
          "ImageX": integer,
          "ImageY": integer,
          "Layer": integer,
          "Opacity": integer,
          "OutputNames": ["string", ...],
          "Width": integer
        },
        "StaticImageOutputDeactivateSettings": {
          "FadeOut": integer,
          "Layer": integer,
          "OutputNames": ["string", ...]
        },
        "Id3SegmentTaggingSettings": {
          "Id3": "string",
          "Tag": "string"
        },
        "TimedMetadataSettings": {
          "Id3": "string"
        }
      },
      "ScheduleActionStartSettings": {
        "FixedModeScheduleActionStartSettings": {
          "Time": "string"
        },
        "FollowModeScheduleActionStartSettings": {
          "FollowPoint": "END"|"START",
          "ReferenceActionName": "string"
        },
        "ImmediateModeScheduleActionStartSettings": {

        }
      }
    }
    ...
  ]
}
```

`--deletes` (structure)
Schedule actions to delete from the schedule.ActionNames -> (list)

A list of schedule actions to delete.

(string)

Placeholder documentation for __string

Shorthand Syntax:

```
ActionNames=string,string
```

JSON Syntax:

```
{
  "ActionNames": ["string", ...]
}
```

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

Creates -> (structure)

Schedule actions created in the schedule.

ScheduleActions -> (list)

List of actions that have been created in the schedule.

(structure)

Contains information on a single schedule action.

ActionName -> (string)

The name of the action, must be unique within the schedule. This name provides the main reference to an action once it is added to the schedule. A name is unique if it is no longer in the schedule. The schedule is automatically cleaned up to remove actions with a start time of more than 1 hour ago (approximately) so at that point a name can be reused.

ScheduleActionSettings -> (structure)

Settings for this schedule action.

HlsId3SegmentTaggingSettings -> (structure)

Action to insert ID3 metadata in every segment, in HLS output groups

Tag -> (string)

Complete this parameter if you want to specify only the metadata, not the entire frame. MediaLive will insert the metadata in a TXXX frame. Enter the value as plain text. You can include standard MediaLive variable data such as the current segment number.

Id3 -> (string)

Complete this parameter if you want to specify the entire ID3 metadata. Enter a base64 string that contains one or more fully formed ID3 tags, according to the ID3 specification: [http://id3.org/id3v2.4.0-structure](http://id3.org/id3v2.4.0-structure)

HlsTimedMetadataSettings -> (structure)

Action to insert ID3 metadata once, in HLS output groups

Id3 -> (string)

Enter a base64 string that contains one or more fully formed ID3 tags.See the ID3 specification: [http://id3.org/id3v2.4.0-structure](http://id3.org/id3v2.4.0-structure)

InputPrepareSettings -> (structure)

Action to prepare an input for a future immediate input switch

InputAttachmentNameReference -> (string)

The name of the input attachment that should be prepared by this action. If no name is provided, the action will stop the most recent prepare (if any) when activated.

InputClippingSettings -> (structure)

Settings to let you create a clip of the file input, in order to set up the input to ingest only a portion of the file.

InputTimecodeSource -> (string)

The source of the timecodes in the source being clipped.

StartTimecode -> (structure)

Settings to identify the start of the clip.

Timecode -> (string)

The timecode for the frame where you want to start the clip. Optional; if not specified, the clip starts at first frame in the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF.

StopTimecode -> (structure)

Settings to identify the end of the clip.

LastFrameClippingBehavior -> (string)

If you specify a StopTimecode in an input (in order to clip the file), you can specify if you want the clip to exclude (the default) or include the frame specified by the timecode.

Timecode -> (string)

The timecode for the frame where you want to stop the clip. Optional; if not specified, the clip continues to the end of the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF.

UrlPath -> (list)

The value for the variable portion of the URL for the dynamic input, for this instance of the input. Each time you use the same dynamic input in an input switch action, you can provide a different value, in order to connect the input to a different content source.

(string)

Placeholder documentation for __string

InputSwitchSettings -> (structure)

Action to switch the input

InputAttachmentNameReference -> (string)

The name of the input attachment (not the name of the input!) to switch to. The name is specified in the channel configuration.

InputClippingSettings -> (structure)

Settings to let you create a clip of the file input, in order to set up the input to ingest only a portion of the file.

InputTimecodeSource -> (string)

The source of the timecodes in the source being clipped.

StartTimecode -> (structure)

Settings to identify the start of the clip.

Timecode -> (string)

The timecode for the frame where you want to start the clip. Optional; if not specified, the clip starts at first frame in the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF.

StopTimecode -> (structure)

Settings to identify the end of the clip.

LastFrameClippingBehavior -> (string)

If you specify a StopTimecode in an input (in order to clip the file), you can specify if you want the clip to exclude (the default) or include the frame specified by the timecode.

Timecode -> (string)

The timecode for the frame where you want to stop the clip. Optional; if not specified, the clip continues to the end of the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF.

UrlPath -> (list)

The value for the variable portion of the URL for the dynamic input, for this instance of the input. Each time you use the same dynamic input in an input switch action, you can provide a different value, in order to connect the input to a different content source.

(string)

Placeholder documentation for __string

MotionGraphicsImageActivateSettings -> (structure)

Action to activate a motion graphics image overlay

Duration -> (long)

Duration (in milliseconds) that motion graphics should render on to the video stream. Leaving out this property or setting to 0 will result in rendering continuing until a deactivate action is processed.

PasswordParam -> (string)

Key used to extract the password from EC2 Parameter store

Url -> (string)

URI of the HTML5 content to be rendered into the live stream.

Username -> (string)

Documentation update needed

MotionGraphicsImageDeactivateSettings -> (structure)

Action to deactivate a motion graphics image overlay

PauseStateSettings -> (structure)

Action to pause or unpause one or both channel pipelines

Pipelines -> (list)

Placeholder documentation for __listOfPipelinePauseStateSettings

(structure)

Settings for pausing a pipeline.

PipelineId -> (string)

Pipeline ID to pause (âPIPELINE_0â or âPIPELINE_1â).

Scte35InputSettings -> (structure)

Action to specify scte35 input

InputAttachmentNameReference -> (string)

In fixed mode, enter the name of the input attachment that you want to use as a SCTE-35 input. (Donât enter the ID of the input.)â

Mode -> (string)

Whether the SCTE-35 input should be the active input or a fixed input.

Scte35ReturnToNetworkSettings -> (structure)

Action to insert SCTE-35 return_to_network message

SpliceEventId -> (long)

The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.

Scte35SpliceInsertSettings -> (structure)

Action to insert SCTE-35 splice_insert message

Duration -> (long)

Optional, the duration for the splice_insert, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. If you enter a duration, there is an expectation that the downstream system can read the duration and cue in at that time. If you do not enter a duration, the splice_insert will continue indefinitely and there is an expectation that you will enter a return_to_network to end the splice_insert at the appropriate time.

SpliceEventId -> (long)

The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.

Scte35TimeSignalSettings -> (structure)

Action to insert SCTE-35 time_signal message

Scte35Descriptors -> (list)

The list of SCTE-35 descriptors accompanying the SCTE-35 time_signal.

(structure)

Holds one set of SCTE-35 Descriptor Settings.

Scte35DescriptorSettings -> (structure)

SCTE-35 Descriptor Settings.

SegmentationDescriptorScte35DescriptorSettings -> (structure)

SCTE-35 Segmentation Descriptor.

DeliveryRestrictions -> (structure)

Holds the four SCTE-35 delivery restriction parameters.

ArchiveAllowedFlag -> (string)

Corresponds to SCTE-35 archive_allowed_flag.

DeviceRestrictions -> (string)

Corresponds to SCTE-35 device_restrictions parameter.

NoRegionalBlackoutFlag -> (string)

Corresponds to SCTE-35 no_regional_blackout_flag parameter.

WebDeliveryAllowedFlag -> (string)

Corresponds to SCTE-35 web_delivery_allowed_flag parameter.

SegmentNum -> (integer)

Corresponds to SCTE-35 segment_num. A value that is valid for the specified segmentation_type_id.

SegmentationCancelIndicator -> (string)

Corresponds to SCTE-35 segmentation_event_cancel_indicator.

SegmentationDuration -> (long)

Corresponds to SCTE-35 segmentation_duration. Optional. The duration for the time_signal, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. Enter time in 90 KHz clock ticks. If you do not enter a duration, the time_signal will continue until you insert a cancellation message.

SegmentationEventId -> (long)

Corresponds to SCTE-35 segmentation_event_id.

SegmentationTypeId -> (integer)

Corresponds to SCTE-35 segmentation_type_id. One of the segmentation_type_id values listed in the SCTE-35 specification. On the console, enter the ID in decimal (for example, â52â). In the CLI, API, or an SDK, enter the ID in hex (for example, â0x34â) or decimal (for example, â52â).

SegmentationUpid -> (string)

Corresponds to SCTE-35 segmentation_upid. Enter a string containing the hexadecimal representation of the characters that make up the SCTE-35 segmentation_upid value. Must contain an even number of hex characters. Do not include spaces between each hex pair. For example, the ASCII âADS Informationâ becomes hex â41445320496e666f726d6174696f6e.

SegmentationUpidType -> (integer)

Corresponds to SCTE-35 segmentation_upid_type. On the console, enter one of the types listed in the SCTE-35 specification, converted to a decimal. For example, â0x0Câ hex from the specification is â12â in decimal. In the CLI, API, or an SDK, enter one of the types listed in the SCTE-35 specification, in either hex (for example, â0x0Câ ) or in decimal (for example, â12â).

SegmentsExpected -> (integer)

Corresponds to SCTE-35 segments_expected. A value that is valid for the specified segmentation_type_id.

SubSegmentNum -> (integer)

Corresponds to SCTE-35 sub_segment_num. A value that is valid for the specified segmentation_type_id.

SubSegmentsExpected -> (integer)

Corresponds to SCTE-35 sub_segments_expected. A value that is valid for the specified segmentation_type_id.

StaticImageActivateSettings -> (structure)

Action to activate a static image overlay

Duration -> (integer)

The duration in milliseconds for the image to remain on the video. If omitted or set to 0 the duration is unlimited and the image will remain until it is explicitly deactivated.

FadeIn -> (integer)

The time in milliseconds for the image to fade in. The fade-in starts at the start time of the overlay. Default is 0 (no fade-in).

FadeOut -> (integer)

Applies only if a duration is specified. The time in milliseconds for the image to fade out. The fade-out starts when the duration time is hit, so it effectively extends the duration. Default is 0 (no fade-out).

Height -> (integer)

The height of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified height. Leave blank to use the native height of the overlay.

Image -> (structure)

The location and filename of the image file to overlay on the video. The file must be a 32-bit BMP, PNG, or TGA file, and must not be larger (in pixels) than the input video.

PasswordParam -> (string)

key used to extract the password from EC2 Parameter store

Uri -> (string)

Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a [http://](http://) URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: ârtmp://fmsserver/liveâ.

Username -> (string)

Documentation update needed

ImageX -> (integer)

Placement of the left edge of the overlay relative to the left edge of the video frame, in pixels. 0 (the default) is the left edge of the frame. If the placement causes the overlay to extend beyond the right edge of the underlying video, then the overlay is cropped on the right.

ImageY -> (integer)

Placement of the top edge of the overlay relative to the top edge of the video frame, in pixels. 0 (the default) is the top edge of the frame. If the placement causes the overlay to extend beyond the bottom edge of the underlying video, then the overlay is cropped on the bottom.

Layer -> (integer)

The number of the layer, 0 to 7. There are 8 layers that can be overlaid on the video, each layer with a different image. The layers are in Z order, which means that overlays with higher values of layer are inserted on top of overlays with lower values of layer. Default is 0.

Opacity -> (integer)

Opacity of image where 0 is transparent and 100 is fully opaque. Default is 100.

Width -> (integer)

The width of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified width. Leave blank to use the native width of the overlay.

StaticImageDeactivateSettings -> (structure)

Action to deactivate a static image overlay

FadeOut -> (integer)

The time in milliseconds for the image to fade out. Default is 0 (no fade-out).

Layer -> (integer)

The image overlay layer to deactivate, 0 to 7. Default is 0.

StaticImageOutputActivateSettings -> (structure)

Action to activate a static image overlay in one or more specified outputs

Duration -> (integer)

The duration in milliseconds for the image to remain on the video. If omitted or set to 0 the duration is unlimited and the image will remain until it is explicitly deactivated.

FadeIn -> (integer)

The time in milliseconds for the image to fade in. The fade-in starts at the start time of the overlay. Default is 0 (no fade-in).

FadeOut -> (integer)

Applies only if a duration is specified. The time in milliseconds for the image to fade out. The fade-out starts when the duration time is hit, so it effectively extends the duration. Default is 0 (no fade-out).

Height -> (integer)

The height of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified height. Leave blank to use the native height of the overlay.

Image -> (structure)

The location and filename of the image file to overlay on the video. The file must be a 32-bit BMP, PNG, or TGA file, and must not be larger (in pixels) than the input video.

PasswordParam -> (string)

key used to extract the password from EC2 Parameter store

Uri -> (string)

Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a [http://](http://) URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: ârtmp://fmsserver/liveâ.

Username -> (string)

Documentation update needed

ImageX -> (integer)

Placement of the left edge of the overlay relative to the left edge of the video frame, in pixels. 0 (the default) is the left edge of the frame. If the placement causes the overlay to extend beyond the right edge of the underlying video, then the overlay is cropped on the right.

ImageY -> (integer)

Placement of the top edge of the overlay relative to the top edge of the video frame, in pixels. 0 (the default) is the top edge of the frame. If the placement causes the overlay to extend beyond the bottom edge of the underlying video, then the overlay is cropped on the bottom.

Layer -> (integer)

The number of the layer, 0 to 7. There are 8 layers that can be overlaid on the video, each layer with a different image. The layers are in Z order, which means that overlays with higher values of layer are inserted on top of overlays with lower values of layer. Default is 0.

Opacity -> (integer)

Opacity of image where 0 is transparent and 100 is fully opaque. Default is 100.

OutputNames -> (list)

The name(s) of the output(s) the activation should apply to.

(string)

Placeholder documentation for __string

Width -> (integer)

The width of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified width. Leave blank to use the native width of the overlay.

StaticImageOutputDeactivateSettings -> (structure)

Action to deactivate a static image overlay in one or more specified outputs

FadeOut -> (integer)

The time in milliseconds for the image to fade out. Default is 0 (no fade-out).

Layer -> (integer)

The image overlay layer to deactivate, 0 to 7. Default is 0.

OutputNames -> (list)

The name(s) of the output(s) the deactivation should apply to.

(string)

Placeholder documentation for __string

Id3SegmentTaggingSettings -> (structure)

Action to insert ID3 metadata in every segment, in applicable output groups

Id3 -> (string)

Complete this parameter if you want to specify the entire ID3 metadata. Enter a base64 string that contains one or more fully formed ID3 tags, according to the ID3 specification: [http://id3.org/id3v2.4.0-structure](http://id3.org/id3v2.4.0-structure)

Tag -> (string)

Complete this parameter if you want to specify only the metadata, not the entire frame. MediaLive will insert the metadata in a TXXX frame. Enter the value as plain text. You can include standard MediaLive variable data such as the current segment number.

TimedMetadataSettings -> (structure)

Action to insert ID3 metadata once, in applicable output groups

Id3 -> (string)

Enter a base64 string that contains one or more fully formed ID3 tags.See the ID3 specification: [http://id3.org/id3v2.4.0-structure](http://id3.org/id3v2.4.0-structure)

ScheduleActionStartSettings -> (structure)

The time for the action to start in the channel.

FixedModeScheduleActionStartSettings -> (structure)

Option for specifying the start time for an action.

Time -> (string)

Start time for the action to start in the channel. (Not the time for the action to be added to the schedule: actions are always added to the schedule immediately.) UTC format: yyyy-mm-ddThh:mm:ss.nnnZ. All the letters are digits (for example, mm might be 01) except for the two constants âTâ for time and âZâ for âUTC formatâ.

FollowModeScheduleActionStartSettings -> (structure)

Option for specifying an action as relative to another action.

FollowPoint -> (string)

Identifies whether this action starts relative to the start or relative to the end of the reference action.

ReferenceActionName -> (string)

The action name of another action that this one refers to.

ImmediateModeScheduleActionStartSettings -> (structure)

Option for specifying an action that should be applied immediately.

Deletes -> (structure)

Schedule actions deleted from the schedule.

ScheduleActions -> (list)

List of actions that have been deleted from the schedule.

(structure)

Contains information on a single schedule action.

ActionName -> (string)

The name of the action, must be unique within the schedule. This name provides the main reference to an action once it is added to the schedule. A name is unique if it is no longer in the schedule. The schedule is automatically cleaned up to remove actions with a start time of more than 1 hour ago (approximately) so at that point a name can be reused.

ScheduleActionSettings -> (structure)

Settings for this schedule action.

HlsId3SegmentTaggingSettings -> (structure)

Action to insert ID3 metadata in every segment, in HLS output groups

Tag -> (string)

Complete this parameter if you want to specify only the metadata, not the entire frame. MediaLive will insert the metadata in a TXXX frame. Enter the value as plain text. You can include standard MediaLive variable data such as the current segment number.

Id3 -> (string)

Complete this parameter if you want to specify the entire ID3 metadata. Enter a base64 string that contains one or more fully formed ID3 tags, according to the ID3 specification: [http://id3.org/id3v2.4.0-structure](http://id3.org/id3v2.4.0-structure)

HlsTimedMetadataSettings -> (structure)

Action to insert ID3 metadata once, in HLS output groups

Id3 -> (string)

Enter a base64 string that contains one or more fully formed ID3 tags.See the ID3 specification: [http://id3.org/id3v2.4.0-structure](http://id3.org/id3v2.4.0-structure)

InputPrepareSettings -> (structure)

Action to prepare an input for a future immediate input switch

InputAttachmentNameReference -> (string)

The name of the input attachment that should be prepared by this action. If no name is provided, the action will stop the most recent prepare (if any) when activated.

InputClippingSettings -> (structure)

Settings to let you create a clip of the file input, in order to set up the input to ingest only a portion of the file.

InputTimecodeSource -> (string)

The source of the timecodes in the source being clipped.

StartTimecode -> (structure)

Settings to identify the start of the clip.

Timecode -> (string)

The timecode for the frame where you want to start the clip. Optional; if not specified, the clip starts at first frame in the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF.

StopTimecode -> (structure)

Settings to identify the end of the clip.

LastFrameClippingBehavior -> (string)

If you specify a StopTimecode in an input (in order to clip the file), you can specify if you want the clip to exclude (the default) or include the frame specified by the timecode.

Timecode -> (string)

The timecode for the frame where you want to stop the clip. Optional; if not specified, the clip continues to the end of the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF.

UrlPath -> (list)

The value for the variable portion of the URL for the dynamic input, for this instance of the input. Each time you use the same dynamic input in an input switch action, you can provide a different value, in order to connect the input to a different content source.

(string)

Placeholder documentation for __string

InputSwitchSettings -> (structure)

Action to switch the input

InputAttachmentNameReference -> (string)

The name of the input attachment (not the name of the input!) to switch to. The name is specified in the channel configuration.

InputClippingSettings -> (structure)

Settings to let you create a clip of the file input, in order to set up the input to ingest only a portion of the file.

InputTimecodeSource -> (string)

The source of the timecodes in the source being clipped.

StartTimecode -> (structure)

Settings to identify the start of the clip.

Timecode -> (string)

The timecode for the frame where you want to start the clip. Optional; if not specified, the clip starts at first frame in the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF.

StopTimecode -> (structure)

Settings to identify the end of the clip.

LastFrameClippingBehavior -> (string)

If you specify a StopTimecode in an input (in order to clip the file), you can specify if you want the clip to exclude (the default) or include the frame specified by the timecode.

Timecode -> (string)

The timecode for the frame where you want to stop the clip. Optional; if not specified, the clip continues to the end of the file. Enter the timecode as HH:MM:SS:FF or HH:MM:SS;FF.

UrlPath -> (list)

The value for the variable portion of the URL for the dynamic input, for this instance of the input. Each time you use the same dynamic input in an input switch action, you can provide a different value, in order to connect the input to a different content source.

(string)

Placeholder documentation for __string

MotionGraphicsImageActivateSettings -> (structure)

Action to activate a motion graphics image overlay

Duration -> (long)

Duration (in milliseconds) that motion graphics should render on to the video stream. Leaving out this property or setting to 0 will result in rendering continuing until a deactivate action is processed.

PasswordParam -> (string)

Key used to extract the password from EC2 Parameter store

Url -> (string)

URI of the HTML5 content to be rendered into the live stream.

Username -> (string)

Documentation update needed

MotionGraphicsImageDeactivateSettings -> (structure)

Action to deactivate a motion graphics image overlay

PauseStateSettings -> (structure)

Action to pause or unpause one or both channel pipelines

Pipelines -> (list)

Placeholder documentation for __listOfPipelinePauseStateSettings

(structure)

Settings for pausing a pipeline.

PipelineId -> (string)

Pipeline ID to pause (âPIPELINE_0â or âPIPELINE_1â).

Scte35InputSettings -> (structure)

Action to specify scte35 input

InputAttachmentNameReference -> (string)

In fixed mode, enter the name of the input attachment that you want to use as a SCTE-35 input. (Donât enter the ID of the input.)â

Mode -> (string)

Whether the SCTE-35 input should be the active input or a fixed input.

Scte35ReturnToNetworkSettings -> (structure)

Action to insert SCTE-35 return_to_network message

SpliceEventId -> (long)

The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.

Scte35SpliceInsertSettings -> (structure)

Action to insert SCTE-35 splice_insert message

Duration -> (long)

Optional, the duration for the splice_insert, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. If you enter a duration, there is an expectation that the downstream system can read the duration and cue in at that time. If you do not enter a duration, the splice_insert will continue indefinitely and there is an expectation that you will enter a return_to_network to end the splice_insert at the appropriate time.

SpliceEventId -> (long)

The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.

Scte35TimeSignalSettings -> (structure)

Action to insert SCTE-35 time_signal message

Scte35Descriptors -> (list)

The list of SCTE-35 descriptors accompanying the SCTE-35 time_signal.

(structure)

Holds one set of SCTE-35 Descriptor Settings.

Scte35DescriptorSettings -> (structure)

SCTE-35 Descriptor Settings.

SegmentationDescriptorScte35DescriptorSettings -> (structure)

SCTE-35 Segmentation Descriptor.

DeliveryRestrictions -> (structure)

Holds the four SCTE-35 delivery restriction parameters.

ArchiveAllowedFlag -> (string)

Corresponds to SCTE-35 archive_allowed_flag.

DeviceRestrictions -> (string)

Corresponds to SCTE-35 device_restrictions parameter.

NoRegionalBlackoutFlag -> (string)

Corresponds to SCTE-35 no_regional_blackout_flag parameter.

WebDeliveryAllowedFlag -> (string)

Corresponds to SCTE-35 web_delivery_allowed_flag parameter.

SegmentNum -> (integer)

Corresponds to SCTE-35 segment_num. A value that is valid for the specified segmentation_type_id.

SegmentationCancelIndicator -> (string)

Corresponds to SCTE-35 segmentation_event_cancel_indicator.

SegmentationDuration -> (long)

Corresponds to SCTE-35 segmentation_duration. Optional. The duration for the time_signal, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. Enter time in 90 KHz clock ticks. If you do not enter a duration, the time_signal will continue until you insert a cancellation message.

SegmentationEventId -> (long)

Corresponds to SCTE-35 segmentation_event_id.

SegmentationTypeId -> (integer)

Corresponds to SCTE-35 segmentation_type_id. One of the segmentation_type_id values listed in the SCTE-35 specification. On the console, enter the ID in decimal (for example, â52â). In the CLI, API, or an SDK, enter the ID in hex (for example, â0x34â) or decimal (for example, â52â).

SegmentationUpid -> (string)

Corresponds to SCTE-35 segmentation_upid. Enter a string containing the hexadecimal representation of the characters that make up the SCTE-35 segmentation_upid value. Must contain an even number of hex characters. Do not include spaces between each hex pair. For example, the ASCII âADS Informationâ becomes hex â41445320496e666f726d6174696f6e.

SegmentationUpidType -> (integer)

Corresponds to SCTE-35 segmentation_upid_type. On the console, enter one of the types listed in the SCTE-35 specification, converted to a decimal. For example, â0x0Câ hex from the specification is â12â in decimal. In the CLI, API, or an SDK, enter one of the types listed in the SCTE-35 specification, in either hex (for example, â0x0Câ ) or in decimal (for example, â12â).

SegmentsExpected -> (integer)

Corresponds to SCTE-35 segments_expected. A value that is valid for the specified segmentation_type_id.

SubSegmentNum -> (integer)

Corresponds to SCTE-35 sub_segment_num. A value that is valid for the specified segmentation_type_id.

SubSegmentsExpected -> (integer)

Corresponds to SCTE-35 sub_segments_expected. A value that is valid for the specified segmentation_type_id.

StaticImageActivateSettings -> (structure)

Action to activate a static image overlay

Duration -> (integer)

The duration in milliseconds for the image to remain on the video. If omitted or set to 0 the duration is unlimited and the image will remain until it is explicitly deactivated.

FadeIn -> (integer)

The time in milliseconds for the image to fade in. The fade-in starts at the start time of the overlay. Default is 0 (no fade-in).

FadeOut -> (integer)

Applies only if a duration is specified. The time in milliseconds for the image to fade out. The fade-out starts when the duration time is hit, so it effectively extends the duration. Default is 0 (no fade-out).

Height -> (integer)

The height of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified height. Leave blank to use the native height of the overlay.

Image -> (structure)

The location and filename of the image file to overlay on the video. The file must be a 32-bit BMP, PNG, or TGA file, and must not be larger (in pixels) than the input video.

PasswordParam -> (string)

key used to extract the password from EC2 Parameter store

Uri -> (string)

Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a [http://](http://) URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: ârtmp://fmsserver/liveâ.

Username -> (string)

Documentation update needed

ImageX -> (integer)

Placement of the left edge of the overlay relative to the left edge of the video frame, in pixels. 0 (the default) is the left edge of the frame. If the placement causes the overlay to extend beyond the right edge of the underlying video, then the overlay is cropped on the right.

ImageY -> (integer)

Placement of the top edge of the overlay relative to the top edge of the video frame, in pixels. 0 (the default) is the top edge of the frame. If the placement causes the overlay to extend beyond the bottom edge of the underlying video, then the overlay is cropped on the bottom.

Layer -> (integer)

The number of the layer, 0 to 7. There are 8 layers that can be overlaid on the video, each layer with a different image. The layers are in Z order, which means that overlays with higher values of layer are inserted on top of overlays with lower values of layer. Default is 0.

Opacity -> (integer)

Opacity of image where 0 is transparent and 100 is fully opaque. Default is 100.

Width -> (integer)

The width of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified width. Leave blank to use the native width of the overlay.

StaticImageDeactivateSettings -> (structure)

Action to deactivate a static image overlay

FadeOut -> (integer)

The time in milliseconds for the image to fade out. Default is 0 (no fade-out).

Layer -> (integer)

The image overlay layer to deactivate, 0 to 7. Default is 0.

StaticImageOutputActivateSettings -> (structure)

Action to activate a static image overlay in one or more specified outputs

Duration -> (integer)

The duration in milliseconds for the image to remain on the video. If omitted or set to 0 the duration is unlimited and the image will remain until it is explicitly deactivated.

FadeIn -> (integer)

The time in milliseconds for the image to fade in. The fade-in starts at the start time of the overlay. Default is 0 (no fade-in).

FadeOut -> (integer)

Applies only if a duration is specified. The time in milliseconds for the image to fade out. The fade-out starts when the duration time is hit, so it effectively extends the duration. Default is 0 (no fade-out).

Height -> (integer)

The height of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified height. Leave blank to use the native height of the overlay.

Image -> (structure)

The location and filename of the image file to overlay on the video. The file must be a 32-bit BMP, PNG, or TGA file, and must not be larger (in pixels) than the input video.

PasswordParam -> (string)

key used to extract the password from EC2 Parameter store

Uri -> (string)

Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a [http://](http://) URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: ârtmp://fmsserver/liveâ.

Username -> (string)

Documentation update needed

ImageX -> (integer)

Placement of the left edge of the overlay relative to the left edge of the video frame, in pixels. 0 (the default) is the left edge of the frame. If the placement causes the overlay to extend beyond the right edge of the underlying video, then the overlay is cropped on the right.

ImageY -> (integer)

Placement of the top edge of the overlay relative to the top edge of the video frame, in pixels. 0 (the default) is the top edge of the frame. If the placement causes the overlay to extend beyond the bottom edge of the underlying video, then the overlay is cropped on the bottom.

Layer -> (integer)

The number of the layer, 0 to 7. There are 8 layers that can be overlaid on the video, each layer with a different image. The layers are in Z order, which means that overlays with higher values of layer are inserted on top of overlays with lower values of layer. Default is 0.

Opacity -> (integer)

Opacity of image where 0 is transparent and 100 is fully opaque. Default is 100.

OutputNames -> (list)

The name(s) of the output(s) the activation should apply to.

(string)

Placeholder documentation for __string

Width -> (integer)

The width of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified width. Leave blank to use the native width of the overlay.

StaticImageOutputDeactivateSettings -> (structure)

Action to deactivate a static image overlay in one or more specified outputs

FadeOut -> (integer)

The time in milliseconds for the image to fade out. Default is 0 (no fade-out).

Layer -> (integer)

The image overlay layer to deactivate, 0 to 7. Default is 0.

OutputNames -> (list)

The name(s) of the output(s) the deactivation should apply to.

(string)

Placeholder documentation for __string

Id3SegmentTaggingSettings -> (structure)

Action to insert ID3 metadata in every segment, in applicable output groups

Id3 -> (string)

Complete this parameter if you want to specify the entire ID3 metadata. Enter a base64 string that contains one or more fully formed ID3 tags, according to the ID3 specification: [http://id3.org/id3v2.4.0-structure](http://id3.org/id3v2.4.0-structure)

Tag -> (string)

Complete this parameter if you want to specify only the metadata, not the entire frame. MediaLive will insert the metadata in a TXXX frame. Enter the value as plain text. You can include standard MediaLive variable data such as the current segment number.

TimedMetadataSettings -> (structure)

Action to insert ID3 metadata once, in applicable output groups

Id3 -> (string)

Enter a base64 string that contains one or more fully formed ID3 tags.See the ID3 specification: [http://id3.org/id3v2.4.0-structure](http://id3.org/id3v2.4.0-structure)

ScheduleActionStartSettings -> (structure)

The time for the action to start in the channel.

FixedModeScheduleActionStartSettings -> (structure)

Option for specifying the start time for an action.

Time -> (string)

Start time for the action to start in the channel. (Not the time for the action to be added to the schedule: actions are always added to the schedule immediately.) UTC format: yyyy-mm-ddThh:mm:ss.nnnZ. All the letters are digits (for example, mm might be 01) except for the two constants âTâ for time and âZâ for âUTC formatâ.

FollowModeScheduleActionStartSettings -> (structure)

Option for specifying an action as relative to another action.

FollowPoint -> (string)

Identifies whether this action starts relative to the start or relative to the end of the reference action.

ReferenceActionName -> (string)

The action name of another action that this one refers to.

ImmediateModeScheduleActionStartSettings -> (structure)

Option for specifying an action that should be applied immediately.