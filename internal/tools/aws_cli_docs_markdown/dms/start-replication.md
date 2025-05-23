# start-replicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-replication.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-replication.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/index.html#cli-aws-dms) ]

# start-replication

## Description

For a given DMS Serverless replication configuration, DMS connects to the source endpoint and collects the metadata to analyze the replication workload. Using this metadata, DMS then computes and provisions the required capacity and starts replicating to the target endpoint using the server resources that DMS has provisioned for the DMS Serverless replication.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/StartReplication)

## Synopsis

```
start-replication
--replication-config-arn <value>
--start-replication-type <value>
[--premigration-assessment-settings <value>]
[--cdc-start-time <value>]
[--cdc-start-position <value>]
[--cdc-stop-position <value>]
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

`--replication-config-arn` (string)

The Amazon Resource Name of the replication for which to start replication.

`--start-replication-type` (string)

The replication type.

When the replication type is `full-load` or `full-load-and-cdc` , the only valid value for the first run of the replication is `start-replication` . This option will start the replication.

You can also use  ReloadTables to reload specific tables that failed during replication instead of restarting the replication.

The `resume-processing` option isnât applicable for a full-load replication, because you canât resume partially loaded tables during the full load phase.

For a `full-load-and-cdc` replication, DMS migrates table data, and then applies data changes that occur on the source. To load all the tables again, and start capturing source changes, use `reload-target` . Otherwise use `resume-processing` , to replicate the changes from the last stop position.

`--premigration-assessment-settings` (string)

User-defined settings for the premigration assessment. The possible values are:

- `ResultLocationFolder` : The folder within an Amazon S3 bucket where you want DMS to store the results of this assessment run.
- `ResultEncryptionMode` : The supported values are `SSE_KMS` and `SSE_S3` . If these values are not provided, then the files are not encrypted at rest. For more information, see [Creating Amazon Web Services KMS keys to encrypt Amazon S3 target objects](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.KMSKeys) .
- `ResultKmsKeyArn` : The ARN of a customer KMS encryption key that you specify when you set `ResultEncryptionMode` to `SSE_KMS` .
- `IncludeOnly` : A space-separated list of names for specific individual assessments that you want to include. These names come from the default list of individual assessments that Database Migration Service supports for the associated migration.
- `Exclude` : A space-separated list of names for specific individual assessments that you want to exclude. These names come from the default list of individual assessments that Database Migration Service supports for the associated migration.
- `FailOnAssessmentFailure` : A configurable setting you can set to `true` (the default setting) or `false` . Use this setting to to stop the replication from starting automatically if the assessment fails. This can help you evaluate the issue that is preventing the replication from running successfully.

`--cdc-start-time` (timestamp)

Indicates the start time for a change data capture (CDC) operation. Use either `CdcStartTime` or `CdcStartPosition` to specify when you want a CDC operation to start. Specifying both values results in an error.

`--cdc-start-position` (string)

Indicates when you want a change data capture (CDC) operation to start. Use either `CdcStartPosition` or `CdcStartTime` to specify when you want a CDC operation to start. Specifying both values results in an error.

The value can be in date, checkpoint, or LSN/SCN format.

`--cdc-stop-position` (string)

Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.

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

Replication -> (structure)

The replication that DMS started.

ReplicationConfigIdentifier -> (string)

The identifier for the `ReplicationConfig` associated with the replication.

ReplicationConfigArn -> (string)

The Amazon Resource Name for the `ReplicationConfig` associated with the replication.

SourceEndpointArn -> (string)

The Amazon Resource Name for an existing `Endpoint` the serverless replication uses for its data source.

TargetEndpointArn -> (string)

The Amazon Resource Name for an existing `Endpoint` the serverless replication uses for its data target.

ReplicationType -> (string)

The type of the serverless replication.

Status -> (string)

The current status of the serverless replication.

ProvisionData -> (structure)

Information about provisioning resources for an DMS serverless replication.

ProvisionState -> (string)

The current provisioning state

ProvisionedCapacityUnits -> (integer)

The number of capacity units the replication is using.

DateProvisioned -> (timestamp)

The timestamp when DMS provisioned replication resources.

IsNewProvisioningAvailable -> (boolean)

Whether the new provisioning is available to the replication.

DateNewProvisioningDataAvailable -> (timestamp)

The timestamp when provisioning became available.

ReasonForNewProvisioningData -> (string)

A message describing the reason that DMS provisioned new resources for the serverless replication.

PremigrationAssessmentStatuses -> (list)

The status output of premigration assessment in describe-replications.

(structure)

The results returned in `describe-replications` to display the results of the premigration assessment from the replication configuration.

PremigrationAssessmentRunArn -> (string)

The Amazon Resource Name (ARN) of this assessment run.

FailOnAssessmentFailure -> (boolean)

A configurable setting you can set to `true` (the defualt setting) or `false` . Use this setting to to stop the replication from starting automatically if the assessment fails. This can help you evaluate the issue that is preventing the replication from running successfully.

Status -> (string)

This describes the assessment run status. The status can be one of the following values:

- `cancelling` : The assessment run was canceled.
- `deleting` : The assessment run was deleted.
- `failed` : At least one individual assessment completed with a failed status.
- `error-provisioning` : An internal error occurred while resources were provisioned (during the `provisioning` status).
- `error-executing` An internal error occurred while individual assessments ran (during the `running` status).
- `invalid state` : The assessment run is in an unknown state.
- `passed` : All individual assessments have completed and none have a failed status.
- `provisioning` : The resources required to run individual assessments are being provisioned.
- `running` : Individual assessments are being run.
- `starting` : The assessment run is starting, but resources are not yet being provisioned for individual assessments.
- `warning` : At least one individual assessment completed with a warning status.

PremigrationAssessmentRunCreationDate -> (timestamp)

The date which the assessment run was created.

AssessmentProgress -> (structure)

The progress values reported by the `AssessmentProgress` response element.

IndividualAssessmentCount -> (integer)

The number of individual assessments that are specified to run.

IndividualAssessmentCompletedCount -> (integer)

The number of individual assessments that have completed, successfully or not.

LastFailureMessage -> (string)

The last message generated by an individual assessment failure.

ResultLocationBucket -> (string)

The Amazon S3 bucket that Database Migration Service Serverless created to store the results of this assessment run.

ResultLocationFolder -> (string)

The folder within an Amazon S3 bucket where you want Database Migration Service to store the results of this assessment run.

ResultEncryptionMode -> (string)

The supported values are `SSE_KMS` and `SSE_S3` . If these values are not provided, then the files are not encrypted at rest. For more information, see [Creating Amazon Web Services KMS keys to encrypt Amazon S3 target objects](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.KMSKeys) .

ResultKmsKeyArn -> (string)

The ARN of a custom KMS encryption key that you specify when you set `ResultEncryptionMode` to `SSE_KMS` .

ResultStatistic -> (structure)

The object containing the result statistics for a completed assessment run.

Passed -> (integer)

The number of individual assessments that successfully passed all checks in the assessment run.

Failed -> (integer)

The number of individual assessments that failed to meet the criteria defined in the assessment run.

Error -> (integer)

The number of individual assessments that encountered a critical error and could not complete properly.

Warning -> (integer)

Indicates that the recent completed AssessmentRun triggered a warning.

Cancelled -> (integer)

The number of individual assessments that were cancelled during the assessment run.

Skipped -> (integer)

The number of individual assessments that were skipped during the assessment run.

StopReason -> (string)

The reason the replication task was stopped. This response parameter can return one of the following values:

- `"Stop Reason NORMAL"`
- `"Stop Reason RECOVERABLE_ERROR"`
- `"Stop Reason FATAL_ERROR"`
- `"Stop Reason FULL_LOAD_ONLY_FINISHED"`
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

FailureMessages -> (list)

Error and other information about why a serverless replication failed.

(string)

ReplicationStats -> (structure)

This object provides a collection of statistics about a serverless replication.

FullLoadProgressPercent -> (integer)

The percent complete for the full load serverless replication.

ElapsedTimeMillis -> (long)

The elapsed time of the replication, in milliseconds.

TablesLoaded -> (integer)

The number of tables loaded for this replication.

TablesLoading -> (integer)

The number of tables currently loading for this replication.

TablesQueued -> (integer)

The number of tables queued for this replication.

TablesErrored -> (integer)

The number of errors that have occured for this replication.

FreshStartDate -> (timestamp)

The date the replication was started either with a fresh start or a target reload.

StartDate -> (timestamp)

The date the replication is scheduled to start.

StopDate -> (timestamp)

The date the replication was stopped.

FullLoadStartDate -> (timestamp)

The date the replication full load was started.

FullLoadFinishDate -> (timestamp)

The date the replication full load was finished.

StartReplicationType -> (string)

The type of replication to start.

CdcStartTime -> (timestamp)

Indicates the start time for a change data capture (CDC) operation. Use either `CdcStartTime` or `CdcStartPosition` to specify when you want a CDC operation to start. Specifying both values results in an error.

CdcStartPosition -> (string)

Indicates the start time for a change data capture (CDC) operation. Use either `CdcStartTime` or `CdcStartPosition` to specify when you want a CDC operation to start. Specifying both values results in an error.

CdcStopPosition -> (string)

Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.

RecoveryCheckpoint -> (string)

Indicates the last checkpoint that occurred during a change data capture (CDC) operation. You can provide this value to the `CdcStartPosition` parameter to start a CDC operation that begins at that checkpoint.

ReplicationCreateTime -> (timestamp)

The time the serverless replication was created.

ReplicationUpdateTime -> (timestamp)

The time the serverless replication was updated.

ReplicationLastStopTime -> (timestamp)

The timestamp when replication was last stopped.

ReplicationDeprovisionTime -> (timestamp)

The timestamp when DMS will deprovision the replication.