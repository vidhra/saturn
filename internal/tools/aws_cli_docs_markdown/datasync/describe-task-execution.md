# describe-task-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-task-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-task-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datasync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/index.html#cli-aws-datasync) ]

# describe-task-execution

## Description

Provides information about an execution of your DataSync task. You can use this operation to help monitor the progress of an ongoing data transfer or check the results of the transfer.

### Note

Some `DescribeTaskExecution` response elements are only relevant to a specific task mode. For information, see [Understanding task mode differences](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html#task-mode-differences) and [Understanding data transfer performance counters](https://docs.aws.amazon.com/datasync/latest/userguide/transfer-performance-counters.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/DescribeTaskExecution)

## Synopsis

```
describe-task-execution
--task-execution-arn <value>
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

Specifies the Amazon Resource Name (ARN) of the task execution that you want information about.

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

TaskExecutionArn -> (string)

The ARN of the task execution that you wanted information about. `TaskExecutionArn` is hierarchical and includes `TaskArn` for the task that was executed.

For example, a `TaskExecution` value with the ARN `arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2/execution/exec-08ef1e88ec491019b` executed the task with the ARN `arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2` .

Status -> (string)

The status of the task execution.

Options -> (structure)

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

Excludes -> (list)

A list of filter rules that exclude specific data during your transfer. For more information and examples, see [Filtering data transferred by DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html) .

(structure)

Specifies which files, folders, and objects to include or exclude when transferring files from source to destination.

FilterType -> (string)

The type of filter rule to apply. DataSync only supports the SIMPLE_PATTERN rule type.

Value -> (string)

A single filter string that consists of the patterns to include or exclude. The patterns are delimited by â|â (that is, a pipe), for example: `/folder1|/folder2`

Includes -> (list)

A list of filter rules that include specific data during your transfer. For more information and examples, see [Filtering data transferred by DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html) .

(structure)

Specifies which files, folders, and objects to include or exclude when transferring files from source to destination.

FilterType -> (string)

The type of filter rule to apply. DataSync only supports the SIMPLE_PATTERN rule type.

Value -> (string)

A single filter string that consists of the patterns to include or exclude. The patterns are delimited by â|â (that is, a pipe), for example: `/folder1|/folder2`

ManifestConfig -> (structure)

The configuration of the manifest that lists the files or objects to transfer. For more information, see [Specifying what DataSync transfers by using a manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html) .

Action -> (string)

Specifies what DataSync uses the manifest for.

Format -> (string)

Specifies the file format of your manifest. For more information, see [Creating a manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-create) .

Source -> (structure)

Specifies the manifest that you want DataSync to use and where itâs hosted.

### Note

You must specify this parameter if youâre configuring a new manifest on or after February 7, 2024.

If you donât, youâll get a 400 status code and `ValidationException` error stating that youâre missing the IAM role for DataSync to access the S3 bucket where youâre hosting your manifest. For more information, see [Providing DataSync access to your manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-access) .

S3 -> (structure)

Specifies the S3 bucket where youâre hosting your manifest.

ManifestObjectPath -> (string)

Specifies the Amazon S3 object key of your manifest. This can include a prefix (for example, `prefix/my-manifest.csv` ).

BucketAccessRoleArn -> (string)

Specifies the Identity and Access Management (IAM) role that allows DataSync to access your manifest. For more information, see [Providing DataSync access to your manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-access) .

S3BucketArn -> (string)

Specifies the Amazon Resource Name (ARN) of the S3 bucket where youâre hosting your manifest.

ManifestObjectVersionId -> (string)

Specifies the object version ID of the manifest that you want DataSync to use. If you donât set this, DataSync uses the latest version of the object.

StartTime -> (timestamp)

The time when the task execution started.

EstimatedFilesToTransfer -> (long)

The number of files, objects, and directories that DataSync expects to transfer over the network. This value is calculated while DataSync [prepares](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses) the transfer.

How this gets calculated depends primarily on your taskâs [transfer mode](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-TransferMode) configuration:

- If `TranserMode` is set to `CHANGED` - The calculation is based on comparing the content of the source and destination locations and determining the difference that needs to be transferred. The difference can include:
- Anything thatâs added or modified at the source location.
- Anything thatâs in both locations and modified at the destination after an initial transfer (unless [OverwriteMode](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-OverwriteMode) is set to `NEVER` ).
- **(Basic task mode only)** The number of items that DataSync expects to delete (if [PreserveDeletedFiles](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-PreserveDeletedFiles) is set to `REMOVE` ).
- If `TranserMode` is set to `ALL` - The calculation is based only on the items that DataSync finds at the source location.

EstimatedBytesToTransfer -> (long)

The number of logical bytes that DataSync expects to write to the destination location.

FilesTransferred -> (long)

The number of files, objects, and directories that DataSync actually transfers over the network. This value is updated periodically during your task execution when something is read from the source and sent over the network.

If DataSync fails to transfer something, this value can be less than `EstimatedFilesToTransfer` . In some cases, this value can also be greater than `EstimatedFilesToTransfer` . This element is implementation-specific for some location types, so donât use it as an exact indication of whatâs transferring or to monitor your task execution.

BytesWritten -> (long)

The number of logical bytes that DataSync actually writes to the destination location.

BytesTransferred -> (long)

The number of bytes that DataSync sends to the network before compression (if compression is possible). For the number of bytes transferred over the network, see [BytesCompressed](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-BytesCompressed) .

BytesCompressed -> (long)

The number of physical bytes that DataSync transfers over the network after compression (if compression is possible). This number is typically less than [BytesTransferred](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-BytesTransferred) unless the data isnât compressible.

Result -> (structure)

The result of the task execution.

PrepareDuration -> (long)

The time in milliseconds that your task execution was in the `PREPARING` step. For more information, see [Task execution statuses](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses) .

For Enhanced mode tasks, the value is always `0` . For more information, see [How DataSync prepares your data transfer](https://docs.aws.amazon.com/datasync/latest/userguide/how-datasync-transfer-works.html#how-datasync-prepares) .

PrepareStatus -> (string)

The status of the `PREPARING` step for your task execution. For more information, see [Task execution statuses](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses) .

TotalDuration -> (long)

The time in milliseconds that your task execution ran.

TransferDuration -> (long)

The time in milliseconds that your task execution was in the `TRANSFERRING` step. For more information, see [Task execution statuses](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses) .

For Enhanced mode tasks, the value is always `0` . For more information, see [How DataSync transfers your data](https://docs.aws.amazon.com/datasync/latest/userguide/how-datasync-transfer-works.html#how-datasync-transfers) .

TransferStatus -> (string)

The status of the `TRANSFERRING` step for your task execution. For more information, see [Task execution statuses](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses) .

VerifyDuration -> (long)

The time in milliseconds that your task execution was in the `VERIFYING` step. For more information, see [Task execution statuses](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses) .

For Enhanced mode tasks, the value is always `0` . For more information, see [How DataSync verifies your dataâs integrity](https://docs.aws.amazon.com/datasync/latest/userguide/how-datasync-transfer-works.html#how-verifying-works) .

VerifyStatus -> (string)

The status of the `VERIFYING` step for your task execution. For more information, see [Task execution statuses](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses) .

ErrorCode -> (string)

An error that DataSync encountered during your task execution. You can use this information to help [troubleshoot issues](https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html) .

ErrorDetail -> (string)

The detailed description of an error that DataSync encountered during your task execution. You can use this information to help [troubleshoot issues](https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html) .

TaskReportConfig -> (structure)

The configuration of your task report, which provides detailed information about for your DataSync transfer. For more information, see [Creating a task report](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html) .

Destination -> (structure)

Specifies the Amazon S3 bucket where DataSync uploads your task report. For more information, see [Task reports](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html#task-report-access) .

S3 -> (structure)

Specifies the Amazon S3 bucket where DataSync uploads your task report.

Subdirectory -> (string)

Specifies a bucket prefix for your report.

S3BucketArn -> (string)

Specifies the ARN of the S3 bucket where DataSync uploads your report.

BucketAccessRoleArn -> (string)

Specifies the Amazon Resource Name (ARN) of the IAM policy that allows DataSync to upload a task report to your S3 bucket. For more information, see [Allowing DataSync to upload a task report to an Amazon S3 bucket](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html) .

OutputType -> (string)

Specifies the type of task report that you want:

- `SUMMARY_ONLY` : Provides necessary details about your task, including the number of files, objects, and directories transferred and transfer duration.
- `STANDARD` : Provides complete details about your task, including a full list of files, objects, and directories that were transferred, skipped, verified, and more.

ReportLevel -> (string)

Specifies whether you want your task report to include only what went wrong with your transfer or a list of what succeeded and didnât.

- `ERRORS_ONLY` : A report shows what DataSync was unable to transfer, skip, verify, and delete.
- `SUCCESSES_AND_ERRORS` : A report shows what DataSync was able and unable to transfer, skip, verify, and delete.

ObjectVersionIds -> (string)

Specifies whether your task report includes the new version of each object transferred into an S3 bucket. This only applies if you [enable versioning on your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html) . Keep in mind that setting this to `INCLUDE` can increase the duration of your task execution.

Overrides -> (structure)

Customizes the reporting level for aspects of your task report. For example, your report might generally only include errors, but you could specify that you want a list of successes and errors just for the files that DataSync attempted to delete in your destination location.

Transferred -> (structure)

Specifies the level of reporting for the files, objects, and directories that DataSync attempted to transfer.

ReportLevel -> (string)

Specifies whether your task report includes errors only or successes and errors.

For example, your report might mostly include only what didnât go well in your transfer (`ERRORS_ONLY` ). At the same time, you want to verify that your [task filter](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html) is working correctly. In this situation, you can get a list of what files DataSync successfully skipped and if something transferred that you didnât to transfer (`SUCCESSES_AND_ERRORS` ).

Verified -> (structure)

Specifies the level of reporting for the files, objects, and directories that DataSync attempted to verify at the end of your transfer.

ReportLevel -> (string)

Specifies whether your task report includes errors only or successes and errors.

For example, your report might mostly include only what didnât go well in your transfer (`ERRORS_ONLY` ). At the same time, you want to verify that your [task filter](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html) is working correctly. In this situation, you can get a list of what files DataSync successfully skipped and if something transferred that you didnât to transfer (`SUCCESSES_AND_ERRORS` ).

Deleted -> (structure)

Specifies the level of reporting for the files, objects, and directories that DataSync attempted to delete in your destination location. This only applies if you [configure your task](https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html) to delete data in the destination that isnât in the source.

ReportLevel -> (string)

Specifies whether your task report includes errors only or successes and errors.

For example, your report might mostly include only what didnât go well in your transfer (`ERRORS_ONLY` ). At the same time, you want to verify that your [task filter](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html) is working correctly. In this situation, you can get a list of what files DataSync successfully skipped and if something transferred that you didnât to transfer (`SUCCESSES_AND_ERRORS` ).

Skipped -> (structure)

Specifies the level of reporting for the files, objects, and directories that DataSync attempted to skip during your transfer.

ReportLevel -> (string)

Specifies whether your task report includes errors only or successes and errors.

For example, your report might mostly include only what didnât go well in your transfer (`ERRORS_ONLY` ). At the same time, you want to verify that your [task filter](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html) is working correctly. In this situation, you can get a list of what files DataSync successfully skipped and if something transferred that you didnât to transfer (`SUCCESSES_AND_ERRORS` ).

FilesDeleted -> (long)

The number of files, objects, and directories that DataSync actually deletes in your destination location. If you donât configure your task to [delete data in the destination that isnât in the source](https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html) , the value is always `0` .

FilesSkipped -> (long)

The number of files, objects, and directories that DataSync skips during your transfer.

FilesVerified -> (long)

The number of files, objects, and directories that DataSync verifies during your transfer.

### Note

When you configure your task to [verify only the data thatâs transferred](https://docs.aws.amazon.com/datasync/latest/userguide/configure-data-verification-options.html) , DataSync doesnât verify directories in some situations or files that fail to transfer.

ReportResult -> (structure)

Indicates whether DataSync generated a complete [task report](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html) for your transfer.

Status -> (string)

Indicates whether DataSync is still working on your report, created a report, or canât create a complete report.

ErrorCode -> (string)

Indicates the code associated with the error if DataSync canât create a complete report.

ErrorDetail -> (string)

Provides details about issues creating a report.

EstimatedFilesToDelete -> (long)

The number of files, objects, and directories that DataSync expects to delete in your destination location. If you donât configure your task to [delete data in the destination that isnât in the source](https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html) , the value is always `0` .

TaskMode -> (string)

The task mode that youâre using. For more information, see [Choosing a task mode for your data transfer](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html) .

FilesPrepared -> (long)

The number of objects that DataSync will attempt to transfer after comparing your source and destination locations.

### Note

Applies only to [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html) .

This counter isnât applicable if you configure your task to [transfer all data](https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html#task-option-transfer-mode) . In that scenario, DataSync copies everything from the source to the destination without comparing differences between the locations.

FilesListed -> (structure)

The number of objects that DataSync finds at your locations.

### Note

Applies only to [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html) .

AtSource -> (long)

The number of objects that DataSync finds at your source location.

- With a [manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html) , DataSync lists only whatâs in your manifest (and not everything at your source location).
- With an include [filter](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html) , DataSync lists only what matches the filter at your source location.
- With an exclude filter, DataSync lists everything at your source location before applying the filter.

AtDestinationForDelete -> (long)

The number of objects that DataSync finds at your destination location. This counter is only applicable if you [configure your task](https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html#task-option-file-object-handling) to delete data in the destination that isnât in the source.

FilesFailed -> (structure)

The number of objects that DataSync fails to prepare, transfer, verify, and delete during your task execution.

### Note

Applies only to [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html) .

Prepare -> (long)

The number of objects that DataSync fails to prepare during your task execution.

Transfer -> (long)

The number of objects that DataSync fails to transfer during your task execution.

Verify -> (long)

The number of objects that DataSync fails to verify during your task execution.

Delete -> (long)

The number of objects that DataSync fails to delete during your task execution.