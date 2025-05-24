# search-users-by-imageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/search-users-by-image.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/search-users-by-image.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# search-users-by-image

## Description

Searches for UserIDs using a supplied image. It first detects the largest face in the image, and then searches a specified collection for matching UserIDs.

The operation returns an array of UserIDs that match the face in the supplied image, ordered by similarity score with the highest similarity first. It also returns a bounding box for the face found in the input image.

Information about faces detected in the supplied image, but not used for the search, is returned in an array of `UnsearchedFace` objects. If no valid face is detected in the image, the response will contain an empty `UserMatches` list and no `SearchedFace` object.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/SearchUsersByImage)

## Synopsis

```
search-users-by-image
--collection-id <value>
[--image <value>]
[--user-match-threshold <value>]
[--max-users <value>]
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

The ID of an existing collection containing the UserID.

`--image` (structure)

Provides the input image either as bytes or an S3 object.

You pass image bytes to an Amazon Rekognition API operation by using the `Bytes` property. For example, you would use the `Bytes` property to pass an image loaded from a local file system. Image bytes passed by using the `Bytes` property must be base64-encoded. Your code may not need to encode image bytes if you are using an AWS SDK to call Amazon Rekognition API operations.

For more information, see Analyzing an Image Loaded from a Local File System in the Amazon Rekognition Developer Guide.

You pass images stored in an S3 bucket to an Amazon Rekognition API operation by using the `S3Object` property. Images stored in an S3 bucket do not need to be base64-encoded.

The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.

If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes using the Bytes property is not supported. You must first upload the image to an Amazon S3 bucket and then call the operation using the S3Object property.

For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see How Amazon Rekognition works with IAM in the Amazon Rekognition Developer Guide.

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

`--user-match-threshold` (float)

Specifies the minimum confidence in the UserID match to return. Default value is 80.

`--max-users` (integer)

Maximum number of UserIDs to return.

`--quality-filter` (string)

A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces arenât searched for in the collection. The default value is NONE.

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

## Output

UserMatches -> (list)

An array of UserID objects that matched the input face, along with the confidence in the match. The returned structure will be empty if there are no matches. Returned if the SearchUsersByImageResponse action is successful.

(structure)

Provides UserID metadata along with the confidence in the match of this UserID with the input face.

Similarity -> (float)

Describes the UserID metadata.

User -> (structure)

Confidence in the match of this UserID with the input face.

UserId -> (string)

A provided ID for the UserID. Unique within the collection.

UserStatus -> (string)

The status of the user matched to a provided FaceID.

FaceModelVersion -> (string)

Version number of the face detection model associated with the input collection CollectionId.

SearchedFace -> (structure)

A list of FaceDetail objects containing the BoundingBox for the largest face in image, as well as the confidence in the bounding box, that was searched for matches. If no valid face is detected in the image the response will contain no SearchedFace object.

FaceDetail -> (structure)

Structure containing attributes of the face that the algorithm detected.

A `FaceDetail` object contains either the default facial attributes or all facial attributes. The default attributes are `BoundingBox` , `Confidence` , `Landmarks` , `Pose` , and `Quality` .

GetFaceDetection is the only Amazon Rekognition Video stored video operation that can return a `FaceDetail` object with all attributes. To specify which attributes to return, use the `FaceAttributes` input parameter for  StartFaceDetection . The following Amazon Rekognition Video operations return only the default attributes. The corresponding Start operations donât have a `FaceAttributes` input parameter:

- GetCelebrityRecognition
- GetPersonTracking
- GetFaceSearch

The Amazon Rekognition Image  DetectFaces and  IndexFaces operations can return all facial attributes. To specify which attributes to return, use the `Attributes` input parameter for `DetectFaces` . For `IndexFaces` , use the `DetectAttributes` input parameter.

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

UnsearchedFaces -> (list)

List of UnsearchedFace objects. Contains the face details infered from the specified image but not used for search. Contains reasons that describe why a face wasnât used for Search.

(structure)

Face details inferred from the image but not used for search. The response attribute contains reasons for why a face wasnât used for Search.

FaceDetails -> (structure)

Structure containing attributes of the face that the algorithm detected.

A `FaceDetail` object contains either the default facial attributes or all facial attributes. The default attributes are `BoundingBox` , `Confidence` , `Landmarks` , `Pose` , and `Quality` .

GetFaceDetection is the only Amazon Rekognition Video stored video operation that can return a `FaceDetail` object with all attributes. To specify which attributes to return, use the `FaceAttributes` input parameter for  StartFaceDetection . The following Amazon Rekognition Video operations return only the default attributes. The corresponding Start operations donât have a `FaceAttributes` input parameter:

- GetCelebrityRecognition
- GetPersonTracking
- GetFaceSearch

The Amazon Rekognition Image  DetectFaces and  IndexFaces operations can return all facial attributes. To specify which attributes to return, use the `Attributes` input parameter for `DetectFaces` . For `IndexFaces` , use the `DetectAttributes` input parameter.

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

Reasons -> (list)

Reasons why a face wasnât used for Search.

(string)