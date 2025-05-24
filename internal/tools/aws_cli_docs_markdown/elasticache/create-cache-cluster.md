# create-cache-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/index.html#cli-aws-elasticache) ]

# create-cache-cluster

## Description

Creates a cluster. All nodes in the cluster run the same protocol-compliant cache engine software, either Memcached, Valkey or Redis OSS.

This operation is not supported for Valkey or Redis OSS (cluster mode enabled) clusters.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateCacheCluster)

## Synopsis

```
create-cache-cluster
--cache-cluster-id <value>
[--replication-group-id <value>]
[--az-mode <value>]
[--preferred-availability-zone <value>]
[--preferred-availability-zones <value>]
[--num-cache-nodes <value>]
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
[--outpost-mode <value>]
[--preferred-outpost-arn <value>]
[--preferred-outpost-arns <value>]
[--log-delivery-configurations <value>]
[--transit-encryption-enabled | --no-transit-encryption-enabled]
[--network-type <value>]
[--ip-discovery <value>]
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

`--cache-cluster-id` (string)

The node group (shard) identifier. This parameter is stored as a lowercase string.

**Constraints:**

- A name must contain from 1 to 50 alphanumeric characters or hyphens.
- The first character must be a letter.
- A name cannot end with a hyphen or contain two consecutive hyphens.

`--replication-group-id` (string)

The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.

If the specified replication group is Multi-AZ enabled and the Availability Zone is not specified, the cluster is created in Availability Zones that provide the best spread of read replicas across Availability Zones.

### Note

This parameter is only valid if the `Engine` parameter is `redis` .

`--az-mode` (string)

Specifies whether the nodes in this Memcached cluster are created in a single Availability Zone or created across multiple Availability Zones in the clusterâs region.

This parameter is only supported for Memcached clusters.

If the `AZMode` and `PreferredAvailabilityZones` are not specified, ElastiCache assumes `single-az` mode.

Possible values:

- `single-az`
- `cross-az`

`--preferred-availability-zone` (string)

The EC2 Availability Zone in which the cluster is created.

All nodes belonging to this cluster are placed in the preferred Availability Zone. If you want to create your nodes across multiple Availability Zones, use `PreferredAvailabilityZones` .

Default: System chosen Availability Zone.

`--preferred-availability-zones` (list)

A list of the Availability Zones in which cache nodes are created. The order of the zones in the list is not important.

This option is only supported on Memcached.

### Note

If you are creating your cluster in an Amazon VPC (recommended) you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group.

The number of Availability Zones listed must equal the value of `NumCacheNodes` .

If you want all the nodes in the same Availability Zone, use `PreferredAvailabilityZone` instead, or repeat the Availability Zone multiple times in the list.

Default: System chosen Availability Zones.

(string)

Syntax:

```
"string" "string" ...
```

`--num-cache-nodes` (integer)

The initial number of cache nodes that the cluster has.

For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.

If you need more than 40 nodes for your Memcached cluster, please fill out the ElastiCache Limit Increase Request form at [http://aws.amazon.com/contact-us/elasticache-node-limit-request/](http://aws.amazon.com/contact-us/elasticache-node-limit-request/) .

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

The name of the cache engine to be used for this cluster.

Valid values for this parameter are: `memcached` | `redis`

`--engine-version` (string)

The version number of the cache engine to be used for this cluster. To view the supported cache engine versions, use the DescribeCacheEngineVersions operation.

**Important:** You can upgrade to a newer engine version (see [Selecting a Cache Engine and Version](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SelectEngine.html#VersionManagement) ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version.

`--cache-parameter-group-name` (string)

The name of the parameter group to associate with this cluster. If this argument is omitted, the default parameter group for the specified engine is used. You cannot use any parameter group which has `cluster-enabled='yes'` when creating a cluster.

`--cache-subnet-group-name` (string)

The name of the subnet group to be used for the cluster.

Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).

### Warning

If youâre going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see [Subnets and Subnet Groups](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.html) .

`--cache-security-group-names` (list)

A list of security group names to associate with this cluster.

Use this parameter only when you are creating a cluster outside of an Amazon Virtual Private Cloud (Amazon VPC).

(string)

Syntax:

```
"string" "string" ...
```

`--security-group-ids` (list)

One or more VPC security groups associated with the cluster.

Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (list)

A list of tags to be added to this resource.

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

A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a Valkey or Redis OSS RDB snapshot file stored in Amazon S3. The snapshot file is used to populate the node group (shard). The Amazon S3 object name in the ARN cannot contain any commas.

### Note

This parameter is only valid if the `Engine` parameter is `redis` .

Example of an Amazon S3 ARN: `arn:aws:s3:::my_bucket/snapshot1.rdb`

(string)

Syntax:

```
"string" "string" ...
```

`--snapshot-name` (string)

The name of a Valkey or Redis OSS snapshot from which to restore data into the new node group (shard). The snapshot status changes to `restoring` while the new node group (shard) is being created.

### Note

This parameter is only valid if the `Engine` parameter is `redis` .

`--preferred-maintenance-window` (string)

Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

`--port` (integer)

The port number on which each of the cache nodes accepts connections.

`--notification-topic-arn` (string)

The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.

### Note

The Amazon SNS topic owner must be the same as the cluster owner.

`--auto-minor-version-upgrade` | `--no-auto-minor-version-upgrade` (boolean)

If you are running Valkey 7.2 and above or Redis OSS engine version 6.0 and above, set this parameter to yes to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions.

`--snapshot-retention-limit` (integer)

The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set `SnapshotRetentionLimit` to 5, a snapshot taken today is retained for 5 days before being deleted.

### Note

This parameter is only valid if the `Engine` parameter is `redis` .

Default: 0 (i.e., automatic backups are disabled for this cache cluster).

`--snapshot-window` (string)

The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).

Example: `05:00-09:00`

If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

### Note

This parameter is only valid if the `Engine` parameter is `redis` .

`--auth-token` (string)

**Reserved parameter.** The password used to access a password protected server.

Password constraints:

- Must be only printable ASCII characters.
- Must be at least 16 characters and no more than 128 characters in length.
- The only permitted printable special characters are !, &, #, $, ^, <, >, and -. Other printable special characters cannot be used in the AUTH token.

For more information, see [AUTH password](http://redis.io/commands/AUTH) at [http://redis.io/commands/AUTH](http://redis.io/commands/AUTH).

`--outpost-mode` (string)

Specifies whether the nodes in the cluster are created in a single outpost or across multiple outposts.

Possible values:

- `single-outpost`
- `cross-outpost`

`--preferred-outpost-arn` (string)

The outpost ARN in which the cache cluster is created.

`--preferred-outpost-arns` (list)

The outpost ARNs in which the cache cluster is created.

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

`--transit-encryption-enabled` | `--no-transit-encryption-enabled` (boolean)

A flag that enables in-transit encryption when set to true.

`--network-type` (string)

Must be either `ipv4` | `ipv6` | `dual_stack` . IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 and Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/) .

Possible values:

- `ipv4`
- `ipv6`
- `dual_stack`

`--ip-discovery` (string)

The network type you choose when modifying a cluster, either `ipv4` | `ipv6` . IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 and Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/) .

Possible values:

- `ipv4`
- `ipv6`

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

**To create a cache cluster**

The following `create-cache-cluster` example creates a cache cluster using the Redis engine.

```
aws elasticache create-cache-cluster \
    --cache-cluster-id "cluster-test" \
    --engine redis \
    --cache-node-type cache.m5.large \
    --num-cache-nodes 1
```

Output:

```
{
    "CacheCluster": {
        "CacheClusterId": "cluster-test",
        "ClientDownloadLandingPage": "https://console.aws.amazon.com/elasticache/home#client-download:",
        "CacheNodeType": "cache.m5.large",
        "Engine": "redis",
        "EngineVersion": "5.0.5",
        "CacheClusterStatus": "creating",
        "NumCacheNodes": 1,
        "PreferredMaintenanceWindow": "sat:13:00-sat:14:00",
        "PendingModifiedValues": {},
        "CacheSecurityGroups": [],
        "CacheParameterGroup": {
            "CacheParameterGroupName": "default.redis5.0",
            "ParameterApplyStatus": "in-sync",
            "CacheNodeIdsToReboot": []
        },
        "CacheSubnetGroupName": "default",
        "AutoMinorVersionUpgrade": true,
        "SnapshotRetentionLimit": 0,
        "SnapshotWindow": "06:30-07:30",
        "TransitEncryptionEnabled": false,
        "AtRestEncryptionEnabled": false
    }
}
```

For more information, see [Creating a Cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Create.html) in the *Elasticache User Guide*.

## Output

CacheCluster -> (structure)

Contains all of the attributes of a specific cluster.

CacheClusterId -> (string)

The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.

ConfigurationEndpoint -> (structure)

Represents a Memcached cluster endpoint which can be used by an application to connect to any node in the cluster. The configuration endpoint will always have `.cfg` in it.

Example: `mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211`

Address -> (string)

The DNS hostname of the cache node.

Port -> (integer)

The port number that the cache engine is listening on.

ClientDownloadLandingPage -> (string)

The URL of the web page where you can download the latest ElastiCache client library.

CacheNodeType -> (string)

The name of the compute and memory capacity node type for the cluster.

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

The name of the cache engine (`memcached` or `redis` ) to be used for this cluster.

EngineVersion -> (string)

The version of the cache engine that is used in this cluster.

CacheClusterStatus -> (string)

The current state of this cluster, one of the following values: `available` , `creating` , `deleted` , `deleting` , `incompatible-network` , `modifying` , `rebooting cluster nodes` , `restore-failed` , or `snapshotting` .

NumCacheNodes -> (integer)

The number of cache nodes in the cluster.

For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.

PreferredAvailabilityZone -> (string)

The name of the Availability Zone in which the cluster is located or âMultipleâ if the cache nodes are located in different Availability Zones.

PreferredOutpostArn -> (string)

The outpost ARN in which the cache cluster is created.

CacheClusterCreateTime -> (timestamp)

The date and time when the cluster was created.

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

PendingModifiedValues -> (structure)

A group of settings that are applied to the cluster in the future, or that are currently being applied.

NumCacheNodes -> (integer)

The new number of cache nodes for the cluster.

For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.

CacheNodeIdsToRemove -> (list)

A list of cache node IDs that are being removed (or will be removed) from the cluster. A node ID is a 4-digit numeric identifier (0001, 0002, etc.).

(string)

EngineVersion -> (string)

The new cache engine version that the cluster runs.

CacheNodeType -> (string)

The cache node type that this cluster or replication group is scaled to.

AuthTokenStatus -> (string)

The auth token status

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

ScaleConfig -> (structure)

The scaling configuration changes that are pending for the Memcached cluster.

ScalePercentage -> (integer)

The percentage by which to scale the Memcached cluster, either horizontally by adding nodes or vertically by increasing resources.

ScaleIntervalMinutes -> (integer)

The time interval in seconds between scaling operations when performing gradual scaling for a Memcached cluster.

NotificationConfiguration -> (structure)

Describes a notification topic and its status. Notification topics are used for publishing ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

TopicArn -> (string)

The Amazon Resource Name (ARN) that identifies the topic.

TopicStatus -> (string)

The current state of the topic.

CacheSecurityGroups -> (list)

A list of cache security group elements, composed of name and status sub-elements.

(structure)

Represents a clusterâs status within a particular cache security group.

CacheSecurityGroupName -> (string)

The name of the cache security group.

Status -> (string)

The membership status in the cache security group. The status changes when a cache security group is modified, or when the cache security groups assigned to a cluster are modified.

CacheParameterGroup -> (structure)

Status of the cache parameter group.

CacheParameterGroupName -> (string)

The name of the cache parameter group.

ParameterApplyStatus -> (string)

The status of parameter updates.

CacheNodeIdsToReboot -> (list)

A list of the cache node IDs which need to be rebooted for parameter changes to be applied. A node ID is a numeric identifier (0001, 0002, etc.).

(string)

CacheSubnetGroupName -> (string)

The name of the cache subnet group associated with the cluster.

CacheNodes -> (list)

A list of cache nodes that are members of the cluster.

(structure)

Represents an individual cache node within a cluster. Each cache node runs its own instance of the clusterâs protocol-compliant caching software - either Memcached, Valkey or Redis OSS.

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

CacheNodeId -> (string)

The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The combination of cluster ID and node ID uniquely identifies every cache node used in a customerâs Amazon account.

CacheNodeStatus -> (string)

The current state of this cache node, one of the following values: `available` , `creating` , `rebooting` , or `deleting` .

CacheNodeCreateTime -> (timestamp)

The date and time when the cache node was created.

Endpoint -> (structure)

The hostname for connecting to this cache node.

Address -> (string)

The DNS hostname of the cache node.

Port -> (integer)

The port number that the cache engine is listening on.

ParameterGroupStatus -> (string)

The status of the parameter group applied to this cache node.

SourceCacheNodeId -> (string)

The ID of the primary node to which this read replica node is synchronized. If this field is empty, this node is not associated with a primary cluster.

CustomerAvailabilityZone -> (string)

The Availability Zone where this node was created and now resides.

CustomerOutpostArn -> (string)

The customer outpost ARN of the cache node.

AutoMinorVersionUpgrade -> (boolean)

If you are running Valkey or Redis OSS engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions.

SecurityGroups -> (list)

A list of VPC Security Groups associated with the cluster.

(structure)

Represents a single cache security group and its status.

SecurityGroupId -> (string)

The identifier of the cache security group.

Status -> (string)

The status of the cache security group membership. The status changes whenever a cache security group is modified, or when the cache security groups assigned to a cluster are modified.

ReplicationGroupId -> (string)

The replication group to which this cluster belongs. If this field is empty, the cluster is not associated with any replication group.

SnapshotRetentionLimit -> (integer)

The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set `SnapshotRetentionLimit` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

### Warning

If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

SnapshotWindow -> (string)

The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.

Example: `05:00-09:00`

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

You cannot modify the value of `AtRestEncryptionEnabled` after the cluster is created. To enable at-rest encryption on a cluster you must set `AtRestEncryptionEnabled` to `true` when you create a cluster.

**Required:** Only available when creating a replication group in an Amazon VPC using Redis OSS version `3.2.6` , `4.x` or later.

Default: `false`

ARN -> (string)

The ARN (Amazon Resource Name) of the cache cluster.

ReplicationGroupLogDeliveryEnabled -> (boolean)

A boolean value indicating whether log delivery is enabled for the replication group.

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

NetworkType -> (string)

Must be either `ipv4` | `ipv6` | `dual_stack` . IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 7.1 or Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/) .

IpDiscovery -> (string)

The network type associated with the cluster, either `ipv4` | `ipv6` . IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/) .

TransitEncryptionMode -> (string)

A setting that allows you to migrate your clients to use in-transit encryption, with no downtime.