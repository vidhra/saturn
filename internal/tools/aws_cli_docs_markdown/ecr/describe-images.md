# describe-imagesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-images.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-images.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html#cli-aws-ecr) ]

# describe-images

## Description

Returns metadata about the images in a repository.

### Note

Beginning with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the `docker images` command shows the uncompressed image size, so it may return a larger image size than the image sizes returned by  DescribeImages .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/DescribeImages)

`describe-images` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `imageDetails`

## Synopsis

```
describe-images
[--registry-id <value>]
--repository-name <value>
[--image-ids <value>]
[--filter <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

The Amazon Web Services account ID associated with the registry that contains the repository in which to describe images. If you do not specify a registry, the default registry is assumed.

`--repository-name` (string)

The repository that contains the images to describe.

`--image-ids` (list)

The list of image IDs for the requested repository.

(structure)

An object with identifying information for an image in an Amazon ECR repository.

imageDigest -> (string)

The `sha256` digest of the image manifest.

imageTag -> (string)

The tag used for the image.

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

`--filter` (structure)

The filter key and value with which to filter your `DescribeImages` results.

tagStatus -> (string)

The tag status with which to filter your  DescribeImages results. You can filter results based on whether they are `TAGGED` or `UNTAGGED` .

Shorthand Syntax:

```
tagStatus=string
```

JSON Syntax:

```
{
  "tagStatus": "TAGGED"|"UNTAGGED"|"ANY"
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To describe an image in a repository**

The folowing `describe-images` example displays details about an image in the `cluster-autoscaler` repository with the tag `v1.13.6`.

```
aws ecr describe-images \
    --repository-name cluster-autoscaler \
    --image-ids imageTag=v1.13.6
```

Output:

```
{
    "imageDetails": [
        {
            "registryId": "012345678910",
            "repositoryName": "cluster-autoscaler",
            "imageDigest": "sha256:4a1c6567c38904384ebc64e35b7eeddd8451110c299e3368d2210066487d97e5",
            "imageTags": [
                "v1.13.6"
            ],
            "imageSizeInBytes": 48318255,
            "imagePushedAt": 1565128275.0
        }
    ]
}
```

## Output

imageDetails -> (list)

A list of  ImageDetail objects that contain data about the image.

(structure)

An object that describes an image returned by a  DescribeImages operation.

registryId -> (string)

The Amazon Web Services account ID associated with the registry to which this image belongs.

repositoryName -> (string)

The name of the repository to which this image belongs.

imageDigest -> (string)

The `sha256` digest of the image manifest.

imageTags -> (list)

The list of tags associated with this image.

(string)

imageSizeInBytes -> (long)

The size, in bytes, of the image in the repository.

If the image is a manifest list, this will be the max size of all manifests in the list.

### Note

Starting with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the `docker images` command shows the uncompressed image size. Therefore, Docker might return a larger image than the image sizes returned by  DescribeImages .

imagePushedAt -> (timestamp)

The date and time, expressed in standard JavaScript date format, at which the current image was pushed to the repository.

imageScanStatus -> (structure)

The current state of the scan.

status -> (string)

The current state of an image scan.

description -> (string)

The description of the image scan status.

imageScanFindingsSummary -> (structure)

A summary of the last completed image scan.

imageScanCompletedAt -> (timestamp)

The time of the last completed image scan.

vulnerabilitySourceUpdatedAt -> (timestamp)

The time when the vulnerability data was last scanned.

findingSeverityCounts -> (map)

The image vulnerability counts, sorted by severity.

key -> (string)

value -> (integer)

imageManifestMediaType -> (string)

The media type of the image manifest.

artifactMediaType -> (string)

The artifact media type of the image.

lastRecordedPullTime -> (timestamp)

The date and time, expressed in standard JavaScript date format, when Amazon ECR recorded the last image pull.

### Note

Amazon ECR refreshes the last image pull timestamp at least once every 24 hours. For example, if you pull an image once a day then the `lastRecordedPullTime` timestamp will indicate the exact time that the image was last pulled. However, if you pull an image once an hour, because Amazon ECR refreshes the `lastRecordedPullTime` timestamp at least once every 24 hours, the result may not be the exact time that the image was last pulled.

nextToken -> (string)

The `nextToken` value to include in a future `DescribeImages` request. When the results of a `DescribeImages` request exceed `maxResults` , this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.