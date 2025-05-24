# create-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/index.html#cli-aws-s3control) ]

# create-job

## Description

This operation creates an S3 Batch Operations job.

You can use S3 Batch Operations to perform large-scale batch actions on Amazon S3 objects. Batch Operations can run a single action on lists of Amazon S3 objects that you specify. For more information, see [S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html) in the *Amazon S3 User Guide* .

Permissions

For information about permissions required to use the Batch Operations, see [Granting permissions for S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-iam-role-policies.html) in the *Amazon S3 User Guide* .

Related actions include:

- [DescribeJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html)
- [ListJobs](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html)
- [UpdateJobPriority](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html)
- [UpdateJobStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html)
- [JobOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobOperation.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/CreateJob)

## Synopsis

```
create-job
--account-id <value>
[--confirmation-required | --no-confirmation-required]
--operation <value>
--report <value>
[--client-request-token <value>]
[--manifest <value>]
[--description <value>]
--priority <value>
--role-arn <value>
[--tags <value>]
[--manifest-generator <value>]
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

The Amazon Web Services account ID that creates the job.

`--confirmation-required` | `--no-confirmation-required` (boolean)

Indicates whether confirmation is required before Amazon S3 runs the job. Confirmation is only required for jobs created through the Amazon S3 console.

`--operation` (structure)

The action that you want this job to perform on every object listed in the manifest. For more information about the available actions, see [Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-operations.html) in the *Amazon S3 User Guide* .

LambdaInvoke -> (structure)

Directs the specified job to invoke an Lambda function on every object in the manifest.

FunctionArn -> (string)

The Amazon Resource Name (ARN) for the Lambda function that the specified job will invoke on every object in the manifest.

InvocationSchemaVersion -> (string)

Specifies the schema version for the payload that Batch Operations sends when invoking an Lambda function. Version `1.0` is the default. Version `2.0` is required when you use Batch Operations to invoke Lambda functions that act on directory buckets, or if you need to specify `UserArguments` . For more information, see [Automate object processing in Amazon S3 directory buckets with S3 Batch Operations and Lambda](https://aws.amazon.com/blogs/storage/automate-object-processing-in-amazon-s3-directory-buckets-with-s3-batch-operations-and-aws-lambda/) in the *Amazon Web Services Storage Blog* .

### Warning

Ensure that your Lambda function code expects `InvocationSchemaVersion` **2.0** and uses bucket name rather than bucket ARN. If the `InvocationSchemaVersion` does not match what your Lambda function expects, your function might not work as expected.

### Note

**Directory buckets** - To initiate Amazon Web Services Lambda function to perform custom actions on objects in directory buckets, you must specify `2.0` .

UserArguments -> (map)

Key-value pairs that are passed in the payload that Batch Operations sends when invoking an Lambda function. You must specify `InvocationSchemaVersion` **2.0** for `LambdaInvoke` operations that include `UserArguments` . For more information, see [Automate object processing in Amazon S3 directory buckets with S3 Batch Operations and Lambda](https://aws.amazon.com/blogs/storage/automate-object-processing-in-amazon-s3-directory-buckets-with-s3-batch-operations-and-aws-lambda/) in the *Amazon Web Services Storage Blog* .

key -> (string)

value -> (string)

S3PutObjectCopy -> (structure)

Directs the specified job to run a PUT Copy object call on every object in the manifest.

TargetResource -> (string)

Specifies the destination bucket Amazon Resource Name (ARN) for the batch copy operation.

- **General purpose buckets** - For example, to copy objects to a general purpose bucket named `destinationBucket` , set the `TargetResource` property to `arn:aws:s3:::destinationBucket` .
- **Directory buckets** - For example, to copy objects to a directory bucket named `destinationBucket` in the Availability Zone identified by the AZ ID `usw2-az1` , set the `TargetResource` property to `arn:aws:s3express:*region* :*account_id* :/bucket/*destination_bucket_base_name* --*usw2-az1* --x-s3` . A directory bucket as a destination bucket can be in Availability Zone or Local Zone.

### Note

Copying objects across different Amazon Web Services Regions isnât supported when the source or destination bucket is in Amazon Web Services Local Zones. The source and destination buckets must have the same parent Amazon Web Services Region. Otherwise, you get an HTTP `400 Bad Request` error with the error code `InvalidRequest` .

CannedAccessControlList -> (string)

### Note

This functionality is not supported by directory buckets.

AccessControlGrants -> (list)

### Note

This functionality is not supported by directory buckets.

(structure)

Grantee -> (structure)

TypeIdentifier -> (string)

Identifier -> (string)

DisplayName -> (string)

Permission -> (string)

MetadataDirective -> (string)

ModifiedSinceConstraint -> (timestamp)

NewObjectMetadata -> (structure)

If you donât provide this parameter, Amazon S3 copies all the metadata from the original objects. If you specify an empty set, the new objects will have no tags. Otherwise, Amazon S3 assigns the supplied tags to the new objects.

CacheControl -> (string)

ContentDisposition -> (string)

ContentEncoding -> (string)

ContentLanguage -> (string)

UserMetadata -> (map)

key -> (string)

value -> (string)

ContentLength -> (long)

*This member has been deprecated.*

ContentMD5 -> (string)

*This member has been deprecated.*

ContentType -> (string)

HttpExpiresDate -> (timestamp)

RequesterCharged -> (boolean)

*This member has been deprecated.*

SSEAlgorithm -> (string)

The server-side encryption algorithm used when storing objects in Amazon S3.

**Directory buckets** - For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (`AES256` ) and server-side encryption with KMS keys (SSE-KMS) (`KMS` ). For more information, see [Protecting data with server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-serv-side-encryption.html) in the *Amazon S3 User Guide* . For [the Copy operation in Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops) , see [S3CopyObjectOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3CopyObjectOperation.html) .

NewObjectTagging -> (list)

Specifies a list of tags to add to the destination objects after they are copied. If `NewObjectTagging` is not specified, the tags of the source objects are copied to destination objects by default.

### Note

**Directory buckets** - Tags arenât supported by directory buckets. If your source objects have tags and your destination bucket is a directory bucket, specify an empty tag set in the `NewObjectTagging` field to prevent copying the source object tags to the directory bucket.

(structure)

A container for a key-value name pair.

Key -> (string)

Key of the tag

Value -> (string)

Value of the tag

RedirectLocation -> (string)

If the destination bucket is configured as a website, specifies an optional metadata property for website redirects, `x-amz-website-redirect-location` . Allows webpage redirects if the object copy is accessed through a website endpoint.

### Note

This functionality is not supported by directory buckets.

RequesterPays -> (boolean)

### Note

This functionality is not supported by directory buckets.

StorageClass -> (string)

Specify the storage class for the destination objects in a `Copy` operation.

### Note

**Directory buckets** - This functionality is not supported by directory buckets.

UnModifiedSinceConstraint -> (timestamp)

SSEAwsKmsKeyId -> (string)

Specifies the KMS key ID (Key ID, Key ARN, or Key Alias) to use for object encryption. If the KMS key doesnât exist in the same account thatâs issuing the command, you must use the full Key ARN not the Key ID.

### Note

**Directory buckets** - If you specify `SSEAlgorithm` with `KMS` , you must specify the `SSEAwsKmsKeyId` parameter with the ID (Key ID or Key ARN) of the KMS symmetric encryption customer managed key to use. Otherwise, you get an HTTP `400 Bad Request` error. The key alias format of the KMS key isnât supported. To encrypt new object copies in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucketâs default encryption configuration with a KMS key (specifically, a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) ). The [Amazon Web Services managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) (`aws/s3` ) isnât supported. Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) per directory bucket for the lifetime of the bucket. After you specify a customer managed key for SSE-KMS as the bucket default encryption, you canât override the customer managed key for the bucketâs SSE-KMS configuration. Then, when you specify server-side encryption settings for new object copies with SSE-KMS, you must make sure the encryption key is the same customer managed key that you specified for the directory bucketâs default encryption configuration.

TargetKeyPrefix -> (string)

Specifies the folder prefix that you want the objects to be copied into. For example, to copy objects into a folder named `Folder1` in the destination bucket, set the `TargetKeyPrefix` property to `Folder1` .

ObjectLockLegalHoldStatus -> (string)

The legal hold status to be applied to all objects in the Batch Operations job.

### Note

This functionality is not supported by directory buckets.

ObjectLockMode -> (string)

The retention mode to be applied to all objects in the Batch Operations job.

### Note

This functionality is not supported by directory buckets.

ObjectLockRetainUntilDate -> (timestamp)

The date when the applied object retention configuration expires on all objects in the Batch Operations job.

### Note

This functionality is not supported by directory buckets.

BucketKeyEnabled -> (boolean)

Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with server-side encryption using Amazon Web Services KMS (SSE-KMS). Setting this header to `true` causes Amazon S3 to use an S3 Bucket Key for object encryption with SSE-KMS.

Specifying this header with an *Copy* action doesnât affect *bucket-level* settings for S3 Bucket Key.

### Note

**Directory buckets** - S3 Bucket Keys arenât supported, when you copy SSE-KMS encrypted objects from general purpose buckets to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [the Copy operation in Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops) . In this case, Amazon S3 makes a call to KMS every time a copy request is made for a KMS-encrypted object.

ChecksumAlgorithm -> (string)

Indicates the algorithm that you want Amazon S3 to use to create the checksum. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide* .

S3PutObjectAcl -> (structure)

Directs the specified job to run a `PutObjectAcl` call on every object in the manifest.

### Note

This functionality is not supported by directory buckets.

AccessControlPolicy -> (structure)

AccessControlList -> (structure)

Owner -> (structure)

ID -> (string)

DisplayName -> (string)

Grants -> (list)

(structure)

Grantee -> (structure)

TypeIdentifier -> (string)

Identifier -> (string)

DisplayName -> (string)

Permission -> (string)

CannedAccessControlList -> (string)

S3PutObjectTagging -> (structure)

Directs the specified job to run a PUT Object tagging call on every object in the manifest.

### Note

This functionality is not supported by directory buckets.

TagSet -> (list)

(structure)

A container for a key-value name pair.

Key -> (string)

Key of the tag

Value -> (string)

Value of the tag

S3DeleteObjectTagging -> (structure)

Directs the specified job to execute a DELETE Object tagging call on every object in the manifest.

### Note

This functionality is not supported by directory buckets.

S3InitiateRestoreObject -> (structure)

Directs the specified job to initiate restore requests for every archived object in the manifest.

### Note

This functionality is not supported by directory buckets.

ExpirationInDays -> (integer)

This argument specifies how long the S3 Glacier or S3 Glacier Deep Archive object remains available in Amazon S3. S3 Initiate Restore Object jobs that target S3 Glacier and S3 Glacier Deep Archive objects require `ExpirationInDays` set to 1 or greater.

Conversely, do *not* set `ExpirationInDays` when creating S3 Initiate Restore Object jobs that target S3 Intelligent-Tiering Archive Access and Deep Archive Access tier objects. Objects in S3 Intelligent-Tiering archive access tiers are not subject to restore expiry, so specifying `ExpirationInDays` results in restore request failure.

S3 Batch Operations jobs can operate either on S3 Glacier and S3 Glacier Deep Archive storage class objects or on S3 Intelligent-Tiering Archive Access and Deep Archive Access storage tier objects, but not both types in the same job. If you need to restore objects of both types you *must* create separate Batch Operations jobs.

GlacierJobTier -> (string)

S3 Batch Operations supports `STANDARD` and `BULK` retrieval tiers, but not the `EXPEDITED` retrieval tier.

S3PutObjectLegalHold -> (structure)

Contains the configuration for an S3 Object Lock legal hold operation that an S3 Batch Operations job passes to every object to the underlying `PutObjectLegalHold` API operation. For more information, see [Using S3 Object Lock legal hold with S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-legal-hold.html) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported by directory buckets.

LegalHold -> (structure)

Contains the Object Lock legal hold status to be applied to all objects in the Batch Operations job.

Status -> (string)

The Object Lock legal hold status to be applied to all objects in the Batch Operations job.

S3PutObjectRetention -> (structure)

Contains the configuration parameters for the Object Lock retention action for an S3 Batch Operations job. Batch Operations passes every object to the underlying `PutObjectRetention` API operation. For more information, see [Using S3 Object Lock retention with S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-retention-date.html) in the *Amazon S3 User Guide* .

### Note

This functionality is not supported by directory buckets.

BypassGovernanceRetention -> (boolean)

Indicates if the action should be applied to objects in the Batch Operations job even if they have Object Lock `GOVERNANCE` type in place.

Retention -> (structure)

Contains the Object Lock retention mode to be applied to all objects in the Batch Operations job. For more information, see [Using S3 Object Lock retention with S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-retention-date.html) in the *Amazon S3 User Guide* .

RetainUntilDate -> (timestamp)

The date when the applied Object Lock retention will expire on all objects set by the Batch Operations job.

Mode -> (string)

The Object Lock retention mode to be applied to all objects in the Batch Operations job.

S3ReplicateObject -> (structure)

Directs the specified job to invoke `ReplicateObject` on every object in the jobâs manifest.

### Note

This functionality is not supported by directory buckets.

JSON Syntax:

```
{
  "LambdaInvoke": {
    "FunctionArn": "string",
    "InvocationSchemaVersion": "string",
    "UserArguments": {"string": "string"
      ...}
  },
  "S3PutObjectCopy": {
    "TargetResource": "string",
    "CannedAccessControlList": "private"|"public-read"|"public-read-write"|"aws-exec-read"|"authenticated-read"|"bucket-owner-read"|"bucket-owner-full-control",
    "AccessControlGrants": [
      {
        "Grantee": {
          "TypeIdentifier": "id"|"emailAddress"|"uri",
          "Identifier": "string",
          "DisplayName": "string"
        },
        "Permission": "FULL_CONTROL"|"READ"|"WRITE"|"READ_ACP"|"WRITE_ACP"
      }
      ...
    ],
    "MetadataDirective": "COPY"|"REPLACE",
    "ModifiedSinceConstraint": timestamp,
    "NewObjectMetadata": {
      "CacheControl": "string",
      "ContentDisposition": "string",
      "ContentEncoding": "string",
      "ContentLanguage": "string",
      "UserMetadata": {"string": "string"
        ...},
      "ContentLength": long,
      "ContentMD5": "string",
      "ContentType": "string",
      "HttpExpiresDate": timestamp,
      "RequesterCharged": true|false,
      "SSEAlgorithm": "AES256"|"KMS"
    },
    "NewObjectTagging": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ],
    "RedirectLocation": "string",
    "RequesterPays": true|false,
    "StorageClass": "STANDARD"|"STANDARD_IA"|"ONEZONE_IA"|"GLACIER"|"INTELLIGENT_TIERING"|"DEEP_ARCHIVE"|"GLACIER_IR",
    "UnModifiedSinceConstraint": timestamp,
    "SSEAwsKmsKeyId": "string",
    "TargetKeyPrefix": "string",
    "ObjectLockLegalHoldStatus": "OFF"|"ON",
    "ObjectLockMode": "COMPLIANCE"|"GOVERNANCE",
    "ObjectLockRetainUntilDate": timestamp,
    "BucketKeyEnabled": true|false,
    "ChecksumAlgorithm": "CRC32"|"CRC32C"|"SHA1"|"SHA256"|"CRC64NVME"
  },
  "S3PutObjectAcl": {
    "AccessControlPolicy": {
      "AccessControlList": {
        "Owner": {
          "ID": "string",
          "DisplayName": "string"
        },
        "Grants": [
          {
            "Grantee": {
              "TypeIdentifier": "id"|"emailAddress"|"uri",
              "Identifier": "string",
              "DisplayName": "string"
            },
            "Permission": "FULL_CONTROL"|"READ"|"WRITE"|"READ_ACP"|"WRITE_ACP"
          }
          ...
        ]
      },
      "CannedAccessControlList": "private"|"public-read"|"public-read-write"|"aws-exec-read"|"authenticated-read"|"bucket-owner-read"|"bucket-owner-full-control"
    }
  },
  "S3PutObjectTagging": {
    "TagSet": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ]
  },
  "S3DeleteObjectTagging": {

  },
  "S3InitiateRestoreObject": {
    "ExpirationInDays": integer,
    "GlacierJobTier": "BULK"|"STANDARD"
  },
  "S3PutObjectLegalHold": {
    "LegalHold": {
      "Status": "OFF"|"ON"
    }
  },
  "S3PutObjectRetention": {
    "BypassGovernanceRetention": true|false,
    "Retention": {
      "RetainUntilDate": timestamp,
      "Mode": "COMPLIANCE"|"GOVERNANCE"
    }
  },
  "S3ReplicateObject": {

  }
}
```

`--report` (structure)

Configuration parameters for the optional job-completion report.

Bucket -> (string)

The Amazon Resource Name (ARN) for the bucket where specified job-completion report will be stored.

### Note

**Directory buckets** - Directory buckets arenât supported as a location for Batch Operations to store job completion reports.

Format -> (string)

The format of the specified job-completion report.

Enabled -> (boolean)

Indicates whether the specified job will generate a job-completion report.

Prefix -> (string)

An optional prefix to describe where in the specified bucket the job-completion report will be stored. Amazon S3 stores the job-completion report at `<prefix>/job-<job-id>/report.json` .

ReportScope -> (string)

Indicates whether the job-completion report will include details of all tasks or only failed tasks.

Shorthand Syntax:

```
Bucket=string,Format=string,Enabled=boolean,Prefix=string,ReportScope=string
```

JSON Syntax:

```
{
  "Bucket": "string",
  "Format": "Report_CSV_20180820",
  "Enabled": true|false,
  "Prefix": "string",
  "ReportScope": "AllTasks"|"FailedTasksOnly"
}
```

`--client-request-token` (string)

An idempotency token to ensure that you donât accidentally submit the same request twice. You can use any string up to the maximum length.

`--manifest` (structure)

Configuration parameters for the manifest.

Spec -> (structure)

Describes the format of the specified jobâs manifest. If the manifest is in CSV format, also describes the columns contained within the manifest.

Format -> (string)

Indicates which of the available formats the specified manifest uses.

Fields -> (list)

If the specified manifest object is in the `S3BatchOperations_CSV_20180820` format, this element describes which columns contain the required data.

(string)

Location -> (structure)

Contains the information required to locate the specified jobâs manifest. Manifests canât be imported from directory buckets. For more information, see [Directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) .

ObjectArn -> (string)

The Amazon Resource Name (ARN) for a manifest object.

### Warning

When youâre using XML requests, you must replace special characters (such as carriage returns) in object keys with their equivalent XML entity codes. For more information, see [XML-related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints) in the *Amazon S3 User Guide* .

ObjectVersionId -> (string)

The optional version ID to identify a specific version of the manifest object.

ETag -> (string)

The ETag for the specified manifest object.

Shorthand Syntax:

```
Spec={Format=string,Fields=[string,string]},Location={ObjectArn=string,ObjectVersionId=string,ETag=string}
```

JSON Syntax:

```
{
  "Spec": {
    "Format": "S3BatchOperations_CSV_20180820"|"S3InventoryReport_CSV_20161130",
    "Fields": ["Ignore"|"Bucket"|"Key"|"VersionId", ...]
  },
  "Location": {
    "ObjectArn": "string",
    "ObjectVersionId": "string",
    "ETag": "string"
  }
}
```

`--description` (string)

A description for this job. You can use any string within the permitted length. Descriptions donât need to be unique and can be used for multiple jobs.

`--priority` (integer)

The numerical priority for this job. Higher numbers indicate higher priority.

`--role-arn` (string)

The Amazon Resource Name (ARN) for the Identity and Access Management (IAM) role that Batch Operations will use to run this jobâs action on every object in the manifest.

`--tags` (list)

A set of tags to associate with the S3 Batch Operations job. This is an optional parameter.

(structure)

A container for a key-value name pair.

Key -> (string)

Key of the tag

Value -> (string)

Value of the tag

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--manifest-generator` (tagged union structure)

The attribute container for the ManifestGenerator details. Jobs must be created with either a manifest file or a ManifestGenerator, but not both.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `S3JobManifestGenerator`.

S3JobManifestGenerator -> (structure)

The S3 job ManifestGeneratorâs configuration details.

ExpectedBucketOwner -> (string)

The Amazon Web Services account ID that owns the bucket the generated manifest is written to. If provided the generated manifest bucketâs owner Amazon Web Services account ID must match this value, else the job fails.

SourceBucket -> (string)

The ARN of the source bucket used by the ManifestGenerator.

### Note

**Directory buckets** - Directory buckets arenât supported as the source buckets used by `S3JobManifestGenerator` to generate the job manifest.

ManifestOutputLocation -> (structure)

Specifies the location the generated manifest will be written to. Manifests canât be written to directory buckets. For more information, see [Directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) .

ExpectedManifestBucketOwner -> (string)

The Account ID that owns the bucket the generated manifest is written to.

Bucket -> (string)

The bucket ARN the generated manifest should be written to.

### Note

**Directory buckets** - Directory buckets arenât supported as the buckets to store the generated manifest.

ManifestPrefix -> (string)

Prefix identifying one or more objects to which the manifest applies.

ManifestEncryption -> (structure)

Specifies what encryption should be used when the generated manifest objects are written.

SSES3 -> (structure)

Specifies the use of SSE-S3 to encrypt generated manifest objects.

SSEKMS -> (structure)

Configuration details on how SSE-KMS is used to encrypt generated manifest objects.

KeyId -> (string)

Specifies the ID of the Amazon Web Services Key Management Service (Amazon Web Services KMS) symmetric encryption customer managed key to use for encrypting generated manifest objects.

ManifestFormat -> (string)

The format of the generated manifest.

Filter -> (structure)

Specifies rules the S3JobManifestGenerator should use to decide whether an object in the source bucket should or should not be included in the generated job manifest.

EligibleForReplication -> (boolean)

Include objects in the generated manifest only if they are eligible for replication according to the Replication configuration on the source bucket.

CreatedAfter -> (timestamp)

If provided, the generated manifest includes only source bucket objects that were created after this time.

CreatedBefore -> (timestamp)

If provided, the generated manifest includes only source bucket objects that were created before this time.

ObjectReplicationStatuses -> (list)

If provided, the generated manifest includes only source bucket objects that have one of the specified Replication statuses.

(string)

KeyNameConstraint -> (structure)

If provided, the generated manifest includes only source bucket objects whose object keys match the string constraints specified for `MatchAnyPrefix` , `MatchAnySuffix` , and `MatchAnySubstring` .

MatchAnyPrefix -> (list)

If provided, the generated manifest includes objects where the specified string appears at the start of the object key string. Each KeyNameConstraint filter accepts an array of strings with a length of 1 string.

(string)

MatchAnySuffix -> (list)

If provided, the generated manifest includes objects where the specified string appears at the end of the object key string. Each KeyNameConstraint filter accepts an array of strings with a length of 1 string.

(string)

MatchAnySubstring -> (list)

If provided, the generated manifest includes objects where the specified string appears anywhere within the object key string. Each KeyNameConstraint filter accepts an array of strings with a length of 1 string.

(string)

ObjectSizeGreaterThanBytes -> (long)

If provided, the generated manifest includes only source bucket objects whose file size is greater than the specified number of bytes.

ObjectSizeLessThanBytes -> (long)

If provided, the generated manifest includes only source bucket objects whose file size is less than the specified number of bytes.

MatchAnyStorageClass -> (list)

If provided, the generated manifest includes only source bucket objects that are stored with the specified storage class.

(string)

EnableManifestOutput -> (boolean)

Determines whether or not to write the jobâs generated manifest to a bucket.

JSON Syntax:

```
{
  "S3JobManifestGenerator": {
    "ExpectedBucketOwner": "string",
    "SourceBucket": "string",
    "ManifestOutputLocation": {
      "ExpectedManifestBucketOwner": "string",
      "Bucket": "string",
      "ManifestPrefix": "string",
      "ManifestEncryption": {
        "SSES3": {

        },
        "SSEKMS": {
          "KeyId": "string"
        }
      },
      "ManifestFormat": "S3InventoryReport_CSV_20211130"
    },
    "Filter": {
      "EligibleForReplication": true|false,
      "CreatedAfter": timestamp,
      "CreatedBefore": timestamp,
      "ObjectReplicationStatuses": ["COMPLETED"|"FAILED"|"REPLICA"|"NONE", ...],
      "KeyNameConstraint": {
        "MatchAnyPrefix": ["string", ...],
        "MatchAnySuffix": ["string", ...],
        "MatchAnySubstring": ["string", ...]
      },
      "ObjectSizeGreaterThanBytes": long,
      "ObjectSizeLessThanBytes": long,
      "MatchAnyStorageClass": ["STANDARD"|"STANDARD_IA"|"ONEZONE_IA"|"GLACIER"|"INTELLIGENT_TIERING"|"DEEP_ARCHIVE"|"GLACIER_IR", ...]
    },
    "EnableManifestOutput": true|false
  }
}
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

**To create an Amazon S3 batch operations job**

The following `create-job` example creates an Amazon S3 batch operations job to tag objects as `confidential` in the bucket ``employee-records`.

```
aws s3control create-job \
    --account-id 123456789012 \
    --operation '{"S3PutObjectTagging": { "TagSet": [{"Key":"confidential", "Value":"true"}] }}' \
    --report '{"Bucket":"arn:aws:s3:::employee-records-logs","Prefix":"batch-op-create-job", "Format":"Report_CSV_20180820","Enabled":true,"ReportScope":"AllTasks"}' \
    --manifest '{"Spec":{"Format":"S3BatchOperations_CSV_20180820","Fields":["Bucket","Key"]},"Location":{"ObjectArn":"arn:aws:s3:::employee-records-logs/inv-report/7a6a9be4-072c-407e-85a2-ec3e982f773e.csv","ETag":"69f52a4e9f797e987155d9c8f5880897"}}' \
    --priority 42 \
    --role-arn arn:aws:iam::123456789012:role/S3BatchJobRole
```

Output:

```
{
    "JobId": "93735294-df46-44d5-8638-6356f335324e"
}
```

## Output

JobId -> (string)

The ID for this job. Amazon S3 generates this ID automatically and returns it after a successful `Create Job` request.