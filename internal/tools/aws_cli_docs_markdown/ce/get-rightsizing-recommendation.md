# get-rightsizing-recommendationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-rightsizing-recommendation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-rightsizing-recommendation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ce](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html#cli-aws-ce) ]

# get-rightsizing-recommendation

## Description

Creates recommendations that help you save cost by identifying idle and underutilized Amazon EC2 instances.

Recommendations are generated to either downsize or terminate instances, along with providing savings detail and metrics. For more information about calculation and function, see [Optimizing Your Cost with Rightsizing Recommendations](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-rightsizing.html) in the *Billing and Cost Management User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetRightsizingRecommendation)

## Synopsis

```
get-rightsizing-recommendation
[--filter <value>]
[--configuration <value>]
--service <value>
[--page-size <value>]
[--next-page-token <value>]
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

`--filter` (structure)

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

`--configuration` (structure)

You can use Configuration to customize recommendations across two attributes. You can choose to view recommendations for instances within the same instance families or across different instance families. You can also choose to view your estimated savings that are associated with recommendations with consideration of existing Savings Plans or RI benefits, or neither.

RecommendationTarget -> (string)

The option to see recommendations within the same instance family or recommendations for instances across other families. The default value is `SAME_INSTANCE_FAMILY` .

BenefitsConsidered -> (boolean)

The option to consider RI or Savings Plans discount benefits in your savings calculation. The default value is `TRUE` .

Shorthand Syntax:

```
RecommendationTarget=string,BenefitsConsidered=boolean
```

JSON Syntax:

```
{
  "RecommendationTarget": "SAME_INSTANCE_FAMILY"|"CROSS_INSTANCE_FAMILY",
  "BenefitsConsidered": true|false
}
```

`--service` (string)

The specific service that you want recommendations for. The only valid value for `GetRightsizingRecommendation` is â`AmazonEC2` â.

`--page-size` (integer)

The number of recommendations that you want returned in a single response object.

`--next-page-token` (string)

The pagination token that indicates the next set of results that you want to retrieve.

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

Metadata -> (structure)

Information regarding this specific recommendation set.

RecommendationId -> (string)

The ID for the recommendation.

GenerationTimestamp -> (string)

The timestamp for when Amazon Web Services made the recommendation.

LookbackPeriodInDays -> (string)

The number of days of previous usage that Amazon Web Services considers when making the recommendation.

AdditionalMetadata -> (string)

Additional metadata that might be applicable to the recommendation.

Summary -> (structure)

Summary of this recommendation set.

TotalRecommendationCount -> (string)

The total number of instance recommendations.

EstimatedTotalMonthlySavingsAmount -> (string)

The estimated total savings resulting from modifications, on a monthly basis.

SavingsCurrencyCode -> (string)

The currency code that Amazon Web Services used to calculate the savings.

SavingsPercentage -> (string)

The savings percentage based on the recommended modifications. Itâs relative to the total On-Demand costs that are associated with these instances.

RightsizingRecommendations -> (list)

Recommendations to rightsize resources.

(structure)

Recommendations to rightsize resources.

AccountId -> (string)

The account that this recommendation is for.

CurrentInstance -> (structure)

Context regarding the current instance.

ResourceId -> (string)

Resource ID of the current instance.

InstanceName -> (string)

The name that you given an instance. This field shows as blank if you havenât given the instance a name.

Tags -> (list)

Cost allocation resource tags that are applied to the instance.

(structure)

The values that are available for a tag.

If `Values` and `Key` arenât specified, the `ABSENT` `MatchOption` is applied to all tags. That is, itâs filtered on resources with no tags.

If `Key` is provided and `Values` isnât specified, the `ABSENT` `MatchOption` is applied to the tag `Key` only. That is, itâs filtered on resources without the given tag key.

Key -> (string)

The key for the tag.

Values -> (list)

The specific value of the tag.

(string)

MatchOptions -> (list)

The match options that you can use to filter your results. `MatchOptions` is only applicable for actions related to Cost Category. The default values for `MatchOptions` are `EQUALS` and `CASE_SENSITIVE` .

(string)

ResourceDetails -> (structure)

Details about the resource and utilization.

EC2ResourceDetails -> (structure)

Details for the Amazon EC2 resource.

HourlyOnDemandRate -> (string)

The hourly public On-Demand rate for the instance type.

InstanceType -> (string)

The type of Amazon Web Services instance.

Platform -> (string)

The platform of the Amazon Web Services instance. The platform is the specific combination of operating system, license model, and software on an instance.

Region -> (string)

The Amazon Web Services Region of the instance.

Sku -> (string)

The SKU of the product.

Memory -> (string)

The memory capacity of the Amazon Web Services instance.

NetworkPerformance -> (string)

The network performance capacity of the Amazon Web Services instance.

Storage -> (string)

The disk storage of the Amazon Web Services instance. This doesnât include EBS storage.

Vcpu -> (string)

The number of VCPU cores in the Amazon Web Services instance type.

ResourceUtilization -> (structure)

Utilization information of the current instance during the lookback period.

EC2ResourceUtilization -> (structure)

The utilization of current Amazon EC2 instance.

MaxCpuUtilizationPercentage -> (string)

The maximum observed or expected CPU utilization of the instance.

MaxMemoryUtilizationPercentage -> (string)

The maximum observed or expected memory utilization of the instance.

MaxStorageUtilizationPercentage -> (string)

The maximum observed or expected storage utilization of the instance. This doesnât include EBS storage.

EBSResourceUtilization -> (structure)

The EBS field that contains a list of EBS metrics that are associated with the current instance.

EbsReadOpsPerSecond -> (string)

The maximum number of read operations per second.

EbsWriteOpsPerSecond -> (string)

The maximum number of write operations per second.

EbsReadBytesPerSecond -> (string)

The maximum size of read operations per second

EbsWriteBytesPerSecond -> (string)

The maximum size of write operations per second.

DiskResourceUtilization -> (structure)

The field that contains a list of disk (local storage) metrics that are associated with the current instance.

DiskReadOpsPerSecond -> (string)

The maximum number of read operations per second.

DiskWriteOpsPerSecond -> (string)

The maximum number of write operations per second.

DiskReadBytesPerSecond -> (string)

The maximum read throughput operations per second.

DiskWriteBytesPerSecond -> (string)

The maximum write throughput operations per second.

NetworkResourceUtilization -> (structure)

The network field that contains a list of network metrics that are associated with the current instance.

NetworkInBytesPerSecond -> (string)

The network inbound throughput utilization measured in Bytes per second (Bps).

NetworkOutBytesPerSecond -> (string)

The network outbound throughput utilization measured in Bytes per second (Bps).

NetworkPacketsInPerSecond -> (string)

The network inbound packets that are measured in packets per second.

NetworkPacketsOutPerSecond -> (string)

The network outbound packets that are measured in packets per second.

ReservationCoveredHoursInLookbackPeriod -> (string)

The number of hours during the lookback period thatâs covered by reservations.

SavingsPlansCoveredHoursInLookbackPeriod -> (string)

The number of hours during the lookback period thatâs covered by Savings Plans.

OnDemandHoursInLookbackPeriod -> (string)

The number of hours during the lookback period thatâs billed at On-Demand rates.

TotalRunningHoursInLookbackPeriod -> (string)

The total number of hours that the instance ran during the lookback period.

MonthlyCost -> (string)

The current On-Demand cost of operating this instance on a monthly basis.

CurrencyCode -> (string)

The currency code that Amazon Web Services used to calculate the costs for this instance.

RightsizingType -> (string)

A recommendation to either terminate or modify the resource.

ModifyRecommendationDetail -> (structure)

The details for the modification recommendations.

TargetInstances -> (list)

Determines whether this instance type is the Amazon Web Services default recommendation.

(structure)

Details on recommended instance.

EstimatedMonthlyCost -> (string)

The expected cost to operate this instance type on a monthly basis.

EstimatedMonthlySavings -> (string)

The estimated savings that result from modification, on a monthly basis.

CurrencyCode -> (string)

The currency code that Amazon Web Services used to calculate the costs for this instance.

DefaultTargetInstance -> (boolean)

Determines whether this recommendation is the defaulted Amazon Web Services recommendation.

ResourceDetails -> (structure)

Details on the target instance type.

EC2ResourceDetails -> (structure)

Details for the Amazon EC2 resource.

HourlyOnDemandRate -> (string)

The hourly public On-Demand rate for the instance type.

InstanceType -> (string)

The type of Amazon Web Services instance.

Platform -> (string)

The platform of the Amazon Web Services instance. The platform is the specific combination of operating system, license model, and software on an instance.

Region -> (string)

The Amazon Web Services Region of the instance.

Sku -> (string)

The SKU of the product.

Memory -> (string)

The memory capacity of the Amazon Web Services instance.

NetworkPerformance -> (string)

The network performance capacity of the Amazon Web Services instance.

Storage -> (string)

The disk storage of the Amazon Web Services instance. This doesnât include EBS storage.

Vcpu -> (string)

The number of VCPU cores in the Amazon Web Services instance type.

ExpectedResourceUtilization -> (structure)

The expected utilization metrics for target instance type.

EC2ResourceUtilization -> (structure)

The utilization of current Amazon EC2 instance.

MaxCpuUtilizationPercentage -> (string)

The maximum observed or expected CPU utilization of the instance.

MaxMemoryUtilizationPercentage -> (string)

The maximum observed or expected memory utilization of the instance.

MaxStorageUtilizationPercentage -> (string)

The maximum observed or expected storage utilization of the instance. This doesnât include EBS storage.

EBSResourceUtilization -> (structure)

The EBS field that contains a list of EBS metrics that are associated with the current instance.

EbsReadOpsPerSecond -> (string)

The maximum number of read operations per second.

EbsWriteOpsPerSecond -> (string)

The maximum number of write operations per second.

EbsReadBytesPerSecond -> (string)

The maximum size of read operations per second

EbsWriteBytesPerSecond -> (string)

The maximum size of write operations per second.

DiskResourceUtilization -> (structure)

The field that contains a list of disk (local storage) metrics that are associated with the current instance.

DiskReadOpsPerSecond -> (string)

The maximum number of read operations per second.

DiskWriteOpsPerSecond -> (string)

The maximum number of write operations per second.

DiskReadBytesPerSecond -> (string)

The maximum read throughput operations per second.

DiskWriteBytesPerSecond -> (string)

The maximum write throughput operations per second.

NetworkResourceUtilization -> (structure)

The network field that contains a list of network metrics that are associated with the current instance.

NetworkInBytesPerSecond -> (string)

The network inbound throughput utilization measured in Bytes per second (Bps).

NetworkOutBytesPerSecond -> (string)

The network outbound throughput utilization measured in Bytes per second (Bps).

NetworkPacketsInPerSecond -> (string)

The network inbound packets that are measured in packets per second.

NetworkPacketsOutPerSecond -> (string)

The network outbound packets that are measured in packets per second.

PlatformDifferences -> (list)

Explains the actions that you might need to take to successfully migrate your workloads from the current instance type to the recommended instance type.

(string)

TerminateRecommendationDetail -> (structure)

The details for termination recommendations.

EstimatedMonthlySavings -> (string)

The estimated savings that result from modification, on a monthly basis.

CurrencyCode -> (string)

The currency code that Amazon Web Services used to calculate the costs for this instance.

FindingReasonCodes -> (list)

The list of possible reasons why the recommendation is generated, such as under- or over-utilization of specific metrics (for example, CPU, Memory, Network).

(string)

NextPageToken -> (string)

The token to retrieve the next set of results.

Configuration -> (structure)

You can use Configuration to customize recommendations across two attributes. You can choose to view recommendations for instances within the same instance families or across different instance families. You can also choose to view your estimated savings that are associated with recommendations with consideration of existing Savings Plans or RI benefits, or neither.

RecommendationTarget -> (string)

The option to see recommendations within the same instance family or recommendations for instances across other families. The default value is `SAME_INSTANCE_FAMILY` .

BenefitsConsidered -> (boolean)

The option to consider RI or Savings Plans discount benefits in your savings calculation. The default value is `TRUE` .