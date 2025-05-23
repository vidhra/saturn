# describe-config-rulesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-config-rules.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-config-rules.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configservice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice) ]

# describe-config-rules

## Description

Returns details about your Config rules.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigRules)

`describe-config-rules` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ConfigRules`

## Synopsis

```
describe-config-rules
[--config-rule-names <value>]
[--filters <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
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

`--config-rule-names` (list)

The names of the Config rules for which you want details. If you do not specify any names, Config returns details for all your rules.

(string)

Syntax:

```
"string" "string" ...
```

`--filters` (structure)

Returns a list of Detective or Proactive Config rules. By default, this API returns an unfiltered list. For more information on Detective or Proactive Config rules, see ` **Evaluation Mode** [https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules).html`__ in the *Config Developer Guide* .

EvaluationMode -> (string)

The mode of an evaluation. The valid values are Detective or Proactive.

Shorthand Syntax:

```
EvaluationMode=string
```

JSON Syntax:

```
{
  "EvaluationMode": "DETECTIVE"|"PROACTIVE"
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

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

**To get details for an AWS Config rule**

The following command returns details for an AWS Config rule named `InstanceTypesAreT2micro`:

```
aws configservice describe-config-rules --config-rule-names InstanceTypesAreT2micro
```

Output:

```
{
    "ConfigRules": [
        {
            "ConfigRuleState": "ACTIVE",
            "Description": "Evaluates whether EC2 instances are the t2.micro type.",
            "ConfigRuleName": "InstanceTypesAreT2micro",
            "ConfigRuleArn": "arn:aws:config:us-east-1:123456789012:config-rule/config-rule-abcdef",
            "Source": {
                "Owner": "CUSTOM_LAMBDA",
                "SourceIdentifier": "arn:aws:lambda:us-east-1:123456789012:function:InstanceTypeCheck",
                "SourceDetails": [
                    {
                        "EventSource": "aws.config",
                        "MessageType": "ConfigurationItemChangeNotification"
                    }
                ]
            },
            "InputParameters": "{\"desiredInstanceType\":\"t2.micro\"}",
            "Scope": {
                "ComplianceResourceTypes": [
                    "AWS::EC2::Instance"
                ]
            },
            "ConfigRuleId": "config-rule-abcdef"
        }
    ]
}
```

## Output

ConfigRules -> (list)

The details about your Config rules.

(structure)

Config rules evaluate the configuration settings of your Amazon Web Services resources. A rule can run when Config detects a configuration change to an Amazon Web Services resource or at a periodic frequency that you choose (for example, every 24 hours). There are two types of rules: *Config Managed Rules* and *Config Custom Rules* .

Config Managed Rules are predefined, customizable rules created by Config. For a list of managed rules, see [List of Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) .

Config Custom Rules are rules that you create from scratch. There are two ways to create Config custom rules: with Lambda functions ([Lambda Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/gettingstarted-concepts.html#gettingstarted-concepts-function) ) and with Guard ([Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard) ), a policy-as-code language. Config custom rules created with Lambda are called *Config Custom Lambda Rules* and Config custom rules created with Guard are called *Config Custom Policy Rules* .

For more information about developing and using Config rules, see [Evaluating Resource with Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) in the *Config Developer Guide* .

### Note

You can use the Amazon Web Services CLI and Amazon Web Services SDKs if you want to create a rule that triggers evaluations for your resources when Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties .

ConfigRuleName -> (string)

The name that you assign to the Config rule. The name is required if you are adding a new rule.

ConfigRuleArn -> (string)

The Amazon Resource Name (ARN) of the Config rule.

ConfigRuleId -> (string)

The ID of the Config rule.

Description -> (string)

The description that you provide for the Config rule.

Scope -> (structure)

Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.

### Note

The scope can be empty.

ComplianceResourceTypes -> (list)

The resource types of only those Amazon Web Services resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for `ComplianceResourceId` .

(string)

TagKey -> (string)

The tag key that is applied to only those Amazon Web Services resources that you want to trigger an evaluation for the rule.

TagValue -> (string)

The tag value applied to only those Amazon Web Services resources that you want to trigger an evaluation for the rule. If you specify a value for `TagValue` , you must also specify a value for `TagKey` .

ComplianceResourceId -> (string)

The ID of the only Amazon Web Services resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for `ComplianceResourceTypes` .

Source -> (structure)

Provides the rule owner (`Amazon Web Services` for managed rules, `CUSTOM_POLICY` for Custom Policy rules, and `CUSTOM_LAMBDA` for Custom Lambda rules), the rule identifier, and the notifications that cause the function to evaluate your Amazon Web Services resources.

Owner -> (string)

Indicates whether Amazon Web Services or the customer owns and manages the Config rule.

Config Managed Rules are predefined rules owned by Amazon Web Services. For more information, see [Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html) in the *Config developer guide* .

Config Custom Rules are rules that you can develop either with Guard (`CUSTOM_POLICY` ) or Lambda (`CUSTOM_LAMBDA` ). For more information, see [Config Custom Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html) in the *Config developer guide* .

SourceIdentifier -> (string)

For Config Managed rules, a predefined identifier from a list. For example, `IAM_PASSWORD_POLICY` is a managed rule. To reference a managed rule, see [List of Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) .

For Config Custom Lambda rules, the identifier is the Amazon Resource Name (ARN) of the ruleâs Lambda function, such as `arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name` .

For Config Custom Policy rules, this field will be ignored.

SourceDetails -> (list)

Provides the source and the message types that cause Config to evaluate your Amazon Web Services resources against a rule. It also provides the frequency with which you want Config to run evaluations for the rule if the trigger type is periodic.

If the owner is set to `CUSTOM_POLICY` , the only acceptable values for the Config rule trigger message type are `ConfigurationItemChangeNotification` and `OversizedConfigurationItemChangeNotification` .

(structure)

Provides the source and the message types that trigger Config to evaluate your Amazon Web Services resources against a rule. It also provides the frequency with which you want Config to run evaluations for the rule if the trigger type is periodic. You can specify the parameter values for `SourceDetail` only for custom rules.

EventSource -> (string)

The source of the event, such as an Amazon Web Services service, that triggers Config to evaluate your Amazon Web Services resources.

MessageType -> (string)

The type of notification that triggers Config to run an evaluation for a rule. You can specify the following notification types:

- `ConfigurationItemChangeNotification` - Triggers an evaluation when Config delivers a configuration item as a result of a resource change.
- `OversizedConfigurationItemChangeNotification` - Triggers an evaluation when Config delivers an oversized configuration item. Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
- `ScheduledNotification` - Triggers a periodic evaluation at the frequency specified for `MaximumExecutionFrequency` .
- `ConfigurationSnapshotDeliveryCompleted` - Triggers a periodic evaluation when Config delivers a configuration snapshot.

If you want your custom rule to be triggered by configuration changes, specify two SourceDetail objects, one for `ConfigurationItemChangeNotification` and one for `OversizedConfigurationItemChangeNotification` .

MaximumExecutionFrequency -> (string)

The frequency at which you want Config to run evaluations for a custom rule with a periodic trigger. If you specify a value for `MaximumExecutionFrequency` , then `MessageType` must use the `ScheduledNotification` value.

### Note

By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the `MaximumExecutionFrequency` parameter.

Based on the valid value you choose, Config runs evaluations once for each valid value. For example, if you choose `Three_Hours` , Config runs evaluations once every three hours. In this case, `Three_Hours` is the frequency of this rule.

CustomPolicyDetails -> (structure)

Provides the runtime system, policy definition, and whether debug logging is enabled. Required when owner is set to `CUSTOM_POLICY` .

PolicyRuntime -> (string)

The runtime system for your Config Custom Policy rule. Guard is a policy-as-code language that allows you to write policies that are enforced by Config Custom Policy rules. For more information about Guard, see the [Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard) .

PolicyText -> (string)

The policy definition containing the logic for your Config Custom Policy rule.

EnableDebugLogDelivery -> (boolean)

The boolean expression for enabling debug logging for your Config Custom Policy rule. The default value is `false` .

InputParameters -> (string)

A string, in JSON format, that is passed to the Config rule Lambda function.

MaximumExecutionFrequency -> (string)

The maximum frequency with which Config runs evaluations for a rule. You can specify a value for `MaximumExecutionFrequency` when:

- This is for an Config managed rule that is triggered at a periodic frequency.
- Your custom rule is triggered when Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties .

### Note

By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the `MaximumExecutionFrequency` parameter.

ConfigRuleState -> (string)

Indicates whether the Config rule is active or is currently being deleted by Config. It can also indicate the evaluation status for the Config rule.

Config sets the state of the rule to `EVALUATING` temporarily after you use the `StartConfigRulesEvaluation` request to evaluate your resources against the Config rule.

Config sets the state of the rule to `DELETING_RESULTS` temporarily after you use the `DeleteEvaluationResults` request to delete the current evaluation results for the Config rule.

Config temporarily sets the state of a rule to `DELETING` after you use the `DeleteConfigRule` request to delete the rule. After Config deletes the rule, the rule and all of its evaluations are erased and are no longer available.

CreatedBy -> (string)

Service principal name of the service that created the rule.

### Note

The field is populated only if the service-linked rule is created by a service. The field is empty if you create your own rule.

EvaluationModes -> (list)

The modes the Config rule can be evaluated in. The valid values are distinct objects. By default, the value is Detective evaluation mode only.

(structure)

The configuration object for Config rule evaluation mode. The supported valid values are Detective or Proactive.

Mode -> (string)

The mode of an evaluation. The valid values are Detective or Proactive.

NextToken -> (string)

The string that you use in a subsequent request to get the next page of results in a paginated response.