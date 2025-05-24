# describe-stream-processorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-stream-processor.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-stream-processor.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# describe-stream-processor

## Description

Provides information about a stream processor created by  CreateStreamProcessor . You can get information about the input and output streams, the input parameters for the face recognition being performed, and the current status of the stream processor.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DescribeStreamProcessor)

## Synopsis

```
describe-stream-processor
--name <value>
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

`--name` (string)

Name of the stream processor for which you want information.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To get information about a stream processor**

The following `describe-stream-processor` command displays details about the specified stream processor.

```
aws rekognition describe-stream-processor \
    --name my-stream-processor
```

Output:

```
{
    "Status": "STOPPED",
    "Name": "my-stream-processor",
    "LastUpdateTimestamp": 1532449292.712,
    "Settings": {
        "FaceSearch": {
            "FaceMatchThreshold": 80.0,
            "CollectionId": "my-collection"
        }
    },
    "RoleArn": "arn:aws:iam::123456789012:role/AmazonRekognitionDetectStream",
    "StreamProcessorArn": "arn:aws:rekognition:us-west-2:123456789012:streamprocessor/my-stream-processpr",
    "Output": {
        "KinesisDataStream": {
            "Arn": "arn:aws:kinesis:us-west-2:123456789012:stream/AmazonRekognitionRekStream"
        }
    },
    "Input": {
        "KinesisVideoStream": {
            "Arn": "arn:aws:kinesisvideo:us-west-2:123456789012:stream/macwebcam/123456789012"
        }
    },
    "CreationTimestamp": 1532449292.712
}
```

For more information, see [Working with Streaming Videos](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video.html) in the *Amazon Rekognition Developer Guide*.

## Output

Name -> (string)

Name of the stream processor.

StreamProcessorArn -> (string)

ARN of the stream processor.

Status -> (string)

Current status of the stream processor.

StatusMessage -> (string)

Detailed status message about the stream processor.

CreationTimestamp -> (timestamp)

Date and time the stream processor was created

LastUpdateTimestamp -> (timestamp)

The time, in Unix format, the stream processor was last updated. For example, when the stream processor moves from a running state to a failed state, or when the user starts or stops the stream processor.

Input -> (structure)

Kinesis video stream that provides the source streaming video.

KinesisVideoStream -> (structure)

The Kinesis video stream input stream for the source streaming video.

Arn -> (string)

ARN of the Kinesis video stream stream that streams the source video.

Output -> (structure)

Kinesis data stream to which Amazon Rekognition Video puts the analysis results.

KinesisDataStream -> (structure)

The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor streams the analysis results.

Arn -> (string)

ARN of the output Amazon Kinesis Data Streams stream.

S3Destination -> (structure)

The Amazon S3 bucket location to which Amazon Rekognition publishes the detailed inference results of a video analysis operation.

Bucket -> (string)

The name of the Amazon S3 bucket you want to associate with the streaming video project. You must be the owner of the Amazon S3 bucket.

KeyPrefix -> (string)

The prefix value of the location within the bucket that you want the information to be published to. For more information, see [Using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) .

RoleArn -> (string)

ARN of the IAM role that allows access to the stream processor.

Settings -> (structure)

Input parameters used in a streaming video analyzed by a stream processor. You can use `FaceSearch` to recognize faces in a streaming video, or you can use `ConnectedHome` to detect labels.

FaceSearch -> (structure)

Face search settings to use on a streaming video.

CollectionId -> (string)

The ID of a collection that contains faces that you want to search for.

FaceMatchThreshold -> (float)

Minimum face match confidence score that must be met to return a result for a recognized face. The default is 80. 0 is the lowest confidence. 100 is the highest confidence. Values between 0 and 100 are accepted, and values lower than 80 are set to 80.

ConnectedHome -> (structure)

Label detection settings to use on a streaming video. Defining the settings is required in the request parameter for  CreateStreamProcessor . Including this setting in the `CreateStreamProcessor` request enables you to use the stream processor for label detection. You can then select what you want the stream processor to detect, such as people or pets. When the stream processor has started, one notification is sent for each object class specified. For example, if packages and pets are selected, one SNS notification is published the first time a package is detected and one SNS notification is published the first time a pet is detected, as well as an end-of-session summary.

Labels -> (list)

Specifies what you want to detect in the video, such as people, packages, or pets. The current valid labels you can include in this list are: âPERSONâ, âPETâ, âPACKAGEâ, and âALLâ.

(string)

MinConfidence -> (float)

The minimum confidence required to label an object in the video.

NotificationChannel -> (structure)

The Amazon Simple Notification Service topic to which Amazon Rekognition publishes the object detection results and completion status of a video analysis operation.

Amazon Rekognition publishes a notification the first time an object of interest or a person is detected in the video stream. For example, if Amazon Rekognition detects a person at second 2, a pet at second 4, and a person again at second 5, Amazon Rekognition sends 2 object class detected notifications, one for a person at second 2 and one for a pet at second 4.

Amazon Rekognition also publishes an an end-of-session notification with a summary when the stream processing session is complete.

SNSTopicArn -> (string)

The Amazon Resource Number (ARN) of the Amazon Amazon Simple Notification Service topic to which Amazon Rekognition posts the completion status.

KmsKeyId -> (string)

The identifier for your AWS Key Management Service key (AWS KMS key). This is an optional parameter for label detection stream processors.

RegionsOfInterest -> (list)

Specifies locations in the frames where Amazon Rekognition checks for objects or people. This is an optional parameter for label detection stream processors.

(structure)

Specifies a location within the frame that Rekognition checks for objects of interest such as text, labels, or faces. It uses a `BoundingBox` or `Polygon` to set a region of the screen.

A word, face, or label is included in the region if it is more than half in that region. If there is more than one region, the word, face, or label is compared with all regions of the screen. Any object of interest that is more than half in a region is kept in the results.

BoundingBox -> (structure)

The box representing a region of interest on screen.

Width -> (float)

Width of the bounding box as a ratio of the overall image width.

Height -> (float)

Height of the bounding box as a ratio of the overall image height.

Left -> (float)

Left coordinate of the bounding box as a ratio of overall image width.

Top -> (float)

Top coordinate of the bounding box as a ratio of overall image height.

Polygon -> (list)

Specifies a shape made up of up to 10 `Point` objects to define a region of interest.

(structure)

The X and Y coordinates of a point on an image or video frame. The X and Y values are ratios of the overall image size or video resolution. For example, if an input image is 700x200 and the values are X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the image.

An array of `Point` objects makes up a `Polygon` . A `Polygon` is returned by  DetectText and by  DetectCustomLabels  `Polygon` represents a fine-grained polygon around a detected item. For more information, see Geometry in the Amazon Rekognition Developer Guide.

X -> (float)

The value of the X coordinate for a point on a `Polygon` .

Y -> (float)

The value of the Y coordinate for a point on a `Polygon` .

DataSharingPreference -> (structure)

Shows whether you are sharing data with Rekognition to improve model performance. You can choose this option at the account level or on a per-stream basis. Note that if you opt out at the account level this setting is ignored on individual streams.

OptIn -> (boolean)

If this option is set to true, you choose to share data with Rekognition to improve model performance.