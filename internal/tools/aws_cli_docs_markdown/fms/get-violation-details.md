# get-violation-detailsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-violation-details.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-violation-details.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [fms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/index.html#cli-aws-fms) ]

# get-violation-details

## Description

Retrieves violations for a resource based on the specified Firewall Manager policy and Amazon Web Services account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetViolationDetails)

## Synopsis

```
get-violation-details
--policy-id <value>
--member-account <value>
--resource-id <value>
--resource-type <value>
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

`--policy-id` (string)

The ID of the Firewall Manager policy that you want the details for. You can get violation details for the following policy types:

- WAF
- DNS Firewall
- Imported Network Firewall
- Network Firewall
- Security group content audit
- Network ACL
- Third-party firewall

`--member-account` (string)

The Amazon Web Services account ID that you want the details for.

`--resource-id` (string)

The ID of the resource that has violations.

`--resource-type` (string)

The resource type. This is in the format shown in the [Amazon Web Services Resource Types Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) . Supported resource types are: `AWS::WAFv2::WebACL` , `AWS::EC2::Instance` , `AWS::EC2::NetworkInterface` , `AWS::EC2::SecurityGroup` , `AWS::NetworkFirewall::FirewallPolicy` , and `AWS::EC2::Subnet` .

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

ViolationDetail -> (structure)

Violation detail for a resource.

PolicyId -> (string)

The ID of the Firewall Manager policy that the violation details were requested for.

MemberAccount -> (string)

The Amazon Web Services account that the violation details were requested for.

ResourceId -> (string)

The resource ID that the violation details were requested for.

ResourceType -> (string)

The resource type that the violation details were requested for.

ResourceViolations -> (list)

List of violations for the requested resource.

(structure)

Violation detail based on resource type.

AwsVPCSecurityGroupViolation -> (structure)

Violation detail for security groups.

ViolationTarget -> (string)

The security group rule that is being evaluated.

ViolationTargetDescription -> (string)

A description of the security group that violates the policy.

PartialMatches -> (list)

List of rules specified in the security group of the Firewall Manager policy that partially match the `ViolationTarget` rule.

(structure)

The reference rule that partially matches the `ViolationTarget` rule and violation reason.

Reference -> (string)

The reference rule from the primary security group of the Firewall Manager policy.

TargetViolationReasons -> (list)

The violation reason.

(string)

PossibleSecurityGroupRemediationActions -> (list)

Remediation options for the rule specified in the `ViolationTarget` .

(structure)

Remediation option for the rule specified in the `ViolationTarget` .

RemediationActionType -> (string)

The remediation action that will be performed.

Description -> (string)

Brief description of the action that will be performed.

RemediationResult -> (structure)

The final state of the rule specified in the `ViolationTarget` after it is remediated.

IPV4Range -> (string)

The IPv4 ranges for the security group rule.

IPV6Range -> (string)

The IPv6 ranges for the security group rule.

PrefixListId -> (string)

The ID of the prefix list for the security group rule.

Protocol -> (string)

The IP protocol name (`tcp` , `udp` , `icmp` , `icmpv6` ) or number.

FromPort -> (long)

The start of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of `-1` indicates all ICMP/ICMPv6 types.

ToPort -> (long)

The end of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of `-1` indicates all ICMP/ICMPv6 codes.

IsDefaultAction -> (boolean)

Indicates if the current action is the default action.

AwsEc2NetworkInterfaceViolation -> (structure)

Violation detail for a network interface.

ViolationTarget -> (string)

The resource ID of the network interface.

ViolatingSecurityGroups -> (list)

List of security groups that violate the rules specified in the primary security group of the Firewall Manager policy.

(string)

AwsEc2InstanceViolation -> (structure)

Violation detail for an EC2 instance.

ViolationTarget -> (string)

The resource ID of the EC2 instance.

AwsEc2NetworkInterfaceViolations -> (list)

Violation detail for network interfaces associated with the EC2 instance.

(structure)

Violation detail for network interfaces associated with an EC2 instance.

ViolationTarget -> (string)

The resource ID of the network interface.

ViolatingSecurityGroups -> (list)

List of security groups that violate the rules specified in the primary security group of the Firewall Manager policy.

(string)

NetworkFirewallMissingFirewallViolation -> (structure)

Violation detail for an Network Firewall policy that indicates that a subnet has no Firewall Manager managed firewall in its VPC.

ViolationTarget -> (string)

The ID of the Network Firewall or VPC resource thatâs in violation.

VPC -> (string)

The resource ID of the VPC associated with a violating subnet.

AvailabilityZone -> (string)

The Availability Zone of a violating subnet.

TargetViolationReason -> (string)

The reason the resource has this violation, if one is available.

NetworkFirewallMissingSubnetViolation -> (structure)

Violation detail for an Network Firewall policy that indicates that an Availability Zone is missing the expected Firewall Manager managed subnet.

ViolationTarget -> (string)

The ID of the Network Firewall or VPC resource thatâs in violation.

VPC -> (string)

The resource ID of the VPC associated with a violating subnet.

AvailabilityZone -> (string)

The Availability Zone of a violating subnet.

TargetViolationReason -> (string)

The reason the resource has this violation, if one is available.

NetworkFirewallMissingExpectedRTViolation -> (structure)

Violation detail for an Network Firewall policy that indicates that a subnet is not associated with the expected Firewall Manager managed route table.

ViolationTarget -> (string)

The ID of the Network Firewall or VPC resource thatâs in violation.

VPC -> (string)

The resource ID of the VPC associated with a violating subnet.

AvailabilityZone -> (string)

The Availability Zone of a violating subnet.

CurrentRouteTable -> (string)

The resource ID of the current route table thatâs associated with the subnet, if one is available.

ExpectedRouteTable -> (string)

The resource ID of the route table that should be associated with the subnet.

NetworkFirewallPolicyModifiedViolation -> (structure)

Violation detail for an Network Firewall policy that indicates that a firewall policy in an individual account has been modified in a way that makes it noncompliant. For example, the individual account owner might have deleted a rule group, changed the priority of a stateless rule group, or changed a policy default action.

ViolationTarget -> (string)

The ID of the Network Firewall or VPC resource thatâs in violation.

CurrentPolicyDescription -> (structure)

The policy thatâs currently in use in the individual account.

StatelessRuleGroups -> (list)

The stateless rule groups that are used in the Network Firewall firewall policy.

(structure)

Network Firewall stateless rule group, used in a  NetworkFirewallPolicyDescription .

RuleGroupName -> (string)

The name of the rule group.

ResourceId -> (string)

The resource ID of the rule group.

Priority -> (integer)

The priority of the rule group. Network Firewall evaluates the stateless rule groups in a firewall policy starting from the lowest priority setting.

StatelessDefaultActions -> (list)

The actions to take on packets that donât match any of the stateless rule groups.

(string)

StatelessFragmentDefaultActions -> (list)

The actions to take on packet fragments that donât match any of the stateless rule groups.

(string)

StatelessCustomActions -> (list)

Names of custom actions that are available for use in the stateless default actions settings.

(string)

StatefulRuleGroups -> (list)

The stateful rule groups that are used in the Network Firewall firewall policy.

(structure)

Network Firewall stateful rule group, used in a  NetworkFirewallPolicyDescription .

RuleGroupName -> (string)

The name of the rule group.

ResourceId -> (string)

The resource ID of the rule group.

Priority -> (integer)

An integer setting that indicates the order in which to run the stateful rule groups in a single Network Firewall firewall policy. This setting only applies to firewall policies that specify the `STRICT_ORDER` rule order in the stateful engine options settings.

Network Firewall evalutes each stateful rule group against a packet starting with the group that has the lowest priority setting. You must ensure that the priority settings are unique within each policy. For information about

You can change the priority settings of your rule groups at any time. To make it easier to insert rule groups later, number them so thereâs a wide range in between, for example use 100, 200, and so on.

Override -> (structure)

The action that allows the policy owner to override the behavior of the rule group within a policy.

Action -> (string)

The action that changes the rule group from `DROP` to `ALERT` . This only applies to managed rule groups.

StatefulDefaultActions -> (list)

The default actions to take on a packet that doesnât match any stateful rules. The stateful default action is optional, and is only valid when using the strict rule order.

Valid values of the stateful default action:

- aws:drop_strict
- aws:drop_established
- aws:alert_strict
- aws:alert_established

(string)

StatefulEngineOptions -> (structure)

Additional options governing how Network Firewall handles stateful rules. The stateful rule groups that you use in your policy must have stateful rule options settings that are compatible with these settings.

RuleOrder -> (string)

Indicates how to manage the order of stateful rule evaluation for the policy. Stateful rules are provided to the rule engine as Suricata compatible strings, and Suricata evaluates them based on certain settings. For more information, see [Evaluation order for stateful rules](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html) in the *Network Firewall Developer Guide* .

Default: `DEFAULT_ACTION_ORDER`

StreamExceptionPolicy -> (string)

Indicates how Network Firewall should handle traffic when a network connection breaks midstream.

- `DROP` - Fail closed and drop all subsequent traffic going to the firewall.
- `CONTINUE` - Continue to apply rules to subsequent traffic without context from traffic before the break. This impacts the behavior of rules that depend on context. For example, with a stateful rule that drops HTTP traffic, Network Firewall wonât match subsequent traffic because the it wonât have the context from session initialization, which defines the application layer protocol as HTTP. However, a TCP-layer rule using a `flow:stateless` rule would still match, and so would the `aws:drop_strict` default action.
- `REJECT` - Fail closed and drop all subsequent traffic going to the firewall. With this option, Network Firewall also sends a TCP reject packet back to the client so the client can immediately establish a new session. With the new session, Network Firewall will have context and will apply rules appropriately. For applications that are reliant on long-lived TCP connections that trigger Gateway Load Balancer idle timeouts, this is the recommended setting.
- `FMS_IGNORE` - Firewall Manager doesnât monitor or modify the Network Firewall stream exception policy settings.

For more information, see [Stream exception policy in your firewall policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stream-exception-policy.html) in the *Network Firewall Developer Guide* .

Default: `FMS_IGNORE`

ExpectedPolicyDescription -> (structure)

The policy that should be in use in the individual account in order to be compliant.

StatelessRuleGroups -> (list)

The stateless rule groups that are used in the Network Firewall firewall policy.

(structure)

Network Firewall stateless rule group, used in a  NetworkFirewallPolicyDescription .

RuleGroupName -> (string)

The name of the rule group.

ResourceId -> (string)

The resource ID of the rule group.

Priority -> (integer)

The priority of the rule group. Network Firewall evaluates the stateless rule groups in a firewall policy starting from the lowest priority setting.

StatelessDefaultActions -> (list)

The actions to take on packets that donât match any of the stateless rule groups.

(string)

StatelessFragmentDefaultActions -> (list)

The actions to take on packet fragments that donât match any of the stateless rule groups.

(string)

StatelessCustomActions -> (list)

Names of custom actions that are available for use in the stateless default actions settings.

(string)

StatefulRuleGroups -> (list)

The stateful rule groups that are used in the Network Firewall firewall policy.

(structure)

Network Firewall stateful rule group, used in a  NetworkFirewallPolicyDescription .

RuleGroupName -> (string)

The name of the rule group.

ResourceId -> (string)

The resource ID of the rule group.

Priority -> (integer)

An integer setting that indicates the order in which to run the stateful rule groups in a single Network Firewall firewall policy. This setting only applies to firewall policies that specify the `STRICT_ORDER` rule order in the stateful engine options settings.

Network Firewall evalutes each stateful rule group against a packet starting with the group that has the lowest priority setting. You must ensure that the priority settings are unique within each policy. For information about

You can change the priority settings of your rule groups at any time. To make it easier to insert rule groups later, number them so thereâs a wide range in between, for example use 100, 200, and so on.

Override -> (structure)

The action that allows the policy owner to override the behavior of the rule group within a policy.

Action -> (string)

The action that changes the rule group from `DROP` to `ALERT` . This only applies to managed rule groups.

StatefulDefaultActions -> (list)

The default actions to take on a packet that doesnât match any stateful rules. The stateful default action is optional, and is only valid when using the strict rule order.

Valid values of the stateful default action:

- aws:drop_strict
- aws:drop_established
- aws:alert_strict
- aws:alert_established

(string)

StatefulEngineOptions -> (structure)

Additional options governing how Network Firewall handles stateful rules. The stateful rule groups that you use in your policy must have stateful rule options settings that are compatible with these settings.

RuleOrder -> (string)

Indicates how to manage the order of stateful rule evaluation for the policy. Stateful rules are provided to the rule engine as Suricata compatible strings, and Suricata evaluates them based on certain settings. For more information, see [Evaluation order for stateful rules](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html) in the *Network Firewall Developer Guide* .

Default: `DEFAULT_ACTION_ORDER`

StreamExceptionPolicy -> (string)

Indicates how Network Firewall should handle traffic when a network connection breaks midstream.

- `DROP` - Fail closed and drop all subsequent traffic going to the firewall.
- `CONTINUE` - Continue to apply rules to subsequent traffic without context from traffic before the break. This impacts the behavior of rules that depend on context. For example, with a stateful rule that drops HTTP traffic, Network Firewall wonât match subsequent traffic because the it wonât have the context from session initialization, which defines the application layer protocol as HTTP. However, a TCP-layer rule using a `flow:stateless` rule would still match, and so would the `aws:drop_strict` default action.
- `REJECT` - Fail closed and drop all subsequent traffic going to the firewall. With this option, Network Firewall also sends a TCP reject packet back to the client so the client can immediately establish a new session. With the new session, Network Firewall will have context and will apply rules appropriately. For applications that are reliant on long-lived TCP connections that trigger Gateway Load Balancer idle timeouts, this is the recommended setting.
- `FMS_IGNORE` - Firewall Manager doesnât monitor or modify the Network Firewall stream exception policy settings.

For more information, see [Stream exception policy in your firewall policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stream-exception-policy.html) in the *Network Firewall Developer Guide* .

Default: `FMS_IGNORE`

NetworkFirewallInternetTrafficNotInspectedViolation -> (structure)

Violation detail for the subnet for which internet traffic hasnât been inspected.

SubnetId -> (string)

The subnet ID.

SubnetAvailabilityZone -> (string)

The subnet Availability Zone.

RouteTableId -> (string)

Information about the route table ID.

ViolatingRoutes -> (list)

The route or routes that are in violation.

(structure)

Describes a route in a route table.

DestinationType -> (string)

The type of destination for the route.

TargetType -> (string)

The type of target for the route.

Destination -> (string)

The destination of the route.

Target -> (string)

The routeâs target.

IsRouteTableUsedInDifferentAZ -> (boolean)

Information about whether the route table is used in another Availability Zone.

CurrentFirewallSubnetRouteTable -> (string)

Information about the subnet route table for the current firewall.

ExpectedFirewallEndpoint -> (string)

The expected endpoint for the current firewall.

FirewallSubnetId -> (string)

The firewall subnet ID.

ExpectedFirewallSubnetRoutes -> (list)

The firewall subnet routes that are expected.

(structure)

Information about the expected route in the route table.

IpV4Cidr -> (string)

Information about the IPv4 CIDR block.

PrefixListId -> (string)

Information about the ID of the prefix list for the route.

IpV6Cidr -> (string)

Information about the IPv6 CIDR block.

ContributingSubnets -> (list)

Information about the contributing subnets.

(string)

AllowedTargets -> (list)

Information about the allowed targets.

(string)

RouteTableId -> (string)

Information about the route table ID.

ActualFirewallSubnetRoutes -> (list)

The actual firewall subnet routes.

(structure)

Describes a route in a route table.

DestinationType -> (string)

The type of destination for the route.

TargetType -> (string)

The type of target for the route.

Destination -> (string)

The destination of the route.

Target -> (string)

The routeâs target.

InternetGatewayId -> (string)

The internet gateway ID.

CurrentInternetGatewayRouteTable -> (string)

The current route table for the internet gateway.

ExpectedInternetGatewayRoutes -> (list)

The internet gateway routes that are expected.

(structure)

Information about the expected route in the route table.

IpV4Cidr -> (string)

Information about the IPv4 CIDR block.

PrefixListId -> (string)

Information about the ID of the prefix list for the route.

IpV6Cidr -> (string)

Information about the IPv6 CIDR block.

ContributingSubnets -> (list)

Information about the contributing subnets.

(string)

AllowedTargets -> (list)

Information about the allowed targets.

(string)

RouteTableId -> (string)

Information about the route table ID.

ActualInternetGatewayRoutes -> (list)

The actual internet gateway routes.

(structure)

Describes a route in a route table.

DestinationType -> (string)

The type of destination for the route.

TargetType -> (string)

The type of target for the route.

Destination -> (string)

The destination of the route.

Target -> (string)

The routeâs target.

VpcId -> (string)

Information about the VPC ID.

NetworkFirewallInvalidRouteConfigurationViolation -> (structure)

The route configuration is invalid.

AffectedSubnets -> (list)

The subnets that are affected.

(string)

RouteTableId -> (string)

The route table ID.

IsRouteTableUsedInDifferentAZ -> (boolean)

Information about whether the route table is used in another Availability Zone.

ViolatingRoute -> (structure)

The route thatâs in violation.

DestinationType -> (string)

The type of destination for the route.

TargetType -> (string)

The type of target for the route.

Destination -> (string)

The destination of the route.

Target -> (string)

The routeâs target.

CurrentFirewallSubnetRouteTable -> (string)

The subnet route table for the current firewall.

ExpectedFirewallEndpoint -> (string)

The firewall endpoint thatâs expected.

ActualFirewallEndpoint -> (string)

The actual firewall endpoint.

ExpectedFirewallSubnetId -> (string)

The expected subnet ID for the firewall.

ActualFirewallSubnetId -> (string)

The actual subnet ID for the firewall.

ExpectedFirewallSubnetRoutes -> (list)

The firewall subnet routes that are expected.

(structure)

Information about the expected route in the route table.

IpV4Cidr -> (string)

Information about the IPv4 CIDR block.

PrefixListId -> (string)

Information about the ID of the prefix list for the route.

IpV6Cidr -> (string)

Information about the IPv6 CIDR block.

ContributingSubnets -> (list)

Information about the contributing subnets.

(string)

AllowedTargets -> (list)

Information about the allowed targets.

(string)

RouteTableId -> (string)

Information about the route table ID.

ActualFirewallSubnetRoutes -> (list)

The actual firewall subnet routes that are expected.

(structure)

Describes a route in a route table.

DestinationType -> (string)

The type of destination for the route.

TargetType -> (string)

The type of target for the route.

Destination -> (string)

The destination of the route.

Target -> (string)

The routeâs target.

InternetGatewayId -> (string)

The internet gateway ID.

CurrentInternetGatewayRouteTable -> (string)

The route table for the current internet gateway.

ExpectedInternetGatewayRoutes -> (list)

The expected routes for the internet gateway.

(structure)

Information about the expected route in the route table.

IpV4Cidr -> (string)

Information about the IPv4 CIDR block.

PrefixListId -> (string)

Information about the ID of the prefix list for the route.

IpV6Cidr -> (string)

Information about the IPv6 CIDR block.

ContributingSubnets -> (list)

Information about the contributing subnets.

(string)

AllowedTargets -> (list)

Information about the allowed targets.

(string)

RouteTableId -> (string)

Information about the route table ID.

ActualInternetGatewayRoutes -> (list)

The actual internet gateway routes.

(structure)

Describes a route in a route table.

DestinationType -> (string)

The type of destination for the route.

TargetType -> (string)

The type of target for the route.

Destination -> (string)

The destination of the route.

Target -> (string)

The routeâs target.

VpcId -> (string)

Information about the VPC ID.

NetworkFirewallBlackHoleRouteDetectedViolation -> (structure)

Violation detail for an internet gateway route with an inactive state in the customer subnet route table or Network Firewall subnet route table.

ViolationTarget -> (string)

The subnet that has an inactive state.

RouteTableId -> (string)

Information about the route table ID.

VpcId -> (string)

Information about the VPC ID.

ViolatingRoutes -> (list)

Information about the route or routes that are in violation.

(structure)

Describes a route in a route table.

DestinationType -> (string)

The type of destination for the route.

TargetType -> (string)

The type of target for the route.

Destination -> (string)

The destination of the route.

Target -> (string)

The routeâs target.

NetworkFirewallUnexpectedFirewallRoutesViolation -> (structure)

Thereâs an unexpected firewall route.

FirewallSubnetId -> (string)

The subnet ID for the firewall.

ViolatingRoutes -> (list)

The routes that are in violation.

(structure)

Describes a route in a route table.

DestinationType -> (string)

The type of destination for the route.

TargetType -> (string)

The type of target for the route.

Destination -> (string)

The destination of the route.

Target -> (string)

The routeâs target.

RouteTableId -> (string)

The ID of the route table.

FirewallEndpoint -> (string)

The endpoint of the firewall.

VpcId -> (string)

Information about the VPC ID.

NetworkFirewallUnexpectedGatewayRoutesViolation -> (structure)

Thereâs an unexpected gateway route.

GatewayId -> (string)

Information about the gateway ID.

ViolatingRoutes -> (list)

The routes that are in violation.

(structure)

Describes a route in a route table.

DestinationType -> (string)

The type of destination for the route.

TargetType -> (string)

The type of target for the route.

Destination -> (string)

The destination of the route.

Target -> (string)

The routeâs target.

RouteTableId -> (string)

Information about the route table.

VpcId -> (string)

Information about the VPC ID.

NetworkFirewallMissingExpectedRoutesViolation -> (structure)

Expected routes are missing from Network Firewall.

ViolationTarget -> (string)

The target of the violation.

ExpectedRoutes -> (list)

The expected routes.

(structure)

Information about the expected route in the route table.

IpV4Cidr -> (string)

Information about the IPv4 CIDR block.

PrefixListId -> (string)

Information about the ID of the prefix list for the route.

IpV6Cidr -> (string)

Information about the IPv6 CIDR block.

ContributingSubnets -> (list)

Information about the contributing subnets.

(string)

AllowedTargets -> (list)

Information about the allowed targets.

(string)

RouteTableId -> (string)

Information about the route table ID.

VpcId -> (string)

Information about the VPC ID.

DnsRuleGroupPriorityConflictViolation -> (structure)

Violation detail for a DNS Firewall policy that indicates that a rule group that Firewall Manager tried to associate with a VPC has the same priority as a rule group thatâs already associated.

ViolationTarget -> (string)

Information about the VPC ID.

ViolationTargetDescription -> (string)

A description of the violation that specifies the VPC and the rule group thatâs already associated with it.

ConflictingPriority -> (integer)

The priority setting of the two conflicting rule groups.

ConflictingPolicyId -> (string)

The ID of the Firewall Manager DNS Firewall policy that was already applied to the VPC. This policy contains the rule group thatâs already associated with the VPC.

UnavailablePriorities -> (list)

The priorities of rule groups that are already associated with the VPC. To retry your operation, choose priority settings that arenât in this list for the rule groups in your new DNS Firewall policy.

(integer)

DnsDuplicateRuleGroupViolation -> (structure)

Violation detail for a DNS Firewall policy that indicates that a rule group that Firewall Manager tried to associate with a VPC is already associated with the VPC and canât be associated again.

ViolationTarget -> (string)

Information about the VPC ID.

ViolationTargetDescription -> (string)

A description of the violation that specifies the rule group and VPC.

DnsRuleGroupLimitExceededViolation -> (structure)

Violation detail for a DNS Firewall policy that indicates that the VPC reached the limit for associated DNS Firewall rule groups. Firewall Manager tried to associate another rule group with the VPC and failed.

ViolationTarget -> (string)

Information about the VPC ID.

ViolationTargetDescription -> (string)

A description of the violation that specifies the rule group and VPC.

NumberOfRuleGroupsAlreadyAssociated -> (integer)

The number of rule groups currently associated with the VPC.

FirewallSubnetIsOutOfScopeViolation -> (structure)

Contains details about the firewall subnet that violates the policy scope.

FirewallSubnetId -> (string)

The ID of the firewall subnet that violates the policy scope.

VpcId -> (string)

The VPC ID of the firewall subnet that violates the policy scope.

SubnetAvailabilityZone -> (string)

The Availability Zone of the firewall subnet that violates the policy scope.

SubnetAvailabilityZoneId -> (string)

The Availability Zone ID of the firewall subnet that violates the policy scope.

VpcEndpointId -> (string)

The VPC endpoint ID of the firewall subnet that violates the policy scope.

RouteHasOutOfScopeEndpointViolation -> (structure)

Contains details about the route endpoint that violates the policy scope.

SubnetId -> (string)

The ID of the subnet associated with the route that violates the policy scope.

VpcId -> (string)

The VPC ID of the route that violates the policy scope.

RouteTableId -> (string)

The ID of the route table.

ViolatingRoutes -> (list)

The list of routes that violate the route table.

(structure)

Describes a route in a route table.

DestinationType -> (string)

The type of destination for the route.

TargetType -> (string)

The type of target for the route.

Destination -> (string)

The destination of the route.

Target -> (string)

The routeâs target.

SubnetAvailabilityZone -> (string)

The subnetâs Availability Zone.

SubnetAvailabilityZoneId -> (string)

The ID of the subnetâs Availability Zone.

CurrentFirewallSubnetRouteTable -> (string)

The route table associated with the current firewall subnet.

FirewallSubnetId -> (string)

The ID of the firewall subnet.

FirewallSubnetRoutes -> (list)

The list of firewall subnet routes.

(structure)

Describes a route in a route table.

DestinationType -> (string)

The type of destination for the route.

TargetType -> (string)

The type of target for the route.

Destination -> (string)

The destination of the route.

Target -> (string)

The routeâs target.

InternetGatewayId -> (string)

The ID of the Internet Gateway.

CurrentInternetGatewayRouteTable -> (string)

The current route table associated with the Internet Gateway.

InternetGatewayRoutes -> (list)

The routes in the route table associated with the Internet Gateway.

(structure)

Describes a route in a route table.

DestinationType -> (string)

The type of destination for the route.

TargetType -> (string)

The type of target for the route.

Destination -> (string)

The destination of the route.

Target -> (string)

The routeâs target.

ThirdPartyFirewallMissingFirewallViolation -> (structure)

The violation details for a third-party firewall thatâs been deleted.

ViolationTarget -> (string)

The ID of the third-party firewall thatâs causing the violation.

VPC -> (string)

The resource ID of the VPC associated with a third-party firewall.

AvailabilityZone -> (string)

The Availability Zone of the third-party firewall thatâs causing the violation.

TargetViolationReason -> (string)

The reason the resource is causing this violation, if a reason is available.

ThirdPartyFirewallMissingSubnetViolation -> (structure)

The violation details for a third-party firewallâs subnet thatâs been deleted.

ViolationTarget -> (string)

The ID of the third-party firewall or VPC resource thatâs causing the violation.

VPC -> (string)

The resource ID of the VPC associated with a subnet thatâs causing the violation.

AvailabilityZone -> (string)

The Availability Zone of a subnet thatâs causing the violation.

TargetViolationReason -> (string)

The reason the resource is causing the violation, if a reason is available.

ThirdPartyFirewallMissingExpectedRouteTableViolation -> (structure)

The violation details for a third-party firewall that has the Firewall Manager managed route table that was associated with the third-party firewall has been deleted.

ViolationTarget -> (string)

The ID of the third-party firewall or VPC resource thatâs causing the violation.

VPC -> (string)

The resource ID of the VPC associated with a fireawll subnet thatâs causing the violation.

AvailabilityZone -> (string)

The Availability Zone of the firewall subnet thatâs causing the violation.

CurrentRouteTable -> (string)

The resource ID of the current route table thatâs associated with the subnet, if one is available.

ExpectedRouteTable -> (string)

The resource ID of the route table that should be associated with the subnet.

FirewallSubnetMissingVPCEndpointViolation -> (structure)

The violation details for a third-party firewallâs VPC endpoint subnet that was deleted.

FirewallSubnetId -> (string)

The ID of the firewall that this VPC endpoint is associated with.

VpcId -> (string)

The resource ID of the VPC associated with the deleted VPC subnet.

SubnetAvailabilityZone -> (string)

The name of the Availability Zone of the deleted VPC subnet.

SubnetAvailabilityZoneId -> (string)

The ID of the Availability Zone of the deleted VPC subnet.

InvalidNetworkAclEntriesViolation -> (structure)

Violation detail for the entries in a network ACL resource.

Vpc -> (string)

The VPC where the violation was found.

Subnet -> (string)

The subnet thatâs associated with the network ACL.

SubnetAvailabilityZone -> (string)

The Availability Zone where the network ACL is in use.

CurrentAssociatedNetworkAcl -> (string)

The network ACL containing the entry violations.

EntryViolations -> (list)

Detailed information about the entry violations in the network ACL.

(structure)

Detailed information about an entry violation in a network ACL. The violation is against the network ACL specification inside the Firewall Manager network ACL policy. This data object is part of `InvalidNetworkAclEntriesViolation` .

ExpectedEntry -> (structure)

The Firewall Manager-managed network ACL entry that is involved in the entry violation.

EntryDetail -> (structure)

Describes a rule in a network ACL.

Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the network ACL, Amazon Web Services processes the entries in the network ACL according to the rule numbers, in ascending order.

When you manage an individual network ACL, you explicitly specify the rule numbers. When you specify the network ACL rules in a Firewall Manager policy, you provide the rules to run first, in the order that you want them to run, and the rules to run last, in the order that you want them to run. Firewall Manager assigns the rule numbers for you when you save the network ACL policy specification.

IcmpTypeCode -> (structure)

ICMP protocol: The ICMP type and code.

Code -> (integer)

ICMP code.

Type -> (integer)

ICMP type.

Protocol -> (string)

The protocol number. A value of â-1â means all protocols.

PortRange -> (structure)

TCP or UDP protocols: The range of ports the rule applies to.

From -> (integer)

The beginning port number of the range.

To -> (integer)

The ending port number of the range.

CidrBlock -> (string)

The IPv4 network range to allow or deny, in CIDR notation.

Ipv6CidrBlock -> (string)

The IPv6 network range to allow or deny, in CIDR notation.

RuleAction -> (string)

Indicates whether to allow or deny the traffic that matches the rule.

Egress -> (boolean)

Indicates whether the rule is an egress, or outbound, rule (applied to traffic leaving the subnet). If itâs not an egress rule, then itâs an ingress, or inbound, rule.

EntryRuleNumber -> (integer)

The rule number for the entry. ACL entries are processed in ascending order by rule number. In a Firewall Manager network ACL policy, Firewall Manager assigns rule numbers.

EntryType -> (string)

Specifies whether the entry is managed by Firewall Manager or by a user, and, for Firewall Manager-managed entries, specifies whether the entry is among those that run first in the network ACL or those that run last.

ExpectedEvaluationOrder -> (string)

The evaluation location within the ordered list of entries where the `ExpectedEntry` should be, according to the network ACL policy specifications.

ActualEvaluationOrder -> (string)

The evaluation location within the ordered list of entries where the `ExpectedEntry` is currently located.

EntryAtExpectedEvaluationOrder -> (structure)

The entry thatâs currently in the `ExpectedEvaluationOrder` location, in place of the expected entry.

EntryDetail -> (structure)

Describes a rule in a network ACL.

Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the network ACL, Amazon Web Services processes the entries in the network ACL according to the rule numbers, in ascending order.

When you manage an individual network ACL, you explicitly specify the rule numbers. When you specify the network ACL rules in a Firewall Manager policy, you provide the rules to run first, in the order that you want them to run, and the rules to run last, in the order that you want them to run. Firewall Manager assigns the rule numbers for you when you save the network ACL policy specification.

IcmpTypeCode -> (structure)

ICMP protocol: The ICMP type and code.

Code -> (integer)

ICMP code.

Type -> (integer)

ICMP type.

Protocol -> (string)

The protocol number. A value of â-1â means all protocols.

PortRange -> (structure)

TCP or UDP protocols: The range of ports the rule applies to.

From -> (integer)

The beginning port number of the range.

To -> (integer)

The ending port number of the range.

CidrBlock -> (string)

The IPv4 network range to allow or deny, in CIDR notation.

Ipv6CidrBlock -> (string)

The IPv6 network range to allow or deny, in CIDR notation.

RuleAction -> (string)

Indicates whether to allow or deny the traffic that matches the rule.

Egress -> (boolean)

Indicates whether the rule is an egress, or outbound, rule (applied to traffic leaving the subnet). If itâs not an egress rule, then itâs an ingress, or inbound, rule.

EntryRuleNumber -> (integer)

The rule number for the entry. ACL entries are processed in ascending order by rule number. In a Firewall Manager network ACL policy, Firewall Manager assigns rule numbers.

EntryType -> (string)

Specifies whether the entry is managed by Firewall Manager or by a user, and, for Firewall Manager-managed entries, specifies whether the entry is among those that run first in the network ACL or those that run last.

EntriesWithConflicts -> (list)

The list of entries that are in conflict with `ExpectedEntry` .

(structure)

Describes a single rule in a network ACL.

EntryDetail -> (structure)

Describes a rule in a network ACL.

Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the network ACL, Amazon Web Services processes the entries in the network ACL according to the rule numbers, in ascending order.

When you manage an individual network ACL, you explicitly specify the rule numbers. When you specify the network ACL rules in a Firewall Manager policy, you provide the rules to run first, in the order that you want them to run, and the rules to run last, in the order that you want them to run. Firewall Manager assigns the rule numbers for you when you save the network ACL policy specification.

IcmpTypeCode -> (structure)

ICMP protocol: The ICMP type and code.

Code -> (integer)

ICMP code.

Type -> (integer)

ICMP type.

Protocol -> (string)

The protocol number. A value of â-1â means all protocols.

PortRange -> (structure)

TCP or UDP protocols: The range of ports the rule applies to.

From -> (integer)

The beginning port number of the range.

To -> (integer)

The ending port number of the range.

CidrBlock -> (string)

The IPv4 network range to allow or deny, in CIDR notation.

Ipv6CidrBlock -> (string)

The IPv6 network range to allow or deny, in CIDR notation.

RuleAction -> (string)

Indicates whether to allow or deny the traffic that matches the rule.

Egress -> (boolean)

Indicates whether the rule is an egress, or outbound, rule (applied to traffic leaving the subnet). If itâs not an egress rule, then itâs an ingress, or inbound, rule.

EntryRuleNumber -> (integer)

The rule number for the entry. ACL entries are processed in ascending order by rule number. In a Firewall Manager network ACL policy, Firewall Manager assigns rule numbers.

EntryType -> (string)

Specifies whether the entry is managed by Firewall Manager or by a user, and, for Firewall Manager-managed entries, specifies whether the entry is among those that run first in the network ACL or those that run last.

EntryViolationReasons -> (list)

Descriptions of the violations that Firewall Manager found for these entries.

(string)

PossibleRemediationActions -> (structure)

A list of possible remediation action lists. Each individual possible remediation action is a list of individual remediation actions.

Description -> (string)

A description of the possible remediation actions list.

Actions -> (list)

Information about the actions.

(structure)

A list of remediation actions.

Description -> (string)

A description of the list of remediation actions.

OrderedRemediationActions -> (list)

The ordered list of remediation actions.

(structure)

An ordered list of actions you can take to remediate a violation.

RemediationAction -> (structure)

Information about an action you can take to remediate a violation.

Description -> (string)

A description of a remediation action.

EC2CreateRouteAction -> (structure)

Information about the CreateRoute action in the Amazon EC2 API.

Description -> (string)

A description of CreateRoute action in Amazon EC2.

DestinationCidrBlock -> (string)

Information about the IPv4 CIDR address block used for the destination match.

DestinationPrefixListId -> (string)

Information about the ID of a prefix list used for the destination match.

DestinationIpv6CidrBlock -> (string)

Information about the IPv6 CIDR block destination.

VpcEndpointId -> (structure)

Information about the ID of a VPC endpoint. Supported for Gateway Load Balancer endpoints only.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

GatewayId -> (structure)

Information about the ID of an internet gateway or virtual private gateway attached to your VPC.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

RouteTableId -> (structure)

Information about the ID of the route table for the route.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

EC2ReplaceRouteAction -> (structure)

Information about the ReplaceRoute action in the Amazon EC2 API.

Description -> (string)

A description of the ReplaceRoute action in Amazon EC2.

DestinationCidrBlock -> (string)

Information about the IPv4 CIDR address block used for the destination match. The value that you provide must match the CIDR of an existing route in the table.

DestinationPrefixListId -> (string)

Information about the ID of the prefix list for the route.

DestinationIpv6CidrBlock -> (string)

Information about the IPv6 CIDR address block used for the destination match. The value that you provide must match the CIDR of an existing route in the table.

GatewayId -> (structure)

Information about the ID of an internet gateway or virtual private gateway.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

RouteTableId -> (structure)

Information about the ID of the route table.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

EC2DeleteRouteAction -> (structure)

Information about the DeleteRoute action in the Amazon EC2 API.

Description -> (string)

A description of the DeleteRoute action.

DestinationCidrBlock -> (string)

Information about the IPv4 CIDR range for the route. The value you specify must match the CIDR for the route exactly.

DestinationPrefixListId -> (string)

Information about the ID of the prefix list for the route.

DestinationIpv6CidrBlock -> (string)

Information about the IPv6 CIDR range for the route. The value you specify must match the CIDR for the route exactly.

RouteTableId -> (structure)

Information about the ID of the route table.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

EC2CopyRouteTableAction -> (structure)

Information about the CopyRouteTable action in the Amazon EC2 API.

Description -> (string)

A description of the copied EC2 route table that is associated with the remediation action.

VpcId -> (structure)

The VPC ID of the copied EC2 route table that is associated with the remediation action.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

RouteTableId -> (structure)

The ID of the copied EC2 route table that is associated with the remediation action.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

EC2ReplaceRouteTableAssociationAction -> (structure)

Information about the ReplaceRouteTableAssociation action in the Amazon EC2 API.

Description -> (string)

A description of the ReplaceRouteTableAssociation action in Amazon EC2.

AssociationId -> (structure)

Information about the association ID.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

RouteTableId -> (structure)

Information about the ID of the new route table to associate with the subnet.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

EC2AssociateRouteTableAction -> (structure)

Information about the AssociateRouteTable action in the Amazon EC2 API.

Description -> (string)

A description of the EC2 route table that is associated with the remediation action.

RouteTableId -> (structure)

The ID of the EC2 route table that is associated with the remediation action.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

SubnetId -> (structure)

The ID of the subnet for the EC2 route table that is associated with the remediation action.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

GatewayId -> (structure)

The ID of the gateway to be used with the EC2 route table that is associated with the remediation action.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

EC2CreateRouteTableAction -> (structure)

Information about the CreateRouteTable action in the Amazon EC2 API.

Description -> (string)

A description of the CreateRouteTable action.

VpcId -> (structure)

Information about the ID of a VPC.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

FMSPolicyUpdateFirewallCreationConfigAction -> (structure)

The remedial action to take when updating a firewall configuration.

Description -> (string)

Describes the remedial action.

FirewallCreationConfig -> (string)

A `FirewallCreationConfig` that you can copy into your current policyâs [SecurityServiceData](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_SecurityServicePolicyData.html) in order to remedy scope violations.

CreateNetworkAclAction -> (structure)

Information about the `CreateNetworkAcl` action in Amazon EC2.

Description -> (string)

Brief description of this remediation action.

Vpc -> (structure)

The VPC thatâs associated with the remediation action.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

FMSCanRemediate -> (boolean)

Indicates whether it is possible for Firewall Manager to perform this remediation action. A false value indicates that auto remediation is disabled or Firewall Manager is unable to perform the action due to a conflict of some kind.

ReplaceNetworkAclAssociationAction -> (structure)

Information about the `ReplaceNetworkAclAssociation` action in Amazon EC2.

Description -> (string)

Brief description of this remediation action.

AssociationId -> (structure)

Describes a remediation action target.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

NetworkAclId -> (structure)

The network ACL thatâs associated with the remediation action.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

FMSCanRemediate -> (boolean)

Indicates whether it is possible for Firewall Manager to perform this remediation action. A false value indicates that auto remediation is disabled or Firewall Manager is unable to perform the action due to a conflict of some kind.

CreateNetworkAclEntriesAction -> (structure)

Information about the `CreateNetworkAclEntries` action in Amazon EC2.

Description -> (string)

Brief description of this remediation action.

NetworkAclId -> (structure)

The network ACL thatâs associated with the remediation action.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

NetworkAclEntriesToBeCreated -> (list)

Lists the entries that the remediation action would create.

(structure)

Describes a single rule in a network ACL.

EntryDetail -> (structure)

Describes a rule in a network ACL.

Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the network ACL, Amazon Web Services processes the entries in the network ACL according to the rule numbers, in ascending order.

When you manage an individual network ACL, you explicitly specify the rule numbers. When you specify the network ACL rules in a Firewall Manager policy, you provide the rules to run first, in the order that you want them to run, and the rules to run last, in the order that you want them to run. Firewall Manager assigns the rule numbers for you when you save the network ACL policy specification.

IcmpTypeCode -> (structure)

ICMP protocol: The ICMP type and code.

Code -> (integer)

ICMP code.

Type -> (integer)

ICMP type.

Protocol -> (string)

The protocol number. A value of â-1â means all protocols.

PortRange -> (structure)

TCP or UDP protocols: The range of ports the rule applies to.

From -> (integer)

The beginning port number of the range.

To -> (integer)

The ending port number of the range.

CidrBlock -> (string)

The IPv4 network range to allow or deny, in CIDR notation.

Ipv6CidrBlock -> (string)

The IPv6 network range to allow or deny, in CIDR notation.

RuleAction -> (string)

Indicates whether to allow or deny the traffic that matches the rule.

Egress -> (boolean)

Indicates whether the rule is an egress, or outbound, rule (applied to traffic leaving the subnet). If itâs not an egress rule, then itâs an ingress, or inbound, rule.

EntryRuleNumber -> (integer)

The rule number for the entry. ACL entries are processed in ascending order by rule number. In a Firewall Manager network ACL policy, Firewall Manager assigns rule numbers.

EntryType -> (string)

Specifies whether the entry is managed by Firewall Manager or by a user, and, for Firewall Manager-managed entries, specifies whether the entry is among those that run first in the network ACL or those that run last.

FMSCanRemediate -> (boolean)

Indicates whether it is possible for Firewall Manager to perform this remediation action. A false value indicates that auto remediation is disabled or Firewall Manager is unable to perform the action due to a conflict of some kind.

DeleteNetworkAclEntriesAction -> (structure)

Information about the `DeleteNetworkAclEntries` action in Amazon EC2.

Description -> (string)

Brief description of this remediation action.

NetworkAclId -> (structure)

The network ACL thatâs associated with the remediation action.

ResourceId -> (string)

The ID of the remediation target.

Description -> (string)

A description of the remediation action target.

NetworkAclEntriesToBeDeleted -> (list)

Lists the entries that the remediation action would delete.

(structure)

Describes a single rule in a network ACL.

EntryDetail -> (structure)

Describes a rule in a network ACL.

Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the network ACL, Amazon Web Services processes the entries in the network ACL according to the rule numbers, in ascending order.

When you manage an individual network ACL, you explicitly specify the rule numbers. When you specify the network ACL rules in a Firewall Manager policy, you provide the rules to run first, in the order that you want them to run, and the rules to run last, in the order that you want them to run. Firewall Manager assigns the rule numbers for you when you save the network ACL policy specification.

IcmpTypeCode -> (structure)

ICMP protocol: The ICMP type and code.

Code -> (integer)

ICMP code.

Type -> (integer)

ICMP type.

Protocol -> (string)

The protocol number. A value of â-1â means all protocols.

PortRange -> (structure)

TCP or UDP protocols: The range of ports the rule applies to.

From -> (integer)

The beginning port number of the range.

To -> (integer)

The ending port number of the range.

CidrBlock -> (string)

The IPv4 network range to allow or deny, in CIDR notation.

Ipv6CidrBlock -> (string)

The IPv6 network range to allow or deny, in CIDR notation.

RuleAction -> (string)

Indicates whether to allow or deny the traffic that matches the rule.

Egress -> (boolean)

Indicates whether the rule is an egress, or outbound, rule (applied to traffic leaving the subnet). If itâs not an egress rule, then itâs an ingress, or inbound, rule.

EntryRuleNumber -> (integer)

The rule number for the entry. ACL entries are processed in ascending order by rule number. In a Firewall Manager network ACL policy, Firewall Manager assigns rule numbers.

EntryType -> (string)

Specifies whether the entry is managed by Firewall Manager or by a user, and, for Firewall Manager-managed entries, specifies whether the entry is among those that run first in the network ACL or those that run last.

FMSCanRemediate -> (boolean)

Indicates whether it is possible for Firewall Manager to perform this remediation action. A false value indicates that auto remediation is disabled or Firewall Manager is unable to perform the action due to a conflict of some kind.

Order -> (integer)

The order of the remediation actions in the list.

IsDefaultAction -> (boolean)

Information about whether an action is taken by default.

WebACLHasIncompatibleConfigurationViolation -> (structure)

The violation details for a web ACL whose configuration is incompatible with the Firewall Manager policy.

WebACLArn -> (string)

The Amazon Resource Name (ARN) of the web ACL.

Description -> (string)

Information about the problems that Firewall Manager encountered with the web ACL configuration.

WebACLHasOutOfScopeResourcesViolation -> (structure)

The violation details for a web ACL thatâs associated with at least one resource thatâs out of scope of the Firewall Manager policy.

WebACLArn -> (string)

The Amazon Resource Name (ARN) of the web ACL.

OutOfScopeResourceList -> (list)

An array of Amazon Resource Name (ARN) for the resources that are out of scope of the policy and are associated with the web ACL.

(string)

ResourceTags -> (list)

The `ResourceTag` objects associated with the resource.

(structure)

A collection of key:value pairs associated with an Amazon Web Services resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as âenvironmentâ) and the tag value represents a specific value within that category (such as âtest,â âdevelopment,â or âproductionâ). You can add up to 50 tags to each Amazon Web Services resource.

Key -> (string)

Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as âcustomer.â Tag keys are case-sensitive.

Value -> (string)

Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as âcompanyAâ or âcompanyB.â Tag values are case-sensitive.

ResourceDescription -> (string)

Brief description for the requested resource.