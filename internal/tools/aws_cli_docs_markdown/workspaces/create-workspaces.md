# create-workspacesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-workspaces.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-workspaces.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/index.html#cli-aws-workspaces) ]

# create-workspaces

## Description

Creates one or more WorkSpaces.

This operation is asynchronous and returns before the WorkSpaces are created.

### Note

- The `MANUAL` running mode value is only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use this value. For more information, see [Amazon WorkSpaces Core](http://aws.amazon.com/workspaces/core/) .
- You donât need to specify the `PCOIP` protocol for Linux bundles because `DCV` (formerly WSP) is the default protocol for those bundles.
- User-decoupled WorkSpaces are only supported by Amazon WorkSpaces Core.
- Review your running mode to ensure you are using one that is optimal for your needs and budget. For more information on switching running modes, see [Can I switch between hourly and monthly billing?](http://aws.amazon.com/workspaces-family/workspaces/faqs/#:~:text=Can%20I%20switch%20between%20hourly%20and%20monthly%20billing%20on%20WorkSpaces%20Personal%3F)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/CreateWorkspaces)

## Synopsis

```
create-workspaces
--workspaces <value>
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

`--workspaces` (list)

The WorkSpaces to create. You can specify up to 25 WorkSpaces.

(structure)

Describes the information used to create a WorkSpace.

DirectoryId -> (string)

The identifier of the Directory Service directory for the WorkSpace. You can use  DescribeWorkspaceDirectories to list the available directories.

UserName -> (string)

The user name of the user for the WorkSpace. This user name must exist in the Directory Service directory for the WorkSpace.

The username is not case-sensitive, but we recommend matching the case in the Directory Service directory to avoid potential incompatibilities.

The reserved keyword, `[UNDEFINED]` , is used when creating user-decoupled WorkSpaces.

BundleId -> (string)

The identifier of the bundle for the WorkSpace. You can use  DescribeWorkspaceBundles to list the available bundles.

VolumeEncryptionKey -> (string)

The ARN of the symmetric KMS key used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric KMS keys.

UserVolumeEncryptionEnabled -> (boolean)

Indicates whether the data stored on the user volume is encrypted.

RootVolumeEncryptionEnabled -> (boolean)

Indicates whether the data stored on the root volume is encrypted.

WorkspaceProperties -> (structure)

The WorkSpace properties.

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

Tags -> (list)

The tags for the WorkSpace.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.

WorkspaceName -> (string)

The name of the user-decoupled WorkSpace.

### Note

`WorkspaceName` is required if `UserName` is `[UNDEFINED]` for user-decoupled WorkSpaces. `WorkspaceName` is not applicable if `UserName` is specified for user-assigned WorkSpaces.

Shorthand Syntax:

```
DirectoryId=string,UserName=string,BundleId=string,VolumeEncryptionKey=string,UserVolumeEncryptionEnabled=boolean,RootVolumeEncryptionEnabled=boolean,WorkspaceProperties={RunningMode=string,RunningModeAutoStopTimeoutInMinutes=integer,RootVolumeSizeGib=integer,UserVolumeSizeGib=integer,ComputeTypeName=string,Protocols=[string,string],OperatingSystemName=string,GlobalAccelerator={Mode=string,PreferredProtocol=string}},Tags=[{Key=string,Value=string},{Key=string,Value=string}],WorkspaceName=string ...
```

JSON Syntax:

```
[
  {
    "DirectoryId": "string",
    "UserName": "string",
    "BundleId": "string",
    "VolumeEncryptionKey": "string",
    "UserVolumeEncryptionEnabled": true|false,
    "RootVolumeEncryptionEnabled": true|false,
    "WorkspaceProperties": {
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
    },
    "Tags": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ],
    "WorkspaceName": "string"
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

**Example 1: To create an AlwaysOn WorkSpace**

The following `create-workspaces` example creates an AlwaysOn WorkSpace for the specified user, using the specified directory and bundle.

```
aws workspaces create-workspaces \
    --workspaces DirectoryId=d-926722edaf,UserName=Mateo,BundleId=wsb-0zsvgp8fc
```

Output:

```
{
    "FailedRequests": [],
    "PendingRequests": [
        {
            "WorkspaceId": "ws-kcqms853t",
            "DirectoryId": "d-926722edaf",
            "UserName": "Mateo",
            "State": "PENDING",
            "BundleId": "wsb-0zsvgp8fc"
        }
    ]
}
```

**Example 2: To create an AutoStop WorkSpace**

The following `create-workspaces` example creates an AutoStop WorkSpace for the specified user, using the specified directory and bundle.

```
aws workspaces create-workspaces \
    --workspaces DirectoryId=d-926722edaf,UserName=Mary,BundleId=wsb-0zsvgp8fc,WorkspaceProperties={RunningMode=AUTO_STOP}
```

Output:

```
{
    "FailedRequests": [],
    "PendingRequests": [
        {
            "WorkspaceId": "ws-dk1xzr417",
            "DirectoryId": "d-926722edaf",
            "UserName": "Mary",
            "State": "PENDING",
            "BundleId": "wsb-0zsvgp8fc"
        }
    ]
}
```

**Example 3: To create a user-decoupled WorkSpace**

The following `create-workspaces` example creates a user-decoupled WorkSpace by setting the username to `[UNDEFINED]`, and specifying a WorkSpace name, directory ID, and bundle ID.

```
aws workspaces create-workspaces \
    --workspaces DirectoryId=d-926722edaf,UserName='"[UNDEFINED]"',WorkspaceName=MaryWorkspace1,BundleId=wsb-0zsvgp8fc,WorkspaceProperties={RunningMode=ALWAYS_ON}
```

Output:

```
{
    "FailedRequests": [],
    "PendingRequests": [
        {
            "WorkspaceId": "ws-abcd1234",
            "DirectoryId": "d-926722edaf",
            "UserName": "[UNDEFINED]",
            "State": "PENDING",
            "BundleId": "wsb-0zsvgp8fc",
            "WorkspaceName": "MaryWorkspace1"
        }
    ]
}
```

For more information, see [Launch a virtual desktop](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspaces-tutorials.html) in the *Amazon WorkSpaces Administration Guide*.

## Output

FailedRequests -> (list)

Information about the WorkSpaces that could not be created.

(structure)

Describes a WorkSpace that cannot be created.

WorkspaceRequest -> (structure)

Information about the WorkSpace.

DirectoryId -> (string)

The identifier of the Directory Service directory for the WorkSpace. You can use  DescribeWorkspaceDirectories to list the available directories.

UserName -> (string)

The user name of the user for the WorkSpace. This user name must exist in the Directory Service directory for the WorkSpace.

The username is not case-sensitive, but we recommend matching the case in the Directory Service directory to avoid potential incompatibilities.

The reserved keyword, `[UNDEFINED]` , is used when creating user-decoupled WorkSpaces.

BundleId -> (string)

The identifier of the bundle for the WorkSpace. You can use  DescribeWorkspaceBundles to list the available bundles.

VolumeEncryptionKey -> (string)

The ARN of the symmetric KMS key used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric KMS keys.

UserVolumeEncryptionEnabled -> (boolean)

Indicates whether the data stored on the user volume is encrypted.

RootVolumeEncryptionEnabled -> (boolean)

Indicates whether the data stored on the root volume is encrypted.

WorkspaceProperties -> (structure)

The WorkSpace properties.

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

Tags -> (list)

The tags for the WorkSpace.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.

WorkspaceName -> (string)

The name of the user-decoupled WorkSpace.

### Note

`WorkspaceName` is required if `UserName` is `[UNDEFINED]` for user-decoupled WorkSpaces. `WorkspaceName` is not applicable if `UserName` is specified for user-assigned WorkSpaces.

ErrorCode -> (string)

The error code that is returned if the WorkSpace cannot be created.

ErrorMessage -> (string)

The text of the error message that is returned if the WorkSpace cannot be created.

PendingRequests -> (list)

Information about the WorkSpaces that were created.

Because this operation is asynchronous, the identifier returned is not immediately available for use with other operations. For example, if you call  DescribeWorkspaces before the WorkSpace is created, the information returned can be incomplete.

(structure)

Describes a WorkSpace.

WorkspaceId -> (string)

The identifier of the WorkSpace.

DirectoryId -> (string)

The identifier of the Directory Service directory for the WorkSpace.

UserName -> (string)

The user for the WorkSpace.

IpAddress -> (string)

The IP address of the WorkSpace.

State -> (string)

The operational state of the WorkSpace.

- `PENDING` â The WorkSpace is in a waiting state (for example, the WorkSpace is being created).
- `AVAILABLE` â The WorkSpace is running and has passed the health checks.
- `IMPAIRED` â Refer to `UNHEALTHY` state.
- `UNHEALTHY` â The WorkSpace is not responding to health checks.
- `REBOOTING` â The WorkSpace is being rebooted (restarted).
- `STARTING` â The WorkSpace is starting up and health checks are being run.
- `REBUILDING` â The WorkSpace is being rebuilt.
- `RESTORING` â The WorkSpace is being restored.
- `MAINTENANCE` â The WorkSpace is undergoing scheduled maintenance by Amazon Web Services.
- `ADMIN_MAINTENANCE` â The WorkSpace is undergoing maintenance by the WorkSpaces administrator.
- `TERMINATING` â The WorkSpace is being deleted.
- `TERMINATED` â The WorkSpace has been deleted.
- `SUSPENDED` â The WorkSpace has been suspended for image creation.
- `UPDATING` â The WorkSpace is undergoing an update.
- `STOPPING` â The WorkSpace is being stopped.
- `STOPPED` â The WorkSpace has been stopped.
- `ERROR` â The WorkSpace is an error state (for example, an error occurred during startup).

### Note

After a WorkSpace is terminated, the `TERMINATED` state is returned only briefly before the WorkSpace directory metadata is cleaned up, so this state is rarely returned. To confirm that a WorkSpace is terminated, check for the WorkSpace ID by using [DescribeWorkSpaces](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaces.html) . If the WorkSpace ID isnât returned, then the WorkSpace has been successfully terminated.

BundleId -> (string)

The identifier of the bundle used to create the WorkSpace.

SubnetId -> (string)

The identifier of the subnet for the WorkSpace.

ErrorMessage -> (string)

The text of the error message that is returned if the WorkSpace cannot be created.

ErrorCode -> (string)

The error code that is returned if the WorkSpace cannot be created.

ComputerName -> (string)

The name of the WorkSpace, as seen by the operating system. The format of this name varies. For more information, see [Launch a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspaces-tutorials.html) .

VolumeEncryptionKey -> (string)

The ARN of the symmetric KMS key used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric KMS keys.

UserVolumeEncryptionEnabled -> (boolean)

Indicates whether the data stored on the user volume is encrypted.

RootVolumeEncryptionEnabled -> (boolean)

Indicates whether the data stored on the root volume is encrypted.

WorkspaceName -> (string)

The name of the user-decoupled WorkSpace.

WorkspaceProperties -> (structure)

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

ModificationStates -> (list)

The modification states of the WorkSpace.

(structure)

Describes a WorkSpace modification.

Resource -> (string)

The resource.

State -> (string)

The modification state.

RelatedWorkspaces -> (list)

The standby WorkSpace or primary WorkSpace related to the specified WorkSpace.

(structure)

Describes the related WorkSpace. The related WorkSpace could be a standby WorkSpace or primary WorkSpace related to the specified WorkSpace.

WorkspaceId -> (string)

The identifier of the related WorkSpace.

Region -> (string)

The Region of the related WorkSpace.

State -> (string)

Indicates the state of the WorkSpace.

Type -> (string)

Indicates the type of WorkSpace.

DataReplicationSettings -> (structure)

Indicates the settings of the data replication.

DataReplication -> (string)

Indicates whether data replication is enabled, and if enabled, the type of data replication.

RecoverySnapshotTime -> (timestamp)

The date and time at which the last successful snapshot was taken of the primary WorkSpace used for replicating data.

StandbyWorkspacesProperties -> (list)

The properties of the standby WorkSpace

(structure)

Describes the properties of the related standby WorkSpaces.

StandbyWorkspaceId -> (string)

The identifier of the standby WorkSpace

DataReplication -> (string)

Indicates whether data replication is enabled, and if enabled, the type of data replication.

RecoverySnapshotTime -> (timestamp)

The date and time at which the last successful snapshot was taken of the primary WorkSpace used for replicating data.