# create-replication-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-replication-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-replication-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/index.html#cli-aws-elasticache) ]

# create-replication-group

## Description

Creates a Valkey or Redis OSS (cluster mode disabled) or a Valkey or Redis OSS (cluster mode enabled) replication group.

This API can be used to create a standalone regional replication group or a secondary replication group associated with a Global datastore.

A Valkey or Redis OSS (cluster mode disabled) replication group is a collection of nodes, where one of the nodes is a read/write primary and the others are read-only replicas. Writes to the primary are asynchronously propagated to the replicas.

A Valkey or Redis OSS cluster-mode enabled cluster is comprised of from 1 to 90 shards (API/CLI: node groups). Each shard has a primary node and up to 5 read-only replica nodes. The configuration can range from 90 shards and 0 replicas to 15 shards and 5 replicas, which is the maximum number or replicas allowed.

The node or shard limit can be increased to a maximum of 500 per cluster if the Valkey or Redis OSS engine version is 5.0.6 or higher. For example, you can choose to configure a 500 node cluster that ranges between 83 shards (one primary and 5 replicas per shard) and 500 shards (single primary and no replicas). Make sure there are enough available IP addresses to accommodate the increase. Common pitfalls include the subnets in the subnet group have too small a CIDR range or the subnets are shared and heavily used by other clusters. For more information, see [Creating a Subnet Group](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.Creating.html) . For versions below 5.0.6, the limit is 250 per cluster.

To request a limit increase, see [Amazon Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) and choose the limit type **Nodes per cluster per instance type** .

When a Valkey or Redis OSS (cluster mode disabled) replication group has been successfully created, you can add one or more read replicas to it, up to a total of 5 read replicas. If you need to increase or decrease the number of node groups (console: shards), you can use scaling. For more information, see [Scaling self-designed clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Scaling.html) in the *ElastiCache User Guide* .

### Note

This operation is valid for Valkey and Redis OSS only.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateReplicationGroup)

## Synopsis

```
create-replication-group
--replication-group-id <value>
--replication-group-description <value>
[--global-replication-group-id <value>]
[--primary-cluster-id <value>]
[--automatic-failover-enabled | --no-automatic-failover-enabled]
[--multi-az-enabled | --no-multi-az-enabled]
[--num-cache-clusters <value>]
[--preferred-cache-cluster-azs <value>]
[--num-node-groups <value>]
[--replicas-per-node-group <value>]
[--node-group-configuration <value>]
[--cache-node-type <value>]
[--engine <value>]
[--engine-version <value>]
[--cache-parameter-group-name <value>]
[--cache-subnet-group-name <value>]
[--cache-security-group-names <value>]
[--security-group-ids <value>]
[--tags <value>]
[--snapshot-arns <value>]
[--snapshot-name <value>]
[--preferred-maintenance-window <value>]
[--port <value>]
[--notification-topic-arn <value>]
[--auto-minor-version-upgrade | --no-auto-minor-version-upgrade]
[--snapshot-retention-limit <value>]
[--snapshot-window <value>]
[--auth-token <value>]
[--transit-encryption-enabled | --no-transit-encryption-enabled]
[--at-rest-encryption-enabled | --no-at-rest-encryption-enabled]
[--kms-key-id <value>]
[--user-group-ids <value>]
[--log-delivery-configurations <value>]
[--data-tiering-enabled | --no-data-tiering-enabled]
[--network-type <value>]
[--ip-discovery <value>]
[--transit-encryption-mode <value>]
[--cluster-mode <value>]
[--serverless-cache-snapshot-name <value>]
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

`--replication-group-id` (string)

The replication group identifier. This parameter is stored as a lowercase string.

Constraints:

- A name must contain from 1 to 40 alphanumeric characters or hyphens.
- The first character must be a letter.
- A name cannot end with a hyphen or contain two consecutive hyphens.

`--replication-group-description` (string)

A user-created description for the replication group.

`--global-replication-group-id` (string)

The name of the Global datastore

`--primary-cluster-id` (string)

The identifier of the cluster that serves as the primary for this replication group. This cluster must already exist and have a status of `available` .

This parameter is not required if `NumCacheClusters` , `NumNodeGroups` , or `ReplicasPerNodeGroup` is specified.

`--automatic-failover-enabled` | `--no-automatic-failover-enabled` (boolean)

Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails.

`AutomaticFailoverEnabled` must be enabled for Valkey or Redis OSS (cluster mode enabled) replication groups.

Default: false

`--multi-az-enabled` | `--no-multi-az-enabled` (boolean)

A flag indicating if you have Multi-AZ enabled to enhance fault tolerance. For more information, see [Minimizing Downtime: Multi-AZ](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html) .

`--num-cache-clusters` (integer)

The number of clusters this replication group initially has.

This parameter is not used if there is more than one node group (shard). You should use `ReplicasPerNodeGroup` instead.

If `AutomaticFailoverEnabled` is `true` , the value of this parameter must be at least 2. If `AutomaticFailoverEnabled` is `false` you can omit this parameter (it will default to 1), or you can explicitly set it to a value between 2 and 6.

The maximum permitted value for `NumCacheClusters` is 6 (1 primary plus 5 replicas).

`--preferred-cache-cluster-azs` (list)

A list of EC2 Availability Zones in which the replication groupâs clusters are created. The order of the Availability Zones in the list is the order in which clusters are allocated. The primary cluster is created in the first AZ in the list.

This parameter is not used if there is more than one node group (shard). You should use `NodeGroupConfiguration` instead.

### Note

If you are creating your replication group in an Amazon VPC (recommended), you can only locate clusters in Availability Zones associated with the subnets in the selected subnet group.

The number of Availability Zones listed must equal the value of `NumCacheClusters` .

Default: system chosen Availability Zones.

(string)

Syntax:

```
"string" "string" ...
```

`--num-node-groups` (integer)

An optional parameter that specifies the number of node groups (shards) for this Valkey or Redis OSS (cluster mode enabled) replication group. For Valkey or Redis OSS (cluster mode disabled) either omit this parameter or set it to 1.

Default: 1

`--replicas-per-node-group` (integer)

An optional parameter that specifies the number of replica nodes in each node group (shard). Valid values are 0 to 5.

`--node-group-configuration` (list)

A list of node group (shard) configuration options. Each node group (shard) configuration has the following members: `PrimaryAvailabilityZone` , `ReplicaAvailabilityZones` , `ReplicaCount` , and `Slots` .

If youâre creating a Valkey or Redis OSS (cluster mode disabled) or a Valkey or Redis OSS (cluster mode enabled) replication group, you can use this parameter to individually configure each node group (shard), or you can omit this parameter. However, it is required when seeding a Valkey or Redis OSS (cluster mode enabled) cluster from a S3 rdb file. You must configure each node group (shard) using this parameter because you must specify the slots for each node group.

(structure)

Node group (shard) configuration options. Each node group (shard) configuration has the following: `Slots` , `PrimaryAvailabilityZone` , `ReplicaAvailabilityZones` , `ReplicaCount` .

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

Shorthand Syntax:

```
NodeGroupId=string,Slots=string,ReplicaCount=integer,PrimaryAvailabilityZone=string,ReplicaAvailabilityZones=string,string,PrimaryOutpostArn=string,ReplicaOutpostArns=string,string ...
```

JSON Syntax:

```
[
  {
    "NodeGroupId": "string",
    "Slots": "string",
    "ReplicaCount": integer,
    "PrimaryAvailabilityZone": "string",
    "ReplicaAvailabilityZones": ["string", ...],
    "PrimaryOutpostArn": "string",
    "ReplicaOutpostArns": ["string", ...]
  }
  ...
]
```

`--cache-node-type` (string)

The compute and memory capacity of the nodes in the node group (shard).

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

`--engine` (string)

The name of the cache engine to be used for the clusters in this replication group. The value must be set to `valkey` or `redis` .

`--engine-version` (string)

The version number of the cache engine to be used for the clusters in this replication group. To view the supported cache engine versions, use the `DescribeCacheEngineVersions` operation.

**Important:** You can upgrade to a newer engine version (see [Selecting a Cache Engine and Version](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SelectEngine.html#VersionManagement) ) in the *ElastiCache User Guide* , but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version.

`--cache-parameter-group-name` (string)

The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.

If you are running Valkey or Redis OSS version 3.2.4 or later, only one node group (shard), and want to use a default parameter group, we recommend that you specify the parameter group by name.

- To create a Valkey or Redis OSS (cluster mode disabled) replication group, use `CacheParameterGroupName=default.redis3.2` .
- To create a Valkey or Redis OSS (cluster mode enabled) replication group, use `CacheParameterGroupName=default.redis3.2.cluster.on` .

`--cache-subnet-group-name` (string)

The name of the cache subnet group to be used for the replication group.

### Warning

If youâre going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see [Subnets and Subnet Groups](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.html) .

`--cache-security-group-names` (list)

A list of cache security group names to associate with this replication group.

(string)

Syntax:

```
"string" "string" ...
```

`--security-group-ids` (list)

One or more Amazon VPC security groups associated with this replication group.

Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud (Amazon VPC).

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (list)

A list of tags to be added to this resource. Tags are comma-separated key,value pairs (e.g. Key=``myKey`` , Value=``myKeyValue`` . You can include multiple tags as shown following: Key=``myKey`` , Value=``myKeyValue`` Key=``mySecondKey`` , Value=``mySecondKeyValue`` . Tags on replication groups will be replicated to all nodes.

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

`--snapshot-arns` (list)

A list of Amazon Resource Names (ARN) that uniquely identify the Valkey or Redis OSS RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new replication group. The Amazon S3 object name in the ARN cannot contain any commas. The new replication group will have the number of node groups (console: shards) specified by the parameter *NumNodeGroups* or the number of node groups configured by *NodeGroupConfiguration* regardless of the number of ARNs specified here.

Example of an Amazon S3 ARN: `arn:aws:s3:::my_bucket/snapshot1.rdb`

(string)

Syntax:

```
"string" "string" ...
```

`--snapshot-name` (string)

The name of a snapshot from which to restore data into the new replication group. The snapshot status changes to `restoring` while the new replication group is being created.

`--preferred-maintenance-window` (string)

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

`--port` (integer)

The port number on which each member of the replication group accepts connections.

`--notification-topic-arn` (string)

The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.

### Note

The Amazon SNS topic owner must be the same as the cluster owner.

`--auto-minor-version-upgrade` | `--no-auto-minor-version-upgrade` (boolean)

If you are running Valkey 7.2 and above or Redis OSS engine version 6.0 and above, set this parameter to yes to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions.

`--snapshot-retention-limit` (integer)

The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set `SnapshotRetentionLimit` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Default: 0 (i.e., automatic backups are disabled for this cluster).

`--snapshot-window` (string)

The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).

Example: `05:00-09:00`

If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

`--auth-token` (string)

**Reserved parameter.** The password used to access a password protected server.

`AuthToken` can be specified only on replication groups where `TransitEncryptionEnabled` is `true` .

### Warning

For HIPAA compliance, you must specify `TransitEncryptionEnabled` as `true` , an `AuthToken` , and a `CacheSubnetGroup` .

Password constraints:

- Must be only printable ASCII characters.
- Must be at least 16 characters and no more than 128 characters in length.
- The only permitted printable special characters are !, &, #, $, ^, <, >, and -. Other printable special characters cannot be used in the AUTH token.

For more information, see [AUTH password](http://redis.io/commands/AUTH) at [http://redis.io/commands/AUTH](http://redis.io/commands/AUTH).

`--transit-encryption-enabled` | `--no-transit-encryption-enabled` (boolean)

A flag that enables in-transit encryption when set to `true` .

This parameter is valid only if the `Engine` parameter is `redis` , the `EngineVersion` parameter is `3.2.6` , `4.x` or later, and the cluster is being created in an Amazon VPC.

If you enable in-transit encryption, you must also specify a value for `CacheSubnetGroup` .

**Required:** Only available when creating a replication group in an Amazon VPC using Redis OSS version `3.2.6` , `4.x` or later.

Default: `false`

### Warning

For HIPAA compliance, you must specify `TransitEncryptionEnabled` as `true` , an `AuthToken` , and a `CacheSubnetGroup` .

`--at-rest-encryption-enabled` | `--no-at-rest-encryption-enabled` (boolean)

A flag that enables encryption at rest when set to `true` .

You cannot modify the value of `AtRestEncryptionEnabled` after the replication group is created. To enable encryption at rest on a replication group you must set `AtRestEncryptionEnabled` to `true` when you create the replication group.

**Required:** Only available when creating a replication group in an Amazon VPC using Valkey 7.2 and later, Redis OSS version `3.2.6` , or Redis OSS `4.x` and later.

Default: `true` when using Valkey, `false` when using Redis OSS

`--kms-key-id` (string)

The ID of the KMS key used to encrypt the disk in the cluster.

`--user-group-ids` (list)

The user group to associate with the replication group.

(string)

Syntax:

```
"string" "string" ...
```

`--log-delivery-configurations` (list)

Specifies the destination, format and type of the logs.

(structure)

Specifies the destination, format and type of the logs.

LogType -> (string)

Refers to [slow-log](https://redis.io/commands/slowlog) or engine-log..

DestinationType -> (string)

Specify either `cloudwatch-logs` or `kinesis-firehose` as the destination type.

DestinationDetails -> (structure)

Configuration details of either a CloudWatch Logs destination or Kinesis Data Firehose destination.

CloudWatchLogsDetails -> (structure)

The configuration details of the CloudWatch Logs destination.

LogGroup -> (string)

The name of the CloudWatch Logs log group.

KinesisFirehoseDetails -> (structure)

The configuration details of the Kinesis Data Firehose destination.

DeliveryStream -> (string)

The name of the Kinesis Data Firehose delivery stream.

LogFormat -> (string)

Specifies either JSON or TEXT

Enabled -> (boolean)

Specify if log delivery is enabled. Default `true` .

Shorthand Syntax:

```
LogType=string,DestinationType=string,DestinationDetails={CloudWatchLogsDetails={LogGroup=string},KinesisFirehoseDetails={DeliveryStream=string}},LogFormat=string,Enabled=boolean ...
```

JSON Syntax:

```
[
  {
    "LogType": "slow-log"|"engine-log",
    "DestinationType": "cloudwatch-logs"|"kinesis-firehose",
    "DestinationDetails": {
      "CloudWatchLogsDetails": {
        "LogGroup": "string"
      },
      "KinesisFirehoseDetails": {
        "DeliveryStream": "string"
      }
    },
    "LogFormat": "text"|"json",
    "Enabled": true|false
  }
  ...
]
```

`--data-tiering-enabled` | `--no-data-tiering-enabled` (boolean)

Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see [Data tiering](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/data-tiering.html) .

`--network-type` (string)

Must be either `ipv4` | `ipv6` | `dual_stack` . IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 and Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/) .

Possible values:

- `ipv4`
- `ipv6`
- `dual_stack`

`--ip-discovery` (string)

The network type you choose when creating a replication group, either `ipv4` | `ipv6` . IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/) .

Possible values:

- `ipv4`
- `ipv6`

`--transit-encryption-mode` (string)

A setting that allows you to migrate your clients to use in-transit encryption, with no downtime.

When setting `TransitEncryptionEnabled` to `true` , you can set your `TransitEncryptionMode` to `preferred` in the same request, to allow both encrypted and unencrypted connections at the same time. Once you migrate all your Valkey or Redis OSS clients to use encrypted connections you can modify the value to `required` to allow encrypted connections only.

Setting `TransitEncryptionMode` to `required` is a two-step process that requires you to first set the `TransitEncryptionMode` to `preferred` , after that you can set `TransitEncryptionMode` to `required` .

This process will not trigger the replacement of the replication group.

Possible values:

- `preferred`
- `required`

`--cluster-mode` (string)

Enabled or Disabled. To modify cluster mode from Disabled to Enabled, you must first set the cluster mode to Compatible. Compatible mode allows your Valkey or Redis OSS clients to connect using both cluster mode enabled and cluster mode disabled. After you migrate all Valkey or Redis OSS clients to use cluster mode enabled, you can then complete cluster mode configuration and set the cluster mode to Enabled.

Possible values:

- `enabled`
- `disabled`
- `compatible`

`--serverless-cache-snapshot-name` (string)

The name of the snapshot used to create a replication group. Available for Valkey, Redis OSS only.

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

**To create a replication group**

The following `create-replication-group` example creates a Redis (cluster mode disabled) or a Redis (cluster mode enabled) replication group. This operation is valid for Redis only.

```
aws elasticache create-replication-group \
    --replication-group-id "mygroup" \
    --replication-group-description "my group" \
    --engine "redis" \
    --cache-node-type "cache.m5.large"
```

Output:

```
{
    "ReplicationGroup": {
        "ReplicationGroupId": "mygroup",
        "Description": "my group",
        "Status": "creating",
        "PendingModifiedValues": {},
        "MemberClusters": [
            "mygroup-001"
        ],
        "AutomaticFailover": "disabled",
        "SnapshotRetentionLimit": 0,
        "SnapshotWindow": "06:00-07:00",
        "ClusterEnabled": false,
        "CacheNodeType": "cache.m5.large",
        "TransitEncryptionEnabled": false,
        "AtRestEncryptionEnabled": false
    }
}
```

For more information, see [Creating a Redis Replication Group](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Replication.CreatingRepGroup.html) in the *Elasticache User Guide*.

## Output

ReplicationGroup -> (structure)

Contains all of the attributes of a specific Valkey or Redis OSS replication group.

ReplicationGroupId -> (string)

The identifier for the replication group.

Description -> (string)

The user supplied description of the replication group.

GlobalReplicationGroupInfo -> (structure)

The name of the Global datastore and role of this replication group in the Global datastore.

GlobalReplicationGroupId -> (string)

The name of the Global datastore

GlobalReplicationGroupMemberRole -> (string)

The role of the replication group in a Global datastore. Can be primary or secondary.

Status -> (string)

The current state of this replication group - `creating` , `available` , `modifying` , `deleting` , `create-failed` , `snapshotting` .

PendingModifiedValues -> (structure)

A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

PrimaryClusterId -> (string)

The primary cluster ID that is applied immediately (if `--apply-immediately` was specified), or during the next maintenance window.

AutomaticFailoverStatus -> (string)

Indicates the status of automatic failover for this Valkey or Redis OSS replication group.

Resharding -> (structure)

The status of an online resharding operation.

SlotMigration -> (structure)

Represents the progress of an online resharding operation.

ProgressPercentage -> (double)

The percentage of the slot migration that is complete.

AuthTokenStatus -> (string)

The auth token status

UserGroups -> (structure)

The user group being modified.

UserGroupIdsToAdd -> (list)

The ID of the user group to add.

(string)

UserGroupIdsToRemove -> (list)

The ID of the user group to remove.

(string)

LogDeliveryConfigurations -> (list)

The log delivery configurations being modified

(structure)

The log delivery configurations being modified

LogType -> (string)

Refers to [slow-log](https://redis.io/commands/slowlog) or engine-log..

DestinationType -> (string)

Returns the destination type, either CloudWatch Logs or Kinesis Data Firehose.

DestinationDetails -> (structure)

Configuration details of either a CloudWatch Logs destination or Kinesis Data Firehose destination.

CloudWatchLogsDetails -> (structure)

The configuration details of the CloudWatch Logs destination.

LogGroup -> (string)

The name of the CloudWatch Logs log group.

KinesisFirehoseDetails -> (structure)

The configuration details of the Kinesis Data Firehose destination.

DeliveryStream -> (string)

The name of the Kinesis Data Firehose delivery stream.

LogFormat -> (string)

Returns the log format, either JSON or TEXT

TransitEncryptionEnabled -> (boolean)

A flag that enables in-transit encryption when set to true.

TransitEncryptionMode -> (string)

A setting that allows you to migrate your clients to use in-transit encryption, with no downtime.

ClusterMode -> (string)

Enabled or Disabled. To modify cluster mode from Disabled to Enabled, you must first set the cluster mode to Compatible. Compatible mode allows your Valkey or Redis OSS clients to connect using both cluster mode enabled and cluster mode disabled. After you migrate all Valkey or Redis OSS clients to use cluster mode enabled, you can then complete cluster mode configuration and set the cluster mode to Enabled.

MemberClusters -> (list)

The names of all the cache clusters that are part of this replication group.

(string)

NodeGroups -> (list)

A list of node groups in this replication group. For Valkey or Redis OSS (cluster mode disabled) replication groups, this is a single-element list. For Valkey or Redis OSS (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

(structure)

Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

NodeGroupId -> (string)

The identifier for the node group (shard). A Valkey or Redis OSS (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Valkey or Redis OSS (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to 0090. Optionally, the user can provide the id for a node group.

Status -> (string)

The current state of this replication group - `creating` , `available` , `modifying` , `deleting` .

PrimaryEndpoint -> (structure)

The endpoint of the primary node in this node group (shard).

Address -> (string)

The DNS hostname of the cache node.

Port -> (integer)

The port number that the cache engine is listening on.

ReaderEndpoint -> (structure)

The endpoint of the replica nodes in this node group (shard). This value is read-only.

Address -> (string)

The DNS hostname of the cache node.

Port -> (integer)

The port number that the cache engine is listening on.

Slots -> (string)

The keyspace for this node group (shard).

NodeGroupMembers -> (list)

A list containing information about individual nodes within the node group (shard).

(structure)

Represents a single node within a node group (shard).

CacheClusterId -> (string)

The ID of the cluster to which the node belongs.

CacheNodeId -> (string)

The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

ReadEndpoint -> (structure)

The information required for client programs to connect to a node for read operations. The read endpoint is only applicable on Valkey or Redis OSS (cluster mode disabled) clusters.

Address -> (string)

The DNS hostname of the cache node.

Port -> (integer)

The port number that the cache engine is listening on.

PreferredAvailabilityZone -> (string)

The name of the Availability Zone in which the node is located.

PreferredOutpostArn -> (string)

The outpost ARN of the node group member.

CurrentRole -> (string)

The role that is currently assigned to the node - `primary` or `replica` . This member is only applicable for Valkey or Redis OSS (cluster mode disabled) replication groups.

SnapshottingClusterId -> (string)

The cluster ID that is used as the daily snapshot source for the replication group.

AutomaticFailover -> (string)

Indicates the status of automatic failover for this Valkey or Redis OSS replication group.

MultiAZ -> (string)

A flag indicating if you have Multi-AZ enabled to enhance fault tolerance. For more information, see [Minimizing Downtime: Multi-AZ](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html)

ConfigurationEndpoint -> (structure)

The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

Address -> (string)

The DNS hostname of the cache node.

Port -> (integer)

The port number that the cache engine is listening on.

SnapshotRetentionLimit -> (integer)

The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set `SnapshotRetentionLimit` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

### Warning

If the value of `SnapshotRetentionLimit` is set to zero (0), backups are turned off.

SnapshotWindow -> (string)

The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).

Example: `05:00-09:00`

If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

### Note

This parameter is only valid if the `Engine` parameter is `redis` .

ClusterEnabled -> (boolean)

A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).

Valid values: `true` | `false`

CacheNodeType -> (string)

The name of the compute and memory capacity node type for each node in the replication group.

AuthTokenEnabled -> (boolean)

A flag that enables using an `AuthToken` (password) when issuing Valkey or Redis OSS commands.

Default: `false`

AuthTokenLastModifiedDate -> (timestamp)

The date the auth token was last modified

TransitEncryptionEnabled -> (boolean)

A flag that enables in-transit encryption when set to `true` .

**Required:** Only available when creating a replication group in an Amazon VPC using Redis OSS version `3.2.6` , `4.x` or later.

Default: `false`

AtRestEncryptionEnabled -> (boolean)

A flag that enables encryption at-rest when set to `true` .

You cannot modify the value of `AtRestEncryptionEnabled` after the cluster is created. To enable encryption at-rest on a cluster you must set `AtRestEncryptionEnabled` to `true` when you create a cluster.

**Required:** Only available when creating a replication group in an Amazon VPC using Redis OSS version `3.2.6` , `4.x` or later.

Default: `false`

MemberClustersOutpostArns -> (list)

The outpost ARNs of the replication groupâs member clusters.

(string)

KmsKeyId -> (string)

The ID of the KMS key used to encrypt the disk in the cluster.

ARN -> (string)

The ARN (Amazon Resource Name) of the replication group.

UserGroupIds -> (list)

The ID of the user group associated to the replication group.

(string)

LogDeliveryConfigurations -> (list)

Returns the destination, format and type of the logs.

(structure)

Returns the destination, format and type of the logs.

LogType -> (string)

Refers to [slow-log](https://redis.io/commands/slowlog) or engine-log.

DestinationType -> (string)

Returns the destination type, either `cloudwatch-logs` or `kinesis-firehose` .

DestinationDetails -> (structure)

Configuration details of either a CloudWatch Logs destination or Kinesis Data Firehose destination.

CloudWatchLogsDetails -> (structure)

The configuration details of the CloudWatch Logs destination.

LogGroup -> (string)

The name of the CloudWatch Logs log group.

KinesisFirehoseDetails -> (structure)

The configuration details of the Kinesis Data Firehose destination.

DeliveryStream -> (string)

The name of the Kinesis Data Firehose delivery stream.

LogFormat -> (string)

Returns the log format, either JSON or TEXT.

Status -> (string)

Returns the log delivery configuration status. Values are one of `enabling` | `disabling` | `modifying` | `active` | `error`

Message -> (string)

Returns an error message for the log delivery configuration.

ReplicationGroupCreateTime -> (timestamp)

The date and time when the cluster was created.

DataTiering -> (string)

Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see [Data tiering](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/data-tiering.html) .

AutoMinorVersionUpgrade -> (boolean)

If you are running Valkey 7.2 and above, or Redis OSS engine version 6.0 and above, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions.

NetworkType -> (string)

Must be either `ipv4` | `ipv6` | `dual_stack` . IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/) .

IpDiscovery -> (string)

The network type you choose when modifying a cluster, either `ipv4` | `ipv6` . IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/) .

TransitEncryptionMode -> (string)

A setting that allows you to migrate your clients to use in-transit encryption, with no downtime.

ClusterMode -> (string)

Enabled or Disabled. To modify cluster mode from Disabled to Enabled, you must first set the cluster mode to Compatible. Compatible mode allows your Valkey or Redis OSS clients to connect using both cluster mode enabled and cluster mode disabled. After you migrate all Valkey or Redis OSS clients to use cluster mode enabled, you can then complete cluster mode configuration and set the cluster mode to Enabled.

Engine -> (string)

The engine used in a replication group. The options are redis, memcached or valkey.