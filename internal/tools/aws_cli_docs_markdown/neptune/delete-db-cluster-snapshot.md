# delete-db-cluster-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-db-cluster-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-db-cluster-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptune](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/index.html#cli-aws-neptune) ]

# delete-db-cluster-snapshot

## Description

Deletes a DB cluster snapshot. If the snapshot is being copied, the copy operation is terminated.

### Note

The DB cluster snapshot must be in the `available` state to be deleted.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DeleteDBClusterSnapshot)

## Synopsis

```
delete-db-cluster-snapshot
--db-cluster-snapshot-identifier <value>
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

`--db-cluster-snapshot-identifier` (string)

The identifier of the DB cluster snapshot to delete.

Constraints: Must be the name of an existing DB cluster snapshot in the `available` state.

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

DBClusterSnapshot -> (structure)

Contains the details for an Amazon Neptune DB cluster snapshot

This data type is used as a response element in the  DescribeDBClusterSnapshots action.

AvailabilityZones -> (list)

Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.

(string)

DBClusterSnapshotIdentifier -> (string)

Specifies the identifier for a DB cluster snapshot. Must match the identifier of an existing snapshot.

After you restore a DB cluster using a `DBClusterSnapshotIdentifier` , you must specify the same `DBClusterSnapshotIdentifier` for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed.

However, if you donât specify the `DBClusterSnapshotIdentifier` , an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the snapshot specified by the `DBClusterSnapshotIdentifier` , and the original DB cluster is deleted.

DBClusterIdentifier -> (string)

Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.

SnapshotCreateTime -> (timestamp)

Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

Engine -> (string)

Specifies the name of the database engine.

AllocatedStorage -> (integer)

Specifies the allocated storage size in gibibytes (GiB).

Status -> (string)

Specifies the status of this DB cluster snapshot.

Port -> (integer)

Specifies the port that the DB cluster was listening on at the time of the snapshot.

VpcId -> (string)

Provides the VPC ID associated with the DB cluster snapshot.

ClusterCreateTime -> (timestamp)

Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

MasterUsername -> (string)

Not supported by Neptune.

EngineVersion -> (string)

Provides the version of the database engine for this DB cluster snapshot.

LicenseModel -> (string)

Provides the license model information for this DB cluster snapshot.

SnapshotType -> (string)

Provides the type of the DB cluster snapshot.

PercentProgress -> (integer)

Specifies the percentage of the estimated data that has been transferred.

StorageEncrypted -> (boolean)

Specifies whether the DB cluster snapshot is encrypted.

KmsKeyId -> (string)

If `StorageEncrypted` is true, the Amazon KMS key identifier for the encrypted DB cluster snapshot.

DBClusterSnapshotArn -> (string)

The Amazon Resource Name (ARN) for the DB cluster snapshot.

SourceDBClusterSnapshotArn -> (string)

If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

IAMDatabaseAuthenticationEnabled -> (boolean)

True if mapping of Amazon Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.

StorageType -> (string)

The storage type associated with the DB cluster snapshot.