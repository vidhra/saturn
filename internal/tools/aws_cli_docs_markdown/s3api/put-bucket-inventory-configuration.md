# put-bucket-inventory-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-inventory-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-inventory-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html#cli-aws-s3api) ]

# put-bucket-inventory-configuration

## Description

### Note

This operation is not supported for directory buckets.

This implementation of the `PUT` action adds an inventory configuration (identified by the inventory ID) to the bucket. You can have up to 1,000 inventory configurations per bucket.

Amazon S3 inventory generates inventories of the objects in the bucket on a daily or weekly basis, and the results are published to a flat file. The bucket that is inventoried is called the *source* bucket, and the bucket where the inventory flat file is stored is called the *destination* bucket. The *destination* bucket must be in the same Amazon Web Services Region as the *source* bucket.

When you configure an inventory for a *source* bucket, you specify the *destination* bucket where you want the inventory to be stored, and whether to generate the inventory daily or weekly. You can also configure what object metadata to include and whether to inventory all object versions or only current versions. For more information, see [Amazon S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html) in the Amazon S3 User Guide.

### Warning

You must create a bucket policy on the *destination* bucket to grant permissions to Amazon S3 to write objects to the bucket in the defined location. For an example policy, see [Granting Permissions for Amazon S3 Inventory and Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-9) .

Permissions

To use this operation, you must have permission to perform the `s3:PutInventoryConfiguration` action. The bucket owner has this permission by default and can grant this permission to others.

The `s3:PutInventoryConfiguration` permission allows a user to create an [S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html) report that includes all object metadata fields available and to specify the destination bucket to store the inventory. A user with read access to objects in the destination bucket can also access all object metadata fields that are available in the inventory report.

To restrict access to an inventory report, see [Restricting access to an Amazon S3 Inventory report](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html#example-bucket-policies-use-case-10) in the *Amazon S3 User Guide* . For more information about the metadata fields available in S3 Inventory, see [Amazon S3 Inventory lists](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html#storage-inventory-contents) in the *Amazon S3 User Guide* . For more information about permissions, see [Permissions related to bucket subresource operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Identity and access management in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) in the *Amazon S3 User Guide* .

`PutBucketInventoryConfiguration` has the following special errors:

HTTP 400 Bad Request Error

*Code:* InvalidArgument

*Cause:* Invalid Argument

HTTP 400 Bad Request Error

*Code:* TooManyConfigurations

*Cause:* You are attempting to create a new configuration but have already reached the 1,000-configuration limit.

HTTP 403 Forbidden Error

*Cause:* You are not the owner of the specified bucket, or you do not have the `s3:PutInventoryConfiguration` bucket permission to set the configuration on the bucket.

The following operations are related to `PutBucketInventoryConfiguration` :

- [GetBucketInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketInventoryConfiguration.html)
- [DeleteBucketInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketInventoryConfiguration.html)
- [ListBucketInventoryConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketInventoryConfigurations.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketInventoryConfiguration)

## Synopsis

```
put-bucket-inventory-configuration
--bucket <value>
--id <value>
--inventory-configuration <value>
[--expected-bucket-owner <value>]
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

`--bucket` (string)

The name of the bucket where the inventory configuration will be stored.

`--id` (string)

The ID used to identify the inventory configuration.

`--inventory-configuration` (structure)

Specifies the inventory configuration.

Destination -> (structure)

Contains information about where to publish the inventory results.

S3BucketDestination -> (structure)

Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where inventory results are published.

AccountId -> (string)

The account ID that owns the destination S3 bucket. If no account ID is provided, the owner is not validated before exporting data.

### Note

Although this value is optional, we strongly recommend that you set it to help prevent problems if the destination bucket ownership changes.

Bucket -> (string)

The Amazon Resource Name (ARN) of the bucket where inventory results will be published.

Format -> (string)

Specifies the output format of the inventory results.

Prefix -> (string)

The prefix that is prepended to all inventory results.

Encryption -> (structure)

Contains the type of server-side encryption used to encrypt the inventory results.

SSES3 -> (structure)

Specifies the use of SSE-S3 to encrypt delivered inventory reports.

SSEKMS -> (structure)

Specifies the use of SSE-KMS to encrypt delivered inventory reports.

KeyId -> (string)

Specifies the ID of the Key Management Service (KMS) symmetric encryption customer managed key to use for encrypting inventory reports.

IsEnabled -> (boolean)

Specifies whether the inventory is enabled or disabled. If set to `True` , an inventory list is generated. If set to `False` , no inventory list is generated.

Filter -> (structure)

Specifies an inventory filter. The inventory only includes objects that meet the filterâs criteria.

Prefix -> (string)

The prefix that an object must have to be included in the inventory results.

Id -> (string)

The ID used to identify the inventory configuration.

IncludedObjectVersions -> (string)

Object versions to include in the inventory list. If set to `All` , the list includes all the object versions, which adds the version-related fields `VersionId` , `IsLatest` , and `DeleteMarker` to the list. If set to `Current` , the list does not contain these version-related fields.

OptionalFields -> (list)

Contains the optional fields that are included in the inventory results.

(string)

Schedule -> (structure)

Specifies the schedule for generating inventory results.

Frequency -> (string)

Specifies how frequently inventory results are produced.

JSON Syntax:

```
{
  "Destination": {
    "S3BucketDestination": {
      "AccountId": "string",
      "Bucket": "string",
      "Format": "CSV"|"ORC"|"Parquet",
      "Prefix": "string",
      "Encryption": {
        "SSES3": {

        },
        "SSEKMS": {
          "KeyId": "string"
        }
      }
    }
  },
  "IsEnabled": true|false,
  "Filter": {
    "Prefix": "string"
  },
  "Id": "string",
  "IncludedObjectVersions": "All"|"Current",
  "OptionalFields": ["Size"|"LastModifiedDate"|"StorageClass"|"ETag"|"IsMultipartUploaded"|"ReplicationStatus"|"EncryptionStatus"|"ObjectLockRetainUntilDate"|"ObjectLockMode"|"ObjectLockLegalHoldStatus"|"IntelligentTieringAccessTier"|"BucketKeyStatus"|"ChecksumAlgorithm"|"ObjectAccessControlList"|"ObjectOwner", ...],
  "Schedule": {
    "Frequency": "Daily"|"Weekly"
  }
}
```

`--expected-bucket-owner` (string)

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To set an inventory configuration for a bucket**

The following `put-bucket-inventory-configuration` example sets a weekly ORC-formatted inventory report for the bucket `amzn-s3-demo-bucket`.

```
aws s3api put-bucket-inventory-configuration \
    --bucket amzn-s3-demo-bucket \
    --id 1 \
    --inventory-configuration '{"Destination": { "S3BucketDestination": { "AccountId": "123456789012", "Bucket": "arn:aws:s3:::amzn-s3-demo-bucket", "Format": "ORC" }}, "IsEnabled": true, "Id": "1", "IncludedObjectVersions": "Current", "Schedule": { "Frequency": "Weekly" }}'
```

This command produces no output.

**Example 2: To set an inventory configuration for a bucket**

The following `put-bucket-inventory-configuration` example sets a daily CSV-formatted inventory report for the bucket `amzn-s3-demo-bucket`.

```
aws s3api put-bucket-inventory-configuration \
    --bucket amzn-s3-demo-bucket \
    --id 2 \
    --inventory-configuration '{"Destination": { "S3BucketDestination": { "AccountId": "123456789012", "Bucket": "arn:aws:s3:::amzn-s3-demo-bucket", "Format": "CSV" }}, "IsEnabled": true, "Id": "2", "IncludedObjectVersions": "Current", "Schedule": { "Frequency": "Daily" }}'
```

This command produces no output.

## Output

None