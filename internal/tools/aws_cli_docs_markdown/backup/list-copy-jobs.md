# list-copy-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-copy-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-copy-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html#cli-aws-backup) ]

# list-copy-jobs

## Description

Returns metadata about your copy jobs.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/ListCopyJobs)

`list-copy-jobs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `CopyJobs`

## Synopsis

```
list-copy-jobs
[--by-resource-arn <value>]
[--by-state <value>]
[--by-created-before <value>]
[--by-created-after <value>]
[--by-resource-type <value>]
[--by-destination-vault-arn <value>]
[--by-account-id <value>]
[--by-complete-before <value>]
[--by-complete-after <value>]
[--by-parent-job-id <value>]
[--by-message-category <value>]
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

`--by-resource-arn` (string)

Returns only copy jobs that match the specified resource Amazon Resource Name (ARN).

`--by-state` (string)

Returns only copy jobs that are in the specified state.

Possible values:

- `CREATED`
- `RUNNING`
- `COMPLETED`
- `FAILED`
- `PARTIAL`

`--by-created-before` (timestamp)

Returns only copy jobs that were created before the specified date.

`--by-created-after` (timestamp)

Returns only copy jobs that were created after the specified date.

`--by-resource-type` (string)

Returns only backup jobs for the specified resources:

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

`--by-destination-vault-arn` (string)

An Amazon Resource Name (ARN) that uniquely identifies a source backup vault to copy from; for example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault` .

`--by-account-id` (string)

The account ID to list the jobs from. Returns only copy jobs associated with the specified account ID.

`--by-complete-before` (timestamp)

Returns only copy jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).

`--by-complete-after` (timestamp)

Returns only copy jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).

`--by-parent-job-id` (string)

This is a filter to list child (nested) jobs based on parent job ID.

`--by-message-category` (string)

This is an optional parameter that can be used to filter out jobs with a MessageCategory which matches the value you input.

Example strings may include `AccessDenied` , `SUCCESS` , `AGGREGATE_ALL` , and `INVALIDPARAMETERS` .

View [Monitoring](https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html) for a list of accepted strings.

The the value ANY returns count of all message categories.

`AGGREGATE_ALL` aggregates job counts for all message categories and returns the sum.

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

CopyJobs -> (list)

An array of structures containing metadata about your copy jobs returned in JSON format.

(structure)

Contains detailed information about a copy job.

AccountId -> (string)

The account ID that owns the copy job.

CopyJobId -> (string)

Uniquely identifies a copy job.

SourceBackupVaultArn -> (string)

An Amazon Resource Name (ARN) that uniquely identifies a source copy vault; for example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault` .

SourceRecoveryPointArn -> (string)

An ARN that uniquely identifies a source recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45` .

DestinationBackupVaultArn -> (string)

An Amazon Resource Name (ARN) that uniquely identifies a destination copy vault; for example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault` .

DestinationRecoveryPointArn -> (string)

An ARN that uniquely identifies a destination recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45` .

ResourceArn -> (string)

The Amazon Web Services resource to be copied; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

CreationDate -> (timestamp)

The date and time a copy job is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CompletionDate -> (timestamp)

The date and time a copy job is completed, in Unix format and Coordinated Universal Time (UTC). The value of `CompletionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

State -> (string)

The current state of a copy job.

StatusMessage -> (string)

A detailed message explaining the status of the job to copy a resource.

BackupSizeInBytes -> (long)

The size, in bytes, of a copy job.

IamRoleArn -> (string)

Specifies the IAM role ARN used to copy the target recovery point; for example, `arn:aws:iam::123456789012:role/S3Access` .

CreatedBy -> (structure)

Contains information about the backup plan and rule that Backup used to initiate the recovery point backup.

BackupPlanId -> (string)

Uniquely identifies a backup plan.

BackupPlanArn -> (string)

An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, `arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50` .

BackupPlanVersion -> (string)

Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.

BackupRuleId -> (string)

Uniquely identifies a rule used to schedule the backup of a selection of resources.

ResourceType -> (string)

The type of Amazon Web Services resource to be copied; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

ParentJobId -> (string)

This uniquely identifies a request to Backup to copy a resource. The return will be the parent (composite) job ID.

IsParent -> (boolean)

This is a boolean value indicating this is a parent (composite) copy job.

CompositeMemberIdentifier -> (string)

The identifier of a resource within a composite group, such as nested (child) recovery point belonging to a composite (parent) stack. The ID is transferred from the [logical ID](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html#resources-section-structure-syntax) within a stack.

NumberOfChildJobs -> (long)

The number of child (nested) copy jobs.

ChildJobsInState -> (map)

This returns the statistics of the included child (nested) copy jobs.

key -> (string)

value -> (long)

ResourceName -> (string)

The non-unique name of the resource that belongs to the specified backup.

MessageCategory -> (string)

This parameter is the job count for the specified message category.

Example strings may include `AccessDenied` , `SUCCESS` , `AGGREGATE_ALL` , and `InvalidParameters` . See [Monitoring](https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html) for a list of MessageCategory strings.

The the value ANY returns count of all message categories.

`AGGREGATE_ALL` aggregates job counts for all message categories and returns the sum

NextToken -> (string)

The next item following a partial list of returned items. For example, if a request is made to return MaxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.