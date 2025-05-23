# get-objectÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html#cli-aws-s3api) ]

# get-object

## Description

Retrieves an object from Amazon S3.

In the `GetObject` request, specify the full key name for the object.

**General purpose buckets** - Both the virtual-hosted-style requests and the path-style requests are supported. For a virtual hosted-style request example, if you have the object `photos/2006/February/sample.jpg` , specify the object key name as `/photos/2006/February/sample.jpg` . For a path-style request example, if you have the object `photos/2006/February/sample.jpg` in the bucket named `examplebucket` , specify the object key name as `/examplebucket/photos/2006/February/sample.jpg` . For more information about request types, see [HTTP Host Header Bucket Specification](https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html#VirtualHostingSpecifyBucket) in the *Amazon S3 User Guide* .

**Directory buckets** - Only virtual-hosted-style requests are supported. For a virtual hosted-style request example, if you have the object `photos/2006/February/sample.jpg` in the bucket named `amzn-s3-demo-bucket--usw2-az1--x-s3` , specify the object key name as `/photos/2006/February/sample.jpg` . Also, when you make requests to this API operation, your requests are sent to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html#id1)[https://](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html)*bucket-name* .s3express-*zone-id* .*region-code* .amazonaws.com/*key-name* `` . Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the *Amazon S3 User Guide* . For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the *Amazon S3 User Guide* .

Permissions

- **General purpose bucket permissions** - You must have the required permissions in a policy. To use `GetObject` , you must have the `READ` access to the object (or version). If you grant `READ` access to the anonymous user, the `GetObject` operation returns the object without using an authorization header. For more information, see [Specifying permissions in a policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html) in the *Amazon S3 User Guide* . If you include a `versionId` in your request header, you must have the `s3:GetObjectVersion` permission to access a specific version of an object. The `s3:GetObject` permission is not required in this scenario. If you request the current version of an object without a specific `versionId` in the request header, only the `s3:GetObject` permission is required. The `s3:GetObjectVersion` permission is not required in this scenario.  If the object that you request doesnât exist, the error that Amazon S3 returns depends on whether you also have the `s3:ListBucket` permission.

- If you have the `s3:ListBucket` permission on the bucket, Amazon S3 returns an HTTP status code `404 Not Found` error.
- If you donât have the `s3:ListBucket` permission, Amazon S3 returns an HTTP status code `403 Access Denied` error.
- **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the ` `CreateSession` [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession).html`__ API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use. Amazon Web Services CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see ` `CreateSession` [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession).html`__ . If the object is encrypted using SSE-KMS, you must also have the `kms:GenerateDataKey` and `kms:Decrypt` permissions in IAM identity-based policies and KMS key policies for the KMS key.

Storage classes

If the object you are retrieving is stored in the S3 Glacier Flexible Retrieval storage class, the S3 Glacier Deep Archive storage class, the S3 Intelligent-Tiering Archive Access tier, or the S3 Intelligent-Tiering Deep Archive Access tier, before you can retrieve the object you must first restore a copy using [RestoreObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html) . Otherwise, this operation returns an `InvalidObjectState` error. For information about restoring archived objects, see [Restoring Archived Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/restoring-objects.html) in the *Amazon S3 User Guide* .

**Directory buckets** - Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones. Unsupported storage class values wonât write a destination object and will respond with the HTTP status code `400 Bad Request` .

Encryption

Encryption request headers, like `x-amz-server-side-encryption` , should not be sent for the `GetObject` requests, if your object uses server-side encryption with Amazon S3 managed encryption keys (SSE-S3), server-side encryption with Key Management Service (KMS) keys (SSE-KMS), or dual-layer server-side encryption with Amazon Web Services KMS keys (DSSE-KMS). If you include the header in your `GetObject` requests for the object that uses these types of keys, youâll get an HTTP `400 Bad Request` error.

**Directory buckets** - For directory buckets, there are only two supported options for server-side encryption: SSE-S3 and SSE-KMS. SSE-C isnât supported. For more information, see [Protecting data with server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-serv-side-encryption.html) in the *Amazon S3 User Guide* .

Overriding response header values through the request

There are times when you want to override certain response header values of a `GetObject` response. For example, you might override the `Content-Disposition` response header value through your `GetObject` request.

You can override values for a set of response headers. These modified response header values are included only in a successful response, that is, when the HTTP status code `200 OK` is returned. The headers you can override using the following query parameters in the request are a subset of the headers that Amazon S3 accepts when you create an object.

The response headers that you can override for the `GetObject` response are `Cache-Control` , `Content-Disposition` , `Content-Encoding` , `Content-Language` , `Content-Type` , and `Expires` .

To override values for a set of response headers in the `GetObject` response, you can use the following query parameters in the request.

- `response-cache-control`
- `response-content-disposition`
- `response-content-encoding`
- `response-content-language`
- `response-content-type`
- `response-expires`

### Note

When you use these parameters, you must sign the request by using either an Authorization header or a presigned URL. These parameters cannot be used with an unsigned (anonymous) request.

HTTP Host header syntax

**Directory buckets** - The HTTP Host header syntax is `` *Bucket-name* .s3express-*zone-id* .*region-code* .amazonaws.com`` .

The following operations are related to `GetObject` :

- [ListBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html)
- [GetObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObject)

## Synopsis

```
get-object
--bucket <value>
[--if-match <value>]
[--if-modified-since <value>]
[--if-none-match <value>]
[--if-unmodified-since <value>]
--key <value>
[--range <value>]
[--response-cache-control <value>]
[--response-content-disposition <value>]
[--response-content-encoding <value>]
[--response-content-language <value>]
[--response-content-type <value>]
[--response-expires <value>]
[--version-id <value>]
[--sse-customer-algorithm <value>]
[--sse-customer-key <value>]
[--sse-customer-key-md5 <value>]
[--request-payer <value>]
[--part-number <value>]
[--expected-bucket-owner <value>]
[--checksum-mode <value>]
<outfile>
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

The bucket name containing the object.

**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `` *Bucket-name* .s3express-*zone-id* .*region-code* .amazonaws.com`` . Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `` *bucket-base-name* â*zone-id* âx-s3`` (for example, `` *amzn-s3-demo-bucket* â*usw2-az1* âx-s3`` ). For information about bucket naming restrictions, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide* .

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName* -*AccountId* .s3-accesspoint.*Region* .amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide* .

**Object Lambda access points** - When you use this action with an Object Lambda access point, you must direct requests to the Object Lambda access point hostname. The Object Lambda access point hostname takes the form *AccessPointName* -*AccountId* .s3-object-lambda.*Region* .amazonaws.com.

### Note

Object Lambda access points are not supported by directory buckets.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form `` *AccessPointName* -*AccountId* .*outpostID* .s3-outposts.*Region* .amazonaws.com`` . When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide* .

`--if-match` (string)

Return the object only if its entity tag (ETag) is the same as the one specified in this header; otherwise, return a `412 Precondition Failed` error.

If both of the `If-Match` and `If-Unmodified-Since` headers are present in the request as follows: `If-Match` condition evaluates to `true` , and; `If-Unmodified-Since` condition evaluates to `false` ; then, S3 returns `200 OK` and the data requested.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232) .

`--if-modified-since` (timestamp)

Return the object only if it has been modified since the specified time; otherwise, return a `304 Not Modified` error.

If both of the `If-None-Match` and `If-Modified-Since` headers are present in the request as follows:`If-None-Match` condition evaluates to `false` , and; `If-Modified-Since` condition evaluates to `true` ; then, S3 returns `304 Not Modified` status code.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232) .

`--if-none-match` (string)

Return the object only if its entity tag (ETag) is different from the one specified in this header; otherwise, return a `304 Not Modified` error.

If both of the `If-None-Match` and `If-Modified-Since` headers are present in the request as follows:`If-None-Match` condition evaluates to `false` , and; `If-Modified-Since` condition evaluates to `true` ; then, S3 returns `304 Not Modified` HTTP status code.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232) .

`--if-unmodified-since` (timestamp)

Return the object only if it has not been modified since the specified time; otherwise, return a `412 Precondition Failed` error.

If both of the `If-Match` and `If-Unmodified-Since` headers are present in the request as follows: `If-Match` condition evaluates to `true` , and; `If-Unmodified-Since` condition evaluates to `false` ; then, S3 returns `200 OK` and the data requested.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232) .

`--key` (string)

Key of the object to get.

`--range` (string)

Downloads the specified byte range of an object. For more information about the HTTP Range header, see [https://www.rfc-editor.org/rfc/rfc9110.html#name-range](https://www.rfc-editor.org/rfc/rfc9110.html#name-range) .

### Note

Amazon S3 doesnât support retrieving multiple ranges of data per `GET` request.

`--response-cache-control` (string)

Sets the `Cache-Control` header of the response.

`--response-content-disposition` (string)

Sets the `Content-Disposition` header of the response.

`--response-content-encoding` (string)

Sets the `Content-Encoding` header of the response.

`--response-content-language` (string)

Sets the `Content-Language` header of the response.

`--response-content-type` (string)

Sets the `Content-Type` header of the response.

`--response-expires` (timestamp)

Sets the `Expires` header of the response.

`--version-id` (string)

Version ID used to reference a specific version of the object.

By default, the `GetObject` operation returns the current version of an object. To return a different version, use the `versionId` subresource.

### Note

- If you include a `versionId` in your request header, you must have the `s3:GetObjectVersion` permission to access a specific version of an object. The `s3:GetObject` permission is not required in this scenario.
- If you request the current version of an object without a specific `versionId` in the request header, only the `s3:GetObject` permission is required. The `s3:GetObjectVersion` permission is not required in this scenario.
- **Directory buckets** - S3 Versioning isnât enabled and supported for directory buckets. For this API operation, only the `null` value of the version ID is supported by directory buckets. You can only specify `null` to the `versionId` query parameter in the request.

For more information about versioning, see [PutBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html) .

`--sse-customer-algorithm` (string)

Specifies the algorithm to use when decrypting the object (for example, `AES256` ).

If you encrypt an object by using server-side encryption with customer-provided encryption keys (SSE-C) when you store the object in Amazon S3, then when you GET the object, you must use the following headers:

- `x-amz-server-side-encryption-customer-algorithm`
- `x-amz-server-side-encryption-customer-key`
- `x-amz-server-side-encryption-customer-key-MD5`

For more information about SSE-C, see [Server-Side Encryption (Using Customer-Provided Encryption Keys)](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported for directory buckets.

`--sse-customer-key` (string)

Specifies the customer-provided encryption key that you originally provided for Amazon S3 to encrypt the data before storing it. This value is used to decrypt the object when recovering it and must match the one used when storing the data. The key must be appropriate for use with the algorithm specified in the `x-amz-server-side-encryption-customer-algorithm` header.

If you encrypt an object by using server-side encryption with customer-provided encryption keys (SSE-C) when you store the object in Amazon S3, then when you GET the object, you must use the following headers:

- `x-amz-server-side-encryption-customer-algorithm`
- `x-amz-server-side-encryption-customer-key`
- `x-amz-server-side-encryption-customer-key-MD5`

For more information about SSE-C, see [Server-Side Encryption (Using Customer-Provided Encryption Keys)](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported for directory buckets.

`--sse-customer-key-md5` (string)

Specifies the 128-bit MD5 digest of the customer-provided encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.

If you encrypt an object by using server-side encryption with customer-provided encryption keys (SSE-C) when you store the object in Amazon S3, then when you GET the object, you must use the following headers:

- `x-amz-server-side-encryption-customer-algorithm`
- `x-amz-server-side-encryption-customer-key`
- `x-amz-server-side-encryption-customer-key-MD5`

For more information about SSE-C, see [Server-Side Encryption (Using Customer-Provided Encryption Keys)](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported for directory buckets.

`--request-payer` (string)

Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for corresponding charges to copy the object. For information about downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported for directory buckets.

Possible values:

- `requester`

`--part-number` (integer)

Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a ârangedâ GET request for the part specified. Useful for downloading just a part of an object.

`--expected-bucket-owner` (string)

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

`--checksum-mode` (string)

To retrieve the checksum, this mode must be enabled.

Possible values:

- `ENABLED`

`outfile` (string)
Filename where the content will be saved

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

The following example uses the `get-object` command to download an object from Amazon S3:

```
aws s3api get-object --bucket text-content --key dir/my_images.tar.bz2 my_images.tar.bz2
```

Note that the outfile parameter is specified without an option name such as ââoutfileâ. The name of the output file must be the last parameter in the command.

The example below demonstrates the use of `--range` to download a specific byte range from an object. Note the byte ranges needs to be prefixed with âbytes=â:

```
aws s3api get-object --bucket text-content --key dir/my_data --range bytes=8888-9999 my_data_range
```

For more information about retrieving objects, see [Getting Objects](http://docs.aws.amazon.com/AmazonS3/latest/dev/GettingObjectsUsingAPIs.html) in the *Amazon S3 Developer Guide*.

## Output

Body -> (streaming blob)

Object data.

DeleteMarker -> (boolean)

Indicates whether the object retrieved was (true) or was not (false) a Delete Marker. If false, this response header does not appear in the response.

### Note

- If the current version of the object is a delete marker, Amazon S3 behaves as if the object was deleted and includes `x-amz-delete-marker: true` in the response.
- If the specified version in the request is a delete marker, the response returns a `405 Method Not Allowed` error and the `Last-Modified: timestamp` response header.

AcceptRanges -> (string)

Indicates that a range of bytes was specified in the request.

Expiration -> (string)

If the object expiration is configured (see ` `PutBucketLifecycleConfiguration` [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration).html`__ ), the response includes this header. It includes the `expiry-date` and `rule-id` key-value pairs providing object expiration information. The value of the `rule-id` is URL-encoded.

### Note

Object expiration information is not returned in directory buckets and this header returns the value â`NotImplemented` â in all responses for directory buckets.

Restore -> (string)

Provides information about object restoration action and expiration time of the restored object copy.

### Note

This functionality is not supported for directory buckets. Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.

LastModified -> (timestamp)

Date and time when the object was last modified.

**General purpose buckets** - When you specify a `versionId` of the object in your request, if the specified version in the request is a delete marker, the response returns a `405 Method Not Allowed` error and the `Last-Modified: timestamp` response header.

ContentLength -> (long)

Size of the body in bytes.

ETag -> (string)

An entity tag (ETag) is an opaque identifier assigned by a web server to a specific version of a resource found at a URL.

ChecksumCRC32 -> (string)

The Base64 encoded, 32-bit `CRC32` checksum of the object. This checksum is only present if the object was uploaded with the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ChecksumCRC32C -> (string)

The Base64 encoded, 32-bit `CRC32C` checksum of the object. This will only be present if the object was uploaded with the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ChecksumCRC64NVME -> (string)

The Base64 encoded, 64-bit `CRC64NVME` checksum of the object. For more information, see [Checking object integrity in the Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) .

ChecksumSHA1 -> (string)

The Base64 encoded, 160-bit `SHA1` digest of the object. This will only be present if the object was uploaded with the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ChecksumSHA256 -> (string)

The Base64 encoded, 256-bit `SHA256` digest of the object. This will only be present if the object was uploaded with the object. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

ChecksumType -> (string)

The checksum type, which determines how part-level checksums are combined to create an object-level checksum for multipart objects. You can use this header response to verify that the checksum type that is received is the same checksum type that was specified in the `CreateMultipartUpload` request. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

MissingMeta -> (integer)

This is set to the number of metadata entries not returned in the headers that are prefixed with `x-amz-meta-` . This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.

### Note

This functionality is not supported for directory buckets.

VersionId -> (string)

Version ID of the object.

### Note

This functionality is not supported for directory buckets.

CacheControl -> (string)

Specifies caching behavior along the request/reply chain.

ContentDisposition -> (string)

Specifies presentational information for the object.

ContentEncoding -> (string)

Indicates what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

ContentLanguage -> (string)

The language the content is in.

ContentRange -> (string)

The portion of the object returned in the response.

ContentType -> (string)

A standard MIME type describing the format of the object data.

Expires -> (timestamp)

The date and time at which the object is no longer cacheable.

### Note

This member has been deprecated. Please use ExpiresString instead.

ExpiresString -> (string)

The raw, unparsed value of the `Expires` field.

WebsiteRedirectLocation -> (string)

If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.

### Note

This functionality is not supported for directory buckets.

ServerSideEncryption -> (string)

The server-side encryption algorithm used when you store this object in Amazon S3.

Metadata -> (map)

A map of metadata to store with the object in S3.

key -> (string)

value -> (string)

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

BucketKeyEnabled -> (boolean)

Indicates whether the object uses an S3 Bucket Key for server-side encryption with Key Management Service (KMS) keys (SSE-KMS).

StorageClass -> (string)

Provides storage class information of the object. Amazon S3 returns this header for all objects except for S3 Standard storage class objects.

### Note

**Directory buckets** - Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.

RequestCharged -> (string)

If present, indicates that the requester was successfully charged for the request.

### Note

This functionality is not supported for directory buckets.

ReplicationStatus -> (string)

Amazon S3 can return this if your request involves a bucket that is either a source or destination in a replication rule.

### Note

This functionality is not supported for directory buckets.

PartsCount -> (integer)

The count of parts this object has. This value is only returned if you specify `partNumber` in your request and the object was uploaded as a multipart upload.

TagCount -> (integer)

The number of tags, if any, on the object, when you have the relevant permission to read object tags.

You can use [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html) to retrieve the tag set associated with an object.

### Note

This functionality is not supported for directory buckets.

ObjectLockMode -> (string)

The Object Lock mode thatâs currently in place for this object.

### Note

This functionality is not supported for directory buckets.

ObjectLockRetainUntilDate -> (timestamp)

The date and time when this objectâs Object Lock will expire.

### Note

This functionality is not supported for directory buckets.

ObjectLockLegalHoldStatus -> (string)

Indicates whether this object has an active legal hold. This field is only returned if you have permission to view an objectâs legal hold status.

### Note

This functionality is not supported for directory buckets.