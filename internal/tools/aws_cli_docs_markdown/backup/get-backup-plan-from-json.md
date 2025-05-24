# get-backup-plan-from-jsonÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-backup-plan-from-json.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-backup-plan-from-json.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html#cli-aws-backup) ]

# get-backup-plan-from-json

## Description

Returns a valid JSON document specifying a backup plan or an error.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/GetBackupPlanFromJSON)

## Synopsis

```
get-backup-plan-from-json
--backup-plan-template-json <value>
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

`--backup-plan-template-json` (string)

A customer-supplied backup plan document in JSON format.

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

BackupPlan -> (structure)

Specifies the body of a backup plan. Includes a `BackupPlanName` and one or more sets of `Rules` .

BackupPlanName -> (string)

The display name of a backup plan. Must contain only alphanumeric or â-_.â special characters.

If this is set in the console, it can contain 1 to 50 characters; if this is set through CLI or API, it can contain 1 to 200 characters.

Rules -> (list)

An array of `BackupRule` objects, each of which specifies a scheduled task that is used to back up a selection of resources.

(structure)

Specifies a scheduled task used to back up a selection of resources.

RuleName -> (string)

A display name for a backup rule. Must contain 1 to 50 alphanumeric or â-_.â characters.

TargetBackupVaultName -> (string)

The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.

ScheduleExpression -> (string)

A cron expression in UTC specifying when Backup initiates a backup job. For more information about Amazon Web Services cron expressions, see [Schedule Expressions for Rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html) in the *Amazon CloudWatch Events User Guide.* . Two examples of Amazon Web Services cron expressions are `15 * ? * * *` (take a backup every hour at 15 minutes past the hour) and `0 12 * * ? *` (take a backup every day at 12 noon UTC). For a table of examples, click the preceding link and scroll down the page.

StartWindowMinutes -> (long)

A value in minutes after a backup is scheduled before a job will be canceled if it doesnât start successfully. This value is optional. If this value is included, it must be at least 60 minutes to avoid errors.

During the start window, the backup job status remains in `CREATED` status until it has successfully begun or until the start window time has run out. If within the start window time Backup receives an error that allows the job to be retried, Backup will automatically retry to begin the job at least every 10 minutes until the backup successfully begins (the job status changes to `RUNNING` ) or until the job status changes to `EXPIRED` (which is expected to occur when the start window time is over).

CompletionWindowMinutes -> (long)

A value in minutes after a backup job is successfully started before it must be completed or it will be canceled by Backup. This value is optional.

Lifecycle -> (structure)

The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup transitions and expires backups automatically according to the lifecycle that you define.

Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the âretentionâ setting must be 90 days greater than the âtransition to cold after daysâ setting. The âtransition to cold after daysâ setting cannot be changed after a backup has been transitioned to cold.

Resource types that can transition to cold storage are listed in the [Feature availability by resource](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource) table. Backup ignores this expression for other resource types.

MoveToColdStorageAfterDays -> (long)

The number of days after creation that a recovery point is moved to cold storage.

DeleteAfterDays -> (long)

The number of days after creation that a recovery point is deleted. This value must be at least 90 days after the number of days specified in `MoveToColdStorageAfterDays` .

OptInToArchiveForSupportedResources -> (boolean)

If the value is true, your backup plan transitions supported resources to archive (cold) storage tier in accordance with your lifecycle settings.

RecoveryPointTags -> (map)

The tags that are assigned to resources that are associated with this rule when restored from backup.

key -> (string)

value -> (string)

RuleId -> (string)

Uniquely identifies a rule that is used to schedule the backup of a selection of resources.

CopyActions -> (list)

An array of `CopyAction` objects, which contains the details of the copy operation.

(structure)

The details of the copy operation.

Lifecycle -> (structure)

Specifies the time period, in days, before a recovery point transitions to cold storage or is deleted.

Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, on the console, the retention setting must be 90 days greater than the transition to cold after days setting. The transition to cold after days setting canât be changed after a backup has been transitioned to cold.

Resource types that can transition to cold storage are listed in the [Feature availability by resource](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource) table. Backup ignores this expression for other resource types.

To remove the existing lifecycle and retention periods and keep your recovery points indefinitely, specify -1 for `MoveToColdStorageAfterDays` and `DeleteAfterDays` .

MoveToColdStorageAfterDays -> (long)

The number of days after creation that a recovery point is moved to cold storage.

DeleteAfterDays -> (long)

The number of days after creation that a recovery point is deleted. This value must be at least 90 days after the number of days specified in `MoveToColdStorageAfterDays` .

OptInToArchiveForSupportedResources -> (boolean)

If the value is true, your backup plan transitions supported resources to archive (cold) storage tier in accordance with your lifecycle settings.

DestinationBackupVaultArn -> (string)

An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup. For example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault` .

EnableContinuousBackup -> (boolean)

Specifies whether Backup creates continuous backups. True causes Backup to create continuous backups capable of point-in-time restore (PITR). False (or not specified) causes Backup to create snapshot backups.

ScheduleExpressionTimezone -> (string)

The timezone in which the schedule expression is set. By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.

IndexActions -> (list)

IndexActions is an array you use to specify how backup data should be indexed.

eEach BackupRule can have 0 or 1 IndexAction, as each backup can have up to one index associated with it.

Within the array is ResourceType. Only one will be accepted for each BackupRule.

(structure)

This is an optional array within a BackupRule.

IndexAction consists of one ResourceTypes.

ResourceTypes -> (list)

0 or 1 index action will be accepted for each BackupRule.

Valid values:

- `EBS` for Amazon Elastic Block Store
- `S3` for Amazon Simple Storage Service (Amazon S3)

(string)

AdvancedBackupSettings -> (list)

Contains a list of `BackupOptions` for each resource type.

(structure)

The backup options for each resource type.

ResourceType -> (string)

Specifies an object containing resource type and backup options. The only supported resource type is Amazon EC2 instances with Windows Volume Shadow Copy Service (VSS). For a CloudFormation example, see the [sample CloudFormation template to enable Windows VSS](https://docs.aws.amazon.com/aws-backup/latest/devguide/integrate-cloudformation-with-aws-backup.html) in the *Backup User Guide* .

Valid values: `EC2` .

BackupOptions -> (map)

Specifies the backup option for a selected resource. This option is only available for Windows VSS backup jobs.

Valid values:

Set to `"WindowsVSS":"enabled"` to enable the `WindowsVSS` backup option and create a Windows VSS backup.

Set to `"WindowsVSS":"disabled"` to create a regular backup. The `WindowsVSS` option is not enabled by default.

If you specify an invalid option, you get an `InvalidParameterValueException` exception.

For more information about Windows VSS backups, see [Creating a VSS-Enabled Windows Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/windows-backups.html) .

key -> (string)

value -> (string)