# update-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [medialive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/index.html#cli-aws-medialive) ]

# update-cluster

## Description

Change the settings for a Cluster.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/UpdateCluster)

## Synopsis

```
update-cluster
--cluster-id <value>
[--name <value>]
[--network-settings <value>]
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

`--cluster-id` (string)
The ID of the cluster

`--name` (string)
Include this parameter only if you want to change the current name of the Cluster. Specify a name that is unique in the AWS account. You canât change the name. Names are case-sensitive.

`--network-settings` (structure)
Include this property only if you want to change the current connections between the Nodes in the Cluster and the Networks the Cluster is associated with.DefaultRoute -> (string)

Include this parameter only if you want to change the default route for the Cluster. Specify one network interface as the default route for traffic to and from the node. MediaLive Anywhere uses this default when the destination for the traffic isnât covered by the route table for any of the networks. Specify the value of the appropriate logicalInterfaceName parameter that you create in the interfaceMappings.

InterfaceMappings -> (list)

An array of interfaceMapping objects for this Cluster. Include this parameter only if you want to change the interface mappings for the Cluster. Typically, you change the interface mappings only to fix an error you made when creating the mapping. In an update request, make sure that you enter the entire set of mappings again, not just the mappings that you want to add or change. You define this mapping so that the mapping can be used by all the Nodes. Each mapping logically connects one interface on the nodes with one Network. Each mapping consists of a pair of parameters. The logicalInterfaceName parameter creates a logical name for the Node interface that handles a specific type of traffic. For example, my-Inputs-Interface. The networkID parameter refers to the ID of the network. When you create the Nodes in this Cluster, you will associate the logicalInterfaceName with the appropriate physical interface.

(structure)

Placeholder documentation for InterfaceMappingUpdateRequest

LogicalInterfaceName -> (string)

The logical name for one interface (on every Node) that handles a specific type of traffic. We recommend that the name hints at the physical interface it applies to. For example, it could refer to the traffic that the physical interface handles. For example, my-Inputs-Interface.

NetworkId -> (string)

The ID of the network that you want to connect to the specified logicalInterfaceName. You can use the ListNetworks operation to discover all the IDs.

Shorthand Syntax:

```
DefaultRoute=string,InterfaceMappings=[{LogicalInterfaceName=string,NetworkId=string},{LogicalInterfaceName=string,NetworkId=string}]
```

JSON Syntax:

```
{
  "DefaultRoute": "string",
  "InterfaceMappings": [
    {
      "LogicalInterfaceName": "string",
      "NetworkId": "string"
    }
    ...
  ]
}
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

## Output

Arn -> (string)

The ARN of the Cluster.

ChannelIds -> (list)

An array of the IDs of the Channels that are associated with this Cluster. One Channel is associated with the Cluster as follows: A Channel belongs to a ChannelPlacementGroup. A ChannelPlacementGroup is attached to a Node. A Node belongs to a Cluster.

(string)

Placeholder documentation for __string

ClusterType -> (string)

The hardware type for the Cluster

Id -> (string)

The unique ID of the Cluster.

Name -> (string)

The user-specified name of the Cluster.

NetworkSettings -> (structure)

Network settings that connect the Nodes in the Cluster to one or more of the Networks that the Cluster is associated with.

DefaultRoute -> (string)

The network interface that is the default route for traffic to and from the node. MediaLive Anywhere uses this default when the destination for the traffic isnât covered by the route table for any of the networks. Specify the value of the appropriate logicalInterfaceName parameter that you create in the interfaceMappings.

InterfaceMappings -> (list)

An array of interfaceMapping objects for this Cluster. Each mapping logically connects one interface on the nodes with one Network. You need only one mapping for each interface because all the Nodes share the mapping.

(structure)

Used in ClusterNetworkSettings

LogicalInterfaceName -> (string)

The logical name for one interface (on every Node) that handles a specific type of traffic. We recommend that the name hints at the physical interface it applies to. For example, it could refer to the traffic that the physical interface handles. For example, my-Inputs-Interface.

NetworkId -> (string)

The ID of the network that you want to connect to the specified logicalInterfaceName.

State -> (string)

The current state of the Cluster.