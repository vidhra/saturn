# create-graphÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune-graph/create-graph.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune-graph/create-graph.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptune-graph](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune-graph/index.html#cli-aws-neptune-graph) ]

# create-graph

## Description

Creates a new Neptune Analytics graph.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptune-graph-2023-11-29/CreateGraph)

## Synopsis

```
create-graph
--graph-name <value>
[--tags <value>]
[--public-connectivity | --no-public-connectivity]
[--kms-key-identifier <value>]
[--vector-search-configuration <value>]
[--replica-count <value>]
[--deletion-protection | --no-deletion-protection]
--provisioned-memory <value>
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

`--graph-name` (string)

A name for the new Neptune Analytics graph to be created.

The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.

`--tags` (map)

Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--public-connectivity` | `--no-public-connectivity` (boolean)

Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (`true` to enable, or `false` to disable.

`--kms-key-identifier` (string)

Specifies a KMS key to use to encrypt data in the new graph.

`--vector-search-configuration` (structure)

Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as `dimension=` value. Max = 65,535

dimension -> (integer)

The number of dimensions.

Shorthand Syntax:

```
dimension=integer
```

JSON Syntax:

```
{
  "dimension": integer
}
```

`--replica-count` (integer)

The number of replicas in other AZs. Min =0, Max = 2, Default = 1.

### Warning

Additional charges equivalent to the m-NCUs selected for the graph apply for each replica.

`--deletion-protection` | `--no-deletion-protection` (boolean)

Indicates whether or not to enable deletion protection on the graph. The graph canât be deleted when deletion protection is enabled. (`true` or `false` ).

`--provisioned-memory` (integer)

The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Min = 16

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

id -> (string)

The ID of the graph.

name -> (string)

The graph name. For example: `my-graph-1` .

The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.

arn -> (string)

The ARN of the graph.

status -> (string)

The current status of the graph.

statusReason -> (string)

The reason the status was given.

createTime -> (timestamp)

The time when the graph was created.

provisionedMemory -> (integer)

The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.

Min = 16

endpoint -> (string)

The graph endpoint.

publicConnectivity -> (boolean)

Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated.

### Note

If enabling public connectivity for the first time, there will be a delay while it is enabled.

vectorSearchConfiguration -> (structure)

The vector-search configuration for the graph, which specifies the vector dimension to use in the vector index, if any.

dimension -> (integer)

The number of dimensions.

replicaCount -> (integer)

The number of replicas in other AZs.

Default: If not specified, the default value is 1.

kmsKeyIdentifier -> (string)

Specifies the KMS key used to encrypt data in the new graph.

sourceSnapshotId -> (string)

The ID of the source graph.

deletionProtection -> (boolean)

A value that indicates whether the graph has deletion protection enabled. The graph canât be deleted when deletion protection is enabled.

buildNumber -> (string)

The build number of the graph software.