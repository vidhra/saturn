# delete-objectsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html#cli-aws-s3api) ]

# delete-objects

## Description

This operation enables you to delete multiple objects from a bucket using a single HTTP request. If you know the object keys that you want to delete, then this operation provides a suitable alternative to sending individual delete requests, reducing per-request overhead.

The request can contain a list of up to 1,000 keys that you want to delete. In the XML, you provide the object key names, and optionally, version IDs if you want to delete a specific version of the object from a versioning-enabled bucket. For each key, Amazon S3 performs a delete operation and returns the result of that delete, success or failure, in the response. If the object specified in the request isnât found, Amazon S3 confirms the deletion by returning the result as deleted.

### Note

- **Directory buckets** - S3 Versioning isnât enabled and supported for directory buckets.
- **Directory buckets** - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html#id1)[https://](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html)*amzn-s3-demo-bucket* .s3express-*zone-id* .*region-code* .amazonaws.com/*key-name* `` . Path-style requests are not supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the *Amazon S3 User Guide* . For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the *Amazon S3 User Guide* .

The operation supports two modes for the response: verbose and quiet. By default, the operation uses verbose mode in which the response includes the result of deletion of each key in your request. In quiet mode the response includes only keys where the delete operation encountered an error. For a successful deletion in a quiet mode, the operation does not return any information about the delete in the response body.

When performing this action on an MFA Delete enabled bucket, that attempts to delete any versioned objects, you must include an MFA token. If you do not provide one, the entire request will fail, even if there are non-versioned objects you are trying to delete. If you provide an invalid token, whether there are versioned keys in the request or not, the entire Multi-Object Delete request will fail. For information about MFA Delete, see [MFA Delete](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html#MultiFactorAuthenticationDelete) in the *Amazon S3 User Guide* .

### Note

**Directory buckets** - MFA delete is not supported by directory buckets.

Permissions

- **General purpose bucket permissions** - The following permissions are required in your policies when your `DeleteObjects` request includes specific headers.

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html#id3)`s3:DeleteObject` ** - To delete an object from a bucket, you must always specify the `s3:DeleteObject` permission.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html#id5)`s3:DeleteObjectVersion` ** - To delete a specific version of an object from a versioning-enabled bucket, you must specify the `s3:DeleteObjectVersion` permission.
- **Directory bucket permissions** - To grant access to this API operation on a directory bucket, we recommend that you use the ` `CreateSession` [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession).html`__ API operation for session-based authorization. Specifically, you grant the `s3express:CreateSession` permission to the directory bucket in a bucket policy or an IAM identity-based policy. Then, you make the `CreateSession` API call on the bucket to obtain a session token. With the session token in your request header, you can make API requests to this operation. After the session token expires, you make another `CreateSession` API call to generate a new session token for use. Amazon Web Services CLI or SDKs create session and refresh the session token automatically to avoid service interruptions when a session expires. For more information about authorization, see ` `CreateSession` [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession).html`__ .

Content-MD5 request header
- **General purpose bucket** - The Content-MD5 request header is required for all Multi-Object Delete requests. Amazon S3 uses the header value to ensure that your request body has not been altered in transit.
- **Directory bucket** - The Content-MD5 request header or a additional checksum request header (including `x-amz-checksum-crc32` , `x-amz-checksum-crc32c` , `x-amz-checksum-sha1` , or `x-amz-checksum-sha256` ) is required for all Multi-Object Delete requests.

HTTP Host header syntax

**Directory buckets** - The HTTP Host header syntax is `` *Bucket-name* .s3express-*zone-id* .*region-code* .amazonaws.com`` .

The following operations are related to `DeleteObjects` :

- [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)
- [UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html)
- [CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html)
- [ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)
- [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteObjects)

## Synopsis

```
delete-objects
--bucket <value>
--delete <value>
[--mfa <value>]
[--request-payer <value>]
[--bypass-governance-retention | --no-bypass-governance-retention]
[--expected-bucket-owner <value>]
[--checksum-algorithm <value>]
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

The bucket name containing the objects to delete.

**Directory buckets** - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format `` *Bucket-name* .s3express-*zone-id* .*region-code* .amazonaws.com`` . Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format `` *bucket-base-name* â*zone-id* âx-s3`` (for example, `` *amzn-s3-demo-bucket* â*usw2-az1* âx-s3`` ). For information about bucket naming restrictions, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide* .

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName* -*AccountId* .s3-accesspoint.*Region* .amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide* .

### Note

Object Lambda access points are not supported by directory buckets.

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form `` *AccessPointName* -*AccountId* .*outpostID* .s3-outposts.*Region* .amazonaws.com`` . When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide* .

`--delete` (structure)

Container for the request.

Objects -> (list)

The object to delete.

### Note

**Directory buckets** - For directory buckets, an object thatâs composed entirely of whitespace characters is not supported by the `DeleteObjects` API operation. The request will receive a `400 Bad Request` error and none of the objects in the request will be deleted.

(structure)

Object Identifier is unique value to identify objects.

Key -> (string)

Key name of the object.

### Warning

Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see [XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints) .

VersionId -> (string)

Version ID for the specific version of the object to delete.

### Note

This functionality is not supported for directory buckets.

ETag -> (string)

An entity tag (ETag) is an identifier assigned by a web server to a specific version of a resource found at a URL. This header field makes the request method conditional on `ETags` .

### Note

Entity tags (ETags) for S3 Express One Zone are random alphanumeric strings unique to the object.

LastModifiedTime -> (timestamp)

If present, the objects are deleted only if its modification times matches the provided `Timestamp` .

### Note

This functionality is only supported for directory buckets.

Size -> (long)

If present, the objects are deleted only if its size matches the provided size in bytes.

### Note

This functionality is only supported for directory buckets.

Quiet -> (boolean)

Element to enable quiet mode for the request. When you add this element, you must set its value to `true` .

Shorthand Syntax:

```
Objects=[{Key=string,VersionId=string,ETag=string,LastModifiedTime=timestamp,Size=long},{Key=string,VersionId=string,ETag=string,LastModifiedTime=timestamp,Size=long}],Quiet=boolean
```

JSON Syntax:

```
{
  "Objects": [
    {
      "Key": "string",
      "VersionId": "string",
      "ETag": "string",
      "LastModifiedTime": timestamp,
      "Size": long
    }
    ...
  ],
  "Quiet": true|false
}
```

`--mfa` (string)

The concatenation of the authentication deviceâs serial number, a space, and the value that is displayed on your authentication device. Required to permanently delete a versioned object if versioning is configured with MFA delete enabled.

When performing the `DeleteObjects` operation on an MFA delete enabled bucket, which attempts to delete the specified versioned objects, you must include an MFA token. If you donât provide an MFA token, the entire request will fail, even if there are non-versioned objects that you are trying to delete. If you provide an invalid token, whether there are versioned object keys in the request or not, the entire Multi-Object Delete request will fail. For information about MFA Delete, see [MFA Delete](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html#MultiFactorAuthenticationDelete) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported for directory buckets.

`--request-payer` (string)

Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for corresponding charges to copy the object. For information about downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported for directory buckets.

Possible values:

- `requester`

`--bypass-governance-retention` | `--no-bypass-governance-retention` (boolean)

Specifies whether you want to delete this object even if it has a Governance-type Object Lock in place. To use this header, you must have the `s3:BypassGovernanceRetention` permission.

### Note

This functionality is not supported for directory buckets.

`--expected-bucket-owner` (string)

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

`--checksum-algorithm` (string)

Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any additional functionality if you donât use the SDK. When you send this header, there must be a corresponding `x-amz-checksum-*algorithm* `` or ``x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request` .

For the [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html#id7)x-amz-checksum-*algorithm* `` header, replace `` *algorithm* `` with the supported algorithm from the following list:

- `CRC32`
- `CRC32C`
- `CRC64NVME`
- `SHA1`
- `SHA256`

For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

If the individual checksum value you provide through `x-amz-checksum-*algorithm* `` doesn't match the checksum algorithm you set through ``x-amz-sdk-checksum-algorithm` , Amazon S3 fails the request with a `BadDigest` error.

If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm` parameter.

Possible values:

- `CRC32`
- `CRC32C`
- `SHA1`
- `SHA256`
- `CRC64NVME`

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

The following command deletes an object from a bucket named `amzn-s3-demo-bucket`:

```
aws s3api delete-objects --bucket amzn-s3-demo-bucket --delete file://delete.json
```

`delete.json` is a JSON document in the current directory that specifies the object to delete:

```
{
  "Objects": [
    {
      "Key": "test1.txt"
    }
  ],
  "Quiet": false
}
```

Output:

```
{
    "Deleted": [
        {
            "DeleteMarkerVersionId": "mYAT5Mc6F7aeUL8SS7FAAqUPO1koHwzU",
            "Key": "test1.txt",
            "DeleteMarker": true
        }
    ]
}
```

## Output

Deleted -> (list)

Container element for a successful delete. It identifies the object that was successfully deleted.

(structure)

Information about the deleted object.

Key -> (string)

The name of the deleted object.

VersionId -> (string)

The version ID of the deleted object.

### Note

This functionality is not supported for directory buckets.

DeleteMarker -> (boolean)

Indicates whether the specified object version that was permanently deleted was (true) or was not (false) a delete marker before deletion. In a simple DELETE, this header indicates whether (true) or not (false) the current version of the object is a delete marker. To learn more about delete markers, see [Working with delete markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html) .

### Note

This functionality is not supported for directory buckets.

DeleteMarkerVersionId -> (string)

The version ID of the delete marker created as a result of the DELETE operation. If you delete a specific object version, the value returned by this header is the version ID of the object version deleted.

### Note

This functionality is not supported for directory buckets.

RequestCharged -> (string)

If present, indicates that the requester was successfully charged for the request.

### Note

This functionality is not supported for directory buckets.

Errors -> (list)

Container for a failed delete action that describes the object that Amazon S3 attempted to delete and the error it encountered.

(structure)

Container for all error elements.

Key -> (string)

The error key.

VersionId -> (string)

The version ID of the error.

### Note

This functionality is not supported for directory buckets.

Code -> (string)

The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type. The following is a list of Amazon S3 error codes. For more information, see [Error responses](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html) .

- - *Code:* AccessDenied
- *Description:* Access Denied
- *HTTP Status Code:* 403 Forbidden
- *SOAP Fault Code Prefix:* Client
- - *Code:* AccountProblem
- *Description:* There is a problem with your Amazon Web Services account that prevents the action from completing successfully. Contact Amazon Web Services Support for further assistance.
- *HTTP Status Code:* 403 Forbidden
- *SOAP Fault Code Prefix:* Client
- - *Code:* AllAccessDisabled
- *Description:* All access to this Amazon S3 resource has been disabled. Contact Amazon Web Services Support for further assistance.
- *HTTP Status Code:* 403 Forbidden
- *SOAP Fault Code Prefix:* Client
- - *Code:* AmbiguousGrantByEmailAddress
- *Description:* The email address you provided is associated with more than one account.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* AuthorizationHeaderMalformed
- *Description:* The authorization header you provided is invalid.
- *HTTP Status Code:* 400 Bad Request
- *HTTP Status Code:* N/A
- - *Code:* BadDigest
- *Description:* The Content-MD5 you specified did not match what we received.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* BucketAlreadyExists
- *Description:* The requested bucket name is not available. The bucket namespace is shared by all users of the system. Please select a different name and try again.
- *HTTP Status Code:* 409 Conflict
- *SOAP Fault Code Prefix:* Client
- - *Code:* BucketAlreadyOwnedByYou
- *Description:* The bucket you tried to create already exists, and you own it. Amazon S3 returns this error in all Amazon Web Services Regions except in the North Virginia Region. For legacy compatibility, if you re-create an existing bucket that you already own in the North Virginia Region, Amazon S3 returns 200 OK and resets the bucket access control lists (ACLs).
- *Code:* 409 Conflict (in all Regions except the North Virginia Region)
- *SOAP Fault Code Prefix:* Client
- - *Code:* BucketNotEmpty
- *Description:* The bucket you tried to delete is not empty.
- *HTTP Status Code:* 409 Conflict
- *SOAP Fault Code Prefix:* Client
- - *Code:* CredentialsNotSupported
- *Description:* This request does not support credentials.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* CrossLocationLoggingProhibited
- *Description:* Cross-location logging not allowed. Buckets in one geographic location cannot log information to a bucket in another location.
- *HTTP Status Code:* 403 Forbidden
- *SOAP Fault Code Prefix:* Client
- - *Code:* EntityTooSmall
- *Description:* Your proposed upload is smaller than the minimum allowed object size.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* EntityTooLarge
- *Description:* Your proposed upload exceeds the maximum allowed object size.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* ExpiredToken
- *Description:* The provided token has expired.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* IllegalVersioningConfigurationException
- *Description:* Indicates that the versioning configuration specified in the request is invalid.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* IncompleteBody
- *Description:* You did not provide the number of bytes specified by the Content-Length HTTP header
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* IncorrectNumberOfFilesInPostRequest
- *Description:* POST requires exactly one file upload per request.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* InlineDataTooLarge
- *Description:* Inline data exceeds the maximum allowed size.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* InternalError
- *Description:* We encountered an internal error. Please try again.
- *HTTP Status Code:* 500 Internal Server Error
- *SOAP Fault Code Prefix:* Server
- - *Code:* InvalidAccessKeyId
- *Description:* The Amazon Web Services access key ID you provided does not exist in our records.
- *HTTP Status Code:* 403 Forbidden
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidAddressingHeader
- *Description:* You must specify the Anonymous role.
- *HTTP Status Code:* N/A
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidArgument
- *Description:* Invalid Argument
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidBucketName
- *Description:* The specified bucket is not valid.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidBucketState
- *Description:* The request is not valid with the current state of the bucket.
- *HTTP Status Code:* 409 Conflict
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidDigest
- *Description:* The Content-MD5 you specified is not valid.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidEncryptionAlgorithmError
- *Description:* The encryption request you specified is not valid. The valid value is AES256.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidLocationConstraint
- *Description:* The specified location constraint is not valid. For more information about Regions, see [How to Select a Region for Your Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html#access-bucket-intro) .
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidObjectState
- *Description:* The action is not valid for the current state of the object.
- *HTTP Status Code:* 403 Forbidden
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidPart
- *Description:* One or more of the specified parts could not be found. The part might not have been uploaded, or the specified entity tag might not have matched the partâs entity tag.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidPartOrder
- *Description:* The list of parts was not in ascending order. Parts list must be specified in order by part number.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidPayer
- *Description:* All access to this object has been disabled. Please contact Amazon Web Services Support for further assistance.
- *HTTP Status Code:* 403 Forbidden
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidPolicyDocument
- *Description:* The content of the form does not meet the conditions specified in the policy document.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidRange
- *Description:* The requested range cannot be satisfied.
- *HTTP Status Code:* 416 Requested Range Not Satisfiable
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidRequest
- *Description:* Please use `AWS4-HMAC-SHA256` .
- *HTTP Status Code:* 400 Bad Request
- *Code:* N/A
- - *Code:* InvalidRequest
- *Description:* SOAP requests must be made over an HTTPS connection.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidRequest
- *Description:* Amazon S3 Transfer Acceleration is not supported for buckets with non-DNS compliant names.
- *HTTP Status Code:* 400 Bad Request
- *Code:* N/A
- - *Code:* InvalidRequest
- *Description:* Amazon S3 Transfer Acceleration is not supported for buckets with periods (.) in their names.
- *HTTP Status Code:* 400 Bad Request
- *Code:* N/A
- - *Code:* InvalidRequest
- *Description:* Amazon S3 Transfer Accelerate endpoint only supports virtual style requests.
- *HTTP Status Code:* 400 Bad Request
- *Code:* N/A
- - *Code:* InvalidRequest
- *Description:* Amazon S3 Transfer Accelerate is not configured on this bucket.
- *HTTP Status Code:* 400 Bad Request
- *Code:* N/A
- - *Code:* InvalidRequest
- *Description:* Amazon S3 Transfer Accelerate is disabled on this bucket.
- *HTTP Status Code:* 400 Bad Request
- *Code:* N/A
- - *Code:* InvalidRequest
- *Description:* Amazon S3 Transfer Acceleration is not supported on this bucket. Contact Amazon Web Services Support for more information.
- *HTTP Status Code:* 400 Bad Request
- *Code:* N/A
- - *Code:* InvalidRequest
- *Description:* Amazon S3 Transfer Acceleration cannot be enabled on this bucket. Contact Amazon Web Services Support for more information.
- *HTTP Status Code:* 400 Bad Request
- *Code:* N/A
- - *Code:* InvalidSecurity
- *Description:* The provided security credentials are not valid.
- *HTTP Status Code:* 403 Forbidden
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidSOAPRequest
- *Description:* The SOAP request body is invalid.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidStorageClass
- *Description:* The storage class you specified is not valid.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidTargetBucketForLogging
- *Description:* The target bucket for logging does not exist, is not owned by you, or does not have the appropriate grants for the log-delivery group.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidToken
- *Description:* The provided token is malformed or otherwise invalid.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* InvalidURI
- *Description:* Couldnât parse the specified URI.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* KeyTooLongError
- *Description:* Your key is too long.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* MalformedACLError
- *Description:* The XML you provided was not well-formed or did not validate against our published schema.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* MalformedPOSTRequest
- *Description:* The body of your POST request is not well-formed multipart/form-data.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* MalformedXML
- *Description:* This happens when the user sends malformed XML (XML that doesnât conform to the published XSD) for the configuration. The error message is, âThe XML you provided was not well-formed or did not validate against our published schema.â
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* MaxMessageLengthExceeded
- *Description:* Your request was too big.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* MaxPostPreDataLengthExceededError
- *Description:* Your POST request fields preceding the upload file were too large.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* MetadataTooLarge
- *Description:* Your metadata headers exceed the maximum allowed metadata size.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* MethodNotAllowed
- *Description:* The specified method is not allowed against this resource.
- *HTTP Status Code:* 405 Method Not Allowed
- *SOAP Fault Code Prefix:* Client
- - *Code:* MissingAttachment
- *Description:* A SOAP attachment was expected, but none were found.
- *HTTP Status Code:* N/A
- *SOAP Fault Code Prefix:* Client
- - *Code:* MissingContentLength
- *Description:* You must provide the Content-Length HTTP header.
- *HTTP Status Code:* 411 Length Required
- *SOAP Fault Code Prefix:* Client
- - *Code:* MissingRequestBodyError
- *Description:* This happens when the user sends an empty XML document as a request. The error message is, âRequest body is empty.â
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* MissingSecurityElement
- *Description:* The SOAP 1.1 request is missing a security element.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* MissingSecurityHeader
- *Description:* Your request is missing a required header.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* NoLoggingStatusForKey
- *Description:* There is no such thing as a logging status subresource for a key.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* NoSuchBucket
- *Description:* The specified bucket does not exist.
- *HTTP Status Code:* 404 Not Found
- *SOAP Fault Code Prefix:* Client
- - *Code:* NoSuchBucketPolicy
- *Description:* The specified bucket does not have a bucket policy.
- *HTTP Status Code:* 404 Not Found
- *SOAP Fault Code Prefix:* Client
- - *Code:* NoSuchKey
- *Description:* The specified key does not exist.
- *HTTP Status Code:* 404 Not Found
- *SOAP Fault Code Prefix:* Client
- - *Code:* NoSuchLifecycleConfiguration
- *Description:* The lifecycle configuration does not exist.
- *HTTP Status Code:* 404 Not Found
- *SOAP Fault Code Prefix:* Client
- - *Code:* NoSuchUpload
- *Description:* The specified multipart upload does not exist. The upload ID might be invalid, or the multipart upload might have been aborted or completed.
- *HTTP Status Code:* 404 Not Found
- *SOAP Fault Code Prefix:* Client
- - *Code:* NoSuchVersion
- *Description:* Indicates that the version ID specified in the request does not match an existing version.
- *HTTP Status Code:* 404 Not Found
- *SOAP Fault Code Prefix:* Client
- - *Code:* NotImplemented
- *Description:* A header you provided implies functionality that is not implemented.
- *HTTP Status Code:* 501 Not Implemented
- *SOAP Fault Code Prefix:* Server
- - *Code:* NotSignedUp
- *Description:* Your account is not signed up for the Amazon S3 service. You must sign up before you can use Amazon S3. You can sign up at the following URL: [Amazon S3](http://aws.amazon.com/s3)
- *HTTP Status Code:* 403 Forbidden
- *SOAP Fault Code Prefix:* Client
- - *Code:* OperationAborted
- *Description:* A conflicting conditional action is currently in progress against this resource. Try again.
- *HTTP Status Code:* 409 Conflict
- *SOAP Fault Code Prefix:* Client
- - *Code:* PermanentRedirect
- *Description:* The bucket you are attempting to access must be addressed using the specified endpoint. Send all future requests to this endpoint.
- *HTTP Status Code:* 301 Moved Permanently
- *SOAP Fault Code Prefix:* Client
- - *Code:* PreconditionFailed
- *Description:* At least one of the preconditions you specified did not hold.
- *HTTP Status Code:* 412 Precondition Failed
- *SOAP Fault Code Prefix:* Client
- - *Code:* Redirect
- *Description:* Temporary redirect.
- *HTTP Status Code:* 307 Moved Temporarily
- *SOAP Fault Code Prefix:* Client
- - *Code:* RestoreAlreadyInProgress
- *Description:* Object restore is already in progress.
- *HTTP Status Code:* 409 Conflict
- *SOAP Fault Code Prefix:* Client
- - *Code:* RequestIsNotMultiPartContent
- *Description:* Bucket POST must be of the enclosure-type multipart/form-data.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* RequestTimeout
- *Description:* Your socket connection to the server was not read from or written to within the timeout period.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* RequestTimeTooSkewed
- *Description:* The difference between the request time and the serverâs time is too large.
- *HTTP Status Code:* 403 Forbidden
- *SOAP Fault Code Prefix:* Client
- - *Code:* RequestTorrentOfBucketError
- *Description:* Requesting the torrent file of a bucket is not permitted.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* SignatureDoesNotMatch
- *Description:* The request signature we calculated does not match the signature you provided. Check your Amazon Web Services secret access key and signing method. For more information, see [REST Authentication](https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html) and [SOAP Authentication](https://docs.aws.amazon.com/AmazonS3/latest/dev/SOAPAuthentication.html) for details.
- *HTTP Status Code:* 403 Forbidden
- *SOAP Fault Code Prefix:* Client
- - *Code:* ServiceUnavailable
- *Description:* Service is unable to handle request.
- *HTTP Status Code:* 503 Service Unavailable
- *SOAP Fault Code Prefix:* Server
- - *Code:* SlowDown
- *Description:* Reduce your request rate.
- *HTTP Status Code:* 503 Slow Down
- *SOAP Fault Code Prefix:* Server
- - *Code:* TemporaryRedirect
- *Description:* You are being redirected to the bucket while DNS updates.
- *HTTP Status Code:* 307 Moved Temporarily
- *SOAP Fault Code Prefix:* Client
- - *Code:* TokenRefreshRequired
- *Description:* The provided token must be refreshed.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* TooManyBuckets
- *Description:* You have attempted to create more buckets than allowed.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* UnexpectedContent
- *Description:* This request does not support content.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* UnresolvableGrantByEmailAddress
- *Description:* The email address you provided does not match any account on record.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client
- - *Code:* UserKeyMustBeSpecified
- *Description:* The bucket POST must contain the specified field name. If it is specified, check the order of the fields.
- *HTTP Status Code:* 400 Bad Request
- *SOAP Fault Code Prefix:* Client

Message -> (string)

The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they donât know how or donât care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.