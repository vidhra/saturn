# put-organization-config-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-organization-config-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-organization-config-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configservice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice) ]

# put-organization-config-rule

## Description

Adds or updates an Config rule for your entire organization to evaluate if your Amazon Web Services resources comply with your desired configurations. For information on how many organization Config rules you can have per account, see ` **Service Limits** [https://docs.aws.amazon.com/config/latest/developerguide/configlimits](https://docs.aws.amazon.com/config/latest/developerguide/configlimits).html`__ in the *Config Developer Guide* .

Only a management account and a delegated administrator can create or update an organization Config rule. When calling this API with a delegated administrator, you must ensure Organizations `ListDelegatedAdministrator` permissions are added. An organization can have up to 3 delegated administrators.

This API enables organization service access through the `EnableAWSServiceAccess` action and creates a service-linked role `AWSServiceRoleForConfigMultiAccountSetup` in the management or delegated administrator account of your organization. The service-linked role is created only when the role does not exist in the caller account. Config verifies the existence of role with `GetRole` action.

To use this API with delegated administrator, register a delegated administrator by calling Amazon Web Services Organization `register-delegated-administrator` for `config-multiaccountsetup.amazonaws.com` .

There are two types of rules: *Config Managed Rules* and *Config Custom Rules* . You can use `PutOrganizationConfigRule` to create both Config Managed Rules and Config Custom Rules.

Config Managed Rules are predefined, customizable rules created by Config. For a list of managed rules, see [List of Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) . If you are adding an Config managed rule, you must specify the ruleâs identifier for the `RuleIdentifier` key.

Config Custom Rules are rules that you create from scratch. There are two ways to create Config custom rules: with Lambda functions ([Lambda Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/gettingstarted-concepts.html#gettingstarted-concepts-function) ) and with Guard ([Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard) ), a policy-as-code language. Config custom rules created with Lambda are called *Config Custom Lambda Rules* and Config custom rules created with Guard are called *Config Custom Policy Rules* .

If you are adding a new Config Custom Lambda rule, you first need to create an Lambda function in the management account or a delegated administrator that the rule invokes to evaluate your resources. You also need to create an IAM role in the managed account that can be assumed by the Lambda function. When you use `PutOrganizationConfigRule` to add a Custom Lambda rule to Config, you must specify the Amazon Resource Name (ARN) that Lambda assigns to the function.

### Note

Prerequisite: Ensure you call `EnableAllFeatures` API to enable all features in an organization.

Make sure to specify one of either `OrganizationCustomPolicyRuleMetadata` for Custom Policy rules, `OrganizationCustomRuleMetadata` for Custom Lambda rules, or `OrganizationManagedRuleMetadata` for managed rules.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutOrganizationConfigRule)

## Synopsis

```
put-organization-config-rule
--organization-config-rule-name <value>
[--organization-managed-rule-metadata <value>]
[--organization-custom-rule-metadata <value>]
[--excluded-accounts <value>]
[--organization-custom-policy-rule-metadata <value>]
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

`--organization-config-rule-name` (string)

The name that you assign to an organization Config rule.

`--organization-managed-rule-metadata` (structure)

An `OrganizationManagedRuleMetadata` object. This object specifies organization managed rule metadata such as resource type and ID of Amazon Web Services resource along with the rule identifier. It also provides the frequency with which you want Config to run evaluations for the rule if the trigger type is periodic.

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

Shorthand Syntax:

```
Description=string,RuleIdentifier=string,InputParameters=string,MaximumExecutionFrequency=string,ResourceTypesScope=string,string,ResourceIdScope=string,TagKeyScope=string,TagValueScope=string
```

JSON Syntax:

```
{
  "Description": "string",
  "RuleIdentifier": "string",
  "InputParameters": "string",
  "MaximumExecutionFrequency": "One_Hour"|"Three_Hours"|"Six_Hours"|"Twelve_Hours"|"TwentyFour_Hours",
  "ResourceTypesScope": ["string", ...],
  "ResourceIdScope": "string",
  "TagKeyScope": "string",
  "TagValueScope": "string"
}
```

`--organization-custom-rule-metadata` (structure)

An `OrganizationCustomRuleMetadata` object. This object specifies organization custom rule metadata such as resource type, resource ID of Amazon Web Services resource, Lambda function ARN, and organization trigger types that trigger Config to evaluate your Amazon Web Services resources against a rule. It also provides the frequency with which you want Config to run evaluations for the rule if the trigger type is periodic.

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

Shorthand Syntax:

```
Description=string,LambdaFunctionArn=string,OrganizationConfigRuleTriggerTypes=string,string,InputParameters=string,MaximumExecutionFrequency=string,ResourceTypesScope=string,string,ResourceIdScope=string,TagKeyScope=string,TagValueScope=string
```

JSON Syntax:

```
{
  "Description": "string",
  "LambdaFunctionArn": "string",
  "OrganizationConfigRuleTriggerTypes": ["ConfigurationItemChangeNotification"|"OversizedConfigurationItemChangeNotification"|"ScheduledNotification", ...],
  "InputParameters": "string",
  "MaximumExecutionFrequency": "One_Hour"|"Three_Hours"|"Six_Hours"|"Twelve_Hours"|"TwentyFour_Hours",
  "ResourceTypesScope": ["string", ...],
  "ResourceIdScope": "string",
  "TagKeyScope": "string",
  "TagValueScope": "string"
}
```

`--excluded-accounts` (list)

A comma-separated list of accounts that you want to exclude from an organization Config rule.

(string)

Syntax:

```
"string" "string" ...
```

`--organization-custom-policy-rule-metadata` (structure)

An `OrganizationCustomPolicyRuleMetadata` object. This object specifies metadata for your organizationâs Config Custom Policy rule. The metadata includes the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata, such as resource type, resource ID of Amazon Web Services resource, and organization trigger types that initiate Config to evaluate Amazon Web Services resources against a rule.

Description -> (string)

The description that you provide for your organization Config Custom Policy rule.

OrganizationConfigRuleTriggerTypes -> (list)

The type of notification that initiates Config to run an evaluation for a rule. For Config Custom Policy rules, Config supports change-initiated notification types:

- `ConfigurationItemChangeNotification` - Initiates an evaluation when Config delivers a configuration item as a result of a resource change.
- `OversizedConfigurationItemChangeNotification` - Initiates an evaluation when Config delivers an oversized configuration item. Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.

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

PolicyText -> (string)

The policy definition containing the logic for your organization Config Custom Policy rule.

DebugLogDeliveryAccounts -> (list)

A list of accounts that you can enable debug logging for your organization Config Custom Policy rule. List is null when debug logging is enabled for all accounts.

(string)

Shorthand Syntax:

```
Description=string,OrganizationConfigRuleTriggerTypes=string,string,InputParameters=string,MaximumExecutionFrequency=string,ResourceTypesScope=string,string,ResourceIdScope=string,TagKeyScope=string,TagValueScope=string,PolicyRuntime=string,PolicyText=string,DebugLogDeliveryAccounts=string,string
```

JSON Syntax:

```
{
  "Description": "string",
  "OrganizationConfigRuleTriggerTypes": ["ConfigurationItemChangeNotification"|"OversizedConfigurationItemChangeNotification", ...],
  "InputParameters": "string",
  "MaximumExecutionFrequency": "One_Hour"|"Three_Hours"|"Six_Hours"|"Twelve_Hours"|"TwentyFour_Hours",
  "ResourceTypesScope": ["string", ...],
  "ResourceIdScope": "string",
  "TagKeyScope": "string",
  "TagValueScope": "string",
  "PolicyRuntime": "string",
  "PolicyText": "string",
  "DebugLogDeliveryAccounts": ["string", ...]
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

OrganizationConfigRuleArn -> (string)

The Amazon Resource Name (ARN) of an organization Config rule.