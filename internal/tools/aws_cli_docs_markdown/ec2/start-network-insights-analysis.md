# start-network-insights-analysisÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/start-network-insights-analysis.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/start-network-insights-analysis.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# start-network-insights-analysis

## Description

Starts analyzing the specified path. If the path is reachable, the operation returns the shortest feasible path.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/StartNetworkInsightsAnalysis)

## Synopsis

```
start-network-insights-analysis
--network-insights-path-id <value>
[--additional-accounts <value>]
[--filter-in-arns <value>]
[--filter-out-arns <value>]
[--dry-run | --no-dry-run]
[--tag-specifications <value>]
[--client-token <value>]
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

`--network-insights-path-id` (string)

The ID of the path.

`--additional-accounts` (list)

The member accounts that contain resources that the path can traverse.

(string)

Syntax:

```
"string" "string" ...
```

`--filter-in-arns` (list)

The Amazon Resource Names (ARN) of the resources that the path must traverse.

(string)

Syntax:

```
"string" "string" ...
```

`--filter-out-arns` (list)

The Amazon Resource Names (ARN) of the resources that the path will ignore.

(string)

Syntax:

```
"string" "string" ...
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--tag-specifications` (list)

The tags to apply.

(structure)

The tags to apply to a resource when the resource is being created. When you specify a tag, you must specify the resource type to tag, otherwise the request will fail.

### Note

The `Valid Values` lists all the resource types that can be tagged. However, the action youâre using might not support tagging all of these resource types. If you try to tag a resource type that is unsupported for the action youâre using, youâll get an error.

ResourceType -> (string)

The type of resource to tag on creation.

Tags -> (list)

The tags to apply to the resource.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

Shorthand Syntax:

```
ResourceType=string,Tags=[{Key=string,Value=string},{Key=string,Value=string}] ...
```

JSON Syntax:

```
[
  {
    "ResourceType": "capacity-reservation"|"client-vpn-endpoint"|"customer-gateway"|"carrier-gateway"|"coip-pool"|"declarative-policies-report"|"dedicated-host"|"dhcp-options"|"egress-only-internet-gateway"|"elastic-ip"|"elastic-gpu"|"export-image-task"|"export-instance-task"|"fleet"|"fpga-image"|"host-reservation"|"image"|"import-image-task"|"import-snapshot-task"|"instance"|"instance-event-window"|"internet-gateway"|"ipam"|"ipam-pool"|"ipam-scope"|"ipv4pool-ec2"|"ipv6pool-ec2"|"key-pair"|"launch-template"|"local-gateway"|"local-gateway-route-table"|"local-gateway-virtual-interface"|"local-gateway-virtual-interface-group"|"local-gateway-route-table-vpc-association"|"local-gateway-route-table-virtual-interface-group-association"|"natgateway"|"network-acl"|"network-interface"|"network-insights-analysis"|"network-insights-path"|"network-insights-access-scope"|"network-insights-access-scope-analysis"|"outpost-lag"|"placement-group"|"prefix-list"|"replace-root-volume-task"|"reserved-instances"|"route-table"|"security-group"|"security-group-rule"|"service-link-virtual-interface"|"snapshot"|"spot-fleet-request"|"spot-instances-request"|"subnet"|"subnet-cidr-reservation"|"traffic-mirror-filter"|"traffic-mirror-session"|"traffic-mirror-target"|"transit-gateway"|"transit-gateway-attachment"|"transit-gateway-connect-peer"|"transit-gateway-multicast-domain"|"transit-gateway-policy-table"|"transit-gateway-route-table"|"transit-gateway-route-table-announcement"|"volume"|"vpc"|"vpc-endpoint"|"vpc-endpoint-connection"|"vpc-endpoint-service"|"vpc-endpoint-service-permission"|"vpc-peering-connection"|"vpn-connection"|"vpn-gateway"|"vpc-flow-log"|"capacity-reservation-fleet"|"traffic-mirror-filter-rule"|"vpc-endpoint-connection-device-type"|"verified-access-instance"|"verified-access-group"|"verified-access-endpoint"|"verified-access-policy"|"verified-access-trust-provider"|"vpn-connection-device-type"|"vpc-block-public-access-exclusion"|"route-server"|"route-server-endpoint"|"route-server-peer"|"ipam-resource-discovery"|"ipam-resource-discovery-association"|"instance-connect-endpoint"|"verified-access-endpoint-target"|"ipam-external-resource-verification-token"|"mac-modification-task",
    "Tags": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ]
  }
  ...
]
```

`--client-token` (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [How to ensure idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html) .

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

**To analyze a path**

The following `start-network-insights-analysis` example analyzes the path between the source and destination. To view the results of the path analysis, use the `describe-network-insights-analyses` command.

```
aws ec2 start-network-insights-analysis \
    --network-insights-path-id nip-0b26f224f1d131fa8
```

Output:

```
{
    "NetworkInsightsAnalysis": {
        "NetworkInsightsAnalysisId": "nia-02207aa13eb480c7a",
        "NetworkInsightsAnalysisArn": "arn:aws:ec2:us-east-1:123456789012:network-insights-analysis/nia-02207aa13eb480c7a",
        "NetworkInsightsPathId": "nip-0b26f224f1d131fa8",
        "StartDate": "2021-01-20T22:58:37.495Z",
        "Status": "running"
    }
}
```

For more information, see [Getting started using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/reachability/getting-started-cli.html) in the *Reachability Analyzer Guide*.

## Output

NetworkInsightsAnalysis -> (structure)

Information about the network insights analysis.

NetworkInsightsAnalysisId -> (string)

The ID of the network insights analysis.

NetworkInsightsAnalysisArn -> (string)

The Amazon Resource Name (ARN) of the network insights analysis.

NetworkInsightsPathId -> (string)

The ID of the path.

AdditionalAccounts -> (list)

The member accounts that contain resources that the path can traverse.

(string)

FilterInArns -> (list)

The Amazon Resource Names (ARN) of the resources that the path must traverse.

(string)

FilterOutArns -> (list)

The Amazon Resource Names (ARN) of the resources that the path must ignore.

(string)

StartDate -> (timestamp)

The time the analysis started.

Status -> (string)

The status of the network insights analysis.

StatusMessage -> (string)

The status message, if the status is `failed` .

WarningMessage -> (string)

The warning message.

NetworkPathFound -> (boolean)

Indicates whether the destination is reachable from the source.

ForwardPathComponents -> (list)

The components in the path from source to destination.

(structure)

Describes a path component.

SequenceNumber -> (integer)

The sequence number.

AclRule -> (structure)

The network ACL rule.

Cidr -> (string)

The IPv4 address range, in CIDR notation.

Egress -> (boolean)

Indicates whether the rule is an outbound rule.

PortRange -> (structure)

The range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocol -> (string)

The protocol.

RuleAction -> (string)

Indicates whether to allow or deny traffic that matches the rule.

RuleNumber -> (integer)

The rule number.

AttachedTo -> (structure)

The resource to which the path component is attached.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Component -> (structure)

The component.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

DestinationVpc -> (structure)

The destination VPC.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

OutboundHeader -> (structure)

The outbound header.

DestinationAddresses -> (list)

The destination addresses.

(string)

DestinationPortRanges -> (list)

The destination port ranges.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocol -> (string)

The protocol.

SourceAddresses -> (list)

The source addresses.

(string)

SourcePortRanges -> (list)

The source port ranges.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

InboundHeader -> (structure)

The inbound header.

DestinationAddresses -> (list)

The destination addresses.

(string)

DestinationPortRanges -> (list)

The destination port ranges.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocol -> (string)

The protocol.

SourceAddresses -> (list)

The source addresses.

(string)

SourcePortRanges -> (list)

The source port ranges.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

RouteTableRoute -> (structure)

The route table route.

DestinationCidr -> (string)

The destination IPv4 address, in CIDR notation.

DestinationPrefixListId -> (string)

The prefix of the Amazon Web Services service.

EgressOnlyInternetGatewayId -> (string)

The ID of an egress-only internet gateway.

GatewayId -> (string)

The ID of the gateway, such as an internet gateway or virtual private gateway.

InstanceId -> (string)

The ID of the instance, such as a NAT instance.

NatGatewayId -> (string)

The ID of a NAT gateway.

NetworkInterfaceId -> (string)

The ID of a network interface.

Origin -> (string)

Describes how the route was created. The following are the possible values:

- CreateRouteTable - The route was automatically created when the route table was created.
- CreateRoute - The route was manually added to the route table.
- EnableVgwRoutePropagation - The route was propagated by route propagation.

TransitGatewayId -> (string)

The ID of a transit gateway.

VpcPeeringConnectionId -> (string)

The ID of a VPC peering connection.

State -> (string)

The state. The following are the possible values:

- active
- blackhole

CarrierGatewayId -> (string)

The ID of a carrier gateway.

CoreNetworkArn -> (string)

The Amazon Resource Name (ARN) of a core network.

LocalGatewayId -> (string)

The ID of a local gateway.

SecurityGroupRule -> (structure)

The security group rule.

Cidr -> (string)

The IPv4 address range, in CIDR notation.

Direction -> (string)

The direction. The following are the possible values:

- egress
- ingress

SecurityGroupId -> (string)

The security group ID.

PortRange -> (structure)

The port range.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

PrefixListId -> (string)

The prefix list ID.

Protocol -> (string)

The protocol name.

SourceVpc -> (structure)

The source VPC.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Subnet -> (structure)

The subnet.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Vpc -> (structure)

The component VPC.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

AdditionalDetails -> (list)

The additional details.

(structure)

Describes an additional detail for a path analysis. For more information, see [Reachability Analyzer additional detail codes](https://docs.aws.amazon.com/vpc/latest/reachability/additional-detail-codes.html) .

AdditionalDetailType -> (string)

The additional detail code.

Component -> (structure)

The path component.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

VpcEndpointService -> (structure)

The VPC endpoint service.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

RuleOptions -> (list)

The rule options.

(structure)

Describes additional settings for a stateful rule.

Keyword -> (string)

The Suricata keyword.

Settings -> (list)

The settings for the keyword.

(string)

RuleGroupTypePairs -> (list)

The rule group type.

(structure)

Describes the type of a stateful rule group.

RuleGroupArn -> (string)

The ARN of the rule group.

RuleGroupType -> (string)

The rule group type. The possible values are `Domain List` and `Suricata` .

RuleGroupRuleOptionsPairs -> (list)

The rule options.

(structure)

Describes the rule options for a stateful rule group.

RuleGroupArn -> (string)

The ARN of the rule group.

RuleOptions -> (list)

The rule options.

(structure)

Describes additional settings for a stateful rule.

Keyword -> (string)

The Suricata keyword.

Settings -> (list)

The settings for the keyword.

(string)

ServiceName -> (string)

The name of the VPC endpoint service.

LoadBalancers -> (list)

The load balancers.

(structure)

Describes a path component.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

TransitGateway -> (structure)

The transit gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

TransitGatewayRouteTableRoute -> (structure)

The route in a transit gateway route table.

DestinationCidr -> (string)

The CIDR block used for destination matches.

State -> (string)

The state of the route.

RouteOrigin -> (string)

The route origin. The following are the possible values:

- static
- propagated

PrefixListId -> (string)

The ID of the prefix list.

AttachmentId -> (string)

The ID of the route attachment.

ResourceId -> (string)

The ID of the resource for the route attachment.

ResourceType -> (string)

The resource type for the route attachment.

Explanations -> (list)

The explanation codes.

(structure)

Describes an explanation code for an unreachable path. For more information, see [Reachability Analyzer explanation codes](https://docs.aws.amazon.com/vpc/latest/reachability/explanation-codes.html) .

Acl -> (structure)

The network ACL.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

AclRule -> (structure)

The network ACL rule.

Cidr -> (string)

The IPv4 address range, in CIDR notation.

Egress -> (boolean)

Indicates whether the rule is an outbound rule.

PortRange -> (structure)

The range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocol -> (string)

The protocol.

RuleAction -> (string)

Indicates whether to allow or deny traffic that matches the rule.

RuleNumber -> (integer)

The rule number.

Address -> (string)

The IPv4 address, in CIDR notation.

Addresses -> (list)

The IPv4 addresses, in CIDR notation.

(string)

AttachedTo -> (structure)

The resource to which the component is attached.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

AvailabilityZones -> (list)

The Availability Zones.

(string)

AvailabilityZoneIds -> (list)

The IDs of the Availability Zones.

(string)

Cidrs -> (list)

The CIDR ranges.

(string)

Component -> (structure)

The component.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

CustomerGateway -> (structure)

The customer gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Destination -> (structure)

The destination.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

DestinationVpc -> (structure)

The destination VPC.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Direction -> (string)

The direction. The following are the possible values:

- egress
- ingress

ExplanationCode -> (string)

The explanation code.

IngressRouteTable -> (structure)

The route table.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

InternetGateway -> (structure)

The internet gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

LoadBalancerArn -> (string)

The Amazon Resource Name (ARN) of the load balancer.

ClassicLoadBalancerListener -> (structure)

The listener for a Classic Load Balancer.

LoadBalancerPort -> (integer)

The port on which the load balancer is listening.

InstancePort -> (integer)

[Classic Load Balancers] The back-end port for the listener.

LoadBalancerListenerPort -> (integer)

The listener port of the load balancer.

LoadBalancerTarget -> (structure)

The target.

Address -> (string)

The IP address.

AvailabilityZone -> (string)

The Availability Zone.

AvailabilityZoneId -> (string)

The ID of the Availability Zone.

Instance -> (structure)

Information about the instance.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Port -> (integer)

The port on which the target is listening.

LoadBalancerTargetGroup -> (structure)

The target group.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

LoadBalancerTargetGroups -> (list)

The target groups.

(structure)

Describes a path component.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

LoadBalancerTargetPort -> (integer)

The target port.

ElasticLoadBalancerListener -> (structure)

The load balancer listener.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

MissingComponent -> (string)

The missing component.

NatGateway -> (structure)

The NAT gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

NetworkInterface -> (structure)

The network interface.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

PacketField -> (string)

The packet field.

VpcPeeringConnection -> (structure)

The VPC peering connection.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Port -> (integer)

The port.

PortRanges -> (list)

The port ranges.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

PrefixList -> (structure)

The prefix list.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Protocols -> (list)

The protocols.

(string)

RouteTableRoute -> (structure)

The route table route.

DestinationCidr -> (string)

The destination IPv4 address, in CIDR notation.

DestinationPrefixListId -> (string)

The prefix of the Amazon Web Services service.

EgressOnlyInternetGatewayId -> (string)

The ID of an egress-only internet gateway.

GatewayId -> (string)

The ID of the gateway, such as an internet gateway or virtual private gateway.

InstanceId -> (string)

The ID of the instance, such as a NAT instance.

NatGatewayId -> (string)

The ID of a NAT gateway.

NetworkInterfaceId -> (string)

The ID of a network interface.

Origin -> (string)

Describes how the route was created. The following are the possible values:

- CreateRouteTable - The route was automatically created when the route table was created.
- CreateRoute - The route was manually added to the route table.
- EnableVgwRoutePropagation - The route was propagated by route propagation.

TransitGatewayId -> (string)

The ID of a transit gateway.

VpcPeeringConnectionId -> (string)

The ID of a VPC peering connection.

State -> (string)

The state. The following are the possible values:

- active
- blackhole

CarrierGatewayId -> (string)

The ID of a carrier gateway.

CoreNetworkArn -> (string)

The Amazon Resource Name (ARN) of a core network.

LocalGatewayId -> (string)

The ID of a local gateway.

RouteTable -> (structure)

The route table.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

SecurityGroup -> (structure)

The security group.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

SecurityGroupRule -> (structure)

The security group rule.

Cidr -> (string)

The IPv4 address range, in CIDR notation.

Direction -> (string)

The direction. The following are the possible values:

- egress
- ingress

SecurityGroupId -> (string)

The security group ID.

PortRange -> (structure)

The port range.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

PrefixListId -> (string)

The prefix list ID.

Protocol -> (string)

The protocol name.

SecurityGroups -> (list)

The security groups.

(structure)

Describes a path component.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

SourceVpc -> (structure)

The source VPC.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

State -> (string)

The state.

Subnet -> (structure)

The subnet.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

SubnetRouteTable -> (structure)

The route table for the subnet.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Vpc -> (structure)

The component VPC.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

VpcEndpoint -> (structure)

The VPC endpoint.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

VpnConnection -> (structure)

The VPN connection.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

VpnGateway -> (structure)

The VPN gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

TransitGateway -> (structure)

The transit gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

TransitGatewayRouteTable -> (structure)

The transit gateway route table.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

TransitGatewayRouteTableRoute -> (structure)

The transit gateway route table route.

DestinationCidr -> (string)

The CIDR block used for destination matches.

State -> (string)

The state of the route.

RouteOrigin -> (string)

The route origin. The following are the possible values:

- static
- propagated

PrefixListId -> (string)

The ID of the prefix list.

AttachmentId -> (string)

The ID of the route attachment.

ResourceId -> (string)

The ID of the resource for the route attachment.

ResourceType -> (string)

The resource type for the route attachment.

TransitGatewayAttachment -> (structure)

The transit gateway attachment.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

ComponentAccount -> (string)

The Amazon Web Services account for the component.

ComponentRegion -> (string)

The Region for the component.

FirewallStatelessRule -> (structure)

The Network Firewall stateless rule.

RuleGroupArn -> (string)

The ARN of the stateless rule group.

Sources -> (list)

The source IP addresses, in CIDR notation.

(string)

Destinations -> (list)

The destination IP addresses, in CIDR notation.

(string)

SourcePorts -> (list)

The source ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

DestinationPorts -> (list)

The destination ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocols -> (list)

The protocols.

(integer)

RuleAction -> (string)

The rule action. The possible values are `pass` , `drop` , and `forward_to_site` .

Priority -> (integer)

The rule priority.

FirewallStatefulRule -> (structure)

The Network Firewall stateful rule.

RuleGroupArn -> (string)

The ARN of the stateful rule group.

Sources -> (list)

The source IP addresses, in CIDR notation.

(string)

Destinations -> (list)

The destination IP addresses, in CIDR notation.

(string)

SourcePorts -> (list)

The source ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

DestinationPorts -> (list)

The destination ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocol -> (string)

The protocol.

RuleAction -> (string)

The rule action. The possible values are `pass` , `drop` , and `alert` .

Direction -> (string)

The direction. The possible values are `FORWARD` and `ANY` .

ElasticLoadBalancerListener -> (structure)

The load balancer listener.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

FirewallStatelessRule -> (structure)

The Network Firewall stateless rule.

RuleGroupArn -> (string)

The ARN of the stateless rule group.

Sources -> (list)

The source IP addresses, in CIDR notation.

(string)

Destinations -> (list)

The destination IP addresses, in CIDR notation.

(string)

SourcePorts -> (list)

The source ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

DestinationPorts -> (list)

The destination ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocols -> (list)

The protocols.

(integer)

RuleAction -> (string)

The rule action. The possible values are `pass` , `drop` , and `forward_to_site` .

Priority -> (integer)

The rule priority.

FirewallStatefulRule -> (structure)

The Network Firewall stateful rule.

RuleGroupArn -> (string)

The ARN of the stateful rule group.

Sources -> (list)

The source IP addresses, in CIDR notation.

(string)

Destinations -> (list)

The destination IP addresses, in CIDR notation.

(string)

SourcePorts -> (list)

The source ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

DestinationPorts -> (list)

The destination ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocol -> (string)

The protocol.

RuleAction -> (string)

The rule action. The possible values are `pass` , `drop` , and `alert` .

Direction -> (string)

The direction. The possible values are `FORWARD` and `ANY` .

ServiceName -> (string)

The name of the VPC endpoint service.

ReturnPathComponents -> (list)

The components in the path from destination to source.

(structure)

Describes a path component.

SequenceNumber -> (integer)

The sequence number.

AclRule -> (structure)

The network ACL rule.

Cidr -> (string)

The IPv4 address range, in CIDR notation.

Egress -> (boolean)

Indicates whether the rule is an outbound rule.

PortRange -> (structure)

The range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocol -> (string)

The protocol.

RuleAction -> (string)

Indicates whether to allow or deny traffic that matches the rule.

RuleNumber -> (integer)

The rule number.

AttachedTo -> (structure)

The resource to which the path component is attached.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Component -> (structure)

The component.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

DestinationVpc -> (structure)

The destination VPC.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

OutboundHeader -> (structure)

The outbound header.

DestinationAddresses -> (list)

The destination addresses.

(string)

DestinationPortRanges -> (list)

The destination port ranges.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocol -> (string)

The protocol.

SourceAddresses -> (list)

The source addresses.

(string)

SourcePortRanges -> (list)

The source port ranges.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

InboundHeader -> (structure)

The inbound header.

DestinationAddresses -> (list)

The destination addresses.

(string)

DestinationPortRanges -> (list)

The destination port ranges.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocol -> (string)

The protocol.

SourceAddresses -> (list)

The source addresses.

(string)

SourcePortRanges -> (list)

The source port ranges.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

RouteTableRoute -> (structure)

The route table route.

DestinationCidr -> (string)

The destination IPv4 address, in CIDR notation.

DestinationPrefixListId -> (string)

The prefix of the Amazon Web Services service.

EgressOnlyInternetGatewayId -> (string)

The ID of an egress-only internet gateway.

GatewayId -> (string)

The ID of the gateway, such as an internet gateway or virtual private gateway.

InstanceId -> (string)

The ID of the instance, such as a NAT instance.

NatGatewayId -> (string)

The ID of a NAT gateway.

NetworkInterfaceId -> (string)

The ID of a network interface.

Origin -> (string)

Describes how the route was created. The following are the possible values:

- CreateRouteTable - The route was automatically created when the route table was created.
- CreateRoute - The route was manually added to the route table.
- EnableVgwRoutePropagation - The route was propagated by route propagation.

TransitGatewayId -> (string)

The ID of a transit gateway.

VpcPeeringConnectionId -> (string)

The ID of a VPC peering connection.

State -> (string)

The state. The following are the possible values:

- active
- blackhole

CarrierGatewayId -> (string)

The ID of a carrier gateway.

CoreNetworkArn -> (string)

The Amazon Resource Name (ARN) of a core network.

LocalGatewayId -> (string)

The ID of a local gateway.

SecurityGroupRule -> (structure)

The security group rule.

Cidr -> (string)

The IPv4 address range, in CIDR notation.

Direction -> (string)

The direction. The following are the possible values:

- egress
- ingress

SecurityGroupId -> (string)

The security group ID.

PortRange -> (structure)

The port range.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

PrefixListId -> (string)

The prefix list ID.

Protocol -> (string)

The protocol name.

SourceVpc -> (structure)

The source VPC.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Subnet -> (structure)

The subnet.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Vpc -> (structure)

The component VPC.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

AdditionalDetails -> (list)

The additional details.

(structure)

Describes an additional detail for a path analysis. For more information, see [Reachability Analyzer additional detail codes](https://docs.aws.amazon.com/vpc/latest/reachability/additional-detail-codes.html) .

AdditionalDetailType -> (string)

The additional detail code.

Component -> (structure)

The path component.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

VpcEndpointService -> (structure)

The VPC endpoint service.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

RuleOptions -> (list)

The rule options.

(structure)

Describes additional settings for a stateful rule.

Keyword -> (string)

The Suricata keyword.

Settings -> (list)

The settings for the keyword.

(string)

RuleGroupTypePairs -> (list)

The rule group type.

(structure)

Describes the type of a stateful rule group.

RuleGroupArn -> (string)

The ARN of the rule group.

RuleGroupType -> (string)

The rule group type. The possible values are `Domain List` and `Suricata` .

RuleGroupRuleOptionsPairs -> (list)

The rule options.

(structure)

Describes the rule options for a stateful rule group.

RuleGroupArn -> (string)

The ARN of the rule group.

RuleOptions -> (list)

The rule options.

(structure)

Describes additional settings for a stateful rule.

Keyword -> (string)

The Suricata keyword.

Settings -> (list)

The settings for the keyword.

(string)

ServiceName -> (string)

The name of the VPC endpoint service.

LoadBalancers -> (list)

The load balancers.

(structure)

Describes a path component.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

TransitGateway -> (structure)

The transit gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

TransitGatewayRouteTableRoute -> (structure)

The route in a transit gateway route table.

DestinationCidr -> (string)

The CIDR block used for destination matches.

State -> (string)

The state of the route.

RouteOrigin -> (string)

The route origin. The following are the possible values:

- static
- propagated

PrefixListId -> (string)

The ID of the prefix list.

AttachmentId -> (string)

The ID of the route attachment.

ResourceId -> (string)

The ID of the resource for the route attachment.

ResourceType -> (string)

The resource type for the route attachment.

Explanations -> (list)

The explanation codes.

(structure)

Describes an explanation code for an unreachable path. For more information, see [Reachability Analyzer explanation codes](https://docs.aws.amazon.com/vpc/latest/reachability/explanation-codes.html) .

Acl -> (structure)

The network ACL.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

AclRule -> (structure)

The network ACL rule.

Cidr -> (string)

The IPv4 address range, in CIDR notation.

Egress -> (boolean)

Indicates whether the rule is an outbound rule.

PortRange -> (structure)

The range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocol -> (string)

The protocol.

RuleAction -> (string)

Indicates whether to allow or deny traffic that matches the rule.

RuleNumber -> (integer)

The rule number.

Address -> (string)

The IPv4 address, in CIDR notation.

Addresses -> (list)

The IPv4 addresses, in CIDR notation.

(string)

AttachedTo -> (structure)

The resource to which the component is attached.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

AvailabilityZones -> (list)

The Availability Zones.

(string)

AvailabilityZoneIds -> (list)

The IDs of the Availability Zones.

(string)

Cidrs -> (list)

The CIDR ranges.

(string)

Component -> (structure)

The component.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

CustomerGateway -> (structure)

The customer gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Destination -> (structure)

The destination.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

DestinationVpc -> (structure)

The destination VPC.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Direction -> (string)

The direction. The following are the possible values:

- egress
- ingress

ExplanationCode -> (string)

The explanation code.

IngressRouteTable -> (structure)

The route table.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

InternetGateway -> (structure)

The internet gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

LoadBalancerArn -> (string)

The Amazon Resource Name (ARN) of the load balancer.

ClassicLoadBalancerListener -> (structure)

The listener for a Classic Load Balancer.

LoadBalancerPort -> (integer)

The port on which the load balancer is listening.

InstancePort -> (integer)

[Classic Load Balancers] The back-end port for the listener.

LoadBalancerListenerPort -> (integer)

The listener port of the load balancer.

LoadBalancerTarget -> (structure)

The target.

Address -> (string)

The IP address.

AvailabilityZone -> (string)

The Availability Zone.

AvailabilityZoneId -> (string)

The ID of the Availability Zone.

Instance -> (structure)

Information about the instance.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Port -> (integer)

The port on which the target is listening.

LoadBalancerTargetGroup -> (structure)

The target group.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

LoadBalancerTargetGroups -> (list)

The target groups.

(structure)

Describes a path component.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

LoadBalancerTargetPort -> (integer)

The target port.

ElasticLoadBalancerListener -> (structure)

The load balancer listener.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

MissingComponent -> (string)

The missing component.

NatGateway -> (structure)

The NAT gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

NetworkInterface -> (structure)

The network interface.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

PacketField -> (string)

The packet field.

VpcPeeringConnection -> (structure)

The VPC peering connection.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Port -> (integer)

The port.

PortRanges -> (list)

The port ranges.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

PrefixList -> (structure)

The prefix list.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Protocols -> (list)

The protocols.

(string)

RouteTableRoute -> (structure)

The route table route.

DestinationCidr -> (string)

The destination IPv4 address, in CIDR notation.

DestinationPrefixListId -> (string)

The prefix of the Amazon Web Services service.

EgressOnlyInternetGatewayId -> (string)

The ID of an egress-only internet gateway.

GatewayId -> (string)

The ID of the gateway, such as an internet gateway or virtual private gateway.

InstanceId -> (string)

The ID of the instance, such as a NAT instance.

NatGatewayId -> (string)

The ID of a NAT gateway.

NetworkInterfaceId -> (string)

The ID of a network interface.

Origin -> (string)

Describes how the route was created. The following are the possible values:

- CreateRouteTable - The route was automatically created when the route table was created.
- CreateRoute - The route was manually added to the route table.
- EnableVgwRoutePropagation - The route was propagated by route propagation.

TransitGatewayId -> (string)

The ID of a transit gateway.

VpcPeeringConnectionId -> (string)

The ID of a VPC peering connection.

State -> (string)

The state. The following are the possible values:

- active
- blackhole

CarrierGatewayId -> (string)

The ID of a carrier gateway.

CoreNetworkArn -> (string)

The Amazon Resource Name (ARN) of a core network.

LocalGatewayId -> (string)

The ID of a local gateway.

RouteTable -> (structure)

The route table.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

SecurityGroup -> (structure)

The security group.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

SecurityGroupRule -> (structure)

The security group rule.

Cidr -> (string)

The IPv4 address range, in CIDR notation.

Direction -> (string)

The direction. The following are the possible values:

- egress
- ingress

SecurityGroupId -> (string)

The security group ID.

PortRange -> (structure)

The port range.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

PrefixListId -> (string)

The prefix list ID.

Protocol -> (string)

The protocol name.

SecurityGroups -> (list)

The security groups.

(structure)

Describes a path component.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

SourceVpc -> (structure)

The source VPC.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

State -> (string)

The state.

Subnet -> (structure)

The subnet.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

SubnetRouteTable -> (structure)

The route table for the subnet.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Vpc -> (structure)

The component VPC.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

VpcEndpoint -> (structure)

The VPC endpoint.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

VpnConnection -> (structure)

The VPN connection.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

VpnGateway -> (structure)

The VPN gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

TransitGateway -> (structure)

The transit gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

TransitGatewayRouteTable -> (structure)

The transit gateway route table.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

TransitGatewayRouteTableRoute -> (structure)

The transit gateway route table route.

DestinationCidr -> (string)

The CIDR block used for destination matches.

State -> (string)

The state of the route.

RouteOrigin -> (string)

The route origin. The following are the possible values:

- static
- propagated

PrefixListId -> (string)

The ID of the prefix list.

AttachmentId -> (string)

The ID of the route attachment.

ResourceId -> (string)

The ID of the resource for the route attachment.

ResourceType -> (string)

The resource type for the route attachment.

TransitGatewayAttachment -> (structure)

The transit gateway attachment.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

ComponentAccount -> (string)

The Amazon Web Services account for the component.

ComponentRegion -> (string)

The Region for the component.

FirewallStatelessRule -> (structure)

The Network Firewall stateless rule.

RuleGroupArn -> (string)

The ARN of the stateless rule group.

Sources -> (list)

The source IP addresses, in CIDR notation.

(string)

Destinations -> (list)

The destination IP addresses, in CIDR notation.

(string)

SourcePorts -> (list)

The source ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

DestinationPorts -> (list)

The destination ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocols -> (list)

The protocols.

(integer)

RuleAction -> (string)

The rule action. The possible values are `pass` , `drop` , and `forward_to_site` .

Priority -> (integer)

The rule priority.

FirewallStatefulRule -> (structure)

The Network Firewall stateful rule.

RuleGroupArn -> (string)

The ARN of the stateful rule group.

Sources -> (list)

The source IP addresses, in CIDR notation.

(string)

Destinations -> (list)

The destination IP addresses, in CIDR notation.

(string)

SourcePorts -> (list)

The source ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

DestinationPorts -> (list)

The destination ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocol -> (string)

The protocol.

RuleAction -> (string)

The rule action. The possible values are `pass` , `drop` , and `alert` .

Direction -> (string)

The direction. The possible values are `FORWARD` and `ANY` .

ElasticLoadBalancerListener -> (structure)

The load balancer listener.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

FirewallStatelessRule -> (structure)

The Network Firewall stateless rule.

RuleGroupArn -> (string)

The ARN of the stateless rule group.

Sources -> (list)

The source IP addresses, in CIDR notation.

(string)

Destinations -> (list)

The destination IP addresses, in CIDR notation.

(string)

SourcePorts -> (list)

The source ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

DestinationPorts -> (list)

The destination ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocols -> (list)

The protocols.

(integer)

RuleAction -> (string)

The rule action. The possible values are `pass` , `drop` , and `forward_to_site` .

Priority -> (integer)

The rule priority.

FirewallStatefulRule -> (structure)

The Network Firewall stateful rule.

RuleGroupArn -> (string)

The ARN of the stateful rule group.

Sources -> (list)

The source IP addresses, in CIDR notation.

(string)

Destinations -> (list)

The destination IP addresses, in CIDR notation.

(string)

SourcePorts -> (list)

The source ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

DestinationPorts -> (list)

The destination ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocol -> (string)

The protocol.

RuleAction -> (string)

The rule action. The possible values are `pass` , `drop` , and `alert` .

Direction -> (string)

The direction. The possible values are `FORWARD` and `ANY` .

ServiceName -> (string)

The name of the VPC endpoint service.

Explanations -> (list)

The explanations. For more information, see [Reachability Analyzer explanation codes](https://docs.aws.amazon.com/vpc/latest/reachability/explanation-codes.html) .

(structure)

Describes an explanation code for an unreachable path. For more information, see [Reachability Analyzer explanation codes](https://docs.aws.amazon.com/vpc/latest/reachability/explanation-codes.html) .

Acl -> (structure)

The network ACL.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

AclRule -> (structure)

The network ACL rule.

Cidr -> (string)

The IPv4 address range, in CIDR notation.

Egress -> (boolean)

Indicates whether the rule is an outbound rule.

PortRange -> (structure)

The range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocol -> (string)

The protocol.

RuleAction -> (string)

Indicates whether to allow or deny traffic that matches the rule.

RuleNumber -> (integer)

The rule number.

Address -> (string)

The IPv4 address, in CIDR notation.

Addresses -> (list)

The IPv4 addresses, in CIDR notation.

(string)

AttachedTo -> (structure)

The resource to which the component is attached.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

AvailabilityZones -> (list)

The Availability Zones.

(string)

AvailabilityZoneIds -> (list)

The IDs of the Availability Zones.

(string)

Cidrs -> (list)

The CIDR ranges.

(string)

Component -> (structure)

The component.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

CustomerGateway -> (structure)

The customer gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Destination -> (structure)

The destination.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

DestinationVpc -> (structure)

The destination VPC.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Direction -> (string)

The direction. The following are the possible values:

- egress
- ingress

ExplanationCode -> (string)

The explanation code.

IngressRouteTable -> (structure)

The route table.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

InternetGateway -> (structure)

The internet gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

LoadBalancerArn -> (string)

The Amazon Resource Name (ARN) of the load balancer.

ClassicLoadBalancerListener -> (structure)

The listener for a Classic Load Balancer.

LoadBalancerPort -> (integer)

The port on which the load balancer is listening.

InstancePort -> (integer)

[Classic Load Balancers] The back-end port for the listener.

LoadBalancerListenerPort -> (integer)

The listener port of the load balancer.

LoadBalancerTarget -> (structure)

The target.

Address -> (string)

The IP address.

AvailabilityZone -> (string)

The Availability Zone.

AvailabilityZoneId -> (string)

The ID of the Availability Zone.

Instance -> (structure)

Information about the instance.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Port -> (integer)

The port on which the target is listening.

LoadBalancerTargetGroup -> (structure)

The target group.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

LoadBalancerTargetGroups -> (list)

The target groups.

(structure)

Describes a path component.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

LoadBalancerTargetPort -> (integer)

The target port.

ElasticLoadBalancerListener -> (structure)

The load balancer listener.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

MissingComponent -> (string)

The missing component.

NatGateway -> (structure)

The NAT gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

NetworkInterface -> (structure)

The network interface.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

PacketField -> (string)

The packet field.

VpcPeeringConnection -> (structure)

The VPC peering connection.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Port -> (integer)

The port.

PortRanges -> (list)

The port ranges.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

PrefixList -> (structure)

The prefix list.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Protocols -> (list)

The protocols.

(string)

RouteTableRoute -> (structure)

The route table route.

DestinationCidr -> (string)

The destination IPv4 address, in CIDR notation.

DestinationPrefixListId -> (string)

The prefix of the Amazon Web Services service.

EgressOnlyInternetGatewayId -> (string)

The ID of an egress-only internet gateway.

GatewayId -> (string)

The ID of the gateway, such as an internet gateway or virtual private gateway.

InstanceId -> (string)

The ID of the instance, such as a NAT instance.

NatGatewayId -> (string)

The ID of a NAT gateway.

NetworkInterfaceId -> (string)

The ID of a network interface.

Origin -> (string)

Describes how the route was created. The following are the possible values:

- CreateRouteTable - The route was automatically created when the route table was created.
- CreateRoute - The route was manually added to the route table.
- EnableVgwRoutePropagation - The route was propagated by route propagation.

TransitGatewayId -> (string)

The ID of a transit gateway.

VpcPeeringConnectionId -> (string)

The ID of a VPC peering connection.

State -> (string)

The state. The following are the possible values:

- active
- blackhole

CarrierGatewayId -> (string)

The ID of a carrier gateway.

CoreNetworkArn -> (string)

The Amazon Resource Name (ARN) of a core network.

LocalGatewayId -> (string)

The ID of a local gateway.

RouteTable -> (structure)

The route table.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

SecurityGroup -> (structure)

The security group.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

SecurityGroupRule -> (structure)

The security group rule.

Cidr -> (string)

The IPv4 address range, in CIDR notation.

Direction -> (string)

The direction. The following are the possible values:

- egress
- ingress

SecurityGroupId -> (string)

The security group ID.

PortRange -> (structure)

The port range.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

PrefixListId -> (string)

The prefix list ID.

Protocol -> (string)

The protocol name.

SecurityGroups -> (list)

The security groups.

(structure)

Describes a path component.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

SourceVpc -> (structure)

The source VPC.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

State -> (string)

The state.

Subnet -> (structure)

The subnet.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

SubnetRouteTable -> (structure)

The route table for the subnet.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

Vpc -> (structure)

The component VPC.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

VpcEndpoint -> (structure)

The VPC endpoint.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

VpnConnection -> (structure)

The VPN connection.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

VpnGateway -> (structure)

The VPN gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

TransitGateway -> (structure)

The transit gateway.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

TransitGatewayRouteTable -> (structure)

The transit gateway route table.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

TransitGatewayRouteTableRoute -> (structure)

The transit gateway route table route.

DestinationCidr -> (string)

The CIDR block used for destination matches.

State -> (string)

The state of the route.

RouteOrigin -> (string)

The route origin. The following are the possible values:

- static
- propagated

PrefixListId -> (string)

The ID of the prefix list.

AttachmentId -> (string)

The ID of the route attachment.

ResourceId -> (string)

The ID of the resource for the route attachment.

ResourceType -> (string)

The resource type for the route attachment.

TransitGatewayAttachment -> (structure)

The transit gateway attachment.

Id -> (string)

The ID of the component.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Name -> (string)

The name of the analysis component.

ComponentAccount -> (string)

The Amazon Web Services account for the component.

ComponentRegion -> (string)

The Region for the component.

FirewallStatelessRule -> (structure)

The Network Firewall stateless rule.

RuleGroupArn -> (string)

The ARN of the stateless rule group.

Sources -> (list)

The source IP addresses, in CIDR notation.

(string)

Destinations -> (list)

The destination IP addresses, in CIDR notation.

(string)

SourcePorts -> (list)

The source ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

DestinationPorts -> (list)

The destination ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocols -> (list)

The protocols.

(integer)

RuleAction -> (string)

The rule action. The possible values are `pass` , `drop` , and `forward_to_site` .

Priority -> (integer)

The rule priority.

FirewallStatefulRule -> (structure)

The Network Firewall stateful rule.

RuleGroupArn -> (string)

The ARN of the stateful rule group.

Sources -> (list)

The source IP addresses, in CIDR notation.

(string)

Destinations -> (list)

The destination IP addresses, in CIDR notation.

(string)

SourcePorts -> (list)

The source ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

DestinationPorts -> (list)

The destination ports.

(structure)

Describes a range of ports.

From -> (integer)

The first port in the range.

To -> (integer)

The last port in the range.

Protocol -> (string)

The protocol.

RuleAction -> (string)

The rule action. The possible values are `pass` , `drop` , and `alert` .

Direction -> (string)

The direction. The possible values are `FORWARD` and `ANY` .

AlternatePathHints -> (list)

Potential intermediate components.

(structure)

Describes an potential intermediate component of a feasible path.

ComponentId -> (string)

The ID of the component.

ComponentArn -> (string)

The Amazon Resource Name (ARN) of the component.

SuggestedAccounts -> (list)

Potential intermediate accounts.

(string)

Tags -> (list)

The tags.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.