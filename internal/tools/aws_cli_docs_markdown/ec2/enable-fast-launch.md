# enable-fast-launchÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-fast-launch.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-fast-launch.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# enable-fast-launch

## Description

When you enable Windows fast launch for a Windows AMI, images are pre-provisioned, using snapshots to launch instances up to 65% faster. To create the optimized Windows image, Amazon EC2 launches an instance and runs through Sysprep steps, rebooting as required. Then it creates a set of reserved snapshots that are used for subsequent launches. The reserved snapshots are automatically replenished as they are used, depending on your settings for launch frequency.

### Note

You can only change these settings for Windows AMIs that you own or that have been shared with you.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/EnableFastLaunch)

## Synopsis

```
enable-fast-launch
--image-id <value>
[--resource-type <value>]
[--snapshot-configuration <value>]
[--launch-template <value>]
[--max-parallel-launches <value>]
[--dry-run | --no-dry-run]
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

`--image-id` (string)

Specify the ID of the image for which to enable Windows fast launch.

`--resource-type` (string)

The type of resource to use for pre-provisioning the AMI for Windows fast launch. Supported values include: `snapshot` , which is the default value.

`--snapshot-configuration` (structure)

Configuration settings for creating and managing the snapshots that are used for pre-provisioning the AMI for Windows fast launch. The associated `ResourceType` must be `snapshot` .

TargetResourceCount -> (integer)

The number of pre-provisioned snapshots to keep on hand for a Windows fast launch enabled AMI.

Shorthand Syntax:

```
TargetResourceCount=integer
```

JSON Syntax:

```
{
  "TargetResourceCount": integer
}
```

`--launch-template` (structure)

The launch template to use when launching Windows instances from pre-provisioned snapshots. Launch template parameters can include either the name or ID of the launch template, but not both.

LaunchTemplateId -> (string)

Specify the ID of the launch template that the AMI should use for Windows fast launch.

LaunchTemplateName -> (string)

Specify the name of the launch template that the AMI should use for Windows fast launch.

Version -> (string)

Specify the version of the launch template that the AMI should use for Windows fast launch.

Shorthand Syntax:

```
LaunchTemplateId=string,LaunchTemplateName=string,Version=string
```

JSON Syntax:

```
{
  "LaunchTemplateId": "string",
  "LaunchTemplateName": "string",
  "Version": "string"
}
```

`--max-parallel-launches` (integer)

The maximum number of instances that Amazon EC2 can launch at the same time to create pre-provisioned snapshots for Windows fast launch. Value must be `6` or greater.

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

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

**To start fast launching for an image**

The following `enable-fast-launch` example configures the specified AMI for Fast Launch and sets the maximum number of parallel instances to launch to 6. The type of resource to use to pre-provision the AMI is set to `snapshot`, which is also the default value.

```
aws ec2 enable-fast-launch \
    --image-id ami-01234567890abcedf \
    --max-parallel-launches 6 \
    --resource-type snapshot
```

Output:

```
{
    "ImageId": "ami-01234567890abcedf",
    "ResourceType": "snapshot",
    "SnapshotConfiguration": {
        "TargetResourceCount": 10
    },
    "LaunchTemplate": {},
    "MaxParallelLaunches": 6,
    "OwnerId": "0123456789123",
    "State": "enabling",
    "StateTransitionReason": "Client.UserInitiated",
    "StateTransitionTime": "2022-01-27T22:16:03.199000+00:00"
}
```

For more information, see [Configure EC2 Fast Launch settings for your Windows AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-fast-launch-configure.html) in the *Amazon EC2 User Guide*.

## Output

ImageId -> (string)

The image ID that identifies the AMI for which Windows fast launch was enabled.

ResourceType -> (string)

The type of resource that was defined for pre-provisioning the AMI for Windows fast launch.

SnapshotConfiguration -> (structure)

Settings to create and manage the pre-provisioned snapshots that Amazon EC2 uses for faster launches from the Windows AMI. This property is returned when the associated `resourceType` is `snapshot` .

TargetResourceCount -> (integer)

The number of pre-provisioned snapshots requested to keep on hand for a Windows fast launch enabled AMI.

LaunchTemplate -> (structure)

The launch template that is used when launching Windows instances from pre-provisioned snapshots.

LaunchTemplateId -> (string)

The ID of the launch template that the AMI uses for Windows fast launch.

LaunchTemplateName -> (string)

The name of the launch template that the AMI uses for Windows fast launch.

Version -> (string)

The version of the launch template that the AMI uses for Windows fast launch.

MaxParallelLaunches -> (integer)

The maximum number of instances that Amazon EC2 can launch at the same time to create pre-provisioned snapshots for Windows fast launch.

OwnerId -> (string)

The owner ID for the AMI for which Windows fast launch was enabled.

State -> (string)

The current state of Windows fast launch for the specified AMI.

StateTransitionReason -> (string)

The reason that the state changed for Windows fast launch for the AMI.

StateTransitionTime -> (timestamp)

The time that the state changed for Windows fast launch for the AMI.