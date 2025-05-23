# describe-clustersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/describe-clusters.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/describe-clusters.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [memorydb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/index.html#cli-aws-memorydb) ]

# describe-clusters

## Description

Returns information about all provisioned clusters if no cluster identifier is specified, or about a specific cluster if a cluster name is supplied.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/memorydb-2021-01-01/DescribeClusters)

`describe-clusters` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Clusters`

## Synopsis

```
describe-clusters
[--cluster-name <value>]
[--show-shard-details | --no-show-shard-details]
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

`--cluster-name` (string)

The name of the cluster.

`--show-shard-details` | `--no-show-shard-details` (boolean)

An optional flag that can be included in the request to retrieve information about the individual shard(s).

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

**To return a list of clusters**

The following describe-clusters` returns a list of clusters.

```
aws memorydb describe-clusters
```

Output:

```
{
    "Clusters": [
        {
                "Name": "my-cluster",
                "Status": "available",
                "NumberOfShards": 2,
                "ClusterEndpoint": {
                    "Address": "clustercfg.my-cluster.llru6f.memorydb.us-east-1.amazonaws.com",
                    "Port": 6379
                },
                "NodeType": "db.r6g.large",
                "EngineVersion": "6.2",
                "EnginePatchVersion": "6.2.6",
                "ParameterGroupName": "default.memorydb-redis6",
                "ParameterGroupStatus": "in-sync",
                "SecurityGroups": [
                    {
                        "SecurityGroupId": "sg-0a1434xxxxxc9fae",
                        "Status": "active"
                    }
                ],
                "SubnetGroupName": "pat-sg",
                "TLSEnabled": true,
                "ARN": "arn:aws:memorydb:us-east-1:49165xxxxxx:cluster/my-cluster",
                "SnapshotRetentionLimit": 0,
                "MaintenanceWindow": "wed:03:00-wed:04:00",
                "SnapshotWindow": "04:30-05:30",
                "ACLName": "my-acl",
                "AutoMinorVersionUpgrade": true
        }
    ]
}
```

For more information, see [Managing clusters](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.html) in the *MemoryDB User Guide*.

## Output

NextToken -> (string)

An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.

Clusters -> (list)

A list of clusters

(structure)

Contains all of the attributes of a specific cluster.

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