# describe-workspacesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspaces.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspaces.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/index.html#cli-aws-workspaces) ]

# describe-workspaces

## Description

Describes the specified WorkSpaces.

You can filter the results by using the bundle identifier, directory identifier, or owner, but you can specify only one filter at a time.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaces)

`describe-workspaces` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Workspaces`

## Synopsis

```
describe-workspaces
[--workspace-ids <value>]
[--directory-id <value>]
[--user-name <value>]
[--bundle-id <value>]
[--workspace-name <value>]
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

`--workspace-ids` (list)

The identifiers of the WorkSpaces. You cannot combine this parameter with any other filter.

Because the  CreateWorkspaces operation is asynchronous, the identifier it returns is not immediately available. If you immediately call  DescribeWorkspaces with this identifier, no information is returned.

(string)

Syntax:

```
"string" "string" ...
```

`--directory-id` (string)

The identifier of the directory. In addition, you can optionally specify a specific directory user (see `UserName` ). You cannot combine this parameter with any other filter.

`--user-name` (string)

The name of the directory user. You must specify this parameter with `DirectoryId` .

`--bundle-id` (string)

The identifier of the bundle. All WorkSpaces that are created from this bundle are retrieved. You cannot combine this parameter with any other filter.

`--workspace-name` (string)

The name of the user-decoupled WorkSpace.

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

**To describe a WorkSpace**

The following `describe-workspaces` example describes the specified WorkSpace.

```
aws workspaces describe-workspaces \
    --workspace-ids ws-dk1xzr417
```

Output:

```
{
    "Workspaces": [
        {
            "WorkspaceId": "ws-dk1xzr417",
            "DirectoryId": "d-926722edaf",
            "UserName": "Mary",
            "IpAddress": "172.16.0.175",
            "State": "STOPPED",
            "BundleId": "wsb-0zsvgp8fc",
            "SubnetId": "subnet-500d5819",
            "ComputerName": "WSAMZN-RBSLTTD9",
            "WorkspaceProperties": {
                "RunningMode": "AUTO_STOP",
                "RunningModeAutoStopTimeoutInMinutes": 60,
                "RootVolumeSizeGib": 80,
                "UserVolumeSizeGib": 10,
                "ComputeTypeName": "VALUE"
            },
            "ModificationStates": []
        }
    ]
}
```

For more information, see [Administer your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/administer-workspaces.html) in the *Amazon WorkSpaces Administration Guide*.

## Output

Workspaces -> (list)

Information about the WorkSpaces.

Because  CreateWorkspaces is an asynchronous operation, some of the returned information could be incomplete.

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

NextToken -> (string)

The token to use to retrieve the next page of results. This value is null when there are no more results to return.