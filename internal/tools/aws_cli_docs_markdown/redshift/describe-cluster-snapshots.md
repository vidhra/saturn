# describe-cluster-snapshotsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-snapshots.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-snapshots.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/index.html#cli-aws-redshift) ]

# describe-cluster-snapshots

## Description

Returns one or more snapshot objects, which contain metadata about your cluster snapshots. By default, this operation returns information about all snapshots of all clusters that are owned by your Amazon Web Services account. No information is returned for snapshots owned by inactive Amazon Web Services accounts.

If you specify both tag keys and tag values in the same request, Amazon Redshift returns all snapshots that match any combination of the specified keys and values. For example, if you have `owner` and `environment` for tag keys, and `admin` and `test` for tag values, all snapshots that have any combination of those values are returned. Only snapshots that you own are returned in the response; shared snapshots are not returned with the tag key and tag value request parameters.

If both tag keys and values are omitted from the request, snapshots are returned regardless of whether they have tag keys or values associated with them.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterSnapshots)

`describe-cluster-snapshots` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Snapshots`

## Synopsis

```
describe-cluster-snapshots
[--cluster-identifier <value>]
[--snapshot-identifier <value>]
[--snapshot-arn <value>]
[--snapshot-type <value>]
[--start-time <value>]
[--end-time <value>]
[--owner-account <value>]
[--tag-keys <value>]
[--tag-values <value>]
[--cluster-exists | --no-cluster-exists]
[--sorting-entities <value>]
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

`--cluster-identifier` (string)

The identifier of the cluster which generated the requested snapshots.

`--snapshot-identifier` (string)

The snapshot identifier of the snapshot about which to return information.

`--snapshot-arn` (string)

The Amazon Resource Name (ARN) of the snapshot associated with the message to describe cluster snapshots.

`--snapshot-type` (string)

The type of snapshots for which you are requesting information. By default, snapshots of all types are returned.

Valid Values: `automated` | `manual`

`--start-time` (timestamp)

A value that requests only snapshots created at or after the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the [ISO8601 Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)

Example: `2012-07-16T18:00:00Z`

`--end-time` (timestamp)

A time value that requests only snapshots created at or before the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the [ISO8601 Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)

Example: `2012-07-16T18:00:00Z`

`--owner-account` (string)

The Amazon Web Services account used to create or copy the snapshot. Use this field to filter the results to snapshots owned by a particular account. To describe snapshots you own, either specify your Amazon Web Services account, or do not specify the parameter.

`--tag-keys` (list)

A tag key or keys for which you want to return all matching cluster snapshots that are associated with the specified key or keys. For example, suppose that you have snapshots that are tagged with keys called `owner` and `environment` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag keys associated with them.

(string)

Syntax:

```
"string" "string" ...
```

`--tag-values` (list)

A tag value or values for which you want to return all matching cluster snapshots that are associated with the specified tag value or values. For example, suppose that you have snapshots that are tagged with values called `admin` and `test` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag values associated with them.

(string)

Syntax:

```
"string" "string" ...
```

`--cluster-exists` | `--no-cluster-exists` (boolean)

A value that indicates whether to return snapshots only for an existing cluster. You can perform table-level restore only by using a snapshot of an existing cluster, that is, a cluster that has not been deleted. Values for this parameter work as follows:

- If `ClusterExists` is set to `true` , `ClusterIdentifier` is required.
- If `ClusterExists` is set to `false` and `ClusterIdentifier` isnât specified, all snapshots associated with deleted clusters (orphaned snapshots) are returned.
- If `ClusterExists` is set to `false` and `ClusterIdentifier` is specified for a deleted cluster, snapshots associated with that cluster are returned.
- If `ClusterExists` is set to `false` and `ClusterIdentifier` is specified for an existing cluster, no snapshots are returned.

`--sorting-entities` (list)

(structure)

Describes a sorting entity

Attribute -> (string)

The category for sorting the snapshots.

SortOrder -> (string)

The order for listing the attributes.

Shorthand Syntax:

```
Attribute=string,SortOrder=string ...
```

JSON Syntax:

```
[
  {
    "Attribute": "SOURCE_TYPE"|"TOTAL_SIZE"|"CREATE_TIME",
    "SortOrder": "ASC"|"DESC"
  }
  ...
]
```

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

### Get a Description of All Cluster Snapshots

This example returns a description of all cluster snapshots for the
account.  By default, the output is in JSON format.

Command:

```
aws redshift describe-cluster-snapshots
```

Result:

```
{
   "Snapshots": [
      {
         "Status": "available",
         "SnapshotCreateTime": "2013-07-17T22:02:22.852Z",
         "EstimatedSecondsToCompletion": -1,
         "AvailabilityZone": "us-east-1a",
         "ClusterVersion": "1.0",
         "MasterUsername": "adminuser",
         "Encrypted": false,
         "OwnerAccount": "111122223333",
         "BackupProgressInMegabytes": 20.0,
         "ElapsedTimeInSeconds": 0,
         "DBName": "dev",
         "CurrentBackupRateInMegabytesPerSecond: 0.0,
         "ClusterCreateTime": "2013-01-22T21:59:29.559Z",
         "ActualIncrementalBackupSizeInMegabytes"; 20.0
         "SnapshotType": "automated",
         "NodeType": "dw.hs1.xlarge",
         "ClusterIdentifier": "mycluster",
         "Port": 5439,
         "TotalBackupSizeInMegabytes": 20.0,
         "NumberOfNodes": "2",
         "SnapshotIdentifier": "cm:mycluster-2013-01-22-22-04-18"
      },
      {
         "EstimatedSecondsToCompletion": 0,
         "OwnerAccount": "111122223333",
         "CurrentBackupRateInMegabytesPerSecond: 0.1534,
         "ActualIncrementalBackupSizeInMegabytes"; 11.0,
         "NumberOfNodes": "2",
         "Status": "available",
         "ClusterVersion": "1.0",
         "MasterUsername": "adminuser",
         "AccountsWithRestoreAccess": [
            {
               "AccountID": "444455556666"
            } ],
         "TotalBackupSizeInMegabytes": 20.0,
         "DBName": "dev",
         "BackupProgressInMegabytes": 11.0,
         "ClusterCreateTime": "2013-01-22T21:59:29.559Z",
         "ElapsedTimeInSeconds": 0,
         "ClusterIdentifier": "mycluster",
         "SnapshotCreateTime": "2013-07-17T22:04:18.947Z",
         "AvailabilityZone": "us-east-1a",
         "NodeType": "dw.hs1.xlarge",
         "Encrypted": false,
         "SnapshotType": "manual",
         "Port": 5439,
         "SnapshotIdentifier": "my-snapshot-id"
      } ]
   }
   (...remaining output omitted...)
```

## Output

Marker -> (string)

A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.

Snapshots -> (list)

A list of  Snapshot instances.

(structure)

Describes a snapshot.

SnapshotIdentifier -> (string)

The snapshot identifier that is provided in the request.

ClusterIdentifier -> (string)

The identifier of the cluster for which the snapshot was taken.

SnapshotCreateTime -> (timestamp)

The time (in UTC format) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.

Status -> (string)

The snapshot status. The value of the status depends on the API operation used:

- CreateClusterSnapshot and  CopyClusterSnapshot returns status as âcreatingâ.
- DescribeClusterSnapshots returns status as âcreatingâ, âavailableâ, âfinal snapshotâ, or âfailedâ.
- DeleteClusterSnapshot returns status as âdeletedâ.

Port -> (integer)

The port that the cluster is listening on.

AvailabilityZone -> (string)

The Availability Zone in which the cluster was created.

ClusterCreateTime -> (timestamp)

The time (UTC) when the cluster was originally created.

MasterUsername -> (string)

The admin user name for the cluster.

ClusterVersion -> (string)

The version ID of the Amazon Redshift engine that is running on the cluster.

EngineFullVersion -> (string)

The cluster version of the cluster used to create the snapshot. For example, 1.0.15503.

SnapshotType -> (string)

The snapshot type. Snapshots created using  CreateClusterSnapshot and  CopyClusterSnapshot are of type âmanualâ.

NodeType -> (string)

The node type of the nodes in the cluster.

NumberOfNodes -> (integer)

The number of nodes in the cluster.

DBName -> (string)

The name of the database that was created when the cluster was created.

VpcId -> (string)

The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.

Encrypted -> (boolean)

If `true` , the data in the snapshot is encrypted at rest.

KmsKeyId -> (string)

The Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.

EncryptedWithHSM -> (boolean)

A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. `true` indicates that the data is encrypted using HSM keys.

AccountsWithRestoreAccess -> (list)

A list of the Amazon Web Services accounts authorized to restore the snapshot. Returns `null` if no accounts are authorized. Visible only to the snapshot owner.

(structure)

Describes an Amazon Web Services account authorized to restore a snapshot.

AccountId -> (string)

The identifier of an Amazon Web Services account authorized to restore a snapshot.

AccountAlias -> (string)

The identifier of an Amazon Web Services support account authorized to restore a snapshot. For Amazon Web Services Support, the identifier is `amazon-redshift-support` .

OwnerAccount -> (string)

For manual snapshots, the Amazon Web Services account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.

TotalBackupSizeInMegaBytes -> (double)

The size of the complete set of backup data that would be used to restore the cluster.

ActualIncrementalBackupSizeInMegaBytes -> (double)

The size of the incremental backup.

BackupProgressInMegaBytes -> (double)

The number of megabytes that have been transferred to the snapshot backup.

CurrentBackupRateInMegaBytesPerSecond -> (double)

The number of megabytes per second being transferred to the snapshot backup. Returns `0` for a completed backup.

EstimatedSecondsToCompletion -> (long)

The estimate of the time remaining before the snapshot backup will complete. Returns `0` for a completed backup.

ElapsedTimeInSeconds -> (long)

The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.

SourceRegion -> (string)

The source region from which the snapshot was copied.

Tags -> (list)

The list of tags for the cluster snapshot.

(structure)

A tag consisting of a name/value pair for a resource.

Key -> (string)

The key, or name, for the resource tag.

Value -> (string)

The value for the resource tag.

RestorableNodeTypes -> (list)

The list of node types that this cluster snapshot is able to restore into.

(string)

EnhancedVpcRouting -> (boolean)

An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see [Enhanced VPC Routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html) in the Amazon Redshift Cluster Management Guide.

If this option is `true` , enhanced VPC routing is enabled.

Default: false

MaintenanceTrackName -> (string)

The name of the maintenance track for the snapshot.

ManualSnapshotRetentionPeriod -> (integer)

The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.

The value must be either -1 or an integer between 1 and 3,653.

ManualSnapshotRemainingDays -> (integer)

The number of days until a manual snapshot will pass its retention period.

SnapshotRetentionStartTime -> (timestamp)

A timestamp representing the start of the retention period for the snapshot.

MasterPasswordSecretArn -> (string)

The Amazon Resource Name (ARN) for the clusterâs admin user credentials secret.

MasterPasswordSecretKmsKeyId -> (string)

The ID of the Key Management Service (KMS) key used to encrypt and store the clusterâs admin credentials secret.

SnapshotArn -> (string)

The Amazon Resource Name (ARN) of the snapshot.