# search-resourcesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/search-resources.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/search-resources.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [macie2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/index.html#cli-aws-macie2) ]

# search-resources

## Description

Retrieves (queries) statistical data and other information about Amazon Web Services resources that Amazon Macie monitors and analyzes for an account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/macie2-2020-01-01/SearchResources)

`search-resources` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `matchingResources`

## Synopsis

```
search-resources
[--bucket-criteria <value>]
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

`--bucket-criteria` (structure)

The filter conditions that determine which S3 buckets to include or exclude from the query results.

excludes -> (structure)

The property- and tag-based conditions that determine which buckets to exclude from the results.

and -> (list)

An array of objects, one for each property- or tag-based condition that includes or excludes resources from the query results. If you specify more than one condition, Amazon Macie uses AND logic to join the conditions.

(structure)

Specifies a property- or tag-based filter condition for including or excluding Amazon Web Services resources from the query results.

simpleCriterion -> (structure)

A property-based condition that defines a property, operator, and one or more values for including or excluding resources from the results.

comparator -> (string)

The operator to use in the condition. Valid values are EQ (equals) and NE (not equals).

key -> (string)

The property to use in the condition.

values -> (list)

An array that lists one or more values to use in the condition. If you specify multiple values, Amazon Macie uses OR logic to join the values. Valid values for each supported property (key) are:

- ACCOUNT_ID - A string that represents the unique identifier for the Amazon Web Services account that owns the resource.
- AUTOMATED_DISCOVERY_MONITORING_STATUS - A string that represents an enumerated value that Macie defines for the [BucketMetadata.automatedDiscoveryMonitoringStatus](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketmetadata-automateddiscoverymonitoringstatus) property of an S3 bucket.
- S3_BUCKET_EFFECTIVE_PERMISSION - A string that represents an enumerated value that Macie defines for the [BucketPublicAccess.effectivePermission](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketpublicaccess-effectivepermission) property of an S3 bucket.
- S3_BUCKET_NAME - A string that represents the name of an S3 bucket.
- S3_BUCKET_SHARED_ACCESS - A string that represents an enumerated value that Macie defines for the [BucketMetadata.sharedAccess](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketmetadata-sharedaccess) property of an S3 bucket.

Values are case sensitive. Also, Macie doesnât support use of partial values or wildcard characters in values.

(string)

tagCriterion -> (structure)

A tag-based condition that defines an operator and tag keys, tag values, or tag key and value pairs for including or excluding resources from the results.

comparator -> (string)

The operator to use in the condition. Valid values are EQ (equals) and NE (not equals).

tagValues -> (list)

The tag keys, tag values, or tag key and value pairs to use in the condition.

(structure)

Specifies a tag key, a tag value, or a tag key and value (as a pair) to use in a tag-based filter condition for a query. Tag keys and values are case sensitive. Also, Amazon Macie doesnât support use of partial values or wildcard characters in tag-based filter conditions.

key -> (string)

The value for the tag key to use in the condition.

value -> (string)

The tag value to use in the condition.

includes -> (structure)

The property- and tag-based conditions that determine which buckets to include in the results.

and -> (list)

An array of objects, one for each property- or tag-based condition that includes or excludes resources from the query results. If you specify more than one condition, Amazon Macie uses AND logic to join the conditions.

(structure)

Specifies a property- or tag-based filter condition for including or excluding Amazon Web Services resources from the query results.

simpleCriterion -> (structure)

A property-based condition that defines a property, operator, and one or more values for including or excluding resources from the results.

comparator -> (string)

The operator to use in the condition. Valid values are EQ (equals) and NE (not equals).

key -> (string)

The property to use in the condition.

values -> (list)

An array that lists one or more values to use in the condition. If you specify multiple values, Amazon Macie uses OR logic to join the values. Valid values for each supported property (key) are:

- ACCOUNT_ID - A string that represents the unique identifier for the Amazon Web Services account that owns the resource.
- AUTOMATED_DISCOVERY_MONITORING_STATUS - A string that represents an enumerated value that Macie defines for the [BucketMetadata.automatedDiscoveryMonitoringStatus](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketmetadata-automateddiscoverymonitoringstatus) property of an S3 bucket.
- S3_BUCKET_EFFECTIVE_PERMISSION - A string that represents an enumerated value that Macie defines for the [BucketPublicAccess.effectivePermission](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketpublicaccess-effectivepermission) property of an S3 bucket.
- S3_BUCKET_NAME - A string that represents the name of an S3 bucket.
- S3_BUCKET_SHARED_ACCESS - A string that represents an enumerated value that Macie defines for the [BucketMetadata.sharedAccess](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketmetadata-sharedaccess) property of an S3 bucket.

Values are case sensitive. Also, Macie doesnât support use of partial values or wildcard characters in values.

(string)

tagCriterion -> (structure)

A tag-based condition that defines an operator and tag keys, tag values, or tag key and value pairs for including or excluding resources from the results.

comparator -> (string)

The operator to use in the condition. Valid values are EQ (equals) and NE (not equals).

tagValues -> (list)

The tag keys, tag values, or tag key and value pairs to use in the condition.

(structure)

Specifies a tag key, a tag value, or a tag key and value (as a pair) to use in a tag-based filter condition for a query. Tag keys and values are case sensitive. Also, Amazon Macie doesnât support use of partial values or wildcard characters in tag-based filter conditions.

key -> (string)

The value for the tag key to use in the condition.

value -> (string)

The tag value to use in the condition.

JSON Syntax:

```
{
  "excludes": {
    "and": [
      {
        "simpleCriterion": {
          "comparator": "EQ"|"NE",
          "key": "ACCOUNT_ID"|"S3_BUCKET_NAME"|"S3_BUCKET_EFFECTIVE_PERMISSION"|"S3_BUCKET_SHARED_ACCESS"|"AUTOMATED_DISCOVERY_MONITORING_STATUS",
          "values": ["string", ...]
        },
        "tagCriterion": {
          "comparator": "EQ"|"NE",
          "tagValues": [
            {
              "key": "string",
              "value": "string"
            }
            ...
          ]
        }
      }
      ...
    ]
  },
  "includes": {
    "and": [
      {
        "simpleCriterion": {
          "comparator": "EQ"|"NE",
          "key": "ACCOUNT_ID"|"S3_BUCKET_NAME"|"S3_BUCKET_EFFECTIVE_PERMISSION"|"S3_BUCKET_SHARED_ACCESS"|"AUTOMATED_DISCOVERY_MONITORING_STATUS",
          "values": ["string", ...]
        },
        "tagCriterion": {
          "comparator": "EQ"|"NE",
          "tagValues": [
            {
              "key": "string",
              "value": "string"
            }
            ...
          ]
        }
      }
      ...
    ]
  }
}
```

`--sort-criteria` (structure)

The criteria to use to sort the results.

attributeName -> (string)

The property to sort the results by.

orderBy -> (string)

The sort order to apply to the results, based on the value for the property specified by the attributeName property. Valid values are: ASC, sort the results in ascending order; and, DESC, sort the results in descending order.

Shorthand Syntax:

```
attributeName=string,orderBy=string
```

JSON Syntax:

```
{
  "attributeName": "ACCOUNT_ID"|"RESOURCE_NAME"|"S3_CLASSIFIABLE_OBJECT_COUNT"|"S3_CLASSIFIABLE_SIZE_IN_BYTES",
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

## Output

matchingResources -> (list)

An array of objects, one for each resource that matches the filter criteria specified in the request.

(structure)

Provides statistical data and other information about an Amazon Web Services resource that Amazon Macie monitors and analyzes for your account.

matchingBucket -> (structure)

The details of an S3 bucket that Amazon Macie monitors and analyzes for your account.

accountId -> (string)

The unique identifier for the Amazon Web Services account that owns the bucket.

automatedDiscoveryMonitoringStatus -> (string)

Specifies whether automated sensitive data discovery is currently configured to analyze objects in the bucket. Possible values are: MONITORED, the bucket is included in analyses; and, NOT_MONITORED, the bucket is excluded from analyses. If automated sensitive data discovery is disabled for your account, this value is NOT_MONITORED.

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

sensitivityScore -> (integer)

The sensitivity score for the bucket, ranging from -1 (classification error) to 100 (sensitive).

If automated sensitive data discovery has never been enabled for your account or itâs been disabled for your organization or standalone account for more than 30 days, possible values are: 1, the bucket is empty; or, 50, the bucket stores objects but itâs been excluded from recent analyses.

sizeInBytes -> (long)

The total storage size, in bytes, of the bucket.

If versioning is enabled for the bucket, Amazon Macie calculates this value based on the size of the latest version of each object in the bucket. This value doesnât reflect the storage size of all versions of each object in the bucket.

sizeInBytesCompressed -> (long)

The total storage size, in bytes, of the objects that are compressed (.gz, .gzip, .zip) files in the bucket.

If versioning is enabled for the bucket, Amazon Macie calculates this value based on the size of the latest version of each applicable object in the bucket. This value doesnât reflect the storage size of all versions of each applicable object in the bucket.

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

nextToken -> (string)

The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.