# create-backup-planÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-plan.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-plan.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html#cli-aws-backup) ]

# create-backup-plan

## Description

Creates a backup plan using a backup plan name and backup rules. A backup plan is a document that contains information that Backup uses to schedule tasks that create recovery points for resources.

If you call `CreateBackupPlan` with a plan that already exists, you receive an `AlreadyExistsException` exception.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/CreateBackupPlan)

## Synopsis

```
create-backup-plan
--backup-plan <value>
[--backup-plan-tags <value>]
[--creator-request-id <value>]
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

`--backup-plan` (structure)

The body of a backup plan. Includes a `BackupPlanName` and one or more sets of `Rules` .

BackupPlanName -> (string)

The display name of a backup plan. Must contain 1 to 50 alphanumeric or â-_.â characters.

Rules -> (list)

An array of `BackupRule` objects, each of which specifies a scheduled task that is used to back up a selection of resources.

(structure)

Specifies a scheduled task used to back up a selection of resources.

RuleName -> (string)

A display name for a backup rule. Must contain 1 to 50 alphanumeric or â-_.â characters.

TargetBackupVaultName -> (string)

The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.

ScheduleExpression -> (string)

A CRON expression in UTC specifying when Backup initiates a backup job.

StartWindowMinutes -> (long)

A value in minutes after a backup is scheduled before a job will be canceled if it doesnât start successfully. This value is optional. If this value is included, it must be at least 60 minutes to avoid errors.

This parameter has a maximum value of 100 years (52,560,000 minutes).

During the start window, the backup job status remains in `CREATED` status until it has successfully begun or until the start window time has run out. If within the start window time Backup receives an error that allows the job to be retried, Backup will automatically retry to begin the job at least every 10 minutes until the backup successfully begins (the job status changes to `RUNNING` ) or until the job status changes to `EXPIRED` (which is expected to occur when the start window time is over).

CompletionWindowMinutes -> (long)

A value in minutes after a backup job is successfully started before it must be completed or it will be canceled by Backup. This value is optional.

Lifecycle -> (structure)

The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup will transition and expire backups automatically according to the lifecycle that you define.

Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the âretentionâ setting must be 90 days greater than the âtransition to cold after daysâ setting. The âtransition to cold after daysâ setting cannot be changed after a backup has been transitioned to cold storage.

Resource types that can transition to cold storage are listed in the [Feature availability by resource](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource) table. Backup ignores this expression for other resource types.

This parameter has a maximum value of 100 years (36,500 days).

MoveToColdStorageAfterDays -> (long)

The number of days after creation that a recovery point is moved to cold storage.

DeleteAfterDays -> (long)

The number of days after creation that a recovery point is deleted. This value must be at least 90 days after the number of days specified in `MoveToColdStorageAfterDays` .

OptInToArchiveForSupportedResources -> (boolean)

If the value is true, your backup plan transitions supported resources to archive (cold) storage tier in accordance with your lifecycle settings.

RecoveryPointTags -> (map)

The tags to assign to the resources.

key -> (string)

value -> (string)

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

There can up to one IndexAction in each BackupRule, as each backup can have 0 or 1 backup index associated with it.

Within the array is ResourceTypes. Only 1 resource type will be accepted for each BackupRule. Valid values:

- `EBS` for Amazon Elastic Block Store
- `S3` for Amazon Simple Storage Service (Amazon S3)

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

Specifies a list of `BackupOptions` for each resource type. These settings are only available for Windows Volume Shadow Copy Service (VSS) backup jobs.

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

JSON Syntax:

```
{
  "BackupPlanName": "string",
  "Rules": [
    {
      "RuleName": "string",
      "TargetBackupVaultName": "string",
      "ScheduleExpression": "string",
      "StartWindowMinutes": long,
      "CompletionWindowMinutes": long,
      "Lifecycle": {
        "MoveToColdStorageAfterDays": long,
        "DeleteAfterDays": long,
        "OptInToArchiveForSupportedResources": true|false
      },
      "RecoveryPointTags": {"string": "string"
        ...},
      "CopyActions": [
        {
          "Lifecycle": {
            "MoveToColdStorageAfterDays": long,
            "DeleteAfterDays": long,
            "OptInToArchiveForSupportedResources": true|false
          },
          "DestinationBackupVaultArn": "string"
        }
        ...
      ],
      "EnableContinuousBackup": true|false,
      "ScheduleExpressionTimezone": "string",
      "IndexActions": [
        {
          "ResourceTypes": ["string", ...]
        }
        ...
      ]
    }
    ...
  ],
  "AdvancedBackupSettings": [
    {
      "ResourceType": "string",
      "BackupOptions": {"string": "string"
        ...}
    }
    ...
  ]
}
```

`--backup-plan-tags` (map)

The tags to assign to the backup plan.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--creator-request-id` (string)

Identifies the request and allows failed requests to be retried without the risk of running the operation twice. If the request includes a `CreatorRequestId` that matches an existing backup plan, that plan is returned. This parameter is optional.

If used, this parameter must contain 1 to 50 alphanumeric or â-_.â characters.

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

**To create a backup plan**

The following `create-backup-plan` example creates the specified backup plan with a 35 day retention.

```
aws backup create-backup-plan \
--backup-plan "{\"BackupPlanName\":\"Example-Backup-Plan\",\"Rules\":[{\"RuleName\":\"DailyBackups\",\"ScheduleExpression\":\"cron(0 5 ? * * *)\",\"StartWindowMinutes\":480,\"TargetBackupVaultName\":\"Default\",\"Lifecycle\":{\"DeleteAfterDays\":35}}]}"
```

Output:

```
{
    "BackupPlanId": "1fa3895c-a7f5-484a-a371-2dd6a1a9f729",
    "BackupPlanArn": "arn:aws:backup:us-west-2:123456789012:backup-plan:1fa3895c-a7f5-484a-a371-2dd6a1a9f729",
    "CreationDate": 1568928754.747,
    "VersionId": "ZjQ2ZTI5YWQtZDg5Yi00MzYzLWJmZTAtMDI1MzhlMDhjYjEz"
}
```

For more information, see [Creating a Backup Plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html) in the *AWS Backup Developer Guide*.

## Output

BackupPlanId -> (string)

The ID of the backup plan.

BackupPlanArn -> (string)

An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, `arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50` .

CreationDate -> (timestamp)

The date and time that a backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

VersionId -> (string)

Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.

AdvancedBackupSettings -> (list)

The settings for a resource type. This option is only available for Windows Volume Shadow Copy Service (VSS) backup jobs.

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