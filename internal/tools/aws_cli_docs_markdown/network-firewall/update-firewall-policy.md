# update-firewall-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-firewall-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-firewall-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [network-firewall](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/index.html#cli-aws-network-firewall) ]

# update-firewall-policy

## Description

Updates the properties of the specified firewall policy.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/network-firewall-2020-11-12/UpdateFirewallPolicy)

## Synopsis

```
update-firewall-policy
--update-token <value>
[--firewall-policy-arn <value>]
[--firewall-policy-name <value>]
--firewall-policy <value>
[--description <value>]
[--dry-run | --no-dry-run]
[--encryption-configuration <value>]
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

A token used for optimistic locking. Network Firewall returns a token to your requests that access the firewall policy. The token marks the state of the policy resource at the time of the request.

To make changes to the policy, you provide the token in your request. Network Firewall uses the token to ensure that the policy hasnât changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException` . If this happens, retrieve the firewall policy again to get a current copy of it with current token. Reapply your changes as needed, then try the operation again using the new token.

`--firewall-policy-arn` (string)

The Amazon Resource Name (ARN) of the firewall policy.

You must specify the ARN or the name, and you can specify both.

`--firewall-policy-name` (string)

The descriptive name of the firewall policy. You canât change the name of a firewall policy after you create it.

You must specify the ARN or the name, and you can specify both.

`--firewall-policy` (structure)

The updated firewall policy to use for the firewall. You canât add or remove a  TLSInspectionConfiguration after you create a firewall policy. However, you can replace an existing TLS inspection configuration with another `TLSInspectionConfiguration` .

StatelessRuleGroupReferences -> (list)

References to the stateless rule groups that are used in the policy. These define the matching criteria in stateless rules.

(structure)

Identifier for a single stateless rule group, used in a firewall policy to refer to the rule group.

ResourceArn -> (string)

The Amazon Resource Name (ARN) of the stateless rule group.

Priority -> (integer)

An integer setting that indicates the order in which to run the stateless rule groups in a single  FirewallPolicy . Network Firewall applies each stateless rule group to a packet starting with the group that has the lowest priority setting. You must ensure that the priority settings are unique within each policy.

StatelessDefaultActions -> (list)

The actions to take on a packet if it doesnât match any of the stateless rules in the policy. If you want non-matching packets to be forwarded for stateful inspection, specify `aws:forward_to_sfe` .

You must specify one of the standard actions: `aws:pass` , `aws:drop` , or `aws:forward_to_sfe` . In addition, you can specify custom actions that are compatible with your standard section choice.

For example, you could specify `["aws:pass"]` or you could specify `["aws:pass", âcustomActionNameâ]` . For information about compatibility, see the custom action descriptions under  CustomAction .

(string)

StatelessFragmentDefaultActions -> (list)

The actions to take on a fragmented UDP packet if it doesnât match any of the stateless rules in the policy. Network Firewall only manages UDP packet fragments and silently drops packet fragments for other protocols. If you want non-matching fragmented UDP packets to be forwarded for stateful inspection, specify `aws:forward_to_sfe` .

You must specify one of the standard actions: `aws:pass` , `aws:drop` , or `aws:forward_to_sfe` . In addition, you can specify custom actions that are compatible with your standard section choice.

For example, you could specify `["aws:pass"]` or you could specify `["aws:pass", âcustomActionNameâ]` . For information about compatibility, see the custom action descriptions under  CustomAction .

(string)

StatelessCustomActions -> (list)

The custom action definitions that are available for use in the firewall policyâs `StatelessDefaultActions` setting. You name each custom action that you define, and then you can use it by name in your default actions specifications.

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

StatefulRuleGroupReferences -> (list)

References to the stateful rule groups that are used in the policy. These define the inspection criteria in stateful rules.

(structure)

Identifier for a single stateful rule group, used in a firewall policy to refer to a rule group.

ResourceArn -> (string)

The Amazon Resource Name (ARN) of the stateful rule group.

Priority -> (integer)

An integer setting that indicates the order in which to run the stateful rule groups in a single  FirewallPolicy . This setting only applies to firewall policies that specify the `STRICT_ORDER` rule order in the stateful engine options settings.

Network Firewall evalutes each stateful rule group against a packet starting with the group that has the lowest priority setting. You must ensure that the priority settings are unique within each policy.

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

For more information, see [Strict evaluation order](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html#suricata-strict-rule-evaluation-order.html) in the *Network Firewall Developer Guide* .

(string)

StatefulEngineOptions -> (structure)

Additional options governing how Network Firewall handles stateful rules. The stateful rule groups that you use in your policy must have stateful rule options settings that are compatible with these settings.

RuleOrder -> (string)

Indicates how to manage the order of stateful rule evaluation for the policy. `STRICT_ORDER` is the default and recommended option. With `STRICT_ORDER` , provide your rules in the order that you want them to be evaluated. You can then choose one or more default actions for packets that donât match any rules. Choose `STRICT_ORDER` to have the stateful rules engine determine the evaluation order of your rules. The default action for this rule order is `PASS` , followed by `DROP` , `REJECT` , and `ALERT` actions. Stateful rules are provided to the rule engine as Suricata compatible strings, and Suricata evaluates them based on your settings. For more information, see [Evaluation order for stateful rules](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html) in the *Network Firewall Developer Guide* .

StreamExceptionPolicy -> (string)

Configures how Network Firewall processes traffic when a network connection breaks midstream. Network connections can break due to disruptions in external networks or within the firewall itself.

- `DROP` - Network Firewall fails closed and drops all subsequent traffic going to the firewall. This is the default behavior.
- `CONTINUE` - Network Firewall continues to apply rules to the subsequent traffic without context from traffic before the break. This impacts the behavior of rules that depend on this context. For example, if you have a stateful rule to `drop http` traffic, Network Firewall wonât match the traffic for this rule because the service wonât have the context from session initialization defining the application layer protocol as HTTP. However, this behavior is rule dependentâa TCP-layer rule using a `flow:stateless` rule would still match, as would the `aws:drop_strict` default action.
- `REJECT` - Network Firewall fails closed and drops all subsequent traffic going to the firewall. Network Firewall also sends a TCP reject packet back to your client so that the client can immediately establish a new session. Network Firewall will have context about the new session and will apply rules to the subsequent traffic.

FlowTimeouts -> (structure)

Configures the amount of time that can pass without any traffic sent through the firewall before the firewall determines that the connection is idle.

TcpIdleTimeoutSeconds -> (integer)

The number of seconds that can pass without any TCP traffic sent through the firewall before the firewall determines that the connection is idle. After the idle timeout passes, data packets are dropped, however, the next TCP SYN packet is considered a new flow and is processed by the firewall. Clients or targets can use TCP keepalive packets to reset the idle timeout.

You can define the `TcpIdleTimeoutSeconds` value to be between 60 and 6000 seconds. If no value is provided, it defaults to 350 seconds.

TLSInspectionConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the TLS inspection configuration.

PolicyVariables -> (structure)

Contains variables that you can use to override default Suricata settings in your firewall policy.

RuleVariables -> (map)

The IPv4 or IPv6 addresses in CIDR notation to use for the Suricata `HOME_NET` variable. If your firewall uses an inspection VPC, you might want to override the `HOME_NET` variable with the CIDRs of your home networks. If you donât override `HOME_NET` with your own CIDRs, Network Firewall by default uses the CIDR of your inspection VPC.

key -> (string)

value -> (structure)

A list of IP addresses and address ranges, in CIDR notation. This is part of a  RuleVariables .

Definition -> (list)

The list of IP addresses and address ranges, in CIDR notation.

(string)

JSON Syntax:

```
{
  "StatelessRuleGroupReferences": [
    {
      "ResourceArn": "string",
      "Priority": integer
    }
    ...
  ],
  "StatelessDefaultActions": ["string", ...],
  "StatelessFragmentDefaultActions": ["string", ...],
  "StatelessCustomActions": [
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
  ],
  "StatefulRuleGroupReferences": [
    {
      "ResourceArn": "string",
      "Priority": integer,
      "Override": {
        "Action": "DROP_TO_ALERT"
      }
    }
    ...
  ],
  "StatefulDefaultActions": ["string", ...],
  "StatefulEngineOptions": {
    "RuleOrder": "DEFAULT_ACTION_ORDER"|"STRICT_ORDER",
    "StreamExceptionPolicy": "DROP"|"CONTINUE"|"REJECT",
    "FlowTimeouts": {
      "TcpIdleTimeoutSeconds": integer
    }
  },
  "TLSInspectionConfigurationArn": "string",
  "PolicyVariables": {
    "RuleVariables": {"string": {
          "Definition": ["string", ...]
        }
      ...}
  }
}
```

`--description` (string)

A description of the firewall policy.

`--dry-run` | `--no-dry-run` (boolean)

Indicates whether you want Network Firewall to just check the validity of the request, rather than run the request.

If set to `TRUE` , Network Firewall checks whether the request can run successfully, but doesnât actually make the requested changes. The call returns the value that the request would return if you ran it with dry run set to `FALSE` , but doesnât make additions or changes to your resources. This option allows you to make sure that you have the required permissions to run the request and that your request parameters are valid.

If set to `FALSE` , Network Firewall makes the requested changes to your resources.

`--encryption-configuration` (structure)

A complex type that contains settings for encryption of your firewall policy resources.

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

A token used for optimistic locking. Network Firewall returns a token to your requests that access the firewall policy. The token marks the state of the policy resource at the time of the request.

To make changes to the policy, you provide the token in your request. Network Firewall uses the token to ensure that the policy hasnât changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException` . If this happens, retrieve the firewall policy again to get a current copy of it with current token. Reapply your changes as needed, then try the operation again using the new token.

FirewallPolicyResponse -> (structure)

The high-level properties of a firewall policy. This, along with the  FirewallPolicy , define the policy. You can retrieve all objects for a firewall policy by calling  DescribeFirewallPolicy .

FirewallPolicyName -> (string)

The descriptive name of the firewall policy. You canât change the name of a firewall policy after you create it.

FirewallPolicyArn -> (string)

The Amazon Resource Name (ARN) of the firewall policy.

### Note

If this response is for a create request that had `DryRun` set to `TRUE` , then this ARN is a placeholder that isnât attached to a valid resource.

FirewallPolicyId -> (string)

The unique identifier for the firewall policy.

Description -> (string)

A description of the firewall policy.

FirewallPolicyStatus -> (string)

The current status of the firewall policy. You can retrieve this for a firewall policy by calling  DescribeFirewallPolicy and providing the firewall policyâs name or ARN.

Tags -> (list)

The key:value pairs to associate with the resource.

(structure)

A key:value pair associated with an Amazon Web Services resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as âenvironmentâ) and the tag value represents a specific value within that category (such as âtest,â âdevelopment,â or âproductionâ). You can add up to 50 tags to each Amazon Web Services resource.

Key -> (string)

The part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as âcustomer.â Tag keys are case-sensitive.

Value -> (string)

The part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as âcompanyAâ or âcompanyB.â Tag values are case-sensitive.

ConsumedStatelessRuleCapacity -> (integer)

The number of capacity units currently consumed by the policyâs stateless rules.

ConsumedStatefulRuleCapacity -> (integer)

The number of capacity units currently consumed by the policyâs stateful rules.

NumberOfAssociations -> (integer)

The number of firewalls that are associated with this firewall policy.

EncryptionConfiguration -> (structure)

A complex type that contains the Amazon Web Services KMS encryption configuration settings for your firewall policy.

KeyId -> (string)

The ID of the Amazon Web Services Key Management Service (KMS) customer managed key. You can use any of the key identifiers that KMS supports, unless youâre using a key thatâs managed by another account. If youâre using a key managed by another account, then specify the key ARN. For more information, see [Key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *Amazon Web Services KMS Developer Guide* .

Type -> (string)

The type of Amazon Web Services KMS key to use for encryption of your Network Firewall resources.

LastModifiedTime -> (timestamp)

The last time that the firewall policy was changed.