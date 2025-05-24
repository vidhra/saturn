# create-orderÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/create-order.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/create-order.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [outposts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/index.html#cli-aws-outposts) ]

# create-order

## Description

Creates an order for an Outpost.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/outposts-2019-12-03/CreateOrder)

## Synopsis

```
create-order
--outpost-identifier <value>
--line-items <value>
--payment-option <value>
[--payment-term <value>]
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

`--outpost-identifier` (string)

The ID or the Amazon Resource Name (ARN) of the Outpost.

`--line-items` (list)

The line items that make up the order.

(structure)

Information about a line item request.

CatalogItemId -> (string)

The ID of the catalog item.

Quantity -> (integer)

The quantity of a line item request.

Shorthand Syntax:

```
CatalogItemId=string,Quantity=integer ...
```

JSON Syntax:

```
[
  {
    "CatalogItemId": "string",
    "Quantity": integer
  }
  ...
]
```

`--payment-option` (string)

The payment option.

Possible values:

- `ALL_UPFRONT`
- `NO_UPFRONT`
- `PARTIAL_UPFRONT`

`--payment-term` (string)

The payment terms.

Possible values:

- `THREE_YEARS`
- `ONE_YEAR`
- `FIVE_YEARS`

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

Order -> (structure)

Information about this order.

OutpostId -> (string)

The ID of the Outpost in the order.

OrderId -> (string)

The ID of the order.

Status -> (string)

The status of the order.

- `PREPARING` - Order is received and being prepared.
- `IN_PROGRESS` - Order is either being built or shipped. To get more details, see the line item status.
- `DELIVERED` - Order was delivered to the Outpost site.
- `COMPLETED` - Order is complete.
- `CANCELLED` - Order is cancelled.
- `ERROR` - Customer should contact support.

### Note

The following status are deprecated: `RECEIVED` , `PENDING` , `PROCESSING` , `INSTALLING` , and `FULFILLED` .

LineItems -> (list)

The line items for the order

(structure)

Information about a line item.

CatalogItemId -> (string)

The ID of the catalog item.

LineItemId -> (string)

The ID of the line item.

Quantity -> (integer)

The quantity of the line item.

Status -> (string)

The status of the line item.

ShipmentInformation -> (structure)

Information about a line item shipment.

ShipmentTrackingNumber -> (string)

The tracking number of the shipment.

ShipmentCarrier -> (string)

The carrier of the shipment.

AssetInformationList -> (list)

Information about assets.

(structure)

Information about a line item asset.

AssetId -> (string)

The ID of the asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.

MacAddressList -> (list)

The MAC addresses of the asset.

(string)

PreviousLineItemId -> (string)

The ID of the previous line item.

PreviousOrderId -> (string)

The ID of the previous order.

PaymentOption -> (string)

The payment option for the order.

OrderSubmissionDate -> (timestamp)

The submission date for the order.

OrderFulfilledDate -> (timestamp)

The fulfillment date of the order.

PaymentTerm -> (string)

The payment term.

OrderType -> (string)

The type of order.