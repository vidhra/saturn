# get-image-recipeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image-recipe.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image-recipe.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [imagebuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html#cli-aws-imagebuilder) ]

# get-image-recipe

## Description

Gets an image recipe.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/imagebuilder-2019-12-02/GetImageRecipe)

## Synopsis

```
get-image-recipe
--image-recipe-arn <value>
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

`--image-recipe-arn` (string)

The Amazon Resource Name (ARN) of the image recipe that you want to retrieve.

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

requestId -> (string)

The request ID that uniquely identifies this request.

imageRecipe -> (structure)

The image recipe object.

arn -> (string)

The Amazon Resource Name (ARN) of the image recipe.

type -> (string)

Specifies which type of image is created by the recipe - an AMI or a container image.

name -> (string)

The name of the image recipe.

description -> (string)

The description of the image recipe.

platform -> (string)

The platform of the image recipe.

owner -> (string)

The owner of the image recipe.

version -> (string)

The version of the image recipe.

components -> (list)

The components that are included in the image recipe. Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.

(structure)

Configuration details of the component.

componentArn -> (string)

The Amazon Resource Name (ARN) of the component.

parameters -> (list)

A group of parameter settings that Image Builder uses to configure the component for a specific recipe.

(structure)

Contains a key/value pair that sets the named component parameter.

name -> (string)

The name of the component parameter to set.

value -> (list)

Sets the value for the named component parameter.

(string)

parentImage -> (string)

The base image for customizations specified in the image recipe. You can specify the parent image using one of the following options:

- AMI ID
- Image Builder image Amazon Resource Name (ARN)
- Amazon Web Services Systems Manager (SSM) Parameter Store Parameter, prefixed by `ssm:` , followed by the parameter name or ARN.
- Amazon Web Services Marketplace product ID

blockDeviceMappings -> (list)

The block device mappings to apply when creating images from this recipe.

(structure)

Defines block device mappings for the instance used to configure your image.

deviceName -> (string)

The device to which these mappings apply.

ebs -> (structure)

Use to manage Amazon EBS-specific configuration for this mapping.

encrypted -> (boolean)

Use to configure device encryption.

deleteOnTermination -> (boolean)

Use to configure delete on termination of the associated device.

iops -> (integer)

Use to configure device IOPS.

kmsKeyId -> (string)

Use to configure the KMS key to use when encrypting the device.

snapshotId -> (string)

The snapshot that defines the device contents.

volumeSize -> (integer)

Use to override the deviceâs volume size.

volumeType -> (string)

Use to override the deviceâs volume type.

throughput -> (integer)

**For GP3 volumes only** â The throughput in MiB/s that the volume supports.

virtualName -> (string)

Use to manage instance ephemeral devices.

noDevice -> (string)

Use to remove a mapping from the base image.

dateCreated -> (string)

The date on which this image recipe was created.

tags -> (map)

The tags of the image recipe.

key -> (string)

value -> (string)

workingDirectory -> (string)

The working directory to be used during build and test workflows.

additionalInstanceConfiguration -> (structure)

Before you create a new AMI, Image Builder launches temporary Amazon EC2 instances to build and test your image configuration. Instance configuration adds a layer of control over those instances. You can define settings and add scripts to run when an instance is launched from your AMI.

systemsManagerAgent -> (structure)

Contains settings for the Systems Manager agent on your build instance.

uninstallAfterBuild -> (boolean)

Controls whether the Systems Manager agent is removed from your final build image, prior to creating the new AMI. If this is set to true, then the agent is removed from the final image. If itâs set to false, then the agent is left in, so that it is included in the new AMI. The default value is false.

userDataOverride -> (string)

Use this property to provide commands or a command script to run when you launch your build instance.

The userDataOverride property replaces any commands that Image Builder might have added to ensure that Systems Manager is installed on your Linux build instance. If you override the user data, make sure that you add commands to install Systems Manager, if it is not pre-installed on your base image.

### Note

The user data is always base 64 encoded. For example, the following commands are encoded as `IyEvYmluL2Jhc2gKbWtkaXIgLXAgL3Zhci9iYi8KdG91Y2ggL3Zhci$` :

*#!/bin/bash*

mkdir -p /var/bb/

touch /var