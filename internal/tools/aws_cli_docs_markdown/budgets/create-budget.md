# create-budgetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-budget.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-budget.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [budgets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/index.html#cli-aws-budgets) ]

# create-budget

## Description

Creates a budget and, if included, notifications and subscribers.

### Warning

Only one of `BudgetLimit` or `PlannedBudgetLimits` can be present in the syntax at one time. Use the syntax that matches your use case. The Request Syntax section shows the `BudgetLimit` syntax. For `PlannedBudgetLimits` , see the [Examples](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CreateBudget.html#API_CreateBudget_Examples) section.

Similarly, only one set of filter and metric selections can be present in the syntax at one time. Either `FilterExpression` and `Metrics` or `CostFilters` and `CostTypes` , not both or a different combination. We recommend using `FilterExpression` and `Metrics` as they provide more flexible and powerful filtering capabilities. The Request Syntax section shows the `FilterExpression` /`Metrics` syntax.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/CreateBudget)

## Synopsis

```
create-budget
--account-id <value>
--budget <value>
[--notifications-with-subscribers <value>]
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

The `accountId` that is associated with the budget.

`--budget` (structure)

The budget object that you want to create.

BudgetName -> (string)

The name of a budget. The name must be unique within an account. The `:` and `\` characters, and the â/action/â substring, arenât allowed in `BudgetName` .

BudgetLimit -> (structure)

The total amount of cost, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage that you want to track with your budget.

`BudgetLimit` is required for cost or usage budgets, but optional for RI or Savings Plans utilization or coverage budgets. RI and Savings Plans utilization or coverage budgets default to `100` . This is the only valid value for RI or Savings Plans utilization or coverage budgets. You canât use `BudgetLimit` with `PlannedBudgetLimits` for `CreateBudget` and `UpdateBudget` actions.

Amount -> (string)

The cost or usage amount thatâs associated with a budget forecast, actual spend, or budget threshold.

Unit -> (string)

The unit of measurement thatâs used for the budget forecast, actual spend, or budget threshold.

PlannedBudgetLimits -> (map)

A map containing multiple `BudgetLimit` , including current or future limits.

`PlannedBudgetLimits` is available for cost or usage budget and supports both monthly and quarterly `TimeUnit` .

For monthly budgets, provide 12 months of `PlannedBudgetLimits` values. This must start from the current month and include the next 11 months. The `key` is the start of the month, `UTC` in epoch seconds.

For quarterly budgets, provide four quarters of `PlannedBudgetLimits` value entries in standard calendar quarter increments. This must start from the current quarter and include the next three quarters. The `key` is the start of the quarter, `UTC` in epoch seconds.

If the planned budget expires before 12 months for monthly or four quarters for quarterly, provide the `PlannedBudgetLimits` values only for the remaining periods.

If the budget begins at a date in the future, provide `PlannedBudgetLimits` values from the start date of the budget.

After all of the `BudgetLimit` values in `PlannedBudgetLimits` are used, the budget continues to use the last limit as the `BudgetLimit` . At that point, the planned budget provides the same experience as a fixed budget.

`DescribeBudget` and `DescribeBudgets` response along with `PlannedBudgetLimits` also contain `BudgetLimit` representing the current month or quarter limit present in `PlannedBudgetLimits` . This only applies to budgets that are created with `PlannedBudgetLimits` . Budgets that are created without `PlannedBudgetLimits` only contain `BudgetLimit` . They donât contain `PlannedBudgetLimits` .

key -> (string)

A generic string.

value -> (structure)

The amount of cost or usage thatâs measured for a budget.

*Cost example:* A `Spend` for `3 USD` of costs has the following parameters:

- An `Amount` of `3`
- A `Unit` of `USD`

*Usage example:* A `Spend` for `3 GB` of S3 usage has the following parameters:

- An `Amount` of `3`
- A `Unit` of `GB`

Amount -> (string)

The cost or usage amount thatâs associated with a budget forecast, actual spend, or budget threshold.

Unit -> (string)

The unit of measurement thatâs used for the budget forecast, actual spend, or budget threshold.

CostFilters -> (map)

The cost filters, such as `Region` , `Service` , `LinkedAccount` , `Tag` , or `CostCategory` , that are applied to a budget.

Amazon Web Services Budgets supports the following services as a `Service` filter for RI budgets:

- Amazon EC2
- Amazon Redshift
- Amazon Relational Database Service
- Amazon ElastiCache
- Amazon OpenSearch Service

key -> (string)

A generic string.

value -> (list)

(string)

CostTypes -> (structure)

The types of costs that are included in this `COST` budget.

`USAGE` , `RI_UTILIZATION` , `RI_COVERAGE` , `SAVINGS_PLANS_UTILIZATION` , and `SAVINGS_PLANS_COVERAGE` budgets do not have `CostTypes` .

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

The length of time until a budget resets the actual and forecasted spend.

TimePeriod -> (structure)

The period of time thatâs covered by a budget. You set the start date and end date. The start date must come before the end date. The end date must come before `06/15/87 00:00 UTC` .

If you create your budget and donât specify a start date, Amazon Web Services defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose `DAILY` , and didnât set a start date, Amazon Web Services set your start date to `01/24/18 00:00 UTC` . If you chose `MONTHLY` , Amazon Web Services set your start date to `01/01/18 00:00 UTC` . If you didnât specify an end date, Amazon Web Services set your end date to `06/15/87 00:00 UTC` . The defaults are the same for the Billing and Cost Management console and the API.

You can change either date with the `UpdateBudget` operation.

After the end date, Amazon Web Services deletes the budget and all the associated notifications and subscribers.

Start -> (timestamp)

The start date for a budget. If you created your budget and didnât specify a start date, Amazon Web Services defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose `DAILY` , and didnât set a start date, Amazon Web Services set your start date to `01/24/18 00:00 UTC` . If you chose `MONTHLY` , Amazon Web Services set your start date to `01/01/18 00:00 UTC` . The defaults are the same for the Billing and Cost Management console and the API.

You can change your start date with the `UpdateBudget` operation.

End -> (timestamp)

The end date for a budget. If you didnât specify an end date, Amazon Web Services set your end date to `06/15/87 00:00 UTC` . The defaults are the same for the Billing and Cost Management console and the API.

After the end date, Amazon Web Services deletes the budget and all the associated notifications and subscribers. You can change your end date with the `UpdateBudget` operation.

CalculatedSpend -> (structure)

The actual and forecasted cost or usage that the budget tracks.

ActualSpend -> (structure)

The amount of cost, usage, RI units, or Savings Plans units that you used.

Amount -> (string)

The cost or usage amount thatâs associated with a budget forecast, actual spend, or budget threshold.

Unit -> (string)

The unit of measurement thatâs used for the budget forecast, actual spend, or budget threshold.

ForecastedSpend -> (structure)

The amount of cost, usage, RI units, or Savings Plans units that youâre forecasted to use.

Amount -> (string)

The cost or usage amount thatâs associated with a budget forecast, actual spend, or budget threshold.

Unit -> (string)

The unit of measurement thatâs used for the budget forecast, actual spend, or budget threshold.

BudgetType -> (string)

Specifies whether this budget tracks costs, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage.

LastUpdatedTime -> (timestamp)

The last time that you updated this budget.

AutoAdjustData -> (structure)

The parameters that determine the budget amount for an auto-adjusting budget.

AutoAdjustType -> (string)

The string that defines whether your budget auto-adjusts based on historical or forecasted data.

HistoricalOptions -> (structure)

The parameters that define or describe the historical data that your auto-adjusting budget is based on.

BudgetAdjustmentPeriod -> (integer)

The number of budget periods included in the moving-average calculation that determines your auto-adjusted budget amount. The maximum value depends on the `TimeUnit` granularity of the budget:

- For the `DAILY` granularity, the maximum value is `60` .
- For the `MONTHLY` granularity, the maximum value is `12` .
- For the `QUARTERLY` granularity, the maximum value is `4` .
- For the `ANNUALLY` granularity, the maximum value is `1` .

LookBackAvailablePeriods -> (integer)

The integer that describes how many budget periods in your `BudgetAdjustmentPeriod` are included in the calculation of your current `BudgetLimit` . If the first budget period in your `BudgetAdjustmentPeriod` has no cost data, then that budget period isnât included in the average that determines your budget limit.

For example, if you set `BudgetAdjustmentPeriod` as `4` quarters, but your account had no cost data in the first quarter, then only the last three quarters are included in the calculation. In this scenario, `LookBackAvailablePeriods` returns `3` .

You canât set your own `LookBackAvailablePeriods` . The value is automatically calculated from the `BudgetAdjustmentPeriod` and your historical cost data.

LastAutoAdjustTime -> (timestamp)

The last time that your budget was auto-adjusted.

FilterExpression -> (structure)

The filtering dimensions for the budget and their corresponding values.

Or -> (list)

Return results that match either Dimension object.

(structure)

Use Expression to filter in various Budgets APIs.

Or -> (list)

Return results that match either Dimension object.

( â¦ recursive â¦ )

And -> (list)

Return results that match both Dimension objects.

( â¦ recursive â¦ )

( â¦ recursive â¦ )Dimensions -> (structure)

The specific Dimension to use for Expression.

Key -> (string)

The name of the dimension that you want to filter on.

Values -> (list)

The metadata values you can specify to filter upon, so that the results all match at least one of the specified values.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results. You can specify only one of these values in the array.

(string)

Tags -> (structure)

The specific Tag to use for Expression.

Key -> (string)

The key for the tag.

Values -> (list)

The specific value of the tag.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results.

(string)

CostCategories -> (structure)

The filter thatâs based on CostCategoryValues.

Key -> (string)

The unique name of the cost category.

Values -> (list)

The specific value of the cost category.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results.

(string)

And -> (list)

Return results that match both Dimension objects.

(structure)

Use Expression to filter in various Budgets APIs.

Or -> (list)

Return results that match either Dimension object.

( â¦ recursive â¦ )

And -> (list)

Return results that match both Dimension objects.

( â¦ recursive â¦ )

( â¦ recursive â¦ )Dimensions -> (structure)

The specific Dimension to use for Expression.

Key -> (string)

The name of the dimension that you want to filter on.

Values -> (list)

The metadata values you can specify to filter upon, so that the results all match at least one of the specified values.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results. You can specify only one of these values in the array.

(string)

Tags -> (structure)

The specific Tag to use for Expression.

Key -> (string)

The key for the tag.

Values -> (list)

The specific value of the tag.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results.

(string)

CostCategories -> (structure)

The filter thatâs based on CostCategoryValues.

Key -> (string)

The unique name of the cost category.

Values -> (list)

The specific value of the cost category.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results.

(string)

Not -> (structure)

Return results that donât match a Dimension object.

Or -> (list)

Return results that match either Dimension object.

( â¦ recursive â¦ )

And -> (list)

Return results that match both Dimension objects.

( â¦ recursive â¦ )

( â¦ recursive â¦ )Dimensions -> (structure)

The specific Dimension to use for Expression.

Key -> (string)

The name of the dimension that you want to filter on.

Values -> (list)

The metadata values you can specify to filter upon, so that the results all match at least one of the specified values.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results. You can specify only one of these values in the array.

(string)

Tags -> (structure)

The specific Tag to use for Expression.

Key -> (string)

The key for the tag.

Values -> (list)

The specific value of the tag.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results.

(string)

CostCategories -> (structure)

The filter thatâs based on CostCategoryValues.

Key -> (string)

The unique name of the cost category.

Values -> (list)

The specific value of the cost category.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results.

(string)

Dimensions -> (structure)

The specific Dimension to use for Expression.

Key -> (string)

The name of the dimension that you want to filter on.

Values -> (list)

The metadata values you can specify to filter upon, so that the results all match at least one of the specified values.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results. You can specify only one of these values in the array.

(string)

Tags -> (structure)

The specific Tag to use for Expression.

Key -> (string)

The key for the tag.

Values -> (list)

The specific value of the tag.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results.

(string)

CostCategories -> (structure)

The filter thatâs based on CostCategoryValues.

Key -> (string)

The unique name of the cost category.

Values -> (list)

The specific value of the cost category.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results.

(string)

Metrics -> (list)

The definition for how the budget data is aggregated.

(string)

JSON Syntax:

```
{
  "BudgetName": "string",
  "BudgetLimit": {
    "Amount": "string",
    "Unit": "string"
  },
  "PlannedBudgetLimits": {"string": {
        "Amount": "string",
        "Unit": "string"
      }
    ...},
  "CostFilters": {"string": ["string", ...]
    ...},
  "CostTypes": {
    "IncludeTax": true|false,
    "IncludeSubscription": true|false,
    "UseBlended": true|false,
    "IncludeRefund": true|false,
    "IncludeCredit": true|false,
    "IncludeUpfront": true|false,
    "IncludeRecurring": true|false,
    "IncludeOtherSubscription": true|false,
    "IncludeSupport": true|false,
    "IncludeDiscount": true|false,
    "UseAmortized": true|false
  },
  "TimeUnit": "DAILY"|"MONTHLY"|"QUARTERLY"|"ANNUALLY",
  "TimePeriod": {
    "Start": timestamp,
    "End": timestamp
  },
  "CalculatedSpend": {
    "ActualSpend": {
      "Amount": "string",
      "Unit": "string"
    },
    "ForecastedSpend": {
      "Amount": "string",
      "Unit": "string"
    }
  },
  "BudgetType": "USAGE"|"COST"|"RI_UTILIZATION"|"RI_COVERAGE"|"SAVINGS_PLANS_UTILIZATION"|"SAVINGS_PLANS_COVERAGE",
  "LastUpdatedTime": timestamp,
  "AutoAdjustData": {
    "AutoAdjustType": "HISTORICAL"|"FORECAST",
    "HistoricalOptions": {
      "BudgetAdjustmentPeriod": integer,
      "LookBackAvailablePeriods": integer
    },
    "LastAutoAdjustTime": timestamp
  },
  "FilterExpression": {
    "Or": [
      {
        "Or": [
          { ... recursive ... }
          ...
        ],
        "And": [
          { ... recursive ... }
          ...
        ],
        "Not": { ... recursive ... },
        "Dimensions": {
          "Key": "AZ"|"INSTANCE_TYPE"|"LINKED_ACCOUNT"|"LINKED_ACCOUNT_NAME"|"OPERATION"|"PURCHASE_TYPE"|"REGION"|"SERVICE"|"SERVICE_CODE"|"USAGE_TYPE"|"USAGE_TYPE_GROUP"|"RECORD_TYPE"|"OPERATING_SYSTEM"|"TENANCY"|"SCOPE"|"PLATFORM"|"SUBSCRIPTION_ID"|"LEGAL_ENTITY_NAME"|"INVOICING_ENTITY"|"DEPLOYMENT_OPTION"|"DATABASE_ENGINE"|"CACHE_ENGINE"|"INSTANCE_TYPE_FAMILY"|"BILLING_ENTITY"|"RESERVATION_ID"|"RESOURCE_ID"|"RIGHTSIZING_TYPE"|"SAVINGS_PLANS_TYPE"|"SAVINGS_PLAN_ARN"|"PAYMENT_OPTION"|"RESERVATION_MODIFIED"|"TAG_KEY"|"COST_CATEGORY_NAME",
          "Values": ["string", ...],
          "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"GREATER_THAN_OR_EQUAL"|"CASE_SENSITIVE"|"CASE_INSENSITIVE", ...]
        },
        "Tags": {
          "Key": "string",
          "Values": ["string", ...],
          "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"GREATER_THAN_OR_EQUAL"|"CASE_SENSITIVE"|"CASE_INSENSITIVE", ...]
        },
        "CostCategories": {
          "Key": "string",
          "Values": ["string", ...],
          "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"GREATER_THAN_OR_EQUAL"|"CASE_SENSITIVE"|"CASE_INSENSITIVE", ...]
        }
      }
      ...
    ],
    "And": [
      {
        "Or": [
          { ... recursive ... }
          ...
        ],
        "And": [
          { ... recursive ... }
          ...
        ],
        "Not": { ... recursive ... },
        "Dimensions": {
          "Key": "AZ"|"INSTANCE_TYPE"|"LINKED_ACCOUNT"|"LINKED_ACCOUNT_NAME"|"OPERATION"|"PURCHASE_TYPE"|"REGION"|"SERVICE"|"SERVICE_CODE"|"USAGE_TYPE"|"USAGE_TYPE_GROUP"|"RECORD_TYPE"|"OPERATING_SYSTEM"|"TENANCY"|"SCOPE"|"PLATFORM"|"SUBSCRIPTION_ID"|"LEGAL_ENTITY_NAME"|"INVOICING_ENTITY"|"DEPLOYMENT_OPTION"|"DATABASE_ENGINE"|"CACHE_ENGINE"|"INSTANCE_TYPE_FAMILY"|"BILLING_ENTITY"|"RESERVATION_ID"|"RESOURCE_ID"|"RIGHTSIZING_TYPE"|"SAVINGS_PLANS_TYPE"|"SAVINGS_PLAN_ARN"|"PAYMENT_OPTION"|"RESERVATION_MODIFIED"|"TAG_KEY"|"COST_CATEGORY_NAME",
          "Values": ["string", ...],
          "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"GREATER_THAN_OR_EQUAL"|"CASE_SENSITIVE"|"CASE_INSENSITIVE", ...]
        },
        "Tags": {
          "Key": "string",
          "Values": ["string", ...],
          "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"GREATER_THAN_OR_EQUAL"|"CASE_SENSITIVE"|"CASE_INSENSITIVE", ...]
        },
        "CostCategories": {
          "Key": "string",
          "Values": ["string", ...],
          "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"GREATER_THAN_OR_EQUAL"|"CASE_SENSITIVE"|"CASE_INSENSITIVE", ...]
        }
      }
      ...
    ],
    "Not": {
      "Or": [
        { ... recursive ... }
        ...
      ],
      "And": [
        { ... recursive ... }
        ...
      ],
      "Not": { ... recursive ... },
      "Dimensions": {
        "Key": "AZ"|"INSTANCE_TYPE"|"LINKED_ACCOUNT"|"LINKED_ACCOUNT_NAME"|"OPERATION"|"PURCHASE_TYPE"|"REGION"|"SERVICE"|"SERVICE_CODE"|"USAGE_TYPE"|"USAGE_TYPE_GROUP"|"RECORD_TYPE"|"OPERATING_SYSTEM"|"TENANCY"|"SCOPE"|"PLATFORM"|"SUBSCRIPTION_ID"|"LEGAL_ENTITY_NAME"|"INVOICING_ENTITY"|"DEPLOYMENT_OPTION"|"DATABASE_ENGINE"|"CACHE_ENGINE"|"INSTANCE_TYPE_FAMILY"|"BILLING_ENTITY"|"RESERVATION_ID"|"RESOURCE_ID"|"RIGHTSIZING_TYPE"|"SAVINGS_PLANS_TYPE"|"SAVINGS_PLAN_ARN"|"PAYMENT_OPTION"|"RESERVATION_MODIFIED"|"TAG_KEY"|"COST_CATEGORY_NAME",
        "Values": ["string", ...],
        "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"GREATER_THAN_OR_EQUAL"|"CASE_SENSITIVE"|"CASE_INSENSITIVE", ...]
      },
      "Tags": {
        "Key": "string",
        "Values": ["string", ...],
        "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"GREATER_THAN_OR_EQUAL"|"CASE_SENSITIVE"|"CASE_INSENSITIVE", ...]
      },
      "CostCategories": {
        "Key": "string",
        "Values": ["string", ...],
        "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"GREATER_THAN_OR_EQUAL"|"CASE_SENSITIVE"|"CASE_INSENSITIVE", ...]
      }
    },
    "Dimensions": {
      "Key": "AZ"|"INSTANCE_TYPE"|"LINKED_ACCOUNT"|"LINKED_ACCOUNT_NAME"|"OPERATION"|"PURCHASE_TYPE"|"REGION"|"SERVICE"|"SERVICE_CODE"|"USAGE_TYPE"|"USAGE_TYPE_GROUP"|"RECORD_TYPE"|"OPERATING_SYSTEM"|"TENANCY"|"SCOPE"|"PLATFORM"|"SUBSCRIPTION_ID"|"LEGAL_ENTITY_NAME"|"INVOICING_ENTITY"|"DEPLOYMENT_OPTION"|"DATABASE_ENGINE"|"CACHE_ENGINE"|"INSTANCE_TYPE_FAMILY"|"BILLING_ENTITY"|"RESERVATION_ID"|"RESOURCE_ID"|"RIGHTSIZING_TYPE"|"SAVINGS_PLANS_TYPE"|"SAVINGS_PLAN_ARN"|"PAYMENT_OPTION"|"RESERVATION_MODIFIED"|"TAG_KEY"|"COST_CATEGORY_NAME",
      "Values": ["string", ...],
      "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"GREATER_THAN_OR_EQUAL"|"CASE_SENSITIVE"|"CASE_INSENSITIVE", ...]
    },
    "Tags": {
      "Key": "string",
      "Values": ["string", ...],
      "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"GREATER_THAN_OR_EQUAL"|"CASE_SENSITIVE"|"CASE_INSENSITIVE", ...]
    },
    "CostCategories": {
      "Key": "string",
      "Values": ["string", ...],
      "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"GREATER_THAN_OR_EQUAL"|"CASE_SENSITIVE"|"CASE_INSENSITIVE", ...]
    }
  },
  "Metrics": ["BlendedCost"|"UnblendedCost"|"AmortizedCost"|"NetUnblendedCost"|"NetAmortizedCost"|"UsageQuantity"|"NormalizedUsageAmount"|"Hours", ...]
}
```

`--notifications-with-subscribers` (list)

A notification that you want to associate with a budget. A budget can have up to five notifications, and each notification can have one SNS subscriber and up to 10 email subscribers. If you include notifications and subscribers in your `CreateBudget` call, Amazon Web Services creates the notifications and subscribers for you.

(structure)

A notification with subscribers. A notification can have one SNS subscriber and up to 10 email subscribers, for a total of 11 subscribers.

Notification -> (structure)

The notification thatâs associated with a budget.

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

Subscribers -> (list)

A list of subscribers who are subscribed to this notification.

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
Notification={NotificationType=string,ComparisonOperator=string,Threshold=double,ThresholdType=string,NotificationState=string},Subscribers=[{SubscriptionType=string,Address=string},{SubscriptionType=string,Address=string}] ...
```

JSON Syntax:

```
[
  {
    "Notification": {
      "NotificationType": "ACTUAL"|"FORECASTED",
      "ComparisonOperator": "GREATER_THAN"|"LESS_THAN"|"EQUAL_TO",
      "Threshold": double,
      "ThresholdType": "PERCENTAGE"|"ABSOLUTE_VALUE",
      "NotificationState": "OK"|"ALARM"
    },
    "Subscribers": [
      {
        "SubscriptionType": "SNS"|"EMAIL",
        "Address": "string"
      }
      ...
    ]
  }
  ...
]
```

`--resource-tags` (list)

An optional list of tags to associate with the specified budget. Each tag consists of a key and a value, and each key must be unique for the resource.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a Cost and Usage budget**

The following `create-budget` command creates a Cost and Usage budget.

```
aws budgets create-budget \
    --account-id 111122223333 \
    --budget file://budget.json \
    --notifications-with-subscribers file://notifications-with-subscribers.json
```

Contents of `budget.json`:

```
{
    "BudgetLimit": {
        "Amount": "100",
        "Unit": "USD"
    },
    "BudgetName": "Example Tag Budget",
    "BudgetType": "COST",
    "CostFilters": {
        "TagKeyValue": [
            "user:Key$value1",
            "user:Key$value2"
        ]
    },
    "CostTypes": {
        "IncludeCredit": true,
        "IncludeDiscount": true,
        "IncludeOtherSubscription": true,
        "IncludeRecurring": true,
        "IncludeRefund": true,
        "IncludeSubscription": true,
        "IncludeSupport": true,
        "IncludeTax": true,
        "IncludeUpfront": true,
        "UseBlended": false
    },
    "TimePeriod": {
        "Start": 1477958399,
        "End": 3706473600
    },
    "TimeUnit": "MONTHLY"
}
```

Contents of `notifications-with-subscribers.json`:

```
[
    {
        "Notification": {
            "ComparisonOperator": "GREATER_THAN",
            "NotificationType": "ACTUAL",
            "Threshold": 80,
            "ThresholdType": "PERCENTAGE"
        },
        "Subscribers": [
            {
                "Address": "example@example.com",
                "SubscriptionType": "EMAIL"
            }
        ]
    }
]
```

## Output

None