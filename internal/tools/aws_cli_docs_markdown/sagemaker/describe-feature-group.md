# describe-feature-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-feature-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-feature-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-feature-group

## Description

Use this operation to describe a `FeatureGroup` . The response includes information on the creation time, `FeatureGroup` name, the unique identifier for each `FeatureGroup` , and more.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeFeatureGroup)

## Synopsis

```
describe-feature-group
--feature-group-name <value>
[--next-token <value>]
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

`--feature-group-name` (string)

The name or Amazon Resource Name (ARN) of the `FeatureGroup` you want described.

`--next-token` (string)

A token to resume pagination of the list of `Features` (`FeatureDefinitions` ). 2,500 `Features` are returned by default.

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

FeatureGroupArn -> (string)

The Amazon Resource Name (ARN) of the `FeatureGroup` .

FeatureGroupName -> (string)

he name of the `FeatureGroup` .

RecordIdentifierFeatureName -> (string)

The name of the `Feature` used for `RecordIdentifier` , whose value uniquely identifies a record stored in the feature store.

EventTimeFeatureName -> (string)

The name of the feature that stores the `EventTime` of a Record in a `FeatureGroup` .

An `EventTime` is a point in time when a new event occurs that corresponds to the creation or update of a `Record` in a `FeatureGroup` . All `Records` in the `FeatureGroup` have a corresponding `EventTime` .

FeatureDefinitions -> (list)

A list of the `Features` in the `FeatureGroup` . Each feature is defined by a `FeatureName` and `FeatureType` .

(structure)

A list of features. You must include `FeatureName` and `FeatureType` . Valid feature `FeatureType` s are `Integral` , `Fractional` and `String` .

FeatureName -> (string)

The name of a feature. The type must be a string. `FeatureName` cannot be any of the following: `is_deleted` , `write_time` , `api_invocation_time` .

The name:

- Must start with an alphanumeric character.
- Can only include alphanumeric characters, underscores, and hyphens. Spaces are not allowed.

FeatureType -> (string)

The value type of a feature. Valid values are Integral, Fractional, or String.

CollectionType -> (string)

A grouping of elements where each element within the collection must have the same feature type (`String` , `Integral` , or `Fractional` ).

- `List` : An ordered collection of elements.
- `Set` : An unordered collection of unique elements.
- `Vector` : A specialized list that represents a fixed-size array of elements. The vector dimension is determined by you. Must have elements with fractional feature types.

CollectionConfig -> (tagged union structure)

Configuration for your collection.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `VectorConfig`.

VectorConfig -> (structure)

Configuration for your vector collection type.

- `Dimension` : The number of elements in your vector.

Dimension -> (integer)

The number of elements in your vector.

CreationTime -> (timestamp)

A timestamp indicating when SageMaker created the `FeatureGroup` .

LastModifiedTime -> (timestamp)

A timestamp indicating when the feature group was last updated.

OnlineStoreConfig -> (structure)

The configuration for the `OnlineStore` .

SecurityConfig -> (structure)

Use to specify KMS Key ID (`KMSKeyId` ) for at-rest encryption of your `OnlineStore` .

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (KMS) key ARN that SageMaker Feature Store uses to encrypt the Amazon S3 objects at rest using Amazon S3 server-side encryption.

The caller (either user or IAM role) of `CreateFeatureGroup` must have below permissions to the `OnlineStore` `KmsKeyId` :

- `"kms:Encrypt"`
- `"kms:Decrypt"`
- `"kms:DescribeKey"`
- `"kms:CreateGrant"`
- `"kms:RetireGrant"`
- `"kms:ReEncryptFrom"`
- `"kms:ReEncryptTo"`
- `"kms:GenerateDataKey"`
- `"kms:ListAliases"`
- `"kms:ListGrants"`
- `"kms:RevokeGrant"`

The caller (either user or IAM role) to all DataPlane operations (`PutRecord` , `GetRecord` , `DeleteRecord` ) must have the following permissions to the `KmsKeyId` :

- `"kms:Decrypt"`

EnableOnlineStore -> (boolean)

Turn `OnlineStore` off by specifying `False` for the `EnableOnlineStore` flag. Turn `OnlineStore` on by specifying `True` for the `EnableOnlineStore` flag.

The default value is `False` .

TtlDuration -> (structure)

Time to live duration, where the record is hard deleted after the expiration time is reached; `ExpiresAt` = `EventTime` + `TtlDuration` . For information on HardDelete, see the [DeleteRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html) API in the Amazon SageMaker API Reference guide.

Unit -> (string)

`TtlDuration` time unit.

Value -> (integer)

`TtlDuration` time value.

StorageType -> (string)

Option for different tiers of low latency storage for real-time data retrieval.

- `Standard` : A managed low latency data store for feature groups.
- `InMemory` : A managed data store for feature groups that supports very low latency retrieval.

OfflineStoreConfig -> (structure)

The configuration of the offline store. It includes the following configurations:

- Amazon S3 location of the offline store.
- Configuration of the Glue data catalog.
- Table format of the offline store.
- Option to disable the automatic creation of a Glue table for the offline store.
- Encryption configuration.

S3StorageConfig -> (structure)

The Amazon Simple Storage (Amazon S3) location of `OfflineStore` .

S3Uri -> (string)

The S3 URI, or location in Amazon S3, of `OfflineStore` .

S3 URIs have a format similar to the following: `s3://example-bucket/prefix/` .

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (KMS) key ARN of the key used to encrypt any objects written into the `OfflineStore` S3 location.

The IAM `roleARN` that is passed as a parameter to `CreateFeatureGroup` must have below permissions to the `KmsKeyId` :

- `"kms:GenerateDataKey"`

ResolvedOutputS3Uri -> (string)

The S3 path where offline records are written.

DisableGlueTableCreation -> (boolean)

Set to `True` to disable the automatic creation of an Amazon Web Services Glue table when configuring an `OfflineStore` . If set to `False` , Feature Store will name the `OfflineStore` Glue table following [Athenaâs naming recommendations](https://docs.aws.amazon.com/athena/latest/ug/tables-databases-columns-names.html) .

The default value is `False` .

DataCatalogConfig -> (structure)

The meta data of the Glue table that is autogenerated when an `OfflineStore` is created.

TableName -> (string)

The name of the Glue table.

Catalog -> (string)

The name of the Glue table catalog.

Database -> (string)

The name of the Glue table database.

TableFormat -> (string)

Format for the offline store table. Supported formats are Glue (Default) and [Apache Iceberg](https://iceberg.apache.org/) .

ThroughputConfig -> (structure)

Active throughput configuration of the feature group. There are two modes: `ON_DEMAND` and `PROVISIONED` . With on-demand mode, you are charged for data reads and writes that your application performs on your feature group. You do not need to specify read and write throughput because Feature Store accommodates your workloads as they ramp up and down. You can switch a feature group to on-demand only once in a 24 hour period. With provisioned throughput mode, you specify the read and write capacity per second that you expect your application to require, and you are billed based on those limits. Exceeding provisioned throughput will result in your requests being throttled.

Note: `PROVISIONED` throughput mode is supported only for feature groups that are offline-only, or use the ` `Standard` [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html#sagemaker-Type-OnlineStoreConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html#sagemaker-Type-OnlineStoreConfig)-StorageType`__ tier online store.

ThroughputMode -> (string)

The mode used for your feature group throughput: `ON_DEMAND` or `PROVISIONED` .

ProvisionedReadCapacityUnits -> (integer)

For provisioned feature groups with online store enabled, this indicates the read throughput you are billed for and can consume without throttling.

This field is not applicable for on-demand feature groups.

ProvisionedWriteCapacityUnits -> (integer)

For provisioned feature groups, this indicates the write throughput you are billed for and can consume without throttling.

This field is not applicable for on-demand feature groups.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM execution role used to persist data into the OfflineStore if an OfflineStoreConfig is provided.

FeatureGroupStatus -> (string)

The status of the feature group.

OfflineStoreStatus -> (structure)

The status of the `OfflineStore` . Notifies you if replicating data into the `OfflineStore` has failed. Returns either: `Active` or `Blocked`

Status -> (string)

An `OfflineStore` status.

BlockedReason -> (string)

The justification for why the OfflineStoreStatus is Blocked (if applicable).

LastUpdateStatus -> (structure)

A value indicating whether the update made to the feature group was successful.

Status -> (string)

A value that indicates whether the update was made successful.

FailureReason -> (string)

If the update wasnât successful, indicates the reason why it failed.

FailureReason -> (string)

The reason that the `FeatureGroup` failed to be replicated in the `OfflineStore` . This is failure can occur because:

- The `FeatureGroup` could not be created in the `OfflineStore` .
- The `FeatureGroup` could not be deleted from the `OfflineStore` .

Description -> (string)

A free form description of the feature group.

NextToken -> (string)

A token to resume pagination of the list of `Features` (`FeatureDefinitions` ).

OnlineStoreTotalSizeBytes -> (long)

The size of the `OnlineStore` in bytes.