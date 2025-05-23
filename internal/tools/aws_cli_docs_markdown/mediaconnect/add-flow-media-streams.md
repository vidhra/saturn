# add-flow-media-streamsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/add-flow-media-streams.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/add-flow-media-streams.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediaconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/index.html#cli-aws-mediaconnect) ]

# add-flow-media-streams

## Description

Adds media streams to an existing flow. After you add a media stream to a flow, you can associate it with a source and/or an output that uses the ST 2110 JPEG XS or CDI protocol.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/AddFlowMediaStreams)

## Synopsis

```
add-flow-media-streams
--flow-arn <value>
--media-streams <value>
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

`--flow-arn` (string)

The Amazon Resource Name (ARN) of the flow.

`--media-streams` (list)

The media streams that you want to add to the flow.

(structure)

The media stream that you want to add to the flow.

Attributes -> (structure)

The attributes that you want to assign to the new media stream.

Fmtp -> (structure)

The settings that you want to use to define the media stream.

ChannelOrder -> (string)

The format of the audio channel.

Colorimetry -> (string)

The format that is used for the representation of color.

ExactFramerate -> (string)

The frame rate for the video stream, in frames/second. For example: 60000/1001. If you specify a whole number, MediaConnect uses a ratio of N/1. For example, if you specify 60, MediaConnect uses 60/1 as the `exactFramerate` .

Par -> (string)

The pixel aspect ratio (PAR) of the video.

Range -> (string)

The encoding range of the video.

ScanMode -> (string)

The type of compression that was used to smooth the videoâs appearance.

Tcs -> (string)

The transfer characteristic system (TCS) that is used in the video.

Lang -> (string)

The audio language, in a format that is recognized by the receiver.

ClockRate -> (integer)

The sample rate (in Hz) for the stream. If the media stream type is video or ancillary data, set this value to 90000. If the media stream type is audio, set this value to either 48000 or 96000.

Description -> (string)

A description that can help you quickly identify what your media stream is used for.

MediaStreamId -> (integer)

A unique identifier for the media stream.

MediaStreamName -> (string)

A name that helps you distinguish one media stream from another.

MediaStreamType -> (string)

The type of media stream.

VideoFormat -> (string)

The resolution of the video.

Shorthand Syntax:

```
Attributes={Fmtp={ChannelOrder=string,Colorimetry=string,ExactFramerate=string,Par=string,Range=string,ScanMode=string,Tcs=string},Lang=string},ClockRate=integer,Description=string,MediaStreamId=integer,MediaStreamName=string,MediaStreamType=string,VideoFormat=string ...
```

JSON Syntax:

```
[
  {
    "Attributes": {
      "Fmtp": {
        "ChannelOrder": "string",
        "Colorimetry": "BT601"|"BT709"|"BT2020"|"BT2100"|"ST2065-1"|"ST2065-3"|"XYZ",
        "ExactFramerate": "string",
        "Par": "string",
        "Range": "NARROW"|"FULL"|"FULLPROTECT",
        "ScanMode": "progressive"|"interlace"|"progressive-segmented-frame",
        "Tcs": "SDR"|"PQ"|"HLG"|"LINEAR"|"BT2100LINPQ"|"BT2100LINHLG"|"ST2065-1"|"ST428-1"|"DENSITY"
      },
      "Lang": "string"
    },
    "ClockRate": integer,
    "Description": "string",
    "MediaStreamId": integer,
    "MediaStreamName": "string",
    "MediaStreamType": "video"|"audio"|"ancillary-data",
    "VideoFormat": "string"
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

FlowArn -> (string)

The ARN of the flow that you added media streams to.

MediaStreams -> (list)

The media streams that you added to the flow.

(structure)

A media stream represents one component of your content, such as video, audio, or ancillary data. After you add a media stream to your flow, you can associate it with sources and outputs that use the ST 2110 JPEG XS or CDI protocol.

Attributes -> (structure)

Attributes that are related to the media stream.

Fmtp -> (structure)

The settings that you want to use to define the media stream.

ChannelOrder -> (string)

The format of the audio channel.

Colorimetry -> (string)

The format used for the representation of color.

ExactFramerate -> (string)

The frame rate for the video stream, in frames/second. For example: 60000/1001.

Par -> (string)

The pixel aspect ratio (PAR) of the video.

Range -> (string)

The encoding range of the video.

ScanMode -> (string)

The type of compression that was used to smooth the videoâs appearance.

Tcs -> (string)

The transfer characteristic system (TCS) that is used in the video.

Lang -> (string)

The audio language, in a format that is recognized by the receiver.

ClockRate -> (integer)

The sample rate for the stream. This value is measured in Hz.

Description -> (string)

A description that can help you quickly identify what your media stream is used for.

Fmt -> (integer)

The format type number (sometimes referred to as RTP payload type) of the media stream. MediaConnect assigns this value to the media stream. For ST 2110 JPEG XS outputs, you need to provide this value to the receiver.

MediaStreamId -> (integer)

A unique identifier for the media stream.

MediaStreamName -> (string)

A name that helps you distinguish one media stream from another.

MediaStreamType -> (string)

The type of media stream.

VideoFormat -> (string)

The resolution of the video.