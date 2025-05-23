# list-price-listsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pricing/list-price-lists.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pricing/list-price-lists.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pricing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pricing/index.html#cli-aws-pricing) ]

# list-price-lists

## Description

- **This feature is in preview release and is subject to change. Your use of Amazon Web Services Price List API is subject to the Beta Service Participation terms of the `Amazon Web Services Service Terms <https://aws.amazon.com/service-terms/>`__ (Section 1.10).** *

This returns a list of Price List references that the requester if authorized to view, given a `ServiceCode` , `CurrencyCode` , and an `EffectiveDate` . Use without a `RegionCode` filter to list Price List references from all available Amazon Web Services Regions. Use with a `RegionCode` filter to get the Price List reference thatâs specific to a specific Amazon Web Services Region. You can use the `PriceListArn` from the response to get your preferred Price List files through the [GetPriceListFileUrl](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetPriceListFileUrl.html) API.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pricing-2017-10-15/ListPriceLists)

`list-price-lists` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `PriceLists`

## Synopsis

```
list-price-lists
--service-code <value>
--effective-date <value>
[--region-code <value>]
--currency-code <value>
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

`--service-code` (string)

The service code or the Savings Plan service code for the attributes that you want to retrieve. For example, to get the list of applicable Amazon EC2 price lists, use `AmazonEC2` . For a full list of service codes containing On-Demand and Reserved Instance (RI) pricing, use the [DescribeServices](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_DescribeServices.html#awscostmanagement-pricing_DescribeServices-request-FormatVersion) API.

To retrieve the Reserved Instance and Compute Savings Plan price lists, use `ComputeSavingsPlans` .

To retrieve Machine Learning Savings Plans price lists, use `MachineLearningSavingsPlans` .

`--effective-date` (timestamp)

The date that the Price List file prices are effective from.

`--region-code` (string)

This is used to filter the Price List by Amazon Web Services Region. For example, to get the price list only for the `US East (N. Virginia)` Region, use `us-east-1` . If nothing is specified, you retrieve price lists for all applicable Regions. The available `RegionCode` list can be retrieved from [GetAttributeValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetAttributeValues.html) API.

`--currency-code` (string)

The three alphabetical character ISO-4217 currency code that the Price List files are denominated in.

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

PriceLists -> (list)

The type of price list references that match your request.

(structure)

- **This feature is in preview release and is subject to change. Your use of Amazon Web Services Price List API is subject to the Beta Service Participation terms of the `Amazon Web Services Service Terms <https://aws.amazon.com/service-terms/>`__ (Section 1.10).** *

This is the type of price list references that match your request.

PriceListArn -> (string)

The unique identifier that maps to where your Price List files are located. `PriceListArn` can be obtained from the ` `ListPriceList` [https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists).html`__ response.

RegionCode -> (string)

This is used to filter the Price List by Amazon Web Services Region. For example, to get the price list only for the `US East (N. Virginia)` Region, use `us-east-1` . If nothing is specified, you retrieve price lists for all applicable Regions. The available `RegionCode` list can be retrieved from ` `GetAttributeValues` [https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetAttributeValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetAttributeValues).html`__ API.

CurrencyCode -> (string)

The three alphabetical character ISO-4217 currency code the Price List files are denominated in.

FileFormats -> (list)

The format you want to retrieve your Price List files. The `FileFormat` can be obtained from the ` `ListPriceList` [https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists).html`__ response.

(string)

NextToken -> (string)

The pagination token that indicates the next set of results to retrieve.