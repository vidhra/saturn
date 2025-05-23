# describe-bucketsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/describe-buckets.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/describe-buckets.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [macie2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/index.html#cli-aws-macie2) ]

# describe-buckets

## Description

Retrieves (queries) statistical data and other information about one or more S3 buckets that Amazon Macie monitors and analyzes for an account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/macie2-2020-01-01/DescribeBuckets)

`describe-buckets` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `buckets`

## Synopsis

```
describe-buckets
[--criteria <value>]
[--sort-criteria <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--criteria` (map)

The criteria to use to filter the query results.

key -> (string)

value -> (structure)

Specifies the operator to use in a property-based condition that filters the results of a query for information about S3 buckets.

eq -> (list)

The value for the property matches (equals) the specified value. If you specify multiple values, Amazon Macie uses OR logic to join the values.

(string)

gt -> (long)

The value for the property is greater than the specified value.

gte -> (long)

The value for the property is greater than or equal to the specified value.

lt -> (long)

The value for the property is less than the specified value.

lte -> (long)

The value for the property is less than or equal to the specified value.

neq -> (list)

The value for the property doesnât match (doesnât equal) the specified value. If you specify multiple values, Amazon Macie uses OR logic to join the values.

(string)

prefix -> (string)

The name of the bucket begins with the specified value.

Shorthand Syntax:

```
KeyName1=eq=string,string,gt=long,gte=long,lt=long,lte=long,neq=string,string,prefix=string,KeyName2=eq=string,string,gt=long,gte=long,lt=long,lte=long,neq=string,string,prefix=string
```

JSON Syntax:

```
{"string": {
      "eq": ["string", ...],
      "gt": long,
      "gte": long,
      "lt": long,
      "lte": long,
      "neq": ["string", ...],
      "prefix": "string"
    }
  ...}
```

`--sort-criteria` (structure)

The criteria to use to sort the query results.

attributeName -> (string)

The name of the bucket property to sort the results by. This value can be one of the following properties that Amazon Macie defines as bucket metadata: accountId, bucketName, classifiableObjectCount, classifiableSizeInBytes, objectCount, sensitivityScore, or sizeInBytes.

orderBy -> (string)

The sort order to apply to the results, based on the value specified by the attributeName property. Valid values are: ASC, sort the results in ascending order; and, DESC, sort the results in descending order.

Shorthand Syntax:

```
attributeName=string,orderBy=string
```

JSON Syntax:

```
{
  "attributeName": "string",
  "orderBy": "ASC"|"DESC"
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To query data about one or more S3 buckets that Amazon Macie monitors and analyzes for your account**

The following `describe-buckets` example queries metadata for all S3 buckets whose names begin with amzn-s3-demo-bucket and are in the current AWS Region.

```
aws macie2 describe-buckets \
    --criteria '{"bucketName":{"prefix":"amzn-s3-demo-bucket"}}'
```

Output:

```
{
    "buckets": [
        {
            "accountId": "123456789012",
            "allowsUnencryptedObjectUploads": "FALSE",
            "automatedDiscoveryMonitoringStatus": "MONITORED",
            "bucketArn": "arn:aws:s3:::amzn-s3-demo-bucket1",
            "bucketCreatedAt": "2020-05-18T19:54:00+00:00",
            "bucketName": "amzn-s3-demo-bucket1",
            "classifiableObjectCount": 13,
            "classifiableSizeInBytes": 1592088,
            "jobDetails": {
                "isDefinedInJob": "TRUE",
                "isMonitoredByJob": "TRUE",
                "lastJobId": "08c81dc4a2f3377fae45c9ddaEXAMPLE",
                "lastJobRunTime": "2024-08-19T14:55:30.270000+00:00"
            },
            "lastAutomatedDiscoveryTime": "2024-10-22T19:11:25.364000+00:00",
            "lastUpdated": "2024-10-25T07:33:06.337000+00:00",
            "objectCount": 13,
            "objectCountByEncryptionType": {
                "customerManaged": 0,
                "kmsManaged": 2,
                "s3Managed": 7,
                "unencrypted": 4,
                "unknown": 0
            },
            "publicAccess": {
                "effectivePermission": "NOT_PUBLIC",
                "permissionConfiguration": {
                    "accountLevelPermissions": {
                        "blockPublicAccess": {
                            "blockPublicAcls": true,
                            "blockPublicPolicy": true,
                            "ignorePublicAcls": true,
                            "restrictPublicBuckets": true
                        }
                    },
                    "bucketLevelPermissions": {
                        "accessControlList": {
                            "allowsPublicReadAccess": false,
                            "allowsPublicWriteAccess": false
                        },
                        "blockPublicAccess": {
                            "blockPublicAcls": true,
                            "blockPublicPolicy": true,
                            "ignorePublicAcls": true,
                            "restrictPublicBuckets": true
                        },
                        "bucketPolicy": {
                            "allowsPublicReadAccess": false,
                            "allowsPublicWriteAccess": false
                        }
                    }
                }
            },
            "region": "us-west-2",
            "replicationDetails": {
                "replicated": false,
                "replicatedExternally": false,
                "replicationAccounts": []
            },
            "sensitivityScore": 78,
            "serverSideEncryption": {
                "kmsMasterKeyId": null,
                "type": "NONE"
            },
            "sharedAccess": "NOT_SHARED",
            "sizeInBytes": 4549746,
            "sizeInBytesCompressed": 0,
            "tags": [
                {
                    "key": "Division",
                    "value": "HR"
                },
                {
                    "key": "Team",
                    "value": "Recruiting"
                }
            ],
            "unclassifiableObjectCount": {
                "fileType": 0,
                "storageClass": 0,
                "total": 0
            },
            "unclassifiableObjectSizeInBytes": {
                "fileType": 0,
                "storageClass": 0,
                "total": 0
            },
            "versioning": true
        },
        {
            "accountId": "123456789012",
            "allowsUnencryptedObjectUploads": "TRUE",
            "automatedDiscoveryMonitoringStatus": "MONITORED",
            "bucketArn": "arn:aws:s3:::amzn-s3-demo-bucket2",
            "bucketCreatedAt": "2020-11-25T18:24:38+00:00",
            "bucketName": "amzn-s3-demo-bucket2",
            "classifiableObjectCount": 8,
            "classifiableSizeInBytes": 133810,
            "jobDetails": {
                "isDefinedInJob": "TRUE",
                "isMonitoredByJob": "FALSE",
                "lastJobId": "188d4f6044d621771ef7d65f2EXAMPLE",
                "lastJobRunTime": "2024-07-09T19:37:11.511000+00:00"
            },
            "lastAutomatedDiscoveryTime": "2024-10-24T19:11:25.364000+00:00",
            "lastUpdated": "2024-10-25T07:33:06.337000+00:00",
            "objectCount": 8,
            "objectCountByEncryptionType": {
                "customerManaged": 0,
                "kmsManaged": 0,
                "s3Managed": 8,
                "unencrypted": 0,
                "unknown": 0
            },
            "publicAccess": {
                "effectivePermission": "NOT_PUBLIC",
                "permissionConfiguration": {
                    "accountLevelPermissions": {
                        "blockPublicAccess": {
                            "blockPublicAcls": true,
                            "blockPublicPolicy": true,
                            "ignorePublicAcls": true,
                            "restrictPublicBuckets": true
                        }
                    },
                    "bucketLevelPermissions": {
                        "accessControlList": {
                            "allowsPublicReadAccess": false,
                            "allowsPublicWriteAccess": false
                        },
                        "blockPublicAccess": {
                            "blockPublicAcls": true,
                            "blockPublicPolicy": true,
                            "ignorePublicAcls": true,
                            "restrictPublicBuckets": true
                        },
                        "bucketPolicy": {
                            "allowsPublicReadAccess": false,
                            "allowsPublicWriteAccess": false
                        }
                    }
                }
            },
            "region": "us-west-2",
            "replicationDetails": {
                "replicated": false,
                "replicatedExternally": false,
                "replicationAccounts": []
            },
            "sensitivityScore": 95,
            "serverSideEncryption": {
                "kmsMasterKeyId": null,
                "type": "AES256"
            },
            "sharedAccess": "EXTERNAL",
            "sizeInBytes": 175978,
            "sizeInBytesCompressed": 0,
            "tags": [
                {
                    "key": "Division",
                    "value": "HR"
                },
                {
                    "key": "Team",
                    "value": "Recruiting"
                }
            ],
            "unclassifiableObjectCount": {
                "fileType": 3,
                "storageClass": 0,
                "total": 3
            },
            "unclassifiableObjectSizeInBytes": {
                "fileType": 2999826,
                "storageClass": 0,
                "total": 2999826
            },
            "versioning": true
        }
    ]
}
```

For more information, see [Filtering your S3 bucket inventory](https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-inventory-filter.html) in the *Amazon Macie User Guide*.

## Output

buckets -> (list)

An array of objects, one for each bucket that matches the filter criteria specified in the request.

(structure)

Provides statistical data and other information about an S3 bucket that Amazon Macie monitors and analyzes for your account. By default, object count and storage size values include data for object parts that are the result of incomplete multipart uploads. For more information, see [How Macie monitors Amazon S3 data security](https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-how-it-works.html) in the *Amazon Macie User Guide* .

If an error or issue prevents Macie from retrieving and processing metadata from Amazon S3 for the bucket or the bucketâs objects, the value for the versioning property is false and the value for most other properties is null or UNKNOWN. Key exceptions are accountId, bucketArn, bucketCreatedAt, bucketName, lastUpdated, and region. To identify the cause, refer to the errorCode and errorMessage values.

accountId -> (string)

The unique identifier for the Amazon Web Services account that owns the bucket.

allowsUnencryptedObjectUploads -> (string)

Specifies whether the bucket policy for the bucket requires server-side encryption of objects when objects are added to the bucket. Possible values are:

- FALSE - The bucket policy requires server-side encryption of new objects. PutObject requests must include a valid server-side encryption header.
- TRUE - The bucket doesnât have a bucket policy or it has a bucket policy that doesnât require server-side encryption of new objects. If a bucket policy exists, it doesnât require PutObject requests to include a valid server-side encryption header.
- UNKNOWN - Amazon Macie canât determine whether the bucket policy requires server-side encryption of new objects.

Valid server-side encryption headers are: x-amz-server-side-encryption with a value of AES256 or aws:kms, and x-amz-server-side-encryption-customer-algorithm with a value of AES256.

automatedDiscoveryMonitoringStatus -> (string)

Specifies whether automated sensitive data discovery is currently configured to analyze objects in the bucket. Possible values are: MONITORED, the bucket is included in analyses; and, NOT_MONITORED, the bucket is excluded from analyses. If automated sensitive data discovery is disabled for your account, this value is NOT_MONITORED.

bucketArn -> (string)

The Amazon Resource Name (ARN) of the bucket.

bucketCreatedAt -> (timestamp)

The date and time, in UTC and extended ISO 8601 format, when the bucket was created. This value can also indicate when changes such as edits to the bucketâs policy were most recently made to the bucket.

bucketName -> (string)

The name of the bucket.

classifiableObjectCount -> (long)

The total number of objects that Amazon Macie can analyze in the bucket. These objects use a supported storage class and have a file name extension for a supported file or storage format.

classifiableSizeInBytes -> (long)

The total storage size, in bytes, of the objects that Amazon Macie can analyze in the bucket. These objects use a supported storage class and have a file name extension for a supported file or storage format.

If versioning is enabled for the bucket, Macie calculates this value based on the size of the latest version of each applicable object in the bucket. This value doesnât reflect the storage size of all versions of each applicable object in the bucket.

errorCode -> (string)

The code for an error or issue that prevented Amazon Macie from retrieving and processing information about the bucket and the bucketâs objects. Possible values are:

- ACCESS_DENIED - Macie doesnât have permission to retrieve the information. For example, the bucket has a restrictive bucket policy and Amazon S3 denied the request.
- BUCKET_COUNT_EXCEEDS_QUOTA - Retrieving and processing the information would exceed the quota for the number of buckets that Macie monitors for an account (10,000).

If this value is null, Macie was able to retrieve and process the information.

errorMessage -> (string)

A brief description of the error or issue (errorCode) that prevented Amazon Macie from retrieving and processing information about the bucket and the bucketâs objects. This value is null if Macie was able to retrieve and process the information.

jobDetails -> (structure)

Specifies whether any one-time or recurring classification jobs are configured to analyze objects in the bucket, and, if so, the details of the job that ran most recently.

isDefinedInJob -> (string)

Specifies whether any one-time or recurring jobs are configured to analyze objects in the bucket. Possible values are:

- TRUE - The bucket is explicitly included in the bucket definition (S3BucketDefinitionForJob) for one or more jobs and at least one of those jobs has a status other than CANCELLED. Or the bucket matched the bucket criteria (S3BucketCriteriaForJob) for at least one job that previously ran.
- FALSE - The bucket isnât explicitly included in the bucket definition (S3BucketDefinitionForJob) for any jobs, all the jobs that explicitly include the bucket in their bucket definitions have a status of CANCELLED, or the bucket didnât match the bucket criteria (S3BucketCriteriaForJob) for any jobs that previously ran.
- UNKNOWN - An exception occurred when Amazon Macie attempted to retrieve job data for the bucket.

isMonitoredByJob -> (string)

Specifies whether any recurring jobs are configured to analyze objects in the bucket. Possible values are:

- TRUE - The bucket is explicitly included in the bucket definition (S3BucketDefinitionForJob) for one or more recurring jobs or the bucket matches the bucket criteria (S3BucketCriteriaForJob) for one or more recurring jobs. At least one of those jobs has a status other than CANCELLED.
- FALSE - The bucket isnât explicitly included in the bucket definition (S3BucketDefinitionForJob) for any recurring jobs, the bucket doesnât match the bucket criteria (S3BucketCriteriaForJob) for any recurring jobs, or all the recurring jobs that are configured to analyze data in the bucket have a status of CANCELLED.
- UNKNOWN - An exception occurred when Amazon Macie attempted to retrieve job data for the bucket.

lastJobId -> (string)

The unique identifier for the job that ran most recently and is configured to analyze objects in the bucket, either the latest run of a recurring job or the only run of a one-time job.

This value is typically null if the value for the isDefinedInJob property is FALSE or UNKNOWN.

lastJobRunTime -> (timestamp)

The date and time, in UTC and extended ISO 8601 format, when the job (lastJobId) started. If the job is a recurring job, this value indicates when the most recent run started.

This value is typically null if the value for the isDefinedInJob property is FALSE or UNKNOWN.

lastAutomatedDiscoveryTime -> (timestamp)

The date and time, in UTC and extended ISO 8601 format, when Amazon Macie most recently analyzed objects in the bucket while performing automated sensitive data discovery. This value is null if this analysis hasnât occurred.

lastUpdated -> (timestamp)

The date and time, in UTC and extended ISO 8601 format, when Amazon Macie most recently retrieved bucket or object metadata from Amazon S3 for the bucket.

objectCount -> (long)

The total number of objects in the bucket.

objectCountByEncryptionType -> (structure)

The total number of objects in the bucket, grouped by server-side encryption type. This includes a grouping that reports the total number of objects that arenât encrypted or use client-side encryption.

customerManaged -> (long)

The total number of objects that are encrypted with customer-provided keys. The objects use server-side encryption with customer-provided keys (SSE-C).

kmsManaged -> (long)

The total number of objects that are encrypted with KMS keys, either Amazon Web Services managed keys or customer managed keys. The objects use dual-layer server-side encryption or server-side encryption with KMS keys (DSSE-KMS or SSE-KMS).

s3Managed -> (long)

The total number of objects that are encrypted with Amazon S3 managed keys. The objects use server-side encryption with Amazon S3 managed keys (SSE-S3).

unencrypted -> (long)

The total number of objects that use client-side encryption or arenât encrypted.

unknown -> (long)

The total number of objects that Amazon Macie doesnât have current encryption metadata for. Macie canât provide current data about the encryption settings for these objects.

publicAccess -> (structure)

Specifies whether the bucket is publicly accessible due to the combination of permissions settings that apply to the bucket, and provides information about those settings.

effectivePermission -> (string)

Specifies whether the bucket is publicly accessible due to the combination of permissions settings that apply to the bucket. Possible values are:

- NOT_PUBLIC - The bucket isnât publicly accessible.
- PUBLIC - The bucket is publicly accessible.
- UNKNOWN - Amazon Macie canât determine whether the bucket is publicly accessible.

permissionConfiguration -> (structure)

The account-level and bucket-level permissions settings for the bucket.

accountLevelPermissions -> (structure)

The account-level permissions settings that apply to the bucket.

blockPublicAccess -> (structure)

The block public access settings for the Amazon Web Services account that owns the bucket.

blockPublicAcls -> (boolean)

Specifies whether Amazon S3 blocks public access control lists (ACLs) for the bucket and objects in the bucket.

blockPublicPolicy -> (boolean)

Specifies whether Amazon S3 blocks public bucket policies for the bucket.

ignorePublicAcls -> (boolean)

Specifies whether Amazon S3 ignores public ACLs for the bucket and objects in the bucket.

restrictPublicBuckets -> (boolean)

Specifies whether Amazon S3 restricts public bucket policies for the bucket.

bucketLevelPermissions -> (structure)

The bucket-level permissions settings for the bucket.

accessControlList -> (structure)

The permissions settings of the access control list (ACL) for the bucket. This value is null if an ACL hasnât been defined for the bucket.

allowsPublicReadAccess -> (boolean)

Specifies whether the ACL grants the general public with read access permissions for the bucket.

allowsPublicWriteAccess -> (boolean)

Specifies whether the ACL grants the general public with write access permissions for the bucket.

blockPublicAccess -> (structure)

The block public access settings for the bucket.

blockPublicAcls -> (boolean)

Specifies whether Amazon S3 blocks public access control lists (ACLs) for the bucket and objects in the bucket.

blockPublicPolicy -> (boolean)

Specifies whether Amazon S3 blocks public bucket policies for the bucket.

ignorePublicAcls -> (boolean)

Specifies whether Amazon S3 ignores public ACLs for the bucket and objects in the bucket.

restrictPublicBuckets -> (boolean)

Specifies whether Amazon S3 restricts public bucket policies for the bucket.

bucketPolicy -> (structure)

The permissions settings of the bucket policy for the bucket. This value is null if a bucket policy hasnât been defined for the bucket.

allowsPublicReadAccess -> (boolean)

Specifies whether the bucket policy allows the general public to have read access to the bucket.

allowsPublicWriteAccess -> (boolean)

Specifies whether the bucket policy allows the general public to have write access to the bucket.

region -> (string)

The Amazon Web Services Region that hosts the bucket.

replicationDetails -> (structure)

Specifies whether the bucket is configured to replicate one or more objects to buckets for other Amazon Web Services accounts and, if so, which accounts.

replicated -> (boolean)

Specifies whether the bucket is configured to replicate one or more objects to any destination.

replicatedExternally -> (boolean)

Specifies whether the bucket is configured to replicate one or more objects to a bucket for an Amazon Web Services account that isnât part of your Amazon Macie organization. An *Amazon Macie organization* is a set of Macie accounts that are centrally managed as a group of related accounts through Organizations or by Macie invitation.

replicationAccounts -> (list)

An array of Amazon Web Services account IDs, one for each Amazon Web Services account that owns a bucket that the bucket is configured to replicate one or more objects to.

(string)

sensitivityScore -> (integer)

The sensitivity score for the bucket, ranging from -1 (classification error) to 100 (sensitive).

If automated sensitive data discovery has never been enabled for your account or itâs been disabled for your organization or standalone account for more than 30 days, possible values are: 1, the bucket is empty; or, 50, the bucket stores objects but itâs been excluded from recent analyses.

serverSideEncryption -> (structure)

The default server-side encryption settings for the bucket.

kmsMasterKeyId -> (string)

The Amazon Resource Name (ARN) or unique identifier (key ID) for the KMS key thatâs used by default to encrypt objects that are added to the bucket. This value is null if the bucket is configured to use an Amazon S3 managed key to encrypt new objects.

type -> (string)

The server-side encryption algorithm thatâs used by default to encrypt objects that are added to the bucket. Possible values are:

- AES256 - New objects use SSE-S3 encryption. Theyâre encrypted with an Amazon S3 managed key.
- aws:kms - New objects use SSE-KMS encryption. Theyâre encrypted with an KMS key (kmsMasterKeyId), either an Amazon Web Services managed key or a customer managed key.
- aws:kms:dsse - New objects use DSSE-KMS encryption. Theyâre encrypted with an KMS key (kmsMasterKeyId), either an Amazon Web Services managed key or a customer managed key.
- NONE - The bucketâs default encryption settings donât specify server-side encryption behavior for new objects.

sharedAccess -> (string)

Specifies whether the bucket is shared with another Amazon Web Services account, an Amazon CloudFront origin access identity (OAI), or a CloudFront origin access control (OAC). Possible values are:

- EXTERNAL - The bucket is shared with one or more of the following or any combination of the following: a CloudFront OAI, a CloudFront OAC, or an Amazon Web Services account that isnât part of your Amazon Macie organization.
- INTERNAL - The bucket is shared with one or more Amazon Web Services accounts that are part of your Amazon Macie organization. It isnât shared with a CloudFront OAI or OAC.
- NOT_SHARED - The bucket isnât shared with another Amazon Web Services account, a CloudFront OAI, or a CloudFront OAC.
- UNKNOWN - Amazon Macie wasnât able to evaluate the shared access settings for the bucket.

An *Amazon Macie organization* is a set of Macie accounts that are centrally managed as a group of related accounts through Organizations or by Macie invitation.

sizeInBytes -> (long)

The total storage size, in bytes, of the bucket.

If versioning is enabled for the bucket, Amazon Macie calculates this value based on the size of the latest version of each object in the bucket. This value doesnât reflect the storage size of all versions of each object in the bucket.

sizeInBytesCompressed -> (long)

The total storage size, in bytes, of the objects that are compressed (.gz, .gzip, .zip) files in the bucket.

If versioning is enabled for the bucket, Amazon Macie calculates this value based on the size of the latest version of each applicable object in the bucket. This value doesnât reflect the storage size of all versions of each applicable object in the bucket.

tags -> (list)

An array that specifies the tags (keys and values) that are associated with the bucket.

(structure)

Provides information about the tags that are associated with an S3 bucket or object. Each tag consists of a required tag key and an associated tag value.

key -> (string)

One part of a key-value pair that comprises a tag. A tag key is a general label that acts as a category for more specific tag values.

value -> (string)

One part of a key-value pair that comprises a tag. A tag value acts as a descriptor for a tag key. A tag value can be an empty string.

unclassifiableObjectCount -> (structure)

The total number of objects that Amazon Macie canât analyze in the bucket. These objects donât use a supported storage class or donât have a file name extension for a supported file or storage format.

fileType -> (long)

The total storage size (in bytes) or number of objects that Amazon Macie canât analyze because the objects donât have a file name extension for a supported file or storage format.

storageClass -> (long)

The total storage size (in bytes) or number of objects that Amazon Macie canât analyze because the objects use an unsupported storage class.

total -> (long)

The total storage size (in bytes) or number of objects that Amazon Macie canât analyze because the objects use an unsupported storage class or donât have a file name extension for a supported file or storage format.

unclassifiableObjectSizeInBytes -> (structure)

The total storage size, in bytes, of the objects that Amazon Macie canât analyze in the bucket. These objects donât use a supported storage class or donât have a file name extension for a supported file or storage format.

fileType -> (long)

The total storage size (in bytes) or number of objects that Amazon Macie canât analyze because the objects donât have a file name extension for a supported file or storage format.

storageClass -> (long)

The total storage size (in bytes) or number of objects that Amazon Macie canât analyze because the objects use an unsupported storage class.

total -> (long)

The total storage size (in bytes) or number of objects that Amazon Macie canât analyze because the objects use an unsupported storage class or donât have a file name extension for a supported file or storage format.

versioning -> (boolean)

Specifies whether versioning is enabled for the bucket.

nextToken -> (string)

The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.