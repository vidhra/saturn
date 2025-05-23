# send-data-integration-eventÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/supplychain/send-data-integration-event.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/supplychain/send-data-integration-event.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [supplychain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/supplychain/index.html#cli-aws-supplychain) ]

# send-data-integration-event

## Description

Send the data payload for the event with real-time data for analysis or monitoring. The real-time data events are stored in an Amazon Web Services service before being processed and stored in data lake.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/supplychain-2024-01-01/SendDataIntegrationEvent)

## Synopsis

```
send-data-integration-event
--instance-id <value>
--event-type <value>
--data <value>
--event-group-id <value>
[--event-timestamp <value>]
[--client-token <value>]
[--dataset-target <value>]
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

`--instance-id` (string)

The AWS Supply Chain instance identifier.

`--event-type` (string)

The data event type.

- **scn.data.dataset** - Send data directly to any specified dataset.
- **scn.data.supplyplan** - Send data to [supply_plan](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/supply-plan-entity.html) dataset.
- **scn.data.shipmentstoporder** - Send data to [shipment_stop_order](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-stop-order-entity.html) dataset.
- **scn.data.shipmentstop** - Send data to [shipment_stop](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-stop-entity.html) dataset.
- **scn.data.shipment** - Send data to [shipment](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-entity.html) dataset.
- **scn.data.reservation** - Send data to [reservation](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/planning-reservation-entity.html) dataset.
- **scn.data.processproduct** - Send data to [process_product](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-product-entity.html) dataset.
- **scn.data.processoperation** - Send data to [process_operation](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-operation-entity.html) dataset.
- **scn.data.processheader** - Send data to [process_header](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-header-entity.html) dataset.
- **scn.data.forecast** - Send data to [forecast](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/forecast-forecast-entity.html) dataset.
- **scn.data.inventorylevel** - Send data to [inv_level](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/inventory_mgmnt-inv-level-entity.html) dataset.
- **scn.data.inboundorder** - Send data to [inbound_order](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-entity.html) dataset.
- **scn.data.inboundorderline** - Send data to [inbound_order_line](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-line-entity.html) dataset.
- **scn.data.inboundorderlineschedule** - Send data to [inbound_order_line_schedule](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-line-schedule-entity.html) dataset.
- **scn.data.outboundorderline** - Send data to [outbound_order_line](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/outbound-fulfillment-order-line-entity.html) dataset.
- **scn.data.outboundshipment** - Send data to [outbound_shipment](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/outbound-fulfillment-shipment-entity.html) dataset.

Possible values:

- `scn.data.forecast`
- `scn.data.inventorylevel`
- `scn.data.inboundorder`
- `scn.data.inboundorderline`
- `scn.data.inboundorderlineschedule`
- `scn.data.outboundorderline`
- `scn.data.outboundshipment`
- `scn.data.processheader`
- `scn.data.processoperation`
- `scn.data.processproduct`
- `scn.data.reservation`
- `scn.data.shipment`
- `scn.data.shipmentstop`
- `scn.data.shipmentstoporder`
- `scn.data.supplyplan`
- `scn.data.dataset`

`--data` (string)

The data payload of the event, should follow the data schema of the target dataset, or see [Data entities supported in AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html) . To send single data record, use JsonObject format; to send multiple data records, use JsonArray format.

Note that for AWS Supply Chain dataset under **asc** namespace, it has a connection_id internal field that is not allowed to be provided by client directly, they will be auto populated.

`--event-group-id` (string)

Event identifier (for example, orderId for InboundOrder) used for data sharding or partitioning. Noted under one eventGroupId of same eventType and instanceId, events are processed sequentially in the order they are received by the server.

`--event-timestamp` (timestamp)

The timestamp (in epoch seconds) associated with the event. If not provided, it will be assigned with current timestamp.

`--client-token` (string)

The idempotent client token. The token is active for 8 hours, and within its lifetime, it ensures the request completes only once upon retry with same client token. If omitted, the AWS SDK generates a unique value so that AWS SDK can safely retry the request upon network errors.

`--dataset-target` (structure)

The target dataset configuration for **scn.data.dataset** event type.

datasetIdentifier -> (string)

The datalake dataset ARN identifier.

operationType -> (string)

The target dataset load operation type.

Shorthand Syntax:

```
datasetIdentifier=string,operationType=string
```

JSON Syntax:

```
{
  "datasetIdentifier": "string",
  "operationType": "APPEND"|"UPSERT"|"DELETE"
}
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

eventId -> (string)

The unique event identifier.