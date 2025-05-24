# probeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/probe.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/probe.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediaconvert](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/index.html#cli-aws-mediaconvert) ]

# probe

## Description

Use Probe to obtain detailed information about your input media files. Probe returns a JSON that includes container, codec, frame rate, resolution, track count, audio layout, captions, and more. You can use this information to learn more about your media files, or to help make decisions while automating your transcoding workflow.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconvert-2017-08-29/Probe)

## Synopsis

```
probe
[--input-files <value>]
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

`--input-files` (list)
Specify a media file to probe.(structure)

The input file that needs to be analyzed.

FileUrl -> (string)

Specify the S3, HTTP, or HTTPS URL for your media file.

Shorthand Syntax:

```
FileUrl=string ...
```

JSON Syntax:

```
[
  {
    "FileUrl": "string"
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

ProbeResults -> (list)

Probe results for your media file.

(structure)

Probe results for your media file.

Container -> (structure)

The container of your media file. This information helps you understand the overall structure and details of your media, including format, duration, and track layout.

Duration -> (double)

The total duration of your media file, in seconds.

Format -> (string)

The format of your media file. For example: MP4, QuickTime (MOV), Matroska (MKV), or WebM. Note that this will be blank if your media file has a format that the MediaConvert Probe operation does not recognize.

Tracks -> (list)

Details about each track (video, audio, or data) in the media file.

(structure)

Details about each track (video, audio, or data) in the media file.

AudioProperties -> (structure)

Details about the media fileâs audio track.

BitDepth -> (integer)

The bit depth of the audio track.

BitRate -> (long)

The bit rate of the audio track, in bits per second.

Channels -> (integer)

The number of audio channels in the audio track.

FrameRate -> (structure)

The frame rate of the video or audio track.

Denominator -> (integer)

The denominator, or bottom number, in the fractional frame rate. For example, if your frame rate is 24000 / 1001 (23.976 frames per second), then the denominator would be 1001.

Numerator -> (integer)

The numerator, or top number, in the fractional frame rate. For example, if your frame rate is 24000 / 1001 (23.976 frames per second), then the numerator would be 24000.

LanguageCode -> (string)

The language code of the audio track, in three character ISO 639-3 format.

SampleRate -> (integer)

The sample rate of the audio track.

Codec -> (string)

The codec of the audio or video track, or caption format of the data track.

DataProperties -> (structure)

Details about the media fileâs data track.

LanguageCode -> (string)

The language code of the data track, in three character ISO 639-3 format.

Duration -> (double)

The duration of the track, in seconds.

Index -> (integer)

The unique index number of the track, starting at 1.

TrackType -> (string)

The type of track: video, audio, or data.

VideoProperties -> (structure)

Details about the media fileâs video track.

BitDepth -> (integer)

The bit depth of the video track.

BitRate -> (long)

The bit rate of the video track, in bits per second.

ColorPrimaries -> (string)

The color space color primaries of the video track.

FrameRate -> (structure)

The frame rate of the video or audio track.

Denominator -> (integer)

The denominator, or bottom number, in the fractional frame rate. For example, if your frame rate is 24000 / 1001 (23.976 frames per second), then the denominator would be 1001.

Numerator -> (integer)

The numerator, or top number, in the fractional frame rate. For example, if your frame rate is 24000 / 1001 (23.976 frames per second), then the numerator would be 24000.

Height -> (integer)

The height of the video track, in pixels.

MatrixCoefficients -> (string)

The color space matrix coefficients of the video track.

TransferCharacteristics -> (string)

The color space transfer characteristics of the video track.

Width -> (integer)

The width of the video track, in pixels.

Metadata -> (structure)

Metadata and other file information.

ETag -> (string)

The entity tag (ETag) of the file.

FileSize -> (long)

The size of the media file, in bytes.

LastModified -> (timestamp)

The last modification timestamp of the media file, in Unix time.

MimeType -> (string)

The MIME type of the media file.

TrackMappings -> (list)

An array containing track mapping information.

(structure)

An array containing track mapping information.

AudioTrackIndexes -> (list)

The index numbers of the audio tracks in your media file.

(integer)

DataTrackIndexes -> (list)

The index numbers of the data tracks in your media file.

(integer)

VideoTrackIndexes -> (list)

The index numbers of the video tracks in your media file.

(integer)