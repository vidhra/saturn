# delete-global-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-global-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-global-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptune](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/index.html#cli-aws-neptune) ]

# delete-global-cluster

## Description

Deletes a global database. The primary and all secondary clusters must already be detached or deleted first.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DeleteGlobalCluster)

## Synopsis

```
delete-global-cluster
--global-cluster-identifier <value>
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

The cluster identifier of the global database cluster being deleted.

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

Contains the details of an Amazon Neptune global database.

This data type is used as a response element for the  CreateGlobalCluster ,  DescribeGlobalClusters ,  ModifyGlobalCluster ,  DeleteGlobalCluster ,  FailoverGlobalCluster , and  RemoveFromGlobalCluster actions.

GlobalClusterIdentifier -> (string)

Contains a user-supplied global database cluster identifier. This identifier is the unique key that identifies a global database.

GlobalClusterResourceId -> (string)

An immutable identifier for the global database that is unique within in all regions. This identifier is found in CloudTrail log entries whenever the KMS key for the DB cluster is accessed.

GlobalClusterArn -> (string)

The Amazon Resource Name (ARN) for the global database.

Status -> (string)

Specifies the current state of this global database.

Engine -> (string)

The Neptune database engine used by the global database (`"neptune"` ).

EngineVersion -> (string)

The Neptune engine version used by the global database.

StorageEncrypted -> (boolean)

The storage encryption setting for the global database.

DeletionProtection -> (boolean)

The deletion protection setting for the global database.

GlobalClusterMembers -> (list)

A list of cluster ARNs and instance ARNs for all the DB clusters that are part of the global database.

(structure)

A data structure with information about any primary and secondary clusters associated with an Neptune global database.

DBClusterArn -> (string)

The Amazon Resource Name (ARN) for each Neptune cluster.

Readers -> (list)

The Amazon Resource Name (ARN) for each read-only secondary cluster associated with the Neptune global database.

(string)

IsWriter -> (boolean)

Specifies whether the Neptune cluster is the primary cluster (that is, has read-write capability) for the Neptune global database with which it is associated.

FailoverState -> (structure)

A data object containing all properties for the current state of an in-process or pending switchover or failover process for this global cluster (Neptune global database). This object is empty unless the `SwitchoverGlobalCluster` or `FailoverGlobalCluster` operation was called on this global cluster.

Status -> (string)

The current status of the global cluster. Possible values are as follows:

- pending â The service received a request to switch over or fail over the global cluster. The global clusterâs primary DB cluster and the specified secondary DB cluster are being verified before the operation starts.
- failing-over â Neptune is promoting the chosen secondary Neptune DB cluster to become the new primary DB cluster to fail over the global cluster.
- cancelling â The request to switch over or fail over the global cluster was cancelled and the primary Neptune DB cluster and the selected secondary Neptune DB cluster are returning to their previous states.
- switching-over â This status covers the range of Neptune internal operations that take place during the switchover process, such as demoting the primary Neptune DB cluster, promoting the secondary Neptune DB cluster, and synchronizing replicas.

FromDbClusterArn -> (string)

The Amazon Resource Name (ARN) of the Neptune DB cluster that is currently being demoted, and which is associated with this state.

ToDbClusterArn -> (string)

The Amazon Resource Name (ARN) of the Neptune DB cluster that is currently being promoted, and which is associated with this state.

IsDataLossAllowed -> (boolean)

Indicates whether the operation is a global switchover or a global failover. If data loss is allowed, then the operation is a global failover. Otherwise, itâs a switchover.