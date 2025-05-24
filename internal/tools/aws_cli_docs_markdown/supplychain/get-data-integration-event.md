# get-data-integration-eventÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/supplychain/get-data-integration-event.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/supplychain/get-data-integration-event.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [supplychain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/supplychain/index.html#cli-aws-supplychain) ]

# get-data-integration-event

## Description

Enables you to programmatically view an Amazon Web Services Supply Chain Data Integration Event. Developers can view the eventType, eventGroupId, eventTimestamp, datasetTarget, datasetLoadExecution.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/supplychain-2024-01-01/GetDataIntegrationEvent)

## Synopsis

```
get-data-integration-event
--instance-id <value>
--event-id <value>
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

The Amazon Web Services Supply Chain instance identifier.

`--event-id` (string)

The unique event identifier.

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

event -> (structure)

The details of the DataIntegrationEvent returned.

instanceId -> (string)

The AWS Supply Chain instance identifier.

eventId -> (string)

The unique event identifier.

eventType -> (string)

The data event type.

eventGroupId -> (string)

Event identifier (for example, orderId for InboundOrder) used for data sharding or partitioning.

eventTimestamp -> (timestamp)

The event timestamp (in epoch seconds).

datasetTargetDetails -> (structure)

The target dataset details for a DATASET event type.

datasetIdentifier -> (string)

The datalake dataset ARN identifier.

operationType -> (string)

The target dataset load operation type. The available options are:

- **APPEND** - Add new records to the dataset. Noted that this operation type will just try to append records as-is without any primary key or partition constraints.
- **UPSERT** - Modify existing records in the dataset with primary key configured, events for datasets without primary keys are not allowed. If event data contains primary keys that match records in the dataset within same partition, then those existing records (in that partition) will be updated. If primary keys do not match, new records will be added. Note that if dataset contain records with duplicate primary key values in the same partition, those duplicate records will be deduped into one updated record.
- **DELETE** - Remove existing records in the dataset with primary key configured, events for datasets without primary keys are not allowed. If event data contains primary keys that match records in the dataset within same partition, then those existing records (in that partition) will be deleted. If primary keys do not match, no actions will be done. Note that if dataset contain records with duplicate primary key values in the same partition, all those duplicates will be removed.

datasetLoadExecution -> (structure)

The target dataset load execution.

status -> (string)

The event load execution status to target dataset.

message -> (string)

The failure message (if any) of failed event load execution to dataset.