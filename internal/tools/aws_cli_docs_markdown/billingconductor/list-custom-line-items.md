# list-custom-line-itemsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/list-custom-line-items.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/list-custom-line-items.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [billingconductor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/index.html#cli-aws-billingconductor) ]

# list-custom-line-items

## Description

A paginated call to get a list of all custom line items (FFLIs) for the given billing period. If you donât provide a billing period, the current billing period is used.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/billingconductor-2021-07-30/ListCustomLineItems)

`list-custom-line-items` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `CustomLineItems`

## Synopsis

```
list-custom-line-items
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

The preferred billing period to get custom line items (FFLIs).

`--filters` (structure)

A `ListCustomLineItemsFilter` that specifies the custom line item names and/or billing group Amazon Resource Names (ARNs) to retrieve FFLI information.

Names -> (list)

A list of custom line items to retrieve information.

(string)

BillingGroups -> (list)

The billing group Amazon Resource Names (ARNs) to retrieve information.

(string)

Arns -> (list)

A list of custom line item ARNs to retrieve information.

(string)

AccountIds -> (list)

The Amazon Web Services accounts in which this custom line item will be applied to.

(string)

Shorthand Syntax:

```
Names=string,string,BillingGroups=string,string,Arns=string,string,AccountIds=string,string
```

JSON Syntax:

```
{
  "Names": ["string", ...],
  "BillingGroups": ["string", ...],
  "Arns": ["string", ...],
  "AccountIds": ["string", ...]
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

CustomLineItems -> (list)

A list of `FreeFormLineItemListElements` received.

(structure)

A representation of a custom line item.

Arn -> (string)

The Amazon Resource Names (ARNs) for custom line items.

Name -> (string)

The custom line itemâs name.

ChargeDetails -> (structure)

A `ListCustomLineItemChargeDetails` that describes the charge details of a custom line item.

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

CurrencyCode -> (string)

The custom line itemâs charge value currency. Only one of the valid values can be used.

Description -> (string)

The custom line itemâs description. This is shown on the Bills page in association with the charge value.

ProductCode -> (string)

The product code thatâs associated with the custom line item.

BillingGroupArn -> (string)

The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.

CreationTime -> (long)

The time created.

LastModifiedTime -> (long)

The most recent time when the custom line item was modified.

AssociationSize -> (long)

The number of resources that are associated to the custom line item.

AccountId -> (string)

The Amazon Web Services account in which this custom line item will be applied to.

NextToken -> (string)

The pagination token thatâs used on subsequent calls to get custom line items (FFLIs).