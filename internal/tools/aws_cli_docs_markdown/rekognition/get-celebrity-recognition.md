# get-celebrity-recognitionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-celebrity-recognition.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-celebrity-recognition.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# get-celebrity-recognition

## Description

Gets the celebrity recognition results for a Amazon Rekognition Video analysis started by  StartCelebrityRecognition .

Celebrity recognition in a video is an asynchronous operation. Analysis is started by a call to  StartCelebrityRecognition which returns a job identifier (`JobId` ).

When the celebrity recognition operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartCelebrityRecognition` . To get the results of the celebrity recognition analysis, first check that the status value published to the Amazon SNS topic is `SUCCEEDED` . If so, call `GetCelebrityDetection` and pass the job identifier (`JobId` ) from the initial call to `StartCelebrityDetection` .

For more information, see Working With Stored Videos in the Amazon Rekognition Developer Guide.

`GetCelebrityRecognition` returns detected celebrities and the time(s) they are detected in an array (`Celebrities` ) of  CelebrityRecognition objects. Each `CelebrityRecognition` contains information about the celebrity in a  CelebrityDetail object and the time, `Timestamp` , the celebrity was detected. This  CelebrityDetail object stores information about the detected celebrityâs face attributes, a face bounding box, known gender, the celebrityâs name, and a confidence estimate.

### Note

`GetCelebrityRecognition` only returns the default facial attributes (`BoundingBox` , `Confidence` , `Landmarks` , `Pose` , and `Quality` ). The `BoundingBox` field only applies to the detected face instance. The other facial attributes listed in the `Face` object of the following response syntax are not returned. For more information, see FaceDetail in the Amazon Rekognition Developer Guide.

By default, the `Celebrities` array is sorted by time (milliseconds from the start of the video). You can also sort the array by celebrity by specifying the value `ID` in the `SortBy` input parameter.

The `CelebrityDetail` object includes the celebrity identifer and additional information urls. If you donât store the additional information urls, you can get them later by calling  GetCelebrityInfo with the celebrity identifer.

No information is returned for faces not recognized as celebrities.

Use MaxResults parameter to limit the number of labels returned. If there are more results than specified in `MaxResults` , the value of `NextToken` in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call `GetCelebrityDetection` and populate the `NextToken` request parameter with the token value returned from the previous call to `GetCelebrityRecognition` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetCelebrityRecognition)

## Synopsis

```
get-celebrity-recognition
--job-id <value>
[--max-results <value>]
[--next-token <value>]
[--sort-by <value>]
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

Job identifier for the required celebrity recognition analysis. You can get the job identifer from a call to `StartCelebrityRecognition` .

`--max-results` (integer)

Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.

`--next-token` (string)

If the previous response was incomplete (because there is more recognized celebrities to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of celebrities.

`--sort-by` (string)

Sort to use for celebrities returned in `Celebrities` field. Specify `ID` to sort by the celebrity identifier, specify `TIMESTAMP` to sort by the time the celebrity was recognized.

Possible values:

- `ID`
- `TIMESTAMP`

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

**To get the results of a celebrity recognition operation**

The following `get-celebrity-recognition` command diplays the results of a celebrity recognition operation that you started previously by calling `start-celebrity-recognition`.

```
aws rekognition get-celebrity-recognition  \
    --job-id 1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
```

Output:

```
{
    "NextToken": "3D01ClxlCiT31VsRDkAO3IybLb/h5AtDWSGuhYi+N1FIJwwPtAkuKzDhL2rV3GcwmNt77+12",
    "Celebrities": [
        {
            "Timestamp": 0,
            "Celebrity": {
                "Confidence": 96.0,
                "Face": {
                    "BoundingBox": {
                        "Width": 0.70333331823349,
                        "Top": 0.16750000417232513,
                        "Left": 0.19555555284023285,
                        "Height": 0.3956249952316284
                    },
                    "Landmarks": [
                        {
                            "Y": 0.31031012535095215,
                            "X": 0.441436767578125,
                            "Type": "eyeLeft"
                        },
                        {
                            "Y": 0.3081788718700409,
                            "X": 0.6437258720397949,
                            "Type": "eyeRight"
                        },
                        {
                            "Y": 0.39542075991630554,
                            "X": 0.5572493076324463,
                            "Type": "nose"
                        },
                        {
                            "Y": 0.4597957134246826,
                            "X": 0.4579732120037079,
                            "Type": "mouthLeft"
                        },
                        {
                            "Y": 0.45688048005104065,
                            "X": 0.6349081993103027,
                            "Type": "mouthRight"
                        }
                    ],
                    "Pose": {
                        "Yaw": 8.943398475646973,
                        "Roll": -2.0309247970581055,
                        "Pitch": -0.5674862861633301
                    },
                    "Quality": {
                        "Sharpness": 99.40211486816406,
                        "Brightness": 89.47132110595703
                    },
                    "Confidence": 99.99861145019531
                },
                "Name": "CelebrityA",
                "Urls": [
                    "www.imdb.com/name/111111111"
                ],
                "Id": "nnnnnn"
            }
        },
        {
            "Timestamp": 467,
            "Celebrity": {
                "Confidence": 99.0,
                "Face": {
                    "BoundingBox": {
                        "Width": 0.6877777576446533,
                        "Top": 0.18437500298023224,
                        "Left": 0.20555555820465088,
                        "Height": 0.3868750035762787
                    },
                    "Landmarks": [
                        {
                            "Y": 0.31895750761032104,
                            "X": 0.4411413371562958,
                            "Type": "eyeLeft"
                        },
                        {
                            "Y": 0.3140959143638611,
                            "X": 0.6523157954216003,
                            "Type": "eyeRight"
                        },
                        {
                            "Y": 0.4016456604003906,
                            "X": 0.5682755708694458,
                            "Type": "nose"
                        },
                        {
                            "Y": 0.46894142031669617,
                            "X": 0.4597797095775604,
                            "Type": "mouthLeft"
                        },
                        {
                            "Y": 0.46971091628074646,
                            "X": 0.6286435127258301,
                            "Type": "mouthRight"
                        }
                    ],
                    "Pose": {
                        "Yaw": 10.433465957641602,
                        "Roll": -3.347442388534546,
                        "Pitch": 1.3709543943405151
                    },
                    "Quality": {
                        "Sharpness": 99.5531005859375,
                        "Brightness": 88.5764389038086
                    },
                    "Confidence": 99.99148559570312
                },
                "Name": "Jane Celebrity",
                "Urls": [
                    "www.imdb.com/name/111111111"
                ],
                "Id": "nnnnnn"
            }
        }
    ],
    "JobStatus": "SUCCEEDED",
    "VideoMetadata": {
        "Format": "QuickTime / MOV",
        "FrameRate": 29.978118896484375,
        "Codec": "h264",
        "DurationMillis": 4570,
        "FrameHeight": 1920,
        "FrameWidth": 1080
    }
}
```

For more information, see [Recognizing Celebrities in a Stored Video](https://docs.aws.amazon.com/rekognition/latest/dg/celebrities-video-sqs.html) in the *Amazon Rekognition Developer Guide*.

## Output

JobStatus -> (string)

The current status of the celebrity recognition job.

StatusMessage -> (string)

If the job fails, `StatusMessage` provides a descriptive error message.

VideoMetadata -> (structure)

Information about a video that Amazon Rekognition Video analyzed. `Videometadata` is returned in every page of paginated responses from a Amazon Rekognition Video operation.

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

If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of celebrities.

Celebrities -> (list)

Array of celebrities recognized in the video.

(structure)

Information about a detected celebrity and the time the celebrity was detected in a stored video. For more information, see GetCelebrityRecognition in the Amazon Rekognition Developer Guide.

Timestamp -> (long)

The time, in milliseconds from the start of the video, that the celebrity was recognized. Note that `Timestamp` is not guaranteed to be accurate to the individual frame where the celebrity first appears.

Celebrity -> (structure)

Information about a recognized celebrity.

Urls -> (list)

An array of URLs pointing to additional celebrity information.

(string)

Name -> (string)

The name of the celebrity.

Id -> (string)

The unique identifier for the celebrity.

Confidence -> (float)

The confidence, in percentage, that Amazon Rekognition has that the recognized face is the celebrity.

BoundingBox -> (structure)

Bounding box around the body of a celebrity.

Width -> (float)

Width of the bounding box as a ratio of the overall image width.

Height -> (float)

Height of the bounding box as a ratio of the overall image height.

Left -> (float)

Left coordinate of the bounding box as a ratio of overall image width.

Top -> (float)

Top coordinate of the bounding box as a ratio of overall image height.

Face -> (structure)

Face details for the recognized celebrity.

BoundingBox -> (structure)

Bounding box of the face. Default attribute.

Width -> (float)

Width of the bounding box as a ratio of the overall image width.

Height -> (float)

Height of the bounding box as a ratio of the overall image height.

Left -> (float)

Left coordinate of the bounding box as a ratio of overall image width.

Top -> (float)

Top coordinate of the bounding box as a ratio of overall image height.

AgeRange -> (structure)

The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.

Low -> (integer)

The lowest estimated age.

High -> (integer)

The highest estimated age.

Smile -> (structure)

Indicates whether or not the face is smiling, and the confidence level in the determination.

Value -> (boolean)

Boolean value that indicates whether the face is smiling or not.

Confidence -> (float)

Level of confidence in the determination.

Eyeglasses -> (structure)

Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.

Value -> (boolean)

Boolean value that indicates whether the face is wearing eye glasses or not.

Confidence -> (float)

Level of confidence in the determination.

Sunglasses -> (structure)

Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.

Value -> (boolean)

Boolean value that indicates whether the face is wearing sunglasses or not.

Confidence -> (float)

Level of confidence in the determination.

Gender -> (structure)

The predicted gender of a detected face.

Value -> (string)

The predicted gender of the face.

Confidence -> (float)

Level of confidence in the prediction.

Beard -> (structure)

Indicates whether or not the face has a beard, and the confidence level in the determination.

Value -> (boolean)

Boolean value that indicates whether the face has beard or not.

Confidence -> (float)

Level of confidence in the determination.

Mustache -> (structure)

Indicates whether or not the face has a mustache, and the confidence level in the determination.

Value -> (boolean)

Boolean value that indicates whether the face has mustache or not.

Confidence -> (float)

Level of confidence in the determination.

EyesOpen -> (structure)

Indicates whether or not the eyes on the face are open, and the confidence level in the determination.

Value -> (boolean)

Boolean value that indicates whether the eyes on the face are open.

Confidence -> (float)

Level of confidence in the determination.

MouthOpen -> (structure)

Indicates whether or not the mouth on the face is open, and the confidence level in the determination.

Value -> (boolean)

Boolean value that indicates whether the mouth on the face is open or not.

Confidence -> (float)

Level of confidence in the determination.

Emotions -> (list)

The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a personâs face. It is not a determination of the personâs internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

(structure)

The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a personâs face. It is not a determination of the personâs internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

Type -> (string)

Type of emotion detected.

Confidence -> (float)

Level of confidence in the determination.

Landmarks -> (list)

Indicates the location of landmarks on the face. Default attribute.

(structure)

Indicates the location of the landmark on the face.

Type -> (string)

Type of landmark.

X -> (float)

The x-coordinate of the landmark expressed as a ratio of the width of the image. The x-coordinate is measured from the left-side of the image. For example, if the image is 700 pixels wide and the x-coordinate of the landmark is at 350 pixels, this value is 0.5.

Y -> (float)

The y-coordinate of the landmark expressed as a ratio of the height of the image. The y-coordinate is measured from the top of the image. For example, if the image height is 200 pixels and the y-coordinate of the landmark is at 50 pixels, this value is 0.25.

Pose -> (structure)

Indicates the pose of the face as determined by its pitch, roll, and yaw. Default attribute.

Roll -> (float)

Value representing the face rotation on the roll axis.

Yaw -> (float)

Value representing the face rotation on the yaw axis.

Pitch -> (float)

Value representing the face rotation on the pitch axis.

Quality -> (structure)

Identifies image brightness and sharpness. Default attribute.

Brightness -> (float)

Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

Sharpness -> (float)

Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.

Confidence -> (float)

Confidence level that the bounding box contains a face (and not a different object such as a tree). Default attribute.

FaceOccluded -> (structure)

`FaceOccluded` should return âtrueâ with a high confidence score if a detected faceâs eyes, nose, and mouth are partially captured or if they are covered by masks, dark sunglasses, cell phones, hands, or other objects. `FaceOccluded` should return âfalseâ with a high confidence score if common occurrences that do not impact face verification are detected, such as eye glasses, lightly tinted sunglasses, strands of hair, and others.

Value -> (boolean)

True if a detected faceâs eyes, nose, and mouth are partially captured or if they are covered by masks, dark sunglasses, cell phones, hands, or other objects. False if common occurrences that do not impact face verification are detected, such as eye glasses, lightly tinted sunglasses, strands of hair, and others.

Confidence -> (float)

The confidence that the service has detected the presence of a face occlusion.

EyeDirection -> (structure)

Indicates the direction the eyes are gazing in, as defined by pitch and yaw.

Yaw -> (float)

Value representing eye direction on the yaw axis.

Pitch -> (float)

Value representing eye direction on the pitch axis.

Confidence -> (float)

The confidence that the service has in its predicted eye direction.

KnownGender -> (structure)

Retrieves the known gender for the celebrity.

Type -> (string)

A string value of the KnownGender info about the Celebrity.

JobId -> (string)

Job identifier for the celebrity recognition operation for which you want to obtain results. The job identifer is returned by an initial call to StartCelebrityRecognition.

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

A job identifier specified in the call to StartCelebrityRecognition and returned in the job completion notification sent to your Amazon Simple Notification Service topic.