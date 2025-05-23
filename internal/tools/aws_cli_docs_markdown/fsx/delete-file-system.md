# delete-file-systemÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/delete-file-system.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/delete-file-system.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [fsx](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/index.html#cli-aws-fsx) ]

# delete-file-system

## Description

Deletes a file system. After deletion, the file system no longer exists, and its data is gone. Any existing automatic backups and snapshots are also deleted.

To delete an Amazon FSx for NetApp ONTAP file system, first delete all the volumes and storage virtual machines (SVMs) on the file system. Then provide a `FileSystemId` value to the `DeleteFileSystem` operation.

By default, when you delete an Amazon FSx for Windows File Server file system, a final backup is created upon deletion. This final backup isnât subject to the file systemâs retention policy, and must be manually deleted.

To delete an Amazon FSx for Lustre file system, first [unmount](https://docs.aws.amazon.com/fsx/latest/LustreGuide/unmounting-fs.html) it from every connected Amazon EC2 instance, then provide a `FileSystemId` value to the `DeleteFileSystem` operation. By default, Amazon FSx will not take a final backup when the `DeleteFileSystem` operation is invoked. On file systems not linked to an Amazon S3 bucket, set `SkipFinalBackup` to `false` to take a final backup of the file system you are deleting. Backups cannot be enabled on S3-linked file systems. To ensure all of your data is written back to S3 before deleting your file system, you can either monitor for the [AgeOfOldestQueuedMessage](https://docs.aws.amazon.com/fsx/latest/LustreGuide/monitoring-cloudwatch.html#auto-import-export-metrics) metric to be zero (if using automatic export) or you can run an [export data repository task](https://docs.aws.amazon.com/fsx/latest/LustreGuide/export-data-repo-task-dra.html) . If you have automatic export enabled and want to use an export data repository task, you have to disable automatic export before executing the export data repository task.

The `DeleteFileSystem` operation returns while the file system has the `DELETING` status. You can check the file system deletion status by calling the [DescribeFileSystems](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystems.html) operation, which returns a list of file systems in your account. If you pass the file system ID for a deleted file system, the `DescribeFileSystems` operation returns a `FileSystemNotFound` error.

### Note

If a data repository task is in a `PENDING` or `EXECUTING` state, deleting an Amazon FSx for Lustre file system will fail with an HTTP status code 400 (Bad Request).

### Warning

The data in a deleted file system is also deleted and canât be recovered by any means.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/DeleteFileSystem)

## Synopsis

```
delete-file-system
--file-system-id <value>
[--client-request-token <value>]
[--windows-configuration <value>]
[--lustre-configuration <value>]
[--open-zfs-configuration <value>]
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

`--file-system-id` (string)

The ID of the file system that you want to delete.

`--client-request-token` (string)

A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent deletion. This token is automatically filled on your behalf when using the Command Line Interface (CLI) or an Amazon Web Services SDK.

`--windows-configuration` (structure)

The configuration object for the Microsoft Windows file system used in the `DeleteFileSystem` operation.

SkipFinalBackup -> (boolean)

By default, Amazon FSx for Windows takes a final backup on your behalf when the `DeleteFileSystem` operation is invoked. Doing this helps protect you from data loss, and we highly recommend taking the final backup. If you want to skip this backup, use this flag to do so.

FinalBackupTags -> (list)

A set of tags for your final backup.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

Shorthand Syntax:

```
SkipFinalBackup=boolean,FinalBackupTags=[{Key=string,Value=string},{Key=string,Value=string}]
```

JSON Syntax:

```
{
  "SkipFinalBackup": true|false,
  "FinalBackupTags": [
    {
      "Key": "string",
      "Value": "string"
    }
    ...
  ]
}
```

`--lustre-configuration` (structure)

The configuration object for the Amazon FSx for Lustre file system being deleted in the `DeleteFileSystem` operation.

SkipFinalBackup -> (boolean)

Set `SkipFinalBackup` to false if you want to take a final backup of the file system you are deleting. By default, Amazon FSx will not take a final backup on your behalf when the `DeleteFileSystem` operation is invoked. (Default = true)

### Note

The `fsx:CreateBackup` permission is required if you set `SkipFinalBackup` to `false` in order to delete the file system and take a final backup.

FinalBackupTags -> (list)

Use if `SkipFinalBackup` is set to `false` , and you want to apply an array of tags to the final backup. If you have set the file system property `CopyTagsToBackups` to true, and you specify one or more `FinalBackupTags` when deleting a file system, Amazon FSx will not copy any existing file system tags to the backup.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

Shorthand Syntax:

```
SkipFinalBackup=boolean,FinalBackupTags=[{Key=string,Value=string},{Key=string,Value=string}]
```

JSON Syntax:

```
{
  "SkipFinalBackup": true|false,
  "FinalBackupTags": [
    {
      "Key": "string",
      "Value": "string"
    }
    ...
  ]
}
```

`--open-zfs-configuration` (structure)

The configuration object for the OpenZFS file system used in the `DeleteFileSystem` operation.

SkipFinalBackup -> (boolean)

By default, Amazon FSx for OpenZFS takes a final backup on your behalf when the `DeleteFileSystem` operation is invoked. Doing this helps protect you from data loss, and we highly recommend taking the final backup. If you want to skip taking a final backup, set this value to `true` .

FinalBackupTags -> (list)

A list of tags to apply to the file systemâs final backup.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

Options -> (list)

To delete a file system if there are child volumes present below the root volume, use the string `DELETE_CHILD_VOLUMES_AND_SNAPSHOTS` . If your file system has child volumes and you donât use this option, the delete request will fail.

(string)

Shorthand Syntax:

```
SkipFinalBackup=boolean,FinalBackupTags=[{Key=string,Value=string},{Key=string,Value=string}],Options=string,string
```

JSON Syntax:

```
{
  "SkipFinalBackup": true|false,
  "FinalBackupTags": [
    {
      "Key": "string",
      "Value": "string"
    }
    ...
  ],
  "Options": ["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS", ...]
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

FileSystemId -> (string)

The ID of the file system thatâs being deleted.

Lifecycle -> (string)

The file system lifecycle for the deletion request. If the `DeleteFileSystem` operation is successful, this status is `DELETING` .

WindowsResponse -> (structure)

The response object for the Microsoft Windows file system used in the `DeleteFileSystem` operation.

FinalBackupId -> (string)

The ID of the final backup for this file system.

FinalBackupTags -> (list)

The set of tags applied to the final backup.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

LustreResponse -> (structure)

The response object for the Amazon FSx for Lustre file system being deleted in the `DeleteFileSystem` operation.

FinalBackupId -> (string)

The ID of the final backup for this file system.

FinalBackupTags -> (list)

The set of tags applied to the final backup.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

OpenZFSResponse -> (structure)

The response object for the OpenZFS file system thatâs being deleted in the `DeleteFileSystem` operation.

FinalBackupId -> (string)

The ID of the source backup. Specifies the backup that you are copying.

FinalBackupTags -> (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .