# create-global-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-global-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-global-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [docdb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/index.html#cli-aws-docdb) ]

# create-global-cluster

## Description

Creates an Amazon DocumentDB global cluster that can span multiple multiple Amazon Web Services Regions. The global cluster contains one primary cluster with read-write capability, and up-to give read-only secondary clusters. Global clusters uses storage-based fast replication across regions with latencies less than one second, using dedicated infrastructure with no impact to your workloadâs performance.

You can create a global cluster that is initially empty, and then add a primary and a secondary to it. Or you can specify an existing cluster during the create operation, and this cluster becomes the primary of the global cluster.

### Note

This action only applies to Amazon DocumentDB clusters.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/CreateGlobalCluster)

## Synopsis

```
create-global-cluster
--global-cluster-identifier <value>
[--source-db-cluster-identifier <value>]
[--engine <value>]
[--engine-version <value>]
[--deletion-protection | --no-deletion-protection]
[--database-name <value>]
[--storage-encrypted | --no-storage-encrypted]
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

`--global-cluster-identifier` (string)

The cluster identifier of the new global cluster.

`--source-db-cluster-identifier` (string)

The Amazon Resource Name (ARN) to use as the primary cluster of the global cluster. This parameter is optional.

`--engine` (string)

The name of the database engine to be used for this cluster.

`--engine-version` (string)

The engine version of the global cluster.

`--deletion-protection` | `--no-deletion-protection` (boolean)

The deletion protection setting for the new global cluster. The global cluster canât be deleted when deletion protection is enabled.

`--database-name` (string)

The name for your database of up to 64 alpha-numeric characters. If you do not provide a name, Amazon DocumentDB will not create a database in the global cluster you are creating.

`--storage-encrypted` | `--no-storage-encrypted` (boolean)

The storage encryption setting for the new global cluster.

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

## Output

GlobalCluster -> (structure)

A data type representing an Amazon DocumentDB global cluster.

GlobalClusterIdentifier -> (string)

Contains a user-supplied global cluster identifier. This identifier is the unique key that identifies a global cluster.

GlobalClusterResourceId -> (string)

The Amazon Web Services Region-unique, immutable identifier for the global database cluster. This identifier is found in CloudTrail log entries whenever the KMS customer master key (CMK) for the cluster is accessed.

GlobalClusterArn -> (string)

The Amazon Resource Name (ARN) for the global cluster.

Status -> (string)

Specifies the current state of this global cluster.

Engine -> (string)

The Amazon DocumentDB database engine used by the global cluster.

EngineVersion -> (string)

Indicates the database engine version.

DatabaseName -> (string)

The default database name within the new global cluster.

StorageEncrypted -> (boolean)

The storage encryption setting for the global cluster.

DeletionProtection -> (boolean)

The deletion protection setting for the new global cluster.

GlobalClusterMembers -> (list)

The list of cluster IDs for secondary clusters within the global cluster. Currently limited to one item.

(structure)

A data structure with information about any primary and secondary clusters associated with an Amazon DocumentDB global clusters.

DBClusterArn -> (string)

The Amazon Resource Name (ARN) for each Amazon DocumentDB cluster.

Readers -> (list)

The Amazon Resource Name (ARN) for each read-only secondary cluster associated with the Aurora global cluster.

(string)

IsWriter -> (boolean)

Specifies whether the Amazon DocumentDB cluster is the primary cluster (that is, has read-write capability) for the Amazon DocumentDB global cluster with which it is associated.