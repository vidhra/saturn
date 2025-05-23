# create-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/create-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/create-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [memorydb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/index.html#cli-aws-memorydb) ]

# create-cluster

## Description

Creates a cluster. All nodes in the cluster run the same protocol-compliant engine software.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/memorydb-2021-01-01/CreateCluster)

## Synopsis

```
create-cluster
--cluster-name <value>
--node-type <value>
[--multi-region-cluster-name <value>]
[--parameter-group-name <value>]
[--description <value>]
[--num-shards <value>]
[--num-replicas-per-shard <value>]
[--subnet-group-name <value>]
[--security-group-ids <value>]
[--maintenance-window <value>]
[--port <value>]
[--sns-topic-arn <value>]
[--tls-enabled | --no-tls-enabled]
[--kms-key-id <value>]
[--snapshot-arns <value>]
[--snapshot-name <value>]
[--snapshot-retention-limit <value>]
[--tags <value>]
[--snapshot-window <value>]
--acl-name <value>
[--engine <value>]
[--engine-version <value>]
[--auto-minor-version-upgrade | --no-auto-minor-version-upgrade]
[--data-tiering | --no-data-tiering]
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

`--cluster-name` (string)

The name of the cluster. This value must be unique as it also serves as the cluster identifier.

`--node-type` (string)

The compute and memory capacity of the nodes in the cluster.

`--multi-region-cluster-name` (string)

The name of the multi-Region cluster to be created.

`--parameter-group-name` (string)

The name of the parameter group associated with the cluster.

`--description` (string)

An optional description of the cluster.

`--num-shards` (integer)

The number of shards the cluster will contain. The default value is 1.

`--num-replicas-per-shard` (integer)

The number of replicas to apply to each shard. The default value is 1. The maximum is 5.

`--subnet-group-name` (string)

The name of the subnet group to be used for the cluster.

`--security-group-ids` (list)

A list of security group names to associate with this cluster.

(string)

Syntax:

```
"string" "string" ...
```

`--maintenance-window` (string)

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

The port number on which each of the nodes accepts connections.

`--sns-topic-arn` (string)

The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.

`--tls-enabled` | `--no-tls-enabled` (boolean)

A flag to enable in-transit encryption on the cluster.

`--kms-key-id` (string)

The ID of the KMS key used to encrypt the cluster.

`--snapshot-arns` (list)

A list of Amazon Resource Names (ARN) that uniquely identify the RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new cluster. The Amazon S3 object name in the ARN cannot contain any commas.

(string)

Syntax:

```
"string" "string" ...
```

`--snapshot-name` (string)

The name of a snapshot from which to restore data into the new cluster. The snapshot status changes to restoring while the new cluster is being created.

`--snapshot-retention-limit` (integer)

The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

`--tags` (list)

A list of tags to be added to this resource. Tags are comma-separated key,value pairs (e.g. Key=myKey, Value=myKeyValue. You can include multiple tags as shown following: Key=myKey, Value=myKeyValue Key=mySecondKey, Value=mySecondKeyValue.

(structure)

A tag that can be added to an MemoryDB resource. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your MemoryDB resources. When you add or remove tags on clusters, those actions will be replicated to all nodes in the cluster. A tag with a null Value is permitted. For more information, see [Tagging your MemoryDB resources](https://docs.aws.amazon.com/MemoryDB/latest/devguide/tagging-resources.html)

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

`--snapshot-window` (string)

The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your shard.

Example: 05:00-09:00

If you do not specify this parameter, MemoryDB automatically chooses an appropriate time range.

`--acl-name` (string)

The name of the Access Control List to associate with the cluster.

`--engine` (string)

The name of the engine to be used for the cluster.

`--engine-version` (string)

The version number of the Redis OSS engine to be used for the cluster.

`--auto-minor-version-upgrade` | `--no-auto-minor-version-upgrade` (boolean)

When set to true, the cluster will automatically receive minor engine version upgrades after launch.

`--data-tiering` | `--no-data-tiering` (boolean)

Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes. For more information, see [Data tiering](https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html) .

`--network-type` (string)

Specifies the IP address type for the cluster. Valid values are âipv4â, âipv6â, or âdual_stackâ. When set to âipv4â, the cluster will only be accessible via IPv4 addresses. When set to âipv6â, the cluster will only be accessible via IPv6 addresses. When set to âdual_stackâ, the cluster will be accessible via both IPv4 and IPv6 addresses. If not specified, the default is âipv4â.

Possible values:

- `ipv4`
- `ipv6`
- `dual_stack`

`--ip-discovery` (string)

The mechanism for discovering IP addresses for the cluster discovery protocol. Valid values are âipv4â or âipv6â. When set to âipv4â, cluster discovery functions such as cluster slots, cluster shards, and cluster nodes return IPv4 addresses for cluster nodes. When set to âipv6â, the cluster discovery functions return IPv6 addresses for cluster nodes. The value must be compatible with the NetworkType parameter. If not specified, the default is âipv4â.

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

**To create a cluster**

The following `create-cluster` example creates a new cluster.

```
aws memorydb create-cluster \
    --cluster-name my-new-cluster \
    --node-type db.r6g.large \
    --acl-name my-acl \
    --subnet-group my-sg
```

Output:

```
{
    "Cluster": {
        "Name": "my-new-cluster",
        "Status": "creating",
        "NumberOfShards": 1,
        "AvailabilityMode": "MultiAZ",
        "ClusterEndpoint": {
            "Port": 6379
        },
        "NodeType": "db.r6g.large",
        "EngineVersion": "6.2",
        "EnginePatchVersion": "6.2.6",
        "ParameterGroupName": "default.memorydb-redis6",
        "ParameterGroupStatus": "in-sync",
        "SubnetGroupName": "my-sg",
        "TLSEnabled": true,
        "ARN": "arn:aws:memorydb:us-east-1:49165xxxxxx:cluster/my-new-cluster",
        "SnapshotRetentionLimit": 0,
        "MaintenanceWindow": "sat:10:00-sat:11:00",
        "SnapshotWindow": "07:30-08:30",
        "ACLName": "my-acl",
        "AutoMinorVersionUpgrade": true
    }
}
```

For more information, see [Managing Clusters](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.html) in the *MemoryDB User Guide*.

## Output

Cluster -> (structure)

The newly-created cluster.

Name -> (string)

The user-supplied name of the cluster. This identifier is a unique key that identifies a cluster.

Description -> (string)

A description of the cluster

Status -> (string)

The status of the cluster. For example, Available, Updating, Creating.

PendingUpdates -> (structure)

A group of settings that are currently being applied.

Resharding -> (structure)

The status of an online resharding operation.

SlotMigration -> (structure)

The status of the online resharding slot migration

ProgressPercentage -> (double)

The percentage of the slot migration that is complete.

ACLs -> (structure)

A list of ACLs associated with the cluster that are being updated

ACLToApply -> (string)

A list of ACLs pending to be applied.

ServiceUpdates -> (list)

A list of service updates being applied to the cluster

(structure)

Update action that has yet to be processed for the corresponding apply/stop request

ServiceUpdateName -> (string)

The unique ID of the service update

Status -> (string)

The status of the service update

MultiRegionClusterName -> (string)

The name of the multi-Region cluster that this cluster belongs to.

NumberOfShards -> (integer)

The number of shards in the cluster

Shards -> (list)

A list of shards that are members of the cluster.

(structure)

Represents a collection of nodes in a cluster. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

Name -> (string)

The name of the shard

Status -> (string)

The current state of this replication group - creating, available, modifying, deleting.

Slots -> (string)

The keyspace for this shard.

Nodes -> (list)

A list containing information about individual nodes within the shard

(structure)

Represents an individual node within a cluster. Each node runs its own instance of the clusterâs protocol-compliant caching software.

Name -> (string)

The node identifier. A node name is a numeric identifier (0001, 0002, etc.). The combination of cluster name, shard name and node name uniquely identifies every node used in a customerâs Amazon account.

Status -> (string)

The status of the service update on the node

AvailabilityZone -> (string)

The Availability Zone in which the node resides

CreateTime -> (timestamp)

The date and time when the node was created.

Endpoint -> (structure)

The hostname for connecting to this node.

Address -> (string)

The DNS hostname of the node.

Port -> (integer)

The port number that the engine is listening on.

NumberOfNodes -> (integer)

The number of nodes in the shard

AvailabilityMode -> (string)

Indicates if the cluster has a Multi-AZ configuration (multiaz) or not (singleaz).

ClusterEndpoint -> (structure)

The clusterâs configuration endpoint

Address -> (string)

The DNS hostname of the node.

Port -> (integer)

The port number that the engine is listening on.

NodeType -> (string)

The clusterâs node type

Engine -> (string)

The name of the engine used by the cluster.

EngineVersion -> (string)

The Redis OSS engine version used by the cluster

EnginePatchVersion -> (string)

The Redis OSS engine patch version used by the cluster

ParameterGroupName -> (string)

The name of the parameter group used by the cluster

ParameterGroupStatus -> (string)

The status of the parameter group used by the cluster, for example âactiveâ or âapplyingâ.

SecurityGroups -> (list)

A list of security groups used by the cluster

(structure)

Represents a single security group and its status.

SecurityGroupId -> (string)

The identifier of the security group.

Status -> (string)

The status of the security group membership. The status changes whenever a security group is modified, or when the security groups assigned to a cluster are modified.

SubnetGroupName -> (string)

The name of the subnet group used by the cluster

TLSEnabled -> (boolean)

A flag to indicate if In-transit encryption is enabled

KmsKeyId -> (string)

The ID of the KMS key used to encrypt the cluster

ARN -> (string)

The Amazon Resource Name (ARN) of the cluster.

SnsTopicArn -> (string)

The Amazon Resource Name (ARN) of the SNS notification topic

SnsTopicStatus -> (string)

The SNS topic must be in Active status to receive notifications

SnapshotRetentionLimit -> (integer)

The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

MaintenanceWindow -> (string)

Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

SnapshotWindow -> (string)

The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your shard. Example: 05:00-09:00 If you do not specify this parameter, MemoryDB automatically chooses an appropriate time range.

ACLName -> (string)

The name of the Access Control List associated with this cluster.

AutoMinorVersionUpgrade -> (boolean)

When set to true, the cluster will automatically receive minor engine version upgrades after launch.

DataTiering -> (string)

Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes. For more information, see [Data tiering](https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html) .

NetworkType -> (string)

The IP address type for the cluster. Returns âipv4â for IPv4 only, âipv6â for IPv6 only, or âdual-stackâ if the cluster supports both IPv4 and IPv6 addressing.

IpDiscovery -> (string)

The mechanism that the cluster uses to discover IP addresses. Returns âipv4â when DNS endpoints resolve to IPv4 addresses, or âipv6â when DNS endpoints resolve to IPv6 addresses.