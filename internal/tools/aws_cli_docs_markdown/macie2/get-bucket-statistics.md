# get-bucket-statisticsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-bucket-statistics.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-bucket-statistics.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [macie2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/index.html#cli-aws-macie2) ]

# get-bucket-statistics

## Description

Retrieves (queries) aggregated statistical data about all the S3 buckets that Amazon Macie monitors and analyzes for an account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/macie2-2020-01-01/GetBucketStatistics)

## Synopsis

```
get-bucket-statistics
[--account-id <value>]
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

`--account-id` (string)

The unique identifier for the Amazon Web Services account.

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

bucketCount -> (long)

The total number of buckets.

bucketCountByEffectivePermission -> (structure)

The total number of buckets that are publicly accessible due to a combination of permissions settings for each bucket.

publiclyAccessible -> (long)

The total number of buckets that allow the general public to have read or write access to the bucket.

publiclyReadable -> (long)

The total number of buckets that allow the general public to have read access to the bucket.

publiclyWritable -> (long)

The total number of buckets that allow the general public to have write access to the bucket.

unknown -> (long)

The total number of buckets that Amazon Macie wasnât able to evaluate permissions settings for. For example, the bucketsâ policies or a quota prevented Macie from retrieving the requisite data. Macie canât determine whether the buckets are publicly accessible.

bucketCountByEncryptionType -> (structure)

The total number of buckets whose settings do or donât specify default server-side encryption behavior for objects that are added to the buckets.

kmsManaged -> (long)

The total number of buckets whose default encryption settings are configured to encrypt new objects with an KMS key, either an Amazon Web Services managed key or a customer managed key. By default, these buckets encrypt new objects automatically using DSSE-KMS or SSE-KMS encryption.

s3Managed -> (long)

The total number of buckets whose default encryption settings are configured to encrypt new objects with an Amazon S3 managed key. By default, these buckets encrypt new objects automatically using SSE-S3 encryption.

unencrypted -> (long)

The total number of buckets that donât specify default server-side encryption behavior for new objects. Default encryption settings arenât configured for these buckets.

unknown -> (long)

The total number of buckets that Amazon Macie doesnât have current encryption metadata for. For example, the bucketsâ permissions settings or a quota prevented Macie from retrieving the default encryption settings for the buckets.

bucketCountByObjectEncryptionRequirement -> (structure)

The total number of buckets whose bucket policies do or donât require server-side encryption of objects when objects are added to the buckets.

allowsUnencryptedObjectUploads -> (long)

The total number of buckets that donât have a bucket policy or have a bucket policy that doesnât require server-side encryption of new objects. If a bucket policy exists, the policy doesnât require PutObject requests to include a valid server-side encryption header: the x-amz-server-side-encryption header with a value of AES256 or aws:kms, or the x-amz-server-side-encryption-customer-algorithm header with a value of AES256.

deniesUnencryptedObjectUploads -> (long)

The total number of buckets whose bucket policies require server-side encryption of new objects. PutObject requests for these buckets must include a valid server-side encryption header: the x-amz-server-side-encryption header with a value of AES256 or aws:kms, or the x-amz-server-side-encryption-customer-algorithm header with a value of AES256.

unknown -> (long)

The total number of buckets that Amazon Macie wasnât able to evaluate server-side encryption requirements for. For example, the bucketsâ permissions settings or a quota prevented Macie from retrieving the requisite data. Macie canât determine whether bucket policies for the buckets require server-side encryption of new objects.

bucketCountBySharedAccessType -> (structure)

The total number of buckets that are or arenât shared with other Amazon Web Services accounts, Amazon CloudFront origin access identities (OAIs), or CloudFront origin access controls (OACs).

external -> (long)

The total number of buckets that are shared with one or more of the following or any combination of the following: an Amazon CloudFront OAI, a CloudFront OAC, or an Amazon Web Services account that isnât in the same Amazon Macie organization.

internal -> (long)

The total number of buckets that are shared with one or more Amazon Web Services accounts in the same Amazon Macie organization. These buckets arenât shared with Amazon CloudFront OAIs or OACs.

notShared -> (long)

The total number of buckets that arenât shared with other Amazon Web Services accounts, Amazon CloudFront OAIs, or CloudFront OACs.

unknown -> (long)

The total number of buckets that Amazon Macie wasnât able to evaluate shared access settings for. For example, the bucketsâ permissions settings or a quota prevented Macie from retrieving the requisite data. Macie canât determine whether the buckets are shared with other Amazon Web Services accounts, Amazon CloudFront OAIs, or CloudFront OACs.

bucketStatisticsBySensitivity -> (structure)

The aggregated sensitive data discovery statistics for the buckets. If automated sensitive data discovery is currently disabled for your account, the value for most statistics is 0.

classificationError -> (structure)

The aggregated statistical data for all buckets that have a sensitivity score of -1.

classifiableSizeInBytes -> (long)

The total storage size, in bytes, of all the objects that Amazon Macie can analyze in the buckets. These objects use a supported storage class and have a file name extension for a supported file or storage format.

If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each applicable object in the buckets. This value doesnât reflect the storage size of all versions of all applicable objects in the buckets.

publiclyAccessibleCount -> (long)

The total number of buckets that are publicly accessible due to a combination of permissions settings for each bucket.

totalCount -> (long)

The total number of buckets.

totalSizeInBytes -> (long)

The total storage size, in bytes, of the buckets.

If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each object in the buckets. This value doesnât reflect the storage size of all versions of the objects in the buckets.

notClassified -> (structure)

The aggregated statistical data for all buckets that have a sensitivity score of 50.

classifiableSizeInBytes -> (long)

The total storage size, in bytes, of all the objects that Amazon Macie can analyze in the buckets. These objects use a supported storage class and have a file name extension for a supported file or storage format.

If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each applicable object in the buckets. This value doesnât reflect the storage size of all versions of all applicable objects in the buckets.

publiclyAccessibleCount -> (long)

The total number of buckets that are publicly accessible due to a combination of permissions settings for each bucket.

totalCount -> (long)

The total number of buckets.

totalSizeInBytes -> (long)

The total storage size, in bytes, of the buckets.

If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each object in the buckets. This value doesnât reflect the storage size of all versions of the objects in the buckets.

notSensitive -> (structure)

The aggregated statistical data for all buckets that have a sensitivity score of 1-49.

classifiableSizeInBytes -> (long)

The total storage size, in bytes, of all the objects that Amazon Macie can analyze in the buckets. These objects use a supported storage class and have a file name extension for a supported file or storage format.

If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each applicable object in the buckets. This value doesnât reflect the storage size of all versions of all applicable objects in the buckets.

publiclyAccessibleCount -> (long)

The total number of buckets that are publicly accessible due to a combination of permissions settings for each bucket.

totalCount -> (long)

The total number of buckets.

totalSizeInBytes -> (long)

The total storage size, in bytes, of the buckets.

If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each object in the buckets. This value doesnât reflect the storage size of all versions of the objects in the buckets.

sensitive -> (structure)

The aggregated statistical data for all buckets that have a sensitivity score of 51-100.

classifiableSizeInBytes -> (long)

The total storage size, in bytes, of all the objects that Amazon Macie can analyze in the buckets. These objects use a supported storage class and have a file name extension for a supported file or storage format.

If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each applicable object in the buckets. This value doesnât reflect the storage size of all versions of all applicable objects in the buckets.

publiclyAccessibleCount -> (long)

The total number of buckets that are publicly accessible due to a combination of permissions settings for each bucket.

totalCount -> (long)

The total number of buckets.

totalSizeInBytes -> (long)

The total storage size, in bytes, of the buckets.

If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each object in the buckets. This value doesnât reflect the storage size of all versions of the objects in the buckets.

classifiableObjectCount -> (long)

The total number of objects that Amazon Macie can analyze in the buckets. These objects use a supported storage class and have a file name extension for a supported file or storage format.

classifiableSizeInBytes -> (long)

The total storage size, in bytes, of all the objects that Amazon Macie can analyze in the buckets. These objects use a supported storage class and have a file name extension for a supported file or storage format.

If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each applicable object in the buckets. This value doesnât reflect the storage size of all versions of all applicable objects in the buckets.

lastUpdated -> (timestamp)

The date and time, in UTC and extended ISO 8601 format, when Amazon Macie most recently retrieved bucket or object metadata from Amazon S3 for the buckets.

objectCount -> (long)

The total number of objects in the buckets.

sizeInBytes -> (long)

The total storage size, in bytes, of the buckets.

If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each object in the buckets. This value doesnât reflect the storage size of all versions of the objects in the buckets.

sizeInBytesCompressed -> (long)

The total storage size, in bytes, of the objects that are compressed (.gz, .gzip, .zip) files in the buckets.

If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each applicable object in the buckets. This value doesnât reflect the storage size of all versions of the applicable objects in the buckets.

unclassifiableObjectCount -> (structure)

The total number of objects that Amazon Macie canât analyze in the buckets. These objects donât use a supported storage class or donât have a file name extension for a supported file or storage format.

fileType -> (long)

The total storage size (in bytes) or number of objects that Amazon Macie canât analyze because the objects donât have a file name extension for a supported file or storage format.

storageClass -> (long)

The total storage size (in bytes) or number of objects that Amazon Macie canât analyze because the objects use an unsupported storage class.

total -> (long)

The total storage size (in bytes) or number of objects that Amazon Macie canât analyze because the objects use an unsupported storage class or donât have a file name extension for a supported file or storage format.

unclassifiableObjectSizeInBytes -> (structure)

The total storage size, in bytes, of the objects that Amazon Macie canât analyze in the buckets. These objects donât use a supported storage class or donât have a file name extension for a supported file or storage format.

fileType -> (long)

The total storage size (in bytes) or number of objects that Amazon Macie canât analyze because the objects donât have a file name extension for a supported file or storage format.

storageClass -> (long)

The total storage size (in bytes) or number of objects that Amazon Macie canât analyze because the objects use an unsupported storage class.

total -> (long)

The total storage size (in bytes) or number of objects that Amazon Macie canât analyze because the objects use an unsupported storage class or donât have a file name extension for a supported file or storage format.