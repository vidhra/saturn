# create-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/create-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/create-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [memorydb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/index.html#cli-aws-memorydb) ]

# create-snapshot

## Description

Creates a copy of an entire cluster at a specific moment in time.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/memorydb-2021-01-01/CreateSnapshot)

## Synopsis

```
create-snapshot
--cluster-name <value>
--snapshot-name <value>
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

`--cluster-name` (string)

The snapshot is created from this cluster.

`--snapshot-name` (string)

A name for the snapshot being created.

`--kms-key-id` (string)

The ID of the KMS key used to encrypt the snapshot.

`--tags` (list)

A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.

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

**To create a snapshot**

The following `create-snapshot` example creates a snapshot.

```
aws memorydb create-snapshot \
    --cluster-name my-cluster \
    --snapshot-name my-cluster-snapshot
```

Output:

```
{
    "Snapshot": {
        "Name": "my-cluster-snapshot1",
        "Status": "creating",
        "Source": "manual",
        "ARN": "arn:aws:memorydb:us-east-1:49165xxxxxx:snapshot/my-cluster-snapshot",
        "ClusterConfiguration": {
            "Name": "my-cluster",
            "Description": "",
            "NodeType": "db.r6g.large",
            "EngineVersion": "6.2",
            "MaintenanceWindow": "wed:03:00-wed:04:00",
            "Port": 6379,
            "ParameterGroupName": "default.memorydb-redis6",
            "SubnetGroupName": "my-sg",
            "VpcId": "vpc-862xxxxc",
            "SnapshotRetentionLimit": 0,
            "SnapshotWindow": "04:30-05:30",
            "NumShards": 2
        }
    }
}
```

For more information, see [Making manual snapshots](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-manual.html) in the *MemoryDB User Guide*.

## Output

Snapshot -> (structure)

The newly-created snapshot.

Name -> (string)

The name of the snapshot

Status -> (string)

The status of the snapshot. Valid values: creating | available | restoring | copying | deleting.

Source -> (string)

Indicates whether the snapshot is from an automatic backup (automated) or was created manually (manual).

KmsKeyId -> (string)

The ID of the KMS key used to encrypt the snapshot.

ARN -> (string)

The ARN (Amazon Resource Name) of the snapshot.

ClusterConfiguration -> (structure)

The configuration of the cluster from which the snapshot was taken

Name -> (string)

The name of the cluster

Description -> (string)

The description of the cluster configuration

NodeType -> (string)

The node type used for the cluster

Engine -> (string)

The name of the engine used by the cluster configuration.

EngineVersion -> (string)

The Redis OSS engine version used by the cluster

MaintenanceWindow -> (string)

The specified maintenance window for the cluster

TopicArn -> (string)

The Amazon Resource Name (ARN) of the SNS notification topic for the cluster

Port -> (integer)

The port used by the cluster

ParameterGroupName -> (string)

The name of parameter group used by the cluster

SubnetGroupName -> (string)

The name of the subnet group used by the cluster

VpcId -> (string)

The ID of the VPC the cluster belongs to

SnapshotRetentionLimit -> (integer)

The snapshot retention limit set by the cluster

SnapshotWindow -> (string)

The snapshot window set by the cluster

NumShards -> (integer)

The number of shards in the cluster

Shards -> (list)

The list of shards in the cluster

(structure)

Provides details of a shard in a snapshot

Name -> (string)

The name of the shard

Configuration -> (structure)

The configuration details of the shard

Slots -> (string)

A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format startkey-endkey.

ReplicaCount -> (integer)

The number of read replica nodes in this shard.

Size -> (string)

The size of the shardâs snapshot

SnapshotCreationTime -> (timestamp)

The date and time that the shardâs snapshot was created

MultiRegionParameterGroupName -> (string)

The name of the multi-Region parameter group associated with the cluster configuration.

MultiRegionClusterName -> (string)

The name for the multi-Region cluster associated with the cluster configuration.

DataTiering -> (string)

Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes. For more information, see [Data tiering](https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html) .