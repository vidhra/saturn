# describe-budget-performance-historyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget-performance-history.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget-performance-history.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [budgets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/index.html#cli-aws-budgets) ]

# describe-budget-performance-history

## Description

Describes the history for `DAILY` , `MONTHLY` , and `QUARTERLY` budgets. Budget history isnât available for `ANNUAL` budgets.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DescribeBudgetPerformanceHistory)

`describe-budget-performance-history` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `BudgetPerformanceHistory`

## Synopsis

```
describe-budget-performance-history
--account-id <value>
--budget-name <value>
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

`--time-period` (structure)

Retrieves how often the budget went into an `ALARM` state for the specified time period.

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

BudgetPerformanceHistory -> (structure)

The history of how often the budget has gone into an `ALARM` state.

For `DAILY` budgets, the history saves the state of the budget for the last 60 days. For `MONTHLY` budgets, the history saves the state of the budget for the current month plus the last 12 months. For `QUARTERLY` budgets, the history saves the state of the budget for the last four quarters.

BudgetName -> (string)

A string that represents the budget name. The â:â and â" characters, and the â/action/â substring, arenât allowed.

BudgetType -> (string)

The type of a budget. It must be one of the following types:

`COST` , `USAGE` , `RI_UTILIZATION` , `RI_COVERAGE` , `SAVINGS_PLANS_UTILIZATION` , or `SAVINGS_PLANS_COVERAGE` .

CostFilters -> (map)

The history of the cost filters for a budget during the specified time period.

key -> (string)

A generic string.

value -> (list)

(string)

CostTypes -> (structure)

The history of the cost types for a budget during the specified time period.

IncludeTax -> (boolean)

Specifies whether a budget includes taxes.

The default value is `true` .

IncludeSubscription -> (boolean)

Specifies whether a budget includes subscriptions.

The default value is `true` .

UseBlended -> (boolean)

Specifies whether a budget uses a blended rate.

The default value is `false` .

IncludeRefund -> (boolean)

Specifies whether a budget includes refunds.

The default value is `true` .

IncludeCredit -> (boolean)

Specifies whether a budget includes credits.

The default value is `true` .

IncludeUpfront -> (boolean)

Specifies whether a budget includes upfront RI costs.

The default value is `true` .

IncludeRecurring -> (boolean)

Specifies whether a budget includes recurring fees such as monthly RI fees.

The default value is `true` .

IncludeOtherSubscription -> (boolean)

Specifies whether a budget includes non-RI subscription costs.

The default value is `true` .

IncludeSupport -> (boolean)

Specifies whether a budget includes support subscription fees.

The default value is `true` .

IncludeDiscount -> (boolean)

Specifies whether a budget includes discounts.

The default value is `true` .

UseAmortized -> (boolean)

Specifies whether a budget uses the amortized rate.

The default value is `false` .

TimeUnit -> (string)

The time unit of the budget, such as MONTHLY or QUARTERLY.

BudgetedAndActualAmountsList -> (list)

A list of amounts of cost or usage that you created budgets for, which are compared to your actual costs or usage.

(structure)

The amount of cost or usage that you created the budget for, compared to your actual costs or usage.

BudgetedAmount -> (structure)

The amount of cost or usage that you created the budget for.

Amount -> (string)

The cost or usage amount thatâs associated with a budget forecast, actual spend, or budget threshold.

Unit -> (string)

The unit of measurement thatâs used for the budget forecast, actual spend, or budget threshold.

ActualAmount -> (structure)

Your actual costs or usage for a budget period.

Amount -> (string)

The cost or usage amount thatâs associated with a budget forecast, actual spend, or budget threshold.

Unit -> (string)

The unit of measurement thatâs used for the budget forecast, actual spend, or budget threshold.

TimePeriod -> (structure)

The time period thatâs covered by this budget comparison.

Start -> (timestamp)

The start date for a budget. If you created your budget and didnât specify a start date, Amazon Web Services defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose `DAILY` , and didnât set a start date, Amazon Web Services set your start date to `01/24/18 00:00 UTC` . If you chose `MONTHLY` , Amazon Web Services set your start date to `01/01/18 00:00 UTC` . The defaults are the same for the Billing and Cost Management console and the API.

You can change your start date with the `UpdateBudget` operation.

End -> (timestamp)

The end date for a budget. If you didnât specify an end date, Amazon Web Services set your end date to `06/15/87 00:00 UTC` . The defaults are the same for the Billing and Cost Management console and the API.

After the end date, Amazon Web Services deletes the budget and all the associated notifications and subscribers. You can change your end date with the `UpdateBudget` operation.

NextToken -> (string)

A generic string.