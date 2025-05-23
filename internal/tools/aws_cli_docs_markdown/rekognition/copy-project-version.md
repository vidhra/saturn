# copy-project-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/copy-project-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/copy-project-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# copy-project-version

## Description

### Note

This operation applies only to Amazon Rekognition Custom Labels.

Copies a version of an Amazon Rekognition Custom Labels model from a source project to a destination project. The source and destination projects can be in different AWS accounts but must be in the same AWS Region. You canât copy a model to another AWS service.

To copy a model version to a different AWS account, you need to create a resource-based policy known as a *project policy* . You attach the project policy to the source project by calling  PutProjectPolicy . The project policy gives permission to copy the model version from a trusting AWS account to a trusted account.

For more information creating and attaching a project policy, see Attaching a project policy (SDK) in the *Amazon Rekognition Custom Labels Developer Guide* .

If you are copying a model version to a project in the same AWS account, you donât need to create a project policy.

### Note

Copying project versions is supported only for Custom Labels models.

To copy a model, the destination project, source project, and source model version must already exist.

Copying a model version takes a while to complete. To get the current status, call  DescribeProjectVersions and check the value of `Status` in the  ProjectVersionDescription object. The copy operation has finished when the value of `Status` is `COPYING_COMPLETED` .

This operation requires permissions to perform the `rekognition:CopyProjectVersion` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/CopyProjectVersion)

## Synopsis

```
copy-project-version
--source-project-arn <value>
--source-project-version-arn <value>
--destination-project-arn <value>
--version-name <value>
--output-config <value>
[--tags <value>]
[--kms-key-id <value>]
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

`--source-project-arn` (string)

The ARN of the source project in the trusting AWS account.

`--source-project-version-arn` (string)

The ARN of the model version in the source project that you want to copy to a destination project.

`--destination-project-arn` (string)

The ARN of the project in the trusted AWS account that you want to copy the model version to.

`--version-name` (string)

A name for the version of the model thatâs copied to the destination project.

`--output-config` (structure)

The S3 bucket and folder location where the training output for the source model version is placed.

S3Bucket -> (string)

The S3 bucket where training output is placed.

S3KeyPrefix -> (string)

The prefix applied to the training output files.

Shorthand Syntax:

```
S3Bucket=string,S3KeyPrefix=string
```

JSON Syntax:

```
{
  "S3Bucket": "string",
  "S3KeyPrefix": "string"
}
```

`--tags` (map)

The key-value tags to assign to the model version.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--kms-key-id` (string)

The identifier for your AWS Key Management Service key (AWS KMS key). You can supply the Amazon Resource Name (ARN) of your KMS key, the ID of your KMS key, an alias for your KMS key, or an alias ARN. The key is used to encrypt training results and manifest files written to the output Amazon S3 bucket (`OutputConfig` ).

If you choose to use your own KMS key, you need the following permissions on the KMS key.

- kms:CreateGrant
- kms:DescribeKey
- kms:GenerateDataKey
- kms:Decrypt

If you donât specify a value for `KmsKeyId` , images copied into the service are encrypted using a key that AWS owns and manages.

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

ProjectVersionArn -> (string)

The ARN of the copied model version in the destination project.