# get-label-detectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-label-detection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-label-detection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# get-label-detection

## Description

Gets the label detection results of a Amazon Rekognition Video analysis started by  StartLabelDetection .

The label detection operation is started by a call to  StartLabelDetection which returns a job identifier (`JobId` ). When the label detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartlabelDetection` .

To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED` . If so, call  GetLabelDetection and pass the job identifier (`JobId` ) from the initial call to `StartLabelDetection` .

`GetLabelDetection` returns an array of detected labels (`Labels` ) sorted by the time the labels were detected. You can also sort by the label name by specifying `NAME` for the `SortBy` input parameter. If there is no `NAME` specified, the default sort is by timestamp.

You can select how results are aggregated by using the `AggregateBy` input parameter. The default aggregation method is `TIMESTAMPS` . You can also aggregate by `SEGMENTS` , which aggregates all instances of labels detected in a given segment.

The returned Labels array may include the following attributes:

- Name - The name of the detected label.
- Confidence - The level of confidence in the label assigned to a detected object.
- Parents - The ancestor labels for a detected label. GetLabelDetection returns a hierarchical taxonomy of detected labels. For example, a detected car might be assigned the label car. The label car has two parent labels: Vehicle (its parent) and Transportation (its grandparent). The response includes the all ancestors for a label, where every ancestor is a unique label. In the previous example, Car, Vehicle, and Transportation are returned as unique labels in the response.
- Aliases - Possible Aliases for the label.
- Categories - The label categories that the detected label belongs to.
- BoundingBox â Bounding boxes are described for all instances of detected common object labels, returned in an array of Instance objects. An Instance object contains a BoundingBox object, describing the location of the label on the input image. It also includes the confidence for the accuracy of the detected bounding box.
- Timestamp - Time, in milliseconds from the start of the video, that the label was detected. For aggregation by `SEGMENTS` , the `StartTimestampMillis` , `EndTimestampMillis` , and `DurationMillis` structures are what define a segment. Although the âTimestampâ structure is still returned with each label, its value is set to be the same as `StartTimestampMillis` .

Timestamp and Bounding box information are returned for detected Instances, only if aggregation is done by `TIMESTAMPS` . If aggregating by `SEGMENTS` , information about detected instances isnât returned.

The version of the label model used for the detection is also returned.

**Note ``DominantColors`` isnât returned for ``Instances`` , although it is shown as part of the response in the sample seen below.**

Use `MaxResults` parameter to limit the number of labels returned. If there are more results than specified in `MaxResults` , the value of `NextToken` in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call `GetlabelDetection` and populate the `NextToken` request parameter with the token value returned from the previous call to `GetLabelDetection` .

If you are retrieving results while using the Amazon Simple Notification Service, note that you will receive an âERRORâ notification if the job encounters an issue.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetLabelDetection)

## Synopsis

```
get-label-detection
--job-id <value>
[--max-results <value>]
[--next-token <value>]
[--sort-by <value>]
[--aggregate-by <value>]
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

Job identifier for the label detection operation for which you want results returned. You get the job identifer from an initial call to `StartlabelDetection` .

`--max-results` (integer)

Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.

`--next-token` (string)

If the previous response was incomplete (because there are more labels to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of labels.

`--sort-by` (string)

Sort to use for elements in the `Labels` array. Use `TIMESTAMP` to sort array elements by the time labels are detected. Use `NAME` to alphabetically group elements for a label together. Within each label group, the array element are sorted by detection confidence. The default sort is by `TIMESTAMP` .

Possible values:

- `NAME`
- `TIMESTAMP`

`--aggregate-by` (string)

Defines how to aggregate the returned results. Results can be aggregated by timestamps or segments.

Possible values:

- `TIMESTAMPS`
- `SEGMENTS`

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

**To get the results of an objects and scenes detection operation**

The following `get-label-detection` command displays the results of an objects and scenes detection operation that you started previously by calling `start-label-detection`.

```
aws rekognition get-label-detection  \
    --job-id 1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
```

Output:

```
{
    "Labels": [
        {
            "Timestamp": 0,
            "Label": {
                "Instances": [],
                "Confidence": 50.19071578979492,
                "Parents": [
                    {
                        "Name": "Person"
                    },
                    {
                        "Name": "Crowd"
                    }
                ],
                "Name": "Audience"
            }
        },
        {
            "Timestamp": 0,
            "Label": {
                "Instances": [],
                "Confidence": 55.74115753173828,
                "Parents": [
                    {
                        "Name": "Room"
                    },
                    {
                        "Name": "Indoors"
                    },
                    {
                        "Name": "School"
                    }
                ],
                "Name": "Classroom"
            }
        }
    ],
    "JobStatus": "SUCCEEDED",
    "LabelModelVersion": "2.0",
    "VideoMetadata": {
        "Format": "QuickTime / MOV",
        "FrameRate": 29.970617294311523,
        "Codec": "h264",
        "DurationMillis": 6806,
        "FrameHeight": 1080,
        "FrameWidth": 1920
    },
    "NextToken": "BMugzAi4L72IERzQdbpyMQuEFBsjlo5W0Yx3mfG+sR9mm98E1/CpObenspRfs/5FBQFs4X7G"
}
```

For more information, see [Detecting Labels in a Video](https://docs.aws.amazon.com/rekognition/latest/dg/labels-detecting-labels-video.html) in the *Amazon Rekognition Developer Guide*.

## Output

JobStatus -> (string)

The current status of the label detection job.

StatusMessage -> (string)

If the job fails, `StatusMessage` provides a descriptive error message.

VideoMetadata -> (structure)

Information about a video that Amazon Rekognition Video analyzed. `Videometadata` is returned in every page of paginated responses from a Amazon Rekognition video operation.

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

NextToken -> (string)

If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of labels.

Labels -> (list)

An array of labels detected in the video. Each element contains the detected label and the time, in milliseconds from the start of the video, that the label was detected.

(structure)

Information about a label detected in a video analysis request and the time the label was detected in the video.

Timestamp -> (long)

Time, in milliseconds from the start of the video, that the label was detected. Note that `Timestamp` is not guaranteed to be accurate to the individual frame where the label first appears.

Label -> (structure)

Details about the detected label.

Name -> (string)

The name (label) of the object or scene.

Confidence -> (float)

Level of confidence.

Instances -> (list)

If `Label` represents an object, `Instances` contains the bounding boxes for each instance of the detected object. Bounding boxes are returned for common object labels such as people, cars, furniture, apparel or pets.

(structure)

An instance of a label returned by Amazon Rekognition Image ( DetectLabels ) or by Amazon Rekognition Video ( GetLabelDetection ).

BoundingBox -> (structure)

The position of the label instance on the image.

Width -> (float)

Width of the bounding box as a ratio of the overall image width.

Height -> (float)

Height of the bounding box as a ratio of the overall image height.

Left -> (float)

Left coordinate of the bounding box as a ratio of overall image width.

Top -> (float)

Top coordinate of the bounding box as a ratio of overall image height.

Confidence -> (float)

The confidence that Amazon Rekognition has in the accuracy of the bounding box.

DominantColors -> (list)

The dominant colors found in an individual instance of a label.

(structure)

A description of the dominant colors in an image.

Red -> (integer)

The Red RGB value for a dominant color.

Blue -> (integer)

The Blue RGB value for a dominant color.

Green -> (integer)

The Green RGB value for a dominant color.

HexCode -> (string)

The Hex code equivalent of the RGB values for a dominant color.

CSSColor -> (string)

The CSS color name of a dominant color.

SimplifiedColor -> (string)

One of 12 simplified color names applied to a dominant color.

PixelPercent -> (float)

The percentage of image pixels that have a given dominant color.

Parents -> (list)

The parent labels for a label. The response includes all ancestor labels.

(structure)

A parent label for a label. A label can have 0, 1, or more parents.

Name -> (string)

The name of the parent label.

Aliases -> (list)

A list of potential aliases for a given label.

(structure)

A potential alias of for a given label.

Name -> (string)

The name of an alias for a given label.

Categories -> (list)

A list of the categories associated with a given label.

(structure)

The category that applies to a given label.

Name -> (string)

The name of a category that applies to a given label.

StartTimestampMillis -> (long)

The time in milliseconds defining the start of the timeline segment containing a continuously detected label.

EndTimestampMillis -> (long)

The time in milliseconds defining the end of the timeline segment containing a continuously detected label.

DurationMillis -> (long)

The time duration of a segment in milliseconds, I.e. time elapsed from StartTimestampMillis to EndTimestampMillis.

LabelModelVersion -> (string)

Version number of the label detection model that was used to detect labels.

JobId -> (string)

Job identifier for the label detection operation for which you want to obtain results. The job identifer is returned by an initial call to StartLabelDetection.

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

A job identifier specified in the call to StartLabelDetection and returned in the job completion notification sent to your Amazon Simple Notification Service topic.

GetRequestMetadata -> (structure)

Information about the paramters used when getting a response. Includes information on aggregation and sorting methods.

SortBy -> (string)

The sorting method chosen for a GetLabelDetection request.

AggregateBy -> (string)

The aggregation method chosen for a GetLabelDetection request.