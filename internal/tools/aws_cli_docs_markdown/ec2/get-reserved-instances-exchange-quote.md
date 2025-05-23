# get-reserved-instances-exchange-quoteÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-reserved-instances-exchange-quote.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-reserved-instances-exchange-quote.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# get-reserved-instances-exchange-quote

## Description

Returns a quote and exchange information for exchanging one or more specified Convertible Reserved Instances for a new Convertible Reserved Instance. If the exchange cannot be performed, the reason is returned in the response. Use  AcceptReservedInstancesExchangeQuote to perform the exchange.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/GetReservedInstancesExchangeQuote)

## Synopsis

```
get-reserved-instances-exchange-quote
[--dry-run | --no-dry-run]
--reserved-instance-ids <value>
[--target-configurations <value>]
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

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--reserved-instance-ids` (list)

The IDs of the Convertible Reserved Instances to exchange.

(string)

Syntax:

```
"string" "string" ...
```

`--target-configurations` (list)

The configuration of the target Convertible Reserved Instance to exchange for your current Convertible Reserved Instances.

(structure)

Details about the target configuration.

InstanceCount -> (integer)

The number of instances the Convertible Reserved Instance offering can be applied to. This parameter is reserved and cannot be specified in a request

OfferingId -> (string)

The Convertible Reserved Instance offering ID.

Shorthand Syntax:

```
InstanceCount=integer,OfferingId=string ...
```

JSON Syntax:

```
[
  {
    "InstanceCount": integer,
    "OfferingId": "string"
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

**To get a quote for exchanging a Convertible Reserved Instance**

This example gets the exchange information for the specified Convertible Reserved Instances.

Command:

```
aws ec2 get-reserved-instances-exchange-quote --reserved-instance-ids 7b8750c3-397e-4da4-bbcb-a45ebexample --target-configurations OfferingId=6fea5434-b379-434c-b07b-a7abexample
```

Output:

```
{
  "CurrencyCode": "USD",
  "ReservedInstanceValueSet": [
      {
          "ReservedInstanceId": "7b8750c3-397e-4da4-bbcb-a45ebexample",
          "ReservationValue": {
              "RemainingUpfrontValue": "0.000000",
              "HourlyPrice": "0.027800",
              "RemainingTotalValue": "730.556200"
          }
      }
  ],
  "PaymentDue": "424.983828",
  "TargetConfigurationValueSet": [
      {
          "TargetConfiguration": {
              "InstanceCount": 5,
              "OfferingId": "6fea5434-b379-434c-b07b-a7abexample"
          },
          "ReservationValue": {
              "RemainingUpfrontValue": "424.983828",
              "HourlyPrice": "0.016000",
              "RemainingTotalValue": "845.447828"
          }
      }
  ],
  "IsValidExchange": true,
  "OutputReservedInstancesWillExpireAt": "2020-10-01T13:03:39Z",
  "ReservedInstanceValueRollup": {
      "RemainingUpfrontValue": "0.000000",
      "HourlyPrice": "0.027800",
      "RemainingTotalValue": "730.556200"
  },
  "TargetConfigurationValueRollup": {
      "RemainingUpfrontValue": "424.983828",
      "HourlyPrice": "0.016000",
      "RemainingTotalValue": "845.447828"
  }
}
```

## Output

CurrencyCode -> (string)

The currency of the transaction.

IsValidExchange -> (boolean)

If `true` , the exchange is valid. If `false` , the exchange cannot be completed.

OutputReservedInstancesWillExpireAt -> (timestamp)

The new end date of the reservation term.

PaymentDue -> (string)

The total true upfront charge for the exchange.

ReservedInstanceValueRollup -> (structure)

The cost associated with the Reserved Instance.

HourlyPrice -> (string)

The hourly rate of the reservation.

RemainingTotalValue -> (string)

The balance of the total value (the sum of remainingUpfrontValue + hourlyPrice * number of hours remaining).

RemainingUpfrontValue -> (string)

The remaining upfront cost of the reservation.

ReservedInstanceValueSet -> (list)

The configuration of your Convertible Reserved Instances.

(structure)

The total value of the Convertible Reserved Instance.

ReservationValue -> (structure)

The total value of the Convertible Reserved Instance that you are exchanging.

HourlyPrice -> (string)

The hourly rate of the reservation.

RemainingTotalValue -> (string)

The balance of the total value (the sum of remainingUpfrontValue + hourlyPrice * number of hours remaining).

RemainingUpfrontValue -> (string)

The remaining upfront cost of the reservation.

ReservedInstanceId -> (string)

The ID of the Convertible Reserved Instance that you are exchanging.

TargetConfigurationValueRollup -> (structure)

The cost associated with the Reserved Instance.

HourlyPrice -> (string)

The hourly rate of the reservation.

RemainingTotalValue -> (string)

The balance of the total value (the sum of remainingUpfrontValue + hourlyPrice * number of hours remaining).

RemainingUpfrontValue -> (string)

The remaining upfront cost of the reservation.

TargetConfigurationValueSet -> (list)

The values of the target Convertible Reserved Instances.

(structure)

The total value of the new Convertible Reserved Instances.

ReservationValue -> (structure)

The total value of the Convertible Reserved Instances that make up the exchange. This is the sum of the list value, remaining upfront price, and additional upfront cost of the exchange.

HourlyPrice -> (string)

The hourly rate of the reservation.

RemainingTotalValue -> (string)

The balance of the total value (the sum of remainingUpfrontValue + hourlyPrice * number of hours remaining).

RemainingUpfrontValue -> (string)

The remaining upfront cost of the reservation.

TargetConfiguration -> (structure)

The configuration of the Convertible Reserved Instances that make up the exchange.

InstanceCount -> (integer)

The number of instances the Convertible Reserved Instance offering can be applied to. This parameter is reserved and cannot be specified in a request

OfferingId -> (string)

The ID of the Convertible Reserved Instance offering.

ValidationFailureReason -> (string)

Describes the reason why the exchange cannot be completed.