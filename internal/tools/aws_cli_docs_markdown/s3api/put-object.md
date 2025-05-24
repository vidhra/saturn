# put-objectÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html#cli-aws-s3api) ]

# put-object

## Description

Adds an object to a bucket.

### Note

- Amazon S3 never adds partial objects; if you receive a success response, Amazon S3 added the entire object to the bucket. You cannot use `PutObject` to only update a single piece of metadata for an existing object. You must put the entire object with updated metadata if you want to update some values.
- If your bucket uses the bucket owner enforced setting for Object Ownership, ACLs are disabled and no longer affect permissions. All objects written to the bucket by any account will be owned by the bucket owner.
- **Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html#id1)[https://](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html)*amzn-s3-demo-bucket* .s3express-*zone-id* .*region-code* .amazonaws.com/*key-name* `` . Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the *Amazon S3 User Guide* . For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the *Amazon S3 User Guide* .

Amazon S3 is a distributed system. If it receives multiple write requests for the same object simultaneously, it overwrites all but the last object written. However, Amazon S3 provides features that can modify this behavior:

- **S3 Object Lock** - To prevent objects from being deleted or overwritten, you can use [Amazon S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported for directory buckets.

- **If-None-Match** - Uploads the object only if the object key name does not already exist in the specified bucket. Otherwise, Amazon S3 returns a `412 Precondition Failed` error. If a conflicting operation occurs during the upload, S3 returns a `409 ConditionalRequestConflict` response. On a 409 failure, retry the upload. Expects the * character (asterisk). For more information, see [Add preconditions to S3 operations with conditional requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html) in the *Amazon S3 User Guide* or [RFC 7232](https://datatracker.ietf.org/doc/rfc7232/) .

### Note

This functionality is not supported for S3 on Outposts.

- **S3 Versioning** - When you enable versioning for a bucket, if Amazon S3 receives multiple write requests for the same object simultaneously, it stores all versions of the objects. For each write request that is made to the same object, Amazon S3 automatically generates a unique version ID of that object being stored in Amazon S3. You can retrieve, replace, or delete any version of the object. For more information about versioning, see [Adding Objects to Versioning-Enabled Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/AddingObjectstoVersioningEnabledBuckets.html) in the *Amazon S3 User Guide* . For information about returning the versioning state of a bucket, see [GetBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html) .

### Note

This functionality is not supported for directory buckets.

Permissions

- **General purpose bucket permissions** - The following permissions are required in your policies when your `PutObject` request includes specific headers.

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html#id3)`s3:PutObject` ** - To successfully complete the `PutObject` request, you must always have the `s3:PutObject` permission on a bucket to add an object to it.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html#id5)`s3:PutObjectAcl` ** - To successfully change the objects ACL of your `PutObject` request, you must have the `s3:PutObjectAcl` .
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html#id7)`s3:PutObjectTagging` ** - To successfully set the tag-set with your `PutObject` request, you must have the `s3:PutObjectTagging` .
- **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the ` `CreateSession` [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession).html`__ API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use. Amazon Web Services CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see ` `CreateSession` [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession).html`__ . If the object is encrypted with SSE-KMS, you must also have the `kms:GenerateDataKey` and `kms:Decrypt` permissions in IAM identity-based policies and KMS key policies for the KMS key.

Data integrity with Content-MD5
- **General purpose bucket** - To ensure that data is not corrupted traversing the network, use the `Content-MD5` header. When you use this header, Amazon S3 checks the object against the provided MD5 value and, if they do not match, Amazon S3 returns an error. Alternatively, when the objectâs ETag is its MD5 digest, you can calculate the MD5 while putting the object to Amazon S3 and compare the returned ETag to the calculated MD5 value.
- **Directory bucket** - This functionality is not supported for directory buckets.

HTTP Host header syntax

**Directory buckets** - The HTTP Host header syntax is `` *Bucket-name* .s3express-*zone-id* .*region-code* .amazonaws.com`` .

For more information about related Amazon S3 APIs, see the following:

- [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html)
- [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObject)

## Synopsis

```
put-object
[--acl <value>]
[--body <value>]
--bucket <value>
[--cache-control <value>]
[--content-disposition <value>]
[--content-encoding <value>]
[--content-language <value>]
[--content-length <value>]
[--content-md5 <value>]
[--content-type <value>]
[--checksum-algorithm <value>]
[--checksum-crc32 <value>]
[--checksum-crc32-c <value>]
[--checksum-crc64-nvme <value>]
[--checksum-sha1 <value>]
[--checksum-sha256 <value>]
[--expires <value>]
[--if-match <value>]
[--if-none-match <value>]
[--grant-full-control <value>]
[--grant-read <value>]
[--grant-read-acp <value>]
[--grant-write-acp <value>]
--key <value>
[--write-offset-bytes <value>]
[--metadata <value>]
[--server-side-encryption <value>]
[--storage-class <value>]
[--website-redirect-location <value>]
[--sse-customer-algorithm <value>]
[--sse-customer-key <value>]
[--sse-customer-key-md5 <value>]
[--ssekms-key-id <value>]
[--ssekms-encryption-context <value>]
[--bucket-key-enabled | --no-bucket-key-enabled]
[--request-payer <value>]
[--tagging <value>]
[--object-lock-mode <value>]
[--object-lock-retain-until-date <value>]
[--object-lock-legal-hold-status <value>]
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

`--acl` (string)

The canned ACL to apply to the object. For more information, see [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL) in the *Amazon S3 User Guide* .

When adding a new object, you can use headers to grant ACL-based permissions to individual Amazon Web Services accounts or to predefined groups defined by Amazon S3. These permissions are then added to the ACL on the object. By default, all objects are private. Only the owner has full access control. For more information, see [Access Control List (ACL) Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html) and [Managing ACLs Using the REST API](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-using-rest-api.html) in the *Amazon S3 User Guide* .

If the bucket that youâre uploading objects to uses the bucket owner enforced setting for S3 Object Ownership, ACLs are disabled and no longer affect permissions. Buckets that use this setting only accept PUT requests that donât specify an ACL or PUT requests that specify bucket owner full control ACLs, such as the `bucket-owner-full-control` canned ACL or an equivalent form of this ACL expressed in the XML format. PUT requests that contain other ACLs (for example, custom grants to certain Amazon Web Services accounts) fail and return a `400` error with the error code `AccessControlListNotSupported` . For more information, see [Controlling ownership of objects and disabling ACLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon S3 User Guide* .

### Note

- This functionality is not supported for directory buckets.
- This functionality is not supported for Amazon S3 on Outposts.

Possible values:

- `private`
- `public-read`
- `public-read-write`
- `authenticated-read`
- `aws-exec-read`
- `bucket-owner-read`
- `bucket-owner-full-control`

`--body` (streaming blob)

Object data.

### Note

This argument is of type: streaming blob. Its value must be the path to a file (e.g. `path/to/file`) and must **not** be prefixed with `file://` or `fileb://`

`--bucket` (string)

The bucket name to which the PUT action was initiated.

**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `` *Bucket-name* .s3express-*zone-id* .*region-code* .amazonaws.com`` . Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `` *bucket-base-name* â*zone-id* âx-s3`` (for example, `` *amzn-s3-demo-bucket* â*usw2-az1* âx-s3`` ). For information about bucket naming restrictions, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide* .

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName* -*AccountId* .s3-accesspoint.*Region* .amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide* .

### Note

Object Lambda access points are not supported by directory buckets.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form `` *AccessPointName* -*AccountId* .*outpostID* .s3-outposts.*Region* .amazonaws.com`` . When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide* .

`--cache-control` (string)

Can be used to specify caching behavior along the request/reply chain. For more information, see [http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) .

`--content-disposition` (string)

Specifies presentational information for the object. For more information, see [https://www.rfc-editor.org/rfc/rfc6266#section-4](https://www.rfc-editor.org/rfc/rfc6266#section-4) .

`--content-encoding` (string)

Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. For more information, see [https://www.rfc-editor.org/rfc/rfc9110.html#field.content-encoding](https://www.rfc-editor.org/rfc/rfc9110.html#field.content-encoding) .

`--content-language` (string)

The language the content is in.

`--content-length` (long)

Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically. For more information, see [https://www.rfc-editor.org/rfc/rfc9110.html#name-content-length](https://www.rfc-editor.org/rfc/rfc9110.html#name-content-length) .

`--content-md5` (string)

The Base64 encoded 128-bit `MD5` digest of the message (without the headers) according to RFC 1864. This header can be used as a message integrity check to verify that the data is the same data that was originally sent. Although it is optional, we recommend using the Content-MD5 mechanism as an end-to-end integrity check. For more information about REST request authentication, see [REST Authentication](https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html) .

### Note

The `Content-MD5` or `x-amz-sdk-checksum-algorithm` header is required for any request to upload an object with a retention period configured using Amazon S3 Object Lock. For more information, see [Uploading objects to an Object Lock enabled bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-managing.html#object-lock-put-object) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported for directory buckets.

`--content-type` (string)

A standard MIME type describing the format of the contents. For more information, see [https://www.rfc-editor.org/rfc/rfc9110.html#name-content-type](https://www.rfc-editor.org/rfc/rfc9110.html#name-content-type) .

`--checksum-algorithm` (string)

Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any additional functionality if you donât use the SDK. When you send this header, there must be a corresponding `x-amz-checksum-*algorithm* `` or ``x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request` .

For the [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html#id9)x-amz-checksum-*algorithm* `` header, replace `` *algorithm* `` with the supported algorithm from the following list:

- `CRC32`
- `CRC32C`
- `CRC64NVME`
- `SHA1`
- `SHA256`

For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

If the individual checksum value you provide through `x-amz-checksum-*algorithm* `` doesn't match the checksum algorithm you set through ``x-amz-sdk-checksum-algorithm` , Amazon S3 fails the request with a `BadDigest` error.

### Note

The `Content-MD5` or `x-amz-sdk-checksum-algorithm` header is required for any request to upload an object with a retention period configured using Amazon S3 Object Lock. For more information, see [Uploading objects to an Object Lock enabled bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-managing.html#object-lock-put-object) in the *Amazon S3 User Guide* .

For directory buckets, when you use Amazon Web Services SDKs, `CRC32` is the default checksum algorithm thatâs used for performance.

Possible values:

- `CRC32`
- `CRC32C`
- `SHA1`
- `SHA256`
- `CRC64NVME`

`--checksum-crc32` (string)

This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 32-bit `CRC32` checksum of the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

`--checksum-crc32-c` (string)

This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 32-bit `CRC32C` checksum of the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

`--checksum-crc64-nvme` (string)

This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 64-bit `CRC64NVME` checksum of the object. The `CRC64NVME` checksum is always a full object checksum. For more information, see [Checking object integrity in the Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) .

`--checksum-sha1` (string)

This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 160-bit `SHA1` digest of the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

`--checksum-sha256` (string)

This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 256-bit `SHA256` digest of the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

`--expires` (timestamp)

The date and time at which the object is no longer cacheable. For more information, see [https://www.rfc-editor.org/rfc/rfc7234#section-5.3](https://www.rfc-editor.org/rfc/rfc7234#section-5.3) .

`--if-match` (string)

Uploads the object only if the ETag (entity tag) value provided during the WRITE operation matches the ETag of the object in S3. If the ETag values do not match, the operation returns a `412 Precondition Failed` error.

If a conflicting operation occurs during the upload S3 returns a `409 ConditionalRequestConflict` response. On a 409 failure you should fetch the objectâs ETag and retry the upload.

Expects the ETag value as a string.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232) , or [Conditional requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html) in the *Amazon S3 User Guide* .

`--if-none-match` (string)

Uploads the object only if the object key name does not already exist in the bucket specified. Otherwise, Amazon S3 returns a `412 Precondition Failed` error.

If a conflicting operation occurs during the upload S3 returns a `409 ConditionalRequestConflict` response. On a 409 failure you should retry the upload.

Expects the â*â (asterisk) character.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232) , or [Conditional requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html) in the *Amazon S3 User Guide* .

`--grant-full-control` (string)

Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.

### Note

- This functionality is not supported for directory buckets.
- This functionality is not supported for Amazon S3 on Outposts.

`--grant-read` (string)

Allows grantee to read the object data and its metadata.

### Note

- This functionality is not supported for directory buckets.
- This functionality is not supported for Amazon S3 on Outposts.

`--grant-read-acp` (string)

Allows grantee to read the object ACL.

### Note

- This functionality is not supported for directory buckets.
- This functionality is not supported for Amazon S3 on Outposts.

`--grant-write-acp` (string)

Allows grantee to write the ACL for the applicable object.

### Note

- This functionality is not supported for directory buckets.
- This functionality is not supported for Amazon S3 on Outposts.

`--key` (string)

Object key for which the PUT action was initiated.

`--write-offset-bytes` (long)

Specifies the offset for appending data to existing objects in bytes. The offset must be equal to the size of the existing object being appended to. If no object exists, setting this header to 0 will create a new object.

### Note

This functionality is only supported for objects in the Amazon S3 Express One Zone storage class in directory buckets.

`--metadata` (map)

A map of metadata to store with the object in S3.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--server-side-encryption` (string)

The server-side encryption algorithm that was used when you store this object in Amazon S3 (for example, `AES256` , `aws:kms` , `aws:kms:dsse` ).

- **General purpose buckets** - You have four mutually exclusive options to protect data using server-side encryption in Amazon S3, depending on how you choose to manage the encryption keys. Specifically, the encryption key options are Amazon S3 managed keys (SSE-S3), Amazon Web Services KMS keys (SSE-KMS or DSSE-KMS), and customer-provided keys (SSE-C). Amazon S3 encrypts data with server-side encryption by using Amazon S3 managed keys (SSE-S3) by default. You can optionally tell Amazon S3 to encrypt data at rest by using server-side encryption with other key options. For more information, see [Using Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html) in the *Amazon S3 User Guide* .
- **Directory buckets** - For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (`AES256` ) and server-side encryption with KMS keys (SSE-KMS) (`aws:kms` ). We recommend that the bucketâs default encryption uses the desired encryption configuration and you donât override the bucket default encryption in your `CreateSession` requests or `PUT` object requests. Then, new objects are automatically encrypted with the desired encryption settings. For more information, see [Protecting data with server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-serv-side-encryption.html) in the *Amazon S3 User Guide* . For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with KMS for new object uploads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-specifying-kms-encryption.html) .  In the Zonal endpoint API calls (except [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) and [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html) ) using the REST API, the encryption request headers must match the encryption settings that are specified in the `CreateSession` request. You canât override the values of the encryption settings (`x-amz-server-side-encryption` , `x-amz-server-side-encryption-aws-kms-key-id` , `x-amz-server-side-encryption-context` , and `x-amz-server-side-encryption-bucket-key-enabled` ) that are specified in the `CreateSession` request. You donât need to explicitly specify these encryption settings values in Zonal endpoint API calls, and Amazon S3 will use the encryption settings values from the `CreateSession` request to protect new objects in the directory bucket.

### Note

When you use the CLI or the Amazon Web Services SDKs, for `CreateSession` , the session token refreshes automatically to avoid service interruptions when a session expires. The CLI or the Amazon Web Services SDKs use the bucketâs default encryption configuration for the `CreateSession` request. Itâs not supported to override the encryption settings values in the `CreateSession` request. So in the Zonal endpoint API calls (except [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) and [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html) ), the encryption request headers must match the default encryption configuration of the directory bucket.

Possible values:

- `AES256`
- `aws:kms`
- `aws:kms:dsse`

`--storage-class` (string)

By default, Amazon S3 uses the STANDARD Storage Class to store newly created objects. The STANDARD storage class provides high durability and high availability. Depending on performance needs, you can specify a different Storage Class. For more information, see [Storage Classes](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html) in the *Amazon S3 User Guide* .

### Note

- Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.
- Amazon S3 on Outposts only uses the OUTPOSTS Storage Class.

Possible values:

- `STANDARD`
- `REDUCED_REDUNDANCY`
- `STANDARD_IA`
- `ONEZONE_IA`
- `INTELLIGENT_TIERING`
- `GLACIER`
- `DEEP_ARCHIVE`
- `OUTPOSTS`
- `GLACIER_IR`
- `SNOW`
- `EXPRESS_ONEZONE`

`--website-redirect-location` (string)

If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata. For information about object metadata, see [Object Key and Metadata](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html) in the *Amazon S3 User Guide* .

In the following example, the request header sets the redirect to an object (anotherPage.html) in the same bucket:

`x-amz-website-redirect-location: /anotherPage.html`

In the following example, the request header sets the object redirect to another website:

`x-amz-website-redirect-location: http://www.example.com/`

For more information about website hosting in Amazon S3, see [Hosting Websites on Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) and [How to Configure Website Page Redirects](https://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported for directory buckets.

`--sse-customer-algorithm` (string)

Specifies the algorithm to use when encrypting the object (for example, `AES256` ).

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

`--ssekms-key-id` (string)

Specifies the KMS key ID (Key ID, Key ARN, or Key Alias) to use for object encryption. If the KMS key doesnât exist in the same account thatâs issuing the command, you must use the full Key ARN not the Key ID.

**General purpose buckets** - If you specify `x-amz-server-side-encryption` with `aws:kms` or `aws:kms:dsse` , this header specifies the ID (Key ID, Key ARN, or Key Alias) of the KMS key to use. If you specify `x-amz-server-side-encryption:aws:kms` or `x-amz-server-side-encryption:aws:kms:dsse` , but do not provide `x-amz-server-side-encryption-aws-kms-key-id` , Amazon S3 uses the Amazon Web Services managed key (`aws/s3` ) to protect the data.

**Directory buckets** - To encrypt data using SSE-KMS, itâs recommended to specify the `x-amz-server-side-encryption` header to `aws:kms` . Then, the `x-amz-server-side-encryption-aws-kms-key-id` header implicitly uses the bucketâs default KMS customer managed key ID. If you want to explicitly set the `x-amz-server-side-encryption-aws-kms-key-id` header, it must match the bucketâs default customer managed key (using key ID or ARN, not alias). Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) per directory bucketâs lifetime. The [Amazon Web Services managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) (`aws/s3` ) isnât supported. Incorrect key specification results in an HTTP `400 Bad Request` error.

`--ssekms-encryption-context` (string)

Specifies the Amazon Web Services KMS Encryption Context as an additional encryption context to use for object encryption. The value of this header is a Base64 encoded string of a UTF-8 encoded JSON, which contains the encryption context as key-value pairs. This value is stored as object metadata and automatically gets passed on to Amazon Web Services KMS for future `GetObject` operations on this object.

**General purpose buckets** - This value must be explicitly added during `CopyObject` operations if you want an additional encryption context for your object. For more information, see [Encryption context](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html#encryption-context) in the *Amazon S3 User Guide* .

**Directory buckets** - You can optionally provide an explicit encryption context value. The value must match the default encryption context - the bucket Amazon Resource Name (ARN). An additional encryption context value is not supported.

`--bucket-key-enabled` | `--no-bucket-key-enabled` (boolean)

Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with server-side encryption using Key Management Service (KMS) keys (SSE-KMS).

**General purpose buckets** - Setting this header to `true` causes Amazon S3 to use an S3 Bucket Key for object encryption with SSE-KMS. Also, specifying this header with a PUT action doesnât affect bucket-level settings for S3 Bucket Key.

**Directory buckets** - S3 Bucket Keys are always enabled for `GET` and `PUT` operations in a directory bucket and canât be disabled. S3 Bucket Keys arenât supported, when you copy SSE-KMS encrypted objects from general purpose buckets to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) , [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html) , [the Copy operation in Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops) , or [the import jobs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job) . In this case, Amazon S3 makes a call to KMS every time a copy request is made for a KMS-encrypted object.

`--request-payer` (string)

Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for corresponding charges to copy the object. For information about downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported for directory buckets.

Possible values:

- `requester`

`--tagging` (string)

The tag-set for the object. The tag-set must be encoded as URL Query parameters. (For example, âKey1=Value1â)

### Note

This functionality is not supported for directory buckets.

`--object-lock-mode` (string)

The Object Lock mode that you want to apply to this object.

### Note

This functionality is not supported for directory buckets.

Possible values:

- `GOVERNANCE`
- `COMPLIANCE`

`--object-lock-retain-until-date` (timestamp)

The date and time when you want this objectâs Object Lock to expire. Must be formatted as a timestamp parameter.

### Note

This functionality is not supported for directory buckets.

`--object-lock-legal-hold-status` (string)

Specifies whether a legal hold will be applied to this object. For more information about S3 Object Lock, see [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported for directory buckets.

Possible values:

- `ON`
- `OFF`

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

**Example 1: Upload an object to Amazon S3**

The following `put-object` command example uploads an object to Amazon S3.

```
aws s3api put-object \
    --bucket amzn-s3-demo-bucket \
    --key my-dir/MySampleImage.png \
    --body MySampleImage.png
```

For more information about uploading objects, see [`Uploading Objects < http://docs.aws.amazon.com/AmazonS3/latest/dev/UploadingObjects.html>`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html#id11) in the *Amazon S3 Developer Guide*.

**Example 2: Upload a video file to Amazon S3**

The following `put-object` command example uploads a video file.

```
aws s3api put-object \
    --bucket amzn-s3-demo-bucket \
    --key my-dir/big-video-file.mp4 \
    --body /media/videos/f-sharp-3-data-services.mp4
```

For more information about uploading objects, see [`Uploading Objects < http://docs.aws.amazon.com/AmazonS3/latest/dev/UploadingObjects.html>`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html#id11) in the *Amazon S3 Developer Guide*.

## Output

Expiration -> (string)

If the expiration is configured for the object (see [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html) ) in the *Amazon S3 User Guide* , the response includes this header. It includes the `expiry-date` and `rule-id` key-value pairs that provide information about object expiration. The value of the `rule-id` is URL-encoded.

### Note

Object expiration information is not returned in directory buckets and this header returns the value â`NotImplemented` â in all responses for directory buckets.

ETag -> (string)

Entity tag for the uploaded object.

**General purpose buckets** - To ensure that data is not corrupted traversing the network, for objects where the ETag is the MD5 digest of the object, you can calculate the MD5 while putting an object to Amazon S3 and compare the returned ETag to the calculated MD5 value.

**Directory buckets** - The ETag for the object in a directory bucket isnât the MD5 digest of the object.

ChecksumCRC32 -> (string)

The Base64 encoded, 32-bit `CRC32 checksum` of the object. This checksum is only be present if the checksum was uploaded with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, itâs a calculation based on the checksum values of each individual part. For more information about how checksums are calculated with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide* .

ChecksumCRC32C -> (string)

The Base64 encoded, 32-bit `CRC32C` checksum of the object. This checksum is only present if the checksum was uploaded with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, itâs a calculation based on the checksum values of each individual part. For more information about how checksums are calculated with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide* .

ChecksumCRC64NVME -> (string)

The Base64 encoded, 64-bit `CRC64NVME` checksum of the object. This header is present if the object was uploaded with the `CRC64NVME` checksum algorithm, or if it was uploaded without a checksum (and Amazon S3 added the default checksum, `CRC64NVME` , to the uploaded object). For more information about how checksums are calculated with multipart uploads, see [Checking object integrity in the Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) .

ChecksumSHA1 -> (string)

The Base64 encoded, 160-bit `SHA1` digest of the object. This will only be present if the object was uploaded with the object. When you use the API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, itâs a calculation based on the checksum values of each individual part. For more information about how checksums are calculated with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide* .

ChecksumSHA256 -> (string)

The Base64 encoded, 256-bit `SHA256` digest of the object. This will only be present if the object was uploaded with the object. When you use an API operation on an object that was uploaded using multipart uploads, this value may not be a direct checksum value of the full object. Instead, itâs a calculation based on the checksum values of each individual part. For more information about how checksums are calculated with multipart uploads, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#large-object-checksums) in the *Amazon S3 User Guide* .

ChecksumType -> (string)

This header specifies the checksum type of the object, which determines how part-level checksums are combined to create an object-level checksum for multipart objects. For `PutObject` uploads, the checksum type is always `FULL_OBJECT` . You can use this header as a data integrity check to verify that the checksum type that is received is the same checksum that was specified. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ServerSideEncryption -> (string)

The server-side encryption algorithm used when you store this object in Amazon S3.

VersionId -> (string)

Version ID of the object.

If you enable versioning for a bucket, Amazon S3 automatically generates a unique version ID for the object being stored. Amazon S3 returns this ID in the response. When you enable versioning for a bucket, if Amazon S3 receives multiple write requests for the same object simultaneously, it stores all of the objects. For more information about versioning, see [Adding Objects to Versioning-Enabled Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/AddingObjectstoVersioningEnabledBuckets.html) in the *Amazon S3 User Guide* . For information about returning the versioning state of a bucket, see [GetBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html) .

### Note

This functionality is not supported for directory buckets.

SSECustomerAlgorithm -> (string)

If server-side encryption with a customer-provided encryption key was requested, the response will include this header to confirm the encryption algorithm thatâs used.

### Note

This functionality is not supported for directory buckets.

SSECustomerKeyMD5 -> (string)

If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide the round-trip message integrity verification of the customer-provided encryption key.

### Note

This functionality is not supported for directory buckets.

SSEKMSKeyId -> (string)

If present, indicates the ID of the KMS key that was used for object encryption.

SSEKMSEncryptionContext -> (string)

If present, indicates the Amazon Web Services KMS Encryption Context to use for object encryption. The value of this header is a Base64 encoded string of a UTF-8 encoded JSON, which contains the encryption context as key-value pairs. This value is stored as object metadata and automatically gets passed on to Amazon Web Services KMS for future `GetObject` operations on this object.

BucketKeyEnabled -> (boolean)

Indicates whether the uploaded object uses an S3 Bucket Key for server-side encryption with Key Management Service (KMS) keys (SSE-KMS).

Size -> (long)

The size of the object in bytes. This value is only be present if you append to an object.

### Note

This functionality is only supported for objects in the Amazon S3 Express One Zone storage class in directory buckets.

RequestCharged -> (string)

If present, indicates that the requester was successfully charged for the request.

### Note

This functionality is not supported for directory buckets.