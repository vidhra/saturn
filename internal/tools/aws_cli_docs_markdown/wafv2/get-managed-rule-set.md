# get-managed-rule-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-managed-rule-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-managed-rule-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [wafv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/index.html#cli-aws-wafv2) ]

# get-managed-rule-set

## Description

Retrieves the specified managed rule set.

### Note

This is intended for use only by vendors of managed rule sets. Vendors are Amazon Web Services and Amazon Web Services Marketplace sellers.

Vendors, you can use the managed rule set APIs to provide controlled rollout of your versioned managed rule group offerings for your customers. The APIs are `ListManagedRuleSets` , `GetManagedRuleSet` , `PutManagedRuleSetVersions` , and `UpdateManagedRuleSetVersionExpiryDate` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/wafv2-2019-07-29/GetManagedRuleSet)

## Synopsis

```
get-managed-rule-set
--name <value>
--scope <value>
--id <value>
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

`--name` (string)

The name of the managed rule set. You use this, along with the rule set ID, to identify the rule set.

This name is assigned to the corresponding managed rule group, which your customers can access and use.

`--scope` (string)

Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use `CLOUDFRONT` .

To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:

- CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1` .
- API and SDKs - For all calls, use the Region endpoint us-east-1.

Possible values:

- `CLOUDFRONT`
- `REGIONAL`

`--id` (string)

A unique identifier for the managed rule set. The ID is returned in the responses to commands like `list` . You provide it to operations like `get` and `update` .

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

ManagedRuleSet -> (structure)

The managed rule set that you requested.

Name -> (string)

The name of the managed rule set. You use this, along with the rule set ID, to identify the rule set.

This name is assigned to the corresponding managed rule group, which your customers can access and use.

Id -> (string)

A unique identifier for the managed rule set. The ID is returned in the responses to commands like `list` . You provide it to operations like `get` and `update` .

ARN -> (string)

The Amazon Resource Name (ARN) of the entity.

Description -> (string)

A description of the set that helps with identification.

PublishedVersions -> (map)

The versions of this managed rule set that are available for use by customers.

key -> (string)

value -> (structure)

Information for a single version of a managed rule set.

### Note

This is intended for use only by vendors of managed rule sets. Vendors are Amazon Web Services and Amazon Web Services Marketplace sellers.

Vendors, you can use the managed rule set APIs to provide controlled rollout of your versioned managed rule group offerings for your customers. The APIs are `ListManagedRuleSets` , `GetManagedRuleSet` , `PutManagedRuleSetVersions` , and `UpdateManagedRuleSetVersionExpiryDate` .

AssociatedRuleGroupArn -> (string)

The Amazon Resource Name (ARN) of the vendor rule group thatâs used to define the published version of your managed rule group.

Capacity -> (long)

The web ACL capacity units (WCUs) required for this rule group.

WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see [WAF web ACL capacity units (WCU)](https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html) in the *WAF Developer Guide* .

ForecastedLifetime -> (integer)

The amount of time you expect this version of your managed rule group to last, in days.

PublishTimestamp -> (timestamp)

The time that you first published this version.

Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, â2016-09-27T14:50Zâ.

LastUpdateTimestamp -> (timestamp)

The last time that you updated this version.

Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, â2016-09-27T14:50Zâ.

ExpiryTimestamp -> (timestamp)

The time that this version is set to expire.

Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, â2016-09-27T14:50Zâ.

RecommendedVersion -> (string)

The version that you would like your customers to use.

LabelNamespace -> (string)

The label namespace prefix for the managed rule groups that are offered to customers from this managed rule set. All labels that are added by rules in the managed rule group have this prefix.

- The syntax for the label namespace prefix for a managed rule group is the following:   `awswaf:managed:<vendor>:<rule group name>` :
- When a rule with a label matches a web request, WAF adds the fully qualified label to the request. A fully qualified label is made up of the label namespace from the rule group or web ACL where the rule is defined and the label from the rule, separated by a colon:   `<label namespace>:<label from rule>`

LockToken -> (string)

A token used for optimistic locking. WAF returns a token to your `get` and `list` requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like `update` and `delete` . WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a `WAFOptimisticLockException` . If this happens, perform another `get` , and use the new token returned by that operation.