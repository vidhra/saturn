# update-multi-region-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/update-multi-region-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/update-multi-region-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [memorydb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/index.html#cli-aws-memorydb) ]

# update-multi-region-cluster

## Description

Updates the configuration of an existing multi-Region cluster.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/memorydb-2021-01-01/UpdateMultiRegionCluster)

## Synopsis

```
update-multi-region-cluster
--multi-region-cluster-name <value>
[--node-type <value>]
[--description <value>]
[--engine-version <value>]
[--shard-configuration <value>]
[--multi-region-parameter-group-name <value>]
[--update-strategy <value>]
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

`--multi-region-cluster-name` (string)

The name of the multi-Region cluster to be updated.

`--node-type` (string)

The new node type to be used for the multi-Region cluster.

`--description` (string)

A new description for the multi-Region cluster.

`--engine-version` (string)

The new engine version to be used for the multi-Region cluster.

`--shard-configuration` (structure)

A request to configure the sharding properties of a cluster

ShardCount -> (integer)

The number of shards in the cluster

Shorthand Syntax:

```
ShardCount=integer
```

JSON Syntax:

```
{
  "ShardCount": integer
}
```

`--multi-region-parameter-group-name` (string)

The new multi-Region parameter group to be associated with the cluster.

`--update-strategy` (string)

The strategy to use for the update operation. Supported values are âcoordinatedâ or âuncoordinatedâ.

Possible values:

- `coordinated`
- `uncoordinated`

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

MultiRegionCluster -> (structure)

The status of updating the multi-Region cluster.

MultiRegionClusterName -> (string)

The name of the multi-Region cluster.

Description -> (string)

The description of the multi-Region cluster.

Status -> (string)

The current status of the multi-Region cluster.

NodeType -> (string)

The node type used by the multi-Region cluster.

Engine -> (string)

The name of the engine used by the multi-Region cluster.

EngineVersion -> (string)

The version of the engine used by the multi-Region cluster.

NumberOfShards -> (integer)

The number of shards in the multi-Region cluster.

Clusters -> (list)

The clusters in this multi-Region cluster.

(structure)

Represents a Regional cluster

ClusterName -> (string)

The name of the Regional cluster

Region -> (string)

The Region the current Regional cluster is assigned to.

Status -> (string)

The status of the Regional cluster.

ARN -> (string)

The Amazon Resource Name (ARN) the Regional cluster

MultiRegionParameterGroupName -> (string)

The name of the multi-Region parameter group associated with the cluster.

TLSEnabled -> (boolean)

Indiciates if the multi-Region cluster is TLS enabled.

ARN -> (string)

The Amazon Resource Name (ARN) of the multi-Region cluster.