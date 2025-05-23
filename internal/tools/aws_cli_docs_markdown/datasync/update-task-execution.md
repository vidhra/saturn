# update-task-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-task-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-task-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datasync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/index.html#cli-aws-datasync) ]

# update-task-execution

## Description

Updates the configuration of a running DataSync task execution.

### Note

Currently, the only `Option` that you can modify with `UpdateTaskExecution` is `` [BytesPerSecond](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-BytesPerSecond) `` , which throttles bandwidth for a running or queued task execution.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/UpdateTaskExecution)

## Synopsis

```
update-task-execution
--task-execution-arn <value>
--options <value>
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

`--task-execution-arn` (string)

Specifies the Amazon Resource Name (ARN) of the task execution that youâre updating.

`--options` (structure)

Indicates how your transfer task is configured. These options include how DataSync handles files, objects, and their associated metadata during your transfer. You also can specify how to verify data integrity, set bandwidth limits for your task, among other options.

Each option has a default value. Unless you need to, you donât have to configure any option before calling [StartTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_StartTaskExecution.html) .

You also can override your task options for each task execution. For example, you might want to adjust the `LogLevel` for an individual execution.

VerifyMode -> (string)

Specifies if and how DataSync checks the integrity of your data at the end of your transfer.

- `ONLY_FILES_TRANSFERRED` (recommended) - DataSync calculates the checksum of transferred data (including metadata) at the source location. At the end of the transfer, DataSync then compares this checksum to the checksum calculated on that data at the destination.

### Note

This is the default option for [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html) .

We recommend this option when transferring to S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes. For more information, see [Storage class considerations with Amazon S3 locations](https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes) .

- `POINT_IN_TIME_CONSISTENT` - At the end of the transfer, DataSync checks the entire source and destination to verify that both locations are fully synchronized.

### Note

The is the default option for [Basic mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html) and isnât currently supported with Enhanced mode tasks.

If you use a [manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html) , DataSync only scans and verifies whatâs listed in the manifest. You canât use this option when transferring to S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes. For more information, see [Storage class considerations with Amazon S3 locations](https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes) .

- `NONE` - DataSync performs data integrity checks only during your transfer. Unlike other options, thereâs no additional verification at the end of your transfer.

OverwriteMode -> (string)

Specifies whether DataSync should modify or preserve data at the destination location.

- `ALWAYS` (default) - DataSync modifies data in the destination location when source data (including metadata) has changed. If DataSync overwrites objects, you might incur additional charges for certain Amazon S3 storage classes (for example, for retrieval or early deletion). For more information, see [Storage class considerations with Amazon S3 transfers](https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes) .
- `NEVER` - DataSync doesnât overwrite data in the destination location even if the source data has changed. You can use this option to protect against overwriting changes made to files or objects in the destination.

Atime -> (string)

Specifies whether to preserve metadata indicating the last time a file was read or written to.

### Note

The behavior of `Atime` isnât fully standard across platforms, so DataSync can only do this on a best-effort basis.

- `BEST_EFFORT` (default) - DataSync attempts to preserve the original `Atime` attribute on all source files (that is, the version before the `PREPARING` steps of the task execution). This option is recommended.
- `NONE` - Ignores `Atime` .

### Note

If `Atime` is set to `BEST_EFFORT` , `Mtime` must be set to `PRESERVE` .

If `Atime` is set to `NONE` , `Mtime` must also be `NONE` .

Mtime -> (string)

Specifies whether to preserve metadata indicating the last time that a file was written to before the `PREPARING` step of your task execution. This option is required when you need to run the a task more than once.

- `PRESERVE` (default) - Preserves original `Mtime` , which is recommended.
- `NONE` - Ignores `Mtime` .

### Note

If `Mtime` is set to `PRESERVE` , `Atime` must be set to `BEST_EFFORT` .

If `Mtime` is set to `NONE` , `Atime` must also be set to `NONE` .

Uid -> (string)

Specifies the POSIX user ID (UID) of the fileâs owner.

- `INT_VALUE` (default) - Preserves the integer value of UID and group ID (GID), which is recommended.
- `NONE` - Ignores UID and GID.

For more information, see [Metadata copied by DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/special-files.html#metadata-copied) .

Gid -> (string)

Specifies the POSIX group ID (GID) of the fileâs owners.

- `INT_VALUE` (default) - Preserves the integer value of user ID (UID) and GID, which is recommended.
- `NONE` - Ignores UID and GID.

For more information, see [Understanding how DataSync handles file and object metadata](https://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) .

PreserveDeletedFiles -> (string)

Specifies whether files in the destination location that donât exist in the source should be preserved. This option can affect your Amazon S3 storage cost. If your task deletes objects, you might incur minimum storage duration charges for certain storage classes. For detailed information, see [Considerations when working with Amazon S3 storage classes in DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes) .

- `PRESERVE` (default) - Ignores such destination files, which is recommended.
- `REMOVE` - Deletes destination files that arenât present in the source.

### Note

If you set this parameter to `REMOVE` , you canât set `TransferMode` to `ALL` . When you transfer all data, DataSync doesnât scan your destination location and doesnât know what to delete.

PreserveDevices -> (string)

Specifies whether DataSync should preserve the metadata of block and character devices in the source location and recreate the files with that device name and metadata on the destination. DataSync copies only the name and metadata of such devices.

### Note

DataSync canât copy the actual contents of these devices because theyâre nonterminal and donât return an end-of-file (EOF) marker.

- `NONE` (default) - Ignores special devices (recommended).
- `PRESERVE` - Preserves character and block device metadata. This option currently isnât supported for Amazon EFS.

PosixPermissions -> (string)

Specifies which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file.

For more information, see [Understanding how DataSync handles file and object metadata](https://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) .

- `PRESERVE` (default) - Preserves POSIX-style permissions, which is recommended.
- `NONE` - Ignores POSIX-style permissions.

### Note

DataSync can preserve extant permissions of a source location.

BytesPerSecond -> (long)

Limits the bandwidth used by a DataSync task. For example, if you want DataSync to use a maximum of 1 MB, set this value to `1048576` (`=1024*1024` ).

### Note

Not applicable to [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html) .

TaskQueueing -> (string)

Specifies whether your transfer tasks should be put into a queue during certain scenarios when [running multiple tasks](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#running-multiple-tasks) . This is `ENABLED` by default.

LogLevel -> (string)

Specifies the type of logs that DataSync publishes to a Amazon CloudWatch Logs log group. To specify the log group, see [CloudWatchLogGroupArn](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateTask.html#DataSync-CreateTask-request-CloudWatchLogGroupArn) .

- `BASIC` - Publishes logs with only basic information (such as transfer errors).
- `TRANSFER` - Publishes logs for all files or objects that your DataSync task transfers and performs data-integrity checks on.
- `OFF` - No logs are published.

TransferMode -> (string)

Specifies whether DataSync transfers only the data (including metadata) that differs between locations following an initial copy or transfers all data every time you run the task. If youâre planning on recurring transfers, you might only want to transfer whatâs changed since your previous task execution.

- `CHANGED` (default) - After your initial full transfer, DataSync copies only the data and metadata that differs between the source and destination location.
- `ALL` - DataSync copies everything in the source to the destination without comparing differences between the locations.

SecurityDescriptorCopyFlags -> (string)

Specifies which components of the SMB security descriptor are copied from source to destination objects.

This value is only used for transfers between SMB and Amazon FSx for Windows File Server locations or between two FSx for Windows File Server locations. For more information, see [Understanding how DataSync handles file and object metadata](https://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) .

- `OWNER_DACL` (default) - For each copied object, DataSync copies the following metadata:
- The object owner.
- NTFS discretionary access control lists (DACLs), which determine whether to grant access to an object. DataSync wonât copy NTFS system access control lists (SACLs) with this option.
- `OWNER_DACL_SACL` - For each copied object, DataSync copies the following metadata:
- The object owner.
- NTFS discretionary access control lists (DACLs), which determine whether to grant access to an object.
- SACLs, which are used by administrators to log attempts to access a secured object. Copying SACLs requires granting additional permissions to the Windows user that DataSync uses to access your SMB location. For information about choosing a user with the right permissions, see required permissions for [SMB](https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions) , [FSx for Windows File Server](https://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html#create-fsx-windows-location-permissions) , or [FSx for ONTAP](https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-smb) (depending on the type of location in your transfer).
- `NONE` - None of the SMB security descriptor components are copied. Destination objects are owned by the user that was provided for accessing the destination location. DACLs and SACLs are set based on the destination serverâs configuration.

ObjectTags -> (string)

Specifies whether you want DataSync to `PRESERVE` object tags (default behavior) when transferring between object storage systems. If you want your DataSync task to ignore object tags, specify the `NONE` value.

Shorthand Syntax:

```
VerifyMode=string,OverwriteMode=string,Atime=string,Mtime=string,Uid=string,Gid=string,PreserveDeletedFiles=string,PreserveDevices=string,PosixPermissions=string,BytesPerSecond=long,TaskQueueing=string,LogLevel=string,TransferMode=string,SecurityDescriptorCopyFlags=string,ObjectTags=string
```

JSON Syntax:

```
{
  "VerifyMode": "POINT_IN_TIME_CONSISTENT"|"ONLY_FILES_TRANSFERRED"|"NONE",
  "OverwriteMode": "ALWAYS"|"NEVER",
  "Atime": "NONE"|"BEST_EFFORT",
  "Mtime": "NONE"|"PRESERVE",
  "Uid": "NONE"|"INT_VALUE"|"NAME"|"BOTH",
  "Gid": "NONE"|"INT_VALUE"|"NAME"|"BOTH",
  "PreserveDeletedFiles": "PRESERVE"|"REMOVE",
  "PreserveDevices": "NONE"|"PRESERVE",
  "PosixPermissions": "NONE"|"PRESERVE",
  "BytesPerSecond": long,
  "TaskQueueing": "ENABLED"|"DISABLED",
  "LogLevel": "OFF"|"BASIC"|"TRANSFER",
  "TransferMode": "CHANGED"|"ALL",
  "SecurityDescriptorCopyFlags": "NONE"|"OWNER_DACL"|"OWNER_DACL_SACL",
  "ObjectTags": "PRESERVE"|"NONE"
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

## Output

None