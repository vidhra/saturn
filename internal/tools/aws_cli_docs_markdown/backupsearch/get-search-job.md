# get-search-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backupsearch/get-search-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backupsearch/get-search-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [backupsearch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backupsearch/index.html#cli-aws-backupsearch) ]

# get-search-job

## Description

This operation retrieves metadata of a search job, including its progress.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/backupsearch-2018-05-10/GetSearchJob)

## Synopsis

```
get-search-job
--search-job-identifier <value>
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

`--search-job-identifier` (string)

Required unique string that specifies the search job.

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

Name -> (string)

Returned name of the specified search job.

SearchScopeSummary -> (structure)

Returned summary of the specified search job scope, including:

- TotalBackupsToScanCount, the number of recovery points returned by the search.
- TotalItemsToScanCount, the number of items returned by the search.

TotalRecoveryPointsToScanCount -> (integer)

This is the count of the total number of backups that will be scanned in a search.

TotalItemsToScanCount -> (long)

This is the count of the total number of items that will be scanned in a search.

CurrentSearchProgress -> (structure)

Returns numbers representing BackupsScannedCount, ItemsScanned, and ItemsMatched.

RecoveryPointsScannedCount -> (integer)

This number is the sum of all backups that have been scanned so far during a search job.

ItemsScannedCount -> (long)

This number is the sum of all items that have been scanned so far during a search job.

ItemsMatchedCount -> (long)

This number is the sum of all items that match the item filters in a search job in progress.

StatusMessage -> (string)

A status message will be returned for either a earch job with a status of `ERRORED` or a status of `COMPLETED` jobs with issues.

For example, a message may say that a search contained recovery points unable to be scanned because of a permissions issue.

EncryptionKeyArn -> (string)

The encryption key for the specified search job.

Example: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab` .

CompletionTime -> (timestamp)

The date and time that a search job completed, in Unix format and Coordinated Universal Time (UTC). The value of `CompletionTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

Status -> (string)

The current status of the specified search job.

A search job may have one of the following statuses: `RUNNING` ; `COMPLETED` ; `STOPPED` ; `FAILED` ; `TIMED_OUT` ; or `EXPIRED` .

SearchScope -> (structure)

The search scope is all backup properties input into a search.

BackupResourceTypes -> (list)

The resource types included in a search.

Eligible resource types include S3 and EBS.

(string)

BackupResourceCreationTime -> (structure)

This is the time a backup resource was created.

CreatedAfter -> (timestamp)

This timestamp includes recovery points only created after the specified time.

CreatedBefore -> (timestamp)

This timestamp includes recovery points only created before the specified time.

SourceResourceArns -> (list)

The Amazon Resource Name (ARN) that uniquely identifies the source resources.

(string)

BackupResourceArns -> (list)

The Amazon Resource Name (ARN) that uniquely identifies the backup resources.

(string)

BackupResourceTags -> (map)

These are one or more tags on the backup (recovery point).

key -> (string)

value -> (string)

ItemFilters -> (structure)

Item Filters represent all input item properties specified when the search was created.

S3ItemFilters -> (list)

This array can contain CreationTimes, ETags, ObjectKeys, Sizes, or VersionIds objects.

(structure)

This contains arrays of objects, which may include ObjectKeys, Sizes, CreationTimes, VersionIds, and/or Etags.

ObjectKeys -> (list)

You can include 1 to 10 values.

If one value is included, the results will return only items that match the value.

If more than one value is included, the results will return all items that match any of the values.

(structure)

This contains the value of the string and can contain one or more operators.

Value -> (string)

The value of the string.

Operator -> (string)

A string that defines what values will be returned.

If this is included, avoid combinations of operators that will return all possible values. For example, including both `EQUALS_TO` and `NOT_EQUALS_TO` with a value of `4` will return all values.

Sizes -> (list)

You can include 1 to 10 values.

If one value is included, the results will return only items that match the value.

If more than one value is included, the results will return all items that match any of the values.

(structure)

The long condition contains a `Value` and can optionally contain an `Operator` .

Value -> (long)

The value of an item included in one of the search item filters.

Operator -> (string)

A string that defines what values will be returned.

If this is included, avoid combinations of operators that will return all possible values. For example, including both `EQUALS_TO` and `NOT_EQUALS_TO` with a value of `4` will return all values.

CreationTimes -> (list)

You can include 1 to 10 values.

If one value is included, the results will return only items that match the value.

If more than one value is included, the results will return all items that match any of the values.

(structure)

A time condition denotes a creation time, last modification time, or other time.

Value -> (timestamp)

This is the timestamp value of the time condition.

Operator -> (string)

A string that defines what values will be returned.

If this is included, avoid combinations of operators that will return all possible values. For example, including both `EQUALS_TO` and `NOT_EQUALS_TO` with a value of `4` will return all values.

VersionIds -> (list)

You can include 1 to 10 values.

If one value is included, the results will return only items that match the value.

If more than one value is included, the results will return all items that match any of the values.

(structure)

This contains the value of the string and can contain one or more operators.

Value -> (string)

The value of the string.

Operator -> (string)

A string that defines what values will be returned.

If this is included, avoid combinations of operators that will return all possible values. For example, including both `EQUALS_TO` and `NOT_EQUALS_TO` with a value of `4` will return all values.

ETags -> (list)

You can include 1 to 10 values.

If one value is included, the results will return only items that match the value.

If more than one value is included, the results will return all items that match any of the values.

(structure)

This contains the value of the string and can contain one or more operators.

Value -> (string)

The value of the string.

Operator -> (string)

A string that defines what values will be returned.

If this is included, avoid combinations of operators that will return all possible values. For example, including both `EQUALS_TO` and `NOT_EQUALS_TO` with a value of `4` will return all values.

EBSItemFilters -> (list)

This array can contain CreationTimes, FilePaths, LastModificationTimes, or Sizes objects.

(structure)

This contains arrays of objects, which may include CreationTimes time condition objects, FilePaths string objects, LastModificationTimes time condition objects,

FilePaths -> (list)

You can include 1 to 10 values.

If one file path is included, the results will return only items that match the file path.

If more than one file path is included, the results will return all items that match any of the file paths.

(structure)

This contains the value of the string and can contain one or more operators.

Value -> (string)

The value of the string.

Operator -> (string)

A string that defines what values will be returned.

If this is included, avoid combinations of operators that will return all possible values. For example, including both `EQUALS_TO` and `NOT_EQUALS_TO` with a value of `4` will return all values.

Sizes -> (list)

You can include 1 to 10 values.

If one is included, the results will return only items that match.

If more than one is included, the results will return all items that match any of the included values.

(structure)

The long condition contains a `Value` and can optionally contain an `Operator` .

Value -> (long)

The value of an item included in one of the search item filters.

Operator -> (string)

A string that defines what values will be returned.

If this is included, avoid combinations of operators that will return all possible values. For example, including both `EQUALS_TO` and `NOT_EQUALS_TO` with a value of `4` will return all values.

CreationTimes -> (list)

You can include 1 to 10 values.

If one is included, the results will return only items that match.

If more than one is included, the results will return all items that match any of the included values.

(structure)

A time condition denotes a creation time, last modification time, or other time.

Value -> (timestamp)

This is the timestamp value of the time condition.

Operator -> (string)

A string that defines what values will be returned.

If this is included, avoid combinations of operators that will return all possible values. For example, including both `EQUALS_TO` and `NOT_EQUALS_TO` with a value of `4` will return all values.

LastModificationTimes -> (list)

You can include 1 to 10 values.

If one is included, the results will return only items that match.

If more than one is included, the results will return all items that match any of the included values.

(structure)

A time condition denotes a creation time, last modification time, or other time.

Value -> (timestamp)

This is the timestamp value of the time condition.

Operator -> (string)

A string that defines what values will be returned.

If this is included, avoid combinations of operators that will return all possible values. For example, including both `EQUALS_TO` and `NOT_EQUALS_TO` with a value of `4` will return all values.

CreationTime -> (timestamp)

The date and time that a search job was created, in Unix format and Coordinated Universal Time (UTC). The value of `CompletionTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

SearchJobIdentifier -> (string)

The unique string that identifies the specified search job.

SearchJobArn -> (string)

The unique string that identifies the Amazon Resource Name (ARN) of the specified search job.