# stop-replication-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/stop-replication-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/stop-replication-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/index.html#cli-aws-dms) ]

# stop-replication-task

## Description

Stops the replication task.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/StopReplicationTask)

## Synopsis

```
stop-replication-task
--replication-task-arn <value>
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

`--replication-task-arn` (string)

The Amazon Resource Name(ARN) of the replication task to be stopped.

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

**To stop a task**

The following `stop-replication-task` example stops a task.

```
aws dms stop-replication-task \
    --replication-task-arn arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII
```

Output:

```
{
    "ReplicationTask": {
        "ReplicationTaskIdentifier": "moveit2",
        "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA",
        "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U",
        "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE",
        "MigrationType": "full-load",
        "TableMappings": ...output omitted...,
        "ReplicationTaskSettings": ...output omitted...,
        "Status": "stopping",
        "ReplicationTaskCreationDate": 1590524772.505,
        "ReplicationTaskStartDate": 1590789424.653,
        "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII"
    }
}
```

For more information, see [Working with AWS DMS Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html) in the *AWS Database Migration Service User Guide*.

## Output

ReplicationTask -> (structure)

The replication task stopped.

ReplicationTaskIdentifier -> (string)

The user-assigned replication task identifier or name.

Constraints:

- Must contain 1-255 alphanumeric characters or hyphens.
- First character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.

SourceEndpointArn -> (string)

The Amazon Resource Name (ARN) that uniquely identifies the endpoint.

TargetEndpointArn -> (string)

The ARN that uniquely identifies the endpoint.

ReplicationInstanceArn -> (string)

The ARN of the replication instance.

MigrationType -> (string)

The type of migration.

TableMappings -> (string)

Table mappings specified in the task.

ReplicationTaskSettings -> (string)

The settings for the replication task.

Status -> (string)

The status of the replication task. This response parameter can return one of the following values:

- `"moving"` â The task is being moved in response to running the ` `MoveReplicationTask` [https://docs.aws.amazon.com/dms/latest/APIReference/API_MoveReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_MoveReplicationTask).html`__ operation.
- `"creating"` â The task is being created in response to running the ` `CreateReplicationTask` [https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask).html`__ operation.
- `"deleting"` â The task is being deleted in response to running the ` `DeleteReplicationTask` [https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteReplicationTask).html`__ operation.
- `"failed"` â The task failed to successfully complete the database migration in response to running the ` `StartReplicationTask` [https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask).html`__ operation.
- `"failed-move"` â The task failed to move in response to running the ` `MoveReplicationTask` [https://docs.aws.amazon.com/dms/latest/APIReference/API_MoveReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_MoveReplicationTask).html`__ operation.
- `"modifying"` â The task definition is being modified in response to running the ` `ModifyReplicationTask` [https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationTask).html`__ operation.
- `"ready"` â The task is in a `ready` state where it can respond to other task operations, such as ` `StartReplicationTask` [https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask).html`__ or ` `DeleteReplicationTask` [https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteReplicationTask).html`__ .
- `"running"` â The task is performing a database migration in response to running the ` `StartReplicationTask` [https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask).html`__ operation.
- `"starting"` â The task is preparing to perform a database migration in response to running the ` `StartReplicationTask` [https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask).html`__ operation.
- `"stopped"` â The task has stopped in response to running the ` `StopReplicationTask` [https://docs.aws.amazon.com/dms/latest/APIReference/API_StopReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_StopReplicationTask).html`__ operation.
- `"stopping"` â The task is preparing to stop in response to running the ` `StopReplicationTask` [https://docs.aws.amazon.com/dms/latest/APIReference/API_StopReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_StopReplicationTask).html`__ operation.
- `"testing"` â The database migration specified for this task is being tested in response to running either the ` `StartReplicationTaskAssessmentRun` [https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessmentRun](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessmentRun).html`__ or the ` `StartReplicationTaskAssessment` [https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessment](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessment).html`__ operation.

### Note

` `StartReplicationTaskAssessmentRun` [https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessmentRun](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessmentRun).html`__ is an improved premigration task assessment operation. The ` `StartReplicationTaskAssessment` [https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessment](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessment).html`__ operation assesses data type compatibility only between the source and target database of a given migration task. In contrast, ` `StartReplicationTaskAssessmentRun` [https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessmentRun](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessmentRun).html`__ enables you to specify a variety of premigration task assessments in addition to data type compatibility. These assessments include ones for the validity of primary key definitions and likely issues with database migration performance, among others.

LastFailureMessage -> (string)

The last error (failure) message generated for the replication task.

StopReason -> (string)

The reason the replication task was stopped. This response parameter can return one of the following values:

- `"Stop Reason NORMAL"` â The task completed successfully with no additional information returned.
- `"Stop Reason RECOVERABLE_ERROR"`
- `"Stop Reason FATAL_ERROR"`
- `"Stop Reason FULL_LOAD_ONLY_FINISHED"` â The task completed the full load phase. DMS applied cached changes if you set `StopTaskCachedChangesApplied` to `true` .
- `"Stop Reason STOPPED_AFTER_FULL_LOAD"` â Full load completed, with cached changes not applied
- `"Stop Reason STOPPED_AFTER_CACHED_EVENTS"` â Full load completed, with cached changes applied
- `"Stop Reason EXPRESS_LICENSE_LIMITS_REACHED"`
- `"Stop Reason STOPPED_AFTER_DDL_APPLY"` â User-defined stop task after DDL applied
- `"Stop Reason STOPPED_DUE_TO_LOW_MEMORY"`
- `"Stop Reason STOPPED_DUE_TO_LOW_DISK"`
- `"Stop Reason STOPPED_AT_SERVER_TIME"` â User-defined server time for stopping task
- `"Stop Reason STOPPED_AT_COMMIT_TIME"` â User-defined commit time for stopping task
- `"Stop Reason RECONFIGURATION_RESTART"`
- `"Stop Reason RECYCLE_TASK"`

ReplicationTaskCreationDate -> (timestamp)

The date the replication task was created.

ReplicationTaskStartDate -> (timestamp)

The date the replication task is scheduled to start.

CdcStartPosition -> (string)

Indicates when you want a change data capture (CDC) operation to start. Use either `CdcStartPosition` or `CdcStartTime` to specify when you want the CDC operation to start. Specifying both values results in an error.

The value can be in date, checkpoint, or LSN/SCN format.

Date Example: âcdc-start-position â2018-03-08T12:12:12â

Checkpoint Example: âcdc-start-position âcheckpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93â

LSN Example: âcdc-start-position âmysql-bin-changelog.000024:373â

CdcStopPosition -> (string)

Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.

Server time example: âcdc-stop-position âserver_time:2018-02-09T12:12:12â

Commit time example: âcdc-stop-position âcommit_time:2018-02-09T12:12:12â

RecoveryCheckpoint -> (string)

Indicates the last checkpoint that occurred during a change data capture (CDC) operation. You can provide this value to the `CdcStartPosition` parameter to start a CDC operation that begins at that checkpoint.

ReplicationTaskArn -> (string)

The Amazon Resource Name (ARN) of the replication task.

ReplicationTaskStats -> (structure)

The statistics for the task, including elapsed time, tables loaded, and table errors.

FullLoadProgressPercent -> (integer)

The percent complete for the full load migration task.

ElapsedTimeMillis -> (long)

The elapsed time of the task, in milliseconds.

TablesLoaded -> (integer)

The number of tables loaded for this task.

TablesLoading -> (integer)

The number of tables currently loading for this task.

TablesQueued -> (integer)

The number of tables queued for this task.

TablesErrored -> (integer)

The number of errors that have occurred during this task.

FreshStartDate -> (timestamp)

The date the replication task was started either with a fresh start or a target reload.

StartDate -> (timestamp)

The date the replication task was started either with a fresh start or a resume. For more information, see [StartReplicationTaskType](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html#DMS-StartReplicationTask-request-StartReplicationTaskType) .

StopDate -> (timestamp)

The date the replication task was stopped.

FullLoadStartDate -> (timestamp)

The date the replication task full load was started.

FullLoadFinishDate -> (timestamp)

The date the replication task full load was completed.

TaskData -> (string)

Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see [Specifying Supplemental Data for Task Settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html) in the *Database Migration Service User Guide.*

TargetReplicationInstanceArn -> (string)

The ARN of the replication instance to which this task is moved in response to running the ` `MoveReplicationTask` [https://docs.aws.amazon.com/dms/latest/APIReference/API_MoveReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_MoveReplicationTask).html`__ operation. Otherwise, this response parameter isnât a member of the `ReplicationTask` object.