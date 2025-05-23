# detect-moderation-labelsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/detect-moderation-labels.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/detect-moderation-labels.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# detect-moderation-labels

## Description

Detects unsafe content in a specified JPEG or PNG format image. Use `DetectModerationLabels` to moderate images depending on your requirements. For example, you might want to filter images that contain nudity, but not images containing suggestive content.

To filter images, use the labels returned by `DetectModerationLabels` to determine which types of content are appropriate.

For information about moderation labels, see Detecting Unsafe Content in the Amazon Rekognition Developer Guide.

You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.

You can specify an adapter to use when retrieving label predictions by providing a `ProjectVersionArn` to the `ProjectVersion` argument.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DetectModerationLabels)

## Synopsis

```
detect-moderation-labels
[--image <value>]
[--min-confidence <value>]
[--human-loop-config <value>]
[--project-version <value>]
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

`--min-confidence` (float)

Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesnât return any labels with a confidence level lower than this specified value.

If you donât specify `MinConfidence` , the operation returns labels with confidence values greater than or equal to 50 percent.

`--human-loop-config` (structure)

Sets up the configuration for human evaluation, including the FlowDefinition the image will be sent to.

HumanLoopName -> (string)

The name of the human review used for this image. This should be kept unique within a region.

FlowDefinitionArn -> (string)

The Amazon Resource Name (ARN) of the flow definition. You can create a flow definition by using the Amazon Sagemaker [CreateFlowDefinition](https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateFlowDefinition.html) Operation.

DataAttributes -> (structure)

Sets attributes of the input data.

ContentClassifiers -> (list)

Sets whether the input image is free of personally identifiable information.

(string)

Shorthand Syntax:

```
HumanLoopName=string,FlowDefinitionArn=string,DataAttributes={ContentClassifiers=[string,string]}
```

JSON Syntax:

```
{
  "HumanLoopName": "string",
  "FlowDefinitionArn": "string",
  "DataAttributes": {
    "ContentClassifiers": ["FreeOfPersonallyIdentifiableInformation"|"FreeOfAdultContent", ...]
  }
}
```

`--project-version` (string)

Identifier for the custom adapter. Expects the ProjectVersionArn as a value. Use the CreateProject or CreateProjectVersion APIs to create a custom adapter.

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

**To detect unsafe content in an image**

The following `detect-moderation-labels` command detects unsafe content in the specified image stored in an Amazon S3 bucket.

```
aws rekognition detect-moderation-labels \
    --image "S3Object={Bucket=MyImageS3Bucket,Name=gun.jpg}"
```

Output:

```
{
    "ModerationModelVersion": "3.0",
    "ModerationLabels": [
        {
            "Confidence": 97.29618072509766,
            "ParentName": "Violence",
            "Name": "Weapon Violence"
        },
        {
            "Confidence": 97.29618072509766,
            "ParentName": "",
            "Name": "Violence"
        }
    ]
}
```

For more information, see [Detecting Unsafe Images](https://docs.aws.amazon.com/rekognition/latest/dg/procedure-moderate-images.html) in the *Amazon Rekognition Developer Guide*.

## Output

ModerationLabels -> (list)

Array of detected Moderation labels. For video operations, this includes the time, in milliseconds from the start of the video, they were detected.

(structure)

Provides information about a single type of inappropriate, unwanted, or offensive content found in an image or video. Each type of moderated content has a label within a hierarchical taxonomy. For more information, see Content moderation in the Amazon Rekognition Developer Guide.

Confidence -> (float)

Specifies the confidence that Amazon Rekognition has that the label has been correctly identified.

If you donât specify the `MinConfidence` parameter in the call to `DetectModerationLabels` , the operation returns labels with a confidence value greater than or equal to 50 percent.

Name -> (string)

The label name for the type of unsafe content detected in the image.

ParentName -> (string)

The name for the parent label. Labels at the top level of the hierarchy have the parent label `""` .

TaxonomyLevel -> (integer)

The level of the moderation label with regard to its taxonomy, from 1 to 3.

ModerationModelVersion -> (string)

Version number of the base moderation detection model that was used to detect unsafe content.

HumanLoopActivationOutput -> (structure)

Shows the results of the human in the loop evaluation.

HumanLoopArn -> (string)

The Amazon Resource Name (ARN) of the HumanLoop created.

HumanLoopActivationReasons -> (list)

Shows if and why human review was needed.

(string)

HumanLoopActivationConditionsEvaluationResults -> (string)

Shows the result of condition evaluations, including those conditions which activated a human review.

ProjectVersion -> (string)

Identifier of the custom adapter that was used during inference. If during inference the adapter was EXPIRED, then the parameter will not be returned, indicating that a base moderation detection project version was used.

ContentTypes -> (list)

A list of predicted results for the type of content an image contains. For example, the image content might be from animation, sports, or a video game.

(structure)

Contains information regarding the confidence and name of a detected content type.

Confidence -> (float)

The confidence level of the label given

Name -> (string)

The name of the label