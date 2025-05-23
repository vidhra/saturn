# get-network-routesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-network-routes.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-network-routes.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [networkmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/index.html#cli-aws-networkmanager) ]

# get-network-routes

## Description

Gets the network routes of the specified global network.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/networkmanager-2019-07-05/GetNetworkRoutes)

## Synopsis

```
get-network-routes
--global-network-id <value>
--route-table-identifier <value>
[--exact-cidr-matches <value>]
[--longest-prefix-matches <value>]
[--subnet-of-matches <value>]
[--supernet-of-matches <value>]
[--prefix-list-ids <value>]
[--states <value>]
[--types <value>]
[--destination-filters <value>]
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

`--global-network-id` (string)

The ID of the global network.

`--route-table-identifier` (structure)

The ID of the route table.

TransitGatewayRouteTableArn -> (string)

The ARN of the transit gateway route table for the attachment request. For example, `"TransitGatewayRouteTableArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway-route-table/tgw-rtb-9876543210123456"` .

CoreNetworkSegmentEdge -> (structure)

The segment edge in a core network.

CoreNetworkId -> (string)

The ID of a core network.

SegmentName -> (string)

The name of the segment edge.

EdgeLocation -> (string)

The Region where the segment edge is located.

CoreNetworkNetworkFunctionGroup -> (structure)

The route table identifier associated with the network function group.

CoreNetworkId -> (string)

The ID of the core network.

NetworkFunctionGroupName -> (string)

The network function group name.

EdgeLocation -> (string)

The location for the core network edge.

Shorthand Syntax:

```
TransitGatewayRouteTableArn=string,CoreNetworkSegmentEdge={CoreNetworkId=string,SegmentName=string,EdgeLocation=string},CoreNetworkNetworkFunctionGroup={CoreNetworkId=string,NetworkFunctionGroupName=string,EdgeLocation=string}
```

JSON Syntax:

```
{
  "TransitGatewayRouteTableArn": "string",
  "CoreNetworkSegmentEdge": {
    "CoreNetworkId": "string",
    "SegmentName": "string",
    "EdgeLocation": "string"
  },
  "CoreNetworkNetworkFunctionGroup": {
    "CoreNetworkId": "string",
    "NetworkFunctionGroupName": "string",
    "EdgeLocation": "string"
  }
}
```

`--exact-cidr-matches` (list)

An exact CIDR block.

(string)

Syntax:

```
"string" "string" ...
```

`--longest-prefix-matches` (list)

The most specific route that matches the traffic (longest prefix match).

(string)

Syntax:

```
"string" "string" ...
```

`--subnet-of-matches` (list)

The routes with a subnet that match the specified CIDR filter.

(string)

Syntax:

```
"string" "string" ...
```

`--supernet-of-matches` (list)

The routes with a CIDR that encompasses the CIDR filter. Example: If you specify 10.0.1.0/30, then the result returns 10.0.1.0/29.

(string)

Syntax:

```
"string" "string" ...
```

`--prefix-list-ids` (list)

The IDs of the prefix lists.

(string)

Syntax:

```
"string" "string" ...
```

`--states` (list)

The route states.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  ACTIVE
  BLACKHOLE
```

`--types` (list)

The route types.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  PROPAGATED
  STATIC
```

`--destination-filters` (map)

Filter by route table destination. Possible Values: TRANSIT_GATEWAY_ATTACHMENT_ID, RESOURCE_ID, or RESOURCE_TYPE.

key -> (string)

value -> (list)

(string)

Shorthand Syntax:

```
KeyName1=string,string,KeyName2=string,string
```

JSON Syntax:

```
{"string": ["string", ...]
  ...}
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

RouteTableArn -> (string)

The ARN of the route table.

CoreNetworkSegmentEdge -> (structure)

Describes a core network segment edge.

CoreNetworkId -> (string)

The ID of a core network.

SegmentName -> (string)

The name of the segment edge.

EdgeLocation -> (string)

The Region where the segment edge is located.

RouteTableType -> (string)

The route table type.

RouteTableTimestamp -> (timestamp)

The route table creation time.

NetworkRoutes -> (list)

The network routes.

(structure)

Describes a network route.

DestinationCidrBlock -> (string)

A unique identifier for the route, such as a CIDR block.

Destinations -> (list)

The destinations.

(structure)

Describes the destination of a network route.

CoreNetworkAttachmentId -> (string)

The ID of a core network attachment.

TransitGatewayAttachmentId -> (string)

The ID of the transit gateway attachment.

SegmentName -> (string)

The name of the segment.

NetworkFunctionGroupName -> (string)

The network function group name associated with the destination.

EdgeLocation -> (string)

The edge location for the network destination.

ResourceType -> (string)

The resource type.

ResourceId -> (string)

The ID of the resource.

PrefixListId -> (string)

The ID of the prefix list.

State -> (string)

The route state. The possible values are `active` and `blackhole` .

Type -> (string)

The route type. The possible values are `propagated` and `static` .