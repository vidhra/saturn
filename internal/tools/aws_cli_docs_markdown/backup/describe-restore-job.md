# describe-restore-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-restore-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-restore-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html#cli-aws-backup) ]

# describe-restore-job

## Description

Returns metadata associated with a restore job that is specified by a job ID.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/DescribeRestoreJob)

## Synopsis

```
describe-restore-job
--restore-job-id <value>
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

`--restore-job-id` (string)

Uniquely identifies the job that restores a recovery point.

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

Returns the account ID that owns the restore job.

RestoreJobId -> (string)

Uniquely identifies the job that restores a recovery point.

RecoveryPointArn -> (string)

An ARN that uniquely identifies a recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45` .

CreationDate -> (timestamp)

The date and time that a restore job is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CompletionDate -> (timestamp)

The date and time that a job to restore a recovery point is completed, in Unix format and Coordinated Universal Time (UTC). The value of `CompletionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

Status -> (string)

Status code specifying the state of the job that is initiated by Backup to restore a recovery point.

StatusMessage -> (string)

A message showing the status of a job to restore a recovery point.

PercentDone -> (string)

Contains an estimated percentage that is complete of a job at the time the job status was queried.

BackupSizeInBytes -> (long)

The size, in bytes, of the restored resource.

IamRoleArn -> (string)

Specifies the IAM role ARN used to create the target recovery point; for example, `arn:aws:iam::123456789012:role/S3Access` .

ExpectedCompletionTimeMinutes -> (long)

The amount of time in minutes that a job restoring a recovery point is expected to take.

CreatedResourceArn -> (string)

The Amazon Resource Name (ARN) of the resource that was created by the restore job.

The format of the ARN depends on the resource type of the backed-up resource.

ResourceType -> (string)

Returns metadata associated with a restore job listed by resource type.

RecoveryPointCreationDate -> (timestamp)

The creation date of the recovery point made by the specifed restore job.

CreatedBy -> (structure)

Contains identifying information about the creation of a restore job.

RestoreTestingPlanArn -> (string)

An Amazon Resource Name (ARN) that uniquely identifies a restore testing plan.

ValidationStatus -> (string)

The status of validation run on the indicated restore job.

ValidationStatusMessage -> (string)

The status message.

DeletionStatus -> (string)

The status of the data generated by the restore test.

DeletionStatusMessage -> (string)

This describes the restore job deletion status.