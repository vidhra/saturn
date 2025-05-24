# delete-replication-task-assessment-runÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-task-assessment-run.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-task-assessment-run.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/index.html#cli-aws-dms) ]

# delete-replication-task-assessment-run

## Description

Deletes the record of a single premigration assessment run.

This operation removes all metadata that DMS maintains about this assessment run. However, the operation leaves untouched all information about this assessment run that is stored in your Amazon S3 bucket.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DeleteReplicationTaskAssessmentRun)

## Synopsis

```
delete-replication-task-assessment-run
--replication-task-assessment-run-arn <value>
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

`--replication-task-assessment-run-arn` (string)

Amazon Resource Name (ARN) of the premigration assessment run to be deleted.

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

ReplicationTaskAssessmentRun -> (structure)

The `ReplicationTaskAssessmentRun` object for the deleted assessment run.

ReplicationTaskAssessmentRunArn -> (string)

Amazon Resource Name (ARN) of this assessment run.

ReplicationTaskArn -> (string)

ARN of the migration task associated with this premigration assessment run.

Status -> (string)

Assessment run status.

This status can have one of the following values:

- `"cancelling"` â The assessment run was canceled by the `CancelReplicationTaskAssessmentRun` operation.
- `"deleting"` â The assessment run was deleted by the `DeleteReplicationTaskAssessmentRun` operation.
- `"failed"` â At least one individual assessment completed with a `failed` status.
- `"error-provisioning"` â An internal error occurred while resources were provisioned (during `provisioning` status).
- `"error-executing"` â An internal error occurred while individual assessments ran (during `running` status).
- `"invalid state"` â The assessment run is in an unknown state.
- `"passed"` â All individual assessments have completed, and none has a `failed` status.
- `"provisioning"` â Resources required to run individual assessments are being provisioned.
- `"running"` â Individual assessments are being run.
- `"starting"` â The assessment run is starting, but resources are not yet being provisioned for individual assessments.
- `"warning"` â At least one individual assessment completed with a `warning` status or all individual assessments were skipped (completed with a `skipped` status).

ReplicationTaskAssessmentRunCreationDate -> (timestamp)

Date on which the assessment run was created using the `StartReplicationTaskAssessmentRun` operation.

AssessmentProgress -> (structure)

Indication of the completion progress for the individual assessments specified to run.

IndividualAssessmentCount -> (integer)

The number of individual assessments that are specified to run.

IndividualAssessmentCompletedCount -> (integer)

The number of individual assessments that have completed, successfully or not.

LastFailureMessage -> (string)

Last message generated by an individual assessment failure.

ServiceAccessRoleArn -> (string)

ARN of the service role used to start the assessment run using the `StartReplicationTaskAssessmentRun` operation. The role must allow the `iam:PassRole` action.

ResultLocationBucket -> (string)

Amazon S3 bucket where DMS stores the results of this assessment run.

ResultLocationFolder -> (string)

Folder in an Amazon S3 bucket where DMS stores the results of this assessment run.

ResultEncryptionMode -> (string)

Encryption mode used to encrypt the assessment run results.

ResultKmsKeyArn -> (string)

ARN of the KMS encryption key used to encrypt the assessment run results.

AssessmentRunName -> (string)

Unique name of the assessment run.

IsLatestTaskAssessmentRun -> (boolean)

Indicates that the following PreflightAssessmentRun is the latest for the ReplicationTask. The status is either true or false.

ResultStatistic -> (structure)

Result statistics for a completed assessment run, showing aggregated statistics of IndividualAssessments for how many assessments were passed, failed, or encountered issues such as errors or warnings.

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