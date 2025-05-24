# modify-cluster-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/index.html#cli-aws-redshift) ]

# modify-cluster-snapshot

## Description

Modifies the settings for a snapshot.

This exanmple modifies the manual retention period setting for a cluster snapshot.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/ModifyClusterSnapshot)

## Synopsis

```
modify-cluster-snapshot
--snapshot-identifier <value>
[--manual-snapshot-retention-period <value>]
[--force | --no-force]
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

`--snapshot-identifier` (string)

The identifier of the snapshot whose setting you want to modify.

`--manual-snapshot-retention-period` (integer)

The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.

If the manual snapshot falls outside of the new retention period, you can specify the force option to immediately delete the snapshot.

The value must be either -1 or an integer between 1 and 3,653.

`--force` | `--no-force` (boolean)

A Boolean option to override an exception if the retention period has already passed.

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

**To modify cluster snapshot**

The following `modify-cluster-snapshot` example sets the manual retention period setting for the specified cluster snapshot to value of 10 days.

```
aws redshift modify-cluster-snapshot \
    --snapshot-identifier mycluster-2019-11-06-16-32 \
    --manual-snapshot-retention-period 10
```

Output:

```
{
    "Snapshot": {
        "SnapshotIdentifier": "mycluster-2019-11-06-16-32",
        "ClusterIdentifier": "mycluster",
        "SnapshotCreateTime": "2019-12-07T00:34:05.633Z",
        "Status": "available",
        "Port": 5439,
        "AvailabilityZone": "us-west-2f",
        "ClusterCreateTime": "2019-12-05T18:44:36.991Z",
        "MasterUsername": "adminuser",
        "ClusterVersion": "1.0",
        "SnapshotType": "manual",
        "NodeType": "dc2.large",
        "NumberOfNodes": 2,
        "DBName": "dev",
        "VpcId": "vpc-b1cel7t9",
        "Encrypted": false,
        "EncryptedWithHSM": false,
        "OwnerAccount": "123456789012",
        "TotalBackupSizeInMegaBytes": 64384.0,
        "ActualIncrementalBackupSizeInMegaBytes": 24.0,
        "BackupProgressInMegaBytes": 24.0,
        "CurrentBackupRateInMegaBytesPerSecond": 13.0011,
        "EstimatedSecondsToCompletion": 0,
        "ElapsedTimeInSeconds": 1,
        "Tags": [
            {
                "Key": "mytagkey",
                "Value": "mytagvalue"
            }
        ],
        "EnhancedVpcRouting": false,
        "MaintenanceTrackName": "current",
        "ManualSnapshotRetentionPeriod": 10,
        "ManualSnapshotRemainingDays": 6,
        "SnapshotRetentionStartTime": "2019-12-07T00:34:07.479Z"
    }
}
```

For more information, see [Amazon Redshift Snapshots](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html) in the *Amazon Redshift Cluster Management Guide*.

## Output

Snapshot -> (structure)

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