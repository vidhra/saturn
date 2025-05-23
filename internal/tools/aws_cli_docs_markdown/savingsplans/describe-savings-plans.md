# describe-savings-plansÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/savingsplans/describe-savings-plans.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/savingsplans/describe-savings-plans.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [savingsplans](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/savingsplans/index.html#cli-aws-savingsplans) ]

# describe-savings-plans

## Description

Describes the specified Savings Plans.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/savingsplans-2019-06-28/DescribeSavingsPlans)

## Synopsis

```
describe-savings-plans
[--savings-plan-arns <value>]
[--savings-plan-ids <value>]
[--next-token <value>]
[--max-results <value>]
[--states <value>]
[--filters <value>]
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

`--savings-plan-arns` (list)

The Amazon Resource Names (ARN) of the Savings Plans.

(string)

Syntax:

```
"string" "string" ...
```

`--savings-plan-ids` (list)

The IDs of the Savings Plans.

(string)

Syntax:

```
"string" "string" ...
```

`--next-token` (string)

The token for the next page of results.

`--max-results` (integer)

The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.

`--states` (list)

The current states of the Savings Plans.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  payment-pending
  payment-failed
  active
  retired
  queued
  queued-deleted
  pending-return
  returned
```

`--filters` (list)

The filters.

(structure)

Information about a Savings Plan filter.

name -> (string)

The filter name.

values -> (list)

The filter value.

(string)

Shorthand Syntax:

```
name=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "region"|"ec2-instance-family"|"commitment"|"upfront"|"term"|"savings-plan-type"|"payment-option"|"start"|"end",
    "values": ["string", ...]
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

## Output

savingsPlans -> (list)

Information about the Savings Plans.

(structure)

Information about a Savings Plan.

offeringId -> (string)

The ID of the offering.

savingsPlanId -> (string)

The ID of the Savings Plan.

savingsPlanArn -> (string)

The Amazon Resource Name (ARN) of the Savings Plan.

description -> (string)

The description.

start -> (string)

The start time.

end -> (string)

The end time.

state -> (string)

The current state.

region -> (string)

The Amazon Web Services Region.

ec2InstanceFamily -> (string)

The EC2 instance family.

savingsPlanType -> (string)

The plan type.

paymentOption -> (string)

The payment option.

productTypes -> (list)

The product types.

(string)

currency -> (string)

The currency.

commitment -> (string)

The hourly commitment amount in the specified currency.

upfrontPaymentAmount -> (string)

The up-front payment amount.

recurringPaymentAmount -> (string)

The recurring payment amount.

termDurationInSeconds -> (long)

The duration of the term, in seconds.

tags -> (map)

One or more tags.

key -> (string)

value -> (string)

returnableUntil -> (string)

The time until when a return for the Savings Plan can be requested. If the Savings Plan is not returnable, the field reflects the Savings Plan start time.

nextToken -> (string)

The token to use to retrieve the next page of results. This value is null when there are no more results to return.