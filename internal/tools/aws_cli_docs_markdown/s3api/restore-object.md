# restore-objectÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/restore-object.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/restore-object.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html#cli-aws-s3api) ]

# restore-object

## Description

### Note

This operation is not supported for directory buckets.

Restores an archived copy of an object back into Amazon S3

This functionality is not supported for Amazon S3 on Outposts.

This action performs the following types of requests:

- `restore an archive` - Restore an archived object

For more information about the `S3` structure in the request body, see the following:

- [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
- [Managing Access with ACLs](https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html) in the *Amazon S3 User Guide*
- [Protecting Data Using Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html) in the *Amazon S3 User Guide*

Permissions

To use this operation, you must have permissions to perform the `s3:RestoreObject` action. The bucket owner has this permission by default and can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Managing Access Permissions to Your Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) in the *Amazon S3 User Guide* .

Restoring objects

Objects that you archive to the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage class, and S3 Intelligent-Tiering Archive or S3 Intelligent-Tiering Deep Archive tiers, are not accessible in real time. For objects in the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes, you must first initiate a restore request, and then wait until a temporary copy of the object is available. If you want a permanent copy of the object, create a copy of it in the Amazon S3 Standard storage class in your S3 bucket. To access an archived object, you must restore the object for the duration (number of days) that you specify. For objects in the Archive Access or Deep Archive Access tiers of S3 Intelligent-Tiering, you must first initiate a restore request, and then wait until the object is moved into the Frequent Access tier.

To restore a specific object version, you can provide a version ID. If you donât provide a version ID, Amazon S3 restores the current version.

When restoring an archived object, you can specify one of the following data access tier options in the `Tier` element of the request body:

- `Expedited` - Expedited retrievals allow you to quickly access your data stored in the S3 Glacier Flexible Retrieval storage class or S3 Intelligent-Tiering Archive tier when occasional urgent requests for restoring archives are required. For all but the largest archived objects (250 MB+), data accessed using Expedited retrievals is typically made available within 1â5 minutes. Provisioned capacity ensures that retrieval capacity for Expedited retrievals is available when you need it. Expedited retrievals and provisioned capacity are not available for objects stored in the S3 Glacier Deep Archive storage class or S3 Intelligent-Tiering Deep Archive tier.
- `Standard` - Standard retrievals allow you to access any of your archived objects within several hours. This is the default option for retrieval requests that do not specify the retrieval option. Standard retrievals typically finish within 3â5 hours for objects stored in the S3 Glacier Flexible Retrieval storage class or S3 Intelligent-Tiering Archive tier. They typically finish within 12 hours for objects stored in the S3 Glacier Deep Archive storage class or S3 Intelligent-Tiering Deep Archive tier. Standard retrievals are free for objects stored in S3 Intelligent-Tiering.
- `Bulk` - Bulk retrievals free for objects stored in the S3 Glacier Flexible Retrieval and S3 Intelligent-Tiering storage classes, enabling you to retrieve large amounts, even petabytes, of data at no cost. Bulk retrievals typically finish within 5â12 hours for objects stored in the S3 Glacier Flexible Retrieval storage class or S3 Intelligent-Tiering Archive tier. Bulk retrievals are also the lowest-cost retrieval option when restoring objects from S3 Glacier Deep Archive. They typically finish within 48 hours for objects stored in the S3 Glacier Deep Archive storage class or S3 Intelligent-Tiering Deep Archive tier.

For more information about archive retrieval options and provisioned capacity for `Expedited` data access, see [Restoring Archived Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/restoring-objects.html) in the *Amazon S3 User Guide* .

You can use Amazon S3 restore speed upgrade to change the restore speed to a faster speed while it is in progress. For more information, see [Upgrading the speed of an in-progress restore](https://docs.aws.amazon.com/AmazonS3/latest/dev/restoring-objects.html#restoring-objects-upgrade-tier.title.html) in the *Amazon S3 User Guide* .

To get the status of object restoration, you can send a `HEAD` request. Operations return the `x-amz-restore` header, which provides information about the restoration status, in the response. You can use Amazon S3 event notifications to notify you when a restore is initiated or completed. For more information, see [Configuring Amazon S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html) in the *Amazon S3 User Guide* .

After restoring an archived object, you can update the restoration period by reissuing the request with a new period. Amazon S3 updates the restoration period relative to the current time and charges only for the request-there are no data transfer charges. You cannot update the restoration period when Amazon S3 is actively processing your current restore request for the object.

If your bucket has a lifecycle configuration with a rule that includes an expiration action, the object expiration overrides the life span that you specify in a restore request. For example, if you restore an object copy for 10 days, but the object is scheduled to expire in 3 days, Amazon S3 deletes the object in 3 days. For more information about lifecycle configuration, see [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html) and [Object Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) in *Amazon S3 User Guide* .

Responses

A successful action returns either the `200 OK` or `202 Accepted` status code.

- If the object is not previously restored, then Amazon S3 returns `202 Accepted` in the response.
- If the object is previously restored, Amazon S3 returns `200 OK` in the response.
- Special errors:
- *Code: RestoreAlreadyInProgress*
- *Cause: Object restore is already in progress.*
- *HTTP Status Code: 409 Conflict*
- *SOAP Fault Code Prefix: Client*
- - *Code: GlacierExpeditedRetrievalNotAvailable*
- *Cause: expedited retrievals are currently not available. Try again later. (Returned if there is insufficient capacity to process the Expedited request. This error applies only to Expedited retrievals and not to S3 Standard or Bulk retrievals.)*
- *HTTP Status Code: 503*
- *SOAP Fault Code Prefix: N/A*

The following operations are related to `RestoreObject` :

- [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html)
- [GetBucketNotificationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotificationConfiguration.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/RestoreObject)

## Synopsis

```
restore-object
--bucket <value>
--key <value>
[--version-id <value>]
[--restore-request <value>]
[--request-payer <value>]
[--checksum-algorithm <value>]
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

The bucket name containing the object to restore.

**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName* -*AccountId* .s3-accesspoint.*Region* .amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide* .

**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form `` *AccessPointName* -*AccountId* .*outpostID* .s3-outposts.*Region* .amazonaws.com`` . When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide* .

`--key` (string)

Object key for which the action was initiated.

`--version-id` (string)

VersionId used to reference a specific version of the object.

`--restore-request` (structure)

Container for restore job parameters.

Days -> (integer)

Lifetime of the active copy in days. Do not use with restores that specify `OutputLocation` .

The Days element is required for regular restores, and must not be provided for select requests.

GlacierJobParameters -> (structure)

S3 Glacier related parameters pertaining to this job. Do not use with restores that specify `OutputLocation` .

Tier -> (string)

Retrieval tier at which the restore will be processed.

Type -> (string)

### Warning

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/)

Type of restore request.

Tier -> (string)

Retrieval tier at which the restore will be processed.

Description -> (string)

The optional description for the job.

SelectParameters -> (structure)

### Warning

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/)

Describes the parameters for Select job types.

InputSerialization -> (structure)

Describes the serialization format of the object.

CSV -> (structure)

Describes the serialization of a CSV-encoded object.

FileHeaderInfo -> (string)

Describes the first line of input. Valid values are:

- `NONE` : First line is not a header.
- `IGNORE` : First line is a header, but you canât use the header values to indicate the column in an expression. You can use column position (such as _1, _2, â¦) to indicate the column (`SELECT s._1 FROM OBJECT s` ).
- `Use` : First line is a header, and you can use the header value to identify a column in an expression (`SELECT "name" FROM OBJECT` ).

Comments -> (string)

A single character used to indicate that a row should be ignored when the character is present at the start of that row. You can specify any character to indicate a comment line. The default character is `#` .

Default: `#`

QuoteEscapeCharacter -> (string)

A single character used for escaping the quotation mark character inside an already escaped value. For example, the value `""" a , b """` is parsed as `" a , b "` .

RecordDelimiter -> (string)

A single character used to separate individual records in the input. Instead of the default value, you can specify an arbitrary delimiter.

FieldDelimiter -> (string)

A single character used to separate individual fields in a record. You can specify an arbitrary delimiter.

QuoteCharacter -> (string)

A single character used for escaping when the field delimiter is part of the value. For example, if the value is `a, b` , Amazon S3 wraps this field value in quotation marks, as follows: `" a , b "` .

Type: String

Default: `"`

Ancestors: `CSV`

AllowQuotedRecordDelimiter -> (boolean)

Specifies that CSV field values may contain quoted record delimiters and such records should be allowed. Default value is FALSE. Setting this value to TRUE may lower performance.

CompressionType -> (string)

Specifies objectâs compression format. Valid values: NONE, GZIP, BZIP2. Default Value: NONE.

JSON -> (structure)

Specifies JSON as objectâs input serialization format.

Type -> (string)

The type of JSON. Valid values: Document, Lines.

Parquet -> (structure)

Specifies Parquet as objectâs input serialization format.

ExpressionType -> (string)

The type of the provided expression (for example, SQL).

Expression -> (string)

### Warning

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/)

The expression that is used to query the object.

OutputSerialization -> (structure)

Describes how the results of the Select job are serialized.

CSV -> (structure)

Describes the serialization of CSV-encoded Select results.

QuoteFields -> (string)

Indicates whether to use quotation marks around output fields.

- `ALWAYS` : Always use quotation marks for output fields.
- `ASNEEDED` : Use quotation marks for output fields when needed.

QuoteEscapeCharacter -> (string)

The single character used for escaping the quote character inside an already escaped value.

RecordDelimiter -> (string)

A single character used to separate individual records in the output. Instead of the default value, you can specify an arbitrary delimiter.

FieldDelimiter -> (string)

The value used to separate individual fields in a record. You can specify an arbitrary delimiter.

QuoteCharacter -> (string)

A single character used for escaping when the field delimiter is part of the value. For example, if the value is `a, b` , Amazon S3 wraps this field value in quotation marks, as follows: `" a , b "` .

JSON -> (structure)

Specifies JSON as requestâs output serialization format.

RecordDelimiter -> (string)

The value used to separate individual records in the output. If no value is specified, Amazon S3 uses a newline character (ânâ).

OutputLocation -> (structure)

Describes the location where the restore jobâs output is stored.

S3 -> (structure)

Describes an S3 location that will receive the results of the restore request.

BucketName -> (string)

The name of the bucket where the restore results will be placed.

Prefix -> (string)

The prefix that is prepended to the restore results for this request.

Encryption -> (structure)

Contains the type of server-side encryption used.

EncryptionType -> (string)

The server-side encryption algorithm used when storing job results in Amazon S3 (for example, AES256, `aws:kms` ).

KMSKeyId -> (string)

If the encryption type is `aws:kms` , this optional value specifies the ID of the symmetric encryption customer managed key to use for encryption of job results. Amazon S3 only supports symmetric encryption KMS keys. For more information, see [Asymmetric keys in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *Amazon Web Services Key Management Service Developer Guide* .

KMSContext -> (string)

If the encryption type is `aws:kms` , this optional value can be used to specify the encryption context for the restore results.

CannedACL -> (string)

The canned ACL to apply to the restore results.

AccessControlList -> (list)

A list of grants that control access to the staged results.

(structure)

Container for grant information.

Grantee -> (structure)

The person being granted permissions.

DisplayName -> (string)

Screen name of the grantee.

EmailAddress -> (string)

Email address of the grantee.

### Note

Using email addresses to specify a grantee is only supported in the following Amazon Web Services Regions:

- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Europe (Ireland)
- South America (SÃ£o Paulo)

For a list of all the Amazon S3 supported Regions and endpoints, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) in the Amazon Web Services General Reference.

ID -> (string)

The canonical user ID of the grantee.

Type -> (string)

Type of grantee

URI -> (string)

URI of the grantee group.

Permission -> (string)

Specifies the permission given to the grantee.

Tagging -> (structure)

The tag-set that is applied to the restore results.

TagSet -> (list)

A collection for a set of tags

(structure)

A container of a key value name pair.

Key -> (string)

Name of the object key.

Value -> (string)

Value of the tag.

UserMetadata -> (list)

A list of metadata to store with the restore results in S3.

(structure)

A metadata key-value pair to store with an object.

Name -> (string)

Name of the object.

Value -> (string)

Value of the object.

StorageClass -> (string)

The class of storage used to store the restore results.

JSON Syntax:

```
{
  "Days": integer,
  "GlacierJobParameters": {
    "Tier": "Standard"|"Bulk"|"Expedited"
  },
  "Type": "SELECT",
  "Tier": "Standard"|"Bulk"|"Expedited",
  "Description": "string",
  "SelectParameters": {
    "InputSerialization": {
      "CSV": {
        "FileHeaderInfo": "USE"|"IGNORE"|"NONE",
        "Comments": "string",
        "QuoteEscapeCharacter": "string",
        "RecordDelimiter": "string",
        "FieldDelimiter": "string",
        "QuoteCharacter": "string",
        "AllowQuotedRecordDelimiter": true|false
      },
      "CompressionType": "NONE"|"GZIP"|"BZIP2",
      "JSON": {
        "Type": "DOCUMENT"|"LINES"
      },
      "Parquet": {

      }
    },
    "ExpressionType": "SQL",
    "Expression": "string",
    "OutputSerialization": {
      "CSV": {
        "QuoteFields": "ALWAYS"|"ASNEEDED",
        "QuoteEscapeCharacter": "string",
        "RecordDelimiter": "string",
        "FieldDelimiter": "string",
        "QuoteCharacter": "string"
      },
      "JSON": {
        "RecordDelimiter": "string"
      }
    }
  },
  "OutputLocation": {
    "S3": {
      "BucketName": "string",
      "Prefix": "string",
      "Encryption": {
        "EncryptionType": "AES256"|"aws:kms"|"aws:kms:dsse",
        "KMSKeyId": "string",
        "KMSContext": "string"
      },
      "CannedACL": "private"|"public-read"|"public-read-write"|"authenticated-read"|"aws-exec-read"|"bucket-owner-read"|"bucket-owner-full-control",
      "AccessControlList": [
        {
          "Grantee": {
            "DisplayName": "string",
            "EmailAddress": "string",
            "ID": "string",
            "Type": "CanonicalUser"|"AmazonCustomerByEmail"|"Group",
            "URI": "string"
          },
          "Permission": "FULL_CONTROL"|"WRITE"|"WRITE_ACP"|"READ"|"READ_ACP"
        }
        ...
      ],
      "Tagging": {
        "TagSet": [
          {
            "Key": "string",
            "Value": "string"
          }
          ...
        ]
      },
      "UserMetadata": [
        {
          "Name": "string",
          "Value": "string"
        }
        ...
      ],
      "StorageClass": "STANDARD"|"REDUCED_REDUNDANCY"|"STANDARD_IA"|"ONEZONE_IA"|"INTELLIGENT_TIERING"|"GLACIER"|"DEEP_ARCHIVE"|"OUTPOSTS"|"GLACIER_IR"|"SNOW"|"EXPRESS_ONEZONE"
    }
  }
}
```

`--request-payer` (string)

Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for corresponding charges to copy the object. For information about downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported for directory buckets.

Possible values:

- `requester`

`--checksum-algorithm` (string)

Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any additional functionality if you donât use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request` . For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm` parameter.

Possible values:

- `CRC32`
- `CRC32C`
- `SHA1`
- `SHA256`
- `CRC64NVME`

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

**To create a restore request for an object**

The following `restore-object` example restores the specified Amazon S3 Glacier object for the bucket `my-glacier-bucket` for 10 days.

```
aws s3api restore-object \
    --bucket my-glacier-bucket \
    --key doc1.rtf \
    --restore-request Days=10
```

This command produces no output.

## Output

RequestCharged -> (string)

If present, indicates that the requester was successfully charged for the request.

### Note

This functionality is not supported for directory buckets.

RestoreOutputPath -> (string)

Indicates the path in the provided S3 output location where Select results will be restored to.