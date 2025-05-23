# get-savings-plans-purchase-recommendationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-savings-plans-purchase-recommendation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-savings-plans-purchase-recommendation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ce](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html#cli-aws-ce) ]

# get-savings-plans-purchase-recommendation

## Description

Retrieves the Savings Plans recommendations for your account. First use `StartSavingsPlansPurchaseRecommendationGeneration` to generate a new set of recommendations, and then use `GetSavingsPlansPurchaseRecommendation` to retrieve them.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetSavingsPlansPurchaseRecommendation)

## Synopsis

```
get-savings-plans-purchase-recommendation
--savings-plans-type <value>
--term-in-years <value>
--payment-option <value>
[--account-scope <value>]
[--next-page-token <value>]
[--page-size <value>]
--lookback-period-in-days <value>
[--filter <value>]
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

`--savings-plans-type` (string)

The Savings Plans recommendation type thatâs requested.

Possible values:

- `COMPUTE_SP`
- `EC2_INSTANCE_SP`
- `SAGEMAKER_SP`

`--term-in-years` (string)

The savings plan recommendation term thatâs used to generate these recommendations.

Possible values:

- `ONE_YEAR`
- `THREE_YEARS`

`--payment-option` (string)

The payment option thatâs used to generate these recommendations.

Possible values:

- `NO_UPFRONT`
- `PARTIAL_UPFRONT`
- `ALL_UPFRONT`
- `LIGHT_UTILIZATION`
- `MEDIUM_UTILIZATION`
- `HEAVY_UTILIZATION`

`--account-scope` (string)

The account scope that you want your recommendations for. Amazon Web Services calculates recommendations including the management account and member accounts if the value is set to `PAYER` . If the value is `LINKED` , recommendations are calculated for individual member accounts only.

Possible values:

- `PAYER`
- `LINKED`

`--next-page-token` (string)

The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.

`--page-size` (integer)

The number of recommendations that you want returned in a single response object.

`--lookback-period-in-days` (string)

The lookback period thatâs used to generate the recommendation.

Possible values:

- `SEVEN_DAYS`
- `THIRTY_DAYS`
- `SIXTY_DAYS`

`--filter` (structure)

You can filter your recommendations by Account ID with the `LINKED_ACCOUNT` dimension. To filter your recommendations by Account ID, specify `Key` as `LINKED_ACCOUNT` and `Value` as the comma-separated Acount ID(s) that you want to see Savings Plans purchase recommendations for.

For GetSavingsPlansPurchaseRecommendation, the `Filter` doesnât include `CostCategories` or `Tags` . It only includes `Dimensions` . With `Dimensions` , `Key` must be `LINKED_ACCOUNT` and `Value` can be a single Account ID or multiple comma-separated Account IDs that you want to see Savings Plans Purchase Recommendations for. `AND` and `OR` operators are not supported.

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

Information that regards this specific recommendation set.

RecommendationId -> (string)

The unique identifier for the recommendation set.

GenerationTimestamp -> (string)

The timestamp that shows when the recommendations were generated.

AdditionalMetadata -> (string)

Additional metadata that might be applicable to the recommendation.

SavingsPlansPurchaseRecommendation -> (structure)

Contains your request parameters, Savings Plan Recommendations Summary, and Details.

AccountScope -> (string)

The account scope that you want your recommendations for. Amazon Web Services calculates recommendations that include the management account and member accounts if the value is set to `PAYER` . If the value is `LINKED` , recommendations are calculated for individual member accounts only.

SavingsPlansType -> (string)

The requested Savings Plans recommendation type.

TermInYears -> (string)

The Savings Plans recommendation term in years. Itâs used to generate the recommendation.

PaymentOption -> (string)

The payment option thatâs used to generate the recommendation.

LookbackPeriodInDays -> (string)

The lookback period in days thatâs used to generate the recommendation.

SavingsPlansPurchaseRecommendationDetails -> (list)

Details for the Savings Plans that we recommend that you purchase to cover existing Savings Plans eligible workloads.

(structure)

Details for your recommended Savings Plans.

SavingsPlansDetails -> (structure)

Details for your recommended Savings Plans.

Region -> (string)

A collection of Amazon Web Services resources in a geographic area. Each Amazon Web Services Region is isolated and independent of the other Regions.

InstanceFamily -> (string)

A group of instance types that Savings Plans applies to.

OfferingId -> (string)

The unique ID thatâs used to distinguish Savings Plans from one another.

AccountId -> (string)

The `AccountID` the recommendation is generated for.

UpfrontCost -> (string)

The upfront cost of the recommended Savings Plans, based on the selected payment option.

EstimatedROI -> (string)

The estimated return on investment thatâs based on the recommended Savings Plans that you purchased. This is calculated as `estimatedSavingsAmount` / `estimatedSPCost` [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-savings-plans-purchase-recommendation.html#id1)100.

CurrencyCode -> (string)

The currency code that Amazon Web Services used to generate the recommendations and present potential savings.

EstimatedSPCost -> (string)

The cost of the recommended Savings Plans over the length of the lookback period.

EstimatedOnDemandCost -> (string)

The remaining On-Demand cost estimated to not be covered by the recommended Savings Plans, over the length of the lookback period.

EstimatedOnDemandCostWithCurrentCommitment -> (string)

The estimated On-Demand costs you expect with no additional commitment, based on your usage of the selected time period and the Savings Plans you own.

EstimatedSavingsAmount -> (string)

The estimated savings amount thatâs based on the recommended Savings Plans over the length of the lookback period.

EstimatedSavingsPercentage -> (string)

The estimated savings percentage relative to the total cost of applicable On-Demand usage over the lookback period.

HourlyCommitmentToPurchase -> (string)

The recommended hourly commitment level for the Savings Plans type and the configuration thatâs based on the usage during the lookback period.

EstimatedAverageUtilization -> (string)

The estimated utilization of the recommended Savings Plans.

EstimatedMonthlySavingsAmount -> (string)

The estimated monthly savings amount based on the recommended Savings Plans.

CurrentMinimumHourlyOnDemandSpend -> (string)

The lowest value of hourly On-Demand spend over the lookback period of the applicable usage type.

CurrentMaximumHourlyOnDemandSpend -> (string)

The highest value of hourly On-Demand spend over the lookback period of the applicable usage type.

CurrentAverageHourlyOnDemandSpend -> (string)

The average value of hourly On-Demand spend over the lookback period of the applicable usage type.

RecommendationDetailId -> (string)

Contains detailed information about a specific Savings Plan recommendation.

SavingsPlansPurchaseRecommendationSummary -> (structure)

Summary metrics for your Savings Plans Recommendations.

EstimatedROI -> (string)

The estimated return on investment thatâs based on the recommended Savings Plans and estimated savings.

CurrencyCode -> (string)

The currency code that Amazon Web Services used to generate the recommendations and present potential savings.

EstimatedTotalCost -> (string)

The estimated total cost of the usage after purchasing the recommended Savings Plans. This is a sum of the cost of Savings Plans during this term, and the remaining On-Demand usage.

CurrentOnDemandSpend -> (string)

The current total on demand spend of the applicable usage types over the lookback period.

EstimatedSavingsAmount -> (string)

The estimated total savings over the lookback period, based on the purchase of the recommended Savings Plans.

TotalRecommendationCount -> (string)

The aggregate number of Savings Plans recommendations that exist for your account.

DailyCommitmentToPurchase -> (string)

The recommended Savings Plans cost on a daily (24 hourly) basis.

HourlyCommitmentToPurchase -> (string)

The recommended hourly commitment thatâs based on the recommendation parameters.

EstimatedSavingsPercentage -> (string)

The estimated savings relative to the total cost of On-Demand usage, over the lookback period. This is calculated as `estimatedSavingsAmount` / `CurrentOnDemandSpend` [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-savings-plans-purchase-recommendation.html#id3)100.

EstimatedMonthlySavingsAmount -> (string)

The estimated monthly savings amount thatâs based on the recommended Savings Plans purchase.

EstimatedOnDemandCostWithCurrentCommitment -> (string)

The estimated On-Demand costs you expect with no additional commitment. Itâs based on your usage of the selected time period and the Savings Plans you own.

NextPageToken -> (string)

The token for the next set of retrievable results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.