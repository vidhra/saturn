# get-text-detectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-text-detection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-text-detection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# get-text-detection

## Description

Gets the text detection results of a Amazon Rekognition Video analysis started by  StartTextDetection .

Text detection with Amazon Rekognition Video is an asynchronous operation. You start text detection by calling  StartTextDetection which returns a job identifier (`JobId` ) When the text detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartTextDetection` . To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED` . if so, call `GetTextDetection` and pass the job identifier (`JobId` ) from the initial call of `StartLabelDetection` .

`GetTextDetection` returns an array of detected text (`TextDetections` ) sorted by the time the text was detected, up to 100 words per frame of video.

Each element of the array includes the detected text, the precentage confidence in the acuracy of the detected text, the time the text was detected, bounding box information for where the text was located, and unique identifiers for words and their lines.

Use MaxResults parameter to limit the number of text detections returned. If there are more results than specified in `MaxResults` , the value of `NextToken` in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call `GetTextDetection` and populate the `NextToken` request parameter with the token value returned from the previous call to `GetTextDetection` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetTextDetection)

## Synopsis

```
get-text-detection
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

Job identifier for the text detection operation for which you want results returned. You get the job identifer from an initial call to `StartTextDetection` .

`--max-results` (integer)

Maximum number of results to return per paginated call. The largest value you can specify is 1000.

`--next-token` (string)

If the previous response was incomplete (because there are more labels to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of text.

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

Current status of the text detection job.

StatusMessage -> (string)

If the job fails, `StatusMessage` provides a descriptive error message.

VideoMetadata -> (structure)

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

TextDetections -> (list)

An array of text detected in the video. Each element contains the detected text, the time in milliseconds from the start of the video that the text was detected, and where it was detected on the screen.

(structure)

Information about text detected in a video. Incudes the detected text, the time in milliseconds from the start of the video that the text was detected, and where it was detected on the screen.

Timestamp -> (long)

The time, in milliseconds from the start of the video, that the text was detected. Note that `Timestamp` is not guaranteed to be accurate to the individual frame where the text first appears.

TextDetection -> (structure)

Details about text detected in a video.

DetectedText -> (string)

The word or line of text recognized by Amazon Rekognition.

Type -> (string)

The type of text that was detected.

Id -> (integer)

The identifier for the detected text. The identifier is only unique for a single call to `DetectText` .

ParentId -> (integer)

The Parent identifier for the detected text identified by the value of `ID` . If the type of detected text is `LINE` , the value of `ParentId` is `Null` .

Confidence -> (float)

The confidence that Amazon Rekognition has in the accuracy of the detected text and the accuracy of the geometry points around the detected text.

Geometry -> (structure)

The location of the detected text on the image. Includes an axis aligned coarse bounding box surrounding the text and a finer grain polygon for more accurate spatial information.

BoundingBox -> (structure)

An axis-aligned coarse representation of the detected itemâs location on the image.

Width -> (float)

Width of the bounding box as a ratio of the overall image width.

Height -> (float)

Height of the bounding box as a ratio of the overall image height.

Left -> (float)

Left coordinate of the bounding box as a ratio of overall image width.

Top -> (float)

Top coordinate of the bounding box as a ratio of overall image height.

Polygon -> (list)

Within the bounding box, a fine-grained polygon around the detected item.

(structure)

The X and Y coordinates of a point on an image or video frame. The X and Y values are ratios of the overall image size or video resolution. For example, if an input image is 700x200 and the values are X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the image.

An array of `Point` objects makes up a `Polygon` . A `Polygon` is returned by  DetectText and by  DetectCustomLabels  `Polygon` represents a fine-grained polygon around a detected item. For more information, see Geometry in the Amazon Rekognition Developer Guide.

X -> (float)

The value of the X coordinate for a point on a `Polygon` .

Y -> (float)

The value of the Y coordinate for a point on a `Polygon` .

NextToken -> (string)

If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of text.

TextModelVersion -> (string)

Version number of the text detection model that was used to detect text.

JobId -> (string)

Job identifier for the text detection operation for which you want to obtain results. The job identifer is returned by an initial call to StartTextDetection.

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

A job identifier specified in the call to StartTextDetection and returned in the job completion notification sent to your Amazon Simple Notification Service topic.