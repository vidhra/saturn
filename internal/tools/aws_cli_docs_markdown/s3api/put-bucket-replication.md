# put-bucket-replicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-replication.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-replication.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html#cli-aws-s3api) ]

# put-bucket-replication

## Description

### Note

This operation is not supported for directory buckets.

Creates a replication configuration or replaces an existing one. For more information, see [Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html) in the *Amazon S3 User Guide* .

Specify the replication configuration in the request body. In the replication configuration, you provide the name of the destination bucket or buckets where you want Amazon S3 to replicate objects, the IAM role that Amazon S3 can assume to replicate objects on your behalf, and other relevant information. You can invoke this request for a specific Amazon Web Services Region by using the ` `aws:RequestedRegion` [https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys)-requestedregion`__ condition key.

A replication configuration must include at least one rule, and can contain a maximum of 1,000. Each rule identifies a subset of objects to replicate by filtering the objects in the source bucket. To choose additional subsets of objects to replicate, add a rule for each subset.

To specify a subset of the objects in the source bucket to apply a replication rule to, add the Filter element as a child of the Rule element. You can filter objects based on an object key prefix, one or more object tags, or both. When you add the Filter element in the configuration, you must also add the following elements: `DeleteMarkerReplication` , `Status` , and `Priority` .

### Note

If you are using an earlier version of the replication configuration, Amazon S3 handles replication of delete markers differently. For more information, see [Backward Compatibility](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-backward-compat-considerations) .

For information about enabling versioning on a bucket, see [Using Versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) .

Handling Replication of Encrypted Objects

By default, Amazon S3 doesnât replicate objects that are stored at rest using server-side encryption with KMS keys. To replicate Amazon Web Services KMS-encrypted objects, add the following: `SourceSelectionCriteria` , `SseKmsEncryptedObjects` , `Status` , `EncryptionConfiguration` , and `ReplicaKmsKeyID` . For information about replication configuration, see [Replicating Objects Created with SSE Using KMS keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-config-for-kms-objects.html) .

For information on `PutBucketReplication` errors, see [List of replication-related error codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ReplicationErrorCodeList)

Permissions

To create a `PutBucketReplication` request, you must have `s3:PutReplicationConfiguration` permissions for the bucket.

By default, a resource owner, in this case the Amazon Web Services account that created the bucket, can perform this operation. The resource owner can also grant others permissions to perform the operation. For more information about permissions, see [Specifying Permissions in a Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html) and [Managing Access Permissions to Your Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) .

### Note

To perform this operation, the user or role performing the action must have the [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) permission.

The following operations are related to `PutBucketReplication` :

- [GetBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketReplication.html)
- [DeleteBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketReplication.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketReplication)

## Synopsis

```
put-bucket-replication
--bucket <value>
[--content-md5 <value>]
[--checksum-algorithm <value>]
--replication-configuration <value>
[--token <value>]
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

The name of the bucket

`--content-md5` (string)

The Base64 encoded 128-bit `MD5` digest of the data. You must use this header as a message integrity check to verify that the request body was not corrupted in transit. For more information, see [RFC 1864](http://www.ietf.org/rfc/rfc1864.txt) .

For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.

`--checksum-algorithm` (string)

Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any additional functionality if you donât use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request` . For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm` parameter.

Possible values:

- `CRC32`
- `CRC32C`
- `SHA1`
- `SHA256`
- `CRC64NVME`

`--replication-configuration` (structure)

A container for replication rules. You can add up to 1,000 rules. The maximum size of a replication configuration is 2 MB.

Role -> (string)

The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that Amazon S3 assumes when replicating objects. For more information, see [How to Set Up Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-how-setup.html) in the *Amazon S3 User Guide* .

Rules -> (list)

A container for one or more replication rules. A replication configuration must have at least one rule and can contain a maximum of 1,000 rules.

(structure)

Specifies which Amazon S3 objects to replicate and where to store the replicas.

ID -> (string)

A unique identifier for the rule. The maximum value is 255 characters.

Priority -> (integer)

The priority indicates which rule has precedence whenever two or more replication rules conflict. Amazon S3 will attempt to replicate objects according to all replication rules. However, if there are two or more rules with the same destination bucket, then objects will be replicated according to the rule with the highest priority. The higher the number, the higher the priority.

For more information, see [Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html) in the *Amazon S3 User Guide* .

Prefix -> (string)

An object key name prefix that identifies the object or objects to which the rule applies. The maximum prefix length is 1,024 characters. To include all objects in a bucket, specify an empty string.

### Warning

Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see [XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints) .

Filter -> (structure)

A filter that identifies the subset of objects to which the replication rule applies. A `Filter` must specify exactly one `Prefix` , `Tag` , or an `And` child element.

Prefix -> (string)

An object key name prefix that identifies the subset of objects to which the rule applies.

### Warning

Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see [XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints) .

Tag -> (structure)

A container for specifying a tag key and value.

The rule applies only to objects that have the tag in their tag set.

Key -> (string)

Name of the object key.

Value -> (string)

Value of the tag.

And -> (structure)

A container for specifying rule filters. The filters determine the subset of objects to which the rule applies. This element is required only if you specify more than one filter. For example:

- If you specify both a `Prefix` and a `Tag` filter, wrap these filters in an `And` tag.
- If you specify a filter based on multiple tags, wrap the `Tag` elements in an `And` tag.

Prefix -> (string)

An object key name prefix that identifies the subset of objects to which the rule applies.

Tags -> (list)

An array of tags containing key and value pairs.

(structure)

A container of a key value name pair.

Key -> (string)

Name of the object key.

Value -> (string)

Value of the tag.

Status -> (string)

Specifies whether the rule is enabled.

SourceSelectionCriteria -> (structure)

A container that describes additional filters for identifying the source objects that you want to replicate. You can choose to enable or disable the replication of these objects. Currently, Amazon S3 supports only the filter that you can specify for objects created with server-side encryption using a customer managed key stored in Amazon Web Services Key Management Service (SSE-KMS).

SseKmsEncryptedObjects -> (structure)

A container for filter information for the selection of Amazon S3 objects encrypted with Amazon Web Services KMS. If you include `SourceSelectionCriteria` in the replication configuration, this element is required.

Status -> (string)

Specifies whether Amazon S3 replicates objects created with server-side encryption using an Amazon Web Services KMS key stored in Amazon Web Services Key Management Service.

ReplicaModifications -> (structure)

A filter that you can specify for selections for modifications on replicas. Amazon S3 doesnât replicate replica modifications by default. In the latest version of replication configuration (when `Filter` is specified), you can specify this element and set the status to `Enabled` to replicate modifications on replicas.

### Note

If you donât specify the `Filter` element, Amazon S3 assumes that the replication configuration is the earlier version, V1. In the earlier version, this element is not allowed

Status -> (string)

Specifies whether Amazon S3 replicates modifications on replicas.

ExistingObjectReplication -> (structure)

Optional configuration to replicate existing source bucket objects.

### Note

This parameter is no longer supported. To replicate existing objects, see [Replicating existing objects with S3 Batch Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-batch.html) in the *Amazon S3 User Guide* .

Status -> (string)

Specifies whether Amazon S3 replicates existing source bucket objects.

Destination -> (structure)

A container for information about the replication destination and its configurations including enabling the S3 Replication Time Control (S3 RTC).

Bucket -> (string)

The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store the results.

Account -> (string)

Destination bucket owner account ID. In a cross-account scenario, if you direct Amazon S3 to change replica ownership to the Amazon Web Services account that owns the destination bucket by specifying the `AccessControlTranslation` property, this is the account ID of the destination bucket owner. For more information, see [Replication Additional Configuration: Changing the Replica Owner](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-change-owner.html) in the *Amazon S3 User Guide* .

StorageClass -> (string)

The storage class to use when replicating objects, such as S3 Standard or reduced redundancy. By default, Amazon S3 uses the storage class of the source object to create the object replica.

For valid values, see the `StorageClass` element of the [PUT Bucket replication](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html) action in the *Amazon S3 API Reference* .

AccessControlTranslation -> (structure)

Specify this only in a cross-account scenario (where source and destination bucket owners are not the same), and you want to change replica ownership to the Amazon Web Services account that owns the destination bucket. If this is not specified in the replication configuration, the replicas are owned by same Amazon Web Services account that owns the source object.

Owner -> (string)

Specifies the replica ownership. For default and valid values, see [PUT bucket replication](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html) in the *Amazon S3 API Reference* .

EncryptionConfiguration -> (structure)

A container that provides information about encryption. If `SourceSelectionCriteria` is specified, you must specify this element.

ReplicaKmsKeyID -> (string)

Specifies the ID (Key ARN or Alias ARN) of the customer managed Amazon Web Services KMS key stored in Amazon Web Services Key Management Service (KMS) for the destination bucket. Amazon S3 uses this key to encrypt replica objects. Amazon S3 only supports symmetric encryption KMS keys. For more information, see [Asymmetric keys in Amazon Web Services KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *Amazon Web Services Key Management Service Developer Guide* .

ReplicationTime -> (structure)

A container specifying S3 Replication Time Control (S3 RTC), including whether S3 RTC is enabled and the time when all objects and operations on objects must be replicated. Must be specified together with a `Metrics` block.

Status -> (string)

Specifies whether the replication time is enabled.

Time -> (structure)

A container specifying the time by which replication should be complete for all objects and operations on objects.

Minutes -> (integer)

Contains an integer specifying time in minutes.

Valid value: 15

Metrics -> (structure)

A container specifying replication metrics-related settings enabling replication metrics and events.

Status -> (string)

Specifies whether the replication metrics are enabled.

EventThreshold -> (structure)

A container specifying the time threshold for emitting the `s3:Replication:OperationMissedThreshold` event.

Minutes -> (integer)

Contains an integer specifying time in minutes.

Valid value: 15

DeleteMarkerReplication -> (structure)

Specifies whether Amazon S3 replicates delete markers. If you specify a `Filter` in your replication configuration, you must also include a `DeleteMarkerReplication` element. If your `Filter` includes a `Tag` element, the `DeleteMarkerReplication` `Status` must be set to Disabled, because Amazon S3 does not support replicating delete markers for tag-based rules. For an example configuration, see [Basic Rule Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-config-min-rule-config) .

For more information about delete marker replication, see [Basic Rule Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/delete-marker-replication.html) .

### Note

If you are using an earlier version of the replication configuration, Amazon S3 handles replication of delete markers differently. For more information, see [Backward Compatibility](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-backward-compat-considerations) .

Status -> (string)

Indicates whether to replicate delete markers.

### Note

Indicates whether to replicate delete markers.

JSON Syntax:

```
{
  "Role": "string",
  "Rules": [
    {
      "ID": "string",
      "Priority": integer,
      "Prefix": "string",
      "Filter": {
        "Prefix": "string",
        "Tag": {
          "Key": "string",
          "Value": "string"
        },
        "And": {
          "Prefix": "string",
          "Tags": [
            {
              "Key": "string",
              "Value": "string"
            }
            ...
          ]
        }
      },
      "Status": "Enabled"|"Disabled",
      "SourceSelectionCriteria": {
        "SseKmsEncryptedObjects": {
          "Status": "Enabled"|"Disabled"
        },
        "ReplicaModifications": {
          "Status": "Enabled"|"Disabled"
        }
      },
      "ExistingObjectReplication": {
        "Status": "Enabled"|"Disabled"
      },
      "Destination": {
        "Bucket": "string",
        "Account": "string",
        "StorageClass": "STANDARD"|"REDUCED_REDUNDANCY"|"STANDARD_IA"|"ONEZONE_IA"|"INTELLIGENT_TIERING"|"GLACIER"|"DEEP_ARCHIVE"|"OUTPOSTS"|"GLACIER_IR"|"SNOW"|"EXPRESS_ONEZONE",
        "AccessControlTranslation": {
          "Owner": "Destination"
        },
        "EncryptionConfiguration": {
          "ReplicaKmsKeyID": "string"
        },
        "ReplicationTime": {
          "Status": "Enabled"|"Disabled",
          "Time": {
            "Minutes": integer
          }
        },
        "Metrics": {
          "Status": "Enabled"|"Disabled",
          "EventThreshold": {
            "Minutes": integer
          }
        }
      },
      "DeleteMarkerReplication": {
        "Status": "Enabled"|"Disabled"
      }
    }
    ...
  ]
}
```

`--token` (string)

A token to allow Object Lock to be enabled for an existing bucket.

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

**To configure replication for an S3 bucket**

The following `put-bucket-replication` example applies a replication configuration to the specified S3 bucket.

```
aws s3api put-bucket-replication \
    --bucket amzn-s3-demo-bucket1 \
    --replication-configuration file://replication.json
```

Contents of `replication.json`:

```
{
    "Role": "arn:aws:iam::123456789012:role/s3-replication-role",
    "Rules": [
        {
            "Status": "Enabled",
            "Priority": 1,
            "DeleteMarkerReplication": { "Status": "Disabled" },
            "Filter" : { "Prefix": ""},
            "Destination": {
                "Bucket": "arn:aws:s3:::amzn-s3-demo-bucket2"
            }
        }
    ]
}
```

The destination bucket must have versioning enabled. The specified role must have permission to write to the destination bucket and have a trust relationship that allows Amazon S3 to assume the role.

Example role permission policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetReplicationConfiguration",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket1"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObjectVersion",
                "s3:GetObjectVersionAcl",
                "s3:GetObjectVersionTagging"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket1/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ReplicateObject",
                "s3:ReplicateDelete",
                "s3:ReplicateTags"
            ],
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket2/*"
        }
    ]
}
```

Example trust relationship policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "s3.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

This command produces no output.

For more information, see [This is the topic title](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/enable-replication.html) in the *Amazon Simple Storage Service Console User Guide*.

## Output

None