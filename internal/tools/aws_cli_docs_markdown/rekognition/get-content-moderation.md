# get-content-moderationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-content-moderation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-content-moderation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# get-content-moderation

## Description

Gets the inappropriate, unwanted, or offensive content analysis results for a Amazon Rekognition Video analysis started by  StartContentModeration . For a list of moderation labels in Amazon Rekognition, see [Using the image and video moderation APIs](https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html#moderation-api) .

Amazon Rekognition Video inappropriate or offensive content detection in a stored video is an asynchronous operation. You start analysis by calling  StartContentModeration which returns a job identifier (`JobId` ). When analysis finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartContentModeration` . To get the results of the content analysis, first check that the status value published to the Amazon SNS topic is `SUCCEEDED` . If so, call `GetContentModeration` and pass the job identifier (`JobId` ) from the initial call to `StartContentModeration` .

For more information, see Working with Stored Videos in the Amazon Rekognition Devlopers Guide.

`GetContentModeration` returns detected inappropriate, unwanted, or offensive content moderation labels, and the time they are detected, in an array, `ModerationLabels` , of  ContentModerationDetection objects.

By default, the moderated labels are returned sorted by time, in milliseconds from the start of the video. You can also sort them by moderated label by specifying `NAME` for the `SortBy` input parameter.

Since video analysis can return a large number of results, use the `MaxResults` parameter to limit the number of labels returned in a single call to `GetContentModeration` . If there are more results than specified in `MaxResults` , the value of `NextToken` in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call `GetContentModeration` and populate the `NextToken` request parameter with the value of `NextToken` returned from the previous call to `GetContentModeration` .

For more information, see moderating content in the Amazon Rekognition Developer Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetContentModeration)

## Synopsis

```
get-content-moderation
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

The identifier for the inappropriate, unwanted, or offensive content moderation job. Use `JobId` to identify the job in a subsequent call to `GetContentModeration` .

`--max-results` (integer)

Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.

`--next-token` (string)

If the previous response was incomplete (because there is more data to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of content moderation labels.

`--sort-by` (string)

Sort to use for elements in the `ModerationLabelDetections` array. Use `TIMESTAMP` to sort array elements by the time labels are detected. Use `NAME` to alphabetically group elements for a label together. Within each label group, the array element are sorted by detection confidence. The default sort is by `TIMESTAMP` .

Possible values:

- `NAME`
- `TIMESTAMP`

`--aggregate-by` (string)

Defines how to aggregate results of the StartContentModeration request. Default aggregation option is TIMESTAMPS. SEGMENTS mode aggregates moderation labels over time.

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

**To get the results of an unsafe content operation**

The following `get-content-moderation` command displays the results of an unsafe content operation that you started previously by calling `start-content-moderation`.

```
aws rekognition get-content-moderation \
    --job-id 1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
```

Output:

```
{
    "NextToken": "dlhcKMHMzpCBGFukz6IO3JMcWiJAamCVhXHt3r6b4b5Tfbyw3q7o+Jeezt+ZpgfOnW9FCCgQ",
    "ModerationLabels": [
        {
            "Timestamp": 0,
            "ModerationLabel": {
                "Confidence": 97.39583587646484,
                "ParentName": "",
                "Name": "Violence"
            }
        },
        {
            "Timestamp": 0,
            "ModerationLabel": {
                "Confidence": 97.39583587646484,
                "ParentName": "Violence",
                "Name": "Weapon Violence"
            }
        }
    ],
    "JobStatus": "SUCCEEDED",
    "VideoMetadata": {
        "Format": "QuickTime / MOV",
        "FrameRate": 29.97515869140625,
        "Codec": "h264",
        "DurationMillis": 6039,
        "FrameHeight": 1920,
        "FrameWidth": 1080
    }
}
```

For more information, see [Detecting Unsafe Stored Videos](https://docs.aws.amazon.com/rekognition/latest/dg/procedure-moderate-videos.html) in the *Amazon Rekognition Developer Guide*.

## Output

JobStatus -> (string)

The current status of the content moderation analysis job.

StatusMessage -> (string)

If the job fails, `StatusMessage` provides a descriptive error message.

VideoMetadata -> (structure)

Information about a video that Amazon Rekognition analyzed. `Videometadata` is returned in every page of paginated responses from `GetContentModeration` .

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

ModerationLabels -> (list)

The detected inappropriate, unwanted, or offensive content moderation labels and the time(s) they were detected.

(structure)

Information about an inappropriate, unwanted, or offensive content label detection in a stored video.

Timestamp -> (long)

Time, in milliseconds from the beginning of the video, that the content moderation label was detected. Note that `Timestamp` is not guaranteed to be accurate to the individual frame where the moderated content first appears.

ModerationLabel -> (structure)

The content moderation label detected by in the stored video.

Confidence -> (float)

Specifies the confidence that Amazon Rekognition has that the label has been correctly identified.

If you donât specify the `MinConfidence` parameter in the call to `DetectModerationLabels` , the operation returns labels with a confidence value greater than or equal to 50 percent.

Name -> (string)

The label name for the type of unsafe content detected in the image.

ParentName -> (string)

The name for the parent label. Labels at the top level of the hierarchy have the parent label `""` .

TaxonomyLevel -> (integer)

The level of the moderation label with regard to its taxonomy, from 1 to 3.

StartTimestampMillis -> (long)

The time in milliseconds defining the start of the timeline segment containing a continuously detected moderation label.

EndTimestampMillis -> (long)

The time in milliseconds defining the end of the timeline segment containing a continuously detected moderation label.

DurationMillis -> (long)

The time duration of a segment in milliseconds, I.e. time elapsed from StartTimestampMillis to EndTimestampMillis.

ContentTypes -> (list)

A list of predicted results for the type of content an image contains. For example, the image content might be from animation, sports, or a video game.

(structure)

Contains information regarding the confidence and name of a detected content type.

Confidence -> (float)

The confidence level of the label given

Name -> (string)

The name of the label

NextToken -> (string)

If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of content moderation labels.

ModerationModelVersion -> (string)

Version number of the moderation detection model that was used to detect inappropriate, unwanted, or offensive content.

JobId -> (string)

Job identifier for the content moderation operation for which you want to obtain results. The job identifer is returned by an initial call to StartContentModeration.

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

A job identifier specified in the call to StartContentModeration and returned in the job completion notification sent to your Amazon Simple Notification Service topic.

GetRequestMetadata -> (structure)

Information about the paramters used when getting a response. Includes information on aggregation and sorting methods.

SortBy -> (string)

The sorting method chosen for a GetContentModeration request.

AggregateBy -> (string)

The aggregation method chosen for a GetContentModeration request.