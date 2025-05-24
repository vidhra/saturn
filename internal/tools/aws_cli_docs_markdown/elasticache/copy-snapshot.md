# copy-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/copy-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/copy-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/index.html#cli-aws-elasticache) ]

# copy-snapshot

## Description

Makes a copy of an existing snapshot.

### Note

This operation is valid for Valkey or Redis OSS only.

### Warning

Users or groups that have permissions to use the `CopySnapshot` operation can create their own Amazon S3 buckets and copy snapshots to it. To control access to your snapshots, use an IAM policy to control who has the ability to use the `CopySnapshot` operation. For more information about using IAM to control the use of ElastiCache operations, see [Exporting Snapshots](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html) and [Authentication & Access Control](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/IAM.html) .

You could receive the following error messages.

**Error Messages**

- **Error Message:** The S3 bucket %s is outside of the region.  **Solution:** Create an Amazon S3 bucket in the same region as your snapshot. For more information, see [Step 1: Create an Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-create-s3-bucket) in the ElastiCache User Guide.
- **Error Message:** The S3 bucket %s does not exist.  **Solution:** Create an Amazon S3 bucket in the same region as your snapshot. For more information, see [Step 1: Create an Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-create-s3-bucket) in the ElastiCache User Guide.
- **Error Message:** The S3 bucket %s is not owned by the authenticated user.  **Solution:** Create an Amazon S3 bucket in the same region as your snapshot. For more information, see [Step 1: Create an Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-create-s3-bucket) in the ElastiCache User Guide.
- **Error Message:** The authenticated user does not have sufficient permissions to perform the desired activity.  **Solution:** Contact your system administrator to get the needed permissions.
- **Error Message:** The S3 bucket %s already contains an object with key %s.  **Solution:** Give the `TargetSnapshotName` a new and unique value. If exporting a snapshot, you could alternatively create a new Amazon S3 bucket and use this same value for `TargetSnapshotName` .
- **Error Message:** ElastiCache has not been granted READ permissions %s on the S3 Bucket.  **Solution:** Add List and Read permissions on the bucket. For more information, see [Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-grant-access) in the ElastiCache User Guide.
- **Error Message:** ElastiCache has not been granted WRITE permissions %s on the S3 Bucket.  **Solution:** Add Upload/Delete permissions on the bucket. For more information, see [Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-grant-access) in the ElastiCache User Guide.
- **Error Message:** ElastiCache has not been granted READ_ACP permissions %s on the S3 Bucket.  **Solution:** Add View Permissions on the bucket. For more information, see [Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-grant-access) in the ElastiCache User Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CopySnapshot)

## Synopsis

```
copy-snapshot
--source-snapshot-name <value>
--target-snapshot-name <value>
[--target-bucket <value>]
[--kms-key-id <value>]
[--tags <value>]
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

`--source-snapshot-name` (string)

The name of an existing snapshot from which to make a copy.

`--target-snapshot-name` (string)

A name for the snapshot copy. ElastiCache does not permit overwriting a snapshot, therefore this name must be unique within its context - ElastiCache or an Amazon S3 bucket if exporting.

`--target-bucket` (string)

The Amazon S3 bucket to which the snapshot is exported. This parameter is used only when exporting a snapshot for external access.

When using this parameter to export a snapshot, be sure Amazon ElastiCache has the needed permissions to this S3 bucket. For more information, see [Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-grant-access) in the *Amazon ElastiCache User Guide* .

For more information, see [Exporting a Snapshot](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html) in the *Amazon ElastiCache User Guide* .

`--kms-key-id` (string)

The ID of the KMS key used to encrypt the target snapshot.

`--tags` (list)

A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.

(structure)

A tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your ElastiCache resources, with the exception of global replication group. When you add or remove tags on replication groups, those actions will be replicated to all nodes in the replication group. A tag with a null Value is permitted.

Key -> (string)

The key for the tag. May not be null.

Value -> (string)

The tagâs value. May be null.

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

**To copy a snapshot**

The following `copy-snapshot` example makes a copy of an existing snapshot.

```
aws elasticache copy-snapshot \
    --source-snapshot-name "my-snapshot" \
    --target-snapshot-name "my-snapshot-copy"
```

Output:

```
{
    "Snapshot":{
        "Engine": "redis",
        "CacheParameterGroupName": "default.redis3.2",
        "VpcId": "vpc-3820329f3",
        "CacheClusterId": "my-redis4",
        "SnapshotRetentionLimit": 7,
        "NumCacheNodes": 1,
        "SnapshotName": "my-snapshot-copy",
        "CacheClusterCreateTime": "2016-12-21T22:24:04.955Z",
        "AutoMinorVersionUpgrade": true,
        "PreferredAvailabilityZone": "us-east-1c",
        "SnapshotStatus": "creating",
        "SnapshotSource": "manual",
        "SnapshotWindow": "07:00-08:00",
        "EngineVersion": "3.2.4",
        "NodeSnapshots": [
            {
                "CacheSize": "3 MB",
                "SnapshotCreateTime": "2016-12-28T07:00:52Z",
                "CacheNodeId": "0001",
                "CacheNodeCreateTime": "2016-12-21T22:24:04.955Z"
            }
        ],
        "CacheSubnetGroupName": "default",
        "Port": 6379,
        "PreferredMaintenanceWindow": "tue:09:30-tue:10:30",
        "CacheNodeType": "cache.m3.large"
    }
}
```

For more information, see [Exporting a Backup](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups-exporting.html) in the *Elasticache User Guide*.

## Output

Snapshot -> (structure)

Represents a copy of an entire Valkey or Redis OSS cluster as of the time when the snapshot was taken.

SnapshotName -> (string)

The name of a snapshot. For an automatic snapshot, the name is system-generated. For a manual snapshot, this is the user-provided name.

ReplicationGroupId -> (string)

The unique identifier of the source replication group.

ReplicationGroupDescription -> (string)

A description of the source replication group.

CacheClusterId -> (string)

The user-supplied identifier of the source cluster.

SnapshotStatus -> (string)

The status of the snapshot. Valid values: `creating` | `available` | `restoring` | `copying` | `deleting` .

SnapshotSource -> (string)

Indicates whether the snapshot is from an automatic backup (`automated` ) or was created manually (`manual` ).

CacheNodeType -> (string)

The name of the compute and memory capacity node type for the source cluster.

The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

- General purpose:

- Current generation:   **M7g node types** : `cache.m7g.large` , `cache.m7g.xlarge` , `cache.m7g.2xlarge` , `cache.m7g.4xlarge` , `cache.m7g.8xlarge` , `cache.m7g.12xlarge` , `cache.m7g.16xlarge`

### Note

For region availability, see [Supported Node Types](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion)

**M6g node types** (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): `cache.m6g.large` , `cache.m6g.xlarge` , `cache.m6g.2xlarge` , `cache.m6g.4xlarge` , `cache.m6g.8xlarge` , `cache.m6g.12xlarge` , `cache.m6g.16xlarge` **M5 node types:** `cache.m5.large` , `cache.m5.xlarge` , `cache.m5.2xlarge` , `cache.m5.4xlarge` , `cache.m5.12xlarge` , `cache.m5.24xlarge` **M4 node types:** `cache.m4.large` , `cache.m4.xlarge` , `cache.m4.2xlarge` , `cache.m4.4xlarge` , `cache.m4.10xlarge` **T4g node types** (available only for Redis OSS engine version 5.0.6 onward and Memcached engine version 1.5.16 onward): `cache.t4g.micro` , `cache.t4g.small` , `cache.t4g.medium` **T3 node types:** `cache.t3.micro` , `cache.t3.small` , `cache.t3.medium` **T2 node types:** `cache.t2.micro` , `cache.t2.small` , `cache.t2.medium`

- Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)  **T1 node types:** `cache.t1.micro` **M1 node types:** `cache.m1.small` , `cache.m1.medium` , `cache.m1.large` , `cache.m1.xlarge` **M3 node types:** `cache.m3.medium` , `cache.m3.large` , `cache.m3.xlarge` , `cache.m3.2xlarge`
- Compute optimized:

- Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)  **C1 node types:** `cache.c1.xlarge`
- Memory optimized:

- Current generation:   **R7g node types** : `cache.r7g.large` , `cache.r7g.xlarge` , `cache.r7g.2xlarge` , `cache.r7g.4xlarge` , `cache.r7g.8xlarge` , `cache.r7g.12xlarge` , `cache.r7g.16xlarge`

### Note

For region availability, see [Supported Node Types](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion)

**R6g node types** (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): `cache.r6g.large` , `cache.r6g.xlarge` , `cache.r6g.2xlarge` , `cache.r6g.4xlarge` , `cache.r6g.8xlarge` , `cache.r6g.12xlarge` , `cache.r6g.16xlarge` **R5 node types:** `cache.r5.large` , `cache.r5.xlarge` , `cache.r5.2xlarge` , `cache.r5.4xlarge` , `cache.r5.12xlarge` , `cache.r5.24xlarge` **R4 node types:** `cache.r4.large` , `cache.r4.xlarge` , `cache.r4.2xlarge` , `cache.r4.4xlarge` , `cache.r4.8xlarge` , `cache.r4.16xlarge`

- Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)  **M2 node types:** `cache.m2.xlarge` , `cache.m2.2xlarge` , `cache.m2.4xlarge` **R3 node types:** `cache.r3.large` , `cache.r3.xlarge` , `cache.r3.2xlarge` , `cache.r3.4xlarge` , `cache.r3.8xlarge`

**Additional node type info**

- All current generation instance types are created in Amazon VPC by default.
- Valkey or Redis OSS append-only files (AOF) are not supported for T1 or T2 instances.
- Valkey or Redis OSS Multi-AZ with automatic failover is not supported on T1 instances.
- The configuration variables `appendonly` and `appendfsync` are not supported on Valkey, or on Redis OSS version 2.8.22 and later.

Engine -> (string)

The name of the cache engine (`memcached` or `redis` ) used by the source cluster.

EngineVersion -> (string)

The version of the cache engine version that is used by the source cluster.

NumCacheNodes -> (integer)

The number of cache nodes in the source cluster.

For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.

PreferredAvailabilityZone -> (string)

The name of the Availability Zone in which the source cluster is located.

PreferredOutpostArn -> (string)

The ARN (Amazon Resource Name) of the preferred outpost.

CacheClusterCreateTime -> (timestamp)

The date and time when the source cluster was created.

PreferredMaintenanceWindow -> (string)

Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

Valid values for `ddd` are:

- `sun`
- `mon`
- `tue`
- `wed`
- `thu`
- `fri`
- `sat`

Example: `sun:23:00-mon:01:30`

TopicArn -> (string)

The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing notifications.

Port -> (integer)

The port number used by each cache nodes in the source cluster.

CacheParameterGroupName -> (string)

The cache parameter group that is associated with the source cluster.

CacheSubnetGroupName -> (string)

The name of the cache subnet group associated with the source cluster.

VpcId -> (string)

The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cluster.

AutoMinorVersionUpgrade -> (boolean)

If you are running Valkey 7.2 and above or Redis OSS engine version 6.0 and above, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions.

SnapshotRetentionLimit -> (integer)

For an automatic snapshot, the number of days for which ElastiCache retains the snapshot before deleting it.

For manual snapshots, this field reflects the `SnapshotRetentionLimit` for the source cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the `DeleteSnapshot` operation.

**Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

SnapshotWindow -> (string)

The daily time range during which ElastiCache takes daily snapshots of the source cluster.

NumNodeGroups -> (integer)

The number of node groups (shards) in this snapshot. When restoring from a snapshot, the number of node groups (shards) in the snapshot and in the restored replication group must be the same.

AutomaticFailover -> (string)

Indicates the status of automatic failover for the source Valkey or Redis OSS replication group.

NodeSnapshots -> (list)

A list of the cache nodes in the source cluster.

(structure)

Represents an individual cache node in a snapshot of a cluster.

CacheClusterId -> (string)

A unique identifier for the source cluster.

NodeGroupId -> (string)

A unique identifier for the source node group (shard).

CacheNodeId -> (string)

The cache node identifier for the node in the source cluster.

NodeGroupConfiguration -> (structure)

The configuration for the source node group (shard).

NodeGroupId -> (string)

Either the ElastiCache supplied 4-digit id or a user supplied id for the node group these configuration values apply to.

Slots -> (string)

A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format `startkey-endkey` .

Example: `"0-3999"`

ReplicaCount -> (integer)

The number of read replica nodes in this node group (shard).

PrimaryAvailabilityZone -> (string)

The Availability Zone where the primary node of this node group (shard) is launched.

ReplicaAvailabilityZones -> (list)

A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of `ReplicaCount` or `ReplicasPerNodeGroup` if not specified.

(string)

PrimaryOutpostArn -> (string)

The outpost ARN of the primary node.

ReplicaOutpostArns -> (list)

The outpost ARN of the node replicas.

(string)

CacheSize -> (string)

The size of the cache on the source cache node.

CacheNodeCreateTime -> (timestamp)

The date and time when the cache node was created in the source cluster.

SnapshotCreateTime -> (timestamp)

The date and time when the source nodeâs metadata and cache data set was obtained for the snapshot.

KmsKeyId -> (string)

The ID of the KMS key used to encrypt the snapshot.

ARN -> (string)

The ARN (Amazon Resource Name) of the snapshot.

DataTiering -> (string)

Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see [Data tiering](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/data-tiering.html) .