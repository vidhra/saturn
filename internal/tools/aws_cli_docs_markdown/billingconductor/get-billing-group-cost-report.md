# get-billing-group-cost-reportÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/get-billing-group-cost-report.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/get-billing-group-cost-report.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [billingconductor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/billingconductor/index.html#cli-aws-billingconductor) ]

# get-billing-group-cost-report

## Description

Retrieves the margin summary report, which includes the Amazon Web Services cost and charged amount (pro forma cost) by Amazon Web Service for a specific billing group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/billingconductor-2021-07-30/GetBillingGroupCostReport)

## Synopsis

```
get-billing-group-cost-report
--arn <value>
[--billing-period-range <value>]
[--group-by <value>]
[--max-results <value>]
[--next-token <value>]
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

The Amazon Resource Number (ARN) that uniquely identifies the billing group.

`--billing-period-range` (structure)

A time range for which the margin summary is effective. You can specify up to 12 months.

InclusiveStartBillingPeriod -> (string)

The inclusive start billing period that defines a billing period range for the margin summary.

ExclusiveEndBillingPeriod -> (string)

The exclusive end billing period that defines a billing period range for the margin summary. For example, if you choose a billing period that starts in October 2023 and ends in December 2023, the margin summary will only include data from October 2023 and November 2023.

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

`--group-by` (list)

A list of strings that specify the attributes that are used to break down costs in the margin summary reports for the billing group. For example, you can view your costs by the Amazon Web Service name or the billing period.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  PRODUCT_NAME
  BILLING_PERIOD
```

`--max-results` (integer)

The maximum number of margin summary reports to retrieve.

`--next-token` (string)

The pagination token used on subsequent calls to get reports.

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

BillingGroupCostReportResults -> (list)

The list of margin summary reports.

(structure)

A paginated call to retrieve a list of summary reports of actual Amazon Web Services charges and the calculated Amazon Web Services charges, broken down by attributes.

Arn -> (string)

The Amazon Resource Number (ARN) that uniquely identifies the billing group.

AWSCost -> (string)

The actual Amazon Web Services charges for the billing group.

ProformaCost -> (string)

The hypothetical Amazon Web Services charges based on the associated pricing plan of a billing group.

Margin -> (string)

The billing group margin.

MarginPercentage -> (string)

The percentage of the billing group margin.

Currency -> (string)

The displayed currency.

Attributes -> (list)

The list of key-value pairs that represent the attributes by which the `BillingGroupCostReportResults` are grouped. For example, if you want the Amazon S3 service-level breakdown of a billing group for November 2023, the attributes list will contain a key-value pair of `"PRODUCT_NAME"` and `"S3"` and a key-value pair of `"BILLING_PERIOD"` and `"Nov 2023"` .

(structure)

The key-value pair that represents the attribute by which the `BillingGroupCostReportResults` are grouped. For example, if you want a service-level breakdown for Amazon Simple Storage Service (Amazon S3) of the billing group, the attribute will be a key-value pair of `"PRODUCT_NAME"` and `"S3"` .

Key -> (string)

The key in a key-value pair that describes the margin summary.

Value -> (string)

The value in a key-value pair that describes the margin summary.

NextToken -> (string)

The pagination token used on subsequent calls to get reports.