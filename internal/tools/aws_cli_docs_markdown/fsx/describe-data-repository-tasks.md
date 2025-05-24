# describe-data-repository-tasksÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/describe-data-repository-tasks.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/describe-data-repository-tasks.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [fsx](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/index.html#cli-aws-fsx) ]

# describe-data-repository-tasks

## Description

Returns the description of specific Amazon FSx for Lustre or Amazon File Cache data repository tasks, if one or more `TaskIds` values are provided in the request, or if filters are used in the request. You can use filters to narrow the response to include just tasks for specific file systems or caches, or tasks in a specific lifecycle state. Otherwise, it returns all data repository tasks owned by your Amazon Web Services account in the Amazon Web Services Region of the endpoint that youâre calling.

When retrieving all tasks, you can paginate the response by using the optional `MaxResults` parameter to limit the number of tasks returned in a response. If more tasks remain, a `NextToken` value is returned in the response. In this case, send a later request with the `NextToken` request parameter set to the value of `NextToken` from the last response.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/DescribeDataRepositoryTasks)

## Synopsis

```
describe-data-repository-tasks
[--task-ids <value>]
[--filters <value>]
[--max-results <value>]
[--next-token <value>]
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

`--task-ids` (list)

(Optional) IDs of the tasks whose descriptions you want to retrieve (String).

(string)

Syntax:

```
"string" "string" ...
```

`--filters` (list)

(Optional) You can use filters to narrow the `DescribeDataRepositoryTasks` response to include just tasks for specific file systems, or tasks in a specific lifecycle state.

(structure)

(Optional) An array of filter objects you can use to filter the response of data repository tasks you will see in the response. You can filter the tasks returned in the response by one or more file system IDs, task lifecycles, and by task type. A filter object consists of a filter `Name` , and one or more `Values` for the filter.

Name -> (string)

Name of the task property to use in filtering the tasks returned in the response.

- Use `file-system-id` to retrieve data repository tasks for specific file systems.
- Use `task-lifecycle` to retrieve data repository tasks with one or more specific lifecycle states, as follows: CANCELED, EXECUTING, FAILED, PENDING, and SUCCEEDED.

Values -> (list)

Use Values to include the specific file system IDs and task lifecycle states for the filters you are using.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "file-system-id"|"task-lifecycle"|"data-repository-association-id"|"file-cache-id",
    "Values": ["string", ...]
  }
  ...
]
```

`--max-results` (integer)

The maximum number of resources to return in the response. This value must be an integer greater than zero.

`--next-token` (string)

(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.

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

DataRepositoryTasks -> (list)

The collection of data repository task descriptions returned.

(structure)

A description of the data repository task.

- You use import and export data repository tasks to perform bulk transfer operations between an Amazon FSx for Lustre file system and a linked data repository.
- You use release data repository tasks to release files that have been exported to a linked S3 bucket from your Amazon FSx for Lustre file system.
- An Amazon File Cache resource uses a task to automatically release files from the cache.

To learn more about data repository tasks, see [Data Repository Tasks](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-repository-tasks.html) .

TaskId -> (string)

The system-generated, unique 17-digit ID of the data repository task.

Lifecycle -> (string)

The lifecycle status of the data repository task, as follows:

- `PENDING` - The task has not started.
- `EXECUTING` - The task is in process.
- `FAILED` - The task was not able to be completed. For example, there may be files the task failed to process. The  DataRepositoryTaskFailureDetails property provides more information about task failures.
- `SUCCEEDED` - The task has completed successfully.
- `CANCELED` - The task was canceled and it did not complete.
- `CANCELING` - The task is in process of being canceled.

### Note

You cannot delete an FSx for Lustre file system if there are data repository tasks for the file system in the `PENDING` or `EXECUTING` states. Please retry when the data repository task is finished (with a status of `CANCELED` , `SUCCEEDED` , or `FAILED` ). You can use the DescribeDataRepositoryTask action to monitor the task status. Contact the FSx team if you need to delete your file system immediately.

Type -> (string)

The type of data repository task.

- `EXPORT_TO_REPOSITORY` tasks export from your Amazon FSx for Lustre file system to a linked data repository.
- `IMPORT_METADATA_FROM_REPOSITORY` tasks import metadata changes from a linked S3 bucket to your Amazon FSx for Lustre file system.
- `RELEASE_DATA_FROM_FILESYSTEM` tasks release files in your Amazon FSx for Lustre file system that have been exported to a linked S3 bucket and that meet your specified release criteria.
- `AUTO_RELEASE_DATA` tasks automatically release files from an Amazon File Cache resource.

CreationTime -> (timestamp)

The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

StartTime -> (timestamp)

The time the system began processing the task.

EndTime -> (timestamp)

The time the system completed processing the task, populated after the task is complete.

ResourceARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

Tags -> (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

FileSystemId -> (string)

The globally unique ID of the file system.

Paths -> (list)

An array of paths that specify the data for the data repository task to process. For example, in an EXPORT_TO_REPOSITORY task, the paths specify which data to export to the linked data repository.

(Default) If `Paths` is not specified, Amazon FSx uses the file system root directory.

(string)

FailureDetails -> (structure)

Failure message describing why the task failed, it is populated only when `Lifecycle` is set to `FAILED` .

Message -> (string)

A detailed error message.

Status -> (structure)

Provides the status of the number of files that the task has processed successfully and failed to process.

TotalCount -> (long)

The total number of files that the task will process. While a task is executing, the sum of `SucceededCount` plus `FailedCount` may not equal `TotalCount` . When the task is complete, `TotalCount` equals the sum of `SucceededCount` plus `FailedCount` .

SucceededCount -> (long)

A running total of the number of files that the task has successfully processed.

FailedCount -> (long)

A running total of the number of files that the task failed to process.

LastUpdatedTime -> (timestamp)

The time at which the task status was last updated.

ReleasedCapacity -> (long)

The total amount of data, in GiB, released by an Amazon File Cache AUTO_RELEASE_DATA task that automatically releases files from the cache.

Report -> (structure)

Provides a report detailing the data repository task results of the files processed that match the criteria specified in the report `Scope` parameter. FSx delivers the report to the file systemâs linked data repository in Amazon S3, using the path specified in the report `Path` parameter. You can specify whether or not a report gets generated for a task using the `Enabled` parameter.

Enabled -> (boolean)

Set `Enabled` to `True` to generate a `CompletionReport` when the task completes. If set to `true` , then you need to provide a report `Scope` , `Path` , and `Format` . Set `Enabled` to `False` if you do not want a `CompletionReport` generated when the task completes.

Path -> (string)

Required if `Enabled` is set to `true` . Specifies the location of the report on the file systemâs linked S3 data repository. An absolute path that defines where the completion report will be stored in the destination location. The `Path` you provide must be located within the file systemâs ExportPath. An example `Path` value is âs3://amzn-s3-demo-bucket/myExportPath/optionalPrefixâ. The report provides the following information for each file in the report: FilePath, FileStatus, and ErrorCode.

Format -> (string)

Required if `Enabled` is set to `true` . Specifies the format of the `CompletionReport` . `REPORT_CSV_20191124` is the only format currently supported. When `Format` is set to `REPORT_CSV_20191124` , the `CompletionReport` is provided in CSV format, and is delivered to `{path}/task-{id}/failures.csv` .

Scope -> (string)

Required if `Enabled` is set to `true` . Specifies the scope of the `CompletionReport` ; `FAILED_FILES_ONLY` is the only scope currently supported. When `Scope` is set to `FAILED_FILES_ONLY` , the `CompletionReport` only contains information about files that the data repository task failed to process.

CapacityToRelease -> (long)

Specifies the amount of data to release, in GiB, by an Amazon File Cache AUTO_RELEASE_DATA task that automatically releases files from the cache.

FileCacheId -> (string)

The system-generated, unique ID of the cache.

ReleaseConfiguration -> (structure)

The configuration that specifies the last accessed time criteria for files that will be released from an Amazon FSx for Lustre file system.

DurationSinceLastAccess -> (structure)

Defines the point-in-time since an exported file was last accessed, in order for that file to be eligible for release. Only files that were last accessed before this point-in-time are eligible to be released from the file system.

Unit -> (string)

The unit of time used by the `Value` parameter to determine if a file can be released, based on when it was last accessed. `DAYS` is the only supported value. This is a required parameter.

Value -> (long)

An integer that represents the minimum amount of time (in days) since a file was last accessed in the file system. Only exported files with a `MAX(atime, ctime, mtime)` timestamp that is more than this amount of time in the past (relative to the task create time) will be released. The default of `Value` is `0` . This is a required parameter.

### Note

If an exported file meets the last accessed time criteria, its file or directory path must also be specified in the `Paths` parameter of the operation in order for the file to be released.

NextToken -> (string)

(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.