# publish-layer-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-layer-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-layer-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lambda](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/index.html#cli-aws-lambda) ]

# publish-layer-version

## Description

Creates an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) from a ZIP archive. Each time you call `PublishLayerVersion` with the same layer name, a new version is created.

Add layers to your function with  CreateFunction or  UpdateFunctionConfiguration .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/PublishLayerVersion)

## Synopsis

```
publish-layer-version
--layer-name <value>
[--description <value>]
[--content <value>]
[--compatible-runtimes <value>]
[--license-info <value>]
[--compatible-architectures <value>]
[--zip-file <value>]
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

`--layer-name` (string)

The name or Amazon Resource Name (ARN) of the layer.

`--description` (string)

The description of the version.

`--content` (structure)

The function layer archive.

S3Bucket -> (string)

The Amazon S3 bucket of the layer archive.

S3Key -> (string)

The Amazon S3 key of the layer archive.

S3ObjectVersion -> (string)

For versioned objects, the version of the layer archive object to use.

Shorthand Syntax:

```
S3Bucket=string,S3Key=string,S3ObjectVersion=string
```

JSON Syntax:

```
{
  "S3Bucket": "string",
  "S3Key": "string",
  "S3ObjectVersion": "string"
}
```

`--compatible-runtimes` (list)

A list of compatible [function runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) . Used for filtering with  ListLayers and  ListLayerVersions .

The following list includes deprecated runtimes. For more information, see [Runtime deprecation policy](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy) .

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  nodejs
  nodejs4.3
  nodejs6.10
  nodejs8.10
  nodejs10.x
  nodejs12.x
  nodejs14.x
  nodejs16.x
  java8
  java8.al2
  java11
  python2.7
  python3.6
  python3.7
  python3.8
  python3.9
  dotnetcore1.0
  dotnetcore2.0
  dotnetcore2.1
  dotnetcore3.1
  dotnet6
  dotnet8
  nodejs4.3-edge
  go1.x
  ruby2.5
  ruby2.7
  provided
  provided.al2
  nodejs18.x
  python3.10
  java17
  ruby3.2
  ruby3.3
  ruby3.4
  python3.11
  nodejs20.x
  provided.al2023
  python3.12
  java21
  python3.13
  nodejs22.x
```

`--license-info` (string)

The layerâs software license. It can be any of the following:

- An [SPDX license identifier](https://spdx.org/licenses/) . For example, `MIT` .
- The URL of a license hosted on the internet. For example, `https://opensource.org/licenses/MIT` .
- The full text of the license.

`--compatible-architectures` (list)

A list of compatible [instruction set architectures](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html) .

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  x86_64
  arm64
```

`--zip-file` (blob)

The path to the zip file of the content you are uploading. Specify âzip-file or âcontent, but not both. Example: fileb://content.zip

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

**To create a Lambda layer version**

The following `publish-layer-version` example creates a new Python library layer version. The command retrieves the layer content a file named `layer.zip` in the specified S3 bucket.

```
aws lambda publish-layer-version \
    --layer-name my-layer \
    --description "My Python layer" \
    --license-info "MIT" \
    --content S3Bucket=lambda-layers-us-west-2-123456789012,S3Key=layer.zip \
    --compatible-runtimes python3.10 python3.11
```

Output:

```
{
    "Content": {
        "Location": "https://awslambda-us-west-2-layers.s3.us-west-2.amazonaws.com/snapshots/123456789012/my-layer-4aaa2fbb-ff77-4b0a-ad92-5b78a716a96a?versionId=27iWyA73cCAYqyH...",
        "CodeSha256": "tv9jJO+rPbXUUXuRKi7CwHzKtLDkDRJLB3cC3Z/ouXo=",
        "CodeSize": 169
    },
    "LayerArn": "arn:aws:lambda:us-west-2:123456789012:layer:my-layer",
    "LayerVersionArn": "arn:aws:lambda:us-west-2:123456789012:layer:my-layer:1",
    "Description": "My Python layer",
    "CreatedDate": "2023-11-14T23:03:52.894+0000",
    "Version": 1,
    "LicenseInfo": "MIT",
    "CompatibleRuntimes": [
        "python3.10",
        "python3.11"
    ]
}
```

For more information, see [AWS Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) in the *AWS Lambda Developer Guide*.

## Output

Content -> (structure)

Details about the layer version.

Location -> (string)

A link to the layer archive in Amazon S3 that is valid for 10 minutes.

CodeSha256 -> (string)

The SHA-256 hash of the layer archive.

CodeSize -> (long)

The size of the layer archive in bytes.

SigningProfileVersionArn -> (string)

The Amazon Resource Name (ARN) for a signing profile version.

SigningJobArn -> (string)

The Amazon Resource Name (ARN) of a signing job.

LayerArn -> (string)

The ARN of the layer.

LayerVersionArn -> (string)

The ARN of the layer version.

Description -> (string)

The description of the version.

CreatedDate -> (string)

The date that the layer version was created, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).

Version -> (long)

The version number.

CompatibleRuntimes -> (list)

The layerâs compatible runtimes.

The following list includes deprecated runtimes. For more information, see [Runtime use after deprecation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels) .

For a list of all currently supported runtimes, see [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported) .

(string)

LicenseInfo -> (string)

The layerâs software license.

CompatibleArchitectures -> (list)

A list of compatible [instruction set architectures](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html) .

(string)