# get-network-insights-access-scope-analysis-findingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-network-insights-access-scope-analysis-findings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-network-insights-access-scope-analysis-findings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# get-network-insights-access-scope-analysis-findings

## Description

Gets the findings for the specified Network Access Scope analysis.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/GetNetworkInsightsAccessScopeAnalysisFindings)

`get-network-insights-access-scope-analysis-findings` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `AnalysisFindings`

## Synopsis

```
get-network-insights-access-scope-analysis-findings
--network-insights-access-scope-analysis-id <value>
[--dry-run | --no-dry-run]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--network-insights-access-scope-analysis-id` (string)

The ID of the Network Access Scope analysis.

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To get the findings of Network Insights access scope analysis**

The following `get-network-insights-access-scope-analysis-findings` example gets the selected scope analysis findings in your AWS account.

```
aws ec2 get-network-insights-access-scope-analysis-findings \
    --region us-east-1 \
    --network-insights-access-scope-analysis-id nis \
    --nis-123456789111
```

Output:

```
{
    "NetworkInsightsAccessScopeAnalysisId": "nisa-123456789222",
    "AnalysisFindings": [
        {
            "NetworkInsightsAccessScopeAnalysisId": "nisa-123456789222",
            "NetworkInsightsAccessScopeId": "nis-123456789111",
            "FindingComponents": [
                {
                    "SequenceNumber": 1,
                    "Component": {
                        "Id": "eni-02e3d42d5cceca67d",
                        "Arn": "arn:aws:ec2:us-east-1:936459623503:network-interface/eni-02e3d32d9cceca17d"
                    },
                    "OutboundHeader": {
                        "DestinationAddresses": [
                            "0.0.0.0/5",
                            "11.0.0.0/8",
                            "12.0.0.0/6",
                            "128.0.0.0/3",
                            "16.0.0.0/4",
                            "160.0.0.0/5",
                            "168.0.0.0/6",
                            "172.0.0.0/12"
                            "8.0.0.0/7"
                        ],
                        "DestinationPortRanges": [
                            {
                                "From": 0,
                                "To": 65535
                            }
                        ],
                        "Protocol": "6",
                        "SourceAddresses": [
                            "10.0.2.253/32"
                        ],
                        "SourcePortRanges": [
                            {
                                "From": 0,
                                "To": 65535
                            }
                        ]
                    }, [etc]
                ]
            }
        }
    ]
}
```

For more information, see [Getting started with Network Access Analyzer using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/getting-started-cli.html) in the *Network Access Analyzer Guide*.

## Output

NetworkInsightsAccessScopeAnalysisId -> (string)

The ID of the Network Access Scope analysis.

AnalysisStatus -> (string)

The status of Network Access Scope Analysis.

AnalysisFindings -> (list)

The findings associated with Network Access Scope Analysis.

(structure)

Describes a finding for a Network Access Scope.

NetworkInsightsAccessScopeAnalysisId -> (string)

The ID of the Network Access Scope analysis.

NetworkInsightsAccessScopeId -> (string)

The ID of the Network Access Scope.

FindingId -> (string)

The ID of the finding.

FindingComponents -> (list)

The finding components.

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

NextToken -> (string)

The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.