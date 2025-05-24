# describe-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/describe-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/describe-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/index.html#cli-aws-s3control) ]

# describe-job

## Description

Retrieves the configuration parameters and status for a Batch Operations job. For more information, see [S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html) in the *Amazon S3 User Guide* .

Permissions

To use the `DescribeJob` operation, you must have permission to perform the `s3:DescribeJob` action.

Related actions include:

- [CreateJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html)
- [ListJobs](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html)
- [UpdateJobPriority](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html)
- [UpdateJobStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/DescribeJob)

## Synopsis

```
describe-job
--account-id <value>
--job-id <value>
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

The Amazon Web Services account ID associated with the S3 Batch Operations job.

`--job-id` (string)

The ID for the job whose information you want to retrieve.

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

**To describe an Amazon S3 batch operations job**

The following `describe-job` provides configuration parameters and status for the specified batch operations job.

```
aws s3control describe-job \
    --account-id 123456789012 \
    --job-id 93735294-df46-44d5-8638-6356f335324e
```

Output:

```
{
    "Job": {
        "TerminationDate": "2019-10-03T21:49:53.944Z",
        "JobId": "93735294-df46-44d5-8638-6356f335324e",
        "FailureReasons": [],
        "Manifest": {
            "Spec": {
                "Fields": [
                    "Bucket",
                    "Key"
                ],
                "Format": "S3BatchOperations_CSV_20180820"
            },
            "Location": {
                "ETag": "69f52a4e9f797e987155d9c8f5880897",
                "ObjectArn": "arn:aws:s3:::employee-records-logs/inv-report/7a6a9be4-072c-407e-85a2-ec3e982f773e.csv"
            }
        },
        "Operation": {
            "S3PutObjectTagging": {
                "TagSet": [
                    {
                        "Value": "true",
                        "Key": "confidential"
                    }
                ]
            }
        },
        "RoleArn": "arn:aws:iam::123456789012:role/S3BatchJobRole",
        "ProgressSummary": {
            "TotalNumberOfTasks": 8,
            "NumberOfTasksFailed": 0,
            "NumberOfTasksSucceeded": 8
        },
        "Priority": 42,
        "Report": {
            "ReportScope": "AllTasks",
            "Format": "Report_CSV_20180820",
            "Enabled": true,
            "Prefix": "batch-op-create-job",
            "Bucket": "arn:aws:s3:::employee-records-logs"
        },
        "JobArn": "arn:aws:s3:us-west-2:123456789012:job/93735294-df46-44d5-8638-6356f335324e",
        "CreationTime": "2019-10-03T21:48:48.048Z",
        "Status": "Complete"
    }
}
```

## Output

Job -> (structure)

Contains the configuration parameters and status for the job specified in the `Describe Job` request.

JobId -> (string)

The ID for the specified job.

ConfirmationRequired -> (boolean)

Indicates whether confirmation is required before Amazon S3 begins running the specified job. Confirmation is required only for jobs created through the Amazon S3 console.

Description -> (string)

The description for this job, if one was provided in this jobâs `Create Job` request.

JobArn -> (string)

The Amazon Resource Name (ARN) for this job.

Status -> (string)

The current status of the specified job.

Manifest -> (structure)

The configuration information for the specified jobâs manifest object.

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

Operation -> (structure)

The operation that the specified job is configured to run on the objects listed in the manifest.

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

Priority -> (integer)

The priority of the specified job.

ProgressSummary -> (structure)

Describes the total number of tasks that the specified job has run, the number of tasks that succeeded, and the number of tasks that failed.

TotalNumberOfTasks -> (long)

NumberOfTasksSucceeded -> (long)

NumberOfTasksFailed -> (long)

Timers -> (structure)

The JobTimers attribute of a jobâs progress summary.

ElapsedTimeInActiveSeconds -> (long)

Indicates the elapsed time in seconds the job has been in the Active job state.

StatusUpdateReason -> (string)

The reason for updating the job.

FailureReasons -> (list)

If the specified job failed, this field contains information describing the failure.

(structure)

If this job failed, this element indicates why the job failed.

FailureCode -> (string)

The failure code, if any, for the specified job.

FailureReason -> (string)

The failure reason, if any, for the specified job.

Report -> (structure)

Contains the configuration information for the job-completion report if you requested one in the `Create Job` request.

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

CreationTime -> (timestamp)

A timestamp indicating when this job was created.

TerminationDate -> (timestamp)

A timestamp indicating when this job terminated. A jobâs termination date is the date and time when it succeeded, failed, or was canceled.

RoleArn -> (string)

The Amazon Resource Name (ARN) for the Identity and Access Management (IAM) role assigned to run the tasks for this job.

SuspendedDate -> (timestamp)

The timestamp when this job was suspended, if it has been suspended.

SuspendedCause -> (string)

The reason why the specified job was suspended. A job is only suspended if you create it through the Amazon S3 console. When you create the job, it enters the `Suspended` state to await confirmation before running. After you confirm the job, it automatically exits the `Suspended` state.

ManifestGenerator -> (tagged union structure)

The manifest generator that was used to generate a job manifest for this job.

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

GeneratedManifestDescriptor -> (structure)

The attribute of the JobDescriptor containing details about the jobâs generated manifest.

Format -> (string)

The format of the generated manifest.

Location -> (structure)

Contains the information required to locate a manifest object. Manifests canât be imported from directory buckets. For more information, see [Directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) .

ObjectArn -> (string)

The Amazon Resource Name (ARN) for a manifest object.

### Warning

When youâre using XML requests, you must replace special characters (such as carriage returns) in object keys with their equivalent XML entity codes. For more information, see [XML-related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints) in the *Amazon S3 User Guide* .

ObjectVersionId -> (string)

The optional version ID to identify a specific version of the manifest object.

ETag -> (string)

The ETag for the specified manifest object.