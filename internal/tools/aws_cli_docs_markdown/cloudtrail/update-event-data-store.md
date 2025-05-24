# update-event-data-storeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-event-data-store.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-event-data-store.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudtrail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/index.html#cli-aws-cloudtrail) ]

# update-event-data-store

## Description

Updates an event data store. The required `EventDataStore` value is an ARN or the ID portion of the ARN. Other parameters are optional, but at least one optional parameter must be specified, or CloudTrail throws an error. `RetentionPeriod` is in days, and valid values are integers between 7 and 3653 if the `BillingMode` is set to `EXTENDABLE_RETENTION_PRICING` , or between 7 and 2557 if `BillingMode` is set to `FIXED_RETENTION_PRICING` . By default, `TerminationProtection` is enabled.

For event data stores for CloudTrail events, `AdvancedEventSelectors` includes or excludes management, data, or network activity events in your event data store. For more information about `AdvancedEventSelectors` , see [AdvancedEventSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html) .

For event data stores for CloudTrail Insights events, Config configuration items, Audit Manager evidence, or non-Amazon Web Services events, `AdvancedEventSelectors` includes events of that type in your event data store.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/UpdateEventDataStore)

## Synopsis

```
update-event-data-store
--event-data-store <value>
[--name <value>]
[--advanced-event-selectors <value>]
[--multi-region-enabled | --no-multi-region-enabled]
[--organization-enabled | --no-organization-enabled]
[--retention-period <value>]
[--termination-protection-enabled | --no-termination-protection-enabled]
[--kms-key-id <value>]
[--billing-mode <value>]
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

The ARN (or the ID suffix of the ARN) of the event data store that you want to update.

`--name` (string)

The event data store name.

`--advanced-event-selectors` (list)

The advanced event selectors used to select events for the event data store. You can configure up to five advanced event selectors for each event data store.

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

JSON Syntax:

```
[
  {
    "Name": "string",
    "FieldSelectors": [
      {
        "Field": "string",
        "Equals": ["string", ...],
        "StartsWith": ["string", ...],
        "EndsWith": ["string", ...],
        "NotEquals": ["string", ...],
        "NotStartsWith": ["string", ...],
        "NotEndsWith": ["string", ...]
      }
      ...
    ]
  }
  ...
]
```

`--multi-region-enabled` | `--no-multi-region-enabled` (boolean)

Specifies whether an event data store collects events from all Regions, or only from the Region in which it was created.

`--organization-enabled` | `--no-organization-enabled` (boolean)

Specifies whether an event data store collects events logged for an organization in Organizations.

### Note

Only the management account for the organization can convert an organization event data store to a non-organization event data store, or convert a non-organization event data store to an organization event data store.

`--retention-period` (integer)

The retention period of the event data store, in days. If `BillingMode` is set to `EXTENDABLE_RETENTION_PRICING` , you can set a retention period of up to 3653 days, the equivalent of 10 years. If `BillingMode` is set to `FIXED_RETENTION_PRICING` , you can set a retention period of up to 2557 days, the equivalent of seven years.

CloudTrail Lake determines whether to retain an event by checking if the `eventTime` of the event is within the specified retention period. For example, if you set a retention period of 90 days, CloudTrail will remove events when the `eventTime` is older than 90 days.

### Note

If you decrease the retention period of an event data store, CloudTrail will remove any events with an `eventTime` older than the new retention period. For example, if the previous retention period was 365 days and you decrease it to 100 days, CloudTrail will remove events with an `eventTime` older than 100 days.

`--termination-protection-enabled` | `--no-termination-protection-enabled` (boolean)

Indicates that termination protection is enabled and the event data store cannot be automatically deleted.

`--kms-key-id` (string)

Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by `alias/` , a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.

### Warning

Disabling or deleting the KMS key, or removing CloudTrail permissions on the key, prevents CloudTrail from logging events to the event data store, and prevents users from querying the data in the event data store that was encrypted with the key. After you associate an event data store with a KMS key, the KMS key cannot be removed or changed. Before you disable or delete a KMS key that you are using with an event data store, delete or back up your event data store.

CloudTrail also supports KMS multi-Region keys. For more information about multi-Region keys, see [Using multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the *Key Management Service Developer Guide* .

Examples:

- `alias/MyAliasName`
- `arn:aws:kms:us-east-2:123456789012:alias/MyAliasName`
- `arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012`
- `12345678-1234-1234-1234-123456789012`

`--billing-mode` (string)

### Note

You canât change the billing mode from `EXTENDABLE_RETENTION_PRICING` to `FIXED_RETENTION_PRICING` . If `BillingMode` is set to `EXTENDABLE_RETENTION_PRICING` and you want to use `FIXED_RETENTION_PRICING` instead, youâll need to stop ingestion on the event data store and create a new event data store that uses `FIXED_RETENTION_PRICING` .

The billing mode for the event data store determines the cost for ingesting events and the default and maximum retention period for the event data store.

The following are the possible values:

- `EXTENDABLE_RETENTION_PRICING` - This billing mode is generally recommended if you want a flexible retention period of up to 3653 days (about 10 years). The default retention period for this billing mode is 366 days.
- `FIXED_RETENTION_PRICING` - This billing mode is recommended if you expect to ingest more than 25 TB of event data per month and need a retention period of up to 2557 days (about 7 years). The default retention period for this billing mode is 2557 days.

For more information about CloudTrail pricing, see [CloudTrail Pricing](http://aws.amazon.com/cloudtrail/pricing/) and [Managing CloudTrail Lake costs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html) .

Possible values:

- `EXTENDABLE_RETENTION_PRICING`
- `FIXED_RETENTION_PRICING`

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

The ARN of the event data store.

Name -> (string)

The name of the event data store.

Status -> (string)

The status of an event data store.

AdvancedEventSelectors -> (list)

The advanced event selectors that are applied to the event data store.

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

The retention period, in days.

TerminationProtectionEnabled -> (boolean)

Indicates whether termination protection is enabled for the event data store.

CreatedTimestamp -> (timestamp)

The timestamp that shows when an event data store was first created.

UpdatedTimestamp -> (timestamp)

The timestamp that shows when the event data store was last updated. `UpdatedTimestamp` is always either the same or newer than the time shown in `CreatedTimestamp` .

KmsKeyId -> (string)

Specifies the KMS key ID that encrypts the events delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the following format.

`arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012`

BillingMode -> (string)

The billing mode for the event data store.

FederationStatus -> (string)

Indicates the [Lake query federation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html) status. The status is `ENABLED` if Lake query federation is enabled, or `DISABLED` if Lake query federation is disabled. You cannot delete an event data store if the `FederationStatus` is `ENABLED` .

FederationRoleArn -> (string)

If Lake query federation is enabled, provides the ARN of the federation role used to access the resources for the federated event data store.