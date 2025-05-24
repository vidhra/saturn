# create-bill-estimateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-pricing-calculator/create-bill-estimate.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-pricing-calculator/create-bill-estimate.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bcm-pricing-calculator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-pricing-calculator/index.html#cli-aws-bcm-pricing-calculator) ]

# create-bill-estimate

## Description

Create a Bill estimate from a Bill scenario. In the Bill scenario you can model usage addition, usage changes, and usage removal. You can also model commitment addition and commitment removal. After all changes in a Bill scenario is made satisfactorily, you can call this API with a Bill scenario ID to generate the Bill estimate. Bill estimate calculates the pre-tax cost for your consolidated billing family, incorporating all modeled usage and commitments alongside existing usage and commitments from your most recent completed anniversary bill, with any applicable discounts applied.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bcm-pricing-calculator-2024-06-19/CreateBillEstimate)

## Synopsis

```
create-bill-estimate
--bill-scenario-id <value>
--name <value>
[--client-token <value>]
[--tags <value>]
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

`--bill-scenario-id` (string)

The ID of the Bill Scenario for which you want to create a Bill estimate.

`--name` (string)

The name of the Bill estimate that will be created. Names must be unique for an account.

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

`--tags` (map)

An optional list of tags to associate with the specified BillEstimate. You can use resource tags to control access to your BillEstimate using IAM policies. Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags:

- Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for Amazon Web Services.
- The maximum length of a key is 128 characters.
- The maximum length of a value is 256 characters.
- Keys and values can only contain alphanumeric characters, spaces, and any of the following: `_.:/=+@-` .
- Keys and values are case sensitive.
- Keys and values are trimmed for any leading or trailing whitespaces.
- Donât use `aws:` as a prefix for your keys. This prefix is reserved for Amazon Web Services.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

id -> (string)

The unique identifier of your newly created Bill estimate.

name -> (string)

The name of your newly created Bill estimate.

status -> (string)

The status of your newly created Bill estimate. Bill estimate creation can take anywhere between 8 to 12 hours. The status will allow you to identify when the Bill estimate is complete or has failed.

failureMessage -> (string)

This attribute provides the reason if a Bill estimate result generation fails.

billInterval -> (structure)

The bill month start and end timestamp that was used to create the Bill estimate. This is set to the last complete anniversary bill month start and end timestamp.

start -> (timestamp)

The start date and time of the interval.

end -> (timestamp)

The end date and time of the interval.

costSummary -> (structure)

Returns summary-level cost information once a Bill estimate is successfully generated. This summary includes: 1) the total cost difference, showing the pre-tax cost change for the consolidated billing family between the completed anniversary bill and the estimated bill, and 2) total cost differences per service, detailing the pre-tax cost of each service, comparing the completed anniversary bill to the estimated bill on a per-service basis.

totalCostDifference -> (structure)

The total difference in cost between the estimated and historical costs.

historicalCost -> (structure)

The historical cost amount.

amount -> (double)

The numeric value of the cost.

currency -> (string)

The currency code for the cost amount.

estimatedCost -> (structure)

The estimated cost amount.

amount -> (double)

The numeric value of the cost.

currency -> (string)

The currency code for the cost amount.

serviceCostDifferences -> (map)

A breakdown of cost differences by Amazon Web Services service.

key -> (string)

value -> (structure)

Represents the difference between historical and estimated costs.

historicalCost -> (structure)

The historical cost amount.

amount -> (double)

The numeric value of the cost.

currency -> (string)

The currency code for the cost amount.

estimatedCost -> (structure)

The estimated cost amount.

amount -> (double)

The numeric value of the cost.

currency -> (string)

The currency code for the cost amount.

createdAt -> (timestamp)

The timestamp of when the Bill estimate create process was started (not when it successfully completed or failed).

expiresAt -> (timestamp)

The timestamp of when the Bill estimate will expire. A Bill estimate becomes inaccessible after expiration.