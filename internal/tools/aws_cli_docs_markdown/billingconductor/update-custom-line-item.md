# update-custom-line-itemÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/update-custom-line-item.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/update-custom-line-item.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [billingconductor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/index.html#cli-aws-billingconductor) ]

# update-custom-line-item

## Description

Update an existing custom line item in the current or previous billing period.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/billingconductor-2021-07-30/UpdateCustomLineItem)

## Synopsis

```
update-custom-line-item
--arn <value>
[--name <value>]
[--description <value>]
[--charge-details <value>]
[--billing-period-range <value>]
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

`--arn` (string)

The ARN of the custom line item to be updated.

`--name` (string)

The new name for the custom line item.

`--description` (string)

The new line item description of the custom line item.

`--charge-details` (structure)

A `ListCustomLineItemChargeDetails` containing the new charge details for the custom line item.

Flat -> (structure)

An `UpdateCustomLineItemFlatChargeDetails` that describes the new charge details of a flat custom line item.

ChargeValue -> (double)

The custom line itemâs new fixed charge value in USD.

Percentage -> (structure)

An `UpdateCustomLineItemPercentageChargeDetails` that describes the new charge details of a percentage custom line item.

PercentageValue -> (double)

The custom line itemâs new percentage value. This will be multiplied against the combined value of its associated resources to determine its charge value.

LineItemFilters -> (list)

A representation of the line item filter.

(structure)

A representation of the line item filter for your custom line item. You can use line item filters to include or exclude specific resource values from the billing groupâs total cost. For example, if you create a custom line item and you want to filter out a value, such as Savings Plan discounts, you can update `LineItemFilter` to exclude it.

Attribute -> (string)

The attribute of the line item filter. This specifies what attribute that you can filter on.

MatchOption -> (string)

The match criteria of the line item filter. This parameter specifies whether not to include the resource value from the billing group total cost.

Values -> (list)

The values of the line item filter. This specifies the values to filter on. Currently, you can only exclude Savings Plan discounts.

(string)

JSON Syntax:

```
{
  "Flat": {
    "ChargeValue": double
  },
  "Percentage": {
    "PercentageValue": double
  },
  "LineItemFilters": [
    {
      "Attribute": "LINE_ITEM_TYPE",
      "MatchOption": "NOT_EQUAL",
      "Values": ["SAVINGS_PLAN_NEGATION", ...]
    }
    ...
  ]
}
```

`--billing-period-range` (structure)

The billing period range in which the custom line item request will be applied.

InclusiveStartBillingPeriod -> (string)

The inclusive start billing period that defines a billing period range where a custom line is applied.

ExclusiveEndBillingPeriod -> (string)

The inclusive end billing period that defines a billing period range where a custom line is applied.

Shorthand Syntax:

```
InclusiveStartBillingPeriod=string,ExclusiveEndBillingPeriod=string
```

JSON Syntax:

```
{
  "InclusiveStartBillingPeriod": "string",
  "ExclusiveEndBillingPeriod": "string"
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

Arn -> (string)

The ARN of the successfully updated custom line item.

BillingGroupArn -> (string)

The ARN of the billing group that the custom line item is applied to.

Name -> (string)

The name of the successfully updated custom line item.

Description -> (string)

The description of the successfully updated custom line item.

ChargeDetails -> (structure)

A `ListCustomLineItemChargeDetails` containing the charge details of the successfully updated custom line item.

Flat -> (structure)

A `ListCustomLineItemFlatChargeDetails` that describes the charge details of a flat custom line item.

ChargeValue -> (double)

The custom line itemâs fixed charge value in USD.

Percentage -> (structure)

A `ListCustomLineItemPercentageChargeDetails` that describes the charge details of a percentage custom line item.

PercentageValue -> (double)

The custom line itemâs percentage value. This will be multiplied against the combined value of its associated resources to determine its charge value.

Type -> (string)

The type of the custom line item that indicates whether the charge is a `fee` or `credit` .

LineItemFilters -> (list)

A representation of the line item filter.

(structure)

A representation of the line item filter for your custom line item. You can use line item filters to include or exclude specific resource values from the billing groupâs total cost. For example, if you create a custom line item and you want to filter out a value, such as Savings Plan discounts, you can update `LineItemFilter` to exclude it.

Attribute -> (string)

The attribute of the line item filter. This specifies what attribute that you can filter on.

MatchOption -> (string)

The match criteria of the line item filter. This parameter specifies whether not to include the resource value from the billing group total cost.

Values -> (list)

The values of the line item filter. This specifies the values to filter on. Currently, you can only exclude Savings Plan discounts.

(string)

LastModifiedTime -> (long)

The most recent time when the custom line item was modified.

AssociationSize -> (long)

The number of resources that are associated to the custom line item.