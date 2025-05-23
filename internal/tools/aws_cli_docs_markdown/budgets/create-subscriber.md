# create-subscriberÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-subscriber.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-subscriber.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [budgets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/index.html#cli-aws-budgets) ]

# create-subscriber

## Description

Creates a subscriber. You must create the associated budget and notification before you create the subscriber.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/CreateSubscriber)

## Synopsis

```
create-subscriber
--account-id <value>
--budget-name <value>
--notification <value>
--subscriber <value>
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

The `accountId` that is associated with the budget that you want to create a subscriber for.

`--budget-name` (string)

The name of the budget that you want to subscribe to. Budget names must be unique within an account.

`--notification` (structure)

The notification that you want to create a subscriber for.

NotificationType -> (string)

Specifies whether the notification is for how much you have spent (`ACTUAL` ) or for how much that youâre forecasted to spend (`FORECASTED` ).

ComparisonOperator -> (string)

The comparison thatâs used for this notification.

Threshold -> (double)

The threshold thatâs associated with a notification. Thresholds are always a percentage, and many customers find value being alerted between 50% - 200% of the budgeted amount. The maximum limit for your threshold is 1,000,000% above the budgeted amount.

ThresholdType -> (string)

The type of threshold for a notification. For `ABSOLUTE_VALUE` thresholds, Amazon Web Services notifies you when you go over or are forecasted to go over your total cost threshold. For `PERCENTAGE` thresholds, Amazon Web Services notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a `PERCENTAGE` threshold of 80%, Amazon Web Services notifies you when you go over 160 dollars.

NotificationState -> (string)

Specifies whether this notification is in alarm. If a budget notification is in the `ALARM` state, you passed the set threshold for the budget.

Shorthand Syntax:

```
NotificationType=string,ComparisonOperator=string,Threshold=double,ThresholdType=string,NotificationState=string
```

JSON Syntax:

```
{
  "NotificationType": "ACTUAL"|"FORECASTED",
  "ComparisonOperator": "GREATER_THAN"|"LESS_THAN"|"EQUAL_TO",
  "Threshold": double,
  "ThresholdType": "PERCENTAGE"|"ABSOLUTE_VALUE",
  "NotificationState": "OK"|"ALARM"
}
```

`--subscriber` (structure)

The subscriber that you want to associate with a budget notification.

SubscriptionType -> (string)

The type of notification that Amazon Web Services sends to a subscriber.

Address -> (string)

The address that Amazon Web Services sends budget notifications to, either an SNS topic or an email.

When you create a subscriber, the value of `Address` canât contain line breaks.

Shorthand Syntax:

```
SubscriptionType=string,Address=string
```

JSON Syntax:

```
{
  "SubscriptionType": "SNS"|"EMAIL",
  "Address": "string"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a subscriber for a notification associated with a Cost and Usage budget**

This example creates a subscriber for the specified notification.

Command:

```
aws budgets create-subscriber --account-id 111122223333 --budget-name "Example Budget" --notification NotificationType=ACTUAL,ComparisonOperator=GREATER_THAN,Threshold=80,ThresholdType=PERCENTAGE --subscriber SubscriptionType=EMAIL,Address=example@example.com
```

## Output

None