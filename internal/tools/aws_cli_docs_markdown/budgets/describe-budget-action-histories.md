# describe-budget-action-historiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget-action-histories.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget-action-histories.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [budgets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/index.html#cli-aws-budgets) ]

# describe-budget-action-histories

## Description

Describes a budget action history detail.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DescribeBudgetActionHistories)

`describe-budget-action-histories` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ActionHistories`

## Synopsis

```
describe-budget-action-histories
--account-id <value>
--budget-name <value>
--action-id <value>
[--time-period <value>]
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

`--account-id` (string)

The account ID of the user. Itâs a 12-digit number.

`--budget-name` (string)

A string that represents the budget name. The â:â and â" characters, and the â/action/â substring, arenât allowed.

`--action-id` (string)

A system-generated universally unique identifier (UUID) for the action.

`--time-period` (structure)

The period of time thatâs covered by a budget. The period has a start date and an end date. The start date must come before the end date. There are no restrictions on the end date.

Start -> (timestamp)

The start date for a budget. If you created your budget and didnât specify a start date, Amazon Web Services defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose `DAILY` , and didnât set a start date, Amazon Web Services set your start date to `01/24/18 00:00 UTC` . If you chose `MONTHLY` , Amazon Web Services set your start date to `01/01/18 00:00 UTC` . The defaults are the same for the Billing and Cost Management console and the API.

You can change your start date with the `UpdateBudget` operation.

End -> (timestamp)

The end date for a budget. If you didnât specify an end date, Amazon Web Services set your end date to `06/15/87 00:00 UTC` . The defaults are the same for the Billing and Cost Management console and the API.

After the end date, Amazon Web Services deletes the budget and all the associated notifications and subscribers. You can change your end date with the `UpdateBudget` operation.

Shorthand Syntax:

```
Start=timestamp,End=timestamp
```

JSON Syntax:

```
{
  "Start": timestamp,
  "End": timestamp
}
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

ActionHistories -> (list)

The historical record of the budget action resource.

(structure)

The historical records for a budget action.

Timestamp -> (timestamp)

A generic time stamp. In Java, itâs transformed to a `Date` object.

Status -> (string)

The status of action at the time of the event.

EventType -> (string)

This distinguishes between whether the events are triggered by the user or are generated by the system.

ActionHistoryDetails -> (structure)

The description of the details for the event.

Message -> (string)

A generic string.

Action -> (structure)

The budget action resource.

ActionId -> (string)

A system-generated universally unique identifier (UUID) for the action.

BudgetName -> (string)

A string that represents the budget name. The â:â and â" characters, and the â/action/â substring, arenât allowed.

NotificationType -> (string)

The type of a notification. It must be ACTUAL or FORECASTED.

ActionType -> (string)

The type of action. This defines the type of tasks that can be carried out by this action. This field also determines the format for definition.

ActionThreshold -> (structure)

The trigger threshold of the action.

ActionThresholdValue -> (double)

The threshold of a notification.

ActionThresholdType -> (string)

The type of threshold for a notification.

Definition -> (structure)

Where you specify all of the type-specific parameters.

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

ExecutionRoleArn -> (string)

The role passed for action execution and reversion. Roles and actions must be in the same account.

ApprovalModel -> (string)

This specifies if the action needs manual or automatic approval.

Status -> (string)

The status of the action.

Subscribers -> (list)

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

NextToken -> (string)

A generic string.