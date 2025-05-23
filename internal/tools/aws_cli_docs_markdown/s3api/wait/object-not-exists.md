# object-not-existsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/wait/object-not-exists.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/wait/object-not-exists.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html#cli-aws-s3api) . [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/wait/index.html#cli-aws-s3api-wait) ]

# object-not-exists

## Description

Wait until 404 response is received when polling with `head-object`. It will poll every 5 seconds until a successful state has been reached. This will exit with a return code of 255 after 20 failed checks.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadObject)

## Synopsis

```
object-not-exists
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

`--if-match` (string)

Return the object only if its entity tag (ETag) is the same as the one specified; otherwise, return a 412 (precondition failed) error.

If both of the `If-Match` and `If-Unmodified-Since` headers are present in the request as follows:

- `If-Match` condition evaluates to `true` , and;
- `If-Unmodified-Since` condition evaluates to `false` ;

Then Amazon S3 returns `200 OK` and the data requested.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232) .

`--if-modified-since` (timestamp)

Return the object only if it has been modified since the specified time; otherwise, return a 304 (not modified) error.

If both of the `If-None-Match` and `If-Modified-Since` headers are present in the request as follows:

- `If-None-Match` condition evaluates to `false` , and;
- `If-Modified-Since` condition evaluates to `true` ;

Then Amazon S3 returns the `304 Not Modified` response code.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232) .

`--if-none-match` (string)

Return the object only if its entity tag (ETag) is different from the one specified; otherwise, return a 304 (not modified) error.

If both of the `If-None-Match` and `If-Modified-Since` headers are present in the request as follows:

- `If-None-Match` condition evaluates to `false` , and;
- `If-Modified-Since` condition evaluates to `true` ;

Then Amazon S3 returns the `304 Not Modified` response code.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232) .

`--if-unmodified-since` (timestamp)

Return the object only if it has not been modified since the specified time; otherwise, return a 412 (precondition failed) error.

If both of the `If-Match` and `If-Unmodified-Since` headers are present in the request as follows:

- `If-Match` condition evaluates to `true` , and;
- `If-Unmodified-Since` condition evaluates to `false` ;

Then Amazon S3 returns `200 OK` and the data requested.

For more information about conditional requests, see [RFC 7232](https://tools.ietf.org/html/rfc7232) .

`--key` (string)

The object key.

`--range` (string)

HeadObject returns only the metadata for an object. If the Range is satisfiable, only the `ContentLength` is affected in the response. If the Range is not satisfiable, S3 returns a `416 - Requested Range Not Satisfiable` error.

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

### Note

For directory buckets in this API operation, only the `null` value of the version ID is supported.

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

`--part-number` (integer)

Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a ârangedâ HEAD request for the part specified. Useful querying about the size of the part and the number of parts in this object.

`--expected-bucket-owner` (string)

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

`--checksum-mode` (string)

To retrieve the checksum, this parameter must be enabled.

**General purpose buckets** - If you enable checksum mode and the object is uploaded with a [checksum](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Checksum.html) and encrypted with an Key Management Service (KMS) key, you must have permission to use the `kms:Decrypt` action to retrieve the checksum.

**Directory buckets** - If you enable `ChecksumMode` and the object is encrypted with Amazon Web Services Key Management Service (Amazon Web Services KMS), you must also have the `kms:GenerateDataKey` and `kms:Decrypt` permissions in IAM identity-based policies and KMS key policies for the KMS key to retrieve the checksum of the object.

Possible values:

- `ENABLED`

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

**To wait (pause running) until an object no longer exists**

The following `wait object-not-exists` example pauses and continues only after it can confirm that the specified object (`--key`) in the specified bucket doesnât exist.

```
aws s3api wait object-not-exists \
    --bucket amzn-s3-demo-bucket \
    --key doc1.rtf
```

This command produces no output.

## Output

None