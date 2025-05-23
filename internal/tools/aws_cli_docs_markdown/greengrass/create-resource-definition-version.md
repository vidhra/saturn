# create-resource-definition-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-resource-definition-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-resource-definition-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [greengrass](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/index.html#cli-aws-greengrass) ]

# create-resource-definition-version

## Description

Creates a version of a resource definition that has already been defined.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateResourceDefinitionVersion)

## Synopsis

```
create-resource-definition-version
[--amzn-client-token <value>]
--resource-definition-id <value>
[--resources <value>]
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

`--amzn-client-token` (string)
A client token used to correlate requests and responses.

`--resource-definition-id` (string)
The ID of the resource definition.

`--resources` (list)
A list of resources.(structure)

Information about a resource.

Id -> (string)

The resource ID, used to refer to a resource in the Lambda function configuration. Max length is 128 characters with pattern ââ[a-zA-Z0-9:_-]+ââ. This must be unique within a Greengrass group.

Name -> (string)

The descriptive resource name, which is displayed on the AWS IoT Greengrass console. Max length 128 characters with pattern ââ[a-zA-Z0-9:_-]+ââ. This must be unique within a Greengrass group.

ResourceDataContainer -> (structure)

A container of data for all resource types.

LocalDeviceResourceData -> (structure)

Attributes that define the local device resource.

GroupOwnerSetting -> (structure)

Group/owner related settings for local resources.

AutoAddGroupOwner -> (boolean)

If true, AWS IoT Greengrass automatically adds the specified Linux OS group owner of the resource to the Lambda process privileges. Thus the Lambda process will have the file access permissions of the added Linux group.

GroupOwner -> (string)

The name of the Linux OS group whose privileges will be added to the Lambda process. This field is optional.

SourcePath -> (string)

The local absolute path of the device resource. The source path for a device resource can refer only to a character device or block device under ââ/devââ.

LocalVolumeResourceData -> (structure)

Attributes that define the local volume resource.

DestinationPath -> (string)

The absolute local path of the resource inside the Lambda environment.

GroupOwnerSetting -> (structure)

Allows you to configure additional group privileges for the Lambda process. This field is optional.

AutoAddGroupOwner -> (boolean)

If true, AWS IoT Greengrass automatically adds the specified Linux OS group owner of the resource to the Lambda process privileges. Thus the Lambda process will have the file access permissions of the added Linux group.

GroupOwner -> (string)

The name of the Linux OS group whose privileges will be added to the Lambda process. This field is optional.

SourcePath -> (string)

The local absolute path of the volume resource on the host. The source path for a volume resource type cannot start with ââ/sysââ.

S3MachineLearningModelResourceData -> (structure)

Attributes that define an Amazon S3 machine learning resource.

DestinationPath -> (string)

The absolute local path of the resource inside the Lambda environment.

OwnerSetting -> (structure)

The owner setting for downloaded machine learning resources.

GroupOwner -> (string)

The group owner of the resource. This is the name of an existing Linux OS group on the system or a GID. The groupâs permissions are added to the Lambda process.

GroupPermission -> (string)

The permissions that the group owner has to the resource. Valid values are âârwââ (read/write) or ââroââ (read-only).

S3Uri -> (string)

The URI of the source model in an S3 bucket. The model package must be in tar.gz or .zip format.

SageMakerMachineLearningModelResourceData -> (structure)

Attributes that define an Amazon SageMaker machine learning resource.

DestinationPath -> (string)

The absolute local path of the resource inside the Lambda environment.

OwnerSetting -> (structure)

The owner setting for downloaded machine learning resources.

GroupOwner -> (string)

The group owner of the resource. This is the name of an existing Linux OS group on the system or a GID. The groupâs permissions are added to the Lambda process.

GroupPermission -> (string)

The permissions that the group owner has to the resource. Valid values are âârwââ (read/write) or ââroââ (read-only).

SageMakerJobArn -> (string)

The ARN of the Amazon SageMaker training job that represents the source model.

SecretsManagerSecretResourceData -> (structure)

Attributes that define a secret resource, which references a secret from AWS Secrets Manager.

ARN -> (string)

The ARN of the Secrets Manager secret to make available on the core. The value of the secretâs latest version (represented by the ââAWSCURRENTââ staging label) is included by default.

AdditionalStagingLabelsToDownload -> (list)

Optional. The staging labels whose values you want to make available on the core, in addition to ââAWSCURRENTââ.

(string)

JSON Syntax:

```
[
  {
    "Id": "string",
    "Name": "string",
    "ResourceDataContainer": {
      "LocalDeviceResourceData": {
        "GroupOwnerSetting": {
          "AutoAddGroupOwner": true|false,
          "GroupOwner": "string"
        },
        "SourcePath": "string"
      },
      "LocalVolumeResourceData": {
        "DestinationPath": "string",
        "GroupOwnerSetting": {
          "AutoAddGroupOwner": true|false,
          "GroupOwner": "string"
        },
        "SourcePath": "string"
      },
      "S3MachineLearningModelResourceData": {
        "DestinationPath": "string",
        "OwnerSetting": {
          "GroupOwner": "string",
          "GroupPermission": "ro"|"rw"
        },
        "S3Uri": "string"
      },
      "SageMakerMachineLearningModelResourceData": {
        "DestinationPath": "string",
        "OwnerSetting": {
          "GroupOwner": "string",
          "GroupPermission": "ro"|"rw"
        },
        "SageMakerJobArn": "string"
      },
      "SecretsManagerSecretResourceData": {
        "ARN": "string",
        "AdditionalStagingLabelsToDownload": ["string", ...]
      }
    }
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

**To create a version of a resource definition**

The following `create-resource-definition-version` example creates a new version of a TwilioAuthToken.

```
aws greengrass create-resource-definition-version \
    --resource-definition-id "c8bb9ebc-c3fd-40a4-9c6a-568d75569d38" \
    --resources "[{\"Id\": \"TwilioAuthToken\",\"Name\": \"MyTwilioAuthToken\",\"ResourceDataContainer\": {\"SecretsManagerSecretResourceData\": {\"ARN\": \"arn:aws:secretsmanager:us-west-2:123456789012:secret:greengrass-TwilioAuthToken-ntSlp6\"}}}]"
```

Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/resources/c8bb9ebc-c3fd-40a4-9c6a-568d75569d38/versions/b3bcada0-5fb6-42df-bf0b-1ee4f15e769e",
    "CreationTimestamp": "2019-06-24T21:17:25.623Z",
    "Id": "c8bb9ebc-c3fd-40a4-9c6a-568d75569d38",
    "Version": "b3bcada0-5fb6-42df-bf0b-1ee4f15e769e"
}
```

## Output

Arn -> (string)

The ARN of the version.

CreationTimestamp -> (string)

The time, in milliseconds since the epoch, when the version was created.

Id -> (string)

The ID of the parent definition that the version is associated with.

Version -> (string)

The ID of the version.