# get-object-attributesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-attributes.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-attributes.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html#cli-aws-s3api) ]

# get-object-attributes

## Description

Retrieves all the metadata from an object without returning the object itself. This operation is useful if youâre interested only in an objectâs metadata.

`GetObjectAttributes` combines the functionality of `HeadObject` and `ListParts` . All of the data returned with each of those individual calls can be returned with a single call to `GetObjectAttributes` .

### Note

**Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-attributes.html#id1)[https://](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-attributes.html)*amzn-s3-demo-bucket* .s3express-*zone-id* .*region-code* .amazonaws.com/*key-name* `` . Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the *Amazon S3 User Guide* . For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the *Amazon S3 User Guide* .

Permissions

- **General purpose bucket permissions** - To use `GetObjectAttributes` , you must have READ access to the object. The permissions that you need to use this operation depend on whether the bucket is versioned. If the bucket is versioned, you need both the `s3:GetObjectVersion` and `s3:GetObjectVersionAttributes` permissions for this operation. If the bucket is not versioned, you need the `s3:GetObject` and `s3:GetObjectAttributes` permissions. For more information, see [Specifying Permissions in a Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html) in the *Amazon S3 User Guide* . If the object that you request does not exist, the error Amazon S3 returns depends on whether you also have the `s3:ListBucket` permission.

- If you have the `s3:ListBucket` permission on the bucket, Amazon S3 returns an HTTP status code `404 Not Found` (âno such keyâ) error.
- If you donât have the `s3:ListBucket` permission, Amazon S3 returns an HTTP status code `403 Forbidden` (âaccess deniedâ) error.
- **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the ` `CreateSession` [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession).html`__ API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use. Amazon Web Services CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see ` `CreateSession` [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession).html`__ . If the object is encrypted with SSE-KMS, you must also have the `kms:GenerateDataKey` and `kms:Decrypt` permissions in IAM identity-based policies and KMS key policies for the KMS key.

Encryption

### Note

Encryption request headers, like `x-amz-server-side-encryption` , should not be sent for `HEAD` requests if your object uses server-side encryption with Key Management Service (KMS) keys (SSE-KMS), dual-layer server-side encryption with Amazon Web Services KMS keys (DSSE-KMS), or server-side encryption with Amazon S3 managed encryption keys (SSE-S3). The `x-amz-server-side-encryption` header is used when you `PUT` an object to S3 and want to specify the encryption method. If you include this header in a `GET` request for an object that uses these types of keys, youâll get an HTTP `400 Bad Request` error. Itâs because the encryption method canât be changed when you retrieve the object.

If you encrypt an object by using server-side encryption with customer-provided encryption keys (SSE-C) when you store the object in Amazon S3, then when you retrieve the metadata from the object, you must use the following headers to provide the encryption key for the server to be able to retrieve the objectâs metadata. The headers are:

- `x-amz-server-side-encryption-customer-algorithm`
- `x-amz-server-side-encryption-customer-key`
- `x-amz-server-side-encryption-customer-key-MD5`

For more information about SSE-C, see [Server-Side Encryption (Using Customer-Provided Encryption Keys)](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the *Amazon S3 User Guide* .

### Note

**Directory bucket permissions** - For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (`AES256` ) and server-side encryption with KMS keys (SSE-KMS) (`aws:kms` ). We recommend that the bucketâs default encryption uses the desired encryption configuration and you donât override the bucket default encryption in your `CreateSession` requests or `PUT` object requests. Then, new objects are automatically encrypted with the desired encryption settings. For more information, see [Protecting data with server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-serv-side-encryption.html) in the *Amazon S3 User Guide* . For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with KMS for new object uploads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-specifying-kms-encryption.html) .

Versioning

**Directory buckets** - S3 Versioning isnât enabled and supported for directory buckets. For this API operation, only the `null` value of the version ID is supported by directory buckets. You can only specify `null` to the `versionId` query parameter in the request.

Conditional request headers

Consider the following when using request headers:

- If both of the `If-Match` and `If-Unmodified-Since` headers are present in the request as follows, then Amazon S3 returns the HTTP status code `200 OK` and the data requested:
- `If-Match` condition evaluates to `true` .
- `If-Unmodified-Since` condition evaluates to `false` .

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232) .

- If both of the `If-None-Match` and `If-Modified-Since` headers are present in the request as follows, then Amazon S3 returns the HTTP status code `304 Not Modified` :
- `If-None-Match` condition evaluates to `false` .
- `If-Modified-Since` condition evaluates to `true` .

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232) .

HTTP Host header syntax

**Directory buckets** - The HTTP Host header syntax is `` *Bucket-name* .s3express-*zone-id* .*region-code* .amazonaws.com`` .

The following actions are related to `GetObjectAttributes` :

- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
- [GetObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html)
- [GetObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLegalHold.html)
- [GetObjectLockConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLockConfiguration.html)
- [GetObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectRetention.html)
- [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html)
- [HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html)
- [ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObjectAttributes)

## Synopsis

```
get-object-attributes
--bucket <value>
--key <value>
[--version-id <value>]
[--max-parts <value>]
[--part-number-marker <value>]
[--sse-customer-algorithm <value>]
[--sse-customer-key <value>]
[--sse-customer-key-md5 <value>]
[--request-payer <value>]
[--expected-bucket-owner <value>]
--object-attributes <value>
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

The name of the bucket that contains the object.

**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `` *Bucket-name* .s3express-*zone-id* .*region-code* .amazonaws.com`` . Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `` *bucket-base-name* â*zone-id* âx-s3`` (for example, `` *amzn-s3-demo-bucket* â*usw2-az1* âx-s3`` ). For information about bucket naming restrictions, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide* .

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName* -*AccountId* .s3-accesspoint.*Region* .amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide* .

### Note

Object Lambda access points are not supported by directory buckets.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form `` *AccessPointName* -*AccountId* .*outpostID* .s3-outposts.*Region* .amazonaws.com`` . When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide* .

`--key` (string)

The object key.

`--version-id` (string)

The version ID used to reference a specific version of the object.

### Note

S3 Versioning isnât enabled and supported for directory buckets. For this API operation, only the `null` value of the version ID is supported by directory buckets. You can only specify `null` to the `versionId` query parameter in the request.

`--max-parts` (integer)

Sets the maximum number of parts to return.

`--part-number-marker` (integer)

Specifies the part after which listing should begin. Only parts with higher part numbers will be listed.

`--sse-customer-algorithm` (string)

Specifies the algorithm to use when encrypting the object (for example, AES256).

### Note

This functionality is not supported for directory buckets.

`--sse-customer-key` (string)

Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the `x-amz-server-side-encryption-customer-algorithm` header.

### Note

This functionality is not supported for directory buckets.

`--sse-customer-key-md5` (string)

Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.

### Note

This functionality is not supported for directory buckets.

`--request-payer` (string)

Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for corresponding charges to copy the object. For information about downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported for directory buckets.

Possible values:

- `requester`

`--expected-bucket-owner` (string)

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

`--object-attributes` (list)

Specifies the fields at the root level that you want returned in the response. Fields that you do not specify are not returned.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  ETag
  Checksum
  ObjectParts
  StorageClass
  ObjectSize
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To retrieves metadata from an object without returning the object itself**

The following `get-object-attributes` example retrieves metadata from the object `doc1.rtf`.

```
aws s3api get-object-attributes \
    --bucket amzn-s3-demo-bucket \
    --key doc1.rtf \
    --object-attributes "StorageClass" "ETag" "ObjectSize"
```

Output:

```
{
    "LastModified": "2022-03-15T19:37:31+00:00",
    "VersionId": "IuCPjXTDzHNfldAuitVBIKJpF2p1fg4P",
    "ETag": "b662d79adeb7c8d787ea7eafb9ef6207",
    "StorageClass": "STANDARD",
    "ObjectSize": 405
}
```

For more information, see [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html) in the Amazon S3 API Reference.

## Output

DeleteMarker -> (boolean)

Specifies whether the object retrieved was (`true` ) or was not (`false` ) a delete marker. If `false` , this response header does not appear in the response. To learn more about delete markers, see [Working with delete markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html) .

### Note

This functionality is not supported for directory buckets.

LastModified -> (timestamp)

Date and time when the object was last modified.

VersionId -> (string)

The version ID of the object.

### Note

This functionality is not supported for directory buckets.

RequestCharged -> (string)

If present, indicates that the requester was successfully charged for the request.

### Note

This functionality is not supported for directory buckets.

ETag -> (string)

An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL.

Checksum -> (structure)

The checksum or digest of the object.

ChecksumCRC32 -> (string)

The Base64 encoded, 32-bit `CRC32 checksum` of the object. This checksum is only be present if the checksum was uploaded with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, itâs a calculation based on the checksum values of each individual part. For more information about how checksums are calculated with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide* .

ChecksumCRC32C -> (string)

The Base64 encoded, 32-bit `CRC32C` checksum of the object. This checksum is only present if the checksum was uploaded with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, itâs a calculation based on the checksum values of each individual part. For more information about how checksums are calculated with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide* .

ChecksumCRC64NVME -> (string)

The Base64 encoded, 64-bit `CRC64NVME` checksum of the object. This checksum is present if the object was uploaded with the `CRC64NVME` checksum algorithm, or if the object was uploaded without a checksum (and Amazon S3 added the default checksum, `CRC64NVME` , to the uploaded object). For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ChecksumSHA1 -> (string)

The Base64 encoded, 160-bit `SHA1` digest of the object. This will only be present if the object was uploaded with the object. When you use the API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, itâs a calculation based on the checksum values of each individual part. For more information about how checksums are calculated with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide* .

ChecksumSHA256 -> (string)

The Base64 encoded, 256-bit `SHA256` digest of the object. This will only be present if the object was uploaded with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, itâs a calculation based on the checksum values of each individual part. For more information about how checksums are calculated with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide* .

ChecksumType -> (string)

The checksum type that is used to calculate the objectâs checksum value. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ObjectParts -> (structure)

A collection of parts associated with a multipart upload.

TotalPartsCount -> (integer)

The total number of parts.

PartNumberMarker -> (integer)

The marker for the current part.

NextPartNumberMarker -> (integer)

When a list is truncated, this element specifies the last part in the list, as well as the value to use for the `PartNumberMarker` request parameter in a subsequent request.

MaxParts -> (integer)

The maximum number of parts allowed in the response.

IsTruncated -> (boolean)

Indicates whether the returned list of parts is truncated. A value of `true` indicates that the list was truncated. A list can be truncated if the number of parts exceeds the limit returned in the `MaxParts` element.

Parts -> (list)

A container for elements related to a particular part. A response can contain zero or more `Parts` elements.

### Note

- **General purpose buckets** - For `GetObjectAttributes` , if a additional checksum (including `x-amz-checksum-crc32` , `x-amz-checksum-crc32c` , `x-amz-checksum-sha1` , or `x-amz-checksum-sha256` ) isnât applied to the object specified in the request, the response doesnât return `Part` .
- **Directory buckets** - For `GetObjectAttributes` , no matter whether a additional checksum is applied to the object specified in the request, the response returns `Part` .

(structure)

A container for elements related to an individual part.

PartNumber -> (integer)

The part number identifying the part. This value is a positive integer between 1 and 10,000.

Size -> (long)

The size of the uploaded part in bytes.

ChecksumCRC32 -> (string)

The Base64 encoded, 32-bit `CRC32` checksum of the part. This checksum is present if the multipart upload request was created with the `CRC32` checksum algorithm. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ChecksumCRC32C -> (string)

The Base64 encoded, 32-bit `CRC32C` checksum of the part. This checksum is present if the multipart upload request was created with the `CRC32C` checksum algorithm. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ChecksumCRC64NVME -> (string)

The Base64 encoded, 64-bit `CRC64NVME` checksum of the part. This checksum is present if the multipart upload request was created with the `CRC64NVME` checksum algorithm, or if the object was uploaded without a checksum (and Amazon S3 added the default checksum, `CRC64NVME` , to the uploaded object). For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ChecksumSHA1 -> (string)

The Base64 encoded, 160-bit `SHA1` checksum of the part. This checksum is present if the multipart upload request was created with the `SHA1` checksum algorithm. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ChecksumSHA256 -> (string)

The Base64 encoded, 256-bit `SHA256` checksum of the part. This checksum is present if the multipart upload request was created with the `SHA256` checksum algorithm. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

StorageClass -> (string)

Provides the storage class information of the object. Amazon S3 returns this header for all objects except for S3 Standard storage class objects.

For more information, see [Storage Classes](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html) .

### Note

**Directory buckets** - Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.

ObjectSize -> (long)

The size of the object in bytes.