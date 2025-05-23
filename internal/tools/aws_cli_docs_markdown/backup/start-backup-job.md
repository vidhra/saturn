# start-backup-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-backup-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-backup-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html#cli-aws-backup) ]

# start-backup-job

## Description

Starts an on-demand backup job for the specified resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/StartBackupJob)

## Synopsis

```
start-backup-job
--backup-vault-name <value>
--resource-arn <value>
--iam-role-arn <value>
[--idempotency-token <value>]
[--start-window-minutes <value>]
[--complete-window-minutes <value>]
[--lifecycle <value>]
[--recovery-point-tags <value>]
[--backup-options <value>]
[--index <value>]
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

`--resource-arn` (string)

An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.

`--iam-role-arn` (string)

Specifies the IAM role ARN used to create the target recovery point; for example, `arn:aws:iam::123456789012:role/S3Access` .

`--idempotency-token` (string)

A customer-chosen string that you can use to distinguish between otherwise identical calls to `StartBackupJob` . Retrying a successful request with the same idempotency token results in a success message with no action taken.

`--start-window-minutes` (long)

A value in minutes after a backup is scheduled before a job will be canceled if it doesnât start successfully. This value is optional, and the default is 8 hours. If this value is included, it must be at least 60 minutes to avoid errors.

This parameter has a maximum value of 100 years (52,560,000 minutes).

During the start window, the backup job status remains in `CREATED` status until it has successfully begun or until the start window time has run out. If within the start window time Backup receives an error that allows the job to be retried, Backup will automatically retry to begin the job at least every 10 minutes until the backup successfully begins (the job status changes to `RUNNING` ) or until the job status changes to `EXPIRED` (which is expected to occur when the start window time is over).

`--complete-window-minutes` (long)

A value in minutes during which a successfully started backup must complete, or else Backup will cancel the job. This value is optional. This value begins counting down from when the backup was scheduled. It does not add additional time for `StartWindowMinutes` , or if the backup started later than scheduled.

Like `StartWindowMinutes` , this parameter has a maximum value of 100 years (52,560,000 minutes).

`--lifecycle` (structure)

The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup will transition and expire backups automatically according to the lifecycle that you define.

Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the âretentionâ setting must be 90 days greater than the âtransition to cold after daysâ setting. The âtransition to cold after daysâ setting cannot be changed after a backup has been transitioned to cold.

Resource types that can transition to cold storage are listed in the [Feature availability by resource](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource) table. Backup ignores this expression for other resource types.

This parameter has a maximum value of 100 years (36,500 days).

MoveToColdStorageAfterDays -> (long)

The number of days after creation that a recovery point is moved to cold storage.

DeleteAfterDays -> (long)

The number of days after creation that a recovery point is deleted. This value must be at least 90 days after the number of days specified in `MoveToColdStorageAfterDays` .

OptInToArchiveForSupportedResources -> (boolean)

If the value is true, your backup plan transitions supported resources to archive (cold) storage tier in accordance with your lifecycle settings.

Shorthand Syntax:

```
MoveToColdStorageAfterDays=long,DeleteAfterDays=long,OptInToArchiveForSupportedResources=boolean
```

JSON Syntax:

```
{
  "MoveToColdStorageAfterDays": long,
  "DeleteAfterDays": long,
  "OptInToArchiveForSupportedResources": true|false
}
```

`--recovery-point-tags` (map)

The tags to assign to the resources.

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

`--backup-options` (map)

The backup option for a selected resource. This option is only available for Windows Volume Shadow Copy Service (VSS) backup jobs.

Valid values: Set to `"WindowsVSS":"enabled"` to enable the `WindowsVSS` backup option and create a Windows VSS backup. Set to `"WindowsVSS""disabled"` to create a regular backup. The `WindowsVSS` option is not enabled by default.

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

`--index` (string)

Include this parameter to enable index creation if your backup job has a resource type that supports backup indexes.

Resource types that support backup indexes include:

- `EBS` for Amazon Elastic Block Store
- `S3` for Amazon Simple Storage Service (Amazon S3)

Index can have 1 of 2 possible values, either `ENABLED` or `DISABLED` .

To create a backup index for an eligible `ACTIVE` recovery point that does not yet have a backup index, set value to `ENABLED` .

To delete a backup index, set value to `DISABLED` .

Possible values:

- `ENABLED`
- `DISABLED`

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

BackupJobId -> (string)

Uniquely identifies a request to Backup to back up a resource.

RecoveryPointArn -> (string)

*Note: This field is only returned for Amazon EFS and Advanced DynamoDB resources.*

An ARN that uniquely identifies a recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45` .

CreationDate -> (timestamp)

The date and time that a backup job is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

IsParent -> (boolean)

This is a returned boolean value indicating this is a parent (composite) backup job.