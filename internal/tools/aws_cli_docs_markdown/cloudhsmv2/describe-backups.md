# describe-backupsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/describe-backups.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/describe-backups.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudhsmv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/index.html#cli-aws-cloudhsmv2) ]

# describe-backups

## Description

Gets information about backups of CloudHSM clusters. Lists either the backups you own or the backups shared with you when the Shared parameter is true.

This is a paginated operation, which means that each response might contain only a subset of all the backups. When the response contains only a subset of backups, it includes a `NextToken` value. Use this value in a subsequent `DescribeBackups` request to get more backups. When you receive a response with no `NextToken` (or an empty or null value), that means there are no more backups to get.

**Cross-account use:** Yes. Customers can describe backups in other Amazon Web Services accounts that are shared with them.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/DescribeBackups)

`describe-backups` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Backups`

## Synopsis

```
describe-backups
[--filters <value>]
[--shared | --no-shared]
[--sort-ascending | --no-sort-ascending]
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

`--filters` (map)

One or more filters to limit the items returned in the response.

Use the `backupIds` filter to return only the specified backups. Specify backups by their backup identifier (ID).

Use the `sourceBackupIds` filter to return only the backups created from a source backup. The `sourceBackupID` of a source backup is returned by the  CopyBackupToRegion operation.

Use the `clusterIds` filter to return only the backups for the specified clusters. Specify clusters by their cluster identifier (ID).

Use the `states` filter to return only backups that match the specified state.

Use the `neverExpires` filter to return backups filtered by the value in the `neverExpires` parameter. `True` returns all backups exempt from the backup retention policy. `False` returns all backups with a backup retention policy defined at the cluster.

key -> (string)

value -> (list)

(string)

Shorthand Syntax:

```
KeyName1=string,string,KeyName2=string,string
```

JSON Syntax:

```
{"string": ["string", ...]
  ...}
```

`--shared` | `--no-shared` (boolean)

Describe backups that are shared with you.

### Note

By default when using this option, the command returns backups that have been shared using a standard Resource Access Manager resource share. In order for a backup that was shared using the PutResourcePolicy command to be returned, the share must be promoted to a standard resource share using the RAM [PromoteResourceShareCreatedFromPolicy](https://docs.aws.amazon.com/cli/latest/reference/ram/promote-resource-share-created-from-policy.html) API operation. For more information about sharing backups, see [Working with shared backups](https://docs.aws.amazon.com/cloudhsm/latest/userguide/sharing.html) in the CloudHSM User Guide.

`--sort-ascending` | `--no-sort-ascending` (boolean)

Designates whether or not to sort the return backups by ascending chronological order of generation.

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

Backups -> (list)

A list of backups.

(structure)

Contains information about a backup of an CloudHSM cluster. All backup objects contain the `BackupId` , `BackupState` , `ClusterId` , and `CreateTimestamp` parameters. Backups that were copied into a destination region additionally contain the `CopyTimestamp` , `SourceBackup` , `SourceCluster` , and `SourceRegion` parameters. A backup that is pending deletion will include the `DeleteTimestamp` parameter.

BackupId -> (string)

The identifier (ID) of the backup.

BackupArn -> (string)

The Amazon Resource Name (ARN) of the backup.

BackupState -> (string)

The state of the backup.

ClusterId -> (string)

The identifier (ID) of the cluster that was backed up.

CreateTimestamp -> (timestamp)

The date and time when the backup was created.

CopyTimestamp -> (timestamp)

The date and time when the backup was copied from a source backup.

NeverExpires -> (boolean)

Specifies whether the service should exempt a backup from the retention policy for the cluster. `True` exempts a backup from the retention policy. `False` means the service applies the backup retention policy defined at the cluster.

SourceRegion -> (string)

The AWS Region that contains the source backup from which the new backup was copied.

SourceBackup -> (string)

The identifier (ID) of the source backup from which the new backup was copied.

SourceCluster -> (string)

The identifier (ID) of the cluster containing the source backup from which the new backup was copied.

DeleteTimestamp -> (timestamp)

The date and time when the backup will be permanently deleted.

TagList -> (list)

The list of tags for the backup.

(structure)

Contains a tag. A tag is a key-value pair.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.

HsmType -> (string)

The HSM type used to create the backup.

Mode -> (string)

The mode of the cluster that was backed up.

NextToken -> (string)

An opaque string that indicates that the response contains only a subset of backups. Use this value in a subsequent `DescribeBackups` request to get more backups.