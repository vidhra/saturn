# describe-backup-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-backup-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-backup-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html#cli-aws-backup) ]

# describe-backup-job

## Description

Returns backup job details for the specified `BackupJobId` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/DescribeBackupJob)

## Synopsis

```
describe-backup-job
--backup-job-id <value>
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

`--backup-job-id` (string)

Uniquely identifies a request to Backup to back up a resource.

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

AccountId -> (string)

Returns the account ID that owns the backup job.

BackupJobId -> (string)

Uniquely identifies a request to Backup to back up a resource.

BackupVaultName -> (string)

The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.

BackupVaultArn -> (string)

An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault` .

RecoveryPointArn -> (string)

An ARN that uniquely identifies a recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45` .

ResourceArn -> (string)

An ARN that uniquely identifies a saved resource. The format of the ARN depends on the resource type.

CreationDate -> (timestamp)

The date and time that a backup job is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CompletionDate -> (timestamp)

The date and time that a job to create a backup job is completed, in Unix format and Coordinated Universal Time (UTC). The value of `CompletionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

State -> (string)

The current state of a backup job.

StatusMessage -> (string)

A detailed message explaining the status of the job to back up a resource.

PercentDone -> (string)

Contains an estimated percentage that is complete of a job at the time the job status was queried.

BackupSizeInBytes -> (long)

The size, in bytes, of a backup.

IamRoleArn -> (string)

Specifies the IAM role ARN used to create the target recovery point; for example, `arn:aws:iam::123456789012:role/S3Access` .

CreatedBy -> (structure)

Contains identifying information about the creation of a backup job, including the `BackupPlanArn` , `BackupPlanId` , `BackupPlanVersion` , and `BackupRuleId` of the backup plan that is used to create it.

BackupPlanId -> (string)

Uniquely identifies a backup plan.

BackupPlanArn -> (string)

An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, `arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50` .

BackupPlanVersion -> (string)

Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.

BackupRuleId -> (string)

Uniquely identifies a rule used to schedule the backup of a selection of resources.

ResourceType -> (string)

The type of Amazon Web Services resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

BytesTransferred -> (long)

The size in bytes transferred to a backup vault at the time that the job status was queried.

ExpectedCompletionDate -> (timestamp)

The date and time that a job to back up resources is expected to be completed, in Unix format and Coordinated Universal Time (UTC). The value of `ExpectedCompletionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

StartBy -> (timestamp)

Specifies the time in Unix format and Coordinated Universal Time (UTC) when a backup job must be started before it is canceled. The value is calculated by adding the start window to the scheduled time. So if the scheduled time were 6:00 PM and the start window is 2 hours, the `StartBy` time would be 8:00 PM on the date specified. The value of `StartBy` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

BackupOptions -> (map)

Represents the options specified as part of backup plan or on-demand backup job.

key -> (string)

value -> (string)

BackupType -> (string)

Represents the actual backup type selected for a backup job. For example, if a successful Windows Volume Shadow Copy Service (VSS) backup was taken, `BackupType` returns `"WindowsVSS"` . If `BackupType` is empty, then the backup type was a regular backup.

ParentJobId -> (string)

This returns the parent (composite) resource backup job ID.

IsParent -> (boolean)

This returns the boolean value that a backup job is a parent (composite) job.

NumberOfChildJobs -> (long)

This returns the number of child (nested) backup jobs.

ChildJobsInState -> (map)

This returns the statistics of the included child (nested) backup jobs.

key -> (string)

value -> (long)

ResourceName -> (string)

The non-unique name of the resource that belongs to the specified backup.

InitiationDate -> (timestamp)

The date a backup job was initiated.

MessageCategory -> (string)

The job count for the specified message category.

Example strings may include `AccessDenied` , `SUCCESS` , `AGGREGATE_ALL` , and `INVALIDPARAMETERS` . View [Monitoring](https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html) for a list of accepted MessageCategory strings.