# create-classification-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-classification-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-classification-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [macie2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/index.html#cli-aws-macie2) ]

# create-classification-job

## Description

Creates and defines the settings for a classification job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/macie2-2020-01-01/CreateClassificationJob)

## Synopsis

```
create-classification-job
[--allow-list-ids <value>]
[--client-token <value>]
[--custom-data-identifier-ids <value>]
[--description <value>]
[--initial-run | --no-initial-run]
--job-type <value>
[--managed-data-identifier-ids <value>]
[--managed-data-identifier-selector <value>]
--name <value>
--s3-job-definition <value>
[--sampling-percentage <value>]
[--schedule-frequency <value>]
[--tags <value>]
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

`--allow-list-ids` (list)

An array of unique identifiers, one for each allow list for the job to use when it analyzes data.

(string)

Syntax:

```
"string" "string" ...
```

`--client-token` (string)

A unique, case-sensitive token that you provide to ensure the idempotency of the request.

`--custom-data-identifier-ids` (list)

An array of unique identifiers, one for each custom data identifier for the job to use when it analyzes data. To use only managed data identifiers, donât specify a value for this property and specify a value other than NONE for the managedDataIdentifierSelector property.

(string)

Syntax:

```
"string" "string" ...
```

`--description` (string)

A custom description of the job. The description can contain as many as 200 characters.

`--initial-run` | `--no-initial-run` (boolean)

For a recurring job, specifies whether to analyze all existing, eligible objects immediately after the job is created (true). To analyze only those objects that are created or changed after you create the job and before the jobâs first scheduled run, set this value to false.

If you configure the job to run only once, donât specify a value for this property.

`--job-type` (string)

The schedule for running the job. Valid values are:

- ONE_TIME - Run the job only once. If you specify this value, donât specify a value for the scheduleFrequency property.
- SCHEDULED - Run the job on a daily, weekly, or monthly basis. If you specify this value, use the scheduleFrequency property to specify the recurrence pattern for the job.

Possible values:

- `ONE_TIME`
- `SCHEDULED`

`--managed-data-identifier-ids` (list)

An array of unique identifiers, one for each managed data identifier for the job to include (use) or exclude (not use) when it analyzes data. Inclusion or exclusion depends on the managed data identifier selection type that you specify for the job (managedDataIdentifierSelector).

To retrieve a list of valid values for this property, use the ListManagedDataIdentifiers operation.

(string)

Syntax:

```
"string" "string" ...
```

`--managed-data-identifier-selector` (string)

The selection type to apply when determining which managed data identifiers the job uses to analyze data. Valid values are:

- ALL - Use all managed data identifiers. If you specify this value, donât specify any values for the managedDataIdentifierIds property.
- EXCLUDE - Use all managed data identifiers except the ones specified by the managedDataIdentifierIds property.
- INCLUDE - Use only the managed data identifiers specified by the managedDataIdentifierIds property.
- NONE - Donât use any managed data identifiers. If you specify this value, specify at least one value for the customDataIdentifierIds property and donât specify any values for the managedDataIdentifierIds property.
- RECOMMENDED (default) - Use the recommended set of managed data identifiers. If you specify this value, donât specify any values for the managedDataIdentifierIds property.

If you donât specify a value for this property, the job uses the recommended set of managed data identifiers.

If the job is a recurring job and you specify ALL or EXCLUDE, each job run automatically uses new managed data identifiers that are released. If you donât specify a value for this property or you specify RECOMMENDED for a recurring job, each job run automatically uses all the managed data identifiers that are in the recommended set when the run starts.

To learn about individual managed data identifiers or determine which ones are in the recommended set, see [Using managed data identifiers](https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html) or [Recommended managed data identifiers](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-mdis-recommended.html) in the *Amazon Macie User Guide* .

Possible values:

- `ALL`
- `EXCLUDE`
- `INCLUDE`
- `NONE`
- `RECOMMENDED`

`--name` (string)

A custom name for the job. The name can contain as many as 500 characters.

`--s3-job-definition` (structure)

The S3 buckets that contain the objects to analyze, and the scope of that analysis.

bucketCriteria -> (structure)

The property- and tag-based conditions that determine which S3 buckets to include or exclude from the analysis. Each time the job runs, the job uses these criteria to determine which buckets contain objects to analyze. A jobâs definition can contain a bucketCriteria object or a bucketDefinitions array, not both.

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

An array of objects, one for each Amazon Web Services account that owns specific S3 buckets to analyze. Each object specifies the account ID for an account and one or more buckets to analyze for that account. A jobâs definition can contain a bucketDefinitions array or a bucketCriteria object, not both.

(structure)

Specifies an Amazon Web Services account that owns S3 buckets for a classification job to analyze, and one or more specific buckets to analyze for that account.

accountId -> (string)

The unique identifier for the Amazon Web Services account that owns the buckets.

buckets -> (list)

An array that lists the names of the buckets.

(string)

scoping -> (structure)

The property- and tag-based conditions that determine which S3 objects to include or exclude from the analysis. Each time the job runs, the job uses these criteria to determine which objects to analyze.

excludes -> (structure)

The property- and tag-based conditions that determine which objects to exclude from the analysis.

and -> (list)

An array of conditions, one for each property- or tag-based condition that determines which objects to include or exclude from the job. If you specify more than one condition, Amazon Macie uses AND logic to join the conditions.

(structure)

Specifies a property- or tag-based condition that defines criteria for including or excluding S3 objects from a classification job. A JobScopeTerm object can contain only one simpleScopeTerm object or one tagScopeTerm object.

simpleScopeTerm -> (structure)

A property-based condition that defines a property, operator, and one or more values for including or excluding objects from the job.

comparator -> (string)

The operator to use in the condition. Valid values for each supported property (key) are:

- OBJECT_EXTENSION - EQ (equals) or NE (not equals)
- OBJECT_KEY - STARTS_WITH
- OBJECT_LAST_MODIFIED_DATE - EQ (equals), GT (greater than), GTE (greater than or equals), LT (less than), LTE (less than or equals), or NE (not equals)
- OBJECT_SIZE - EQ (equals), GT (greater than), GTE (greater than or equals), LT (less than), LTE (less than or equals), or NE (not equals)

key -> (string)

The object property to use in the condition.

values -> (list)

An array that lists the values to use in the condition. If the value for the key property is OBJECT_EXTENSION or OBJECT_KEY, this array can specify multiple values and Amazon Macie uses OR logic to join the values. Otherwise, this array can specify only one value.

Valid values for each supported property (key) are:

- OBJECT_EXTENSION - A string that represents the file name extension of an object. For example: docx or pdf
- OBJECT_KEY - A string that represents the key prefix (folder name or path) of an object. For example: logs or awslogs/eventlogs. This value applies a condition to objects whose keys (names) begin with the specified value.
- OBJECT_LAST_MODIFIED_DATE - The date and time (in UTC and extended ISO 8601 format) when an object was created or last changed, whichever is latest. For example: 2023-09-24T14:31:13Z
- OBJECT_SIZE - An integer that represents the storage size (in bytes) of an object.

Macie doesnât support use of wildcard characters in these values. Also, string values are case sensitive.

(string)

tagScopeTerm -> (structure)

A tag-based condition that defines the operator and tag keys or tag key and value pairs for including or excluding objects from the job.

comparator -> (string)

The operator to use in the condition. Valid values are EQ (equals) or NE (not equals).

key -> (string)

The object property to use in the condition. The only valid value is TAG.

tagValues -> (list)

The tag keys or tag key and value pairs to use in the condition. To specify only tag keys in a condition, specify the keys in this array and set the value for each associated tag value to an empty string.

(structure)

Specifies a tag key or tag key and value pair to use in a tag-based condition that determines whether an S3 object is included or excluded from a classification job. Tag keys and values are case sensitive. Also, Amazon Macie doesnât support use of partial values or wildcard characters in tag-based conditions.

key -> (string)

The value for the tag key to use in the condition.

value -> (string)

The tag value, associated with the specified tag key (key), to use in the condition. To specify only a tag key for a condition, specify the tag key for the key property and set this value to an empty string.

target -> (string)

The type of object to apply the condition to.

includes -> (structure)

The property- and tag-based conditions that determine which objects to include in the analysis.

and -> (list)

An array of conditions, one for each property- or tag-based condition that determines which objects to include or exclude from the job. If you specify more than one condition, Amazon Macie uses AND logic to join the conditions.

(structure)

Specifies a property- or tag-based condition that defines criteria for including or excluding S3 objects from a classification job. A JobScopeTerm object can contain only one simpleScopeTerm object or one tagScopeTerm object.

simpleScopeTerm -> (structure)

A property-based condition that defines a property, operator, and one or more values for including or excluding objects from the job.

comparator -> (string)

The operator to use in the condition. Valid values for each supported property (key) are:

- OBJECT_EXTENSION - EQ (equals) or NE (not equals)
- OBJECT_KEY - STARTS_WITH
- OBJECT_LAST_MODIFIED_DATE - EQ (equals), GT (greater than), GTE (greater than or equals), LT (less than), LTE (less than or equals), or NE (not equals)
- OBJECT_SIZE - EQ (equals), GT (greater than), GTE (greater than or equals), LT (less than), LTE (less than or equals), or NE (not equals)

key -> (string)

The object property to use in the condition.

values -> (list)

An array that lists the values to use in the condition. If the value for the key property is OBJECT_EXTENSION or OBJECT_KEY, this array can specify multiple values and Amazon Macie uses OR logic to join the values. Otherwise, this array can specify only one value.

Valid values for each supported property (key) are:

- OBJECT_EXTENSION - A string that represents the file name extension of an object. For example: docx or pdf
- OBJECT_KEY - A string that represents the key prefix (folder name or path) of an object. For example: logs or awslogs/eventlogs. This value applies a condition to objects whose keys (names) begin with the specified value.
- OBJECT_LAST_MODIFIED_DATE - The date and time (in UTC and extended ISO 8601 format) when an object was created or last changed, whichever is latest. For example: 2023-09-24T14:31:13Z
- OBJECT_SIZE - An integer that represents the storage size (in bytes) of an object.

Macie doesnât support use of wildcard characters in these values. Also, string values are case sensitive.

(string)

tagScopeTerm -> (structure)

A tag-based condition that defines the operator and tag keys or tag key and value pairs for including or excluding objects from the job.

comparator -> (string)

The operator to use in the condition. Valid values are EQ (equals) or NE (not equals).

key -> (string)

The object property to use in the condition. The only valid value is TAG.

tagValues -> (list)

The tag keys or tag key and value pairs to use in the condition. To specify only tag keys in a condition, specify the keys in this array and set the value for each associated tag value to an empty string.

(structure)

Specifies a tag key or tag key and value pair to use in a tag-based condition that determines whether an S3 object is included or excluded from a classification job. Tag keys and values are case sensitive. Also, Amazon Macie doesnât support use of partial values or wildcard characters in tag-based conditions.

key -> (string)

The value for the tag key to use in the condition.

value -> (string)

The tag value, associated with the specified tag key (key), to use in the condition. To specify only a tag key for a condition, specify the tag key for the key property and set this value to an empty string.

target -> (string)

The type of object to apply the condition to.

JSON Syntax:

```
{
  "bucketCriteria": {
    "excludes": {
      "and": [
        {
          "simpleCriterion": {
            "comparator": "EQ"|"GT"|"GTE"|"LT"|"LTE"|"NE"|"CONTAINS"|"STARTS_WITH",
            "key": "ACCOUNT_ID"|"S3_BUCKET_NAME"|"S3_BUCKET_EFFECTIVE_PERMISSION"|"S3_BUCKET_SHARED_ACCESS",
            "values": ["string", ...]
          },
          "tagCriterion": {
            "comparator": "EQ"|"GT"|"GTE"|"LT"|"LTE"|"NE"|"CONTAINS"|"STARTS_WITH",
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
            "comparator": "EQ"|"GT"|"GTE"|"LT"|"LTE"|"NE"|"CONTAINS"|"STARTS_WITH",
            "key": "ACCOUNT_ID"|"S3_BUCKET_NAME"|"S3_BUCKET_EFFECTIVE_PERMISSION"|"S3_BUCKET_SHARED_ACCESS",
            "values": ["string", ...]
          },
          "tagCriterion": {
            "comparator": "EQ"|"GT"|"GTE"|"LT"|"LTE"|"NE"|"CONTAINS"|"STARTS_WITH",
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
  },
  "bucketDefinitions": [
    {
      "accountId": "string",
      "buckets": ["string", ...]
    }
    ...
  ],
  "scoping": {
    "excludes": {
      "and": [
        {
          "simpleScopeTerm": {
            "comparator": "EQ"|"GT"|"GTE"|"LT"|"LTE"|"NE"|"CONTAINS"|"STARTS_WITH",
            "key": "OBJECT_EXTENSION"|"OBJECT_LAST_MODIFIED_DATE"|"OBJECT_SIZE"|"OBJECT_KEY",
            "values": ["string", ...]
          },
          "tagScopeTerm": {
            "comparator": "EQ"|"GT"|"GTE"|"LT"|"LTE"|"NE"|"CONTAINS"|"STARTS_WITH",
            "key": "string",
            "tagValues": [
              {
                "key": "string",
                "value": "string"
              }
              ...
            ],
            "target": "S3_OBJECT"
          }
        }
        ...
      ]
    },
    "includes": {
      "and": [
        {
          "simpleScopeTerm": {
            "comparator": "EQ"|"GT"|"GTE"|"LT"|"LTE"|"NE"|"CONTAINS"|"STARTS_WITH",
            "key": "OBJECT_EXTENSION"|"OBJECT_LAST_MODIFIED_DATE"|"OBJECT_SIZE"|"OBJECT_KEY",
            "values": ["string", ...]
          },
          "tagScopeTerm": {
            "comparator": "EQ"|"GT"|"GTE"|"LT"|"LTE"|"NE"|"CONTAINS"|"STARTS_WITH",
            "key": "string",
            "tagValues": [
              {
                "key": "string",
                "value": "string"
              }
              ...
            ],
            "target": "S3_OBJECT"
          }
        }
        ...
      ]
    }
  }
}
```

`--sampling-percentage` (integer)

The sampling depth, as a percentage, for the job to apply when processing objects. This value determines the percentage of eligible objects that the job analyzes. If this value is less than 100, Amazon Macie selects the objects to analyze at random, up to the specified percentage, and analyzes all the data in those objects.

`--schedule-frequency` (structure)

The recurrence pattern for running the job. To run the job only once, donât specify a value for this property and set the value for the jobType property to ONE_TIME.

dailySchedule -> (structure)

Specifies a daily recurrence pattern for running the job.

monthlySchedule -> (structure)

Specifies a monthly recurrence pattern for running the job.

dayOfMonth -> (integer)

The numeric day of the month when Amazon Macie runs the job. This value can be an integer from 1 through 31.

If this value exceeds the number of days in a certain month, Macie doesnât run the job that month. Macie runs the job only during months that have the specified day. For example, if this value is 31 and a month has only 30 days, Macie doesnât run the job that month. To run the job every month, specify a value thatâs less than 29.

weeklySchedule -> (structure)

Specifies a weekly recurrence pattern for running the job.

dayOfWeek -> (string)

The day of the week when Amazon Macie runs the job.

Shorthand Syntax:

```
dailySchedule={},monthlySchedule={dayOfMonth=integer},weeklySchedule={dayOfWeek=string}
```

JSON Syntax:

```
{
  "dailySchedule": {

  },
  "monthlySchedule": {
    "dayOfMonth": integer
  },
  "weeklySchedule": {
    "dayOfWeek": "SUNDAY"|"MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY"|"SATURDAY"
  }
}
```

`--tags` (map)

A map of key-value pairs that specifies the tags to associate with the job.

A job can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.

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

jobArn -> (string)

The Amazon Resource Name (ARN) of the job.

jobId -> (string)

The unique identifier for the job.