# list-pricing-rulesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/list-pricing-rules.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/list-pricing-rules.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [billingconductor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/index.html#cli-aws-billingconductor) ]

# list-pricing-rules

## Description

Describes a pricing rule that can be associated to a pricing plan, or set of pricing plans.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/billingconductor-2021-07-30/ListPricingRules)

`list-pricing-rules` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `PricingRules`

## Synopsis

```
list-pricing-rules
[--billing-period <value>]
[--filters <value>]
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

`--billing-period` (string)

The preferred billing period to get the pricing plan.

`--filters` (structure)

A `DescribePricingRuleFilter` that specifies the Amazon Resource Name (ARNs) of pricing rules to retrieve pricing rules information.

Arns -> (list)

A list containing the pricing rule Amazon Resource Names (ARNs) to include in the API response.

(string)

Shorthand Syntax:

```
Arns=string,string
```

JSON Syntax:

```
{
  "Arns": ["string", ...]
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

BillingPeriod -> (string)

The billing period for which the described pricing rules are applicable.

PricingRules -> (list)

A list containing the described pricing rules.

(structure)

A representation of a pricing rule.

Name -> (string)

The name of a pricing rule.

Arn -> (string)

The Amazon Resource Name (ARN) used to uniquely identify a pricing rule.

Description -> (string)

The pricing rule description.

Scope -> (string)

The scope of pricing rule that indicates if it is globally applicable, or if it is service-specific.

Type -> (string)

The type of pricing rule.

ModifierPercentage -> (double)

A percentage modifier applied on the public pricing rates.

Service -> (string)

If the `Scope` attribute is `SERVICE` , this attribute indicates which service the `PricingRule` is applicable for.

AssociatedPricingPlanCount -> (long)

The pricing plans count that this pricing rule is associated with.

CreationTime -> (long)

The time when the pricing rule was created.

LastModifiedTime -> (long)

The most recent time when the pricing rule was modified.

BillingEntity -> (string)

The seller of services provided by Amazon Web Services, their affiliates, or third-party providers selling services via Amazon Web Services Marketplace.

Tiering -> (structure)

The set of tiering configurations for the pricing rule.

FreeTier -> (structure)

The possible Amazon Web Services Free Tier configurations.

Activated -> (boolean)

Activate or deactivate Amazon Web Services Free Tier application.

UsageType -> (string)

Usage type is the unit that each service uses to measure the usage of a specific type of resource.

If the `Scope` attribute is set to `SKU` , this attribute indicates which usage type the `PricingRule` is modifying. For example, `USW2-BoxUsage:m2.2xlarge` describes an``M2 High Memory Double Extra Large`` instance in the US West (Oregon) Region. `</p>`

Operation -> (string)

Operation is the specific Amazon Web Services action covered by this line item. This describes the specific usage of the line item.

If the `Scope` attribute is set to `SKU` , this attribute indicates which operation the `PricingRule` is modifying. For example, a value of `RunInstances:0202` indicates the operation of running an Amazon EC2 instance.

NextToken -> (string)

The pagination token thatâs used on subsequent calls to get pricing rules.