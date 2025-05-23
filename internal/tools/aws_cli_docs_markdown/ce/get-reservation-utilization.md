# get-reservation-utilizationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-reservation-utilization.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-reservation-utilization.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ce](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html#cli-aws-ce) ]

# get-reservation-utilization

## Description

Retrieves the reservation utilization for your account. Management account in an organization have access to member accounts. You can filter data by dimensions in a time period. You can use `GetDimensionValues` to determine the possible dimension values. Currently, you can group only by `SUBSCRIPTION_ID` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetReservationUtilization)

## Synopsis

```
get-reservation-utilization
--time-period <value>
[--group-by <value>]
[--granularity <value>]
[--filter <value>]
[--sort-by <value>]
[--next-page-token <value>]
[--max-results <value>]
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

`--time-period` (structure)

Sets the start and end dates for retrieving Reserved Instance (RI) utilization. The start date is inclusive, but the end date is exclusive. For example, if `start` is `2017-01-01` and `end` is `2017-05-01` , then the cost and usage data is retrieved from `2017-01-01` up to and including `2017-04-30` but not including `2017-05-01` .

Start -> (string)

The beginning of the time period. The start date is inclusive. For example, if `start` is `2017-01-01` , Amazon Web Services retrieves cost and usage data starting at `2017-01-01` up to the end date. The start date must be equal to or no later than the current date to avoid a validation error.

End -> (string)

The end of the time period. The end date is exclusive. For example, if `end` is `2017-05-01` , Amazon Web Services retrieves cost and usage data from the start date up to, but not including, `2017-05-01` .

Shorthand Syntax:

```
Start=string,End=string
```

JSON Syntax:

```
{
  "Start": "string",
  "End": "string"
}
```

`--group-by` (list)

Groups only by `SUBSCRIPTION_ID` . Metadata is included.

(structure)

Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.

Type -> (string)

The string that represents the type of group.

Key -> (string)

The string that represents a key for a specified group.

Shorthand Syntax:

```
Type=string,Key=string ...
```

JSON Syntax:

```
[
  {
    "Type": "DIMENSION"|"TAG"|"COST_CATEGORY",
    "Key": "string"
  }
  ...
]
```

`--granularity` (string)

If `GroupBy` is set, `Granularity` canât be set. If `Granularity` isnât set, the response object doesnât include `Granularity` , either `MONTHLY` or `DAILY` . If both `GroupBy` and `Granularity` arenât set, `GetReservationUtilization` defaults to `DAILY` .

The `GetReservationUtilization` operation supports only `DAILY` and `MONTHLY` granularities.

Possible values:

- `DAILY`
- `MONTHLY`
- `HOURLY`

`--filter` (structure)

Filters utilization data by dimensions. You can filter by the following dimensions:

- AZ
- CACHE_ENGINE
- DEPLOYMENT_OPTION
- INSTANCE_TYPE
- LINKED_ACCOUNT
- OPERATING_SYSTEM
- PLATFORM
- REGION
- SERVICE

### Note

If not specified, the `SERVICE` filter defaults to Amazon Elastic Compute Cloud - Compute. Supported values for `SERVICE` are Amazon Elastic Compute Cloud - Compute, Amazon Relational Database Service, Amazon ElastiCache, Amazon Redshift, and Amazon Elasticsearch Service. The value for the `SERVICE` filter should not exceed â1â.

- SCOPE
- TENANCY

`GetReservationUtilization` uses the same [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html) object as the other operations, but only `AND` is supported among each dimension, and nesting is supported up to only one level deep. If there are multiple values for a dimension, they are ORâd together.

Or -> (list)

Return results that match either `Dimension` object.

(structure)

Use `Expression` to filter in various Cost Explorer APIs.

Not all `Expression` types are supported in each API. Refer to the documentation for each specific API to see what is supported.

There are two patterns:

- Simple dimension values.
- There are three types of simple dimension values: `CostCategories` , `Tags` , and `Dimensions` .
- Specify the `CostCategories` field to define a filter that acts on Cost Categories.
- Specify the `Tags` field to define a filter that acts on Cost Allocation Tags.
- Specify the `Dimensions` field to define a filter that acts on the ` `DimensionValues` [https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DimensionValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DimensionValues).html`__ .
- For each filter type, you can set the dimension name and values for the filters that you plan to use.
- For example, you can filter for `REGION==us-east-1 OR REGION==us-west-1` . For `GetRightsizingRecommendation` , the Region is a full name (for example, `REGION==US East (N. Virginia)` .
- The corresponding `Expression` for this example is as follows: `{ "Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] } }`
- As shown in the previous example, lists of dimension values are combined with `OR` when applying the filter.
- You can also set different match options to further control how the filter behaves. Not all APIs support match options. Refer to the documentation for each specific API to see what is supported.
- For example, you can filter for linked account names that start with âaâ.
- The corresponding `Expression` for this example is as follows: `{ "Dimensions": { "Key": "LINKED_ACCOUNT_NAME", "MatchOptions": [ "STARTS_WITH" ], "Values": [ "a" ] } }`
- Compound `Expression` types with logical operations.
- You can use multiple `Expression` types and the logical operators `AND/OR/NOT` to create a list of one or more `Expression` objects. By doing this, you can filter by more advanced options.
- For example, you can filter by `((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer)` .
- The corresponding `Expression` for this example is as follows: `{ "And": [ {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }`

### Note

Because each `Expression` can have only one operator, the service returns an error if more than one is specified. The following example shows an `Expression` object that creates an error: `{ "And": [ ... ], "Dimensions": { "Key": "USAGE_TYPE", "Values": [ "DataTransfer" ] } }`

The following is an example of the corresponding error message: `"Expression has more than one roots. Only one root operator is allowed for each expression: And, Or, Not, Dimensions, Tags, CostCategories"`

### Note

For the `GetRightsizingRecommendation` action, a combination of OR and NOT isnât supported. OR isnât supported between different dimensions, or dimensions and tags. NOT operators arenât supported. Dimensions are also limited to `LINKED_ACCOUNT` , `REGION` , or `RIGHTSIZING_TYPE` .

For the `GetReservationPurchaseRecommendation` action, only NOT is supported. AND and OR arenât supported. Dimensions are limited to `LINKED_ACCOUNT` .

Or -> (list)

Return results that match either `Dimension` object.

( â¦ recursive â¦ )

And -> (list)

Return results that match both `Dimension` objects.

( â¦ recursive â¦ )

( â¦ recursive â¦ )Dimensions -> (structure)

The specific `Dimension` to use for `Expression` .

Key -> (string)

The names of the metadata types that you can use to filter and group your results. For example, `AZ` returns a list of Availability Zones.

Not all dimensions are supported in each API. Refer to the documentation for each specific API to see what is supported.

`LINKED_ACCOUNT_NAME` and `SERVICE_CODE` can only be used in [CostCategoryRule](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryRule.html) .

`ANOMALY_TOTAL_IMPACT_ABSOLUTE` and `ANOMALY_TOTAL_IMPACT_PERCENTAGE` can only be used in [AnomalySubscriptions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html) .

Values -> (list)

The metadata values that you can use to filter and group your results. You can use `GetDimensionValues` to find specific values.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results.

`MatchOptions` is only applicable for actions related to Cost Category and Anomaly Subscriptions. Refer to the documentation for each specific API to see what is supported.

The default values for `MatchOptions` are `EQUALS` and `CASE_SENSITIVE` .

(string)

Tags -> (structure)

The specific `Tag` to use for `Expression` .

Key -> (string)

The key for the tag.

Values -> (list)

The specific value of the tag.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results. `MatchOptions` is only applicable for actions related to Cost Category. The default values for `MatchOptions` are `EQUALS` and `CASE_SENSITIVE` .

(string)

CostCategories -> (structure)

The filter thatâs based on `CostCategory` values.

Key -> (string)

The unique name of the Cost Category.

Values -> (list)

The specific value of the Cost Category.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for actions related to cost category. The default values for `MatchOptions` is `EQUALS` and `CASE_SENSITIVE` .

(string)

And -> (list)

Return results that match both `Dimension` objects.

(structure)

Use `Expression` to filter in various Cost Explorer APIs.

Not all `Expression` types are supported in each API. Refer to the documentation for each specific API to see what is supported.

There are two patterns:

- Simple dimension values.
- There are three types of simple dimension values: `CostCategories` , `Tags` , and `Dimensions` .
- Specify the `CostCategories` field to define a filter that acts on Cost Categories.
- Specify the `Tags` field to define a filter that acts on Cost Allocation Tags.
- Specify the `Dimensions` field to define a filter that acts on the ` `DimensionValues` [https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DimensionValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DimensionValues).html`__ .
- For each filter type, you can set the dimension name and values for the filters that you plan to use.
- For example, you can filter for `REGION==us-east-1 OR REGION==us-west-1` . For `GetRightsizingRecommendation` , the Region is a full name (for example, `REGION==US East (N. Virginia)` .
- The corresponding `Expression` for this example is as follows: `{ "Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] } }`
- As shown in the previous example, lists of dimension values are combined with `OR` when applying the filter.
- You can also set different match options to further control how the filter behaves. Not all APIs support match options. Refer to the documentation for each specific API to see what is supported.
- For example, you can filter for linked account names that start with âaâ.
- The corresponding `Expression` for this example is as follows: `{ "Dimensions": { "Key": "LINKED_ACCOUNT_NAME", "MatchOptions": [ "STARTS_WITH" ], "Values": [ "a" ] } }`
- Compound `Expression` types with logical operations.
- You can use multiple `Expression` types and the logical operators `AND/OR/NOT` to create a list of one or more `Expression` objects. By doing this, you can filter by more advanced options.
- For example, you can filter by `((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer)` .
- The corresponding `Expression` for this example is as follows: `{ "And": [ {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }`

### Note

Because each `Expression` can have only one operator, the service returns an error if more than one is specified. The following example shows an `Expression` object that creates an error: `{ "And": [ ... ], "Dimensions": { "Key": "USAGE_TYPE", "Values": [ "DataTransfer" ] } }`

The following is an example of the corresponding error message: `"Expression has more than one roots. Only one root operator is allowed for each expression: And, Or, Not, Dimensions, Tags, CostCategories"`

### Note

For the `GetRightsizingRecommendation` action, a combination of OR and NOT isnât supported. OR isnât supported between different dimensions, or dimensions and tags. NOT operators arenât supported. Dimensions are also limited to `LINKED_ACCOUNT` , `REGION` , or `RIGHTSIZING_TYPE` .

For the `GetReservationPurchaseRecommendation` action, only NOT is supported. AND and OR arenât supported. Dimensions are limited to `LINKED_ACCOUNT` .

Or -> (list)

Return results that match either `Dimension` object.

( â¦ recursive â¦ )

And -> (list)

Return results that match both `Dimension` objects.

( â¦ recursive â¦ )

( â¦ recursive â¦ )Dimensions -> (structure)

The specific `Dimension` to use for `Expression` .

Key -> (string)

The names of the metadata types that you can use to filter and group your results. For example, `AZ` returns a list of Availability Zones.

Not all dimensions are supported in each API. Refer to the documentation for each specific API to see what is supported.

`LINKED_ACCOUNT_NAME` and `SERVICE_CODE` can only be used in [CostCategoryRule](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryRule.html) .

`ANOMALY_TOTAL_IMPACT_ABSOLUTE` and `ANOMALY_TOTAL_IMPACT_PERCENTAGE` can only be used in [AnomalySubscriptions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html) .

Values -> (list)

The metadata values that you can use to filter and group your results. You can use `GetDimensionValues` to find specific values.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results.

`MatchOptions` is only applicable for actions related to Cost Category and Anomaly Subscriptions. Refer to the documentation for each specific API to see what is supported.

The default values for `MatchOptions` are `EQUALS` and `CASE_SENSITIVE` .

(string)

Tags -> (structure)

The specific `Tag` to use for `Expression` .

Key -> (string)

The key for the tag.

Values -> (list)

The specific value of the tag.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results. `MatchOptions` is only applicable for actions related to Cost Category. The default values for `MatchOptions` are `EQUALS` and `CASE_SENSITIVE` .

(string)

CostCategories -> (structure)

The filter thatâs based on `CostCategory` values.

Key -> (string)

The unique name of the Cost Category.

Values -> (list)

The specific value of the Cost Category.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for actions related to cost category. The default values for `MatchOptions` is `EQUALS` and `CASE_SENSITIVE` .

(string)

Not -> (structure)

Return results that donât match a `Dimension` object.

Or -> (list)

Return results that match either `Dimension` object.

( â¦ recursive â¦ )

And -> (list)

Return results that match both `Dimension` objects.

( â¦ recursive â¦ )

( â¦ recursive â¦ )Dimensions -> (structure)

The specific `Dimension` to use for `Expression` .

Key -> (string)

The names of the metadata types that you can use to filter and group your results. For example, `AZ` returns a list of Availability Zones.

Not all dimensions are supported in each API. Refer to the documentation for each specific API to see what is supported.

`LINKED_ACCOUNT_NAME` and `SERVICE_CODE` can only be used in [CostCategoryRule](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryRule.html) .

`ANOMALY_TOTAL_IMPACT_ABSOLUTE` and `ANOMALY_TOTAL_IMPACT_PERCENTAGE` can only be used in [AnomalySubscriptions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html) .

Values -> (list)

The metadata values that you can use to filter and group your results. You can use `GetDimensionValues` to find specific values.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results.

`MatchOptions` is only applicable for actions related to Cost Category and Anomaly Subscriptions. Refer to the documentation for each specific API to see what is supported.

The default values for `MatchOptions` are `EQUALS` and `CASE_SENSITIVE` .

(string)

Tags -> (structure)

The specific `Tag` to use for `Expression` .

Key -> (string)

The key for the tag.

Values -> (list)

The specific value of the tag.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results. `MatchOptions` is only applicable for actions related to Cost Category. The default values for `MatchOptions` are `EQUALS` and `CASE_SENSITIVE` .

(string)

CostCategories -> (structure)

The filter thatâs based on `CostCategory` values.

Key -> (string)

The unique name of the Cost Category.

Values -> (list)

The specific value of the Cost Category.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for actions related to cost category. The default values for `MatchOptions` is `EQUALS` and `CASE_SENSITIVE` .

(string)

Dimensions -> (structure)

The specific `Dimension` to use for `Expression` .

Key -> (string)

The names of the metadata types that you can use to filter and group your results. For example, `AZ` returns a list of Availability Zones.

Not all dimensions are supported in each API. Refer to the documentation for each specific API to see what is supported.

`LINKED_ACCOUNT_NAME` and `SERVICE_CODE` can only be used in [CostCategoryRule](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryRule.html) .

`ANOMALY_TOTAL_IMPACT_ABSOLUTE` and `ANOMALY_TOTAL_IMPACT_PERCENTAGE` can only be used in [AnomalySubscriptions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html) .

Values -> (list)

The metadata values that you can use to filter and group your results. You can use `GetDimensionValues` to find specific values.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results.

`MatchOptions` is only applicable for actions related to Cost Category and Anomaly Subscriptions. Refer to the documentation for each specific API to see what is supported.

The default values for `MatchOptions` are `EQUALS` and `CASE_SENSITIVE` .

(string)

Tags -> (structure)

The specific `Tag` to use for `Expression` .

Key -> (string)

The key for the tag.

Values -> (list)

The specific value of the tag.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results. `MatchOptions` is only applicable for actions related to Cost Category. The default values for `MatchOptions` are `EQUALS` and `CASE_SENSITIVE` .

(string)

CostCategories -> (structure)

The filter thatâs based on `CostCategory` values.

Key -> (string)

The unique name of the Cost Category.

Values -> (list)

The specific value of the Cost Category.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for actions related to cost category. The default values for `MatchOptions` is `EQUALS` and `CASE_SENSITIVE` .

(string)

JSON Syntax:

```
{
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
        "Key": "AZ"|"INSTANCE_TYPE"|"LINKED_ACCOUNT"|"LINKED_ACCOUNT_NAME"|"OPERATION"|"PURCHASE_TYPE"|"REGION"|"SERVICE"|"SERVICE_CODE"|"USAGE_TYPE"|"USAGE_TYPE_GROUP"|"RECORD_TYPE"|"OPERATING_SYSTEM"|"TENANCY"|"SCOPE"|"PLATFORM"|"SUBSCRIPTION_ID"|"LEGAL_ENTITY_NAME"|"DEPLOYMENT_OPTION"|"DATABASE_ENGINE"|"CACHE_ENGINE"|"INSTANCE_TYPE_FAMILY"|"BILLING_ENTITY"|"RESERVATION_ID"|"RESOURCE_ID"|"RIGHTSIZING_TYPE"|"SAVINGS_PLANS_TYPE"|"SAVINGS_PLAN_ARN"|"PAYMENT_OPTION"|"AGREEMENT_END_DATE_TIME_AFTER"|"AGREEMENT_END_DATE_TIME_BEFORE"|"INVOICING_ENTITY"|"ANOMALY_TOTAL_IMPACT_ABSOLUTE"|"ANOMALY_TOTAL_IMPACT_PERCENTAGE",
        "Values": ["string", ...],
        "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"CASE_SENSITIVE"|"CASE_INSENSITIVE"|"GREATER_THAN_OR_EQUAL", ...]
      },
      "Tags": {
        "Key": "string",
        "Values": ["string", ...],
        "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"CASE_SENSITIVE"|"CASE_INSENSITIVE"|"GREATER_THAN_OR_EQUAL", ...]
      },
      "CostCategories": {
        "Key": "string",
        "Values": ["string", ...],
        "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"CASE_SENSITIVE"|"CASE_INSENSITIVE"|"GREATER_THAN_OR_EQUAL", ...]
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
        "Key": "AZ"|"INSTANCE_TYPE"|"LINKED_ACCOUNT"|"LINKED_ACCOUNT_NAME"|"OPERATION"|"PURCHASE_TYPE"|"REGION"|"SERVICE"|"SERVICE_CODE"|"USAGE_TYPE"|"USAGE_TYPE_GROUP"|"RECORD_TYPE"|"OPERATING_SYSTEM"|"TENANCY"|"SCOPE"|"PLATFORM"|"SUBSCRIPTION_ID"|"LEGAL_ENTITY_NAME"|"DEPLOYMENT_OPTION"|"DATABASE_ENGINE"|"CACHE_ENGINE"|"INSTANCE_TYPE_FAMILY"|"BILLING_ENTITY"|"RESERVATION_ID"|"RESOURCE_ID"|"RIGHTSIZING_TYPE"|"SAVINGS_PLANS_TYPE"|"SAVINGS_PLAN_ARN"|"PAYMENT_OPTION"|"AGREEMENT_END_DATE_TIME_AFTER"|"AGREEMENT_END_DATE_TIME_BEFORE"|"INVOICING_ENTITY"|"ANOMALY_TOTAL_IMPACT_ABSOLUTE"|"ANOMALY_TOTAL_IMPACT_PERCENTAGE",
        "Values": ["string", ...],
        "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"CASE_SENSITIVE"|"CASE_INSENSITIVE"|"GREATER_THAN_OR_EQUAL", ...]
      },
      "Tags": {
        "Key": "string",
        "Values": ["string", ...],
        "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"CASE_SENSITIVE"|"CASE_INSENSITIVE"|"GREATER_THAN_OR_EQUAL", ...]
      },
      "CostCategories": {
        "Key": "string",
        "Values": ["string", ...],
        "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"CASE_SENSITIVE"|"CASE_INSENSITIVE"|"GREATER_THAN_OR_EQUAL", ...]
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
      "Key": "AZ"|"INSTANCE_TYPE"|"LINKED_ACCOUNT"|"LINKED_ACCOUNT_NAME"|"OPERATION"|"PURCHASE_TYPE"|"REGION"|"SERVICE"|"SERVICE_CODE"|"USAGE_TYPE"|"USAGE_TYPE_GROUP"|"RECORD_TYPE"|"OPERATING_SYSTEM"|"TENANCY"|"SCOPE"|"PLATFORM"|"SUBSCRIPTION_ID"|"LEGAL_ENTITY_NAME"|"DEPLOYMENT_OPTION"|"DATABASE_ENGINE"|"CACHE_ENGINE"|"INSTANCE_TYPE_FAMILY"|"BILLING_ENTITY"|"RESERVATION_ID"|"RESOURCE_ID"|"RIGHTSIZING_TYPE"|"SAVINGS_PLANS_TYPE"|"SAVINGS_PLAN_ARN"|"PAYMENT_OPTION"|"AGREEMENT_END_DATE_TIME_AFTER"|"AGREEMENT_END_DATE_TIME_BEFORE"|"INVOICING_ENTITY"|"ANOMALY_TOTAL_IMPACT_ABSOLUTE"|"ANOMALY_TOTAL_IMPACT_PERCENTAGE",
      "Values": ["string", ...],
      "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"CASE_SENSITIVE"|"CASE_INSENSITIVE"|"GREATER_THAN_OR_EQUAL", ...]
    },
    "Tags": {
      "Key": "string",
      "Values": ["string", ...],
      "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"CASE_SENSITIVE"|"CASE_INSENSITIVE"|"GREATER_THAN_OR_EQUAL", ...]
    },
    "CostCategories": {
      "Key": "string",
      "Values": ["string", ...],
      "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"CASE_SENSITIVE"|"CASE_INSENSITIVE"|"GREATER_THAN_OR_EQUAL", ...]
    }
  },
  "Dimensions": {
    "Key": "AZ"|"INSTANCE_TYPE"|"LINKED_ACCOUNT"|"LINKED_ACCOUNT_NAME"|"OPERATION"|"PURCHASE_TYPE"|"REGION"|"SERVICE"|"SERVICE_CODE"|"USAGE_TYPE"|"USAGE_TYPE_GROUP"|"RECORD_TYPE"|"OPERATING_SYSTEM"|"TENANCY"|"SCOPE"|"PLATFORM"|"SUBSCRIPTION_ID"|"LEGAL_ENTITY_NAME"|"DEPLOYMENT_OPTION"|"DATABASE_ENGINE"|"CACHE_ENGINE"|"INSTANCE_TYPE_FAMILY"|"BILLING_ENTITY"|"RESERVATION_ID"|"RESOURCE_ID"|"RIGHTSIZING_TYPE"|"SAVINGS_PLANS_TYPE"|"SAVINGS_PLAN_ARN"|"PAYMENT_OPTION"|"AGREEMENT_END_DATE_TIME_AFTER"|"AGREEMENT_END_DATE_TIME_BEFORE"|"INVOICING_ENTITY"|"ANOMALY_TOTAL_IMPACT_ABSOLUTE"|"ANOMALY_TOTAL_IMPACT_PERCENTAGE",
    "Values": ["string", ...],
    "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"CASE_SENSITIVE"|"CASE_INSENSITIVE"|"GREATER_THAN_OR_EQUAL", ...]
  },
  "Tags": {
    "Key": "string",
    "Values": ["string", ...],
    "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"CASE_SENSITIVE"|"CASE_INSENSITIVE"|"GREATER_THAN_OR_EQUAL", ...]
  },
  "CostCategories": {
    "Key": "string",
    "Values": ["string", ...],
    "MatchOptions": ["EQUALS"|"ABSENT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS"|"CASE_SENSITIVE"|"CASE_INSENSITIVE"|"GREATER_THAN_OR_EQUAL", ...]
  }
}
```

`--sort-by` (structure)

The value that you want to sort the data by.

The following values are supported for `Key` :

- `UtilizationPercentage`
- `UtilizationPercentageInUnits`
- `PurchasedHours`
- `PurchasedUnits`
- `TotalActualHours`
- `TotalActualUnits`
- `UnusedHours`
- `UnusedUnits`
- `OnDemandCostOfRIHoursUsed`
- `NetRISavings`
- `TotalPotentialRISavings`
- `AmortizedUpfrontFee`
- `AmortizedRecurringFee`
- `TotalAmortizedFee`
- `RICostForUnusedHours`
- `RealizedSavings`
- `UnrealizedSavings`

The supported values for `SortOrder` are `ASCENDING` and `DESCENDING` .

Key -> (string)

The key thatâs used to sort the data.

SortOrder -> (string)

The order thatâs used to sort the data.

Shorthand Syntax:

```
Key=string,SortOrder=string
```

JSON Syntax:

```
{
  "Key": "string",
  "SortOrder": "ASCENDING"|"DESCENDING"
}
```

`--next-page-token` (string)

The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.

`--max-results` (integer)

The maximum number of objects that you returned for this request. If more objects are available, in the response, Amazon Web Services provides a NextPageToken value that you can use in a subsequent call to get the next batch of objects.

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

**To retrieve the reservation utilization for your account**

The following `get-reservation-utilization` example retrieves the RI utilization for all t2.nano instance types from 2018-03-01 to 2018-08-01 for the account.

```
aws ce get-reservation-utilization \
    --time-period Start=2018-03-01,End=2018-08-01 \
    --filter file://filters.json
```

Contents of `filters.json`:

```
{
    "Dimensions": {
        "Key": "INSTANCE_TYPE",
        "Values": [
            "t2.nano"
        ]
    }
}
```

Output:

```
{
    "Total": {
        "TotalAmortizedFee": "0",
        "UtilizationPercentage": "0",
        "PurchasedHours": "0",
        "NetRISavings": "0",
        "TotalActualHours": "0",
        "AmortizedRecurringFee": "0",
        "UnusedHours": "0",
        "TotalPotentialRISavings": "0",
        "OnDemandCostOfRIHoursUsed": "0",
        "AmortizedUpfrontFee": "0"
    },
    "UtilizationsByTime": []
}
```

## Output

UtilizationsByTime -> (list)

The amount of time that you used your Reserved Instances (RIs).

(structure)

The amount of utilization, in hours.

TimePeriod -> (structure)

The period of time that this utilization was used for.

Start -> (string)

The beginning of the time period. The start date is inclusive. For example, if `start` is `2017-01-01` , Amazon Web Services retrieves cost and usage data starting at `2017-01-01` up to the end date. The start date must be equal to or no later than the current date to avoid a validation error.

End -> (string)

The end of the time period. The end date is exclusive. For example, if `end` is `2017-05-01` , Amazon Web Services retrieves cost and usage data from the start date up to, but not including, `2017-05-01` .

Groups -> (list)

The groups that this utilization result uses.

(structure)

A group of reservations that share a set of attributes.

Key -> (string)

The key for a specific reservation attribute.

Value -> (string)

The value of a specific reservation attribute.

Attributes -> (map)

The attributes for this group of reservations.

key -> (string)

value -> (string)

Utilization -> (structure)

How much you used this group of reservations.

UtilizationPercentage -> (string)

The percentage of reservation time that you used.

UtilizationPercentageInUnits -> (string)

The percentage of Amazon EC2 reservation time that you used. Itâs converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

PurchasedHours -> (string)

How many reservation hours that you purchased.

PurchasedUnits -> (string)

The number of Amazon EC2 reservation hours that you purchased. Itâs converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

TotalActualHours -> (string)

The total number of reservation hours that you used.

TotalActualUnits -> (string)

The total number of Amazon EC2 reservation hours that you used. Itâs converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

UnusedHours -> (string)

The number of reservation hours that you didnât use.

UnusedUnits -> (string)

The number of Amazon EC2 reservation hours that you didnât use. Itâs converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

OnDemandCostOfRIHoursUsed -> (string)

How much your reservation costs if charged On-Demand rates.

NetRISavings -> (string)

How much you saved due to purchasing and utilizing reservation. Amazon Web Services calculates this by subtracting `TotalAmortizedFee` from `OnDemandCostOfRIHoursUsed` .

TotalPotentialRISavings -> (string)

How much you might save if you use your entire reservation.

AmortizedUpfrontFee -> (string)

The upfront cost of your reservation. Itâs amortized over the reservation period.

AmortizedRecurringFee -> (string)

The monthly cost of your reservation. Itâs amortized over the reservation period.

TotalAmortizedFee -> (string)

The total cost of your reservation. Itâs amortized over the reservation period.

RICostForUnusedHours -> (string)

The cost of unused hours for your reservation.

RealizedSavings -> (string)

The realized savings because of purchasing and using a reservation.

UnrealizedSavings -> (string)

The unrealized savings because of purchasing and using a reservation.

Total -> (structure)

The total number of reservation hours that were used.

UtilizationPercentage -> (string)

The percentage of reservation time that you used.

UtilizationPercentageInUnits -> (string)

The percentage of Amazon EC2 reservation time that you used. Itâs converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

PurchasedHours -> (string)

How many reservation hours that you purchased.

PurchasedUnits -> (string)

The number of Amazon EC2 reservation hours that you purchased. Itâs converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

TotalActualHours -> (string)

The total number of reservation hours that you used.

TotalActualUnits -> (string)

The total number of Amazon EC2 reservation hours that you used. Itâs converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

UnusedHours -> (string)

The number of reservation hours that you didnât use.

UnusedUnits -> (string)

The number of Amazon EC2 reservation hours that you didnât use. Itâs converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

OnDemandCostOfRIHoursUsed -> (string)

How much your reservation costs if charged On-Demand rates.

NetRISavings -> (string)

How much you saved due to purchasing and utilizing reservation. Amazon Web Services calculates this by subtracting `TotalAmortizedFee` from `OnDemandCostOfRIHoursUsed` .

TotalPotentialRISavings -> (string)

How much you might save if you use your entire reservation.

AmortizedUpfrontFee -> (string)

The upfront cost of your reservation. Itâs amortized over the reservation period.

AmortizedRecurringFee -> (string)

The monthly cost of your reservation. Itâs amortized over the reservation period.

TotalAmortizedFee -> (string)

The total cost of your reservation. Itâs amortized over the reservation period.

RICostForUnusedHours -> (string)

The cost of unused hours for your reservation.

RealizedSavings -> (string)

The realized savings because of purchasing and using a reservation.

UnrealizedSavings -> (string)

The unrealized savings because of purchasing and using a reservation.

Total -> (structure)

The total amount of time that you used your Reserved Instances (RIs).

UtilizationPercentage -> (string)

The percentage of reservation time that you used.

UtilizationPercentageInUnits -> (string)

The percentage of Amazon EC2 reservation time that you used. Itâs converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

PurchasedHours -> (string)

How many reservation hours that you purchased.

PurchasedUnits -> (string)

The number of Amazon EC2 reservation hours that you purchased. Itâs converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

TotalActualHours -> (string)

The total number of reservation hours that you used.

TotalActualUnits -> (string)

The total number of Amazon EC2 reservation hours that you used. Itâs converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

UnusedHours -> (string)

The number of reservation hours that you didnât use.

UnusedUnits -> (string)

The number of Amazon EC2 reservation hours that you didnât use. Itâs converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

OnDemandCostOfRIHoursUsed -> (string)

How much your reservation costs if charged On-Demand rates.

NetRISavings -> (string)

How much you saved due to purchasing and utilizing reservation. Amazon Web Services calculates this by subtracting `TotalAmortizedFee` from `OnDemandCostOfRIHoursUsed` .

TotalPotentialRISavings -> (string)

How much you might save if you use your entire reservation.

AmortizedUpfrontFee -> (string)

The upfront cost of your reservation. Itâs amortized over the reservation period.

AmortizedRecurringFee -> (string)

The monthly cost of your reservation. Itâs amortized over the reservation period.

TotalAmortizedFee -> (string)

The total cost of your reservation. Itâs amortized over the reservation period.

RICostForUnusedHours -> (string)

The cost of unused hours for your reservation.

RealizedSavings -> (string)

The realized savings because of purchasing and using a reservation.

UnrealizedSavings -> (string)

The unrealized savings because of purchasing and using a reservation.

NextPageToken -> (string)

The token for the next set of retrievable results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.