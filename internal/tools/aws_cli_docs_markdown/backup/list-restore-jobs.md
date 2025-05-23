# list-restore-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-restore-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-restore-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html#cli-aws-backup) ]

# list-restore-jobs

## Description

Returns a list of jobs that Backup initiated to restore a saved resource, including details about the recovery process.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/ListRestoreJobs)

`list-restore-jobs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `RestoreJobs`

## Synopsis

```
list-restore-jobs
[--by-account-id <value>]
[--by-resource-type <value>]
[--by-created-before <value>]
[--by-created-after <value>]
[--by-status <value>]
[--by-complete-before <value>]
[--by-complete-after <value>]
[--by-restore-testing-plan-arn <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--by-account-id` (string)

The account ID to list the jobs from. Returns only restore jobs associated with the specified account ID.

`--by-resource-type` (string)

Include this parameter to return only restore jobs for the specified resources:

- `Aurora` for Amazon Aurora
- `CloudFormation` for CloudFormation
- `DocumentDB` for Amazon DocumentDB (with MongoDB compatibility)
- `DynamoDB` for Amazon DynamoDB
- `EBS` for Amazon Elastic Block Store
- `EC2` for Amazon Elastic Compute Cloud
- `EFS` for Amazon Elastic File System
- `FSx` for Amazon FSx
- `Neptune` for Amazon Neptune
- `RDS` for Amazon Relational Database Service
- `Redshift` for Amazon Redshift
- `S3` for Amazon Simple Storage Service (Amazon S3)
- `SAP HANA on Amazon EC2` for SAP HANA databases on Amazon Elastic Compute Cloud instances
- `Storage Gateway` for Storage Gateway
- `Timestream` for Amazon Timestream
- `VirtualMachine` for VMware virtual machines

`--by-created-before` (timestamp)

Returns only restore jobs that were created before the specified date.

`--by-created-after` (timestamp)

Returns only restore jobs that were created after the specified date.

`--by-status` (string)

Returns only restore jobs associated with the specified job status.

Possible values:

- `PENDING`
- `RUNNING`
- `COMPLETED`
- `ABORTED`
- `FAILED`

`--by-complete-before` (timestamp)

Returns only copy jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).

`--by-complete-after` (timestamp)

Returns only copy jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).

`--by-restore-testing-plan-arn` (string)

This returns only restore testing jobs that match the specified resource Amazon Resource Name (ARN).

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

RestoreJobs -> (list)

An array of objects that contain detailed information about jobs to restore saved resources.

(structure)

Contains metadata about a restore job.

AccountId -> (string)

The account ID that owns the restore job.

RestoreJobId -> (string)

Uniquely identifies the job that restores a recovery point.

RecoveryPointArn -> (string)

An ARN that uniquely identifies a recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45` .

CreationDate -> (timestamp)

The date and time a restore job is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CompletionDate -> (timestamp)

The date and time a job to restore a recovery point is completed, in Unix format and Coordinated Universal Time (UTC). The value of `CompletionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

Status -> (string)

A status code specifying the state of the job initiated by Backup to restore a recovery point.

StatusMessage -> (string)

A detailed message explaining the status of the job to restore a recovery point.

PercentDone -> (string)

Contains an estimated percentage complete of a job at the time the job status was queried.

BackupSizeInBytes -> (long)

The size, in bytes, of the restored resource.

IamRoleArn -> (string)

The IAM role ARN used to create the target recovery point; for example, `arn:aws:iam::123456789012:role/S3Access` .

ExpectedCompletionTimeMinutes -> (long)

The amount of time in minutes that a job restoring a recovery point is expected to take.

CreatedResourceArn -> (string)

An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.

ResourceType -> (string)

The resource type of the listed restore jobs; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database. For Windows Volume Shadow Copy Service (VSS) backups, the only supported resource type is Amazon EC2.

RecoveryPointCreationDate -> (timestamp)

The date on which a recovery point was created.

CreatedBy -> (structure)

Contains identifying information about the creation of a restore job.

RestoreTestingPlanArn -> (string)

An Amazon Resource Name (ARN) that uniquely identifies a restore testing plan.

ValidationStatus -> (string)

The status of validation run on the indicated restore job.

ValidationStatusMessage -> (string)

This describes the status of validation run on the indicated restore job.

DeletionStatus -> (string)

This notes the status of the data generated by the restore test. The status may be `Deleting` , `Failed` , or `Successful` .

DeletionStatusMessage -> (string)

This describes the restore job deletion status.

NextToken -> (string)

The next item following a partial list of returned items. For example, if a request is made to return `MaxResults` number of items, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.