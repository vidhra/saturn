# get-segment-detectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-segment-detection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-segment-detection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# get-segment-detection

## Description

Gets the segment detection results of a Amazon Rekognition Video analysis started by  StartSegmentDetection .

Segment detection with Amazon Rekognition Video is an asynchronous operation. You start segment detection by calling  StartSegmentDetection which returns a job identifier (`JobId` ). When the segment detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartSegmentDetection` . To get the results of the segment detection operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED` . if so, call `GetSegmentDetection` and pass the job identifier (`JobId` ) from the initial call of `StartSegmentDetection` .

`GetSegmentDetection` returns detected segments in an array (`Segments` ) of  SegmentDetection objects. `Segments` is sorted by the segment types specified in the `SegmentTypes` input parameter of `StartSegmentDetection` . Each element of the array includes the detected segment, the precentage confidence in the acuracy of the detected segment, the type of the segment, and the frame in which the segment was detected.

Use `SelectedSegmentTypes` to find out the type of segment detection requested in the call to `StartSegmentDetection` .

Use the `MaxResults` parameter to limit the number of segment detections returned. If there are more results than specified in `MaxResults` , the value of `NextToken` in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call `GetSegmentDetection` and populate the `NextToken` request parameter with the token value returned from the previous call to `GetSegmentDetection` .

For more information, see Detecting video segments in stored video in the Amazon Rekognition Developer Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetSegmentDetection)

## Synopsis

```
get-segment-detection
--job-id <value>
[--max-results <value>]
[--next-token <value>]
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

`--job-id` (string)

Job identifier for the text detection operation for which you want results returned. You get the job identifer from an initial call to `StartSegmentDetection` .

`--max-results` (integer)

Maximum number of results to return per paginated call. The largest value you can specify is 1000.

`--next-token` (string)

If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of text.

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

JobStatus -> (string)

Current status of the segment detection job.

StatusMessage -> (string)

If the job fails, `StatusMessage` provides a descriptive error message.

VideoMetadata -> (list)

Currently, Amazon Rekognition Video returns a single object in the `VideoMetadata` array. The object contains information about the video stream in the input file that Amazon Rekognition Video chose to analyze. The `VideoMetadata` object includes the video codec, video format and other information. Video metadata is returned in each page of information returned by `GetSegmentDetection` .

(structure)

Information about a video that Amazon Rekognition analyzed. `Videometadata` is returned in every page of paginated responses from a Amazon Rekognition video operation.

Codec -> (string)

Type of compression used in the analyzed video.

DurationMillis -> (long)

Length of the video in milliseconds.

Format -> (string)

Format of the analyzed video. Possible values are MP4, MOV and AVI.

FrameRate -> (float)

Number of frames per second in the video.

FrameHeight -> (long)

Vertical pixel dimension of the video.

FrameWidth -> (long)

Horizontal pixel dimension of the video.

ColorRange -> (string)

A description of the range of luminance values in a video, either LIMITED (16 to 235) or FULL (0 to 255).

AudioMetadata -> (list)

An array of objects. There can be multiple audio streams. Each `AudioMetadata` object contains metadata for a single audio stream. Audio information in an `AudioMetadata` objects includes the audio codec, the number of audio channels, the duration of the audio stream, and the sample rate. Audio metadata is returned in each page of information returned by `GetSegmentDetection` .

(structure)

Metadata information about an audio stream. An array of `AudioMetadata` objects for the audio streams found in a stored video is returned by  GetSegmentDetection .

Codec -> (string)

The audio codec used to encode or decode the audio stream.

DurationMillis -> (long)

The duration of the audio stream in milliseconds.

SampleRate -> (long)

The sample rate for the audio stream.

NumberOfChannels -> (long)

The number of audio channels in the segment.

NextToken -> (string)

If the previous response was incomplete (because there are more labels to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of text.

Segments -> (list)

An array of segments detected in a video. The array is sorted by the segment types (TECHNICAL_CUE or SHOT) specified in the `SegmentTypes` input parameter of `StartSegmentDetection` . Within each segment type the array is sorted by timestamp values.

(structure)

A technical cue or shot detection segment detected in a video. An array of `SegmentDetection` objects containing all segments detected in a stored video is returned by  GetSegmentDetection .

Type -> (string)

The type of the segment. Valid values are `TECHNICAL_CUE` and `SHOT` .

StartTimestampMillis -> (long)

The start time of the detected segment in milliseconds from the start of the video. This value is rounded down. For example, if the actual timestamp is 100.6667 milliseconds, Amazon Rekognition Video returns a value of 100 millis.

EndTimestampMillis -> (long)

The end time of the detected segment, in milliseconds, from the start of the video. This value is rounded down.

DurationMillis -> (long)

The duration of the detected segment in milliseconds.

StartTimecodeSMPTE -> (string)

The frame-accurate SMPTE timecode, from the start of a video, for the start of a detected segment. `StartTimecode` is in *HH:MM:SS:fr* format (and *;fr* for drop frame-rates).

EndTimecodeSMPTE -> (string)

The frame-accurate SMPTE timecode, from the start of a video, for the end of a detected segment. `EndTimecode` is in *HH:MM:SS:fr* format (and *;fr* for drop frame-rates).

DurationSMPTE -> (string)

The duration of the timecode for the detected segment in SMPTE format.

TechnicalCueSegment -> (structure)

If the segment is a technical cue, contains information about the technical cue.

Type -> (string)

The type of the technical cue.

Confidence -> (float)

The confidence that Amazon Rekognition Video has in the accuracy of the detected segment.

ShotSegment -> (structure)

If the segment is a shot detection, contains information about the shot detection.

Index -> (long)

An Identifier for a shot detection segment detected in a video.

Confidence -> (float)

The confidence that Amazon Rekognition Video has in the accuracy of the detected segment.

StartFrameNumber -> (long)

The frame number of the start of a video segment, using a frame index that starts with 0.

EndFrameNumber -> (long)

The frame number at the end of a video segment, using a frame index that starts with 0.

DurationFrames -> (long)

The duration of a video segment, expressed in frames.

SelectedSegmentTypes -> (list)

An array containing the segment types requested in the call to `StartSegmentDetection` .

(structure)

Information about the type of a segment requested in a call to  StartSegmentDetection . An array of `SegmentTypeInfo` objects is returned by the response from  GetSegmentDetection .

Type -> (string)

The type of a segment (technical cue or shot detection).

ModelVersion -> (string)

The version of the model used to detect segments.

JobId -> (string)

Job identifier for the segment detection operation for which you want to obtain results. The job identifer is returned by an initial call to StartSegmentDetection.

Video -> (structure)

Video file stored in an Amazon S3 bucket. Amazon Rekognition video start operations such as  StartLabelDetection use `Video` to specify a video for analysis. The supported file formats are .mp4, .mov and .avi.

S3Object -> (structure)

The Amazon S3 bucket name and file name for the video.

Bucket -> (string)

Name of the S3 bucket.

Name -> (string)

S3 object key name.

Version -> (string)

If the bucket is versioning enabled, you can specify the object version.

JobTag -> (string)

A job identifier specified in the call to StartSegmentDetection and returned in the job completion notification sent to your Amazon Simple Notification Service topic.