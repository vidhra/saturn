# get-dimension-valuesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-dimension-values.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-dimension-values.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ce](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html#cli-aws-ce) ]

# get-dimension-values

## Description

Retrieves all available filter values for a specified filter over a period of time. You can search the dimension values for an arbitrary string.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetDimensionValues)

## Synopsis

```
get-dimension-values
[--search-string <value>]
--time-period <value>
--dimension <value>
[--context <value>]
[--filter <value>]
[--sort-by <value>]
[--billing-view-arn <value>]
[--max-results <value>]
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

`--search-string` (string)

The value that you want to search the filter values for.

`--time-period` (structure)

The start date and end date for retrieving the dimension values. The start date is inclusive, but the end date is exclusive. For example, if `start` is `2017-01-01` and `end` is `2017-05-01` , then the cost and usage data is retrieved from `2017-01-01` up to and including `2017-04-30` but not including `2017-05-01` .

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

`--dimension` (string)

The name of the dimension. Each `Dimension` is available for a different `Context` . For more information, see `Context` . `LINK_ACCOUNT_NAME` and `SERVICE_CODE` can only be used in [CostCategoryRule](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/AAPI_CostCategoryRule.html) .

Possible values:

- `AZ`
- `INSTANCE_TYPE`
- `LINKED_ACCOUNT`
- `LINKED_ACCOUNT_NAME`
- `OPERATION`
- `PURCHASE_TYPE`
- `REGION`
- `SERVICE`
- `SERVICE_CODE`
- `USAGE_TYPE`
- `USAGE_TYPE_GROUP`
- `RECORD_TYPE`
- `OPERATING_SYSTEM`
- `TENANCY`
- `SCOPE`
- `PLATFORM`
- `SUBSCRIPTION_ID`
- `LEGAL_ENTITY_NAME`
- `DEPLOYMENT_OPTION`
- `DATABASE_ENGINE`
- `CACHE_ENGINE`
- `INSTANCE_TYPE_FAMILY`
- `BILLING_ENTITY`
- `RESERVATION_ID`
- `RESOURCE_ID`
- `RIGHTSIZING_TYPE`
- `SAVINGS_PLANS_TYPE`
- `SAVINGS_PLAN_ARN`
- `PAYMENT_OPTION`
- `AGREEMENT_END_DATE_TIME_AFTER`
- `AGREEMENT_END_DATE_TIME_BEFORE`
- `INVOICING_ENTITY`
- `ANOMALY_TOTAL_IMPACT_ABSOLUTE`
- `ANOMALY_TOTAL_IMPACT_PERCENTAGE`

`--context` (string)

The context for the call to `GetDimensionValues` . This can be `RESERVATIONS` or `COST_AND_USAGE` . The default value is `COST_AND_USAGE` . If the context is set to `RESERVATIONS` , the resulting dimension values can be used in the `GetReservationUtilization` operation. If the context is set to `COST_AND_USAGE` , the resulting dimension values can be used in the `GetCostAndUsage` operation.

If you set the context to `COST_AND_USAGE` , you can use the following dimensions for searching:

- AZ - The Availability Zone. An example is `us-east-1a` .
- BILLING_ENTITY - The Amazon Web Services seller that your account is with. Possible values are the following: - Amazon Web Services(Amazon Web Services): The entity that sells Amazon Web Services services. - AISPL (Amazon Internet Services Pvt. Ltd.): The local Indian entity thatâs an acting reseller for Amazon Web Services services in India. - Amazon Web Services Marketplace: The entity that supports the sale of solutions that are built on Amazon Web Services by third-party software providers.
- CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.
- DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are `SingleAZ` and `MultiAZ` .
- DATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL.
- INSTANCE_TYPE - The type of Amazon EC2 instance. An example is `m4.xlarge` .
- INSTANCE_TYPE_FAMILY - A family of instance types optimized to fit different use cases. Examples are `Compute Optimized` (for example, `C4` , `C5` , `C6g` , and `C7g` ), `Memory Optimization` (for example, `R4` , `R5n` , `R5b` , and `R6g` ).
- INVOICING_ENTITY - The name of the entity that issues the Amazon Web Services invoice.
- LEGAL_ENTITY_NAME - The name of the organization that sells you Amazon Web Services services, such as Amazon Web Services.
- LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the Amazon Web Services ID of the member account.
- OPERATING_SYSTEM - The operating system. Examples are Windows or Linux.
- OPERATION - The action performed. Examples include `RunInstance` and `CreateBucket` .
- PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
- PURCHASE_TYPE - The reservation type of the purchase that this usage is related to. Examples include On-Demand Instances and Standard Reserved Instances.
- RESERVATION_ID - The unique identifier for an Amazon Web Services Reservation Instance.
- SAVINGS_PLAN_ARN - The unique identifier for your Savings Plans.
- SAVINGS_PLANS_TYPE - Type of Savings Plans (EC2 Instance or Compute).
- SERVICE - The Amazon Web Services service such as Amazon DynamoDB.
- TENANCY - The tenancy of a resource. Examples are shared or dedicated.
- USAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the `GetDimensionValues` operation includes a unit attribute. Examples include GB and Hrs.
- USAGE_TYPE_GROUP - The grouping of common usage types. An example is Amazon EC2: CloudWatch â Alarms. The response for this operation includes a unit attribute.
- REGION - The Amazon Web Services Region.
- RECORD_TYPE - The different types of charges such as Reserved Instance (RI) fees, usage costs, tax refunds, and credits.
- RESOURCE_ID - The unique identifier of the resource. ResourceId is an opt-in feature only available for last 14 days for EC2-Compute Service.

If you set the context to `RESERVATIONS` , you can use the following dimensions for searching:

- AZ - The Availability Zone. An example is `us-east-1a` .
- CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.
- DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are `SingleAZ` and `MultiAZ` .
- INSTANCE_TYPE - The type of Amazon EC2 instance. An example is `m4.xlarge` .
- LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the Amazon Web Services ID of the member account.
- PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
- REGION - The Amazon Web Services Region.
- SCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a single Availability Zone.
- TAG (Coverage only) - The tags that are associated with a Reserved Instance (RI).
- TENANCY - The tenancy of a resource. Examples are shared or dedicated.

If you set the context to `SAVINGS_PLANS` , you can use the following dimensions for searching:

- SAVINGS_PLANS_TYPE - Type of Savings Plans (EC2 Instance or Compute)
- PAYMENT_OPTION - The payment option for the given Savings Plans (for example, All Upfront)
- REGION - The Amazon Web Services Region.
- INSTANCE_TYPE_FAMILY - The family of instances (For example, `m5` )
- LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the Amazon Web Services ID of the member account.
- SAVINGS_PLAN_ARN - The unique identifier for your Savings Plans.

Possible values:

- `COST_AND_USAGE`
- `RESERVATIONS`
- `SAVINGS_PLANS`

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

`--sort-by` (list)

The value that you want to sort the data by.

The key represents cost and usage metrics. The following values are supported:

- `BlendedCost`
- `UnblendedCost`
- `AmortizedCost`
- `NetAmortizedCost`
- `NetUnblendedCost`
- `UsageQuantity`
- `NormalizedUsageAmount`

The supported values for the `SortOrder` key are `ASCENDING` or `DESCENDING` .

When you specify a `SortBy` paramater, the context must be `COST_AND_USAGE` . Further, when using `SortBy` , `NextPageToken` and `SearchString` arenât supported.

(structure)

The details for how to sort the data.

Key -> (string)

The key thatâs used to sort the data.

SortOrder -> (string)

The order thatâs used to sort the data.

Shorthand Syntax:

```
Key=string,SortOrder=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "SortOrder": "ASCENDING"|"DESCENDING"
  }
  ...
]
```

`--billing-view-arn` (string)

The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.

`--max-results` (integer)

This field is only used when SortBy is provided in the request. The maximum number of objects that are returned for this request. If MaxResults isnât specified with SortBy, the request returns 1000 results as the default value for this parameter.

For `GetDimensionValues` , MaxResults has an upper limit of 1000.

`--next-page-token` (string)

The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.

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

**To retrieve the tags for the dimension SERVICE, with a value of âElasticâ**

This example retrieves the tags for the dimension SERVICE, with a value of âElasticâ for January 01 2017 through May 18 2017.

Command:

```
aws ce get-dimension-values --search-string Elastic --time-period Start=2017-01-01,End=2017-05-18 --dimension SERVICE
```

Output:

```
{
   "TotalSize": 6,
   "DimensionValues": [
       {
           "Attributes": {},
           "Value": "Amazon ElastiCache"
       },
       {
           "Attributes": {},
           "Value": "EC2 - Other"
       },
       {
           "Attributes": {},
           "Value": "Amazon Elastic Compute Cloud - Compute"
       },
       {
           "Attributes": {},
           "Value": "Amazon Elastic Load Balancing"
       },
       {
           "Attributes": {},
           "Value": "Amazon Elastic MapReduce"
       },
       {
           "Attributes": {},
           "Value": "Amazon Elasticsearch Service"
       }
   ],
   "ReturnSize": 6
}
```

## Output

DimensionValues -> (list)

The filters that you used to filter your request. Some dimensions are available only for a specific context.

If you set the context to `COST_AND_USAGE` , you can use the following dimensions for searching:

- AZ - The Availability Zone. An example is `us-east-1a` .
- DATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL.
- INSTANCE_TYPE - The type of Amazon EC2 instance. An example is `m4.xlarge` .
- LEGAL_ENTITY_NAME - The name of the organization that sells you Amazon Web Services services, such as Amazon Web Services.
- LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the Amazon Web Services ID of the member account.
- OPERATING_SYSTEM - The operating system. Examples are Windows or Linux.
- OPERATION - The action performed. Examples include `RunInstance` and `CreateBucket` .
- PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
- PURCHASE_TYPE - The reservation type of the purchase to which this usage is related. Examples include On-Demand Instances and Standard Reserved Instances.
- SERVICE - The Amazon Web Services service such as Amazon DynamoDB.
- USAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the `GetDimensionValues` operation includes a unit attribute. Examples include GB and Hrs.
- USAGE_TYPE_GROUP - The grouping of common usage types. An example is Amazon EC2: CloudWatch â Alarms. The response for this operation includes a unit attribute.
- RECORD_TYPE - The different types of charges such as RI fees, usage costs, tax refunds, and credits.
- RESOURCE_ID - The unique identifier of the resource. ResourceId is an opt-in feature only available for last 14 days for EC2-Compute Service. You can opt-in by enabling `Hourly` and `Resource Level Data` in Cost Management Console preferences.

If you set the context to `RESERVATIONS` , you can use the following dimensions for searching:

- AZ - The Availability Zone. An example is `us-east-1a` .
- CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.
- DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are `SingleAZ` and `MultiAZ` .
- INSTANCE_TYPE - The type of Amazon EC2 instance. An example is `m4.xlarge` .
- LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the Amazon Web Services ID of the member account.
- PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
- REGION - The Amazon Web Services Region.
- SCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a single Availability Zone.
- TAG (Coverage only) - The tags that are associated with a Reserved Instance (RI).
- TENANCY - The tenancy of a resource. Examples are shared or dedicated.

If you set the context to `SAVINGS_PLANS` , you can use the following dimensions for searching:

- SAVINGS_PLANS_TYPE - Type of Savings Plans (EC2 Instance or Compute)
- PAYMENT_OPTION - Payment option for the given Savings Plans (for example, All Upfront)
- REGION - The Amazon Web Services Region.
- INSTANCE_TYPE_FAMILY - The family of instances (For example, `m5` )
- LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the Amazon Web Services ID of the member account.
- SAVINGS_PLAN_ARN - The unique identifier for your Savings Plan

(structure)

The metadata of a specific type that you can use to filter and group your results. You can use `GetDimensionValues` to find specific values.

Value -> (string)

The value of a dimension with a specific attribute.

Attributes -> (map)

The attribute that applies to a specific `Dimension` .

key -> (string)

value -> (string)

ReturnSize -> (integer)

The number of results that Amazon Web Services returned at one time.

TotalSize -> (integer)

The total number of search results.

NextPageToken -> (string)

The token for the next set of retrievable results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.