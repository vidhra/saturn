# search-faces-by-imageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/search-faces-by-image.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/search-faces-by-image.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# search-faces-by-image

## Description

For a given input image, first detects the largest face in the image, and then searches the specified collection for matching faces. The operation compares the features of the input face with faces in the specified collection.

### Note

To search for all faces in an input image, you might first call the  IndexFaces operation, and then use the face IDs returned in subsequent calls to the  SearchFaces operation.

You can also call the `DetectFaces` operation and use the bounding boxes in the response to make face crops, which then you can pass in to the `SearchFacesByImage` operation.

You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.

The response returns an array of faces that match, ordered by similarity score with the highest similarity first. More specifically, it is an array of metadata for each face match found. Along with the metadata, the response also includes a `similarity` indicating how similar the face is to the input face. In the response, the operation also returns the bounding box (and a confidence level that the bounding box contains a face) of the face that Amazon Rekognition used for the input image.

If no faces are detected in the input image, `SearchFacesByImage` returns an `InvalidParameterException` error.

For an example, Searching for a Face Using an Image in the Amazon Rekognition Developer Guide.

The `QualityFilter` input parameter allows you to filter out detected faces that donât meet a required quality bar. The quality bar is based on a variety of common use cases. Use `QualityFilter` to set the quality bar for filtering by specifying `LOW` , `MEDIUM` , or `HIGH` . If you do not want to filter detected faces, specify `NONE` . The default value is `NONE` .

### Note

To use quality filtering, you need a collection associated with version 3 of the face model or higher. To get the version of the face model associated with a collection, call  DescribeCollection .

This operation requires permissions to perform the `rekognition:SearchFacesByImage` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/SearchFacesByImage)

## Synopsis

```
search-faces-by-image
--collection-id <value>
[--image <value>]
[--max-faces <value>]
[--face-match-threshold <value>]
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

ID of the collection to search.

`--image` (structure)

The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.

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

`--max-faces` (integer)

Maximum number of faces to return. The operation returns the maximum number of faces with the highest confidence in the match.

`--face-match-threshold` (float)

(Optional) Specifies the minimum confidence in the face match to return. For example, donât return any matches where confidence in matches is less than 70%. The default value is 80%.

`--quality-filter` (string)

A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces arenât searched for in the collection. If you specify `AUTO` , Amazon Rekognition chooses the quality bar. If you specify `LOW` , `MEDIUM` , or `HIGH` , filtering removes all faces that donât meet the chosen quality bar. The quality bar is based on a variety of common use cases. Low-quality detections can occur for a number of reasons. Some examples are an object thatâs misidentified as a face, a face thatâs too blurry, or a face with a pose thatâs too extreme to use. If you specify `NONE` , no filtering is performed. The default value is `NONE` .

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

**To search for faces in a collection that match the largest face in an image.**

The following `search-faces-by-image` command searches for faces in a collection that match the largest face in the specified image.:

```
aws rekognition search-faces-by-image \
    --image '{"S3Object":{"Bucket":"MyImageS3Bucket","Name":"ExamplePerson.jpg"}}' \
    --collection-id MyFaceImageCollection

{
    "SearchedFaceBoundingBox": {
        "Width": 0.18562500178813934,
        "Top": 0.1618015021085739,
        "Left": 0.5575000047683716,
        "Height": 0.24770642817020416
    },
    "SearchedFaceConfidence": 99.993408203125,
    "FaceMatches": [
        {
            "Face": {
                "BoundingBox": {
                    "Width": 0.18562500178813934,
                    "Top": 0.1618019938468933,
                    "Left": 0.5575000047683716,
                    "Height": 0.24770599603652954
                },
                "FaceId": "ce7ed422-2132-4a11-ab14-06c5c410f29f",
                "ExternalImageId": "example-image.jpg",
                "Confidence": 99.99340057373047,
                "ImageId": "8d67061e-90d2-598f-9fbd-29c8497039c0"
            },
            "Similarity": 99.97913360595703
        },
        {
            "Face": {
                "BoundingBox": {
                    "Width": 0.18562500178813934,
                    "Top": 0.1618019938468933,
                    "Left": 0.5575000047683716,
                    "Height": 0.24770599603652954
                },
                "FaceId": "13692fe4-990a-4679-b14a-5ac23d135eab",
                "ExternalImageId": "image3.jpg",
                "Confidence": 99.99340057373047,
                "ImageId": "8df18239-9ad1-5acd-a46a-6581ff98f51b"
            },
            "Similarity": 99.97913360595703
        },
        {
            "Face": {
                "BoundingBox": {
                    "Width": 0.41499999165534973,
                    "Top": 0.09187500178813934,
                    "Left": 0.28083300590515137,
                    "Height": 0.3112500011920929
                },
                "FaceId": "8d3cfc70-4ba8-4b36-9644-90fba29c2dac",
                "ExternalImageId": "image2.jpg",
                "Confidence": 99.99769592285156,
                "ImageId": "a294da46-2cb1-5cc4-9045-61d7ca567662"
            },
            "Similarity": 99.18069458007812
        },
        {
            "Face": {
                "BoundingBox": {
                    "Width": 0.48166701197624207,
                    "Top": 0.20999999344348907,
                    "Left": 0.21250000596046448,
                    "Height": 0.36125001311302185
                },
                "FaceId": "bd4ceb4d-9acc-4ab7-8ef8-1c2d2ba0a66a",
                "ExternalImageId": "image1.jpg",
                "Confidence": 99.99949645996094,
                "ImageId": "5e1a7588-e5a0-5ee3-bd00-c642518dfe3a"
            },
            "Similarity": 98.66607666015625
        },
        {
            "Face": {
                "BoundingBox": {
                    "Width": 0.5349419713020325,
                    "Top": 0.29124999046325684,
                    "Left": 0.16389399766921997,
                    "Height": 0.40187498927116394
                },
                "FaceId": "745f7509-b1fa-44e0-8b95-367b1359638a",
                "ExternalImageId": "image9.jpg",
                "Confidence": 99.99979400634766,
                "ImageId": "67a34327-48d1-5179-b042-01e52ccfeada"
            },
            "Similarity": 98.24278259277344
        },
        {
            "Face": {
                "BoundingBox": {
                    "Width": 0.5307819843292236,
                    "Top": 0.2862499952316284,
                    "Left": 0.1564060002565384,
                    "Height": 0.3987500071525574
                },
                "FaceId": "2eb5f3fd-e2a9-4b1c-a89f-afa0a518fe06",
                "ExternalImageId": "image10.jpg",
                "Confidence": 99.99970245361328,
                "ImageId": "3c314792-197d-528d-bbb6-798ed012c150"
            },
            "Similarity": 98.10665893554688
        },
        {
            "Face": {
                "BoundingBox": {
                    "Width": 0.5074880123138428,
                    "Top": 0.3774999976158142,
                    "Left": 0.18302799761295319,
                    "Height": 0.3812499940395355
                },
                "FaceId": "086261e8-6deb-4bc0-ac73-ab22323cc38d",
                "ExternalImageId": "image6.jpg",
                "Confidence": 99.99930572509766,
                "ImageId": "ae1593b0-a8f6-5e24-a306-abf529e276fa"
            },
            "Similarity": 98.10526275634766
        },
        {
            "Face": {
                "BoundingBox": {
                    "Width": 0.5574039816856384,
                    "Top": 0.37187498807907104,
                    "Left": 0.14559100568294525,
                    "Height": 0.4181250035762787
                },
                "FaceId": "11c4bd3c-19c5-4eb8-aecc-24feb93a26e1",
                "ExternalImageId": "image5.jpg",
                "Confidence": 99.99960327148438,
                "ImageId": "80739b4d-883f-5b78-97cf-5124038e26b9"
            },
            "Similarity": 97.94659423828125
        },
        {
            "Face": {
                "BoundingBox": {
                    "Width": 0.5773710012435913,
                    "Top": 0.34437501430511475,
                    "Left": 0.12396000325679779,
                    "Height": 0.4337500035762787
                },
                "FaceId": "57189455-42b0-4839-a86c-abda48b13174",
                "ExternalImageId": "image8.jpg",
                "Confidence": 100.0,
                "ImageId": "0aff2f37-e7a2-5dbc-a3a3-4ef6ec18eaa0"
            },
            "Similarity": 97.93476867675781
        }
    ],
    "FaceModelVersion": "3.0"
}
```

For more information, see [Searching for a Face Using an Image](https://docs.aws.amazon.com/rekognition/latest/dg/search-face-with-image-procedure.html) in the *Amazon Rekognition Developer Guide*.

## Output

SearchedFaceBoundingBox -> (structure)

The bounding box around the face in the input image that Amazon Rekognition used for the search.

Width -> (float)

Width of the bounding box as a ratio of the overall image width.

Height -> (float)

Height of the bounding box as a ratio of the overall image height.

Left -> (float)

Left coordinate of the bounding box as a ratio of overall image width.

Top -> (float)

Top coordinate of the bounding box as a ratio of overall image height.

SearchedFaceConfidence -> (float)

The level of confidence that the `searchedFaceBoundingBox` , contains a face.

FaceMatches -> (list)

An array of faces that match the input face, along with the confidence in the match.

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

FaceModelVersion -> (string)

Version number of the face detection model associated with the input collection (`CollectionId` ).