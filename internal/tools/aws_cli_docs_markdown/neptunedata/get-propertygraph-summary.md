# get-propertygraph-summaryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/get-propertygraph-summary.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/get-propertygraph-summary.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptunedata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/index.html#cli-aws-neptunedata) ]

# get-propertygraph-summary

## Description

Gets a graph summary for a property graph.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:GetGraphSummary](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getgraphsummary) IAM action in that cluster.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptunedata-2023-08-01/GetPropertygraphSummary)

## Synopsis

```
get-propertygraph-summary
[--mode <value>]
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

`--mode` (string)

Mode can take one of two values: `BASIC` (the default), and `DETAILED` .

Possible values:

- `basic`
- `detailed`

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

statusCode -> (integer)

The HTTP return code of the request. If the request succeeded, the code is 200.

payload -> (structure)

Payload containing the property graph summary response.

version -> (string)

The version of this graph summary response.

lastStatisticsComputationTime -> (timestamp)

The timestamp, in ISO 8601 format, of the time at which Neptune last computed statistics.

graphSummary -> (structure)

The graph summary.

numNodes -> (long)

The number of nodes in the graph.

numEdges -> (long)

The number of edges in the graph.

numNodeLabels -> (long)

The number of distinct node labels in the graph.

numEdgeLabels -> (long)

The number of distinct edge labels in the graph.

nodeLabels -> (list)

A list of the distinct node labels in the graph.

(string)

edgeLabels -> (list)

A list of the distinct edge labels in the graph.

(string)

numNodeProperties -> (long)

A list of the distinct node properties in the graph, along with the count of nodes where each property is used.

numEdgeProperties -> (long)

The number of distinct edge properties in the graph.

nodeProperties -> (list)

The number of distinct node properties in the graph.

(map)

key -> (string)

value -> (long)

edgeProperties -> (list)

A list of the distinct edge properties in the graph, along with the count of edges where each property is used.

(map)

key -> (string)

value -> (long)

totalNodePropertyValues -> (long)

The total number of usages of all node properties.

totalEdgePropertyValues -> (long)

The total number of usages of all edge properties.

nodeStructures -> (list)

This field is only present when the requested mode is `DETAILED` . It contains a list of node structures.

(structure)

A node structure.

count -> (long)

Number of nodes that have this specific structure.

nodeProperties -> (list)

A list of the node properties present in this specific structure.

(string)

distinctOutgoingEdgeLabels -> (list)

A list of distinct outgoing edge labels present in this specific structure.

(string)

edgeStructures -> (list)

This field is only present when the requested mode is `DETAILED` . It contains a list of edge structures.

(structure)

An edge structure.

count -> (long)

The number of edges that have this specific structure.

edgeProperties -> (list)

A list of edge properties present in this specific structure.

(string)