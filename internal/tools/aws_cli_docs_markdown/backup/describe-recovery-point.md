# describe-recovery-pointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-recovery-point.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-recovery-point.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html#cli-aws-backup) ]

# describe-recovery-point

## Description

Returns metadata associated with a recovery point, including ID, status, encryption, and lifecycle.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/DescribeRecoveryPoint)

## Synopsis

```
describe-recovery-point
--backup-vault-name <value>
--recovery-point-arn <value>
[--backup-vault-account-id <value>]
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

`--backup-vault-name` (string)

The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.

`--recovery-point-arn` (string)

An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45` .

`--backup-vault-account-id` (string)

The account ID of the specified backup vault.

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

RecoveryPointArn -> (string)

An ARN that uniquely identifies a recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45` .

BackupVaultName -> (string)

The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.

BackupVaultArn -> (string)

An ARN that uniquely identifies a backup vault; for example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault` .

SourceBackupVaultArn -> (string)

An Amazon Resource Name (ARN) that uniquely identifies the source vault where the resource was originally backed up in; for example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault` . If the recovery is restored to the same Amazon Web Services account or Region, this value will be `null` .

ResourceArn -> (string)

An ARN that uniquely identifies a saved resource. The format of the ARN depends on the resource type.

ResourceType -> (string)

The type of Amazon Web Services resource to save as a recovery point; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

CreatedBy -> (structure)

Contains identifying information about the creation of a recovery point, including the `BackupPlanArn` , `BackupPlanId` , `BackupPlanVersion` , and `BackupRuleId` of the backup plan used to create it.

BackupPlanId -> (string)

Uniquely identifies a backup plan.

BackupPlanArn -> (string)

An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, `arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50` .

BackupPlanVersion -> (string)

Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.

BackupRuleId -> (string)

Uniquely identifies a rule used to schedule the backup of a selection of resources.

IamRoleArn -> (string)

Specifies the IAM role ARN used to create the target recovery point; for example, `arn:aws:iam::123456789012:role/S3Access` .

Status -> (string)

A status code specifying the state of the recovery point.

`PARTIAL` status indicates Backup could not create the recovery point before the backup window closed. To increase your backup plan window using the API, see [UpdateBackupPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateBackupPlan.html) . You can also increase your backup plan window using the Console by choosing and editing your backup plan.

`EXPIRED` status indicates that the recovery point has exceeded its retention period, but Backup lacks permission or is otherwise unable to delete it. To manually delete these recovery points, see [Step 3: Delete the recovery points](https://docs.aws.amazon.com/aws-backup/latest/devguide/gs-cleanup-resources.html#cleanup-backups) in the *Clean up resources* section of *Getting started* .

`STOPPED` status occurs on a continuous backup where a user has taken some action that causes the continuous backup to be disabled. This can be caused by the removal of permissions, turning off versioning, turning off events being sent to EventBridge, or disabling the EventBridge rules that are put in place by Backup. For recovery points of Amazon S3, Amazon RDS, and Amazon Aurora resources, this status occurs when the retention period of a continuous backup rule is changed.

To resolve `STOPPED` status, ensure that all requested permissions are in place and that versioning is enabled on the S3 bucket. Once these conditions are met, the next instance of a backup rule running will result in a new continuous recovery point being created. The recovery points with STOPPED status do not need to be deleted.

For SAP HANA on Amazon EC2 `STOPPED` status occurs due to user action, application misconfiguration, or backup failure. To ensure that future continuous backups succeed, refer to the recovery point status and check SAP HANA for details.

StatusMessage -> (string)

A status message explaining the status of the recovery point.

CreationDate -> (timestamp)

The date and time that a recovery point is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CompletionDate -> (timestamp)

The date and time that a job to create a recovery point is completed, in Unix format and Coordinated Universal Time (UTC). The value of `CompletionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

BackupSizeInBytes -> (long)

The size, in bytes, of a backup.

CalculatedLifecycle -> (structure)

A `CalculatedLifecycle` object containing `DeleteAt` and `MoveToColdStorageAt` timestamps.

MoveToColdStorageAt -> (timestamp)

A timestamp that specifies when to transition a recovery point to cold storage.

DeleteAt -> (timestamp)

A timestamp that specifies when to delete a recovery point.

Lifecycle -> (structure)

The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup transitions and expires backups automatically according to the lifecycle that you define.

Backups that are transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the âretentionâ setting must be 90 days greater than the âtransition to cold after daysâ setting. The âtransition to cold after daysâ setting cannot be changed after a backup has been transitioned to cold.

Resource types that can transition to cold storage are listed in the [Feature availability by resource](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource) table. Backup ignores this expression for other resource types.

MoveToColdStorageAfterDays -> (long)

The number of days after creation that a recovery point is moved to cold storage.

DeleteAfterDays -> (long)

The number of days after creation that a recovery point is deleted. This value must be at least 90 days after the number of days specified in `MoveToColdStorageAfterDays` .

OptInToArchiveForSupportedResources -> (boolean)

If the value is true, your backup plan transitions supported resources to archive (cold) storage tier in accordance with your lifecycle settings.

EncryptionKeyArn -> (string)

The server-side encryption key used to protect your backups; for example, `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab` .

IsEncrypted -> (boolean)

A Boolean value that is returned as `TRUE` if the specified recovery point is encrypted, or `FALSE` if the recovery point is not encrypted.

StorageClass -> (string)

Specifies the storage class of the recovery point. Valid values are `WARM` or `COLD` .

LastRestoreTime -> (timestamp)

The date and time that a recovery point was last restored, in Unix format and Coordinated Universal Time (UTC). The value of `LastRestoreTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

ParentRecoveryPointArn -> (string)

This is an ARN that uniquely identifies a parent (composite) recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45` .

CompositeMemberIdentifier -> (string)

The identifier of a resource within a composite group, such as nested (child) recovery point belonging to a composite (parent) stack. The ID is transferred from the [logical ID](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html#resources-section-structure-syntax) within a stack.

IsParent -> (boolean)

This returns the boolean value that a recovery point is a parent (composite) job.

ResourceName -> (string)

The name of the resource that belongs to the specified backup.

VaultType -> (string)

The type of vault in which the described recovery point is stored.

IndexStatus -> (string)

This is the current status for the backup index associated with the specified recovery point.

Statuses are: `PENDING` | `ACTIVE` | `FAILED` | `DELETING`

A recovery point with an index that has the status of `ACTIVE` can be included in a search.

IndexStatusMessage -> (string)

A string in the form of a detailed message explaining the status of a backup index associated with the recovery point.