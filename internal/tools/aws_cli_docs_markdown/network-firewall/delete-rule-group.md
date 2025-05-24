# delete-rule-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-rule-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-rule-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [network-firewall](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/index.html#cli-aws-network-firewall) ]

# delete-rule-group

## Description

Deletes the specified  RuleGroup .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/network-firewall-2020-11-12/DeleteRuleGroup)

## Synopsis

```
delete-rule-group
[--rule-group-name <value>]
[--rule-group-arn <value>]
[--type <value>]
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

`--rule-group-name` (string)

The descriptive name of the rule group. You canât change the name of a rule group after you create it.

You must specify the ARN or the name, and you can specify both.

`--rule-group-arn` (string)

The Amazon Resource Name (ARN) of the rule group.

You must specify the ARN or the name, and you can specify both.

`--type` (string)

Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.

### Note

This setting is required for requests that do not include the `RuleGroupARN` .

Possible values:

- `STATELESS`
- `STATEFUL`

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