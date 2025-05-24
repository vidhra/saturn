# get-face-searchÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-face-search.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-face-search.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# get-face-search

## Description

Gets the face search results for Amazon Rekognition Video face search started by  StartFaceSearch . The search returns faces in a collection that match the faces of persons detected in a video. It also includes the time(s) that faces are matched in the video.

Face search in a video is an asynchronous operation. You start face search by calling to  StartFaceSearch which returns a job identifier (`JobId` ). When the search operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartFaceSearch` . To get the search results, first check that the status value published to the Amazon SNS topic is `SUCCEEDED` . If so, call `GetFaceSearch` and pass the job identifier (`JobId` ) from the initial call to `StartFaceSearch` .

For more information, see Searching Faces in a Collection in the Amazon Rekognition Developer Guide.

The search results are retured in an array, `Persons` , of  PersonMatch objects. Each``PersonMatch`` element contains details about the matching faces in the input collection, person information (facial attributes, bounding boxes, and person identifer) for the matched person, and the time the person was matched in the video.

### Note

`GetFaceSearch` only returns the default facial attributes (`BoundingBox` , `Confidence` , `Landmarks` , `Pose` , and `Quality` ). The other facial attributes listed in the `Face` object of the following response syntax are not returned. For more information, see FaceDetail in the Amazon Rekognition Developer Guide.

By default, the `Persons` array is sorted by the time, in milliseconds from the start of the video, persons are matched. You can also sort by persons by specifying `INDEX` for the `SORTBY` input parameter.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetFaceSearch)

## Synopsis

```
get-face-search
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

The job identifer for the search request. You get the job identifier from an initial call to `StartFaceSearch` .

`--max-results` (integer)

Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.

`--next-token` (string)

If the previous response was incomplete (because there is more search results to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of search results.

`--sort-by` (string)

Sort to use for grouping faces in the response. Use `TIMESTAMP` to group faces by the time that they are recognized. Use `INDEX` to sort by recognized faces.

Possible values:

- `INDEX`
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

**To get the results of a face search operation**

The following `get-face-search` command displays the results of a face search operation that you started previously by calling `start-face-search`.

```
aws rekognition get-face-search  \
    --job-id 1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
```

Output:

```
{
    "Persons": [
        {
            "Timestamp": 467,
            "FaceMatches": [],
            "Person": {
                "Index": 0,
                "Face": {
                    "BoundingBox": {
                        "Width": 0.1560753583908081,
                        "Top": 0.13555361330509186,
                        "Left": -0.0952017530798912,
                        "Height": 0.6934483051300049
                    },
                    "Landmarks": [
                        {
                            "Y": 0.4013825058937073,
                            "X": -0.041750285774469376,
                            "Type": "eyeLeft"
                        },
                        {
                            "Y": 0.41695496439933777,
                            "X": 0.027979329228401184,
                            "Type": "eyeRight"
                        },
                        {
                            "Y": 0.6375303268432617,
                            "X": -0.04034662991762161,
                            "Type": "mouthLeft"
                        },
                        {
                            "Y": 0.6497718691825867,
                            "X": 0.013960429467260838,
                            "Type": "mouthRight"
                        },
                        {
                            "Y": 0.5238034129142761,
                            "X": 0.008022055961191654,
                            "Type": "nose"
                        }
                    ],
                    "Pose": {
                        "Yaw": -58.07863998413086,
                        "Roll": 1.9384294748306274,
                        "Pitch": -24.66305160522461
                    },
                    "Quality": {
                        "Sharpness": 83.14741516113281,
                        "Brightness": 25.75942611694336
                    },
                    "Confidence": 87.7622299194336
                }
            }
        },
        {
            "Timestamp": 967,
            "FaceMatches": [
                {
                    "Face": {
                        "BoundingBox": {
                            "Width": 0.12368900328874588,
                            "Top": 0.16007399559020996,
                            "Left": 0.5901259779930115,
                            "Height": 0.2514039874076843
                        },
                        "FaceId": "056a95fa-2060-4159-9cab-7ed4daa030fa",
                        "ExternalImageId": "image3.jpg",
                        "Confidence": 100.0,
                        "ImageId": "08f8a078-8929-37fd-8e8f-aadf690e8232"
                    },
                    "Similarity": 98.44476318359375
                }
            ],
            "Person": {
                "Index": 1,
                "Face": {
                    "BoundingBox": {
                        "Width": 0.28559377789497375,
                        "Top": 0.19436298310756683,
                        "Left": 0.024553587660193443,
                        "Height": 0.7216082215309143
                    },
                    "Landmarks": [
                        {
                            "Y": 0.4650231599807739,
                            "X": 0.16269078850746155,
                            "Type": "eyeLeft"
                        },
                        {
                            "Y": 0.4843238294124603,
                            "X": 0.2782580852508545,
                            "Type": "eyeRight"
                        },
                        {
                            "Y": 0.71530681848526,
                            "X": 0.1741468608379364,
                            "Type": "mouthLeft"
                        },
                        {
                            "Y": 0.7310671210289001,
                            "X": 0.26857468485832214,
                            "Type": "mouthRight"
                        },
                        {
                            "Y": 0.582602322101593,
                            "X": 0.2566150426864624,
                            "Type": "nose"
                        }
                    ],
                    "Pose": {
                        "Yaw": 11.487052917480469,
                        "Roll": 5.074230670928955,
                        "Pitch": 15.396159172058105
                    },
                    "Quality": {
                        "Sharpness": 73.32209777832031,
                        "Brightness": 54.96497344970703
                    },
                    "Confidence": 99.99998474121094
                }
            }
        }
    ],
    "NextToken": "5bkgcezyuaqhtWk3C8OTW6cjRghrwV9XDMivm5B3MXm+Lv6G+L+GejyFHPhoNa/ldXIC4c/d",
    "JobStatus": "SUCCEEDED",
    "VideoMetadata": {
        "Format": "QuickTime / MOV",
        "FrameRate": 29.970617294311523,
        "Codec": "h264",
        "DurationMillis": 6806,
        "FrameHeight": 1080,
        "FrameWidth": 1920
    }
}
```

For more information, see [Searching Stored Videos for Faces](https://docs.aws.amazon.com/rekognition/latest/dg/procedure-person-search-videos.html) in the *Amazon Rekognition Developer Guide*.

## Output

JobStatus -> (string)

The current status of the face search job.

StatusMessage -> (string)

If the job fails, `StatusMessage` provides a descriptive error message.

NextToken -> (string)

If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of search results.

VideoMetadata -> (structure)

Information about a video that Amazon Rekognition analyzed. `Videometadata` is returned in every page of paginated responses from a Amazon Rekognition Video operation.

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

Persons -> (list)

An array of persons,  PersonMatch , in the video whose face(s) match the face(s) in an Amazon Rekognition collection. It also includes time information for when persons are matched in the video. You specify the input collection in an initial call to `StartFaceSearch` . Each `Persons` element includes a time the person was matched, face match details (`FaceMatches` ) for matching faces in the collection, and person information (`Person` ) for the matched person.

(structure)

Information about a person whose face matches a face(s) in an Amazon Rekognition collection. Includes information about the faces in the Amazon Rekognition collection ( FaceMatch ), information about the person ( PersonDetail ), and the time stamp for when the person was detected in a video. An array of `PersonMatch` objects is returned by  GetFaceSearch .

Timestamp -> (long)

The time, in milliseconds from the beginning of the video, that the person was matched in the video.

Person -> (structure)

Information about the matched person.

Index -> (long)

Identifier for the person detected person within a video. Use to keep track of the person throughout the video. The identifier is not stored by Amazon Rekognition.

BoundingBox -> (structure)

Bounding box around the detected person.

Width -> (float)

Width of the bounding box as a ratio of the overall image width.

Height -> (float)

Height of the bounding box as a ratio of the overall image height.

Left -> (float)

Left coordinate of the bounding box as a ratio of overall image width.

Top -> (float)

Top coordinate of the bounding box as a ratio of overall image height.

Face -> (structure)

Face details for the detected person.

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

FaceMatches -> (list)

Information about the faces in the input collection that match the face of a person in the video.

(structure)

Provides face metadata. In addition, it also provides the confidence in the match of this face with the input face.

Similarity -> (float)

Confidence in the match of this face with the input face.

Face -> (structure)

Describes the face properties such as the bounding box, face ID, image ID of the source image, and external image ID that you assigned.

FaceId -> (string)

Unique identifier that Amazon Rekognition assigns to the face.

BoundingBox -> (structure)

Bounding box of the face.

Width -> (float)

Width of the bounding box as a ratio of the overall image width.

Height -> (float)

Height of the bounding box as a ratio of the overall image height.

Left -> (float)

Left coordinate of the bounding box as a ratio of overall image width.

Top -> (float)

Top coordinate of the bounding box as a ratio of overall image height.

ImageId -> (string)

Unique identifier that Amazon Rekognition assigns to the input image.

ExternalImageId -> (string)

Identifier that you assign to all the faces in the input image.

Confidence -> (float)

Confidence level that the bounding box contains a face (and not a different object such as a tree).

IndexFacesModelVersion -> (string)

The version of the face detect and storage model that was used when indexing the face vector.

UserId -> (string)

Unique identifier assigned to the user.

JobId -> (string)

Job identifier for the face search operation for which you want to obtain results. The job identifer is returned by an initial call to StartFaceSearch.

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

A job identifier specified in the call to StartFaceSearch and returned in the job completion notification sent to your Amazon Simple Notification Service topic.