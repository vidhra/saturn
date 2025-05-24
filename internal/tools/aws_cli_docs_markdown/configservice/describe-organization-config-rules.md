# describe-organization-config-rulesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-organization-config-rules.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-organization-config-rules.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configservice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice) ]

# describe-organization-config-rules

## Description

Returns a list of organization Config rules.

### Note

When you specify the limit and the next token, you receive a paginated response.

Limit and next token are not applicable if you specify organization Config rule names. It is only applicable, when you request all the organization Config rules.

*For accounts within an organization*

If you deploy an organizational rule or conformance pack in an organization administrator account, and then establish a delegated administrator and deploy an organizational rule or conformance pack in the delegated administrator account, you wonât be able to see the organizational rule or conformance pack in the organization administrator account from the delegated administrator account or see the organizational rule or conformance pack in the delegated administrator account from organization administrator account. The `DescribeOrganizationConfigRules` and `DescribeOrganizationConformancePacks` APIs can only see and interact with the organization-related resource that were deployed from within the account calling those APIs.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeOrganizationConfigRules)

`describe-organization-config-rules` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `OrganizationConfigRules`

## Synopsis

```
describe-organization-config-rules
[--organization-config-rule-names <value>]
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

`--organization-config-rule-names` (list)

The names of organization Config rules for which you want details. If you do not specify any names, Config returns details for all your organization Config rules.

(string)

Syntax:

```
"string" "string" ...
```

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

## Output

OrganizationConfigRules -> (list)

Returns a list of `OrganizationConfigRule` objects.

(structure)

An organization Config rule that has information about Config rules that Config creates in member accounts.

OrganizationConfigRuleName -> (string)

The name that you assign to organization Config rule.

OrganizationConfigRuleArn -> (string)

Amazon Resource Name (ARN) of organization Config rule.

OrganizationManagedRuleMetadata -> (structure)

An `OrganizationManagedRuleMetadata` object.

Description -> (string)

The description that you provide for your organization Config rule.

RuleIdentifier -> (string)

For organization config managed rules, a predefined identifier from a list. For example, `IAM_PASSWORD_POLICY` is a managed rule. To reference a managed rule, see [Using Config managed rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html) .

InputParameters -> (string)

A string, in JSON format, that is passed to your organization Config rule Lambda function.

MaximumExecutionFrequency -> (string)

The maximum frequency with which Config runs evaluations for a rule. This is for an Config managed rule that is triggered at a periodic frequency.

### Note

By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the `MaximumExecutionFrequency` parameter.

ResourceTypesScope -> (list)

The type of the Amazon Web Services resource that was evaluated.

(string)

ResourceIdScope -> (string)

The ID of the Amazon Web Services resource that was evaluated.

TagKeyScope -> (string)

One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.

TagValueScope -> (string)

The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).

OrganizationCustomRuleMetadata -> (structure)

An `OrganizationCustomRuleMetadata` object.

Description -> (string)

The description that you provide for your organization Config rule.

LambdaFunctionArn -> (string)

The lambda function ARN.

OrganizationConfigRuleTriggerTypes -> (list)

The type of notification that triggers Config to run an evaluation for a rule. You can specify the following notification types:

- `ConfigurationItemChangeNotification` - Triggers an evaluation when Config delivers a configuration item as a result of a resource change.
- `OversizedConfigurationItemChangeNotification` - Triggers an evaluation when Config delivers an oversized configuration item. Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
- `ScheduledNotification` - Triggers a periodic evaluation at the frequency specified for `MaximumExecutionFrequency` .

(string)

InputParameters -> (string)

A string, in JSON format, that is passed to your organization Config rule Lambda function.

MaximumExecutionFrequency -> (string)

The maximum frequency with which Config runs evaluations for a rule. Your custom rule is triggered when Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties .

### Note

By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the `MaximumExecutionFrequency` parameter.

ResourceTypesScope -> (list)

The type of the Amazon Web Services resource that was evaluated.

(string)

ResourceIdScope -> (string)

The ID of the Amazon Web Services resource that was evaluated.

TagKeyScope -> (string)

One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.

TagValueScope -> (string)

The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).

ExcludedAccounts -> (list)

A comma-separated list of accounts excluded from organization Config rule.

(string)

LastUpdateTime -> (timestamp)

The timestamp of the last update.

OrganizationCustomPolicyRuleMetadata -> (structure)

An object that specifies metadata for your organizationâs Config Custom Policy rule. The metadata includes the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata, such as resource type, resource ID of Amazon Web Services resource, and organization trigger types that initiate Config to evaluate Amazon Web Services resources against a rule.

Description -> (string)

The description that you provide for your organization Config Custom Policy rule.

OrganizationConfigRuleTriggerTypes -> (list)

The type of notification that triggers Config to run an evaluation for a rule. For Config Custom Policy rules, Config supports change triggered notification types:

- `ConfigurationItemChangeNotification` - Triggers an evaluation when Config delivers a configuration item as a result of a resource change.
- `OversizedConfigurationItemChangeNotification` - Triggers an evaluation when Config delivers an oversized configuration item. Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.

(string)

InputParameters -> (string)

A string, in JSON format, that is passed to your organization Config Custom Policy rule.

MaximumExecutionFrequency -> (string)

The maximum frequency with which Config runs evaluations for a rule. Your Config Custom Policy rule is triggered when Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties .

ResourceTypesScope -> (list)

The type of the Amazon Web Services resource that was evaluated.

(string)

ResourceIdScope -> (string)

The ID of the Amazon Web Services resource that was evaluated.

TagKeyScope -> (string)

One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.

TagValueScope -> (string)

The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).

PolicyRuntime -> (string)

The runtime system for your organization Config Custom Policy rules. Guard is a policy-as-code language that allows you to write policies that are enforced by Config Custom Policy rules. For more information about Guard, see the [Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard) .

DebugLogDeliveryAccounts -> (list)

A list of accounts that you can enable debug logging for your organization Config Custom Policy rule. List is null when debug logging is enabled for all accounts.

(string)

NextToken -> (string)

The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.