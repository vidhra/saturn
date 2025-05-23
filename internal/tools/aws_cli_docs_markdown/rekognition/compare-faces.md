# compare-facesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/compare-faces.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/compare-faces.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# compare-faces

## Description

Compares a face in the *source* input image with each of the 100 largest faces detected in the *target* input image.

If the source image contains multiple faces, the service detects the largest face and compares it with each face detected in the target image.

### Note

CompareFaces uses machine learning algorithms, which are probabilistic. A false negative is an incorrect prediction that a face in the target image has a low similarity confidence score when compared to the face in the source image. To reduce the probability of false negatives, we recommend that you compare the target image against multiple source images. If you plan to use `CompareFaces` to make a decision that impacts an individualâs rights, privacy, or access to services, we recommend that you pass the result to a human for review and further validation before taking action.

You pass the input and target images either as base64-encoded image bytes or as references to images in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes isnât supported. The image must be formatted as a PNG or JPEG file.

In response, the operation returns an array of face matches ordered by similarity score in descending order. For each face match, the response provides a bounding box of the face, facial landmarks, pose details (pitch, roll, and yaw), quality (brightness and sharpness), and confidence value (indicating the level of confidence that the bounding box contains a face). The response also provides a similarity score, which indicates how closely the faces match.

### Note

By default, only faces with a similarity score of greater than or equal to 80% are returned in the response. You can change this value by specifying the `SimilarityThreshold` parameter.

`CompareFaces` also returns an array of faces that donât match the source image. For each face, it returns a bounding box, confidence value, landmarks, pose details, and quality. The response also returns information about the face in the source image, including the bounding box of the face and confidence value.

The `QualityFilter` input parameter allows you to filter out detected faces that donât meet a required quality bar. The quality bar is based on a variety of common use cases. Use `QualityFilter` to set the quality bar by specifying `LOW` , `MEDIUM` , or `HIGH` . If you do not want to filter detected faces, specify `NONE` . The default value is `NONE` .

If the image doesnât contain Exif metadata, `CompareFaces` returns orientation information for the source and target images. Use these values to display the images with the correct image orientation.

If no faces are detected in the source or target images, `CompareFaces` returns an `InvalidParameterException` error.

### Note

This is a stateless API operation. That is, data returned by this operation doesnât persist.

For an example, see Comparing Faces in Images in the Amazon Rekognition Developer Guide.

This operation requires permissions to perform the `rekognition:CompareFaces` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/CompareFaces)

## Synopsis

```
compare-faces
[--source-image <value>]
[--target-image <value>]
[--similarity-threshold <value>]
[--quality-filter <value>]
[--source-image-bytes <value>]
[--target-image-bytes <value>]
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

`--source-image` (structure)

The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.

If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the `Bytes` field. For more information, see Images in the Amazon Rekognition developer guide.

To specify a local file use `--source-image-bytes` instead.

Bytes -> (blob)

Blob of image bytes up to 5 MBs. Note that the maximum image size you can pass to `DetectCustomLabels` is 4MB.

S3Object -> (structure)

Identifies an S3 object as the image source.

Bucket -> (string)

Name of the S3 bucket.

Name -> (string)

S3 object key name.

Version -> (string)

If the bucket is versioning enabled, you can specify the object version.

Shorthand Syntax:

```
Bytes=blob,S3Object={Bucket=string,Name=string,Version=string}
```

JSON Syntax:

```
{
  "Bytes": blob,
  "S3Object": {
    "Bucket": "string",
    "Name": "string",
    "Version": "string"
  }
}
```

`--target-image` (structure)

The target image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.

If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the `Bytes` field. For more information, see Images in the Amazon Rekognition developer guide.

To specify a local file use `--target-image-bytes` instead.

Bytes -> (blob)

Blob of image bytes up to 5 MBs. Note that the maximum image size you can pass to `DetectCustomLabels` is 4MB.

S3Object -> (structure)

Identifies an S3 object as the image source.

Bucket -> (string)

Name of the S3 bucket.

Name -> (string)

S3 object key name.

Version -> (string)

If the bucket is versioning enabled, you can specify the object version.

Shorthand Syntax:

```
Bytes=blob,S3Object={Bucket=string,Name=string,Version=string}
```

JSON Syntax:

```
{
  "Bytes": blob,
  "S3Object": {
    "Bucket": "string",
    "Name": "string",
    "Version": "string"
  }
}
```

`--similarity-threshold` (float)

The minimum level of confidence in the face matches that a match must meet to be included in the `FaceMatches` array.

`--quality-filter` (string)

A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces arenât compared. If you specify `AUTO` , Amazon Rekognition chooses the quality bar. If you specify `LOW` , `MEDIUM` , or `HIGH` , filtering removes all faces that donât meet the chosen quality bar. The quality bar is based on a variety of common use cases. Low-quality detections can occur for a number of reasons. Some examples are an object thatâs misidentified as a face, a face thatâs too blurry, or a face with a pose thatâs too extreme to use. If you specify `NONE` , no filtering is performed. The default value is `NONE` .

To use quality filtering, the collection you are using must be associated with version 3 of the face model or higher.

Possible values:

- `NONE`
- `AUTO`
- `LOW`
- `MEDIUM`
- `HIGH`

`--source-image-bytes` (blob)

The content of the image to be uploaded. To specify the content of a local file use the fileb:// prefix. Example: fileb://image.png

`--target-image-bytes` (blob)

The content of the image to be uploaded. To specify the content of a local file use the fileb:// prefix. Example: fileb://image.png

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

**To compare faces in two images**

The following `compare-faces` command compares faces in two images stored in an Amazon S3 bucket.

```
aws rekognition compare-faces \
    --source-image '{"S3Object":{"Bucket":"MyImageS3Bucket","Name":"source.jpg"}}' \
    --target-image '{"S3Object":{"Bucket":"MyImageS3Bucket","Name":"target.jpg"}}'
```

Output:

```
{
    "UnmatchedFaces": [],
    "FaceMatches": [
        {
            "Face": {
                "BoundingBox": {
                    "Width": 0.12368916720151901,
                    "Top": 0.16007372736930847,
                    "Left": 0.5901257991790771,
                    "Height": 0.25140416622161865
                },
                "Confidence": 100.0,
                "Pose": {
                    "Yaw": -3.7351467609405518,
                    "Roll": -0.10309021919965744,
                    "Pitch": 0.8637830018997192
                },
                "Quality": {
                    "Sharpness": 95.51618957519531,
                    "Brightness": 65.29893493652344
                },
                "Landmarks": [
                    {
                        "Y": 0.26721030473709106,
                        "X": 0.6204193830490112,
                        "Type": "eyeLeft"
                    },
                    {
                        "Y": 0.26831310987472534,
                        "X": 0.6776827573776245,
                        "Type": "eyeRight"
                    },
                    {
                        "Y": 0.3514654338359833,
                        "X": 0.6241428852081299,
                        "Type": "mouthLeft"
                    },
                    {
                        "Y": 0.35258132219314575,
                        "X": 0.6713621020317078,
                        "Type": "mouthRight"
                    },
                    {
                        "Y": 0.3140771687030792,
                        "X": 0.6428444981575012,
                        "Type": "nose"
                    }
                ]
            },
            "Similarity": 100.0
        }
    ],
    "SourceImageFace": {
        "BoundingBox": {
            "Width": 0.12368916720151901,
            "Top": 0.16007372736930847,
            "Left": 0.5901257991790771,
            "Height": 0.25140416622161865
        },
        "Confidence": 100.0
    }
}
```

For more information, see [Comparing Faces in Images](https://docs.aws.amazon.com/rekognition/latest/dg/faces-comparefaces.html) in the *Amazon Rekognition Developer Guide*.

## Output

SourceImageFace -> (structure)

The face in the source image that was used for comparison.

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

Confidence -> (float)

Confidence level that the selected bounding box contains a face.

FaceMatches -> (list)

An array of faces in the target image that match the source image face. Each `CompareFacesMatch` object provides the bounding box, the confidence level that the bounding box contains a face, and the similarity score for the face in the bounding box and the face in the source image.

(structure)

Provides information about a face in a target image that matches the source image face analyzed by `CompareFaces` . The `Face` property contains the bounding box of the face in the target image. The `Similarity` property is the confidence that the source image face matches the face in the bounding box.

Similarity -> (float)

Level of confidence that the faces match.

Face -> (structure)

Provides face metadata (bounding box and confidence that the bounding box actually contains a face).

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

Confidence -> (float)

Level of confidence that what the bounding box contains is a face.

Landmarks -> (list)

An array of facial landmarks.

(structure)

Indicates the location of the landmark on the face.

Type -> (string)

Type of landmark.

X -> (float)

The x-coordinate of the landmark expressed as a ratio of the width of the image. The x-coordinate is measured from the left-side of the image. For example, if the image is 700 pixels wide and the x-coordinate of the landmark is at 350 pixels, this value is 0.5.

Y -> (float)

The y-coordinate of the landmark expressed as a ratio of the height of the image. The y-coordinate is measured from the top of the image. For example, if the image height is 200 pixels and the y-coordinate of the landmark is at 50 pixels, this value is 0.25.

Pose -> (structure)

Indicates the pose of the face as determined by its pitch, roll, and yaw.

Roll -> (float)

Value representing the face rotation on the roll axis.

Yaw -> (float)

Value representing the face rotation on the yaw axis.

Pitch -> (float)

Value representing the face rotation on the pitch axis.

Quality -> (structure)

Identifies face image brightness and sharpness.

Brightness -> (float)

Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

Sharpness -> (float)

Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.

Emotions -> (list)

The emotions that appear to be expressed on the face, and the confidence level in the determination. Valid values include âHappyâ, âSadâ, âAngryâ, âConfusedâ, âDisgustedâ, âSurprisedâ, âCalmâ, âUnknownâ, and âFearâ.

(structure)

The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a personâs face. It is not a determination of the personâs internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

Type -> (string)

Type of emotion detected.

Confidence -> (float)

Level of confidence in the determination.

Smile -> (structure)

Indicates whether or not the face is smiling, and the confidence level in the determination.

Value -> (boolean)

Boolean value that indicates whether the face is smiling or not.

Confidence -> (float)

Level of confidence in the determination.

UnmatchedFaces -> (list)

An array of faces in the target image that did not match the source image face.

(structure)

Provides face metadata for target image faces that are analyzed by `CompareFaces` and `RecognizeCelebrities` .

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

Confidence -> (float)

Level of confidence that what the bounding box contains is a face.

Landmarks -> (list)

An array of facial landmarks.

(structure)

Indicates the location of the landmark on the face.

Type -> (string)

Type of landmark.

X -> (float)

The x-coordinate of the landmark expressed as a ratio of the width of the image. The x-coordinate is measured from the left-side of the image. For example, if the image is 700 pixels wide and the x-coordinate of the landmark is at 350 pixels, this value is 0.5.

Y -> (float)

The y-coordinate of the landmark expressed as a ratio of the height of the image. The y-coordinate is measured from the top of the image. For example, if the image height is 200 pixels and the y-coordinate of the landmark is at 50 pixels, this value is 0.25.

Pose -> (structure)

Indicates the pose of the face as determined by its pitch, roll, and yaw.

Roll -> (float)

Value representing the face rotation on the roll axis.

Yaw -> (float)

Value representing the face rotation on the yaw axis.

Pitch -> (float)

Value representing the face rotation on the pitch axis.

Quality -> (structure)

Identifies face image brightness and sharpness.

Brightness -> (float)

Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

Sharpness -> (float)

Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.

Emotions -> (list)

The emotions that appear to be expressed on the face, and the confidence level in the determination. Valid values include âHappyâ, âSadâ, âAngryâ, âConfusedâ, âDisgustedâ, âSurprisedâ, âCalmâ, âUnknownâ, and âFearâ.

(structure)

The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a personâs face. It is not a determination of the personâs internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

Type -> (string)

Type of emotion detected.

Confidence -> (float)

Level of confidence in the determination.

Smile -> (structure)

Indicates whether or not the face is smiling, and the confidence level in the determination.

Value -> (boolean)

Boolean value that indicates whether the face is smiling or not.

Confidence -> (float)

Level of confidence in the determination.

SourceImageOrientationCorrection -> (string)

The value of `SourceImageOrientationCorrection` is always null.

If the input image is in .jpeg format, it might contain exchangeable image file format (Exif) metadata that includes the imageâs orientation. Amazon Rekognition uses this orientation information to perform image correction. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation. Images in .png format donât contain Exif metadata.

Amazon Rekognition doesnât perform image correction for images in .png format and .jpeg images without orientation information in the image Exif metadata. The bounding box coordinates arenât translated and represent the object locations before the image is rotated.

TargetImageOrientationCorrection -> (string)

The value of `TargetImageOrientationCorrection` is always null.

If the input image is in .jpeg format, it might contain exchangeable image file format (Exif) metadata that includes the imageâs orientation. Amazon Rekognition uses this orientation information to perform image correction. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation. Images in .png format donât contain Exif metadata.

Amazon Rekognition doesnât perform image correction for images in .png format and .jpeg images without orientation information in the image Exif metadata. The bounding box coordinates arenât translated and represent the object locations before the image is rotated.