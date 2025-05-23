# index-facesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index-faces.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index-faces.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# index-faces

## Description

Detects faces in the input image and adds them to the specified collection.

Amazon Rekognition doesnât save the actual faces that are detected. Instead, the underlying detection algorithm first detects the faces in the input image. For each face, the algorithm extracts facial features into a feature vector, and stores it in the backend database. Amazon Rekognition uses feature vectors when it performs face match and search operations using the  SearchFaces and  SearchFacesByImage operations.

For more information, see Adding faces to a collection in the Amazon Rekognition Developer Guide.

To get the number of faces in a collection, call  DescribeCollection .

If youâre using version 1.0 of the face detection model, `IndexFaces` indexes the 15 largest faces in the input image. Later versions of the face detection model index the 100 largest faces in the input image.

If youâre using version 4 or later of the face model, image orientation information is not returned in the `OrientationCorrection` field.

To determine which version of the model youâre using, call  DescribeCollection and supply the collection ID. You can also get the model version from the value of `FaceModelVersion` in the response from `IndexFaces`

For more information, see Model Versioning in the Amazon Rekognition Developer Guide.

If you provide the optional `ExternalImageId` for the input image you provided, Amazon Rekognition associates this ID with all faces that it detects. When you call the  ListFaces operation, the response returns the external ID. You can use this external image ID to create a client-side index to associate the faces with each image. You can then use the index to find all faces in an image.

You can specify the maximum number of faces to index with the `MaxFaces` input parameter. This is useful when you want to index the largest faces in an image and donât want to index smaller faces, such as those belonging to people standing in the background.

The `QualityFilter` input parameter allows you to filter out detected faces that donât meet a required quality bar. The quality bar is based on a variety of common use cases. By default, `IndexFaces` chooses the quality bar thatâs used to filter faces. You can also explicitly choose the quality bar. Use `QualityFilter` , to set the quality bar by specifying `LOW` , `MEDIUM` , or `HIGH` . If you do not want to filter detected faces, specify `NONE` .

### Note

To use quality filtering, you need a collection associated with version 3 of the face model or higher. To get the version of the face model associated with a collection, call  DescribeCollection .

Information about faces detected in an image, but not indexed, is returned in an array of  UnindexedFace objects, `UnindexedFaces` . Faces arenât indexed for reasons such as:

- The number of faces detected exceeds the value of the `MaxFaces` request parameter.
- The face is too small compared to the image dimensions.
- The face is too blurry.
- The image is too dark.
- The face has an extreme pose.
- The face doesnât have enough detail to be suitable for face search.

In response, the `IndexFaces` operation returns an array of metadata for all detected faces, `FaceRecords` . This includes:

- The bounding box, `BoundingBox` , of the detected face.
- A confidence value, `Confidence` , which indicates the confidence that the bounding box contains a face.
- A face ID, `FaceId` , assigned by the service for each face thatâs detected and stored.
- An image ID, `ImageId` , assigned by the service for the input image.

If you request `ALL` or specific facial attributes (e.g., `FACE_OCCLUDED` ) by using the detectionAttributes parameter, Amazon Rekognition returns detailed facial attributes, such as facial landmarks (for example, location of eye and mouth), facial occlusion, and other facial attributes.

If you provide the same image, specify the same collection, and use the same external ID in the `IndexFaces` operation, Amazon Rekognition doesnât save duplicate face metadata.

The input image is passed either as base64-encoded image bytes, or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes isnât supported. The image must be formatted as a PNG or JPEG file.

This operation requires permissions to perform the `rekognition:IndexFaces` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/IndexFaces)

## Synopsis

```
index-faces
--collection-id <value>
[--image <value>]
[--external-image-id <value>]
[--detection-attributes <value>]
[--max-faces <value>]
[--quality-filter <value>]
[--image-bytes <value>]
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

`--collection-id` (string)

The ID of an existing collection to which you want to add the faces that are detected in the input images.

`--image` (structure)

The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes isnât supported.

If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the `Bytes` field. For more information, see Images in the Amazon Rekognition developer guide.

To specify a local file use `--image-bytes` instead.

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

`--external-image-id` (string)

The ID you want to assign to all the faces detected in the image.

`--detection-attributes` (list)

An array of facial attributes you want to be returned. A `DEFAULT` subset of facial attributes - `BoundingBox` , `Confidence` , `Pose` , `Quality` , and `Landmarks` - will always be returned. You can request for specific facial attributes (in addition to the default list) - by using `["DEFAULT", "FACE_OCCLUDED"]` or just `["FACE_OCCLUDED"]` . You can request for all facial attributes by using `["ALL"]` . Requesting more attributes may increase response time.

If you provide both, `["ALL", "DEFAULT"]` , the service uses a logical AND operator to determine which attributes to return (in this case, all attributes).

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  DEFAULT
  ALL
  AGE_RANGE
  BEARD
  EMOTIONS
  EYE_DIRECTION
  EYEGLASSES
  EYES_OPEN
  GENDER
  MOUTH_OPEN
  MUSTACHE
  FACE_OCCLUDED
  SMILE
  SUNGLASSES
```

`--max-faces` (integer)

The maximum number of faces to index. The value of `MaxFaces` must be greater than or equal to 1. `IndexFaces` returns no more than 100 detected faces in an image, even if you specify a larger value for `MaxFaces` .

If `IndexFaces` detects more faces than the value of `MaxFaces` , the faces with the lowest quality are filtered out first. If there are still more faces than the value of `MaxFaces` , the faces with the smallest bounding boxes are filtered out (up to the number thatâs needed to satisfy the value of `MaxFaces` ). Information about the unindexed faces is available in the `UnindexedFaces` array.

The faces that are returned by `IndexFaces` are sorted by the largest face bounding box size to the smallest size, in descending order.

`MaxFaces` can be used with a collection associated with any version of the face model.

`--quality-filter` (string)

A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces arenât indexed. If you specify `AUTO` , Amazon Rekognition chooses the quality bar. If you specify `LOW` , `MEDIUM` , or `HIGH` , filtering removes all faces that donât meet the chosen quality bar. The default value is `AUTO` . The quality bar is based on a variety of common use cases. Low-quality detections can occur for a number of reasons. Some examples are an object thatâs misidentified as a face, a face thatâs too blurry, or a face with a pose thatâs too extreme to use. If you specify `NONE` , no filtering is performed.

To use quality filtering, the collection you are using must be associated with version 3 of the face model or higher.

Possible values:

- `NONE`
- `AUTO`
- `LOW`
- `MEDIUM`
- `HIGH`

`--image-bytes` (blob)

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

**To add faces to a collection**

The following `index-faces` command adds the faces found in an image to the specified collection.

```
aws rekognition index-faces \
    --image '{"S3Object":{"Bucket":"MyVideoS3Bucket","Name":"MyPicture.jpg"}}' \
    --collection-id MyCollection \
    --max-faces 1 \
    --quality-filter "AUTO" \
    --detection-attributes "ALL" \
    --external-image-id "MyPicture.jpg"
```

Output:

```
{
    "FaceRecords": [
        {
            "FaceDetail": {
                "Confidence": 99.993408203125,
                "Eyeglasses": {
                    "Confidence": 99.11750030517578,
                    "Value": false
                },
                "Sunglasses": {
                    "Confidence": 99.98249053955078,
                    "Value": false
                },
                "Gender": {
                    "Confidence": 99.92769622802734,
                    "Value": "Male"
                },
                "Landmarks": [
                    {
                        "Y": 0.26750367879867554,
                        "X": 0.6202793717384338,
                        "Type": "eyeLeft"
                    },
                    {
                        "Y": 0.26642778515815735,
                        "X": 0.6787431836128235,
                        "Type": "eyeRight"
                    },
                    {
                        "Y": 0.31361380219459534,
                        "X": 0.6421601176261902,
                        "Type": "nose"
                    },
                    {
                        "Y": 0.3495299220085144,
                        "X": 0.6216195225715637,
                        "Type": "mouthLeft"
                    },
                    {
                        "Y": 0.35194727778434753,
                        "X": 0.669899046421051,
                        "Type": "mouthRight"
                    },
                    {
                        "Y": 0.26844894886016846,
                        "X": 0.6210268139839172,
                        "Type": "leftPupil"
                    },
                    {
                        "Y": 0.26707562804222107,
                        "X": 0.6817160844802856,
                        "Type": "rightPupil"
                    },
                    {
                        "Y": 0.24834522604942322,
                        "X": 0.6018546223640442,
                        "Type": "leftEyeBrowLeft"
                    },
                    {
                        "Y": 0.24397172033786774,
                        "X": 0.6172008514404297,
                        "Type": "leftEyeBrowUp"
                    },
                    {
                        "Y": 0.24677404761314392,
                        "X": 0.6339119076728821,
                        "Type": "leftEyeBrowRight"
                    },
                    {
                        "Y": 0.24582654237747192,
                        "X": 0.6619398593902588,
                        "Type": "rightEyeBrowLeft"
                    },
                    {
                        "Y": 0.23973053693771362,
                        "X": 0.6804757118225098,
                        "Type": "rightEyeBrowUp"
                    },
                    {
                        "Y": 0.24441994726657867,
                        "X": 0.6978968977928162,
                        "Type": "rightEyeBrowRight"
                    },
                    {
                        "Y": 0.2695908546447754,
                        "X": 0.6085202693939209,
                        "Type": "leftEyeLeft"
                    },
                    {
                        "Y": 0.26716896891593933,
                        "X": 0.6315826177597046,
                        "Type": "leftEyeRight"
                    },
                    {
                        "Y": 0.26289820671081543,
                        "X": 0.6202316880226135,
                        "Type": "leftEyeUp"
                    },
                    {
                        "Y": 0.27123287320137024,
                        "X": 0.6205548048019409,
                        "Type": "leftEyeDown"
                    },
                    {
                        "Y": 0.2668408751487732,
                        "X": 0.6663622260093689,
                        "Type": "rightEyeLeft"
                    },
                    {
                        "Y": 0.26741549372673035,
                        "X": 0.6910083889961243,
                        "Type": "rightEyeRight"
                    },
                    {
                        "Y": 0.2614026665687561,
                        "X": 0.6785826086997986,
                        "Type": "rightEyeUp"
                    },
                    {
                        "Y": 0.27075251936912537,
                        "X": 0.6789616942405701,
                        "Type": "rightEyeDown"
                    },
                    {
                        "Y": 0.3211299479007721,
                        "X": 0.6324167847633362,
                        "Type": "noseLeft"
                    },
                    {
                        "Y": 0.32276326417922974,
                        "X": 0.6558475494384766,
                        "Type": "noseRight"
                    },
                    {
                        "Y": 0.34385165572166443,
                        "X": 0.6444970965385437,
                        "Type": "mouthUp"
                    },
                    {
                        "Y": 0.3671635091304779,
                        "X": 0.6459195017814636,
                        "Type": "mouthDown"
                    }
                ],
                "Pose": {
                    "Yaw": -9.54541015625,
                    "Roll": -0.5709401965141296,
                    "Pitch": 0.6045494675636292
                },
                "Emotions": [
                    {
                        "Confidence": 39.90074157714844,
                        "Type": "HAPPY"
                    },
                    {
                        "Confidence": 23.38753890991211,
                        "Type": "CALM"
                    },
                    {
                        "Confidence": 5.840933322906494,
                        "Type": "CONFUSED"
                    }
                ],
                "AgeRange": {
                    "High": 63,
                    "Low": 45
                },
                "EyesOpen": {
                    "Confidence": 99.80887603759766,
                    "Value": true
                },
                "BoundingBox": {
                    "Width": 0.18562500178813934,
                    "Top": 0.1618015021085739,
                    "Left": 0.5575000047683716,
                    "Height": 0.24770642817020416
                },
                "Smile": {
                    "Confidence": 99.69740295410156,
                    "Value": false
                },
                "MouthOpen": {
                    "Confidence": 99.97393798828125,
                    "Value": false
                },
                "Quality": {
                    "Sharpness": 95.54405975341797,
                    "Brightness": 63.867706298828125
                },
                "Mustache": {
                    "Confidence": 97.05007934570312,
                    "Value": false
                },
                "Beard": {
                    "Confidence": 87.34505462646484,
                    "Value": false
                }
            },
            "Face": {
                "BoundingBox": {
                    "Width": 0.18562500178813934,
                    "Top": 0.1618015021085739,
                    "Left": 0.5575000047683716,
                    "Height": 0.24770642817020416
                },
                "FaceId": "ce7ed422-2132-4a11-ab14-06c5c410f29f",
                "ExternalImageId": "example-image.jpg",
                "Confidence": 99.993408203125,
                "ImageId": "8d67061e-90d2-598f-9fbd-29c8497039c0"
            }
        }
    ],
    "UnindexedFaces": [],
    "FaceModelVersion": "3.0",
    "OrientationCorrection": "ROTATE_0"
}
```

For more information, see [Adding Faces to a Collection](https://docs.aws.amazon.com/rekognition/latest/dg/add-faces-to-collection-procedure.html) in the *Amazon Rekognition Developer Guide*.

## Output

FaceRecords -> (list)

An array of faces detected and added to the collection. For more information, see Searching Faces in a Collection in the Amazon Rekognition Developer Guide.

(structure)

Object containing both the face metadata (stored in the backend database), and facial attributes that are detected but arenât stored in the database.

Face -> (structure)

Describes the face properties such as the bounding box, face ID, image ID of the input image, and external image ID that you assigned.

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

FaceDetail -> (structure)

Structure containing attributes of the face that the algorithm detected.

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

OrientationCorrection -> (string)

If your collection is associated with a face detection model thatâs later than version 3.0, the value of `OrientationCorrection` is always null and no orientation information is returned.

If your collection is associated with a face detection model thatâs version 3.0 or earlier, the following applies:

- If the input image is in .jpeg format, it might contain exchangeable image file format (Exif) metadata that includes the imageâs orientation. Amazon Rekognition uses this orientation information to perform image correction - the bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation. Images in .png format donât contain Exif metadata. The value of `OrientationCorrection` is null.
- If the image doesnât contain orientation information in its Exif metadata, Amazon Rekognition returns an estimated orientation (ROTATE_0, ROTATE_90, ROTATE_180, ROTATE_270). Amazon Rekognition doesnât perform image correction for images. The bounding box coordinates arenât translated and represent the object locations before the image is rotated.

Bounding box information is returned in the `FaceRecords` array. You can get the version of the face detection model by calling  DescribeCollection .

FaceModelVersion -> (string)

The version number of the face detection model thatâs associated with the input collection (`CollectionId` ).

UnindexedFaces -> (list)

An array of faces that were detected in the image but werenât indexed. They werenât indexed because the quality filter identified them as low quality, or the `MaxFaces` request parameter filtered them out. To use the quality filter, you specify the `QualityFilter` request parameter.

(structure)

A face that  IndexFaces detected, but didnât index. Use the `Reasons` response attribute to determine why a face wasnât indexed.

Reasons -> (list)

An array of reasons that specify why a face wasnât indexed.

- EXTREME_POSE - The face is at a pose that canât be detected. For example, the head is turned too far away from the camera.
- EXCEEDS_MAX_FACES - The number of faces detected is already higher than that specified by the `MaxFaces` input parameter for `IndexFaces` .
- LOW_BRIGHTNESS - The image is too dark.
- LOW_SHARPNESS - The image is too blurry.
- LOW_CONFIDENCE - The face was detected with a low confidence.
- SMALL_BOUNDING_BOX - The bounding box around the face is too small.

(string)

FaceDetail -> (structure)

The structure that contains attributes of a face that `IndexFaces` detected, but didnât index.

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