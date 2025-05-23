# copy-db-cluster-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/copy-db-cluster-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/copy-db-cluster-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [docdb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/index.html#cli-aws-docdb) ]

# copy-db-cluster-snapshot

## Description

Copies a snapshot of a cluster.

To copy a cluster snapshot from a shared manual cluster snapshot, `SourceDBClusterSnapshotIdentifier` must be the Amazon Resource Name (ARN) of the shared cluster snapshot. You can only copy a shared DB cluster snapshot, whether encrypted or not, in the same Amazon Web Services Region.

To cancel the copy operation after it is in progress, delete the target cluster snapshot identified by `TargetDBClusterSnapshotIdentifier` while that cluster snapshot is in the *copying* status.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/CopyDBClusterSnapshot)

## Synopsis

```
copy-db-cluster-snapshot
--source-db-cluster-snapshot-identifier <value>
--target-db-cluster-snapshot-identifier <value>
[--kms-key-id <value>]
[--pre-signed-url <value>]
[--copy-tags | --no-copy-tags]
[--tags <value>]
[--source-region <value>]
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

`--source-db-cluster-snapshot-identifier` (string)

The identifier of the cluster snapshot to copy. This parameter is not case sensitive.

Constraints:

- Must specify a valid system snapshot in the *available* state.
- If the source snapshot is in the same Amazon Web Services Region as the copy, specify a valid snapshot identifier.
- If the source snapshot is in a different Amazon Web Services Region than the copy, specify a valid cluster snapshot ARN.

Example: `my-cluster-snapshot1`

`--target-db-cluster-snapshot-identifier` (string)

The identifier of the new cluster snapshot to create from the source cluster snapshot. This parameter is not case sensitive.

Constraints:

- Must contain from 1 to 63 letters, numbers, or hyphens.
- The first character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.

Example: `my-cluster-snapshot2`

`--kms-key-id` (string)

The KMS key ID for an encrypted cluster snapshot. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.

If you copy an encrypted cluster snapshot from your Amazon Web Services account, you can specify a value for `KmsKeyId` to encrypt the copy with a new KMS encryption key. If you donât specify a value for `KmsKeyId` , then the copy of the cluster snapshot is encrypted with the same KMS key as the source cluster snapshot.

If you copy an encrypted cluster snapshot that is shared from another Amazon Web Services account, then you must specify a value for `KmsKeyId` .

To copy an encrypted cluster snapshot to another Amazon Web Services Region, set `KmsKeyId` to the KMS key ID that you want to use to encrypt the copy of the cluster snapshot in the destination Region. KMS encryption keys are specific to the Amazon Web Services Region that they are created in, and you canât use encryption keys from one Amazon Web Services Region in another Amazon Web Services Region.

If you copy an unencrypted cluster snapshot and specify a value for the `KmsKeyId` parameter, an error is returned.

`--pre-signed-url` (string)

The URL that contains a Signature Version 4 signed request for the``CopyDBClusterSnapshot`` API action in the Amazon Web Services Region that contains the source cluster snapshot to copy. You must use the `PreSignedUrl` parameter when copying a cluster snapshot from another Amazon Web Services Region.

If you are using an Amazon Web Services SDK tool or the CLI, you can specify `SourceRegion` (or `--source-region` for the CLI) instead of specifying `PreSignedUrl` manually. Specifying `SourceRegion` autogenerates a pre-signed URL that is a valid request for the operation that can be executed in the source Amazon Web Services Region.

The presigned URL must be a valid request for the `CopyDBClusterSnapshot` API action that can be executed in the source Amazon Web Services Region that contains the cluster snapshot to be copied. The presigned URL request must contain the following parameter values:

- `SourceRegion` - The ID of the region that contains the snapshot to be copied.
- `SourceDBClusterSnapshotIdentifier` - The identifier for the the encrypted cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source Amazon Web Services Region. For example, if you are copying an encrypted cluster snapshot from the us-east-1 Amazon Web Services Region, then your `SourceDBClusterSnapshotIdentifier` looks something like the following: `arn:aws:rds:us-east-1:12345678012:sample-cluster:sample-cluster-snapshot` .
- `TargetDBClusterSnapshotIdentifier` - The identifier for the new cluster snapshot to be created. This parameter isnât case sensitive.

`--copy-tags` | `--no-copy-tags` (boolean)

Set to `true` to copy all tags from the source cluster snapshot to the target cluster snapshot, and otherwise `false` . The default is `false` .

`--tags` (list)

The tags to be assigned to the cluster snapshot.

(structure)

Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

Key -> (string)

The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and canât be prefixed with â`aws:` â or â`rds:` â. The string can contain only the set of Unicode letters, digits, white space, â_â, â.â, â/â, â=â, â+â, â-â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$â).

Value -> (string)

The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and canât be prefixed with â`aws:` â or â`rds:` â. The string can contain only the set of Unicode letters, digits, white space, â_â, â.â, â/â, â=â, â+â, â-â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$â).

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--source-region` (string)

The ID of the region that contains the snapshot to be copied.

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

**To create a copy of a snapshot**

The following `copy-db-cluster-snapshot` example makes a copy of `sample-cluster-snapshot` named `sample-cluster-snapshot-copy`. The copy has all the tags of the original plus a new tag with the key name `CopyNumber`.

```
aws docdb copy-db-cluster-snapshot \
    --source-db-cluster-snapshot-identifier sample-cluster-snapshot \
    --target-db-cluster-snapshot-identifier sample-cluster-snapshot-copy \
    --copy-tags \
    --tags Key="CopyNumber",Value="1"
```

This command produces no output.

For more information, see [Copying a Cluster Snapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup-restore.db-cluster-snapshot-copy.html) in the *Amazon DocumentDB Developer Guide*.

## Output

DBClusterSnapshot -> (structure)

Detailed information about a cluster snapshot.

AvailabilityZones -> (list)

Provides the list of Amazon EC2 Availability Zones that instances in the cluster snapshot can be restored in.

(string)

DBClusterSnapshotIdentifier -> (string)

Specifies the identifier for the cluster snapshot.

DBClusterIdentifier -> (string)

Specifies the cluster identifier of the cluster that this cluster snapshot was created from.

SnapshotCreateTime -> (timestamp)

Provides the time when the snapshot was taken, in UTC.

Engine -> (string)

Specifies the name of the database engine.

Status -> (string)

Specifies the status of this cluster snapshot.

Port -> (integer)

Specifies the port that the cluster was listening on at the time of the snapshot.

VpcId -> (string)

Provides the virtual private cloud (VPC) ID that is associated with the cluster snapshot.

ClusterCreateTime -> (timestamp)

Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).

MasterUsername -> (string)

Provides the master user name for the cluster snapshot.

EngineVersion -> (string)

Provides the version of the database engine for this cluster snapshot.

SnapshotType -> (string)

Provides the type of the cluster snapshot.

PercentProgress -> (integer)

Specifies the percentage of the estimated data that has been transferred.

StorageEncrypted -> (boolean)

Specifies whether the cluster snapshot is encrypted.

KmsKeyId -> (string)

If `StorageEncrypted` is `true` , the KMS key identifier for the encrypted cluster snapshot.

DBClusterSnapshotArn -> (string)

The Amazon Resource Name (ARN) for the cluster snapshot.

SourceDBClusterSnapshotArn -> (string)

If the cluster snapshot was copied from a source cluster snapshot, the ARN for the source cluster snapshot; otherwise, a null value.

StorageType -> (string)

Storage type associated with your cluster snapshot

For information on storage types for Amazon DocumentDB clusters, see Cluster storage configurations in the *Amazon DocumentDB Developer Guide* .

Valid values for storage type - `standard | iopt1`

Default value is `standard`