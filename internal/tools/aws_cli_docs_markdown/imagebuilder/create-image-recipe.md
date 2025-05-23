# create-image-recipeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image-recipe.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image-recipe.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [imagebuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html#cli-aws-imagebuilder) ]

# create-image-recipe

## Description

Creates a new image recipe. Image recipes define how images are configured, tested, and assessed.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/imagebuilder-2019-12-02/CreateImageRecipe)

## Synopsis

```
create-image-recipe
--name <value>
[--description <value>]
--semantic-version <value>
--components <value>
--parent-image <value>
[--block-device-mappings <value>]
[--tags <value>]
[--working-directory <value>]
[--additional-instance-configuration <value>]
[--client-token <value>]
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

`--name` (string)

The name of the image recipe.

`--description` (string)

The description of the image recipe.

`--semantic-version` (string)

The semantic version of the image recipe. This version follows the semantic version syntax.

### Note

The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.

**Assignment:** For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.

**Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.

`--components` (list)

The components included in the image recipe.

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

JSON Syntax:

```
[
  {
    "componentArn": "string",
    "parameters": [
      {
        "name": "string",
        "value": ["string", ...]
      }
      ...
    ]
  }
  ...
]
```

`--parent-image` (string)

The base image for customizations specified in the image recipe. You can specify the parent image using one of the following options:

- AMI ID
- Image Builder image Amazon Resource Name (ARN)
- Amazon Web Services Systems Manager (SSM) Parameter Store Parameter, prefixed by `ssm:` , followed by the parameter name or ARN.
- Amazon Web Services Marketplace product ID

If you enter an AMI ID or an SSM parameter that contains the AMI ID, you must have access to the AMI, and the AMI must be in the source Region.

`--block-device-mappings` (list)

The block device mappings of the image recipe.

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

Shorthand Syntax:

```
deviceName=string,ebs={encrypted=boolean,deleteOnTermination=boolean,iops=integer,kmsKeyId=string,snapshotId=string,volumeSize=integer,volumeType=string,throughput=integer},virtualName=string,noDevice=string ...
```

JSON Syntax:

```
[
  {
    "deviceName": "string",
    "ebs": {
      "encrypted": true|false,
      "deleteOnTermination": true|false,
      "iops": integer,
      "kmsKeyId": "string",
      "snapshotId": "string",
      "volumeSize": integer,
      "volumeType": "standard"|"io1"|"io2"|"gp2"|"gp3"|"sc1"|"st1",
      "throughput": integer
    },
    "virtualName": "string",
    "noDevice": "string"
  }
  ...
]
```

`--tags` (map)

The tags of the image recipe.

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

`--working-directory` (string)

The working directory used during build and test workflows.

`--additional-instance-configuration` (structure)

Specify additional settings and launch scripts for your build instances.

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

Shorthand Syntax:

```
systemsManagerAgent={uninstallAfterBuild=boolean},userDataOverride=string
```

JSON Syntax:

```
{
  "systemsManagerAgent": {
    "uninstallAfterBuild": true|false
  },
  "userDataOverride": "string"
}
```

`--client-token` (string)

Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference* .

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

**To create a recipe**

The following `create-image-recipe` example creates an image recipe using a JSON file. Components are installed in the order in which they are specified.

```
aws imagebuilder create-image-recipe \
    --cli-input-json file://create-image-recipe.json
```

Contents of `create-image-recipe.json`:

```
{
    "name": "MyBasicRecipe",
    "description": "This example image recipe creates a Windows 2016 image.",
    "semanticVersion": "2019.12.03",
    "components":
    [
        {
            "componentArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/myexamplecomponent/2019.12.02/1"
        },
        {
            "componentArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/myimportedcomponent/1.0.0/1"
        }
    ],
    "parentImage": "arn:aws:imagebuilder:us-west-2:aws:image/windows-server-2016-english-full-base-x86/xxxx.x.x"
}
```

Output:

```
{
    "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/mybasicrecipe/2019.12.03"
}
```

For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html) in the *EC2 Image Builder Users Guide*.

## Output

requestId -> (string)

The request ID that uniquely identifies this request.

clientToken -> (string)

The client token that uniquely identifies the request.

imageRecipeArn -> (string)

The Amazon Resource Name (ARN) of the image recipe that was created by this request.