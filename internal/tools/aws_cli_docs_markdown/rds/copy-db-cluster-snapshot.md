# copy-db-cluster-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-cluster-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-cluster-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# copy-db-cluster-snapshot

## Description

Copies a snapshot of a DB cluster.

To copy a DB cluster snapshot from a shared manual DB cluster snapshot, `SourceDBClusterSnapshotIdentifier` must be the Amazon Resource Name (ARN) of the shared DB cluster snapshot.

You can copy an encrypted DB cluster snapshot from another Amazon Web Services Region. In that case, the Amazon Web Services Region where you call the `CopyDBClusterSnapshot` operation is the destination Amazon Web Services Region for the encrypted DB cluster snapshot to be copied to. To copy an encrypted DB cluster snapshot from another Amazon Web Services Region, you must provide the following values:

- `KmsKeyId` - The Amazon Web Services Key Management System (Amazon Web Services KMS) key identifier for the key to use to encrypt the copy of the DB cluster snapshot in the destination Amazon Web Services Region.
- `TargetDBClusterSnapshotIdentifier` - The identifier for the new copy of the DB cluster snapshot in the destination Amazon Web Services Region.
- `SourceDBClusterSnapshotIdentifier` - The DB cluster snapshot identifier for the encrypted DB cluster snapshot to be copied. This identifier must be in the ARN format for the source Amazon Web Services Region and is the same value as the `SourceDBClusterSnapshotIdentifier` in the presigned URL.

To cancel the copy operation once it is in progress, delete the target DB cluster snapshot identified by `TargetDBClusterSnapshotIdentifier` while that DB cluster snapshot is in âcopyingâ status.

For more information on copying encrypted Amazon Aurora DB cluster snapshots from one Amazon Web Services Region to another, see [Copying a Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CopySnapshot.html) in the *Amazon Aurora User Guide* .

For more information on Amazon Aurora DB clusters, see [What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide* .

For more information on Multi-AZ DB clusters, see [Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/CopyDBClusterSnapshot)

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

The identifier of the DB cluster snapshot to copy. This parameter isnât case-sensitive.

You canât copy an encrypted, shared DB cluster snapshot from one Amazon Web Services Region to another.

Constraints:

- Must specify a valid system snapshot in the âavailableâ state.
- If the source snapshot is in the same Amazon Web Services Region as the copy, specify a valid DB snapshot identifier.
- If the source snapshot is in a different Amazon Web Services Region than the copy, specify a valid DB cluster snapshot ARN. For more information, go to [Copying Snapshots Across Amazon Web Services Regions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CopySnapshot.html#USER_CopySnapshot.AcrossRegions) in the *Amazon Aurora User Guide* .

Example: `my-cluster-snapshot1`

`--target-db-cluster-snapshot-identifier` (string)

The identifier of the new DB cluster snapshot to create from the source DB cluster snapshot. This parameter isnât case-sensitive.

Constraints:

- Must contain from 1 to 63 letters, numbers, or hyphens.
- First character must be a letter.
- Canât end with a hyphen or contain two consecutive hyphens.

Example: `my-cluster-snapshot2`

`--kms-key-id` (string)

The Amazon Web Services KMS key identifier for an encrypted DB cluster snapshot. The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the Amazon Web Services KMS key.

If you copy an encrypted DB cluster snapshot from your Amazon Web Services account, you can specify a value for `KmsKeyId` to encrypt the copy with a new KMS key. If you donât specify a value for `KmsKeyId` , then the copy of the DB cluster snapshot is encrypted with the same KMS key as the source DB cluster snapshot.

If you copy an encrypted DB cluster snapshot that is shared from another Amazon Web Services account, then you must specify a value for `KmsKeyId` .

To copy an encrypted DB cluster snapshot to another Amazon Web Services Region, you must set `KmsKeyId` to the Amazon Web Services KMS key identifier you want to use to encrypt the copy of the DB cluster snapshot in the destination Amazon Web Services Region. KMS keys are specific to the Amazon Web Services Region that they are created in, and you canât use KMS keys from one Amazon Web Services Region in another Amazon Web Services Region.

If you copy an unencrypted DB cluster snapshot and specify a value for the `KmsKeyId` parameter, an error is returned.

`--pre-signed-url` (string)

When you are copying a DB cluster snapshot from one Amazon Web Services GovCloud (US) Region to another, the URL that contains a Signature Version 4 signed request for the `CopyDBClusterSnapshot` API operation in the Amazon Web Services Region that contains the source DB cluster snapshot to copy. Use the `PreSignedUrl` parameter when copying an encrypted DB cluster snapshot from another Amazon Web Services Region. Donât specify `PreSignedUrl` when copying an encrypted DB cluster snapshot in the same Amazon Web Services Region.

This setting applies only to Amazon Web Services GovCloud (US) Regions. Itâs ignored in other Amazon Web Services Regions.

The presigned URL must be a valid request for the `CopyDBClusterSnapshot` API operation that can run in the source Amazon Web Services Region that contains the encrypted DB cluster snapshot to copy. The presigned URL request must contain the following parameter values:

- `KmsKeyId` - The KMS key identifier for the KMS key to use to encrypt the copy of the DB cluster snapshot in the destination Amazon Web Services Region. This is the same identifier for both the `CopyDBClusterSnapshot` operation that is called in the destination Amazon Web Services Region, and the operation contained in the presigned URL.
- `DestinationRegion` - The name of the Amazon Web Services Region that the DB cluster snapshot is to be created in.
- `SourceDBClusterSnapshotIdentifier` - The DB cluster snapshot identifier for the encrypted DB cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source Amazon Web Services Region. For example, if you are copying an encrypted DB cluster snapshot from the us-west-2 Amazon Web Services Region, then your `SourceDBClusterSnapshotIdentifier` looks like the following example: `arn:aws:rds:us-west-2:123456789012:cluster-snapshot:aurora-cluster1-snapshot-20161115` .

To learn how to generate a Signature Version 4 signed request, see [Authenticating Requests: Using Query Parameters (Amazon Web Services Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html) and [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) .

### Note

If you are using an Amazon Web Services SDK tool or the CLI, you can specify `SourceRegion` (or `--source-region` for the CLI) instead of specifying `PreSignedUrl` manually. Specifying `SourceRegion` autogenerates a presigned URL that is a valid request for the operation that can run in the source Amazon Web Services Region.

`--copy-tags` | `--no-copy-tags` (boolean)

Specifies whether to copy all tags from the source DB cluster snapshot to the target DB cluster snapshot. By default, tags are not copied.

`--tags` (list)

A list of tags.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

(structure)

Metadata assigned to an Amazon RDS resource consisting of a key-value pair.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

Key -> (string)

A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

Value -> (string)

A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

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

**To copy a DB cluster snapshot**

The following `copy-db-cluster-snapshot` example creates a copy of a DB cluster snapshot, including its tags.

```
aws rds copy-db-cluster-snapshot \
    --source-db-cluster-snapshot-identifier arn:aws:rds:us-east-1:123456789012:cluster-snapshot:rds:myaurora-2019-06-04-09-16
    --target-db-cluster-snapshot-identifier myclustersnapshotcopy \
    --copy-tags
```

Output:

```
{
    "DBClusterSnapshot": {
        "AvailabilityZones": [
            "us-east-1a",
            "us-east-1b",
            "us-east-1e"
        ],
        "DBClusterSnapshotIdentifier": "myclustersnapshotcopy",
        "DBClusterIdentifier": "myaurora",
        "SnapshotCreateTime": "2019-06-04T09:16:42.649Z",
        "Engine": "aurora-mysql",
        "AllocatedStorage": 0,
        "Status": "available",
        "Port": 0,
        "VpcId": "vpc-6594f31c",
        "ClusterCreateTime": "2019-04-15T14:18:42.785Z",
        "MasterUsername": "myadmin",
        "EngineVersion": "5.7.mysql_aurora.2.04.2",
        "LicenseModel": "aurora-mysql",
        "SnapshotType": "manual",
        "PercentProgress": 100,
        "StorageEncrypted": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE",
        "DBClusterSnapshotArn": "arn:aws:rds:us-east-1:123456789012:cluster-snapshot:myclustersnapshotcopy",
        "IAMDatabaseAuthenticationEnabled": false
    }
}
```

For more information, see [Copying a Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CopySnapshot.html) in the *Amazon Aurora User Guide*.

## Output

DBClusterSnapshot -> (structure)

Contains the details for an Amazon RDS DB cluster snapshot

This data type is used as a response element in the `DescribeDBClusterSnapshots` action.

AvailabilityZones -> (list)

The list of Availability Zones (AZs) where instances in the DB cluster snapshot can be restored.

(string)

DBClusterSnapshotIdentifier -> (string)

The identifier for the DB cluster snapshot.

DBClusterIdentifier -> (string)

The DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.

SnapshotCreateTime -> (timestamp)

The time when the snapshot was taken, in Universal Coordinated Time (UTC).

Engine -> (string)

The name of the database engine for this DB cluster snapshot.

EngineMode -> (string)

The engine mode of the database engine for this DB cluster snapshot.

AllocatedStorage -> (integer)

The allocated storage size of the DB cluster snapshot in gibibytes (GiB).

Status -> (string)

The status of this DB cluster snapshot. Valid statuses are the following:

- `available`
- `copying`
- `creating`

Port -> (integer)

The port that the DB cluster was listening on at the time of the snapshot.

VpcId -> (string)

The VPC ID associated with the DB cluster snapshot.

ClusterCreateTime -> (timestamp)

The time when the DB cluster was created, in Universal Coordinated Time (UTC).

MasterUsername -> (string)

The master username for this DB cluster snapshot.

EngineVersion -> (string)

The version of the database engine for this DB cluster snapshot.

LicenseModel -> (string)

The license model information for this DB cluster snapshot.

SnapshotType -> (string)

The type of the DB cluster snapshot.

PercentProgress -> (integer)

The percentage of the estimated data that has been transferred.

StorageEncrypted -> (boolean)

Indicates whether the DB cluster snapshot is encrypted.

KmsKeyId -> (string)

If `StorageEncrypted` is true, the Amazon Web Services KMS key identifier for the encrypted DB cluster snapshot.

The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

DBClusterSnapshotArn -> (string)

The Amazon Resource Name (ARN) for the DB cluster snapshot.

SourceDBClusterSnapshotArn -> (string)

If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

IAMDatabaseAuthenticationEnabled -> (boolean)

Indicates whether mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled.

TagList -> (list)

A list of tags.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

(structure)

Metadata assigned to an Amazon RDS resource consisting of a key-value pair.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

Key -> (string)

A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

Value -> (string)

A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

DBSystemId -> (string)

Reserved for future use.

StorageType -> (string)

The storage type associated with the DB cluster snapshot.

This setting is only for Aurora DB clusters.

DbClusterResourceId -> (string)

The resource ID of the DB cluster that this DB cluster snapshot was created from.

StorageThroughput -> (integer)

The storage throughput for the DB cluster snapshot. The throughput is automatically set based on the IOPS that you provision, and is not configurable.

This setting is only for non-Aurora Multi-AZ DB clusters.