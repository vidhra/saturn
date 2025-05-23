# update-safety-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53-recovery-control-config/update-safety-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53-recovery-control-config/update-safety-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53-recovery-control-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53-recovery-control-config/index.html#cli-aws-route53-recovery-control-config) ]

# update-safety-rule

## Description

Update a safety rule (an assertion rule or gating rule). You can only update the name and the waiting period for a safety rule. To make other updates, delete the safety rule and create a new one.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-recovery-control-config-2020-11-02/UpdateSafetyRule)

## Synopsis

```
update-safety-rule
[--assertion-rule-update <value>]
[--gating-rule-update <value>]
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

`--assertion-rule-update` (structure)

The assertion rule to update.

Name -> (string)

The name of the assertion rule. You can use any non-white space character in the name.

SafetyRuleArn -> (string)

The Amazon Resource Name (ARN) of the assertion rule.

WaitPeriodMs -> (integer)

An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent âflappingâ of state. The wait period is 5000 ms by default, but you can choose a custom value.

Shorthand Syntax:

```
Name=string,SafetyRuleArn=string,WaitPeriodMs=integer
```

JSON Syntax:

```
{
  "Name": "string",
  "SafetyRuleArn": "string",
  "WaitPeriodMs": integer
}
```

`--gating-rule-update` (structure)

The gating rule to update.

Name -> (string)

The name for the gating rule. You can use any non-white space character in the name.

SafetyRuleArn -> (string)

The Amazon Resource Name (ARN) of the gating rule.

WaitPeriodMs -> (integer)

An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent âflappingâ of state. The wait period is 5000 ms by default, but you can choose a custom value.

Shorthand Syntax:

```
Name=string,SafetyRuleArn=string,WaitPeriodMs=integer
```

JSON Syntax:

```
{
  "Name": "string",
  "SafetyRuleArn": "string",
  "WaitPeriodMs": integer
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

AssertionRule -> (structure)

The assertion rule updated.

AssertedControls -> (list)

The routing controls that are part of transactions that are evaluated to determine if a request to change a routing control state is allowed. For example, you might include three routing controls, one for each of three Amazon Web Services Regions.

(string)

ControlPanelArn -> (string)

The Amazon Resource Name (ARN) of the control panel.

Name -> (string)

Name of the assertion rule. You can use any non-white space character in the name.

RuleConfig -> (structure)

The criteria that you set for specific assertion routing controls (AssertedControls) that designate how many routing control states must be ON as the result of a transaction. For example, if you have three assertion routing controls, you might specify ATLEAST 2 for your rule configuration. This means that at least two assertion routing control states must be ON, so that at least two Amazon Web Services Regions have traffic flowing to them.

Inverted -> (boolean)

Logical negation of the rule. If the rule would usually evaluate true, itâs evaluated as false, and vice versa.

Threshold -> (integer)

The value of N, when you specify an ATLEAST rule type. That is, Threshold is the number of controls that must be set when you specify an ATLEAST type.

Type -> (string)

A rule can be one of the following: ATLEAST, AND, or OR.

SafetyRuleArn -> (string)

The Amazon Resource Name (ARN) of the assertion rule.

Status -> (string)

The deployment status of an assertion rule. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.

WaitPeriodMs -> (integer)

An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent âflappingâ of state. The wait period is 5000 ms by default, but you can choose a custom value.

Owner -> (string)

The Amazon Web Services account ID of the assertion rule owner.

GatingRule -> (structure)

The gating rule updated.

ControlPanelArn -> (string)

The Amazon Resource Name (ARN) of the control panel.

GatingControls -> (list)

An array of gating routing control Amazon Resource Names (ARNs). For a simple âon/offâ switch, specify the ARN for one routing control. The gating routing controls are evaluated by the rule configuration that you specify to determine if the target routing control states can be changed.

(string)

Name -> (string)

The name for the gating rule. You can use any non-white space character in the name.

RuleConfig -> (structure)

The criteria that you set for gating routing controls that designate how many of the routing control states must be ON to allow you to update target routing control states.

Inverted -> (boolean)

Logical negation of the rule. If the rule would usually evaluate true, itâs evaluated as false, and vice versa.

Threshold -> (integer)

The value of N, when you specify an ATLEAST rule type. That is, Threshold is the number of controls that must be set when you specify an ATLEAST type.

Type -> (string)

A rule can be one of the following: ATLEAST, AND, or OR.

SafetyRuleArn -> (string)

The Amazon Resource Name (ARN) of the gating rule.

Status -> (string)

The deployment status of a gating rule. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.

TargetControls -> (list)

An array of target routing control Amazon Resource Names (ARNs) for which the states can only be updated if the rule configuration that you specify evaluates to true for the gating routing control. As a simple example, if you have a single gating control, it acts as an overall âon/offâ switch for a set of target routing controls. You can use this to manually override automated failover, for example.

(string)

WaitPeriodMs -> (integer)

An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent âflappingâ of state. The wait period is 5000 ms by default, but you can choose a custom value.

Owner -> (string)

The Amazon Web Services account ID of the gating rule owner.