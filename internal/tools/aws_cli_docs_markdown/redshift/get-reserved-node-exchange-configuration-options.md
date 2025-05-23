# get-reserved-node-exchange-configuration-optionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/get-reserved-node-exchange-configuration-options.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/get-reserved-node-exchange-configuration-options.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/index.html#cli-aws-redshift) ]

# get-reserved-node-exchange-configuration-options

## Description

Gets the configuration options for the reserved-node exchange. These options include information about the source reserved node and target reserved node offering. Details include the node type, the price, the node count, and the offering type.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/GetReservedNodeExchangeConfigurationOptions)

`get-reserved-node-exchange-configuration-options` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ReservedNodeConfigurationOptionList`

## Synopsis

```
get-reserved-node-exchange-configuration-options
--action-type <value>
[--cluster-identifier <value>]
[--snapshot-identifier <value>]
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

`--action-type` (string)

The action type of the reserved-node configuration. The action type can be an exchange initiated from either a snapshot or a resize.

Possible values:

- `restore-cluster`
- `resize-cluster`

`--cluster-identifier` (string)

The identifier for the cluster that is the source for a reserved-node exchange.

`--snapshot-identifier` (string)

The identifier for the snapshot that is the source for the reserved-node exchange.

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

Marker -> (string)

A pagination token provided by a previous `GetReservedNodeExchangeConfigurationOptions` request.

ReservedNodeConfigurationOptionList -> (list)

the configuration options for the reserved-node exchange. These options include information about the source reserved node and target reserved node. Details include the node type, the price, the node count, and the offering type.

(structure)

Details for a reserved-node exchange. Examples include the node type for a reserved node, the price for a node, the nodeâs state, and other details.

SourceReservedNode -> (structure)

Describes a reserved node. You can call the  DescribeReservedNodeOfferings API to obtain the available reserved node offerings.

ReservedNodeId -> (string)

The unique identifier for the reservation.

ReservedNodeOfferingId -> (string)

The identifier for the reserved node offering.

NodeType -> (string)

The node type of the reserved node.

StartTime -> (timestamp)

The time the reservation started. You purchase a reserved node offering for a duration. This is the start time of that duration.

Duration -> (integer)

The duration of the node reservation in seconds.

FixedPrice -> (double)

The fixed cost Amazon Redshift charges you for this reserved node.

UsagePrice -> (double)

The hourly rate Amazon Redshift charges you for this reserved node.

CurrencyCode -> (string)

The currency code for the reserved cluster.

NodeCount -> (integer)

The number of reserved compute nodes.

State -> (string)

The state of the reserved compute node.

Possible Values:

- pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed.
- active-This reserved node is owned by the caller and is available for use.
- payment-failed-Payment failed for the purchase attempt.
- retired-The reserved node is no longer available.
- exchanging-The owner is exchanging the reserved node for another reserved node.

OfferingType -> (string)

The anticipated utilization of the reserved node, as defined in the reserved node offering.

RecurringCharges -> (list)

The recurring charges for the reserved node.

(structure)

Describes a recurring charge.

RecurringChargeAmount -> (double)

The amount charged per the period of time specified by the recurring charge frequency.

RecurringChargeFrequency -> (string)

The frequency at which the recurring charge amount is applied.

ReservedNodeOfferingType -> (string)

TargetReservedNodeCount -> (integer)

The target reserved-node count.

TargetReservedNodeOffering -> (structure)

Describes a reserved node offering.

ReservedNodeOfferingId -> (string)

The offering identifier.

NodeType -> (string)

The node type offered by the reserved node offering.

Duration -> (integer)

The duration, in seconds, for which the offering will reserve the node.

FixedPrice -> (double)

The upfront fixed charge you will pay to purchase the specific reserved node offering.

UsagePrice -> (double)

The rate you are charged for each hour the cluster that is using the offering is running.

CurrencyCode -> (string)

The currency code for the compute nodes offering.

OfferingType -> (string)

The anticipated utilization of the reserved node, as defined in the reserved node offering.

RecurringCharges -> (list)

The charge to your account regardless of whether you are creating any clusters using the node offering. Recurring charges are only in effect for heavy-utilization reserved nodes.

(structure)

Describes a recurring charge.

RecurringChargeAmount -> (double)

The amount charged per the period of time specified by the recurring charge frequency.

RecurringChargeFrequency -> (string)

The frequency at which the recurring charge amount is applied.

ReservedNodeOfferingType -> (string)