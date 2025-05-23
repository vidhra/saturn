# write-get-object-responseÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/write-get-object-response.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/write-get-object-response.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html#cli-aws-s3api) ]

# write-get-object-response

## Description

### Note

This operation is not supported for directory buckets.

Passes transformed objects to a `GetObject` operation when using Object Lambda access points. For information about Object Lambda access points, see [Transforming objects with Object Lambda access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html) in the *Amazon S3 User Guide* .

This operation supports metadata that can be returned by [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) , in addition to `RequestRoute` , `RequestToken` , `StatusCode` , `ErrorCode` , and `ErrorMessage` . The `GetObject` response metadata is supported so that the `WriteGetObjectResponse` caller, typically an Lambda function, can provide the same metadata when it internally invokes `GetObject` . When `WriteGetObjectResponse` is called by a customer-owned Lambda function, the metadata returned to the end user `GetObject` call might differ from what Amazon S3 would normally return.

You can include any number of metadata headers. When including a metadata header, it should be prefaced with `x-amz-meta` . For example, `x-amz-meta-my-custom-header: MyCustomValue` . The primary use case for this is to forward `GetObject` metadata.

Amazon Web Services provides some prebuilt Lambda functions that you can use with S3 Object Lambda to detect and redact personally identifiable information (PII) and decompress S3 objects. These Lambda functions are available in the Amazon Web Services Serverless Application Repository, and can be selected through the Amazon Web Services Management Console when you create your Object Lambda access point.

Example 1: PII Access Control - This Lambda function uses Amazon Comprehend, a natural language processing (NLP) service using machine learning to find insights and relationships in text. It automatically detects personally identifiable information (PII) such as names, addresses, dates, credit card numbers, and social security numbers from documents in your Amazon S3 bucket.

Example 2: PII Redaction - This Lambda function uses Amazon Comprehend, a natural language processing (NLP) service using machine learning to find insights and relationships in text. It automatically redacts personally identifiable information (PII) such as names, addresses, dates, credit card numbers, and social security numbers from documents in your Amazon S3 bucket.

Example 3: Decompression - The Lambda function S3ObjectLambdaDecompression, is equipped to decompress objects stored in S3 in one of six compressed file formats including bzip2, gzip, snappy, zlib, zstandard and ZIP.

For information on how to view and use these functions, see [Using Amazon Web Services built Lambda functions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-examples.html) in the *Amazon S3 User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/WriteGetObjectResponse)

## Synopsis

```
write-get-object-response
--request-route <value>
--request-token <value>
[--body <value>]
[--status-code <value>]
[--error-code <value>]
[--error-message <value>]
[--accept-ranges <value>]
[--cache-control <value>]
[--content-disposition <value>]
[--content-encoding <value>]
[--content-language <value>]
[--content-length <value>]
[--content-range <value>]
[--content-type <value>]
[--checksum-crc32 <value>]
[--checksum-crc32-c <value>]
[--checksum-crc64-nvme <value>]
[--checksum-sha1 <value>]
[--checksum-sha256 <value>]
[--delete-marker | --no-delete-marker]
[--e-tag <value>]
[--expires <value>]
[--expiration <value>]
[--last-modified <value>]
[--missing-meta <value>]
[--metadata <value>]
[--object-lock-mode <value>]
[--object-lock-legal-hold-status <value>]
[--object-lock-retain-until-date <value>]
[--parts-count <value>]
[--replication-status <value>]
[--request-charged <value>]
[--restore <value>]
[--server-side-encryption <value>]
[--sse-customer-algorithm <value>]
[--ssekms-key-id <value>]
[--sse-customer-key-md5 <value>]
[--storage-class <value>]
[--tag-count <value>]
[--version-id <value>]
[--bucket-key-enabled | --no-bucket-key-enabled]
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

`--request-route` (string)

Route prefix to the HTTP URL generated.

`--request-token` (string)

A single use encrypted token that maps `WriteGetObjectResponse` to the end user `GetObject` request.

`--body` (streaming blob)

The object data.

### Note

This argument is of type: streaming blob. Its value must be the path to a file (e.g. `path/to/file`) and must **not** be prefixed with `file://` or `fileb://`

`--status-code` (integer)

The integer status code for an HTTP response of a corresponding `GetObject` request. The following is a list of status codes.

- `200 - OK`
- `206 - Partial Content`
- `304 - Not Modified`
- `400 - Bad Request`
- `401 - Unauthorized`
- `403 - Forbidden`
- `404 - Not Found`
- `405 - Method Not Allowed`
- `409 - Conflict`
- `411 - Length Required`
- `412 - Precondition Failed`
- `416 - Range Not Satisfiable`
- `500 - Internal Server Error`
- `503 - Service Unavailable`

`--error-code` (string)

A string that uniquely identifies an error condition. Returned in the <Code> tag of the error XML response for a corresponding `GetObject` call. Cannot be used with a successful `StatusCode` header or when the transformed object is provided in the body. All error codes from S3 are sentence-cased. The regular expression (regex) value is `"^[A-Z][a-zA-Z]+$"` .

`--error-message` (string)

Contains a generic description of the error condition. Returned in the <Message> tag of the error XML response for a corresponding `GetObject` call. Cannot be used with a successful `StatusCode` header or when the transformed object is provided in body.

`--accept-ranges` (string)

Indicates that a range of bytes was specified.

`--cache-control` (string)

Specifies caching behavior along the request/reply chain.

`--content-disposition` (string)

Specifies presentational information for the object.

`--content-encoding` (string)

Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

`--content-language` (string)

The language the content is in.

`--content-length` (long)

The size of the content body in bytes.

`--content-range` (string)

The portion of the object returned in the response.

`--content-type` (string)

A standard MIME type describing the format of the object data.

`--checksum-crc32` (string)

This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This specifies the Base64 encoded, 32-bit `CRC32` checksum of the object returned by the Object Lambda function. This may not match the checksum for the object stored in Amazon S3. Amazon S3 will perform validation of the checksum values only when the original `GetObject` request required checksum validation. For more information about checksums, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

Only one checksum header can be specified at a time. If you supply multiple checksum headers, this request will fail.

`--checksum-crc32-c` (string)

This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This specifies the Base64 encoded, 32-bit `CRC32C` checksum of the object returned by the Object Lambda function. This may not match the checksum for the object stored in Amazon S3. Amazon S3 will perform validation of the checksum values only when the original `GetObject` request required checksum validation. For more information about checksums, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

Only one checksum header can be specified at a time. If you supply multiple checksum headers, this request will fail.

`--checksum-crc64-nvme` (string)

This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This header specifies the Base64 encoded, 64-bit `CRC64NVME` checksum of the part. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

`--checksum-sha1` (string)

This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This specifies the Base64 encoded, 160-bit `SHA1` digest of the object returned by the Object Lambda function. This may not match the checksum for the object stored in Amazon S3. Amazon S3 will perform validation of the checksum values only when the original `GetObject` request required checksum validation. For more information about checksums, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

Only one checksum header can be specified at a time. If you supply multiple checksum headers, this request will fail.

`--checksum-sha256` (string)

This header can be used as a data integrity check to verify that the data received is the same data that was originally sent. This specifies the Base64 encoded, 256-bit `SHA256` digest of the object returned by the Object Lambda function. This may not match the checksum for the object stored in Amazon S3. Amazon S3 will perform validation of the checksum values only when the original `GetObject` request required checksum validation. For more information about checksums, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

Only one checksum header can be specified at a time. If you supply multiple checksum headers, this request will fail.

`--delete-marker` | `--no-delete-marker` (boolean)

Specifies whether an object stored in Amazon S3 is (`true` ) or is not (`false` ) a delete marker. To learn more about delete markers, see [Working with delete markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html) .

`--e-tag` (string)

An opaque identifier assigned by a web server to a specific version of a resource found at a URL.

`--expires` (timestamp)

The date and time at which the object is no longer cacheable.

`--expiration` (string)

If the object expiration is configured (see PUT Bucket lifecycle), the response includes this header. It includes the `expiry-date` and `rule-id` key-value pairs that provide the object expiration information. The value of the `rule-id` is URL-encoded.

`--last-modified` (timestamp)

The date and time that the object was last modified.

`--missing-meta` (integer)

Set to the number of metadata entries not returned in `x-amz-meta` headers. This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.

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

`--object-lock-mode` (string)

Indicates whether an object stored in Amazon S3 has Object Lock enabled. For more information about S3 Object Lock, see [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) .

Possible values:

- `GOVERNANCE`
- `COMPLIANCE`

`--object-lock-legal-hold-status` (string)

Indicates whether an object stored in Amazon S3 has an active legal hold.

Possible values:

- `ON`
- `OFF`

`--object-lock-retain-until-date` (timestamp)

The date and time when Object Lock is configured to expire.

`--parts-count` (integer)

The count of parts this object has.

`--replication-status` (string)

Indicates if request involves bucket that is either a source or destination in a Replication rule. For more information about S3 Replication, see [Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) .

Possible values:

- `COMPLETE`
- `PENDING`
- `FAILED`
- `REPLICA`
- `COMPLETED`

`--request-charged` (string)

If present, indicates that the requester was successfully charged for the request.

### Note

This functionality is not supported for directory buckets.

Possible values:

- `requester`

`--restore` (string)

Provides information about object restoration operation and expiration time of the restored object copy.

`--server-side-encryption` (string)

The server-side encryption algorithm used when storing requested object in Amazon S3 (for example, AES256, `aws:kms` ).

Possible values:

- `AES256`
- `aws:kms`
- `aws:kms:dsse`

`--sse-customer-algorithm` (string)

Encryption algorithm used if server-side encryption with a customer-provided encryption key was specified for object stored in Amazon S3.

`--ssekms-key-id` (string)

If present, specifies the ID (Key ID, Key ARN, or Key Alias) of the Amazon Web Services Key Management Service (Amazon Web Services KMS) symmetric encryption customer managed key that was used for stored in Amazon S3 object.

`--sse-customer-key-md5` (string)

128-bit MD5 digest of customer-provided encryption key used in Amazon S3 to encrypt data stored in S3. For more information, see [Protecting data using server-side encryption with customer-provided encryption keys (SSE-C)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html) .

`--storage-class` (string)

Provides storage class information of the object. Amazon S3 returns this header for all objects except for S3 Standard storage class objects.

For more information, see [Storage Classes](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html) .

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

`--tag-count` (integer)

The number of tags, if any, on the object.

`--version-id` (string)

An ID used to reference a specific version of the object.

`--bucket-key-enabled` | `--no-bucket-key-enabled` (boolean)

Indicates whether the object stored in Amazon S3 uses an S3 bucket key for server-side encryption with Amazon Web Services KMS (SSE-KMS).

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

None