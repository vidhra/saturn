# modify-workspace-propertiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/modify-workspace-properties.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/modify-workspace-properties.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/index.html#cli-aws-workspaces) ]

# modify-workspace-properties

## Description

Modifies the specified WorkSpace properties. For important information about how to modify the size of the root and user volumes, see [Modify a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html) .

### Note

The `MANUAL` running mode value is only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use this value. For more information, see [Amazon WorkSpaces Core](http://aws.amazon.com/workspaces/core/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/ModifyWorkspaceProperties)

## Synopsis

```
modify-workspace-properties
--workspace-id <value>
[--workspace-properties <value>]
[--data-replication <value>]
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

`--workspace-id` (string)

The identifier of the WorkSpace.

`--workspace-properties` (structure)

The properties of the WorkSpace.

RunningMode -> (string)

The running mode. For more information, see [Manage the WorkSpace Running Mode](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html) .

### Note

The `MANUAL` value is only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use this value. For more information, see [Amazon WorkSpaces Core](http://aws.amazon.com/workspaces/core/) .

Review your running mode to ensure you are using one that is optimal for your needs and budget. For more information on switching running modes, see [Can I switch between hourly and monthly billing?](http://aws.amazon.com/workspaces-family/workspaces/faqs/#:~:text=Can%20I%20switch%20between%20hourly%20and%20monthly%20billing%20on%20WorkSpaces%20Personal%3F)

RunningModeAutoStopTimeoutInMinutes -> (integer)

The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.

RootVolumeSizeGib -> (integer)

The size of the root volume. For important information about how to modify the size of the root and user volumes, see [Modify a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html) .

UserVolumeSizeGib -> (integer)

The size of the user storage. For important information about how to modify the size of the root and user volumes, see [Modify a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html) .

ComputeTypeName -> (string)

The compute type. For more information, see [Amazon WorkSpaces Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles) .

Protocols -> (list)

The protocol. For more information, see [Protocols for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-protocols.html) .

### Note

- Only available for WorkSpaces created with PCoIP bundles.
- The `Protocols` property is case sensitive. Ensure you use `PCOIP` or `DCV` (formerly WSP).
- Unavailable for Windows 7 WorkSpaces and WorkSpaces using GPU-based bundles (Graphics, GraphicsPro, Graphics.g4dn, and GraphicsPro.g4dn).

(string)

OperatingSystemName -> (string)

The name of the operating system.

GlobalAccelerator -> (structure)

Indicates the Global Accelerator properties.

Mode -> (string)

Indicates if Global Accelerator for WorkSpaces is enabled, disabled, or the same mode as the associated directory.

PreferredProtocol -> (string)

Indicates the preferred protocol for Global Accelerator.

Shorthand Syntax:

```
RunningMode=string,RunningModeAutoStopTimeoutInMinutes=integer,RootVolumeSizeGib=integer,UserVolumeSizeGib=integer,ComputeTypeName=string,Protocols=string,string,OperatingSystemName=string,GlobalAccelerator={Mode=string,PreferredProtocol=string}
```

JSON Syntax:

```
{
  "RunningMode": "AUTO_STOP"|"ALWAYS_ON"|"MANUAL",
  "RunningModeAutoStopTimeoutInMinutes": integer,
  "RootVolumeSizeGib": integer,
  "UserVolumeSizeGib": integer,
  "ComputeTypeName": "VALUE"|"STANDARD"|"PERFORMANCE"|"POWER"|"GRAPHICS"|"POWERPRO"|"GENERALPURPOSE_4XLARGE"|"GENERALPURPOSE_8XLARGE"|"GRAPHICSPRO"|"GRAPHICS_G4DN"|"GRAPHICSPRO_G4DN",
  "Protocols": ["PCOIP"|"WSP", ...],
  "OperatingSystemName": "AMAZON_LINUX_2"|"UBUNTU_18_04"|"UBUNTU_20_04"|"UBUNTU_22_04"|"UNKNOWN"|"WINDOWS_10"|"WINDOWS_11"|"WINDOWS_7"|"WINDOWS_SERVER_2016"|"WINDOWS_SERVER_2019"|"WINDOWS_SERVER_2022"|"RHEL_8"|"ROCKY_8",
  "GlobalAccelerator": {
    "Mode": "ENABLED_AUTO"|"DISABLED"|"INHERITED",
    "PreferredProtocol": "TCP"|"NONE"|"INHERITED"
  }
}
```

`--data-replication` (string)

Indicates the data replication status.

Possible values:

- `NO_REPLICATION`
- `PRIMARY_AS_SOURCE`

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

**To modify the running mode of a WorkSpace**

The following `modify-workspace-properties` example sets the running mode of the specified WorkSpace to `AUTO_STOP`.

```
aws workspaces modify-workspace-properties \
    --workspace-id ws-dk1xzr417 \
    --workspace-properties RunningMode=AUTO_STOP
```

This command produces no output.

For more information, see [Modify a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html) in the *Amazon WorkSpaces Administration Guide*.

## Output

None