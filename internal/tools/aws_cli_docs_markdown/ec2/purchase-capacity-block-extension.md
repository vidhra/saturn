# purchase-capacity-block-extensionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/purchase-capacity-block-extension.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/purchase-capacity-block-extension.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# purchase-capacity-block-extension

## Description

Purchase the Capacity Block extension for use with your account. You must specify the ID of the Capacity Block extension offering you are purchasing.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/PurchaseCapacityBlockExtension)

## Synopsis

```
purchase-capacity-block-extension
--capacity-block-extension-offering-id <value>
--capacity-reservation-id <value>
[--dry-run | --no-dry-run]
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

`--capacity-block-extension-offering-id` (string)

The ID of the Capacity Block extension offering to purchase.

`--capacity-reservation-id` (string)

The ID of the Capacity reservation to be extended.

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

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

CapacityBlockExtensions -> (list)

The purchased Capacity Block extensions.

(structure)

Describes a Capacity Block extension. With an extension, you can extend the duration of time for an existing Capacity Block.

CapacityReservationId -> (string)

The reservation ID of the Capacity Block extension.

InstanceType -> (string)

The instance type of the Capacity Block extension.

InstanceCount -> (integer)

The number of instances in the Capacity Block extension.

AvailabilityZone -> (string)

The Availability Zone of the Capacity Block extension.

AvailabilityZoneId -> (string)

The Availability Zone ID of the Capacity Block extension.

CapacityBlockExtensionOfferingId -> (string)

The ID of the Capacity Block extension offering.

CapacityBlockExtensionDurationHours -> (integer)

The duration of the Capacity Block extension in hours.

CapacityBlockExtensionStatus -> (string)

The status of the Capacity Block extension. A Capacity Block extension can have one of the following statuses:

- `payment-pending` - The Capacity Block extension payment is processing. If your payment canât be processed within 12 hours, the Capacity Block extension is failed.
- `payment-failed` - Payment for the Capacity Block extension request was not successful.
- `payment-succeeded` - Payment for the Capacity Block extension request was successful. You receive an invoice that reflects the one-time upfront payment. In the invoice, you can associate the paid amount with the Capacity Block reservation ID.

CapacityBlockExtensionPurchaseDate -> (timestamp)

The date when the Capacity Block extension was purchased.

CapacityBlockExtensionStartDate -> (timestamp)

The start date of the Capacity Block extension.

CapacityBlockExtensionEndDate -> (timestamp)

The end date of the Capacity Block extension.

UpfrontFee -> (string)

The total price to be paid up front.

CurrencyCode -> (string)

The currency of the payment for the Capacity Block extension.