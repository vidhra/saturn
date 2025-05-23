# create-feature-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-feature-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-feature-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-feature-group

## Description

Create a new `FeatureGroup` . A `FeatureGroup` is a group of `Features` defined in the `FeatureStore` to describe a `Record` .

The `FeatureGroup` defines the schema and features contained in the `FeatureGroup` . A `FeatureGroup` definition is composed of a list of `Features` , a `RecordIdentifierFeatureName` , an `EventTimeFeatureName` and configurations for its `OnlineStore` and `OfflineStore` . Check [Amazon Web Services service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) to see the `FeatureGroup` s quota for your Amazon Web Services account.

Note that it can take approximately 10-15 minutes to provision an `OnlineStore` `FeatureGroup` with the `InMemory` `StorageType` .

### Warning

You must include at least one of `OnlineStoreConfig` and `OfflineStoreConfig` to create a `FeatureGroup` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateFeatureGroup)

## Synopsis

```
create-feature-group
--feature-group-name <value>
--record-identifier-feature-name <value>
--event-time-feature-name <value>
--feature-definitions <value>
[--online-store-config <value>]
[--offline-store-config <value>]
[--throughput-config <value>]
[--role-arn <value>]
[--description <value>]
[--tags <value>]
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

The name of the `FeatureGroup` . The name must be unique within an Amazon Web Services Region in an Amazon Web Services account.

The name:

- Must start with an alphanumeric character.
- Can only include alphanumeric characters, underscores, and hyphens. Spaces are not allowed.

`--record-identifier-feature-name` (string)

The name of the `Feature` whose value uniquely identifies a `Record` defined in the `FeatureStore` . Only the latest record per identifier value will be stored in the `OnlineStore` . `RecordIdentifierFeatureName` must be one of feature definitionsâ names.

You use the `RecordIdentifierFeatureName` to access data in a `FeatureStore` .

This name:

- Must start with an alphanumeric character.
- Can only contains alphanumeric characters, hyphens, underscores. Spaces are not allowed.

`--event-time-feature-name` (string)

The name of the feature that stores the `EventTime` of a `Record` in a `FeatureGroup` .

An `EventTime` is a point in time when a new event occurs that corresponds to the creation or update of a `Record` in a `FeatureGroup` . All `Records` in the `FeatureGroup` must have a corresponding `EventTime` .

An `EventTime` can be a `String` or `Fractional` .

- `Fractional` : `EventTime` feature values must be a Unix timestamp in seconds.
- `String` : `EventTime` feature values must be an ISO-8601 string in the format. The following formats are supported `yyyy-MM-dd'T'HH:mm:ssZ` and `yyyy-MM-dd'T'HH:mm:ss.SSSZ` where `yyyy` , `MM` , and `dd` represent the year, month, and day respectively and `HH` , `mm` , `ss` , and if applicable, `SSS` represent the hour, month, second and milliseconds respsectively. `'T'` and `Z` are constants.

`--feature-definitions` (list)

A list of `Feature` names and types. `Name` and `Type` is compulsory per `Feature` .

Valid feature `FeatureType` s are `Integral` , `Fractional` and `String` .

`FeatureName` s cannot be any of the following: `is_deleted` , `write_time` , `api_invocation_time`

You can create up to 2,500 `FeatureDefinition` s per `FeatureGroup` .

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

Shorthand Syntax:

```
FeatureName=string,FeatureType=string,CollectionType=string,CollectionConfig={VectorConfig={Dimension=integer}} ...
```

JSON Syntax:

```
[
  {
    "FeatureName": "string",
    "FeatureType": "Integral"|"Fractional"|"String",
    "CollectionType": "List"|"Set"|"Vector",
    "CollectionConfig": {
      "VectorConfig": {
        "Dimension": integer
      }
    }
  }
  ...
]
```

`--online-store-config` (structure)

You can turn the `OnlineStore` on or off by specifying `True` for the `EnableOnlineStore` flag in `OnlineStoreConfig` .

You can also include an Amazon Web Services KMS key ID (`KMSKeyId` ) for at-rest encryption of the `OnlineStore` .

The default value is `False` .

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

Shorthand Syntax:

```
SecurityConfig={KmsKeyId=string},EnableOnlineStore=boolean,TtlDuration={Unit=string,Value=integer},StorageType=string
```

JSON Syntax:

```
{
  "SecurityConfig": {
    "KmsKeyId": "string"
  },
  "EnableOnlineStore": true|false,
  "TtlDuration": {
    "Unit": "Seconds"|"Minutes"|"Hours"|"Days"|"Weeks",
    "Value": integer
  },
  "StorageType": "Standard"|"InMemory"
}
```

`--offline-store-config` (structure)

Use this to configure an `OfflineFeatureStore` . This parameter allows you to specify:

- The Amazon Simple Storage Service (Amazon S3) location of an `OfflineStore` .
- A configuration for an Amazon Web Services Glue or Amazon Web Services Hive data catalog.
- An KMS encryption key to encrypt the Amazon S3 location used for `OfflineStore` . If KMS encryption key is not specified, by default we encrypt all data at rest using Amazon Web Services KMS key. By defining your [bucket-level key](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html) for SSE, you can reduce Amazon Web Services KMS requests costs by up to 99 percent.
- Format for the offline store table. Supported formats are Glue (Default) and [Apache Iceberg](https://iceberg.apache.org/) .

To learn more about this parameter, see [OfflineStoreConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OfflineStoreConfig.html) .

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

Shorthand Syntax:

```
S3StorageConfig={S3Uri=string,KmsKeyId=string,ResolvedOutputS3Uri=string},DisableGlueTableCreation=boolean,DataCatalogConfig={TableName=string,Catalog=string,Database=string},TableFormat=string
```

JSON Syntax:

```
{
  "S3StorageConfig": {
    "S3Uri": "string",
    "KmsKeyId": "string",
    "ResolvedOutputS3Uri": "string"
  },
  "DisableGlueTableCreation": true|false,
  "DataCatalogConfig": {
    "TableName": "string",
    "Catalog": "string",
    "Database": "string"
  },
  "TableFormat": "Default"|"Glue"|"Iceberg"
}
```

`--throughput-config` (structure)

Used to set feature group throughput configuration. There are two modes: `ON_DEMAND` and `PROVISIONED` . With on-demand mode, you are charged for data reads and writes that your application performs on your feature group. You do not need to specify read and write throughput because Feature Store accommodates your workloads as they ramp up and down. You can switch a feature group to on-demand only once in a 24 hour period. With provisioned throughput mode, you specify the read and write capacity per second that you expect your application to require, and you are billed based on those limits. Exceeding provisioned throughput will result in your requests being throttled.

Note: `PROVISIONED` throughput mode is supported only for feature groups that are offline-only, or use the ` `Standard` [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html#sagemaker-Type-OnlineStoreConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html#sagemaker-Type-OnlineStoreConfig)-StorageType`__ tier online store.

ThroughputMode -> (string)

The mode used for your feature group throughput: `ON_DEMAND` or `PROVISIONED` .

ProvisionedReadCapacityUnits -> (integer)

For provisioned feature groups with online store enabled, this indicates the read throughput you are billed for and can consume without throttling.

This field is not applicable for on-demand feature groups.

ProvisionedWriteCapacityUnits -> (integer)

For provisioned feature groups, this indicates the write throughput you are billed for and can consume without throttling.

This field is not applicable for on-demand feature groups.

Shorthand Syntax:

```
ThroughputMode=string,ProvisionedReadCapacityUnits=integer,ProvisionedWriteCapacityUnits=integer
```

JSON Syntax:

```
{
  "ThroughputMode": "OnDemand"|"Provisioned",
  "ProvisionedReadCapacityUnits": integer,
  "ProvisionedWriteCapacityUnits": integer
}
```

`--role-arn` (string)

The Amazon Resource Name (ARN) of the IAM execution role used to persist data into the `OfflineStore` if an `OfflineStoreConfig` is provided.

`--description` (string)

A free-form description of a `FeatureGroup` .

`--tags` (list)

Tags used to identify `Features` in each `FeatureGroup` .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
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

## Output

FeatureGroupArn -> (string)

The Amazon Resource Name (ARN) of the `FeatureGroup` . This is a unique identifier for the feature group.