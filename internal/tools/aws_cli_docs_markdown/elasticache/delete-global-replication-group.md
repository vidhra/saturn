# delete-global-replication-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-global-replication-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-global-replication-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/index.html#cli-aws-elasticache) ]

# delete-global-replication-group

## Description

Deleting a Global datastore is a two-step process:

- First, you must  DisassociateGlobalReplicationGroup to remove the secondary clusters in the Global datastore.
- Once the Global datastore contains only the primary cluster, you can use the `DeleteGlobalReplicationGroup` API to delete the Global datastore while retainining the primary cluster using `RetainPrimaryReplicationGroup=true` .

Since the Global Datastore has only a primary cluster, you can delete the Global Datastore while retaining the primary by setting `RetainPrimaryReplicationGroup=true` . The primary cluster is never deleted when deleting a Global Datastore. It can only be deleted when it no longer is associated with any Global Datastore.

When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the selected resources; you cannot cancel or revert this operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DeleteGlobalReplicationGroup)

## Synopsis

```
delete-global-replication-group
--global-replication-group-id <value>
--retain-primary-replication-group | --no-retain-primary-replication-group
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

`--global-replication-group-id` (string)

The name of the Global datastore

`--retain-primary-replication-group` | `--no-retain-primary-replication-group` (boolean)

The primary replication group is retained as a standalone replication group.

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

**To delete a global replication group**

The following `delete-global-replication-group` example deletes a new global replication group.

```
aws elasticache delete-global-replication-group \
    --global-replication-group-id my-global-replication-group \
    --retain-primary-replication-group
```

Output:

```
{
    "GlobalReplicationGroup": {
        "GlobalReplicationGroupId": "sgaui-my-grg",
        "GlobalReplicationGroupDescription": "my-grg",
        "Status": "deleting",
        "CacheNodeType": "cache.r5.large",
        "Engine": "redis",
        "EngineVersion": "5.0.6",
        "Members": [
            {
                "ReplicationGroupId": "my-cluster-grg",
                "ReplicationGroupRegion": "us-west-2",
                "Role": "PRIMARY",
                "AutomaticFailover": "enabled",
                "Status": "associated"
            }
        ],
        "ClusterEnabled": false,
        "AuthTokenEnabled": false,
        "TransitEncryptionEnabled": false,
        "AtRestEncryptionEnabled": false
    }
}
```

For more information, see [Replication Across AWS Regions Using Global Datastore](https://docs.amazonaws.cn/en_us/AmazonElastiCache/latest/red-ug/Redis-Global-Datastore.html) in the *Elasticache User Guide*.

## Output

GlobalReplicationGroup -> (structure)

Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different Amazon region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.

- The **GlobalReplicationGroupIdSuffix** represents the name of the Global datastore, which is what you use to associate a secondary cluster.

GlobalReplicationGroupId -> (string)

The name of the Global datastore

GlobalReplicationGroupDescription -> (string)

The optional description of the Global datastore

Status -> (string)

The status of the Global datastore

CacheNodeType -> (string)

The cache node type of the Global datastore

Engine -> (string)

The ElastiCache engine. For Valkey or Redis OSS only.

EngineVersion -> (string)

The ElastiCache engine version.

Members -> (list)

The replication groups that comprise the Global datastore.

(structure)

A member of a Global datastore. It contains the Replication Group Id, the Amazon region and the role of the replication group.

ReplicationGroupId -> (string)

The replication group id of the Global datastore member.

ReplicationGroupRegion -> (string)

The Amazon region of the Global datastore member.

Role -> (string)

Indicates the role of the replication group, primary or secondary.

AutomaticFailover -> (string)

Indicates whether automatic failover is enabled for the replication group.

Status -> (string)

The status of the membership of the replication group.

ClusterEnabled -> (boolean)

A flag that indicates whether the Global datastore is cluster enabled.

GlobalNodeGroups -> (list)

Indicates the slot configuration and global identifier for each slice group.

(structure)

Indicates the slot configuration and global identifier for a slice group.

GlobalNodeGroupId -> (string)

The name of the global node group

Slots -> (string)

The keyspace for this node group

AuthTokenEnabled -> (boolean)

A flag that enables using an `AuthToken` (password) when issuing Valkey or Redis OSS commands.

Default: `false`

TransitEncryptionEnabled -> (boolean)

A flag that enables in-transit encryption when set to true.

**Required:** Only available when creating a replication group in an Amazon VPC using Redis OSS version `3.2.6` , `4.x` or later.

AtRestEncryptionEnabled -> (boolean)

A flag that enables encryption at rest when set to `true` .

You cannot modify the value of `AtRestEncryptionEnabled` after the replication group is created. To enable encryption at rest on a replication group you must set `AtRestEncryptionEnabled` to `true` when you create the replication group.

**Required:** Only available when creating a replication group in an Amazon VPC using Redis OSS version `3.2.6` , `4.x` or later.

ARN -> (string)

The ARN (Amazon Resource Name) of the global replication group.