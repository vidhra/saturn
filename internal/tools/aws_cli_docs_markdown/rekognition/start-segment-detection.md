# start-segment-detectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-segment-detection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-segment-detection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# start-segment-detection

## Description

Starts asynchronous detection of segment detection in a stored video.

Amazon Rekognition Video can detect segments in a video stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. `StartSegmentDetection` returns a job identifier (`JobId` ) which you use to get the results of the operation. When segment detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in `NotificationChannel` .

You can use the `Filters` ( StartSegmentDetectionFilters ) input parameter to specify the minimum detection confidence returned in the response. Within `Filters` , use `ShotFilter` ( StartShotDetectionFilter ) to filter detected shots. Use `TechnicalCueFilter` ( StartTechnicalCueDetectionFilter ) to filter technical cues.

To get the results of the segment detection operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED` . if so, call  GetSegmentDetection and pass the job identifier (`JobId` ) from the initial call to `StartSegmentDetection` .

For more information, see Detecting video segments in stored video in the Amazon Rekognition Developer Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartSegmentDetection)

## Synopsis

```
start-segment-detection
--video <value>
[--client-request-token <value>]
[--notification-channel <value>]
[--job-tag <value>]
[--filters <value>]
--segment-types <value>
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

`--video` (structure)

Video file stored in an Amazon S3 bucket. Amazon Rekognition video start operations such as  StartLabelDetection use `Video` to specify a video for analysis. The supported file formats are .mp4, .mov and .avi.

S3Object -> (structure)

The Amazon S3 bucket name and file name for the video.

Bucket -> (string)

Name of the S3 bucket.

Name -> (string)

S3 object key name.

Version -> (string)

If the bucket is versioning enabled, you can specify the object version.

Shorthand Syntax:

```
S3Object={Bucket=string,Name=string,Version=string}
```

JSON Syntax:

```
{
  "S3Object": {
    "Bucket": "string",
    "Name": "string",
    "Version": "string"
  }
}
```

`--client-request-token` (string)

Idempotent token used to identify the start request. If you use the same token with multiple `StartSegmentDetection` requests, the same `JobId` is returned. Use `ClientRequestToken` to prevent the same job from being accidently started more than once.

`--notification-channel` (structure)

The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the completion status of the segment detection operation. Note that the Amazon SNS topic must have a topic name that begins with *AmazonRekognition* if you are using the AmazonRekognitionServiceRole permissions policy to access the topic.

SNSTopicArn -> (string)

The Amazon SNS topic to which Amazon Rekognition posts the completion status.

RoleArn -> (string)

The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic.

Shorthand Syntax:

```
SNSTopicArn=string,RoleArn=string
```

JSON Syntax:

```
{
  "SNSTopicArn": "string",
  "RoleArn": "string"
}
```

`--job-tag` (string)

An identifier you specify thatâs returned in the completion notification thatâs published to your Amazon Simple Notification Service topic. For example, you can use `JobTag` to group related jobs and identify them in the completion notification.

`--filters` (structure)

Filters for technical cue or shot detection.

TechnicalCueFilter -> (structure)

Filters that are specific to technical cues.

MinSegmentConfidence -> (float)

Specifies the minimum confidence that Amazon Rekognition Video must have in order to return a detected segment. Confidence represents how certain Amazon Rekognition is that a segment is correctly identified. 0 is the lowest confidence. 100 is the highest confidence. Amazon Rekognition Video doesnât return any segments with a confidence level lower than this specified value.

If you donât specify `MinSegmentConfidence` , `GetSegmentDetection` returns segments with confidence values greater than or equal to 50 percent.

BlackFrame -> (structure)

A filter that allows you to control the black frame detection by specifying the black levels and pixel coverage of black pixels in a frame. Videos can come from multiple sources, formats, and time periods, with different standards and varying noise levels for black frames that need to be accounted for.

MaxPixelThreshold -> (float)

A threshold used to determine the maximum luminance value for a pixel to be considered black. In a full color range video, luminance values range from 0-255. A pixel value of 0 is pure black, and the most strict filter. The maximum black pixel value is computed as follows: max_black_pixel_value = minimum_luminance + MaxPixelThreshold [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-segment-detection.html#id1)luminance_range.

For example, for a full range video with BlackPixelThreshold = 0.1, max_black_pixel_value is 0 + 0.1 * (255-0) = 25.5.

The default value of MaxPixelThreshold is 0.2, which maps to a max_black_pixel_value of 51 for a full range video. You can lower this threshold to be more strict on black levels.

MinCoveragePercentage -> (float)

The minimum percentage of pixels in a frame that need to have a luminance below the max_black_pixel_value for a frame to be considered a black frame. Luminance is calculated using the BT.709 matrix.

The default value is 99, which means at least 99% of all pixels in the frame are black pixels as per the `MaxPixelThreshold` set. You can reduce this value to allow more noise on the black frame.

ShotFilter -> (structure)

Filters that are specific to shot detections.

MinSegmentConfidence -> (float)

Specifies the minimum confidence that Amazon Rekognition Video must have in order to return a detected segment. Confidence represents how certain Amazon Rekognition is that a segment is correctly identified. 0 is the lowest confidence. 100 is the highest confidence. Amazon Rekognition Video doesnât return any segments with a confidence level lower than this specified value.

If you donât specify `MinSegmentConfidence` , the `GetSegmentDetection` returns segments with confidence values greater than or equal to 50 percent.

Shorthand Syntax:

```
TechnicalCueFilter={MinSegmentConfidence=float,BlackFrame={MaxPixelThreshold=float,MinCoveragePercentage=float}},ShotFilter={MinSegmentConfidence=float}
```

JSON Syntax:

```
{
  "TechnicalCueFilter": {
    "MinSegmentConfidence": float,
    "BlackFrame": {
      "MaxPixelThreshold": float,
      "MinCoveragePercentage": float
    }
  },
  "ShotFilter": {
    "MinSegmentConfidence": float
  }
}
```

`--segment-types` (list)

An array of segment types to detect in the video. Valid values are TECHNICAL_CUE and SHOT.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  TECHNICAL_CUE
  SHOT
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

JobId -> (string)

Unique identifier for the segment detection job. The `JobId` is returned from `StartSegmentDetection` .