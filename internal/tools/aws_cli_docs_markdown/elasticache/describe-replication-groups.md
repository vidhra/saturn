# describe-replication-groupsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-replication-groups.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-replication-groups.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/index.html#cli-aws-elasticache) ]

# describe-replication-groups

## Description

Returns information about a particular replication group. If no identifier is specified, `DescribeReplicationGroups` returns information about all replication groups.

### Note

This operation is valid for Valkey or Redis OSS only.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReplicationGroups)

`describe-replication-groups` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ReplicationGroups`

## Synopsis

```
describe-replication-groups
[--replication-group-id <value>]
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

`--replication-group-id` (string)

The identifier for the replication group to be described. This parameter is not case sensitive.

If you do not specify this parameter, information about all replication groups is returned.

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

**To return a list of replication group details**

The following `describe-replication-groups` example returns the replication groups.

```
aws elasticache describe-replication-groups
```

Output:

```
{
    "ReplicationGroups": [
        {
            "ReplicationGroupId": "my-cluster",
            "Description": "mycluster",
            "Status": "available",
            "PendingModifiedValues": {},
            "MemberClusters": [
                "pat-cluster-001",
                "pat-cluster-002",
                "pat-cluster-003",
                "pat-cluster-004"
            ],
            "NodeGroups": [
                {
                    "NodeGroupId": "0001",
                    "Status": "available",
                    "PrimaryEndpoint": {
                        "Address": "my-cluster.xxxxih.ng.0001.usw2.cache.amazonaws.com",
                        "Port": 6379
                    },
                    "ReaderEndpoint": {
                        "Address": "my-cluster-ro.xxxxih.ng.0001.usw2.cache.amazonaws.com",
                        "Port": 6379
                    },
                    "NodeGroupMembers": [
                        {
                            "CacheClusterId": "my-cluster-001",
                            "CacheNodeId": "0001",
                            "ReadEndpoint": {
                                "Address": "pat-cluster-001.xxxih.0001.usw2.cache.amazonaws.com",
                                "Port": 6379
                            },
                            "PreferredAvailabilityZone": "us-west-2a",
                            "CurrentRole": "primary"
                        },
                        {
                            "CacheClusterId": "my-cluster-002",
                            "CacheNodeId": "0001",
                            "ReadEndpoint": {
                                "Address": "pat-cluster-002.xxxxih.0001.usw2.cache.amazonaws.com",
                                "Port": 6379
                            },
                            "PreferredAvailabilityZone": "us-west-2a",
                            "CurrentRole": "replica"
                        },
                        {
                            "CacheClusterId": "my-cluster-003",
                            "CacheNodeId": "0001",
                            "ReadEndpoint": {
                                "Address": "pat-cluster-003.xxxxih.0001.usw2.cache.amazonaws.com",
                                "Port": 6379
                            },
                            "PreferredAvailabilityZone": "us-west-2a",
                            "CurrentRole": "replica"
                        },
                        {
                            "CacheClusterId": "my-cluster-004",
                            "CacheNodeId": "0001",
                            "ReadEndpoint": {
                                "Address": "pat-cluster-004.xxxih.0001.usw2.cache.amazonaws.com",
                                "Port": 6379
                            },
                            "PreferredAvailabilityZone": "us-west-2a",
                            "CurrentRole": "replica"
                        }
                    ]
                }
            ],
            "AutomaticFailover": "disabled",
            "SnapshotRetentionLimit": 0,
            "SnapshotWindow": "07:30-08:30",
            "ClusterEnabled": false,
            "CacheNodeType": "cache.r5.xlarge",
            "AuthTokenEnabled": false,
            "TransitEncryptionEnabled": false,
            "AtRestEncryptionEnabled": false,
            "ARN": "arn:aws:elasticache:us-west-2:xxxxxxxxxxx152:replicationgroup:my-cluster",
            "LogDeliveryConfigurations": [
                {
                    "LogType": "slow-log",
                    "DestinationType": "cloudwatch-logs",
                    "DestinationDetails": {
                        "CloudWatchLogsDetails": {
                            "LogGroup": "test-log"
                        }
                    },
                    "LogFormat": "json",
                    "Status": "active"
                }
            ]
        }
    ]
}
```

For more information, see [Managing Clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.html) in the *Elasticache User Guide*.

## Output

Marker -> (string)

Provides an identifier to allow retrieval of paginated results.

ReplicationGroups -> (list)

A list of replication groups. Each item in the list contains detailed information about one replication group.

(structure)

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