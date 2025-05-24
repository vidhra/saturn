# copy-objectÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html#cli-aws-s3api) ]

# copy-object

## Description

Creates a copy of an object that is already stored in Amazon S3.

### Note

You can store individual objects of up to 5 TB in Amazon S3. You create a copy of your object up to 5 GB in size in a single atomic action using this API. However, to copy an object greater than 5 GB, you must use the multipart upload Upload Part - Copy (UploadPartCopy) API. For more information, see [Copy Object Using the REST Multipart Upload API](https://docs.aws.amazon.com/AmazonS3/latest/dev/CopyingObjctsUsingRESTMPUapi.html) .

You can copy individual objects between general purpose buckets, between directory buckets, and between general purpose buckets and directory buckets.

### Note

- Amazon S3 supports copy operations using Multi-Region Access Points only as a destination when using the Multi-Region Access Point ARN.
- **Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html#id1)[https://](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html)*amzn-s3-demo-bucket* .s3express-*zone-id* .*region-code* .amazonaws.com/*key-name* `` . Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the *Amazon S3 User Guide* . For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the *Amazon S3 User Guide* .
- VPC endpoints donât support cross-Region requests (including copies). If youâre using VPC endpoints, your source and destination buckets should be in the same Amazon Web Services Region as your VPC endpoint.

Both the Region that you want to copy the object from and the Region that you want to copy the object to must be enabled for your account. For more information about how to enable a Region for your account, see [Enable or disable a Region for standalone accounts](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#manage-acct-regions-enable-standalone) in the *Amazon Web Services Account Management Guide* .

### Warning

Amazon S3 transfer acceleration does not support cross-Region copies. If you request a cross-Region copy using a transfer acceleration endpoint, you get a `400 Bad Request` error. For more information, see [Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html) .

Authentication and authorization

All `CopyObject` requests must be authenticated and signed by using IAM credentials (access key ID and secret access key for the IAM identities). All headers with the `x-amz-` prefix, including `x-amz-copy-source` , must be signed. For more information, see [REST Authentication](https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html) .

**Directory buckets** - You must use the IAM credentials to authenticate and authorize your access to the `CopyObject` API operation, instead of using the temporary security credentials through the `CreateSession` API operation.

Amazon Web Services CLI or SDKs handles authentication and authorization on your behalf.

Permissions

You must have *read* access to the source object and *write* access to the destination bucket.

- **General purpose bucket permissions** - You must have permissions in an IAM policy based on the source and destination bucket types in a `CopyObject` operation.
- If the source object is in a general purpose bucket, you must have ** `s3:GetObject` ** permission to read the source object that is being copied.
- If the destination bucket is a general purpose bucket, you must have ** `s3:PutObject` ** permission to write the object copy to the destination bucket.
- **Directory bucket permissions** - You must have permissions in a bucket policy or an IAM identity-based policy based on the source and destination bucket types in a `CopyObject` operation.
- If the source object that you want to copy is in a directory bucket, you must have the ** `s3express:CreateSession` ** permission in the `Action` element of a policy to read the object. By default, the session is in the `ReadWrite` mode. If you want to restrict the access, you can explicitly set the `s3express:SessionMode` condition key to `ReadOnly` on the copy source bucket.
- If the copy destination is a directory bucket, you must have the ** `s3express:CreateSession` ** permission in the `Action` element of a policy to write the object to the destination. The `s3express:SessionMode` condition key canât be set to `ReadOnly` on the copy destination bucket.

If the object is encrypted with SSE-KMS, you must also have the `kms:GenerateDataKey` and `kms:Decrypt` permissions in IAM identity-based policies and KMS key policies for the KMS key.

For example policies, see [Example bucket policies for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam-example-bucket-policies.html) and [Amazon Web Services Identity and Access Management (IAM) identity-based policies for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam-identity-policies.html) in the *Amazon S3 User Guide* .

Response and special errors

When the request is an HTTP 1.1 request, the response is chunk encoded. When the request is not an HTTP 1.1 request, the response would not contain the `Content-Length` . You always need to read the entire response body to check if the copy succeeds.

- If the copy is successful, you receive a response with information about the copied object.
- A copy request might return an error when Amazon S3 receives the copy request or while Amazon S3 is copying the files. A `200 OK` response can contain either a success or an error.

- If the error occurs before the copy action starts, you receive a standard Amazon S3 error.
- If the error occurs during the copy operation, the error response is embedded in the `200 OK` response. For example, in a cross-region copy, you may encounter throttling and receive a `200 OK` response. For more information, see [Resolve the Error 200 response when copying objects to Amazon S3](https://repost.aws/knowledge-center/s3-resolve-200-internalerror) . The `200 OK` status code means the copy was accepted, but it doesnât mean the copy is complete. Another example is when you disconnect from Amazon S3 before the copy is complete, Amazon S3 might cancel the copy and you may receive a `200 OK` response. You must stay connected to Amazon S3 until the entire response is successfully received and processed. If you call this API operation directly, make sure to design your application to parse the content of the response and handle it appropriately. If you use Amazon Web Services SDKs, SDKs handle this condition. The SDKs detect the embedded error and apply error handling per your configuration settings (including automatically retrying the request as appropriate). If the condition persists, the SDKs throw an exception (or, for the SDKs that donât use exceptions, they return an error).

Charge

The copy request charge is based on the storage class and Region that you specify for the destination object. The request can also result in a data retrieval charge for the source if the source storage class bills for data retrieval. If the copy source is in a different region, the data transfer is billed to the copy source account. For pricing information, see [Amazon S3 pricing](http://aws.amazon.com/s3/pricing/) .

HTTP Host header syntax

- **Directory buckets** - The HTTP Host header syntax is `` *Bucket-name* .s3express-*zone-id* .*region-code* .amazonaws.com`` .
- **Amazon S3 on Outposts** - When you use this action with S3 on Outposts through the REST API, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form `` *AccessPointName* -*AccountId* .*outpostID* .s3-outposts.*Region* .amazonaws.com`` . The hostname isnât required when you use the Amazon Web Services CLI or SDKs.

The following operations are related to `CopyObject` :

- [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CopyObject)

## Synopsis

```
copy-object
[--acl <value>]
--bucket <value>
[--cache-control <value>]
[--checksum-algorithm <value>]
[--content-disposition <value>]
[--content-encoding <value>]
[--content-language <value>]
[--content-type <value>]
--copy-source <value>
[--copy-source-if-match <value>]
[--copy-source-if-modified-since <value>]
[--copy-source-if-none-match <value>]
[--copy-source-if-unmodified-since <value>]
[--expires <value>]
[--grant-full-control <value>]
[--grant-read <value>]
[--grant-read-acp <value>]
[--grant-write-acp <value>]
--key <value>
[--metadata <value>]
[--metadata-directive <value>]
[--tagging-directive <value>]
[--server-side-encryption <value>]
[--storage-class <value>]
[--website-redirect-location <value>]
[--sse-customer-algorithm <value>]
[--sse-customer-key <value>]
[--sse-customer-key-md5 <value>]
[--ssekms-key-id <value>]
[--ssekms-encryption-context <value>]
[--bucket-key-enabled | --no-bucket-key-enabled]
[--copy-source-sse-customer-algorithm <value>]
[--copy-source-sse-customer-key <value>]
[--copy-source-sse-customer-key-md5 <value>]
[--request-payer <value>]
[--tagging <value>]
[--object-lock-mode <value>]
[--object-lock-retain-until-date <value>]
[--object-lock-legal-hold-status <value>]
[--expected-bucket-owner <value>]
[--expected-source-bucket-owner <value>]
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

The canned access control list (ACL) to apply to the object.

When you copy an object, the ACL metadata is not preserved and is set to `private` by default. Only the owner has full access control. To override the default ACL setting, specify a new ACL when you generate a copy request. For more information, see [Using ACLs](https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html) .

If the destination bucket that youâre copying objects to uses the bucket owner enforced setting for S3 Object Ownership, ACLs are disabled and no longer affect permissions. Buckets that use this setting only accept `PUT` requests that donât specify an ACL or `PUT` requests that specify bucket owner full control ACLs, such as the `bucket-owner-full-control` canned ACL or an equivalent form of this ACL expressed in the XML format. For more information, see [Controlling ownership of objects and disabling ACLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon S3 User Guide* .

### Note

- If your destination bucket uses the bucket owner enforced setting for Object Ownership, all objects written to the bucket by any account will be owned by the bucket owner.
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

`--bucket` (string)

The name of the destination bucket.

**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `` *Bucket-name* .s3express-*zone-id* .*region-code* .amazonaws.com`` . Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `` *bucket-base-name* â*zone-id* âx-s3`` (for example, `` *amzn-s3-demo-bucket* â*usw2-az1* âx-s3`` ). For information about bucket naming restrictions, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide* .

### Note

Copying objects across different Amazon Web Services Regions isnât supported when the source or destination bucket is in Amazon Web Services Local Zones. The source and destination buckets must have the same parent Amazon Web Services Region. Otherwise, you get an HTTP `400 Bad Request` error with the error code `InvalidRequest` .

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName* -*AccountId* .s3-accesspoint.*Region* .amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide* .

### Note

Object Lambda access points are not supported by directory buckets.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must use the Outpost bucket access point ARN or the access point alias for the destination bucket. You can only copy objects within the same Outpost bucket. Itâs not supported to copy objects across different Amazon Web Services Outposts, between buckets on the same Outposts, or between Outposts buckets and any other bucket types. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *S3 on Outposts guide* . When you use this action with S3 on Outposts through the REST API, you must direct requests to the S3 on Outposts hostname, in the format `` *AccessPointName* -*AccountId* .*outpostID* .s3-outposts.*Region* .amazonaws.com`` . The hostname isnât required when you use the Amazon Web Services CLI or SDKs.

`--cache-control` (string)

Specifies the caching behavior along the request/reply chain.

`--checksum-algorithm` (string)

Indicates the algorithm that you want Amazon S3 to use to create the checksum for the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

When you copy an object, if the source object has a checksum, that checksum value will be copied to the new object by default. If the `CopyObject` request does not include this `x-amz-checksum-algorithm` header, the checksum algorithm will be copied from the source object to the destination object (if itâs present on the source object). You can optionally specify a different checksum algorithm to use with the `x-amz-checksum-algorithm` header. Unrecognized or unsupported values will respond with the HTTP status code `400 Bad Request` .

### Note

For directory buckets, when you use Amazon Web Services SDKs, `CRC32` is the default checksum algorithm thatâs used for performance.

Possible values:

- `CRC32`
- `CRC32C`
- `SHA1`
- `SHA256`
- `CRC64NVME`

`--content-disposition` (string)

Specifies presentational information for the object. Indicates whether an object should be displayed in a web browser or downloaded as a file. It allows specifying the desired filename for the downloaded file.

`--content-encoding` (string)

Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

### Note

For directory buckets, only the `aws-chunked` value is supported in this header field.

`--content-language` (string)

The language the content is in.

`--content-type` (string)

A standard MIME type that describes the format of the object data.

`--copy-source` (string)

Specifies the source object for the copy operation. The source object can be up to 5 GB. If the source object is an object that was uploaded by using a multipart upload, the object copy will be a single part object after the source object is copied to the destination bucket.

You specify the value of the copy source in one of two formats, depending on whether you want to access the source object through an [access point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html) :

- For objects not accessed through an access point, specify the name of the source bucket and the key of the source object, separated by a slash (/). For example, to copy the object `reports/january.pdf` from the general purpose bucket `awsexamplebucket` , use `awsexamplebucket/reports/january.pdf` . The value must be URL-encoded. To copy the object `reports/january.pdf` from the directory bucket `awsexamplebucket--use1-az5--x-s3` , use `awsexamplebucket--use1-az5--x-s3/reports/january.pdf` . The value must be URL-encoded.
- For objects accessed through access points, specify the Amazon Resource Name (ARN) of the object as accessed through the access point, in the format `arn:aws:s3:<Region>:<account-id>:accesspoint/<access-point-name>/object/<key>` . For example, to copy the object `reports/january.pdf` through access point `my-access-point` owned by account `123456789012` in Region `us-west-2` , use the URL encoding of `arn:aws:s3:us-west-2:123456789012:accesspoint/my-access-point/object/reports/january.pdf` . The value must be URL encoded.

### Note

- Amazon S3 supports copy operations using Access points only when the source and destination buckets are in the same Amazon Web Services Region.
- Access points are not supported by directory buckets.

Alternatively, for objects accessed through Amazon S3 on Outposts, specify the ARN of the object as accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/object/<key>` . For example, to copy the object `reports/january.pdf` through outpost `my-outpost` owned by account `123456789012` in Region `us-west-2` , use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/object/reports/january.pdf` . The value must be URL-encoded.

If your source bucket versioning is enabled, the `x-amz-copy-source` header by default identifies the current version of an object to copy. If the current version is a delete marker, Amazon S3 behaves as if the object was deleted. To copy a different version, use the `versionId` query parameter. Specifically, append `?versionId=<version-id>` to the value (for example, `awsexamplebucket/reports/january.pdf?versionId=QUpfdndhfd8438MNFDN93jdnJFkdmqnh893` ). If you donât specify a version ID, Amazon S3 copies the latest version of the source object.

If you enable versioning on the destination bucket, Amazon S3 generates a unique version ID for the copied object. This version ID is different from the version ID of the source object. Amazon S3 returns the version ID of the copied object in the `x-amz-version-id` response header in the response.

If you do not enable versioning or suspend it on the destination bucket, the version ID that Amazon S3 generates in the `x-amz-version-id` response header is always null.

### Note

**Directory buckets** - S3 Versioning isnât enabled and supported for directory buckets.

`--copy-source-if-match` (string)

Copies the object if its entity tag (ETag) matches the specified tag.

If both the `x-amz-copy-source-if-match` and `x-amz-copy-source-if-unmodified-since` headers are present in the request and evaluate as follows, Amazon S3 returns `200 OK` and copies the data:

- `x-amz-copy-source-if-match` condition evaluates to true
- `x-amz-copy-source-if-unmodified-since` condition evaluates to false

`--copy-source-if-modified-since` (timestamp)

Copies the object if it has been modified since the specified time.

If both the `x-amz-copy-source-if-none-match` and `x-amz-copy-source-if-modified-since` headers are present in the request and evaluate as follows, Amazon S3 returns the `412 Precondition Failed` response code:

- `x-amz-copy-source-if-none-match` condition evaluates to false
- `x-amz-copy-source-if-modified-since` condition evaluates to true

`--copy-source-if-none-match` (string)

Copies the object if its entity tag (ETag) is different than the specified ETag.

If both the `x-amz-copy-source-if-none-match` and `x-amz-copy-source-if-modified-since` headers are present in the request and evaluate as follows, Amazon S3 returns the `412 Precondition Failed` response code:

- `x-amz-copy-source-if-none-match` condition evaluates to false
- `x-amz-copy-source-if-modified-since` condition evaluates to true

`--copy-source-if-unmodified-since` (timestamp)

Copies the object if it hasnât been modified since the specified time.

If both the `x-amz-copy-source-if-match` and `x-amz-copy-source-if-unmodified-since` headers are present in the request and evaluate as follows, Amazon S3 returns `200 OK` and copies the data:

- `x-amz-copy-source-if-match` condition evaluates to true
- `x-amz-copy-source-if-unmodified-since` condition evaluates to false

`--expires` (timestamp)

The date and time at which the object is no longer cacheable.

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

The key of the destination object.

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

`--metadata-directive` (string)

Specifies whether the metadata is copied from the source object or replaced with metadata thatâs provided in the request. When copying an object, you can preserve all metadata (the default) or specify new metadata. If this header isnât specified, `COPY` is the default behavior.

**General purpose bucket** - For general purpose buckets, when you grant permissions, you can use the `s3:x-amz-metadata-directive` condition key to enforce certain metadata behavior when objects are uploaded. For more information, see [Amazon S3 condition key examples](https://docs.aws.amazon.com/AmazonS3/latest/dev/amazon-s3-policy-keys.html) in the *Amazon S3 User Guide* .

### Note

`x-amz-website-redirect-location` is unique to each object and is not copied when using the `x-amz-metadata-directive` header. To copy the value, you must specify `x-amz-website-redirect-location` in the request header.

Possible values:

- `COPY`
- `REPLACE`

`--tagging-directive` (string)

Specifies whether the object tag-set is copied from the source object or replaced with the tag-set thatâs provided in the request.

The default value is `COPY` .

### Note

**Directory buckets** - For directory buckets in a `CopyObject` operation, only the empty tag-set is supported. Any requests that attempt to write non-empty tags into directory buckets will receive a `501 Not Implemented` status code. When the destination bucket is a directory bucket, you will receive a `501 Not Implemented` response in any of the following situations:

- When you attempt to `COPY` the tag-set from an S3 source object that has non-empty tags.
- When you attempt to `REPLACE` the tag-set of a source object and set a non-empty value to `x-amz-tagging` .
- When you donât set the `x-amz-tagging-directive` header and the source object has non-empty tags. This is because the default value of `x-amz-tagging-directive` is `COPY` .

Because only the empty tag-set is supported for directory buckets in a `CopyObject` operation, the following situations are allowed:

- When you attempt to `COPY` the tag-set from a directory bucket source object that has no tags to a general purpose bucket. It copies an empty tag-set to the destination object.
- When you attempt to `REPLACE` the tag-set of a directory bucket source object and set the `x-amz-tagging` value of the directory bucket destination object to empty.
- When you attempt to `REPLACE` the tag-set of a general purpose bucket source object that has non-empty tags and set the `x-amz-tagging` value of the directory bucket destination object to empty.
- When you attempt to `REPLACE` the tag-set of a directory bucket source object and donât set the `x-amz-tagging` value of the directory bucket destination object. This is because the default value of `x-amz-tagging` is the empty value.

Possible values:

- `COPY`
- `REPLACE`

`--server-side-encryption` (string)

The server-side encryption algorithm used when storing this object in Amazon S3. Unrecognized or unsupported values wonât write a destination object and will receive a `400 Bad Request` response.

Amazon S3 automatically encrypts all new objects that are copied to an S3 bucket. When copying an object, if you donât specify encryption information in your copy request, the encryption setting of the target object is set to the default encryption configuration of the destination bucket. By default, all buckets have a base level of encryption configuration that uses server-side encryption with Amazon S3 managed keys (SSE-S3). If the destination bucket has a different default encryption configuration, Amazon S3 uses the corresponding encryption key to encrypt the target object copy.

With server-side encryption, Amazon S3 encrypts your data as it writes your data to disks in its data centers and decrypts the data when you access it. For more information about server-side encryption, see [Using Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html) in the *Amazon S3 User Guide* .

**General purpose buckets**

- For general purpose buckets, there are the following supported options for server-side encryption: server-side encryption with Key Management Service (KMS) keys (SSE-KMS), dual-layer server-side encryption with Amazon Web Services KMS keys (DSSE-KMS), and server-side encryption with customer-provided encryption keys (SSE-C). Amazon S3 uses the corresponding KMS key, or a customer-provided key to encrypt the target object copy.
- When you perform a `CopyObject` operation, if you want to use a different type of encryption setting for the target object, you can specify appropriate encryption-related headers to encrypt the target object with an Amazon S3 managed key, a KMS key, or a customer-provided key. If the encryption setting in your request is different from the default encryption configuration of the destination bucket, the encryption setting in your request takes precedence.

**Directory buckets**

- For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (`AES256` ) and server-side encryption with KMS keys (SSE-KMS) (`aws:kms` ). We recommend that the bucketâs default encryption uses the desired encryption configuration and you donât override the bucket default encryption in your `CreateSession` requests or `PUT` object requests. Then, new objects are automatically encrypted with the desired encryption settings. For more information, see [Protecting data with server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-serv-side-encryption.html) in the *Amazon S3 User Guide* . For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with KMS for new object uploads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-specifying-kms-encryption.html) .
- To encrypt new object copies to a directory bucket with SSE-KMS, we recommend you specify SSE-KMS as the directory bucketâs default encryption configuration with a KMS key (specifically, a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) ). The [Amazon Web Services managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) (`aws/s3` ) isnât supported. Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) per directory bucket for the lifetime of the bucket. After you specify a customer managed key for SSE-KMS, you canât override the customer managed key for the bucketâs SSE-KMS configuration. Then, when you perform a `CopyObject` operation and want to specify server-side encryption settings for new object copies with SSE-KMS in the encryption-related request headers, you must ensure the encryption key is the same customer managed key that you specified for the directory bucketâs default encryption configuration.

Possible values:

- `AES256`
- `aws:kms`
- `aws:kms:dsse`

`--storage-class` (string)

If the `x-amz-storage-class` header is not used, the copied object will be stored in the `STANDARD` Storage Class by default. The `STANDARD` storage class provides high durability and high availability. Depending on performance needs, you can specify a different Storage Class.

### Note

- **Directory buckets** - Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones. Unsupported storage class values wonât write a destination object and will respond with the HTTP status code `400 Bad Request` .
- **Amazon S3 on Outposts** - S3 on Outposts only uses the `OUTPOSTS` Storage Class.

You can use the `CopyObject` action to change the storage class of an object that is already stored in Amazon S3 by using the `x-amz-storage-class` header. For more information, see [Storage Classes](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html) in the *Amazon S3 User Guide* .

Before using an object as a source object for the copy operation, you must restore a copy of it if it meets any of the following conditions:

- The storage class of the source object is `GLACIER` or `DEEP_ARCHIVE` .
- The storage class of the source object is `INTELLIGENT_TIERING` and itâs [S3 Intelligent-Tiering access tier](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html#intel-tiering-tier-definition) is `Archive Access` or `Deep Archive Access` .

For more information, see [RestoreObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html) and [Copying Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/CopyingObjectsExamples.html) in the *Amazon S3 User Guide* .

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

If the destination bucket is configured as a website, redirects requests for this object copy to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata. This value is unique to each object and is not copied when using the `x-amz-metadata-directive` header. Instead, you may opt to provide this header in combination with the `x-amz-metadata-directive` header.

### Note

This functionality is not supported for directory buckets.

`--sse-customer-algorithm` (string)

Specifies the algorithm to use when encrypting the object (for example, `AES256` ).

When you perform a `CopyObject` operation, if you want to use a different type of encryption setting for the target object, you can specify appropriate encryption-related headers to encrypt the target object with an Amazon S3 managed key, a KMS key, or a customer-provided key. If the encryption setting in your request is different from the default encryption configuration of the destination bucket, the encryption setting in your request takes precedence.

### Note

This functionality is not supported when the destination bucket is a directory bucket.

`--sse-customer-key` (string)

Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded. Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the `x-amz-server-side-encryption-customer-algorithm` header.

### Note

This functionality is not supported when the destination bucket is a directory bucket.

`--sse-customer-key-md5` (string)

Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.

### Note

This functionality is not supported when the destination bucket is a directory bucket.

`--ssekms-key-id` (string)

Specifies the KMS key ID (Key ID, Key ARN, or Key Alias) to use for object encryption. All GET and PUT requests for an object protected by KMS will fail if theyâre not made via SSL or using SigV4. For information about configuring any of the officially supported Amazon Web Services SDKs and Amazon Web Services CLI, see [Specifying the Signature Version in Request Authentication](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version) in the *Amazon S3 User Guide* .

**Directory buckets** - To encrypt data using SSE-KMS, itâs recommended to specify the `x-amz-server-side-encryption` header to `aws:kms` . Then, the `x-amz-server-side-encryption-aws-kms-key-id` header implicitly uses the bucketâs default KMS customer managed key ID. If you want to explicitly set the `x-amz-server-side-encryption-aws-kms-key-id` header, it must match the bucketâs default customer managed key (using key ID or ARN, not alias). Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) per directory bucketâs lifetime. The [Amazon Web Services managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) (`aws/s3` ) isnât supported. Incorrect key specification results in an HTTP `400 Bad Request` error.

`--ssekms-encryption-context` (string)

Specifies the Amazon Web Services KMS Encryption Context as an additional encryption context to use for the destination object encryption. The value of this header is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.

**General purpose buckets** - This value must be explicitly added to specify encryption context for `CopyObject` requests if you want an additional encryption context for your destination object. The additional encryption context of the source object wonât be copied to the destination object. For more information, see [Encryption context](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html#encryption-context) in the *Amazon S3 User Guide* .

**Directory buckets** - You can optionally provide an explicit encryption context value. The value must match the default encryption context - the bucket Amazon Resource Name (ARN). An additional encryption context value is not supported.

`--bucket-key-enabled` | `--no-bucket-key-enabled` (boolean)

Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with server-side encryption using Key Management Service (KMS) keys (SSE-KMS). If a target object uses SSE-KMS, you can enable an S3 Bucket Key for the object.

Setting this header to `true` causes Amazon S3 to use an S3 Bucket Key for object encryption with SSE-KMS. Specifying this header with a COPY action doesnât affect bucket-level settings for S3 Bucket Key.

For more information, see [Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html) in the *Amazon S3 User Guide* .

### Note

**Directory buckets** - S3 Bucket Keys arenât supported, when you copy SSE-KMS encrypted objects from general purpose buckets to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) . In this case, Amazon S3 makes a call to KMS every time a copy request is made for a KMS-encrypted object.

`--copy-source-sse-customer-algorithm` (string)

Specifies the algorithm to use when decrypting the source object (for example, `AES256` ).

If the source object for the copy is stored in Amazon S3 using SSE-C, you must provide the necessary encryption information in your request so that Amazon S3 can decrypt the object for copying.

### Note

This functionality is not supported when the source object is in a directory bucket.

`--copy-source-sse-customer-key` (string)

Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be the same one that was used when the source object was created.

If the source object for the copy is stored in Amazon S3 using SSE-C, you must provide the necessary encryption information in your request so that Amazon S3 can decrypt the object for copying.

### Note

This functionality is not supported when the source object is in a directory bucket.

`--copy-source-sse-customer-key-md5` (string)

Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.

If the source object for the copy is stored in Amazon S3 using SSE-C, you must provide the necessary encryption information in your request so that Amazon S3 can decrypt the object for copying.

### Note

This functionality is not supported when the source object is in a directory bucket.

`--request-payer` (string)

Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for corresponding charges to copy the object. For information about downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported for directory buckets.

Possible values:

- `requester`

`--tagging` (string)

The tag-set for the object copy in the destination bucket. This value must be used in conjunction with the `x-amz-tagging-directive` if you choose `REPLACE` for the `x-amz-tagging-directive` . If you choose `COPY` for the `x-amz-tagging-directive` , you donât need to set the `x-amz-tagging` header, because the tag-set will be copied from the source object directly. The tag-set must be encoded as URL Query parameters.

The default value is the empty value.

### Note

**Directory buckets** - For directory buckets in a `CopyObject` operation, only the empty tag-set is supported. Any requests that attempt to write non-empty tags into directory buckets will receive a `501 Not Implemented` status code. When the destination bucket is a directory bucket, you will receive a `501 Not Implemented` response in any of the following situations:

- When you attempt to `COPY` the tag-set from an S3 source object that has non-empty tags.
- When you attempt to `REPLACE` the tag-set of a source object and set a non-empty value to `x-amz-tagging` .
- When you donât set the `x-amz-tagging-directive` header and the source object has non-empty tags. This is because the default value of `x-amz-tagging-directive` is `COPY` .

Because only the empty tag-set is supported for directory buckets in a `CopyObject` operation, the following situations are allowed:

- When you attempt to `COPY` the tag-set from a directory bucket source object that has no tags to a general purpose bucket. It copies an empty tag-set to the destination object.
- When you attempt to `REPLACE` the tag-set of a directory bucket source object and set the `x-amz-tagging` value of the directory bucket destination object to empty.
- When you attempt to `REPLACE` the tag-set of a general purpose bucket source object that has non-empty tags and set the `x-amz-tagging` value of the directory bucket destination object to empty.
- When you attempt to `REPLACE` the tag-set of a directory bucket source object and donât set the `x-amz-tagging` value of the directory bucket destination object. This is because the default value of `x-amz-tagging` is the empty value.

`--object-lock-mode` (string)

The Object Lock mode that you want to apply to the object copy.

### Note

This functionality is not supported for directory buckets.

Possible values:

- `GOVERNANCE`
- `COMPLIANCE`

`--object-lock-retain-until-date` (timestamp)

The date and time when you want the Object Lock of the object copy to expire.

### Note

This functionality is not supported for directory buckets.

`--object-lock-legal-hold-status` (string)

Specifies whether you want to apply a legal hold to the object copy.

### Note

This functionality is not supported for directory buckets.

Possible values:

- `ON`
- `OFF`

`--expected-bucket-owner` (string)

The account ID of the expected destination bucket owner. If the account ID that you provide does not match the actual owner of the destination bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

`--expected-source-bucket-owner` (string)

The account ID of the expected source bucket owner. If the account ID that you provide does not match the actual owner of the source bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

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

The following command copies an object from `bucket-1` to `bucket-2`:

```
aws s3api copy-object --copy-source bucket-1/test.txt --key test.txt --bucket bucket-2
```

Output:

```
{
    "CopyObjectResult": {
        "LastModified": "2015-11-10T01:07:25.000Z",
        "ETag": "\"589c8b79c230a6ecd5a7e1d040a9a030\""
    },
    "VersionId": "YdnYvTCVDqRRFA.NFJjy36p0hxifMlkA"
}
```

## Output

CopyObjectResult -> (structure)

Container for all response elements.

ETag -> (string)

Returns the ETag of the new object. The ETag reflects only changes to the contents of an object, not its metadata.

LastModified -> (timestamp)

Creation date of the object.

ChecksumType -> (string)

The checksum type that is used to calculate the objectâs checksum value. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ChecksumCRC32 -> (string)

The Base64 encoded, 32-bit `CRC32` checksum of the object. This checksum is only present if the object was uploaded with the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ChecksumCRC32C -> (string)

The Base64 encoded, 32-bit `CRC32C` checksum of the object. This will only be present if the object was uploaded with the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ChecksumCRC64NVME -> (string)

The Base64 encoded, 64-bit `CRC64NVME` checksum of the object. This checksum is present if the object being copied was uploaded with the `CRC64NVME` checksum algorithm, or if the object was uploaded without a checksum (and Amazon S3 added the default checksum, `CRC64NVME` , to the uploaded object). For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ChecksumSHA1 -> (string)

The Base64 encoded, 160-bit `SHA1` digest of the object. This will only be present if the object was uploaded with the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ChecksumSHA256 -> (string)

The Base64 encoded, 256-bit `SHA256` digest of the object. This will only be present if the object was uploaded with the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

Expiration -> (string)

If the object expiration is configured, the response includes this header.

### Note

Object expiration information is not returned in directory buckets and this header returns the value â`NotImplemented` â in all responses for directory buckets.

CopySourceVersionId -> (string)

Version ID of the source object that was copied.

### Note

This functionality is not supported when the source object is in a directory bucket.

VersionId -> (string)

Version ID of the newly created copy.

### Note

This functionality is not supported for directory buckets.

ServerSideEncryption -> (string)

The server-side encryption algorithm used when you store this object in Amazon S3 (for example, `AES256` , `aws:kms` , `aws:kms:dsse` ).

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

If present, indicates the Amazon Web Services KMS Encryption Context to use for object encryption. The value of this header is a Base64 encoded UTF-8 string holding JSON with the encryption context key-value pairs.

BucketKeyEnabled -> (boolean)

Indicates whether the copied object uses an S3 Bucket Key for server-side encryption with Key Management Service (KMS) keys (SSE-KMS).

RequestCharged -> (string)

If present, indicates that the requester was successfully charged for the request.

### Note

This functionality is not supported for directory buckets.