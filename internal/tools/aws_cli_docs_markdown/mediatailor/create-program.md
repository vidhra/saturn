# create-programÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/create-program.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/create-program.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediatailor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/index.html#cli-aws-mediatailor) ]

# create-program

## Description

Creates a program within a channel. For information about programs, see [Working with programs](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-programs.html) in the *MediaTailor User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/CreateProgram)

## Synopsis

```
create-program
[--ad-breaks <value>]
--channel-name <value>
[--live-source-name <value>]
--program-name <value>
--schedule-configuration <value>
--source-location-name <value>
[--vod-source-name <value>]
[--audience-media <value>]
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

`--ad-breaks` (list)

The ad break configuration settings.

(structure)

Ad break configuration parameters.

MessageType -> (string)

The SCTE-35 ad insertion type. Accepted value: `SPLICE_INSERT` , `TIME_SIGNAL` .

OffsetMillis -> (long)

How long (in milliseconds) after the beginning of the program that an ad starts. This value must fall within 100ms of a segment boundary, otherwise the ad break will be skipped.

Slate -> (structure)

Ad break slate configuration.

SourceLocationName -> (string)

The name of the source location where the slate VOD source is stored.

VodSourceName -> (string)

The slate VOD source name. The VOD source must already exist in a source location before it can be used for slate.

SpliceInsertMessage -> (structure)

This defines the SCTE-35 `splice_insert()` message inserted around the ad. For information about using `splice_insert()` , see the SCTE-35 specficiaiton, section 9.7.3.1.

AvailNum -> (integer)

This is written to `splice_insert.avail_num` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0` . Values must be between `0` and `256` , inclusive.

AvailsExpected -> (integer)

This is written to `splice_insert.avails_expected` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0` . Values must be between `0` and `256` , inclusive.

SpliceEventId -> (integer)

This is written to `splice_insert.splice_event_id` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `1` .

UniqueProgramId -> (integer)

This is written to `splice_insert.unique_program_id` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0` . Values must be between `0` and `256` , inclusive.

TimeSignalMessage -> (structure)

Defines the SCTE-35 `time_signal` message inserted around the ad.

Programs on a channelâs schedule can be configured with one or more ad breaks. You can attach a `splice_insert` SCTE-35 message to the ad break. This message provides basic metadata about the ad break.

See section 9.7.4 of the 2022 SCTE-35 specification for more information.

SegmentationDescriptors -> (list)

The configurations for the SCTE-35 `segmentation_descriptor` message(s) sent with the `time_signal` message.

(structure)

The `segmentation_descriptor` message can contain advanced metadata fields, like content identifiers, to convey a wide range of information about the ad break. MediaTailor writes the ad metadata in the egress manifest as part of the `EXT-X-DATERANGE` or `EventStream` ad markerâs SCTE-35 data.

`segmentation_descriptor` messages must be sent with the `time_signal` message type.

See the `segmentation_descriptor()` table of the 2022 SCTE-35 specification for more information.

SegmentationEventId -> (integer)

The Event Identifier to assign to the `segmentation_descriptor.segmentation_event_id` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. The default value is 1.

SegmentationUpidType -> (integer)

The Upid Type to assign to the `segmentation_descriptor.segmentation_upid_type` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is 14.

SegmentationUpid -> (string)

The Upid to assign to the `segmentation_descriptor.segmentation_upid` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. The value must be a hexadecimal string containing only the characters 0 though 9 and A through F. The default value is ââ (an empty string).

SegmentationTypeId -> (integer)

The Type Identifier to assign to the `segmentation_descriptor.segmentation_type_id` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is 48.

SegmentNum -> (integer)

The segment number to assign to the `segmentation_descriptor.segment_num` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification Values must be between 0 and 256, inclusive. The default value is 0.

SegmentsExpected -> (integer)

The number of segments expected, which is assigned to the `segmentation_descriptor.segments_expectedS` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification Values must be between 0 and 256, inclusive. The default value is 0.

SubSegmentNum -> (integer)

The sub-segment number to assign to the `segmentation_descriptor.sub_segment_num` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The defualt value is null.

SubSegmentsExpected -> (integer)

The number of sub-segments expected, which is assigned to the `segmentation_descriptor.sub_segments_expected` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is null.

AdBreakMetadata -> (list)

Defines a list of key/value pairs that MediaTailor generates within the `EXT-X-ASSET` tag for `SCTE35_ENHANCED` output.

(structure)

For `SCTE35_ENHANCED` output, defines a key and corresponding value. MediaTailor generates these pairs within the `EXT-X-ASSET` tag.

Key -> (string)

For `SCTE35_ENHANCED` output, defines a key. MediaTailor takes this key, and its associated value, and generates the key/value pair within the `EXT-X-ASSET` tag. If you specify a key, you must also specify a corresponding value.

Value -> (string)

For `SCTE35_ENHANCED` output, defines a value. MediaTailor; takes this value, and its associated key, and generates the key/value pair within the `EXT-X-ASSET` tag. If you specify a value, you must also specify a corresponding key.

JSON Syntax:

```
[
  {
    "MessageType": "SPLICE_INSERT"|"TIME_SIGNAL",
    "OffsetMillis": long,
    "Slate": {
      "SourceLocationName": "string",
      "VodSourceName": "string"
    },
    "SpliceInsertMessage": {
      "AvailNum": integer,
      "AvailsExpected": integer,
      "SpliceEventId": integer,
      "UniqueProgramId": integer
    },
    "TimeSignalMessage": {
      "SegmentationDescriptors": [
        {
          "SegmentationEventId": integer,
          "SegmentationUpidType": integer,
          "SegmentationUpid": "string",
          "SegmentationTypeId": integer,
          "SegmentNum": integer,
          "SegmentsExpected": integer,
          "SubSegmentNum": integer,
          "SubSegmentsExpected": integer
        }
        ...
      ]
    },
    "AdBreakMetadata": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ]
  }
  ...
]
```

`--channel-name` (string)

The name of the channel for this Program.

`--live-source-name` (string)

The name of the LiveSource for this Program.

`--program-name` (string)

The name of the Program.

`--schedule-configuration` (structure)

The schedule configuration settings.

Transition -> (structure)

Program transition configurations.

DurationMillis -> (long)

The duration of the live program in seconds.

RelativePosition -> (string)

The position where this program will be inserted relative to the `RelativePosition` .

RelativeProgram -> (string)

The name of the program that this program will be inserted next to, as defined by `RelativePosition` .

ScheduledStartTimeMillis -> (long)

The date and time that the program is scheduled to start, in epoch milliseconds.

Type -> (string)

Defines when the program plays in the schedule. You can set the value to `ABSOLUTE` or `RELATIVE` .

`ABSOLUTE` - The program plays at a specific wall clock time. This setting can only be used for channels using the `LINEAR` `PlaybackMode` .

Note the following considerations when using `ABSOLUTE` transitions:

If the preceding program in the schedule has a duration that extends past the wall clock time, MediaTailor truncates the preceding program on a common segment boundary.

If there are gaps in playback, MediaTailor plays the `FillerSlate` you configured for your linear channel.

`RELATIVE` - The program is inserted into the schedule either before or after a program that you specify via `RelativePosition` .

ClipRange -> (structure)

Program clip range configuration.

EndOffsetMillis -> (long)

The end offset of the clip range, in milliseconds, starting from the beginning of the VOD source associated with the program.

StartOffsetMillis -> (long)

The start offset of the clip range, in milliseconds. This offset truncates the start at the number of milliseconds into the duration of the VOD source.

Shorthand Syntax:

```
Transition={DurationMillis=long,RelativePosition=string,RelativeProgram=string,ScheduledStartTimeMillis=long,Type=string},ClipRange={EndOffsetMillis=long,StartOffsetMillis=long}
```

JSON Syntax:

```
{
  "Transition": {
    "DurationMillis": long,
    "RelativePosition": "BEFORE_PROGRAM"|"AFTER_PROGRAM",
    "RelativeProgram": "string",
    "ScheduledStartTimeMillis": long,
    "Type": "string"
  },
  "ClipRange": {
    "EndOffsetMillis": long,
    "StartOffsetMillis": long
  }
}
```

`--source-location-name` (string)

The name of the source location.

`--vod-source-name` (string)

The name thatâs used to refer to a VOD source.

`--audience-media` (list)

The list of AudienceMedia defined in program.

(structure)

An AudienceMedia object contains an Audience and a list of AlternateMedia.

Audience -> (string)

The Audience defined in AudienceMedia.

AlternateMedia -> (list)

The list of AlternateMedia defined in AudienceMedia.

(structure)

A playlist of media (VOD and/or live) to be played instead of the default media on a particular program.

SourceLocationName -> (string)

The name of the source location for alternateMedia.

LiveSourceName -> (string)

The name of the live source for alternateMedia.

VodSourceName -> (string)

The name of the VOD source for alternateMedia.

ClipRange -> (structure)

Clip range configuration for the VOD source associated with the program.

EndOffsetMillis -> (long)

The end offset of the clip range, in milliseconds, starting from the beginning of the VOD source associated with the program.

StartOffsetMillis -> (long)

The start offset of the clip range, in milliseconds. This offset truncates the start at the number of milliseconds into the duration of the VOD source.

ScheduledStartTimeMillis -> (long)

The date and time that the alternateMedia is scheduled to start, in epoch milliseconds.

AdBreaks -> (list)

Ad break configuration parameters defined in AlternateMedia.

(structure)

Ad break configuration parameters.

MessageType -> (string)

The SCTE-35 ad insertion type. Accepted value: `SPLICE_INSERT` , `TIME_SIGNAL` .

OffsetMillis -> (long)

How long (in milliseconds) after the beginning of the program that an ad starts. This value must fall within 100ms of a segment boundary, otherwise the ad break will be skipped.

Slate -> (structure)

Ad break slate configuration.

SourceLocationName -> (string)

The name of the source location where the slate VOD source is stored.

VodSourceName -> (string)

The slate VOD source name. The VOD source must already exist in a source location before it can be used for slate.

SpliceInsertMessage -> (structure)

This defines the SCTE-35 `splice_insert()` message inserted around the ad. For information about using `splice_insert()` , see the SCTE-35 specficiaiton, section 9.7.3.1.

AvailNum -> (integer)

This is written to `splice_insert.avail_num` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0` . Values must be between `0` and `256` , inclusive.

AvailsExpected -> (integer)

This is written to `splice_insert.avails_expected` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0` . Values must be between `0` and `256` , inclusive.

SpliceEventId -> (integer)

This is written to `splice_insert.splice_event_id` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `1` .

UniqueProgramId -> (integer)

This is written to `splice_insert.unique_program_id` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0` . Values must be between `0` and `256` , inclusive.

TimeSignalMessage -> (structure)

Defines the SCTE-35 `time_signal` message inserted around the ad.

Programs on a channelâs schedule can be configured with one or more ad breaks. You can attach a `splice_insert` SCTE-35 message to the ad break. This message provides basic metadata about the ad break.

See section 9.7.4 of the 2022 SCTE-35 specification for more information.

SegmentationDescriptors -> (list)

The configurations for the SCTE-35 `segmentation_descriptor` message(s) sent with the `time_signal` message.

(structure)

The `segmentation_descriptor` message can contain advanced metadata fields, like content identifiers, to convey a wide range of information about the ad break. MediaTailor writes the ad metadata in the egress manifest as part of the `EXT-X-DATERANGE` or `EventStream` ad markerâs SCTE-35 data.

`segmentation_descriptor` messages must be sent with the `time_signal` message type.

See the `segmentation_descriptor()` table of the 2022 SCTE-35 specification for more information.

SegmentationEventId -> (integer)

The Event Identifier to assign to the `segmentation_descriptor.segmentation_event_id` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. The default value is 1.

SegmentationUpidType -> (integer)

The Upid Type to assign to the `segmentation_descriptor.segmentation_upid_type` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is 14.

SegmentationUpid -> (string)

The Upid to assign to the `segmentation_descriptor.segmentation_upid` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. The value must be a hexadecimal string containing only the characters 0 though 9 and A through F. The default value is ââ (an empty string).

SegmentationTypeId -> (integer)

The Type Identifier to assign to the `segmentation_descriptor.segmentation_type_id` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is 48.

SegmentNum -> (integer)

The segment number to assign to the `segmentation_descriptor.segment_num` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification Values must be between 0 and 256, inclusive. The default value is 0.

SegmentsExpected -> (integer)

The number of segments expected, which is assigned to the `segmentation_descriptor.segments_expectedS` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification Values must be between 0 and 256, inclusive. The default value is 0.

SubSegmentNum -> (integer)

The sub-segment number to assign to the `segmentation_descriptor.sub_segment_num` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The defualt value is null.

SubSegmentsExpected -> (integer)

The number of sub-segments expected, which is assigned to the `segmentation_descriptor.sub_segments_expected` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is null.

AdBreakMetadata -> (list)

Defines a list of key/value pairs that MediaTailor generates within the `EXT-X-ASSET` tag for `SCTE35_ENHANCED` output.

(structure)

For `SCTE35_ENHANCED` output, defines a key and corresponding value. MediaTailor generates these pairs within the `EXT-X-ASSET` tag.

Key -> (string)

For `SCTE35_ENHANCED` output, defines a key. MediaTailor takes this key, and its associated value, and generates the key/value pair within the `EXT-X-ASSET` tag. If you specify a key, you must also specify a corresponding value.

Value -> (string)

For `SCTE35_ENHANCED` output, defines a value. MediaTailor; takes this value, and its associated key, and generates the key/value pair within the `EXT-X-ASSET` tag. If you specify a value, you must also specify a corresponding key.

DurationMillis -> (long)

The duration of the alternateMedia in milliseconds.

JSON Syntax:

```
[
  {
    "Audience": "string",
    "AlternateMedia": [
      {
        "SourceLocationName": "string",
        "LiveSourceName": "string",
        "VodSourceName": "string",
        "ClipRange": {
          "EndOffsetMillis": long,
          "StartOffsetMillis": long
        },
        "ScheduledStartTimeMillis": long,
        "AdBreaks": [
          {
            "MessageType": "SPLICE_INSERT"|"TIME_SIGNAL",
            "OffsetMillis": long,
            "Slate": {
              "SourceLocationName": "string",
              "VodSourceName": "string"
            },
            "SpliceInsertMessage": {
              "AvailNum": integer,
              "AvailsExpected": integer,
              "SpliceEventId": integer,
              "UniqueProgramId": integer
            },
            "TimeSignalMessage": {
              "SegmentationDescriptors": [
                {
                  "SegmentationEventId": integer,
                  "SegmentationUpidType": integer,
                  "SegmentationUpid": "string",
                  "SegmentationTypeId": integer,
                  "SegmentNum": integer,
                  "SegmentsExpected": integer,
                  "SubSegmentNum": integer,
                  "SubSegmentsExpected": integer
                }
                ...
              ]
            },
            "AdBreakMetadata": [
              {
                "Key": "string",
                "Value": "string"
              }
              ...
            ]
          }
          ...
        ],
        "DurationMillis": long
      }
      ...
    ]
  }
  ...
]
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

AdBreaks -> (list)

The ad break configuration settings.

(structure)

Ad break configuration parameters.

MessageType -> (string)

The SCTE-35 ad insertion type. Accepted value: `SPLICE_INSERT` , `TIME_SIGNAL` .

OffsetMillis -> (long)

How long (in milliseconds) after the beginning of the program that an ad starts. This value must fall within 100ms of a segment boundary, otherwise the ad break will be skipped.

Slate -> (structure)

Ad break slate configuration.

SourceLocationName -> (string)

The name of the source location where the slate VOD source is stored.

VodSourceName -> (string)

The slate VOD source name. The VOD source must already exist in a source location before it can be used for slate.

SpliceInsertMessage -> (structure)

This defines the SCTE-35 `splice_insert()` message inserted around the ad. For information about using `splice_insert()` , see the SCTE-35 specficiaiton, section 9.7.3.1.

AvailNum -> (integer)

This is written to `splice_insert.avail_num` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0` . Values must be between `0` and `256` , inclusive.

AvailsExpected -> (integer)

This is written to `splice_insert.avails_expected` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0` . Values must be between `0` and `256` , inclusive.

SpliceEventId -> (integer)

This is written to `splice_insert.splice_event_id` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `1` .

UniqueProgramId -> (integer)

This is written to `splice_insert.unique_program_id` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0` . Values must be between `0` and `256` , inclusive.

TimeSignalMessage -> (structure)

Defines the SCTE-35 `time_signal` message inserted around the ad.

Programs on a channelâs schedule can be configured with one or more ad breaks. You can attach a `splice_insert` SCTE-35 message to the ad break. This message provides basic metadata about the ad break.

See section 9.7.4 of the 2022 SCTE-35 specification for more information.

SegmentationDescriptors -> (list)

The configurations for the SCTE-35 `segmentation_descriptor` message(s) sent with the `time_signal` message.

(structure)

The `segmentation_descriptor` message can contain advanced metadata fields, like content identifiers, to convey a wide range of information about the ad break. MediaTailor writes the ad metadata in the egress manifest as part of the `EXT-X-DATERANGE` or `EventStream` ad markerâs SCTE-35 data.

`segmentation_descriptor` messages must be sent with the `time_signal` message type.

See the `segmentation_descriptor()` table of the 2022 SCTE-35 specification for more information.

SegmentationEventId -> (integer)

The Event Identifier to assign to the `segmentation_descriptor.segmentation_event_id` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. The default value is 1.

SegmentationUpidType -> (integer)

The Upid Type to assign to the `segmentation_descriptor.segmentation_upid_type` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is 14.

SegmentationUpid -> (string)

The Upid to assign to the `segmentation_descriptor.segmentation_upid` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. The value must be a hexadecimal string containing only the characters 0 though 9 and A through F. The default value is ââ (an empty string).

SegmentationTypeId -> (integer)

The Type Identifier to assign to the `segmentation_descriptor.segmentation_type_id` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is 48.

SegmentNum -> (integer)

The segment number to assign to the `segmentation_descriptor.segment_num` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification Values must be between 0 and 256, inclusive. The default value is 0.

SegmentsExpected -> (integer)

The number of segments expected, which is assigned to the `segmentation_descriptor.segments_expectedS` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification Values must be between 0 and 256, inclusive. The default value is 0.

SubSegmentNum -> (integer)

The sub-segment number to assign to the `segmentation_descriptor.sub_segment_num` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The defualt value is null.

SubSegmentsExpected -> (integer)

The number of sub-segments expected, which is assigned to the `segmentation_descriptor.sub_segments_expected` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is null.

AdBreakMetadata -> (list)

Defines a list of key/value pairs that MediaTailor generates within the `EXT-X-ASSET` tag for `SCTE35_ENHANCED` output.

(structure)

For `SCTE35_ENHANCED` output, defines a key and corresponding value. MediaTailor generates these pairs within the `EXT-X-ASSET` tag.

Key -> (string)

For `SCTE35_ENHANCED` output, defines a key. MediaTailor takes this key, and its associated value, and generates the key/value pair within the `EXT-X-ASSET` tag. If you specify a key, you must also specify a corresponding value.

Value -> (string)

For `SCTE35_ENHANCED` output, defines a value. MediaTailor; takes this value, and its associated key, and generates the key/value pair within the `EXT-X-ASSET` tag. If you specify a value, you must also specify a corresponding key.

Arn -> (string)

The ARN to assign to the program.

ChannelName -> (string)

The name to assign to the channel for this program.

CreationTime -> (timestamp)

The time the program was created.

LiveSourceName -> (string)

The name of the LiveSource for this Program.

ProgramName -> (string)

The name to assign to this program.

ScheduledStartTime -> (timestamp)

The scheduled start time for this Program.

SourceLocationName -> (string)

The name to assign to the source location for this program.

VodSourceName -> (string)

The name thatâs used to refer to a VOD source.

ClipRange -> (structure)

The clip range configuration settings.

EndOffsetMillis -> (long)

The end offset of the clip range, in milliseconds, starting from the beginning of the VOD source associated with the program.

StartOffsetMillis -> (long)

The start offset of the clip range, in milliseconds. This offset truncates the start at the number of milliseconds into the duration of the VOD source.

DurationMillis -> (long)

The duration of the live program in milliseconds.

AudienceMedia -> (list)

The list of AudienceMedia defined in program.

(structure)

An AudienceMedia object contains an Audience and a list of AlternateMedia.

Audience -> (string)

The Audience defined in AudienceMedia.

AlternateMedia -> (list)

The list of AlternateMedia defined in AudienceMedia.

(structure)

A playlist of media (VOD and/or live) to be played instead of the default media on a particular program.

SourceLocationName -> (string)

The name of the source location for alternateMedia.

LiveSourceName -> (string)

The name of the live source for alternateMedia.

VodSourceName -> (string)

The name of the VOD source for alternateMedia.

ClipRange -> (structure)

Clip range configuration for the VOD source associated with the program.

EndOffsetMillis -> (long)

The end offset of the clip range, in milliseconds, starting from the beginning of the VOD source associated with the program.

StartOffsetMillis -> (long)

The start offset of the clip range, in milliseconds. This offset truncates the start at the number of milliseconds into the duration of the VOD source.

ScheduledStartTimeMillis -> (long)

The date and time that the alternateMedia is scheduled to start, in epoch milliseconds.

AdBreaks -> (list)

Ad break configuration parameters defined in AlternateMedia.

(structure)

Ad break configuration parameters.

MessageType -> (string)

The SCTE-35 ad insertion type. Accepted value: `SPLICE_INSERT` , `TIME_SIGNAL` .

OffsetMillis -> (long)

How long (in milliseconds) after the beginning of the program that an ad starts. This value must fall within 100ms of a segment boundary, otherwise the ad break will be skipped.

Slate -> (structure)

Ad break slate configuration.

SourceLocationName -> (string)

The name of the source location where the slate VOD source is stored.

VodSourceName -> (string)

The slate VOD source name. The VOD source must already exist in a source location before it can be used for slate.

SpliceInsertMessage -> (structure)

This defines the SCTE-35 `splice_insert()` message inserted around the ad. For information about using `splice_insert()` , see the SCTE-35 specficiaiton, section 9.7.3.1.

AvailNum -> (integer)

This is written to `splice_insert.avail_num` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0` . Values must be between `0` and `256` , inclusive.

AvailsExpected -> (integer)

This is written to `splice_insert.avails_expected` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0` . Values must be between `0` and `256` , inclusive.

SpliceEventId -> (integer)

This is written to `splice_insert.splice_event_id` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `1` .

UniqueProgramId -> (integer)

This is written to `splice_insert.unique_program_id` , as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0` . Values must be between `0` and `256` , inclusive.

TimeSignalMessage -> (structure)

Defines the SCTE-35 `time_signal` message inserted around the ad.

Programs on a channelâs schedule can be configured with one or more ad breaks. You can attach a `splice_insert` SCTE-35 message to the ad break. This message provides basic metadata about the ad break.

See section 9.7.4 of the 2022 SCTE-35 specification for more information.

SegmentationDescriptors -> (list)

The configurations for the SCTE-35 `segmentation_descriptor` message(s) sent with the `time_signal` message.

(structure)

The `segmentation_descriptor` message can contain advanced metadata fields, like content identifiers, to convey a wide range of information about the ad break. MediaTailor writes the ad metadata in the egress manifest as part of the `EXT-X-DATERANGE` or `EventStream` ad markerâs SCTE-35 data.

`segmentation_descriptor` messages must be sent with the `time_signal` message type.

See the `segmentation_descriptor()` table of the 2022 SCTE-35 specification for more information.

SegmentationEventId -> (integer)

The Event Identifier to assign to the `segmentation_descriptor.segmentation_event_id` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. The default value is 1.

SegmentationUpidType -> (integer)

The Upid Type to assign to the `segmentation_descriptor.segmentation_upid_type` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is 14.

SegmentationUpid -> (string)

The Upid to assign to the `segmentation_descriptor.segmentation_upid` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. The value must be a hexadecimal string containing only the characters 0 though 9 and A through F. The default value is ââ (an empty string).

SegmentationTypeId -> (integer)

The Type Identifier to assign to the `segmentation_descriptor.segmentation_type_id` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is 48.

SegmentNum -> (integer)

The segment number to assign to the `segmentation_descriptor.segment_num` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification Values must be between 0 and 256, inclusive. The default value is 0.

SegmentsExpected -> (integer)

The number of segments expected, which is assigned to the `segmentation_descriptor.segments_expectedS` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification Values must be between 0 and 256, inclusive. The default value is 0.

SubSegmentNum -> (integer)

The sub-segment number to assign to the `segmentation_descriptor.sub_segment_num` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The defualt value is null.

SubSegmentsExpected -> (integer)

The number of sub-segments expected, which is assigned to the `segmentation_descriptor.sub_segments_expected` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is null.

AdBreakMetadata -> (list)

Defines a list of key/value pairs that MediaTailor generates within the `EXT-X-ASSET` tag for `SCTE35_ENHANCED` output.

(structure)

For `SCTE35_ENHANCED` output, defines a key and corresponding value. MediaTailor generates these pairs within the `EXT-X-ASSET` tag.

Key -> (string)

For `SCTE35_ENHANCED` output, defines a key. MediaTailor takes this key, and its associated value, and generates the key/value pair within the `EXT-X-ASSET` tag. If you specify a key, you must also specify a corresponding value.

Value -> (string)

For `SCTE35_ENHANCED` output, defines a value. MediaTailor; takes this value, and its associated key, and generates the key/value pair within the `EXT-X-ASSET` tag. If you specify a value, you must also specify a corresponding key.

DurationMillis -> (long)

The duration of the alternateMedia in milliseconds.