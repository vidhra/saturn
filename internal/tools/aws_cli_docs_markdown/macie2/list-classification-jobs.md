# list-classification-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-classification-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-classification-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [macie2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/index.html#cli-aws-macie2) ]

# list-classification-jobs

## Description

Retrieves a subset of information about one or more classification jobs.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/macie2-2020-01-01/ListClassificationJobs)

`list-classification-jobs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `items`

## Synopsis

```
list-classification-jobs
[--filter-criteria <value>]
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

`--filter-criteria` (structure)

The criteria to use to filter the results.

excludes -> (list)

An array of objects, one for each condition that determines which jobs to exclude from the results.

(structure)

Specifies a condition that filters the results of a request for information about classification jobs. Each condition consists of a property, an operator, and one or more values.

comparator -> (string)

The operator to use to filter the results.

key -> (string)

The property to use to filter the results.

values -> (list)

An array that lists one or more values to use to filter the results.

(string)

includes -> (list)

An array of objects, one for each condition that determines which jobs to include in the results.

(structure)

Specifies a condition that filters the results of a request for information about classification jobs. Each condition consists of a property, an operator, and one or more values.

comparator -> (string)

The operator to use to filter the results.

key -> (string)

The property to use to filter the results.

values -> (list)

An array that lists one or more values to use to filter the results.

(string)

JSON Syntax:

```
{
  "excludes": [
    {
      "comparator": "EQ"|"GT"|"GTE"|"LT"|"LTE"|"NE"|"CONTAINS"|"STARTS_WITH",
      "key": "jobType"|"jobStatus"|"createdAt"|"name",
      "values": ["string", ...]
    }
    ...
  ],
  "includes": [
    {
      "comparator": "EQ"|"GT"|"GTE"|"LT"|"LTE"|"NE"|"CONTAINS"|"STARTS_WITH",
      "key": "jobType"|"jobStatus"|"createdAt"|"name",
      "values": ["string", ...]
    }
    ...
  ]
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
  "attributeName": "createdAt"|"jobStatus"|"name"|"jobType",
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

items -> (list)

An array of objects, one for each job that matches the filter criteria specified in the request.

(structure)

Provides information about a classification job, including the current status of the job.

bucketCriteria -> (structure)

The property- and tag-based conditions that determine which S3 buckets are included or excluded from the jobâs analysis. Each time the job runs, the job uses these criteria to determine which buckets to analyze. A jobâs definition can contain a bucketCriteria object or a bucketDefinitions array, not both.

excludes -> (structure)

The property- and tag-based conditions that determine which buckets to exclude from the job.

and -> (list)

An array of conditions, one for each condition that determines which buckets to include or exclude from the job. If you specify more than one condition, Amazon Macie uses AND logic to join the conditions.

(structure)

Specifies a property- or tag-based condition that defines criteria for including or excluding S3 buckets from a classification job.

simpleCriterion -> (structure)

A property-based condition that defines a property, operator, and one or more values for including or excluding buckets from the job.

comparator -> (string)

The operator to use in the condition. Valid values are EQ (equals) and NE (not equals).

key -> (string)

The property to use in the condition.

values -> (list)

An array that lists one or more values to use in the condition. If you specify multiple values, Amazon Macie uses OR logic to join the values. Valid values for each supported property (key) are:

- ACCOUNT_ID - A string that represents the unique identifier for the Amazon Web Services account that owns the bucket.
- S3_BUCKET_EFFECTIVE_PERMISSION - A string that represents an enumerated value that Macie defines for the [BucketPublicAccess.effectivePermission](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketpublicaccess-effectivepermission) property of a bucket.
- S3_BUCKET_NAME - A string that represents the name of a bucket.
- S3_BUCKET_SHARED_ACCESS - A string that represents an enumerated value that Macie defines for the [BucketMetadata.sharedAccess](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketmetadata-sharedaccess) property of a bucket.

Values are case sensitive. Also, Macie doesnât support use of partial values or wildcard characters in these values.

(string)

tagCriterion -> (structure)

A tag-based condition that defines an operator and tag keys, tag values, or tag key and value pairs for including or excluding buckets from the job.

comparator -> (string)

The operator to use in the condition. Valid values are EQ (equals) and NE (not equals).

tagValues -> (list)

The tag keys, tag values, or tag key and value pairs to use in the condition.

(structure)

Specifies a tag key, a tag value, or a tag key and value (as a pair) to use in a tag-based condition that determines whether an S3 bucket is included or excluded from a classification job. Tag keys and values are case sensitive. Also, Amazon Macie doesnât support use of partial values or wildcard characters in tag-based conditions.

key -> (string)

The value for the tag key to use in the condition.

value -> (string)

The tag value to use in the condition.

includes -> (structure)

The property- and tag-based conditions that determine which buckets to include in the job.

and -> (list)

An array of conditions, one for each condition that determines which buckets to include or exclude from the job. If you specify more than one condition, Amazon Macie uses AND logic to join the conditions.

(structure)

Specifies a property- or tag-based condition that defines criteria for including or excluding S3 buckets from a classification job.

simpleCriterion -> (structure)

A property-based condition that defines a property, operator, and one or more values for including or excluding buckets from the job.

comparator -> (string)

The operator to use in the condition. Valid values are EQ (equals) and NE (not equals).

key -> (string)

The property to use in the condition.

values -> (list)

An array that lists one or more values to use in the condition. If you specify multiple values, Amazon Macie uses OR logic to join the values. Valid values for each supported property (key) are:

- ACCOUNT_ID - A string that represents the unique identifier for the Amazon Web Services account that owns the bucket.
- S3_BUCKET_EFFECTIVE_PERMISSION - A string that represents an enumerated value that Macie defines for the [BucketPublicAccess.effectivePermission](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketpublicaccess-effectivepermission) property of a bucket.
- S3_BUCKET_NAME - A string that represents the name of a bucket.
- S3_BUCKET_SHARED_ACCESS - A string that represents an enumerated value that Macie defines for the [BucketMetadata.sharedAccess](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketmetadata-sharedaccess) property of a bucket.

Values are case sensitive. Also, Macie doesnât support use of partial values or wildcard characters in these values.

(string)

tagCriterion -> (structure)

A tag-based condition that defines an operator and tag keys, tag values, or tag key and value pairs for including or excluding buckets from the job.

comparator -> (string)

The operator to use in the condition. Valid values are EQ (equals) and NE (not equals).

tagValues -> (list)

The tag keys, tag values, or tag key and value pairs to use in the condition.

(structure)

Specifies a tag key, a tag value, or a tag key and value (as a pair) to use in a tag-based condition that determines whether an S3 bucket is included or excluded from a classification job. Tag keys and values are case sensitive. Also, Amazon Macie doesnât support use of partial values or wildcard characters in tag-based conditions.

key -> (string)

The value for the tag key to use in the condition.

value -> (string)

The tag value to use in the condition.

bucketDefinitions -> (list)

An array of objects, one for each Amazon Web Services account that owns specific S3 buckets for the job to analyze. Each object specifies the account ID for an account and one or more buckets to analyze for that account. A jobâs definition can contain a bucketDefinitions array or a bucketCriteria object, not both.

(structure)

Specifies an Amazon Web Services account that owns S3 buckets for a classification job to analyze, and one or more specific buckets to analyze for that account.

accountId -> (string)

The unique identifier for the Amazon Web Services account that owns the buckets.

buckets -> (list)

An array that lists the names of the buckets.

(string)

createdAt -> (timestamp)

The date and time, in UTC and extended ISO 8601 format, when the job was created.

jobId -> (string)

The unique identifier for the job.

jobStatus -> (string)

The current status of the job. Possible values are:

- CANCELLED - You cancelled the job or, if itâs a one-time job, you paused the job and didnât resume it within 30 days.
- COMPLETE - For a one-time job, Amazon Macie finished processing the data specified for the job. This value doesnât apply to recurring jobs.
- IDLE - For a recurring job, the previous scheduled run is complete and the next scheduled run is pending. This value doesnât apply to one-time jobs.
- PAUSED - Macie started running the job but additional processing would exceed the monthly sensitive data discovery quota for your account or one or more member accounts that the job analyzes data for.
- RUNNING - For a one-time job, the job is in progress. For a recurring job, a scheduled run is in progress.
- USER_PAUSED - You paused the job. If you paused the job while it had a status of RUNNING and you donât resume it within 30 days of pausing it, the job or job run will expire and be cancelled, depending on the jobâs type. To check the expiration date, refer to the UserPausedDetails.jobExpiresAt property.

jobType -> (string)

The schedule for running the job. Possible values are:

- ONE_TIME - The job runs only once.
- SCHEDULED - The job runs on a daily, weekly, or monthly basis.

lastRunErrorStatus -> (structure)

Specifies whether any account- or bucket-level access errors occurred when the job ran. For a recurring job, this value indicates the error status of the jobâs most recent run.

code -> (string)

Specifies whether any account- or bucket-level access errors occurred when the job ran. For a recurring job, this value indicates the error status of the jobâs most recent run. Possible values are:

- ERROR - One or more errors occurred. Amazon Macie didnât process all the data specified for the job.
- NONE - No errors occurred. Macie processed all the data specified for the job.

name -> (string)

The custom name of the job.

userPausedDetails -> (structure)

If the current status of the job is USER_PAUSED, specifies when the job was paused and when the job or job run will expire and be cancelled if it isnât resumed. This value is present only if the value for jobStatus is USER_PAUSED.

jobExpiresAt -> (timestamp)

The date and time, in UTC and extended ISO 8601 format, when the job or job run will expire and be cancelled if you donât resume it first.

jobImminentExpirationHealthEventArn -> (string)

The Amazon Resource Name (ARN) of the Health event that Amazon Macie sent to notify you of the job or job runâs pending expiration and cancellation. This value is null if a job has been paused for less than 23 days.

jobPausedAt -> (timestamp)

The date and time, in UTC and extended ISO 8601 format, when you paused the job.

nextToken -> (string)

The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.