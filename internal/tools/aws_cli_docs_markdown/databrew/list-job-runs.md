# list-job-runsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/list-job-runs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/list-job-runs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [databrew](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/index.html#cli-aws-databrew) ]

# list-job-runs

## Description

Lists all of the previous runs of a particular DataBrew job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/databrew-2017-07-25/ListJobRuns)

`list-job-runs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `JobRuns`

## Synopsis

```
list-job-runs
--name <value>
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

`--name` (string)

The name of the job.

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

JobRuns -> (list)

A list of job runs that have occurred for the specified job.

(structure)

Represents one run of a DataBrew job.

Attempt -> (integer)

The number of times that DataBrew has attempted to run the job.

CompletedOn -> (timestamp)

The date and time when the job completed processing.

DatasetName -> (string)

The name of the dataset for the job to process.

ErrorMessage -> (string)

A message indicating an error (if any) that was encountered when the job ran.

ExecutionTime -> (integer)

The amount of time, in seconds, during which a job run consumed resources.

JobName -> (string)

The name of the job being processed during this run.

RunId -> (string)

The unique identifier of the job run.

State -> (string)

The current state of the job run entity itself.

LogSubscription -> (string)

The current status of Amazon CloudWatch logging for the job run.

LogGroupName -> (string)

The name of an Amazon CloudWatch log group, where the job writes diagnostic messages when it runs.

Outputs -> (list)

One or more output artifacts from a job run.

(structure)

Represents options that specify how and where in Amazon S3 DataBrew writes the output generated by recipe jobs or profile jobs.

CompressionFormat -> (string)

The compression algorithm used to compress the output text of the job.

Format -> (string)

The data format of the output of the job.

PartitionColumns -> (list)

The names of one or more partition columns for the output of the job.

(string)

Location -> (structure)

The location in Amazon S3 where the job writes its output.

Bucket -> (string)

The Amazon S3 bucket name.

Key -> (string)

The unique name of the object in the bucket.

BucketOwner -> (string)

The Amazon Web Services account ID of the bucket owner.

Overwrite -> (boolean)

A value that, if true, means that any data in the location specified for output is overwritten with new output.

FormatOptions -> (structure)

Represents options that define how DataBrew formats job output files.

Csv -> (structure)

Represents a set of options that define the structure of comma-separated value (CSV) job output.

Delimiter -> (string)

A single character that specifies the delimiter used to create CSV job output.

MaxOutputFiles -> (integer)

Maximum number of files to be generated by the job and written to the output folder. For output partitioned by column(s), the MaxOutputFiles value is the maximum number of files per partition.

DataCatalogOutputs -> (list)

One or more artifacts that represent the Glue Data Catalog output from running the job.

(structure)

Represents options that specify how and where in the Glue Data Catalog DataBrew writes the output generated by recipe jobs.

CatalogId -> (string)

The unique identifier of the Amazon Web Services account that holds the Data Catalog that stores the data.

DatabaseName -> (string)

The name of a database in the Data Catalog.

TableName -> (string)

The name of a table in the Data Catalog.

S3Options -> (structure)

Represents options that specify how and where DataBrew writes the Amazon S3 output generated by recipe jobs.

Location -> (structure)

Represents an Amazon S3 location (bucket name and object key) where DataBrew can write output from a job.

Bucket -> (string)

The Amazon S3 bucket name.

Key -> (string)

The unique name of the object in the bucket.

BucketOwner -> (string)

The Amazon Web Services account ID of the bucket owner.

DatabaseOptions -> (structure)

Represents options that specify how and where DataBrew writes the database output generated by recipe jobs.

TempDirectory -> (structure)

Represents an Amazon S3 location (bucket name and object key) where DataBrew can store intermediate results.

Bucket -> (string)

The Amazon S3 bucket name.

Key -> (string)

The unique name of the object in the bucket.

BucketOwner -> (string)

The Amazon Web Services account ID of the bucket owner.

TableName -> (string)

A prefix for the name of a table DataBrew will create in the database.

Overwrite -> (boolean)

A value that, if true, means that any data in the location specified for output is overwritten with new output. Not supported with DatabaseOptions.

DatabaseOutputs -> (list)

Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write into.

(structure)

Represents a JDBC database output object which defines the output destination for a DataBrew recipe job to write into.

GlueConnectionName -> (string)

The Glue connection that stores the connection information for the target database.

DatabaseOptions -> (structure)

Represents options that specify how and where DataBrew writes the database output generated by recipe jobs.

TempDirectory -> (structure)

Represents an Amazon S3 location (bucket name and object key) where DataBrew can store intermediate results.

Bucket -> (string)

The Amazon S3 bucket name.

Key -> (string)

The unique name of the object in the bucket.

BucketOwner -> (string)

The Amazon Web Services account ID of the bucket owner.

TableName -> (string)

A prefix for the name of a table DataBrew will create in the database.

DatabaseOutputMode -> (string)

The output mode to write into the database. Currently supported option: NEW_TABLE.

RecipeReference -> (structure)

The set of steps processed by the job.

Name -> (string)

The name of the recipe.

RecipeVersion -> (string)

The identifier for the version for the recipe.

StartedBy -> (string)

The Amazon Resource Name (ARN) of the user who initiated the job run.

StartedOn -> (timestamp)

The date and time when the job run began.

JobSample -> (structure)

A sample configuration for profile jobs only, which determines the number of rows on which the profile job is run. If a `JobSample` value isnât provided, the default is used. The default value is CUSTOM_ROWS for the mode parameter and 20,000 for the size parameter.

Mode -> (string)

A value that determines whether the profile job is run on the entire dataset or a specified number of rows. This value must be one of the following:

- FULL_DATASET - The profile job is run on the entire dataset.
- CUSTOM_ROWS - The profile job is run on the number of rows specified in the `Size` parameter.

Size -> (long)

The `Size` parameter is only required when the mode is CUSTOM_ROWS. The profile job is run on the specified number of rows. The maximum value for size is Long.MAX_VALUE.

Long.MAX_VALUE = 9223372036854775807

ValidationConfigurations -> (list)

List of validation configurations that are applied to the profile job run.

(structure)

Configuration for data quality validation. Used to select the Rulesets and Validation Mode to be used in the profile job. When ValidationConfiguration is null, the profile job will run without data quality validation.

RulesetArn -> (string)

The Amazon Resource Name (ARN) for the ruleset to be validated in the profile job. The TargetArn of the selected ruleset should be the same as the Amazon Resource Name (ARN) of the dataset that is associated with the profile job.

ValidationMode -> (string)

Mode of data quality validation. Default mode is âCHECK_ALLâ which verifies all rules defined in the selected ruleset.

NextToken -> (string)

A token that you can use in a subsequent call to retrieve the next set of results.