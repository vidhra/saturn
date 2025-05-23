# detect-protective-equipmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/detect-protective-equipment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/detect-protective-equipment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# detect-protective-equipment

## Description

Detects Personal Protective Equipment (PPE) worn by people detected in an image. Amazon Rekognition can detect the following types of PPE.

- Face cover
- Hand cover
- Head cover

You pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. The image must be either a PNG or JPG formatted file.

`DetectProtectiveEquipment` detects PPE worn by up to 15 persons detected in an image.

For each person detected in the image the API returns an array of body parts (face, head, left-hand, right-hand). For each body part, an array of detected items of PPE is returned, including an indicator of whether or not the PPE covers the body part. The API returns the confidence it has in each detection (person, PPE, body part and body part coverage). It also returns a bounding box ( BoundingBox ) for each detected person and each detected item of PPE.

You can optionally request a summary of detected PPE items with the `SummarizationAttributes` input parameter. The summary provides the following information.

- The persons detected as wearing all of the types of PPE that you specify.
- The persons detected as not wearing all of the types PPE that you specify.
- The persons detected where PPE adornment could not be determined.

This is a stateless API operation. That is, the operation does not persist any data.

This operation requires permissions to perform the `rekognition:DetectProtectiveEquipment` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DetectProtectiveEquipment)

## Synopsis

```
detect-protective-equipment
[--image <value>]
[--summarization-attributes <value>]
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

`--image` (structure)

The image in which you want to detect PPE on detected persons. The image can be passed as image bytes or you can reference an image stored in an Amazon S3 bucket.

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

`--summarization-attributes` (structure)

An array of PPE types that you want to summarize.

MinConfidence -> (float)

The minimum confidence level for which you want summary information. The confidence level applies to person detection, body part detection, equipment detection, and body part coverage. Amazon Rekognition doesnât return summary information with a confidence than this specified value. There isnât a default value.

Specify a `MinConfidence` value that is between 50-100% as `DetectProtectiveEquipment` returns predictions only where the detection confidence is between 50% - 100%. If you specify a value that is less than 50%, the results are the same specifying a value of 50%.

RequiredEquipmentTypes -> (list)

An array of personal protective equipment types for which you want summary information. If a person is detected wearing a required requipment type, the personâs ID is added to the `PersonsWithRequiredEquipment` array field returned in  ProtectiveEquipmentSummary by `DetectProtectiveEquipment` .

(string)

Shorthand Syntax:

```
MinConfidence=float,RequiredEquipmentTypes=string,string
```

JSON Syntax:

```
{
  "MinConfidence": float,
  "RequiredEquipmentTypes": ["FACE_COVER"|"HAND_COVER"|"HEAD_COVER", ...]
}
```

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

ProtectiveEquipmentModelVersion -> (string)

The version number of the PPE detection model used to detect PPE in the image.

Persons -> (list)

An array of persons detected in the image (including persons not wearing PPE).

(structure)

A person detected by a call to  DetectProtectiveEquipment . The API returns all persons detected in the input image in an array of `ProtectiveEquipmentPerson` objects.

BodyParts -> (list)

An array of body parts detected on a personâs body (including body parts without PPE).

(structure)

Information about a body part detected by  DetectProtectiveEquipment that contains PPE. An array of `ProtectiveEquipmentBodyPart` objects is returned for each person detected by `DetectProtectiveEquipment` .

Name -> (string)

The detected body part.

Confidence -> (float)

The confidence that Amazon Rekognition has in the detection accuracy of the detected body part.

EquipmentDetections -> (list)

An array of Personal Protective Equipment items detected around a body part.

(structure)

Information about an item of Personal Protective Equipment (PPE) detected by  DetectProtectiveEquipment . For more information, see  DetectProtectiveEquipment .

BoundingBox -> (structure)

A bounding box surrounding the item of detected PPE.

Width -> (float)

Width of the bounding box as a ratio of the overall image width.

Height -> (float)

Height of the bounding box as a ratio of the overall image height.

Left -> (float)

Left coordinate of the bounding box as a ratio of overall image width.

Top -> (float)

Top coordinate of the bounding box as a ratio of overall image height.

Confidence -> (float)

The confidence that Amazon Rekognition has that the bounding box (`BoundingBox` ) contains an item of PPE.

Type -> (string)

The type of detected PPE.

CoversBodyPart -> (structure)

Information about the body part covered by the detected PPE.

Confidence -> (float)

The confidence that Amazon Rekognition has in the value of `Value` .

Value -> (boolean)

True if the PPE covers the corresponding body part, otherwise false.

BoundingBox -> (structure)

A bounding box around the detected person.

Width -> (float)

Width of the bounding box as a ratio of the overall image width.

Height -> (float)

Height of the bounding box as a ratio of the overall image height.

Left -> (float)

Left coordinate of the bounding box as a ratio of overall image width.

Top -> (float)

Top coordinate of the bounding box as a ratio of overall image height.

Confidence -> (float)

The confidence that Amazon Rekognition has that the bounding box contains a person.

Id -> (integer)

The identifier for the detected person. The identifier is only unique for a single call to `DetectProtectiveEquipment` .

Summary -> (structure)

Summary information for the types of PPE specified in the `SummarizationAttributes` input parameter.

PersonsWithRequiredEquipment -> (list)

An array of IDs for persons who are wearing detected personal protective equipment.

(integer)

PersonsWithoutRequiredEquipment -> (list)

An array of IDs for persons who are not wearing all of the types of PPE specified in the `RequiredEquipmentTypes` field of the detected personal protective equipment.

(integer)

PersonsIndeterminate -> (list)

An array of IDs for persons where it was not possible to determine if they are wearing personal protective equipment.

(integer)