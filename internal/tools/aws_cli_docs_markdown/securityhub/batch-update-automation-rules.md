# batch-update-automation-rulesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-update-automation-rules.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-update-automation-rules.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [securityhub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/index.html#cli-aws-securityhub) ]

# batch-update-automation-rules

## Description

Updates one or more automation rules based on rule Amazon Resource Names (ARNs) and input parameters.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/BatchUpdateAutomationRules)

## Synopsis

```
batch-update-automation-rules
--update-automation-rules-request-items <value>
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

`--update-automation-rules-request-items` (list)

An array of ARNs for the rules that are to be updated. Optionally, you can also include `RuleStatus` and `RuleOrder` .

(structure)

Specifies the parameters to update in an existing automation rule.

RuleArn -> (string)

The Amazon Resource Name (ARN) for the rule.

RuleStatus -> (string)

Whether the rule is active after it is created. If this parameter is equal to `ENABLED` , Security Hub starts applying the rule to findings and finding updates after the rule is created. To change the value of this parameter after creating a rule, use ` `BatchUpdateAutomationRules` [https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateAutomationRules](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateAutomationRules).html`__ .

RuleOrder -> (integer)

An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings. Security Hub applies rules with lower values for this parameter first.

Description -> (string)

A description of the rule.

RuleName -> (string)

The name of the rule.

IsTerminal -> (boolean)

Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria. This is useful when a finding matches the criteria for multiple rules, and each rule has different actions. If a rule is terminal, Security Hub applies the rule action to a finding that matches the rule criteria and doesnât evaluate other rules for the finding. By default, a rule isnât terminal.

Criteria -> (structure)

A set of ASFF finding field attributes and corresponding expected values that Security Hub uses to filter findings. If a rule is enabled and a finding matches the conditions specified in this parameter, Security Hub applies the rule action to the finding.

ProductArn -> (list)

The Amazon Resource Name (ARN) for a third-party product that generated a finding in Security Hub.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

AwsAccountId -> (list)

The Amazon Web Services account ID in which a finding was generated.

Array Members: Minimum number of 1 item. Maximum number of 100 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

Id -> (list)

The product-specific identifier for a finding.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

GeneratorId -> (list)

The identifier for the solution-specific component that generated a finding.

Array Members: Minimum number of 1 item. Maximum number of 100 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

Type -> (list)

One or more finding types in the format of namespace/category/classifier that classify a finding. For a list of namespaces, classifiers, and categories, see [Types taxonomy for ASFF](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format-type-taxonomy.html) in the *Security Hub User Guide* .

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

FirstObservedAt -> (list)

A timestamp that indicates when the potential security issue captured by a finding was first observed by the security findings product.

For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps) .

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A date filter for querying findings.

Start -> (string)

A timestamp that provides the start date for the date filter.

For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps) .

End -> (string)

A timestamp that provides the end date for the date filter.

For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps) .

DateRange -> (structure)

A date range for the date filter.

Value -> (integer)

A date range value for the date filter.

Unit -> (string)

A date range unit for the date filter.

LastObservedAt -> (list)

A timestamp that indicates when the security findings provider most recently observed a change in the resource that is involved in the finding.

For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps) .

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A date filter for querying findings.

Start -> (string)

A timestamp that provides the start date for the date filter.

For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps) .

End -> (string)

A timestamp that provides the end date for the date filter.

For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps) .

DateRange -> (structure)

A date range for the date filter.

Value -> (integer)

A date range value for the date filter.

Unit -> (string)

A date range unit for the date filter.

CreatedAt -> (list)

A timestamp that indicates when this finding record was created.

For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps) .

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A date filter for querying findings.

Start -> (string)

A timestamp that provides the start date for the date filter.

For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps) .

End -> (string)

A timestamp that provides the end date for the date filter.

For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps) .

DateRange -> (structure)

A date range for the date filter.

Value -> (integer)

A date range value for the date filter.

Unit -> (string)

A date range unit for the date filter.

UpdatedAt -> (list)

A timestamp that indicates when the finding record was most recently updated.

For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps) .

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A date filter for querying findings.

Start -> (string)

A timestamp that provides the start date for the date filter.

For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps) .

End -> (string)

A timestamp that provides the end date for the date filter.

For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps) .

DateRange -> (structure)

A date range for the date filter.

Value -> (integer)

A date range value for the date filter.

Unit -> (string)

A date range unit for the date filter.

Confidence -> (list)

The likelihood that a finding accurately identifies the behavior or issue that it was intended to identify. `Confidence` is scored on a 0â100 basis using a ratio scale. A value of `0` means 0 percent confidence, and a value of `100` means 100 percent confidence. For example, a data exfiltration detection based on a statistical deviation of network traffic has low confidence because an actual exfiltration hasnât been verified. For more information, see [Confidence](https://docs.aws.amazon.com/securityhub/latest/userguide/asff-top-level-attributes.html#asff-confidence) in the *Security Hub User Guide* .

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A number filter for querying findings.

Gte -> (double)

The greater-than-equal condition to be applied to a single field when querying for findings.

Lte -> (double)

The less-than-equal condition to be applied to a single field when querying for findings.

Eq -> (double)

The equal-to condition to be applied to a single field when querying for findings.

Gt -> (double)

The greater-than condition to be applied to a single field when querying for findings.

Lt -> (double)

The less-than condition to be applied to a single field when querying for findings.

Criticality -> (list)

The level of importance that is assigned to the resources that are associated with a finding. `Criticality` is scored on a 0â100 basis, using a ratio scale that supports only full integers. A score of `0` means that the underlying resources have no criticality, and a score of `100` is reserved for the most critical resources. For more information, see [Criticality](https://docs.aws.amazon.com/securityhub/latest/userguide/asff-top-level-attributes.html#asff-criticality) in the *Security Hub User Guide* .

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A number filter for querying findings.

Gte -> (double)

The greater-than-equal condition to be applied to a single field when querying for findings.

Lte -> (double)

The less-than-equal condition to be applied to a single field when querying for findings.

Eq -> (double)

The equal-to condition to be applied to a single field when querying for findings.

Gt -> (double)

The greater-than condition to be applied to a single field when querying for findings.

Lt -> (double)

The less-than condition to be applied to a single field when querying for findings.

Title -> (list)

A findingâs title.

Array Members: Minimum number of 1 item. Maximum number of 100 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

Description -> (list)

A findingâs description.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

SourceUrl -> (list)

Provides a URL that links to a page about the current finding in the finding product.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

ProductName -> (list)

Provides the name of the product that generated the finding. For control-based findings, the product name is Security Hub.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

CompanyName -> (list)

The name of the company for the product that generated the finding. For control-based findings, the company is Amazon Web Services.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

SeverityLabel -> (list)

The severity value of the finding.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

ResourceType -> (list)

The type of resource that the finding pertains to.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

ResourceId -> (list)

The identifier for the given resource type. For Amazon Web Services resources that are identified by Amazon Resource Names (ARNs), this is the ARN. For Amazon Web Services resources that lack ARNs, this is the identifier as defined by the Amazon Web Services service that created the resource. For non-Amazon Web Services resources, this is a unique identifier that is associated with the resource.

Array Members: Minimum number of 1 item. Maximum number of 100 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

ResourcePartition -> (list)

The partition in which the resource that the finding pertains to is located. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

ResourceRegion -> (list)

The Amazon Web Services Region where the resource that a finding pertains to is located.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

ResourceTags -> (list)

A list of Amazon Web Services tags associated with a resource at the time the finding was processed.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A map filter for filtering Security Hub findings. Each map filter provides the field to check for, the value to check for, and the comparison operator.

Key -> (string)

The key of the map filter. For example, for `ResourceTags` , `Key` identifies the name of the tag. For `UserDefinedFields` , `Key` is the name of the field.

Value -> (string)

The value for the key in the map filter. Filter values are case sensitive. For example, one of the values for a tag called `Department` might be `Security` . If you provide `security` as the filter value, then thereâs no match.

Comparison -> (string)

The condition to apply to the key value when filtering Security Hub findings with a map filter.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, for the `ResourceTags` field, the filter `Department CONTAINS Security` matches findings that include the value `Security` for the `Department` tag. In the same example, a finding with a value of `Security team` for the `Department` tag is a match.
- To search for values that exactly match the filter value, use `EQUALS` . For example, for the `ResourceTags` field, the filter `Department EQUALS Security` matches findings that have the value `Security` for the `Department` tag.

`CONTAINS` and `EQUALS` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Department CONTAINS Security OR Department CONTAINS Finance` match a finding that includes either `Security` , `Finance` , or both values.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, for the `ResourceTags` field, the filter `Department NOT_CONTAINS Finance` matches findings that exclude the value `Finance` for the `Department` tag.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, for the `ResourceTags` field, the filter `Department NOT_EQUALS Finance` matches findings that donât have the value `Finance` for the `Department` tag.

`NOT_CONTAINS` and `NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Department NOT_CONTAINS Security AND Department NOT_CONTAINS Finance` match a finding that excludes both the `Security` and `Finance` values.

`CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât have both an `EQUALS` filter and a `NOT_EQUALS` filter on the same field. Combining filters in this way returns an error.

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

ResourceDetailsOther -> (list)

Custom fields and values about the resource that a finding pertains to.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A map filter for filtering Security Hub findings. Each map filter provides the field to check for, the value to check for, and the comparison operator.

Key -> (string)

The key of the map filter. For example, for `ResourceTags` , `Key` identifies the name of the tag. For `UserDefinedFields` , `Key` is the name of the field.

Value -> (string)

The value for the key in the map filter. Filter values are case sensitive. For example, one of the values for a tag called `Department` might be `Security` . If you provide `security` as the filter value, then thereâs no match.

Comparison -> (string)

The condition to apply to the key value when filtering Security Hub findings with a map filter.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, for the `ResourceTags` field, the filter `Department CONTAINS Security` matches findings that include the value `Security` for the `Department` tag. In the same example, a finding with a value of `Security team` for the `Department` tag is a match.
- To search for values that exactly match the filter value, use `EQUALS` . For example, for the `ResourceTags` field, the filter `Department EQUALS Security` matches findings that have the value `Security` for the `Department` tag.

`CONTAINS` and `EQUALS` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Department CONTAINS Security OR Department CONTAINS Finance` match a finding that includes either `Security` , `Finance` , or both values.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, for the `ResourceTags` field, the filter `Department NOT_CONTAINS Finance` matches findings that exclude the value `Finance` for the `Department` tag.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, for the `ResourceTags` field, the filter `Department NOT_EQUALS Finance` matches findings that donât have the value `Finance` for the `Department` tag.

`NOT_CONTAINS` and `NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Department NOT_CONTAINS Security AND Department NOT_CONTAINS Finance` match a finding that excludes both the `Security` and `Finance` values.

`CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât have both an `EQUALS` filter and a `NOT_EQUALS` filter on the same field. Combining filters in this way returns an error.

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

ComplianceStatus -> (list)

The result of a security check. This field is only used for findings generated from controls.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

ComplianceSecurityControlId -> (list)

The security control ID for which a finding was generated. Security control IDs are the same across standards.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

ComplianceAssociatedStandardsId -> (list)

The unique identifier of a standard in which a control is enabled. This field consists of the resource portion of the Amazon Resource Name (ARN) returned for a standard in the [DescribeStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html) API response.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

VerificationState -> (list)

Provides the veracity of a finding.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

WorkflowStatus -> (list)

Provides information about the status of the investigation into a finding.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

RecordState -> (list)

Provides the current state of a finding.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

RelatedFindingsProductArn -> (list)

The ARN for the product that generated a related finding.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

RelatedFindingsId -> (list)

The product-generated identifier for a related finding.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

NoteText -> (list)

The text of a user-defined note thatâs added to a finding.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

NoteUpdatedAt -> (list)

The timestamp of when the note was updated.

For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps) .

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A date filter for querying findings.

Start -> (string)

A timestamp that provides the start date for the date filter.

For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps) .

End -> (string)

A timestamp that provides the end date for the date filter.

For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps) .

DateRange -> (structure)

A date range for the date filter.

Value -> (integer)

A date range value for the date filter.

Unit -> (string)

A date range unit for the date filter.

NoteUpdatedBy -> (list)

The principal that created a note.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

UserDefinedFields -> (list)

A list of user-defined name and value string pairs added to a finding.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A map filter for filtering Security Hub findings. Each map filter provides the field to check for, the value to check for, and the comparison operator.

Key -> (string)

The key of the map filter. For example, for `ResourceTags` , `Key` identifies the name of the tag. For `UserDefinedFields` , `Key` is the name of the field.

Value -> (string)

The value for the key in the map filter. Filter values are case sensitive. For example, one of the values for a tag called `Department` might be `Security` . If you provide `security` as the filter value, then thereâs no match.

Comparison -> (string)

The condition to apply to the key value when filtering Security Hub findings with a map filter.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, for the `ResourceTags` field, the filter `Department CONTAINS Security` matches findings that include the value `Security` for the `Department` tag. In the same example, a finding with a value of `Security team` for the `Department` tag is a match.
- To search for values that exactly match the filter value, use `EQUALS` . For example, for the `ResourceTags` field, the filter `Department EQUALS Security` matches findings that have the value `Security` for the `Department` tag.

`CONTAINS` and `EQUALS` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Department CONTAINS Security OR Department CONTAINS Finance` match a finding that includes either `Security` , `Finance` , or both values.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, for the `ResourceTags` field, the filter `Department NOT_CONTAINS Finance` matches findings that exclude the value `Finance` for the `Department` tag.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, for the `ResourceTags` field, the filter `Department NOT_EQUALS Finance` matches findings that donât have the value `Finance` for the `Department` tag.

`NOT_CONTAINS` and `NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Department NOT_CONTAINS Security AND Department NOT_CONTAINS Finance` match a finding that excludes both the `Security` and `Finance` values.

`CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât have both an `EQUALS` filter and a `NOT_EQUALS` filter on the same field. Combining filters in this way returns an error.

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

ResourceApplicationArn -> (list)

The Amazon Resource Name (ARN) of the application that is related to a finding.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

ResourceApplicationName -> (list)

The name of the application that is related to a finding.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

AwsAccountName -> (list)

The name of the Amazon Web Services account in which a finding was generated.

Array Members: Minimum number of 1 item. Maximum number of 20 items.

(structure)

A string filter for filtering Security Hub findings.

Value -> (string)

The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is `Security Hub` . If you provide `security hub` as the filter value, thereâs no match.

Comparison -> (string)

The condition to apply to a string value when filtering Security Hub findings.

To search for values that have the filter value, use one of the following comparison operators:

- To search for values that include the filter value, use `CONTAINS` . For example, the filter `Title CONTAINS CloudFront` matches findings that have a `Title` that includes the string CloudFront.
- To search for values that exactly match the filter value, use `EQUALS` . For example, the filter `AwsAccountId EQUALS 123456789012` only matches findings that have an account ID of `123456789012` .
- To search for values that start with the filter value, use `PREFIX` . For example, the filter `ResourceRegion PREFIX us` matches findings that have a `ResourceRegion` that starts with `us` . A `ResourceRegion` that starts with a different value, such as `af` , `ap` , or `ca` , doesnât match.

`CONTAINS` , `EQUALS` , and `PREFIX` filters on the same field are joined by `OR` . A finding matches if it matches any one of those filters. For example, the filters `Title CONTAINS CloudFront OR Title CONTAINS CloudWatch` match a finding that includes either `CloudFront` , `CloudWatch` , or both strings in the title.

To search for values that donât have the filter value, use one of the following comparison operators:

- To search for values that exclude the filter value, use `NOT_CONTAINS` . For example, the filter `Title NOT_CONTAINS CloudFront` matches findings that have a `Title` that excludes the string CloudFront.
- To search for values other than the filter value, use `NOT_EQUALS` . For example, the filter `AwsAccountId NOT_EQUALS 123456789012` only matches findings that have an account ID other than `123456789012` .
- To search for values that donât start with the filter value, use `PREFIX_NOT_EQUALS` . For example, the filter `ResourceRegion PREFIX_NOT_EQUALS us` matches findings with a `ResourceRegion` that starts with a value other than `us` .

`NOT_CONTAINS` , `NOT_EQUALS` , and `PREFIX_NOT_EQUALS` filters on the same field are joined by `AND` . A finding matches only if it matches all of those filters. For example, the filters `Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch` match a finding that excludes both `CloudFront` and `CloudWatch` in the title.

You canât have both a `CONTAINS` filter and a `NOT_CONTAINS` filter on the same field. Similarly, you canât provide both an `EQUALS` filter and a `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filter on the same field. Combining filters in this way returns an error. `CONTAINS` filters can only be used with other `CONTAINS` filters. `NOT_CONTAINS` filters can only be used with other `NOT_CONTAINS` filters.

You can combine `PREFIX` filters with `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters for the same field. Security Hub first processes the `PREFIX` filters, and then the `NOT_EQUALS` or `PREFIX_NOT_EQUALS` filters.

For example, for the following filters, Security Hub first identifies findings that have resource types that start with either `AwsIam` or `AwsEc2` . It then excludes findings that have a resource type of `AwsIamPolicy` and findings that have a resource type of `AwsEc2NetworkInterface` .

- `ResourceType PREFIX AwsIam`
- `ResourceType PREFIX AwsEc2`
- `ResourceType NOT_EQUALS AwsIamPolicy`
- `ResourceType NOT_EQUALS AwsEc2NetworkInterface`

`CONTAINS` and `NOT_CONTAINS` operators can be used only with automation rules. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *Security Hub User Guide* .

Actions -> (list)

One or more actions to update finding fields if a finding matches the conditions specified in `Criteria` .

(structure)

One or more actions that Security Hub takes when a finding matches the defined criteria of a rule.

Type -> (string)

Specifies the type of action that Security Hub takes when a finding matches the defined criteria of a rule.

FindingFieldsUpdate -> (structure)

Specifies that the automation rule action is an update to a finding field.

Note -> (structure)

The updated note.

Text -> (string)

The updated note text.

UpdatedBy -> (string)

The principal that updated the note.

Severity -> (structure)

Updates to the severity information for a finding.

Normalized -> (integer)

The normalized severity for the finding. This attribute is to be deprecated in favor of `Label` .

If you provide `Normalized` and donât provide `Label` , `Label` is set automatically as follows.

- 0 - `INFORMATIONAL`
- 1â39 - `LOW`
- 40â69 - `MEDIUM`
- 70â89 - `HIGH`
- 90â100 - `CRITICAL`

Product -> (double)

The native severity as defined by the Amazon Web Services service or integrated partner product that generated the finding.

Label -> (string)

The severity value of the finding. The allowed values are the following.

- `INFORMATIONAL` - No issue was found.
- `LOW` - The issue does not require action on its own.
- `MEDIUM` - The issue must be addressed but not urgently.
- `HIGH` - The issue must be addressed as a priority.
- `CRITICAL` - The issue must be remediated immediately to avoid it escalating.

VerificationState -> (string)

The rule action updates the `VerificationState` field of a finding.

Confidence -> (integer)

The rule action updates the `Confidence` field of a finding.

Criticality -> (integer)

The rule action updates the `Criticality` field of a finding.

Types -> (list)

The rule action updates the `Types` field of a finding.

(string)

UserDefinedFields -> (map)

The rule action updates the `UserDefinedFields` field of a finding.

key -> (string)

value -> (string)

Workflow -> (structure)

Used to update information about the investigation into the finding.

Status -> (string)

The status of the investigation into the finding. The workflow status is specific to an individual finding. It does not affect the generation of new findings. For example, setting the workflow status to `SUPPRESSED` or `RESOLVED` does not prevent a new finding for the same issue.

The allowed values are the following.

- `NEW` - The initial state of a finding, before it is reviewed. Security Hub also resets `WorkFlowStatus` from `NOTIFIED` or `RESOLVED` to `NEW` in the following cases:
- The record state changes from `ARCHIVED` to `ACTIVE` .
- The compliance status changes from `PASSED` to either `WARNING` , `FAILED` , or `NOT_AVAILABLE` .
- `NOTIFIED` - Indicates that you notified the resource owner about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.
- `RESOLVED` - The finding was reviewed and remediated and is now considered resolved.
- `SUPPRESSED` - Indicates that you reviewed the finding and donât believe that any action is needed. The finding is no longer updated.

RelatedFindings -> (list)

The rule action updates the `RelatedFindings` field of a finding.

(structure)

Details about a related finding.

ProductArn -> (string)

The ARN of the product that generated a related finding.

Id -> (string)

The product-generated identifier for a related finding.

JSON Syntax:

```
[
  {
    "RuleArn": "string",
    "RuleStatus": "ENABLED"|"DISABLED",
    "RuleOrder": integer,
    "Description": "string",
    "RuleName": "string",
    "IsTerminal": true|false,
    "Criteria": {
      "ProductArn": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "AwsAccountId": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "Id": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "GeneratorId": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "Type": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "FirstObservedAt": [
        {
          "Start": "string",
          "End": "string",
          "DateRange": {
            "Value": integer,
            "Unit": "DAYS"
          }
        }
        ...
      ],
      "LastObservedAt": [
        {
          "Start": "string",
          "End": "string",
          "DateRange": {
            "Value": integer,
            "Unit": "DAYS"
          }
        }
        ...
      ],
      "CreatedAt": [
        {
          "Start": "string",
          "End": "string",
          "DateRange": {
            "Value": integer,
            "Unit": "DAYS"
          }
        }
        ...
      ],
      "UpdatedAt": [
        {
          "Start": "string",
          "End": "string",
          "DateRange": {
            "Value": integer,
            "Unit": "DAYS"
          }
        }
        ...
      ],
      "Confidence": [
        {
          "Gte": double,
          "Lte": double,
          "Eq": double,
          "Gt": double,
          "Lt": double
        }
        ...
      ],
      "Criticality": [
        {
          "Gte": double,
          "Lte": double,
          "Eq": double,
          "Gt": double,
          "Lt": double
        }
        ...
      ],
      "Title": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "Description": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "SourceUrl": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "ProductName": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "CompanyName": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "SeverityLabel": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "ResourceType": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "ResourceId": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "ResourcePartition": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "ResourceRegion": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "ResourceTags": [
        {
          "Key": "string",
          "Value": "string",
          "Comparison": "EQUALS"|"NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "ResourceDetailsOther": [
        {
          "Key": "string",
          "Value": "string",
          "Comparison": "EQUALS"|"NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "ComplianceStatus": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "ComplianceSecurityControlId": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "ComplianceAssociatedStandardsId": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "VerificationState": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "WorkflowStatus": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "RecordState": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "RelatedFindingsProductArn": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "RelatedFindingsId": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "NoteText": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "NoteUpdatedAt": [
        {
          "Start": "string",
          "End": "string",
          "DateRange": {
            "Value": integer,
            "Unit": "DAYS"
          }
        }
        ...
      ],
      "NoteUpdatedBy": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "UserDefinedFields": [
        {
          "Key": "string",
          "Value": "string",
          "Comparison": "EQUALS"|"NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "ResourceApplicationArn": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "ResourceApplicationName": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ],
      "AwsAccountName": [
        {
          "Value": "string",
          "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"
        }
        ...
      ]
    },
    "Actions": [
      {
        "Type": "FINDING_FIELDS_UPDATE",
        "FindingFieldsUpdate": {
          "Note": {
            "Text": "string",
            "UpdatedBy": "string"
          },
          "Severity": {
            "Normalized": integer,
            "Product": double,
            "Label": "INFORMATIONAL"|"LOW"|"MEDIUM"|"HIGH"|"CRITICAL"
          },
          "VerificationState": "UNKNOWN"|"TRUE_POSITIVE"|"FALSE_POSITIVE"|"BENIGN_POSITIVE",
          "Confidence": integer,
          "Criticality": integer,
          "Types": ["string", ...],
          "UserDefinedFields": {"string": "string"
            ...},
          "Workflow": {
            "Status": "NEW"|"NOTIFIED"|"RESOLVED"|"SUPPRESSED"
          },
          "RelatedFindings": [
            {
              "ProductArn": "string",
              "Id": "string"
            }
            ...
          ]
        }
      }
      ...
    ]
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

**To update automation rules**

The following `batch-update-automation-rules` example updates the specified automation rule. You can update one or more rules with a single command. Only the Security Hub administrator account can run this command.

```
aws securityhub batch-update-automation-rules \
    --update-automation-rules-request-items '[ \
        { \
            "Actions": [{ \
                "Type": "FINDING_FIELDS_UPDATE", \
                "FindingFieldsUpdate": { \
                    "Note": { \
                        "Text": "Known issue that is a risk", \
                        "UpdatedBy": "sechub-automation" \
                    }, \
                    "Workflow": { \
                        "Status": "NEW" \
                    } \
                } \
            }], \
            "Criteria": { \
                "SeverityLabel": [{ \
                    "Value": "LOW", \
                    "Comparison": "EQUALS" \
                }] \
            }, \
            "RuleArn": "arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", \
            "RuleOrder": 1, \
            "RuleStatus": "DISABLED" \
        } \
    ]'
```

Output:

```
{
    "ProcessedAutomationRules": [
        "arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    ],
    "UnprocessedAutomationRules": []
}
```

For more information, see [Editing automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html#edit-automation-rules) in the *AWS Security Hub User Guide*.

## Output

ProcessedAutomationRules -> (list)

A list of properly processed rule ARNs.

(string)

UnprocessedAutomationRules -> (list)

A list of objects containing `RuleArn` , `ErrorCode` , and `ErrorMessage` . This parameter tells you which automation rules the request didnât update and why.

(structure)

A list of objects containing `RuleArn` , `ErrorCode` , and `ErrorMessage` . This parameter tells you which automation rules the request didnât process and why.

RuleArn -> (string)

The Amazon Resource Name (ARN) for the unprocessed automation rule.

ErrorCode -> (integer)

The error code associated with the unprocessed automation rule.

ErrorMessage -> (string)

An error message describing why a request didnât process a specific rule.