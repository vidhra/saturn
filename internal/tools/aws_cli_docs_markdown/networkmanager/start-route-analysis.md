# start-route-analysisÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/start-route-analysis.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/start-route-analysis.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [networkmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/index.html#cli-aws-networkmanager) ]

# start-route-analysis

## Description

Starts analyzing the routing path between the specified source and destination. For more information, see [Route Analyzer](https://docs.aws.amazon.com/vpc/latest/tgw/route-analyzer.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/networkmanager-2019-07-05/StartRouteAnalysis)

## Synopsis

```
start-route-analysis
--global-network-id <value>
--source <value>
--destination <value>
[--include-return-path | --no-include-return-path]
[--use-middleboxes | --no-use-middleboxes]
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

`--source` (structure)

The source from which traffic originates.

TransitGatewayAttachmentArn -> (string)

The ARN of the transit gateway attachment.

IpAddress -> (string)

The IP address.

Shorthand Syntax:

```
TransitGatewayAttachmentArn=string,IpAddress=string
```

JSON Syntax:

```
{
  "TransitGatewayAttachmentArn": "string",
  "IpAddress": "string"
}
```

`--destination` (structure)

The destination.

TransitGatewayAttachmentArn -> (string)

The ARN of the transit gateway attachment.

IpAddress -> (string)

The IP address.

Shorthand Syntax:

```
TransitGatewayAttachmentArn=string,IpAddress=string
```

JSON Syntax:

```
{
  "TransitGatewayAttachmentArn": "string",
  "IpAddress": "string"
}
```

`--include-return-path` | `--no-include-return-path` (boolean)

Indicates whether to analyze the return path. The default is `false` .

`--use-middleboxes` | `--no-use-middleboxes` (boolean)

Indicates whether to include the location of middlebox appliances in the route analysis. The default is `false` .

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

**To start route analysis**

The following `start-route-analysis` example starts the analysis between a source and destination, including the optional `include-return-path`.

```
aws networkmanager start-route-analysis \
    --global-network-id global-network-00aa0aaa0b0aaa000 \
    --source TransitGatewayAttachmentArn=arn:aws:ec2:us-east-1:503089527312:transit-gateway-attachment/tgw-attach-0d4a2d491bf68c093,IpAddress=10.0.0.0 \
    --destination TransitGatewayAttachmentArn=arn:aws:ec2:us-west-1:503089527312:transit-gateway-attachment/tgw-attach-002577f30bb181742,IpAddress=11.0.0.0 \
    --include-return-path
```

Output:

```
{
    "RouteAnalysis": {
        "GlobalNetworkId": "global-network-00aa0aaa0b0aaa000
        "OwnerAccountId": "1111222233333",
        "RouteAnalysisId": "a1873de1-273c-470c-1a2bc2345678",
        "StartTimestamp": 1695760154.0,
        "Status": "RUNNING",
        "Source": {
            "TransitGatewayAttachmentArn": "arn:aws:ec2:us-east-1:111122223333:transit-gateway-attachment/tgw-attach-1234567890abcdef0,
            "TransitGatewayArn": "arn:aws:ec2:us-east-1:111122223333:transit-gateway/tgw-abcdef01234567890",
            "IpAddress": "10.0.0.0"
        },
        "Destination": {
            "TransitGatewayAttachmentArn": "arn:aws:ec2:us-west-1:555555555555:transit-gateway-attachment/tgw-attach-021345abcdef6789",
            "TransitGatewayArn": "arn:aws:ec2:us-west-1:111122223333:transit-gateway/tgw-09876543210fedcba0",
            "IpAddress": "11.0.0.0"
        },
        "IncludeReturnPath": true,
        "UseMiddleboxes": false
    }
}
```

For more information, see [Route Analyzer](https://docs.aws.amazon.com/network-manager/latest/tgwnm/route-analyzer.html) in the *AWS Global Networks for Transit Gateways User Guide*.

## Output

RouteAnalysis -> (structure)

The route analysis.

GlobalNetworkId -> (string)

The ID of the global network.

OwnerAccountId -> (string)

The ID of the AWS account that created the route analysis.

RouteAnalysisId -> (string)

The ID of the route analysis.

StartTimestamp -> (timestamp)

The time that the analysis started.

Status -> (string)

The status of the route analysis.

Source -> (structure)

The source.

TransitGatewayAttachmentArn -> (string)

The ARN of the transit gateway attachment.

TransitGatewayArn -> (string)

The ARN of the transit gateway.

IpAddress -> (string)

The IP address.

Destination -> (structure)

The destination.

TransitGatewayAttachmentArn -> (string)

The ARN of the transit gateway attachment.

TransitGatewayArn -> (string)

The ARN of the transit gateway.

IpAddress -> (string)

The IP address.

IncludeReturnPath -> (boolean)

Indicates whether to analyze the return path. The return path is not analyzed if the forward path analysis does not succeed.

UseMiddleboxes -> (boolean)

Indicates whether to include the location of middlebox appliances in the route analysis.

ForwardPath -> (structure)

The forward path.

CompletionStatus -> (structure)

The status of the analysis at completion.

ResultCode -> (string)

The result of the analysis. If the status is `NOT_CONNECTED` , check the reason code.

ReasonCode -> (string)

The reason code. Available only if a connection is not found.

- `BLACKHOLE_ROUTE_FOR_DESTINATION_FOUND` - Found a black hole route with the destination CIDR block.
- `CYCLIC_PATH_DETECTED` - Found the same resource multiple times while traversing the path.
- `INACTIVE_ROUTE_FOR_DESTINATION_FOUND` - Found an inactive route with the destination CIDR block.
- `MAX_HOPS_EXCEEDED` - Analysis exceeded 64 hops without finding the destination.
- `ROUTE_NOT_FOUND` - Cannot find a route table with the destination CIDR block.
- `TGW_ATTACH_ARN_NO_MATCH` - Found an attachment, but not with the correct destination ARN.
- `TGW_ATTACH_NOT_FOUND` - Cannot find an attachment.
- `TGW_ATTACH_NOT_IN_TGW` - Found an attachment, but not to the correct transit gateway.
- `TGW_ATTACH_STABLE_ROUTE_TABLE_NOT_FOUND` - The state of the route table association is not associated.

ReasonContext -> (map)

Additional information about the path. Available only if a connection is not found.

key -> (string)

value -> (string)

Path -> (list)

The route analysis path.

(structure)

Describes a path component.

Sequence -> (integer)

The sequence number in the path. The destination is 0.

Resource -> (structure)

The resource.

RegisteredGatewayArn -> (string)

The ARN of the gateway.

ResourceArn -> (string)

The ARN of the resource.

ResourceType -> (string)

The resource type.

Definition -> (string)

Information about the resource, in JSON format. Network Manager gets this information by describing the resource using its Describe API call.

NameTag -> (string)

The value for the Name tag.

IsMiddlebox -> (boolean)

Indicates whether this is a middlebox appliance.

DestinationCidrBlock -> (string)

The destination CIDR block in the route table.

ReturnPath -> (structure)

The return path.

CompletionStatus -> (structure)

The status of the analysis at completion.

ResultCode -> (string)

The result of the analysis. If the status is `NOT_CONNECTED` , check the reason code.

ReasonCode -> (string)

The reason code. Available only if a connection is not found.

- `BLACKHOLE_ROUTE_FOR_DESTINATION_FOUND` - Found a black hole route with the destination CIDR block.
- `CYCLIC_PATH_DETECTED` - Found the same resource multiple times while traversing the path.
- `INACTIVE_ROUTE_FOR_DESTINATION_FOUND` - Found an inactive route with the destination CIDR block.
- `MAX_HOPS_EXCEEDED` - Analysis exceeded 64 hops without finding the destination.
- `ROUTE_NOT_FOUND` - Cannot find a route table with the destination CIDR block.
- `TGW_ATTACH_ARN_NO_MATCH` - Found an attachment, but not with the correct destination ARN.
- `TGW_ATTACH_NOT_FOUND` - Cannot find an attachment.
- `TGW_ATTACH_NOT_IN_TGW` - Found an attachment, but not to the correct transit gateway.
- `TGW_ATTACH_STABLE_ROUTE_TABLE_NOT_FOUND` - The state of the route table association is not associated.

ReasonContext -> (map)

Additional information about the path. Available only if a connection is not found.

key -> (string)

value -> (string)

Path -> (list)

The route analysis path.

(structure)

Describes a path component.

Sequence -> (integer)

The sequence number in the path. The destination is 0.

Resource -> (structure)

The resource.

RegisteredGatewayArn -> (string)

The ARN of the gateway.

ResourceArn -> (string)

The ARN of the resource.

ResourceType -> (string)

The resource type.

Definition -> (string)

Information about the resource, in JSON format. Network Manager gets this information by describing the resource using its Describe API call.

NameTag -> (string)

The value for the Name tag.

IsMiddlebox -> (boolean)

Indicates whether this is a middlebox appliance.

DestinationCidrBlock -> (string)

The destination CIDR block in the route table.