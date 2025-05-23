# get-event-data-storeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-event-data-store.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-event-data-store.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudtrail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/index.html#cli-aws-cloudtrail) ]

# get-event-data-store

## Description

Returns information about an event data store specified as either an ARN or the ID portion of the ARN.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/GetEventDataStore)

## Synopsis

```
get-event-data-store
--event-data-store <value>
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

`--event-data-store` (string)

The ARN (or ID suffix of the ARN) of the event data store about which you want information.

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

EventDataStoreArn -> (string)

The event data store Amazon Resource Number (ARN).

Name -> (string)

The name of the event data store.

Status -> (string)

The status of an event data store.

AdvancedEventSelectors -> (list)

The advanced event selectors used to select events for the data store.

(structure)

Advanced event selectors let you create fine-grained selectors for CloudTrail management, data, and network activity events. They help you control costs by logging only those events that are important to you. For more information about configuring advanced event selectors, see the [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) , [Logging network activity events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html) , and [Logging management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html) topics in the *CloudTrail User Guide* .

You cannot apply both event selectors and advanced event selectors to a trail.

For information about configurable advanced event selector fields, see [AdvancedEventSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html) in the *CloudTrail API Reference* .

Name -> (string)

An optional, descriptive name for an advanced event selector, such as âLog data events for only two S3 bucketsâ.

FieldSelectors -> (list)

Contains all selector statements in an advanced event selector.

(structure)

A single selector statement in an advanced event selector.

Field -> (string)

A field in a CloudTrail event record on which to filter events to be logged. For event data stores for CloudTrail Insights events, Config configuration items, Audit Manager evidence, or events outside of Amazon Web Services, the field is used only for selecting events as filtering is not supported.

For more information, see [AdvancedFieldSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html) in the *CloudTrail API Reference* .

### Note

Selectors donât support the use of wildcards like `*` . To match multiple values with a single condition, you may use `StartsWith` , `EndsWith` , `NotStartsWith` , or `NotEndsWith` to explicitly match the beginning or end of the event field.

Equals -> (list)

An operator that includes events that match the exact value of the event record field specified as the value of `Field` . This is the only valid operator that you can use with the `readOnly` , `eventCategory` , and `resources.type` fields.

(string)

StartsWith -> (list)

An operator that includes events that match the first few characters of the event record field specified as the value of `Field` .

(string)

EndsWith -> (list)

An operator that includes events that match the last few characters of the event record field specified as the value of `Field` .

(string)

NotEquals -> (list)

An operator that excludes events that match the exact value of the event record field specified as the value of `Field` .

(string)

NotStartsWith -> (list)

An operator that excludes events that match the first few characters of the event record field specified as the value of `Field` .

(string)

NotEndsWith -> (list)

An operator that excludes events that match the last few characters of the event record field specified as the value of `Field` .

(string)

MultiRegionEnabled -> (boolean)

Indicates whether the event data store includes events from all Regions, or only from the Region in which it was created.

OrganizationEnabled -> (boolean)

Indicates whether an event data store is collecting logged events for an organization in Organizations.

RetentionPeriod -> (integer)

The retention period of the event data store, in days.

TerminationProtectionEnabled -> (boolean)

Indicates that termination protection is enabled.

CreatedTimestamp -> (timestamp)

The timestamp of the event data storeâs creation.

UpdatedTimestamp -> (timestamp)

Shows the time that an event data store was updated, if applicable. `UpdatedTimestamp` is always either the same or newer than the time shown in `CreatedTimestamp` .

KmsKeyId -> (string)

Specifies the KMS key ID that encrypts the events delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the following format.

`arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012`

BillingMode -> (string)

The billing mode for the event data store.

FederationStatus -> (string)

Indicates the [Lake query federation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html) status. The status is `ENABLED` if Lake query federation is enabled, or `DISABLED` if Lake query federation is disabled. You cannot delete an event data store if the `FederationStatus` is `ENABLED` .

FederationRoleArn -> (string)

If Lake query federation is enabled, provides the ARN of the federation role used to access the resources for the federated event data store.

PartitionKeys -> (list)

The partition keys for the event data store. To improve query performance and efficiency, CloudTrail Lake organizes event data into partitions based on values derived from partition keys.

(structure)

Contains information about a partition key for an event data store.

Name -> (string)

The name of the partition key.

Type -> (string)

The data type of the partition key. For example, `bigint` or `string` .