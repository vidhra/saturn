# get-storage-lens-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-storage-lens-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-storage-lens-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/index.html#cli-aws-s3control) ]

# get-storage-lens-configuration

## Description

### Note

This operation is not supported by directory buckets.

Gets the Amazon S3 Storage Lens configuration. For more information, see [Assessing your storage activity and usage with Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html) in the *Amazon S3 User Guide* . For a complete list of S3 Storage Lens metrics, see [S3 Storage Lens metrics glossary](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_metrics_glossary.html) in the *Amazon S3 User Guide* .

### Note

To use this action, you must have permission to perform the `s3:GetStorageLensConfiguration` action. For more information, see [Setting permissions to use Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html) in the *Amazon S3 User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/GetStorageLensConfiguration)

## Synopsis

```
get-storage-lens-configuration
--config-id <value>
--account-id <value>
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

`--config-id` (string)

The ID of the Amazon S3 Storage Lens configuration.

`--account-id` (string)

The account ID of the requester.

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

StorageLensConfiguration -> (structure)

The S3 Storage Lens configuration requested.

Id -> (string)

A container for the Amazon S3 Storage Lens configuration ID.

AccountLevel -> (structure)

A container for all the account-level configurations of your S3 Storage Lens configuration.

ActivityMetrics -> (structure)

A container element for S3 Storage Lens activity metrics.

IsEnabled -> (boolean)

A container that indicates whether activity metrics are enabled.

BucketLevel -> (structure)

A container element for the S3 Storage Lens bucket-level configuration.

ActivityMetrics -> (structure)

A container for the bucket-level activity metrics for S3 Storage Lens.

IsEnabled -> (boolean)

A container that indicates whether activity metrics are enabled.

PrefixLevel -> (structure)

A container for the prefix-level metrics for S3 Storage Lens.

StorageMetrics -> (structure)

A container for the prefix-level storage metrics for S3 Storage Lens.

IsEnabled -> (boolean)

A container for whether prefix-level storage metrics are enabled.

SelectionCriteria -> (structure)

Delimiter -> (string)

A container for the delimiter of the selection criteria being used.

MaxDepth -> (integer)

The max depth of the selection criteria

MinStorageBytesPercentage -> (double)

The minimum number of storage bytes percentage whose metrics will be selected.

### Note

You must choose a value greater than or equal to `1.0` .

AdvancedCostOptimizationMetrics -> (structure)

A container for bucket-level advanced cost-optimization metrics for S3 Storage Lens.

IsEnabled -> (boolean)

A container that indicates whether advanced cost-optimization metrics are enabled.

AdvancedDataProtectionMetrics -> (structure)

A container for bucket-level advanced data-protection metrics for S3 Storage Lens.

IsEnabled -> (boolean)

A container that indicates whether advanced data-protection metrics are enabled.

DetailedStatusCodesMetrics -> (structure)

A container for bucket-level detailed status code metrics for S3 Storage Lens.

IsEnabled -> (boolean)

A container that indicates whether detailed status code metrics are enabled.

AdvancedCostOptimizationMetrics -> (structure)

A container element for S3 Storage Lens advanced cost-optimization metrics.

IsEnabled -> (boolean)

A container that indicates whether advanced cost-optimization metrics are enabled.

AdvancedDataProtectionMetrics -> (structure)

A container element for S3 Storage Lens advanced data-protection metrics.

IsEnabled -> (boolean)

A container that indicates whether advanced data-protection metrics are enabled.

DetailedStatusCodesMetrics -> (structure)

A container element for detailed status code metrics.

IsEnabled -> (boolean)

A container that indicates whether detailed status code metrics are enabled.

StorageLensGroupLevel -> (structure)

A container element for S3 Storage Lens groups metrics.

SelectionCriteria -> (structure)

Indicates which Storage Lens group ARNs to include or exclude in the Storage Lens group aggregation. If this value is left null, then all Storage Lens groups are selected.

Include -> (list)

Indicates which Storage Lens group ARNs to include in the Storage Lens group aggregation.

(string)

Exclude -> (list)

Indicates which Storage Lens group ARNs to exclude from the Storage Lens group aggregation.

(string)

Include -> (structure)

A container for what is included in this configuration. This container can only be valid if there is no `Exclude` container submitted, and itâs not empty.

Buckets -> (list)

A container for the S3 Storage Lens bucket includes.

(string)

Regions -> (list)

A container for the S3 Storage Lens Region includes.

(string)

Exclude -> (structure)

A container for what is excluded in this configuration. This container can only be valid if there is no `Include` container submitted, and itâs not empty.

Buckets -> (list)

A container for the S3 Storage Lens bucket excludes.

(string)

Regions -> (list)

A container for the S3 Storage Lens Region excludes.

(string)

DataExport -> (structure)

A container to specify the properties of your S3 Storage Lens metrics export including, the destination, schema and format.

S3BucketDestination -> (structure)

A container for the bucket where the S3 Storage Lens metrics export will be located.

### Note

This bucket must be located in the same Region as the storage lens configuration.

Format -> (string)

OutputSchemaVersion -> (string)

The schema version of the export file.

AccountId -> (string)

The account ID of the owner of the S3 Storage Lens metrics export bucket.

Arn -> (string)

The Amazon Resource Name (ARN) of the bucket. This property is read-only and follows the following format: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-storage-lens-configuration.html#id1)arn:aws:s3:*us-east-1* :*example-account-id* :bucket/*your-destination-bucket-name* ``

Prefix -> (string)

The prefix of the destination bucket where the metrics export will be delivered.

Encryption -> (structure)

The container for the type encryption of the metrics exports in this bucket.

SSES3 -> (structure)

SSEKMS -> (structure)

KeyId -> (string)

A container for the ARN of the SSE-KMS encryption. This property is read-only and follows the following format: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-storage-lens-configuration.html#id3)arn:aws:kms:*us-east-1* :*example-account-id* :key/*example-9a73-4afc-8d29-8f5900cef44e* ``

CloudWatchMetrics -> (structure)

A container for enabling Amazon CloudWatch publishing for S3 Storage Lens metrics.

IsEnabled -> (boolean)

A container that indicates whether CloudWatch publishing for S3 Storage Lens metrics is enabled. A value of `true` indicates that CloudWatch publishing for S3 Storage Lens metrics is enabled.

IsEnabled -> (boolean)

A container for whether the S3 Storage Lens configuration is enabled.

AwsOrg -> (structure)

A container for the Amazon Web Services organization for this S3 Storage Lens configuration.

Arn -> (string)

A container for the Amazon Resource Name (ARN) of the Amazon Web Services organization. This property is read-only and follows the following format: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-storage-lens-configuration.html#id5)arn:aws:organizations:*us-east-1* :*example-account-id* :organization/*o-ex2l495dck* ``

StorageLensArn -> (string)

The Amazon Resource Name (ARN) of the S3 Storage Lens configuration. This property is read-only and follows the following format: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-storage-lens-configuration.html#id7)arn:aws:s3:*us-east-1* :*example-account-id* :storage-lens/*your-dashboard-name* ``