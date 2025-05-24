# update-rule-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-rule-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-rule-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [network-firewall](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/index.html#cli-aws-network-firewall) ]

# update-rule-group

## Description

Updates the rule settings for the specified rule group. You use a rule group by reference in one or more firewall policies. When you modify a rule group, you modify all firewall policies that use the rule group.

To update a rule group, first call  DescribeRuleGroup to retrieve the current  RuleGroup object, update the object as needed, and then provide the updated object to this call.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/network-firewall-2020-11-12/UpdateRuleGroup)

## Synopsis

```
update-rule-group
--update-token <value>
[--rule-group-arn <value>]
[--rule-group-name <value>]
[--rule-group <value>]
[--rules <value>]
[--type <value>]
[--description <value>]
[--dry-run | --no-dry-run]
[--encryption-configuration <value>]
[--source-metadata <value>]
[--analyze-rule-group | --no-analyze-rule-group]
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

`--update-token` (string)

A token used for optimistic locking. Network Firewall returns a token to your requests that access the rule group. The token marks the state of the rule group resource at the time of the request.

To make changes to the rule group, you provide the token in your request. Network Firewall uses the token to ensure that the rule group hasnât changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException` . If this happens, retrieve the rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.

`--rule-group-arn` (string)

The Amazon Resource Name (ARN) of the rule group.

You must specify the ARN or the name, and you can specify both.

`--rule-group-name` (string)

The descriptive name of the rule group. You canât change the name of a rule group after you create it.

You must specify the ARN or the name, and you can specify both.

`--rule-group` (structure)

An object that defines the rule group rules.

### Note

You must provide either this rule group setting or a `Rules` setting, but not both.

RuleVariables -> (structure)

Settings that are available for use in the rules in the rule group. You can only use these for stateful rule groups.

IPSets -> (map)

A list of IP addresses and address ranges, in CIDR notation.

key -> (string)

value -> (structure)

A list of IP addresses and address ranges, in CIDR notation. This is part of a  RuleVariables .

Definition -> (list)

The list of IP addresses and address ranges, in CIDR notation.

(string)

PortSets -> (map)

A list of port ranges.

key -> (string)

value -> (structure)

A set of port ranges for use in the rules in a rule group.

Definition -> (list)

The set of port ranges.

(string)

ReferenceSets -> (structure)

The list of a rule groupâs reference sets.

IPSetReferences -> (map)

The list of IP set references.

key -> (string)

value -> (structure)

Configures one or more IP set references for a Suricata-compatible rule group. This is used in  CreateRuleGroup or  UpdateRuleGroup . An IP set reference is a rule variable that references resources that you create and manage in another Amazon Web Services service, such as an Amazon VPC prefix list. Network Firewall IP set references enable you to dynamically update the contents of your rules. When you create, update, or delete the resource you are referencing in your rule, Network Firewall automatically updates the ruleâs content with the changes. For more information about IP set references in Network Firewall, see [Using IP set references](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-ip-set-references) in the *Network Firewall Developer Guide* .

Network Firewall currently supports [Amazon VPC prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html) and [resource groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-ip-set-references.html#rule-groups-referencing-resource-groups) in IP set references.

ReferenceArn -> (string)

The Amazon Resource Name (ARN) of the resource that you are referencing in your rule group.

RulesSource -> (structure)

The stateful rules or stateless rules for the rule group.

RulesString -> (string)

Stateful inspection criteria, provided in Suricata compatible rules. Suricata is an open-source threat detection framework that includes a standard rule-based language for network traffic inspection.

These rules contain the inspection criteria and the action to take for traffic that matches the criteria, so this type of rule group doesnât have a separate action setting.

### Note

You canât use the `priority` keyword if the `RuleOrder` option in  StatefulRuleOptions is set to `STRICT_ORDER` .

RulesSourceList -> (structure)

Stateful inspection criteria for a domain list rule group.

Targets -> (list)

The domains that you want to inspect for in your traffic flows. Valid domain specifications are the following:

- Explicit names. For example, `abc.example.com` matches only the domain `abc.example.com` .
- Names that use a domain wildcard, which you indicate with an initial â`.` â. For example,``.example.com`` matches `example.com` and matches all subdomains of `example.com` , such as `abc.example.com` and `www.example.com` .

(string)

TargetTypes -> (list)

The protocols you want to inspect. Specify `TLS_SNI` for `HTTPS` . Specify `HTTP_HOST` for `HTTP` . You can specify either or both.

(string)

GeneratedRulesType -> (string)

Whether you want to allow or deny access to the domains in your target list.

StatefulRules -> (list)

An array of individual stateful rules inspection criteria to be used together in a stateful rule group. Use this option to specify simple Suricata rules with protocol, source and destination, ports, direction, and rule options. For information about the Suricata `Rules` format, see [Rules Format](https://suricata.readthedocs.io/en/suricata-7.0.3/rules/intro.html) .

(structure)

A single Suricata rules specification, for use in a stateful rule group. Use this option to specify a simple Suricata rule with protocol, source and destination, ports, direction, and rule options. For information about the Suricata `Rules` format, see [Rules Format](https://suricata.readthedocs.io/en/suricata-7.0.3/rules/intro.html) .

Action -> (string)

Defines what Network Firewall should do with the packets in a traffic flow when the flow matches the stateful rule criteria. For all actions, Network Firewall performs the specified action and discontinues stateful inspection of the traffic flow.

The actions for a stateful rule are defined as follows:

- **PASS** - Permits the packets to go to the intended destination.
- **DROP** - Blocks the packets from going to the intended destination and sends an alert log message, if alert logging is configured in the  Firewall   LoggingConfiguration .
- **ALERT** - Sends an alert log message, if alert logging is configured in the  Firewall   LoggingConfiguration .  You can use this action to test a rule that you intend to use to drop traffic. You can enable the rule with `ALERT` action, verify in the logs that the rule is filtering as you want, then change the action to `DROP` .
- **REJECT** - Drops traffic that matches the conditions of the stateful rule, and sends a TCP reset packet back to sender of the packet. A TCP reset packet is a packet with no payload and an RST bit contained in the TCP header flags. REJECT is available only for TCP traffic. This option doesnât support FTP or IMAP protocols.

Header -> (structure)

The stateful inspection criteria for this rule, used to inspect traffic flows.

Protocol -> (string)

The protocol to inspect for. To specify all, you can use `IP` , because all traffic on Amazon Web Services and on the internet is IP.

Source -> (string)

The source IP address or address range to inspect for, in CIDR notation. To match with any address, specify `ANY` .

Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6.

Examples:

- To configure Network Firewall to inspect for the IP address 192.0.2.44, specify `192.0.2.44/32` .
- To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify `192.0.2.0/24` .
- To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify `1111:0000:0000:0000:0000:0000:0000:0111/128` .
- To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify `1111:0000:0000:0000:0000:0000:0000:0000/64` .

For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) .

SourcePort -> (string)

The source port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994` . To match with any port, specify `ANY` .

Direction -> (string)

The direction of traffic flow to inspect. If set to `ANY` , the inspection matches bidirectional traffic, both from the source to the destination and from the destination to the source. If set to `FORWARD` , the inspection only matches traffic going from the source to the destination.

Destination -> (string)

The destination IP address or address range to inspect for, in CIDR notation. To match with any address, specify `ANY` .

Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6.

Examples:

- To configure Network Firewall to inspect for the IP address 192.0.2.44, specify `192.0.2.44/32` .
- To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify `192.0.2.0/24` .
- To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify `1111:0000:0000:0000:0000:0000:0000:0111/128` .
- To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify `1111:0000:0000:0000:0000:0000:0000:0000/64` .

For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) .

DestinationPort -> (string)

The destination port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994` . To match with any port, specify `ANY` .

RuleOptions -> (list)

Additional options for the rule. These are the Suricata `RuleOptions` settings.

(structure)

Additional settings for a stateful rule. This is part of the  StatefulRule configuration.

Keyword -> (string)

The keyword for the Suricata compatible rule option. You must include a `sid` (signature ID), and can optionally include other keywords. For information about Suricata compatible keywords, see [Rule options](https://suricata.readthedocs.io/en/suricata-7.0.3/rules/intro.html#rule-options) in the Suricata documentation.

Settings -> (list)

The settings of the Suricata compatible rule option. Rule options have zero or more setting values, and the number of possible and required settings depends on the `Keyword` . For more information about the settings for specific options, see [Rule options](https://suricata.readthedocs.io/en/suricata-7.0.3/rules/intro.html#rule-options) .

(string)

StatelessRulesAndCustomActions -> (structure)

Stateless inspection criteria to be used in a stateless rule group.

StatelessRules -> (list)

Defines the set of stateless rules for use in a stateless rule group.

(structure)

A single stateless rule. This is used in  StatelessRulesAndCustomActions .

RuleDefinition -> (structure)

Defines the stateless 5-tuple packet inspection criteria and the action to take on a packet that matches the criteria.

MatchAttributes -> (structure)

Criteria for Network Firewall to use to inspect an individual packet in stateless rule inspection. Each match attributes set can include one or more items such as IP address, CIDR range, port number, protocol, and TCP flags.

Sources -> (list)

The source IP addresses and address ranges to inspect for, in CIDR notation. If not specified, this matches with any source address.

(structure)

A single IP address specification. This is used in the  MatchAttributes source and destination specifications.

AddressDefinition -> (string)

Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6.

Examples:

- To configure Network Firewall to inspect for the IP address 192.0.2.44, specify `192.0.2.44/32` .
- To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify `192.0.2.0/24` .
- To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify `1111:0000:0000:0000:0000:0000:0000:0111/128` .
- To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify `1111:0000:0000:0000:0000:0000:0000:0000/64` .

For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) .

Destinations -> (list)

The destination IP addresses and address ranges to inspect for, in CIDR notation. If not specified, this matches with any destination address.

(structure)

A single IP address specification. This is used in the  MatchAttributes source and destination specifications.

AddressDefinition -> (string)

Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6.

Examples:

- To configure Network Firewall to inspect for the IP address 192.0.2.44, specify `192.0.2.44/32` .
- To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify `192.0.2.0/24` .
- To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify `1111:0000:0000:0000:0000:0000:0000:0111/128` .
- To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify `1111:0000:0000:0000:0000:0000:0000:0000/64` .

For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) .

SourcePorts -> (list)

The source port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994` . To match with any port, specify `ANY` .

If not specified, this matches with any source port.

This setting is only used for protocols 6 (TCP) and 17 (UDP).

(structure)

A single port range specification. This is used for source and destination port ranges in the stateless rule  MatchAttributes , `SourcePorts` , and `DestinationPorts` settings.

FromPort -> (integer)

The lower limit of the port range. This must be less than or equal to the `ToPort` specification.

ToPort -> (integer)

The upper limit of the port range. This must be greater than or equal to the `FromPort` specification.

DestinationPorts -> (list)

The destination port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994` . To match with any port, specify `ANY` .

This setting is only used for protocols 6 (TCP) and 17 (UDP).

(structure)

A single port range specification. This is used for source and destination port ranges in the stateless rule  MatchAttributes , `SourcePorts` , and `DestinationPorts` settings.

FromPort -> (integer)

The lower limit of the port range. This must be less than or equal to the `ToPort` specification.

ToPort -> (integer)

The upper limit of the port range. This must be greater than or equal to the `FromPort` specification.

Protocols -> (list)

The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.

(integer)

TCPFlags -> (list)

The TCP flags and masks to inspect for. If not specified, this matches with any settings. This setting is only used for protocol 6 (TCP).

(structure)

TCP flags and masks to inspect packets for, used in stateless rules  MatchAttributes settings.

Flags -> (list)

Used in conjunction with the `Masks` setting to define the flags that must be set and flags that must not be set in order for the packet to match. This setting can only specify values that are also specified in the `Masks` setting.

For the flags that are specified in the masks setting, the following must be true for the packet to match:

- The ones that are set in this flags setting must be set in the packet.
- The ones that are not set in this flags setting must also not be set in the packet.

(string)

Masks -> (list)

The set of flags to consider in the inspection. To inspect all flags in the valid values list, leave this with no setting.

(string)

Actions -> (list)

The actions to take on a packet that matches one of the stateless rule definitionâs match attributes. You must specify a standard action and you can add custom actions.

### Note

Network Firewall only forwards a packet for stateful rule inspection if you specify `aws:forward_to_sfe` for a rule that the packet matches, or if the packet doesnât match any stateless rule and you specify `aws:forward_to_sfe` for the `StatelessDefaultActions` setting for the  FirewallPolicy .

For every rule, you must specify exactly one of the following standard actions.

- **aws:pass** - Discontinues all inspection of the packet and permits it to go to its intended destination.
- **aws:drop** - Discontinues all inspection of the packet and blocks it from going to its intended destination.
- **aws:forward_to_sfe** - Discontinues stateless inspection of the packet and forwards it to the stateful rule engine for inspection.

Additionally, you can specify a custom action. To do this, you define a custom action by name and type, then provide the name youâve assigned to the action in this `Actions` setting. For information about the options, see  CustomAction .

To provide more than one action in this setting, separate the settings with a comma. For example, if you have a custom `PublishMetrics` action that youâve named `MyMetricsAction` , then you could specify the standard action `aws:pass` and the custom action with `[âaws:passâ, âMyMetricsActionâ]` .

(string)

Priority -> (integer)

Indicates the order in which to run this rule relative to all of the rules that are defined for a stateless rule group. Network Firewall evaluates the rules in a rule group starting with the lowest priority setting. You must ensure that the priority settings are unique for the rule group.

Each stateless rule group uses exactly one `StatelessRulesAndCustomActions` object, and each `StatelessRulesAndCustomActions` contains exactly one `StatelessRules` object. To ensure unique priority settings for your rule groups, set unique priorities for the stateless rules that you define inside any single `StatelessRules` object.

You can change the priority settings of your rules at any time. To make it easier to insert rules later, number them so thereâs a wide range in between, for example use 100, 200, and so on.

CustomActions -> (list)

Defines an array of individual custom action definitions that are available for use by the stateless rules in this `StatelessRulesAndCustomActions` specification. You name each custom action that you define, and then you can use it by name in your  StatelessRule   RuleDefinition  `Actions` specification.

(structure)

An optional, non-standard action to use for stateless packet handling. You can define this in addition to the standard action that you must specify.

You define and name the custom actions that you want to be able to use, and then you reference them by name in your actions settings.

You can use custom actions in the following places:

- In a rule groupâs  StatelessRulesAndCustomActions specification. The custom actions are available for use by name inside the `StatelessRulesAndCustomActions` where you define them. You can use them for your stateless rule actions to specify what to do with a packet that matches the ruleâs match attributes.
- In a  FirewallPolicy specification, in `StatelessCustomActions` . The custom actions are available for use inside the policy where you define them. You can use them for the policyâs default stateless actions settings to specify what to do with packets that donât match any of the policyâs stateless rules.

ActionName -> (string)

The descriptive name of the custom action. You canât change the name of a custom action after you create it.

ActionDefinition -> (structure)

The custom action associated with the action name.

PublishMetricAction -> (structure)

Stateless inspection criteria that publishes the specified metrics to Amazon CloudWatch for the matching packet. This setting defines a CloudWatch dimension value to be published.

You can pair this custom action with any of the standard stateless rule actions. For example, you could pair this in a rule action with the standard action that forwards the packet for stateful inspection. Then, when a packet matches the rule, Network Firewall publishes metrics for the packet and forwards it.

Dimensions -> (list)

(structure)

The value to use in an Amazon CloudWatch custom metric dimension. This is used in the `PublishMetrics`   CustomAction . A CloudWatch custom metric dimension is a name/value pair thatâs part of the identity of a metric.

Network Firewall sets the dimension name to `CustomAction` and you provide the dimension value.

For more information about CloudWatch custom metric dimensions, see [Publishing Custom Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html#usingDimensions) in the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) .

Value -> (string)

The value to use in the custom metric dimension.

StatefulRuleOptions -> (structure)

Additional options governing how Network Firewall handles stateful rules. The policies where you use your stateful rule group must have stateful rule options settings that are compatible with these settings. Some limitations apply; for more information, see [Strict evaluation order](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-limitations-caveats.html) in the *Network Firewall Developer Guide* .

RuleOrder -> (string)

Indicates how to manage the order of the rule evaluation for the rule group. `DEFAULT_ACTION_ORDER` is the default behavior. Stateful rules are provided to the rule engine as Suricata compatible strings, and Suricata evaluates them based on certain settings. For more information, see [Evaluation order for stateful rules](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html) in the *Network Firewall Developer Guide* .

JSON Syntax:

```
{
  "RuleVariables": {
    "IPSets": {"string": {
          "Definition": ["string", ...]
        }
      ...},
    "PortSets": {"string": {
          "Definition": ["string", ...]
        }
      ...}
  },
  "ReferenceSets": {
    "IPSetReferences": {"string": {
          "ReferenceArn": "string"
        }
      ...}
  },
  "RulesSource": {
    "RulesString": "string",
    "RulesSourceList": {
      "Targets": ["string", ...],
      "TargetTypes": ["TLS_SNI"|"HTTP_HOST", ...],
      "GeneratedRulesType": "ALLOWLIST"|"DENYLIST"
    },
    "StatefulRules": [
      {
        "Action": "PASS"|"DROP"|"ALERT"|"REJECT",
        "Header": {
          "Protocol": "IP"|"TCP"|"UDP"|"ICMP"|"HTTP"|"FTP"|"TLS"|"SMB"|"DNS"|"DCERPC"|"SSH"|"SMTP"|"IMAP"|"MSN"|"KRB5"|"IKEV2"|"TFTP"|"NTP"|"DHCP",
          "Source": "string",
          "SourcePort": "string",
          "Direction": "FORWARD"|"ANY",
          "Destination": "string",
          "DestinationPort": "string"
        },
        "RuleOptions": [
          {
            "Keyword": "string",
            "Settings": ["string", ...]
          }
          ...
        ]
      }
      ...
    ],
    "StatelessRulesAndCustomActions": {
      "StatelessRules": [
        {
          "RuleDefinition": {
            "MatchAttributes": {
              "Sources": [
                {
                  "AddressDefinition": "string"
                }
                ...
              ],
              "Destinations": [
                {
                  "AddressDefinition": "string"
                }
                ...
              ],
              "SourcePorts": [
                {
                  "FromPort": integer,
                  "ToPort": integer
                }
                ...
              ],
              "DestinationPorts": [
                {
                  "FromPort": integer,
                  "ToPort": integer
                }
                ...
              ],
              "Protocols": [integer, ...],
              "TCPFlags": [
                {
                  "Flags": ["FIN"|"SYN"|"RST"|"PSH"|"ACK"|"URG"|"ECE"|"CWR", ...],
                  "Masks": ["FIN"|"SYN"|"RST"|"PSH"|"ACK"|"URG"|"ECE"|"CWR", ...]
                }
                ...
              ]
            },
            "Actions": ["string", ...]
          },
          "Priority": integer
        }
        ...
      ],
      "CustomActions": [
        {
          "ActionName": "string",
          "ActionDefinition": {
            "PublishMetricAction": {
              "Dimensions": [
                {
                  "Value": "string"
                }
                ...
              ]
            }
          }
        }
        ...
      ]
    }
  },
  "StatefulRuleOptions": {
    "RuleOrder": "DEFAULT_ACTION_ORDER"|"STRICT_ORDER"
  }
}
```

`--rules` (string)

A string containing stateful rule group rules specifications in Suricata flat format, with one rule per line. Use this to import your existing Suricata compatible rule groups.

### Note

You must provide either this rules setting or a populated `RuleGroup` setting, but not both.

You can provide your rule group specification in Suricata flat format through this setting when you create or update your rule group. The call response returns a  RuleGroup object that Network Firewall has populated from your string.

`--type` (string)

Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.

### Note

This setting is required for requests that do not include the `RuleGroupARN` .

Possible values:

- `STATELESS`
- `STATEFUL`

`--description` (string)

A description of the rule group.

`--dry-run` | `--no-dry-run` (boolean)

Indicates whether you want Network Firewall to just check the validity of the request, rather than run the request.

If set to `TRUE` , Network Firewall checks whether the request can run successfully, but doesnât actually make the requested changes. The call returns the value that the request would return if you ran it with dry run set to `FALSE` , but doesnât make additions or changes to your resources. This option allows you to make sure that you have the required permissions to run the request and that your request parameters are valid.

If set to `FALSE` , Network Firewall makes the requested changes to your resources.

`--encryption-configuration` (structure)

A complex type that contains settings for encryption of your rule group resources.

KeyId -> (string)

The ID of the Amazon Web Services Key Management Service (KMS) customer managed key. You can use any of the key identifiers that KMS supports, unless youâre using a key thatâs managed by another account. If youâre using a key managed by another account, then specify the key ARN. For more information, see [Key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *Amazon Web Services KMS Developer Guide* .

Type -> (string)

The type of Amazon Web Services KMS key to use for encryption of your Network Firewall resources.

Shorthand Syntax:

```
KeyId=string,Type=string
```

JSON Syntax:

```
{
  "KeyId": "string",
  "Type": "CUSTOMER_KMS"|"AWS_OWNED_KMS_KEY"
}
```

`--source-metadata` (structure)

A complex type that contains metadata about the rule group that your own rule group is copied from. You can use the metadata to keep track of updates made to the originating rule group.

SourceArn -> (string)

The Amazon Resource Name (ARN) of the rule group that your own rule group is copied from.

SourceUpdateToken -> (string)

The update token of the Amazon Web Services managed rule group that your own rule group is copied from. To determine the update token for the managed rule group, call [DescribeRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeRuleGroup.html#networkfirewall-DescribeRuleGroup-response-UpdateToken) .

Shorthand Syntax:

```
SourceArn=string,SourceUpdateToken=string
```

JSON Syntax:

```
{
  "SourceArn": "string",
  "SourceUpdateToken": "string"
}
```

`--analyze-rule-group` | `--no-analyze-rule-group` (boolean)

Indicates whether you want Network Firewall to analyze the stateless rules in the rule group for rule behavior such as asymmetric routing. If set to `TRUE` , Network Firewall runs the analysis and then updates the rule group for you. To run the stateless rule group analyzer without updating the rule group, set `DryRun` to `TRUE` .

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

UpdateToken -> (string)

A token used for optimistic locking. Network Firewall returns a token to your requests that access the rule group. The token marks the state of the rule group resource at the time of the request.

To make changes to the rule group, you provide the token in your request. Network Firewall uses the token to ensure that the rule group hasnât changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException` . If this happens, retrieve the rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.

RuleGroupResponse -> (structure)

The high-level properties of a rule group. This, along with the  RuleGroup , define the rule group. You can retrieve all objects for a rule group by calling  DescribeRuleGroup .

RuleGroupArn -> (string)

The Amazon Resource Name (ARN) of the rule group.

### Note

If this response is for a create request that had `DryRun` set to `TRUE` , then this ARN is a placeholder that isnât attached to a valid resource.

RuleGroupName -> (string)

The descriptive name of the rule group. You canât change the name of a rule group after you create it.

RuleGroupId -> (string)

The unique identifier for the rule group.

Description -> (string)

A description of the rule group.

Type -> (string)

Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.

Capacity -> (integer)

The maximum operating resources that this rule group can use. Rule group capacity is fixed at creation. When you update a rule group, you are limited to this capacity. When you reference a rule group from a firewall policy, Network Firewall reserves this capacity for the rule group.

You can retrieve the capacity that would be required for a rule group before you create the rule group by calling  CreateRuleGroup with `DryRun` set to `TRUE` .

RuleGroupStatus -> (string)

Detailed information about the current status of a rule group.

Tags -> (list)

The key:value pairs to associate with the resource.

(structure)

A key:value pair associated with an Amazon Web Services resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as âenvironmentâ) and the tag value represents a specific value within that category (such as âtest,â âdevelopment,â or âproductionâ). You can add up to 50 tags to each Amazon Web Services resource.

Key -> (string)

The part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as âcustomer.â Tag keys are case-sensitive.

Value -> (string)

The part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as âcompanyAâ or âcompanyB.â Tag values are case-sensitive.

ConsumedCapacity -> (integer)

The number of capacity units currently consumed by the rule group rules.

NumberOfAssociations -> (integer)

The number of firewall policies that use this rule group.

EncryptionConfiguration -> (structure)

A complex type that contains the Amazon Web Services KMS encryption configuration settings for your rule group.

KeyId -> (string)

The ID of the Amazon Web Services Key Management Service (KMS) customer managed key. You can use any of the key identifiers that KMS supports, unless youâre using a key thatâs managed by another account. If youâre using a key managed by another account, then specify the key ARN. For more information, see [Key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *Amazon Web Services KMS Developer Guide* .

Type -> (string)

The type of Amazon Web Services KMS key to use for encryption of your Network Firewall resources.

SourceMetadata -> (structure)

A complex type that contains metadata about the rule group that your own rule group is copied from. You can use the metadata to track the version updates made to the originating rule group.

SourceArn -> (string)

The Amazon Resource Name (ARN) of the rule group that your own rule group is copied from.

SourceUpdateToken -> (string)

The update token of the Amazon Web Services managed rule group that your own rule group is copied from. To determine the update token for the managed rule group, call [DescribeRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeRuleGroup.html#networkfirewall-DescribeRuleGroup-response-UpdateToken) .

SnsTopic -> (string)

The Amazon resource name (ARN) of the Amazon Simple Notification Service SNS topic thatâs used to record changes to the managed rule group. You can subscribe to the SNS topic to receive notifications when the managed rule group is modified, such as for new versions and for version expiration. For more information, see the [Amazon Simple Notification Service Developer Guide.](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) .

LastModifiedTime -> (timestamp)

The last time that the rule group was changed.

AnalysisResults -> (list)

The list of analysis results for `AnalyzeRuleGroup` . If you set `AnalyzeRuleGroup` to `TRUE` in  CreateRuleGroup ,  UpdateRuleGroup , or  DescribeRuleGroup , Network Firewall analyzes the rule group and identifies the rules that might adversely effect your firewallâs functionality. For example, if Network Firewall detects a rule thatâs routing traffic asymmetrically, which impacts the serviceâs ability to properly process traffic, the service includes the rule in the list of analysis results.

(structure)

The analysis result for Network Firewallâs stateless rule group analyzer. Every time you call  CreateRuleGroup ,  UpdateRuleGroup , or  DescribeRuleGroup on a stateless rule group, Network Firewall analyzes the stateless rule groups in your account and identifies the rules that might adversely effect your firewallâs functionality. For example, if Network Firewall detects a rule thatâs routing traffic asymmetrically, which impacts the serviceâs ability to properly process traffic, the service includes the rule in a list of analysis results.

The `AnalysisResult` data type is not related to traffic analysis reports you generate using  StartAnalysisReport . For information on traffic analysis report results, see  AnalysisTypeReportResult .

IdentifiedRuleIds -> (list)

The priority number of the stateless rules identified in the analysis.

(string)

IdentifiedType -> (string)

The types of rule configurations that Network Firewall analyzes your rule groups for. Network Firewall analyzes stateless rule groups for the following types of rule configurations:

- `STATELESS_RULE_FORWARDING_ASYMMETRICALLY`   Cause: One or more stateless rules with the action `pass` or `forward` are forwarding traffic asymmetrically. Specifically, the ruleâs set of source IP addresses or their associated port numbers, donât match the set of destination IP addresses or their associated port numbers. To mitigate: Make sure that thereâs an existing return path. For example, if the rule allows traffic from source 10.1.0.0/24 to destination 20.1.0.0/24, you should allow return traffic from source 20.1.0.0/24 to destination 10.1.0.0/24.
- `STATELESS_RULE_CONTAINS_TCP_FLAGS`   Cause: At least one stateless rule with the action `pass` or``forward`` contains TCP flags that are inconsistent in the forward and return directions. To mitigate: Prevent asymmetric routing issues caused by TCP flags by following these actions:
- Remove unnecessary TCP flag inspections from the rules.
- If you need to inspect TCP flags, check that the rules correctly account for changes in TCP flags throughout the TCP connection cycle, for example `SYN` and `ACK` flags used in a 3-way TCP handshake.

AnalysisDetail -> (string)

Provides analysis details for the identified rule.