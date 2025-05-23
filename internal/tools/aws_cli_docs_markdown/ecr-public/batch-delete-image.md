# batch-delete-imageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/batch-delete-image.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/batch-delete-image.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecr-public](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/index.html#cli-aws-ecr-public) ]

# batch-delete-image

## Description

Deletes a list of specified images that are within a repository in a public registry. Images are specified with either an `imageTag` or `imageDigest` .

You can remove a tag from an image by specifying the imageâs tag in your request. When you remove the last tag from an image, the image is deleted from your repository.

You can completely delete an image (and all of its tags) by specifying the digest of the image in your request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecr-public-2020-10-30/BatchDeleteImage)

## Synopsis

```
batch-delete-image
[--registry-id <value>]
--repository-name <value>
--image-ids <value>
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

`--registry-id` (string)

The Amazon Web Services account ID, or registry alias, thatâs associated with the registry that contains the image to delete. If you do not specify a registry, the default public registry is assumed.

`--repository-name` (string)

The repository in a public registry that contains the image to delete.

`--image-ids` (list)

A list of image ID references that correspond to images to delete. The format of the `imageIds` reference is `imageTag=tag` or `imageDigest=digest` .

(structure)

An object with identifying information for an Amazon ECR image.

imageDigest -> (string)

The `sha256` digest of the image manifest.

imageTag -> (string)

The tag thatâs used for the image.

Shorthand Syntax:

```
imageDigest=string,imageTag=string ...
```

JSON Syntax:

```
[
  {
    "imageDigest": "string",
    "imageTag": "string"
  }
  ...
]
```

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

**Example 1: To delete an image by using image digest ids, the image and all of its tags are deleted within a repository in a public registry**

The following `batch-delete-image` example deletes an image by specifying the image digest.:

```
aws ecr-public batch-delete-image \
    --repository-name project-a/nginx-web-app \
    --image-ids imageDigest=sha256:b1f9deb5fe3711a3278379ebbcaefbc5d70a2263135db86bd27a0dae150546c2
```

Output:

```
{
"imageIds": [
    {
        "imageDigest": "sha256:b1f9deb5fe3711a3278379ebbcaefbc5d70a2263135db86bd27a0dae150546c2",
        "imageTag": "latest"
    }
],
"failures": []
}
```

For more information, see [Deleting an image in a public repository](https://docs.aws.amazon.com/AmazonECR/latest/public/public-image-delete.html) in the *Amazon ECR Public User Guide*.

**Example 2: To delete any image by specifying the tag associated with the image you want to delete from the repository.**

The following `batch-delete-image` example deletes an image by specifying the tag associated with the image repository named `project-a/nginx-web-app` in a public registry. If you have only one tag and execute this command, it will remove the image. Otherwise, if you have multiple tags for the same image, specify one, and only the tag is removed from repository and not the image.

```
aws ecr-public batch-delete-image \
    --repository-name project-a/nginx-web-app \
    --image-ids imageTag=_temp
```

Output:

```
{
    "imageIds": [
        {
            "imageDigest": "sha256:f7a86a0760e2f8d7eff07e515fc87bf4bac45c35376c06f9a280f15ecad6d7e0",
            "imageTag": "_temp"
        }
    ],
    "failures": []
}
```

For more information, see [Deleting an image in a public repository](https://docs.aws.amazon.com/AmazonECR/latest/public/public-image-delete.html) in the *Amazon ECR Public User Guide*.

**Example 3: To delete multiple images, you can specify multiple image tags or image digests in the request for a repository in a public registry.**

The following `batch-delete-image` example delete multiple images from a repository named project-a/nginx-web-app by specifying multiple image tags or image digests in the request.

```
aws ecr-public batch-delete-image \
    --repository-name project-a/nginx-web-app \
    --image-ids imageTag=temp2.0  imageDigest=sha256:47ba980bc055353d9c0af89b1894f68faa43ca93856917b8406316be86f01278
```

Output:

```
{
     "imageIds": [
         {
             "imageDigest": "sha256:47ba980bc055353d9c0af89b1894f68faa43ca93856917b8406316be86f01278"
         },
         {
             "imageDigest": "sha256:f7a86a0760e2f8d7eff07e515fc87bf4bac45c35376c06f9a280f15ecad6d7e0",
             "imageTag": "temp2.0"
         }
     ],
     "failures": []
 }
```

For more information, see [Deleting an image in a public repository](https://docs.aws.amazon.com/AmazonECR/latest/public/public-image-delete.html) in the *Amazon ECR Public User Guide*.

**Example 4: To delete an image in cross AWS Account using registry-id and imagedigest ids, the image and all of its tags are deleted within a repository in a public registry**

The following `batch-delete-image` example deletes an image by specifying the image digest in the cross AWS Account.:

```
aws ecr-public batch-delete-image \
    --registry-id 123456789098 \
    --repository-name project-a/nginx-web-app \
    --image-ids imageDigest=sha256:b1f9deb5fe3711a3278379ebbcaefbc5d70a2263135db86bd27a0dae150546c2 \
    --region us-east-1
```

Output:

```
{
    "imageIds": [
        {
            "imageDigest": "sha256:b1f9deb5fe3711a3278379ebbcaefbc5d70a2263135db86bd27a0dae150546c2",
            "imageTag": "temp2.0"
        }
    ],
    "failures": []
}
```

For more information, see [Deleting an image in a public repository](https://docs.aws.amazon.com/AmazonECR/latest/public/public-image-delete.html) in the *Amazon ECR Public User Guide*.

## Output

imageIds -> (list)

The image IDs of the deleted images.

(structure)

An object with identifying information for an Amazon ECR image.

imageDigest -> (string)

The `sha256` digest of the image manifest.

imageTag -> (string)

The tag thatâs used for the image.

failures -> (list)

Any failures associated with the call.

(structure)

An object that represents an Amazon ECR image failure.

imageId -> (structure)

The image ID thatâs associated with the failure.

imageDigest -> (string)

The `sha256` digest of the image manifest.

imageTag -> (string)

The tag thatâs used for the image.

failureCode -> (string)

The code thatâs associated with the failure.

failureReason -> (string)

The reason for the failure.