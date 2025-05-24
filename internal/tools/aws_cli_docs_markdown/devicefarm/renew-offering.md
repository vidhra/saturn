# renew-offeringÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/renew-offering.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/renew-offering.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [devicefarm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/index.html#cli-aws-devicefarm) ]

# renew-offering

## Description

Explicitly sets the quantity of devices to renew for an offering, starting from the `effectiveDate` of the next period. The API returns a `NotEligible` error if the user is not permitted to invoke the operation. If you must be able to invoke this operation, contact [aws-devicefarm-support@amazon.com](mailto:aws-devicefarm-support%40amazon.com) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/RenewOffering)

## Synopsis

```
renew-offering
--offering-id <value>
--quantity <value>
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

`--offering-id` (string)

The ID of a request to renew an offering.

`--quantity` (integer)

The quantity requested in an offering renewal.

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

offeringTransaction -> (structure)

Represents the status of the offering transaction for the renewal.

offeringStatus -> (structure)

The status of an offering transaction.

type -> (string)

The type specified for the offering status.

offering -> (structure)

Represents the metadata of an offering status.

id -> (string)

The ID that corresponds to a device offering.

description -> (string)

A string that describes the offering.

type -> (string)

The type of offering (for example, `RECURRING` ) for a device.

platform -> (string)

The platform of the device (for example, `ANDROID` or `IOS` ).

recurringCharges -> (list)

Specifies whether there are recurring charges for the offering.

(structure)

Specifies whether charges for devices are recurring.

cost -> (structure)

The cost of the recurring charge.

amount -> (double)

The numerical amount of an offering or transaction.

currencyCode -> (string)

The currency code of a monetary amount. For example, `USD` means U.S. dollars.

frequency -> (string)

The frequency in which charges recur.

quantity -> (integer)

The number of available devices in the offering.

effectiveOn -> (timestamp)

The date on which the offering is effective.

transactionId -> (string)

The transaction ID of the offering transaction.

offeringPromotionId -> (string)

The ID that corresponds to a device offering promotion.

createdOn -> (timestamp)

The date on which an offering transaction was created.

cost -> (structure)

The cost of an offering transaction.

amount -> (double)

The numerical amount of an offering or transaction.

currencyCode -> (string)

The currency code of a monetary amount. For example, `USD` means U.S. dollars.