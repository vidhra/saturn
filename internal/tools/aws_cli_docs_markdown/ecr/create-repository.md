# create-repositoryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/create-repository.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/create-repository.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html#cli-aws-ecr) ]

# create-repository

## Description

Creates a repository. For more information, see [Amazon ECR repositories](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html) in the *Amazon Elastic Container Registry User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/CreateRepository)

## Synopsis

```
create-repository
[--registry-id <value>]
--repository-name <value>
[--tags <value>]
[--image-tag-mutability <value>]
[--image-scanning-configuration <value>]
[--encryption-configuration <value>]
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

The Amazon Web Services account ID associated with the registry to create the repository. If you do not specify a registry, the default registry is assumed.

`--repository-name` (string)

The name to use for the repository. The repository name may be specified on its own (such as `nginx-web-app` ) or it can be prepended with a namespace to group the repository into a category (such as `project-a/nginx-web-app` ).

The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes.

`--tags` (list)

The metadata that you apply to the repository to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.

(structure)

The metadata to apply to a resource to help you categorize and organize them. Each tag consists of a key and a value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.

Key -> (string)

One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.

Value -> (string)

A `value` acts as a descriptor within a tag category (key).

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--image-tag-mutability` (string)

The tag mutability setting for the repository. If this parameter is omitted, the default setting of `MUTABLE` will be used which will allow image tags to be overwritten. If `IMMUTABLE` is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.

Possible values:

- `MUTABLE`
- `IMMUTABLE`

`--image-scanning-configuration` (structure)

The image scanning configuration for the repository. This determines whether images are scanned for known vulnerabilities after being pushed to the repository.

scanOnPush -> (boolean)

The setting that determines whether images are scanned after being pushed to a repository. If set to `true` , images will be scanned after being pushed. If this parameter is not specified, it will default to `false` and images will not be scanned unless a scan is manually started with the [API_StartImageScan](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_StartImageScan.html) API.

Shorthand Syntax:

```
scanOnPush=boolean
```

JSON Syntax:

```
{
  "scanOnPush": true|false
}
```

`--encryption-configuration` (structure)

The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.

encryptionType -> (string)

The encryption type to use.

If you use the `KMS` encryption type, the contents of the repository will be encrypted using server-side encryption with Key Management Service key stored in KMS. When you use KMS to encrypt your data, you can either use the default Amazon Web Services managed KMS key for Amazon ECR, or specify your own KMS key, which you already created.

If you use the `KMS_DSSE` encryption type, the contents of the repository will be encrypted with two layers of encryption using server-side encryption with the KMS Management Service key stored in KMS. Similar to the `KMS` encryption type, you can either use the default Amazon Web Services managed KMS key for Amazon ECR, or specify your own KMS key, which youâve already created.

If you use the `AES256` encryption type, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts the images in the repository using an AES256 encryption algorithm.

For more information, see [Amazon ECR encryption at rest](https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html) in the *Amazon Elastic Container Registry User Guide* .

kmsKey -> (string)

If you use the `KMS` encryption type, specify the KMS key to use for encryption. The alias, key ID, or full ARN of the KMS key can be specified. The key must exist in the same Region as the repository. If no key is specified, the default Amazon Web Services managed KMS key for Amazon ECR will be used.

Shorthand Syntax:

```
encryptionType=string,kmsKey=string
```

JSON Syntax:

```
{
  "encryptionType": "AES256"|"KMS"|"KMS_DSSE",
  "kmsKey": "string"
}
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

**Example 1: To create a repository**

The following `create-repository` example creates a repository inside the specified namespace in the default registry for an account.

```
aws ecr create-repository \
    --repository-name project-a/sample-repo
```

Output:

```
{
    "repository": {
        "registryId": "123456789012",
        "repositoryName": "project-a/sample-repo",
        "repositoryArn": "arn:aws:ecr:us-west-2:123456789012:repository/project-a/sample-repo"
    }
}
```

For more information, see [Creating a Repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html) in the *Amazon ECR User Guide*.

**Example 2: To create a repository configured with image tag immutability**

The following `create-repository` example creates a repository configured for tag immutability in the default registry for an account.

```
aws ecr create-repository \
    --repository-name project-a/sample-repo \
    --image-tag-mutability IMMUTABLE
```

Output:

```
{
    "repository": {
        "registryId": "123456789012",
        "repositoryName": "project-a/sample-repo",
        "repositoryArn": "arn:aws:ecr:us-west-2:123456789012:repository/project-a/sample-repo",
        "imageTagMutability": "IMMUTABLE"
    }
}
```

For more information, see [Image Tag Mutability](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-tag-mutability.html) in the *Amazon ECR User Guide*.

**Example 3: To create a repository configured with a scanning configuration**

The following `create-repository` example creates a repository configured to perform a vulnerability scan on image push in the default registry for an account.

```
aws ecr create-repository \
    --repository-name project-a/sample-repo \
    --image-scanning-configuration scanOnPush=true
```

Output:

```
{
    "repository": {
        "registryId": "123456789012",
        "repositoryName": "project-a/sample-repo",
        "repositoryArn": "arn:aws:ecr:us-west-2:123456789012:repository/project-a/sample-repo",
        "imageScanningConfiguration": {
            "scanOnPush": true
        }
    }
}
```

For more information, see [Image Scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) in the *Amazon ECR User Guide*.

## Output

repository -> (structure)

The repository that was created.

repositoryArn -> (string)

The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the `arn:aws:ecr` namespace, followed by the region of the repository, Amazon Web Services account ID of the repository owner, repository namespace, and repository name. For example, `arn:aws:ecr:region:012345678910:repository-namespace/repository-name` .

registryId -> (string)

The Amazon Web Services account ID associated with the registry that contains the repository.

repositoryName -> (string)

The name of the repository.

repositoryUri -> (string)

The URI for the repository. You can use this URI for container image `push` and `pull` operations.

createdAt -> (timestamp)

The date and time, in JavaScript date format, when the repository was created.

imageTagMutability -> (string)

The tag mutability setting for the repository.

imageScanningConfiguration -> (structure)

The image scanning configuration for a repository.

scanOnPush -> (boolean)

The setting that determines whether images are scanned after being pushed to a repository. If set to `true` , images will be scanned after being pushed. If this parameter is not specified, it will default to `false` and images will not be scanned unless a scan is manually started with the [API_StartImageScan](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_StartImageScan.html) API.

encryptionConfiguration -> (structure)

The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.

encryptionType -> (string)

The encryption type to use.

If you use the `KMS` encryption type, the contents of the repository will be encrypted using server-side encryption with Key Management Service key stored in KMS. When you use KMS to encrypt your data, you can either use the default Amazon Web Services managed KMS key for Amazon ECR, or specify your own KMS key, which you already created.

If you use the `KMS_DSSE` encryption type, the contents of the repository will be encrypted with two layers of encryption using server-side encryption with the KMS Management Service key stored in KMS. Similar to the `KMS` encryption type, you can either use the default Amazon Web Services managed KMS key for Amazon ECR, or specify your own KMS key, which youâve already created.

If you use the `AES256` encryption type, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts the images in the repository using an AES256 encryption algorithm.

For more information, see [Amazon ECR encryption at rest](https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html) in the *Amazon Elastic Container Registry User Guide* .

kmsKey -> (string)

If you use the `KMS` encryption type, specify the KMS key to use for encryption. The alias, key ID, or full ARN of the KMS key can be specified. The key must exist in the same Region as the repository. If no key is specified, the default Amazon Web Services managed KMS key for Amazon ECR will be used.