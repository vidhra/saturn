# create-budget-actionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-budget-action.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-budget-action.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [budgets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/index.html#cli-aws-budgets) ]

# create-budget-action

## Description

Creates a budget action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/CreateBudgetAction)

## Synopsis

```
create-budget-action
--account-id <value>
--budget-name <value>
--notification-type <value>
--action-type <value>
--action-threshold <value>
--definition <value>
--execution-role-arn <value>
--approval-model <value>
--subscribers <value>
[--resource-tags <value>]
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

`--account-id` (string)

The account ID of the user. Itâs a 12-digit number.

`--budget-name` (string)

A string that represents the budget name. The â:â and â" characters, and the â/action/â substring, arenât allowed.

`--notification-type` (string)

The type of a notification. It must be ACTUAL or FORECASTED.

Possible values:

- `ACTUAL`
- `FORECASTED`

`--action-type` (string)

The type of action. This defines the type of tasks that can be carried out by this action. This field also determines the format for definition.

Possible values:

- `APPLY_IAM_POLICY`
- `APPLY_SCP_POLICY`
- `RUN_SSM_DOCUMENTS`

`--action-threshold` (structure)

The trigger threshold of the action.

ActionThresholdValue -> (double)

The threshold of a notification.

ActionThresholdType -> (string)

The type of threshold for a notification.

Shorthand Syntax:

```
ActionThresholdValue=double,ActionThresholdType=string
```

JSON Syntax:

```
{
  "ActionThresholdValue": double,
  "ActionThresholdType": "PERCENTAGE"|"ABSOLUTE_VALUE"
}
```

`--definition` (structure)

Specifies all of the type-specific parameters.

IamActionDefinition -> (structure)

The Identity and Access Management (IAM) action definition details.

PolicyArn -> (string)

The Amazon Resource Name (ARN) of the policy to be attached.

Roles -> (list)

A list of roles to be attached. There must be at least one role.

(string)

Groups -> (list)

A list of groups to be attached. There must be at least one group.

(string)

Users -> (list)

A list of users to be attached. There must be at least one user.

(string)

ScpActionDefinition -> (structure)

The service control policies (SCPs) action definition details.

PolicyId -> (string)

The policy ID attached.

TargetIds -> (list)

A list of target IDs.

(string)

SsmActionDefinition -> (structure)

The Amazon Web Services Systems Manager (SSM) action definition details.

ActionSubType -> (string)

The action subType.

Region -> (string)

The Region to run the SSM document.

InstanceIds -> (list)

The EC2 and RDS instance IDs.

(string)

Shorthand Syntax:

```
IamActionDefinition={PolicyArn=string,Roles=[string,string],Groups=[string,string],Users=[string,string]},ScpActionDefinition={PolicyId=string,TargetIds=[string,string]},SsmActionDefinition={ActionSubType=string,Region=string,InstanceIds=[string,string]}
```

JSON Syntax:

```
{
  "IamActionDefinition": {
    "PolicyArn": "string",
    "Roles": ["string", ...],
    "Groups": ["string", ...],
    "Users": ["string", ...]
  },
  "ScpActionDefinition": {
    "PolicyId": "string",
    "TargetIds": ["string", ...]
  },
  "SsmActionDefinition": {
    "ActionSubType": "STOP_EC2_INSTANCES"|"STOP_RDS_INSTANCES",
    "Region": "string",
    "InstanceIds": ["string", ...]
  }
}
```

`--execution-role-arn` (string)

The role passed for action execution and reversion. Roles and actions must be in the same account.

`--approval-model` (string)

This specifies if the action needs manual or automatic approval.

Possible values:

- `AUTOMATIC`
- `MANUAL`

`--subscribers` (list)

A list of subscribers.

(structure)

The subscriber to a budget notification. The subscriber consists of a subscription type and either an Amazon SNS topic or an email address.

For example, an email subscriber has the following parameters:

- A `subscriptionType` of `EMAIL`
- An `address` of `example@example.com`

SubscriptionType -> (string)

The type of notification that Amazon Web Services sends to a subscriber.

Address -> (string)

The address that Amazon Web Services sends budget notifications to, either an SNS topic or an email.

When you create a subscriber, the value of `Address` canât contain line breaks.

Shorthand Syntax:

```
SubscriptionType=string,Address=string ...
```

JSON Syntax:

```
[
  {
    "SubscriptionType": "SNS"|"EMAIL",
    "Address": "string"
  }
  ...
]
```

`--resource-tags` (list)

An optional list of tags to associate with the specified budget action. Each tag consists of a key and a value, and each key must be unique for the resource.

(structure)

The tag structure that contains a tag key and value.

Key -> (string)

The key thatâs associated with the tag.

Value -> (string)

The value thatâs associated with the tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
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

AccountId -> (string)

The account ID of the user. Itâs a 12-digit number.

BudgetName -> (string)

A string that represents the budget name. The â:â and â" characters, and the â/action/â substring, arenât allowed.

ActionId -> (string)

A system-generated universally unique identifier (UUID) for the action.