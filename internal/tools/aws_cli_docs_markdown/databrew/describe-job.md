# describe-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/describe-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/describe-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [databrew](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/index.html#cli-aws-databrew) ]

# describe-job

## Description

Returns the definition of a specific DataBrew job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/databrew-2017-07-25/DescribeJob)

## Synopsis

```
describe-job
--name <value>
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

`--name` (string)

The name of the job to be described.

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

CreateDate -> (timestamp)

The date and time that the job was created.

CreatedBy -> (string)

The identifier (user name) of the user associated with the creation of the job.

DatasetName -> (string)

The dataset that the job acts upon.

EncryptionKeyArn -> (string)

The Amazon Resource Name (ARN) of an encryption key that is used to protect the job.

EncryptionMode -> (string)

The encryption mode for the job, which can be one of the following:

- `SSE-KMS` - Server-side encryption with keys managed by KMS.
- `SSE-S3` - Server-side encryption with keys managed by Amazon S3.

Name -> (string)

The name of the job.

Type -> (string)

The job type, which must be one of the following:

- `PROFILE` - The job analyzes the dataset to determine its size, data types, data distribution, and more.
- `RECIPE` - The job applies one or more transformations to a dataset.

LastModifiedBy -> (string)

The identifier (user name) of the user who last modified the job.

LastModifiedDate -> (timestamp)

The date and time that the job was last modified.

LogSubscription -> (string)

Indicates whether Amazon CloudWatch logging is enabled for this job.

MaxCapacity -> (integer)

The maximum number of compute nodes that DataBrew can consume when the job processes data.

MaxRetries -> (integer)

The maximum number of times to retry the job after a job run fails.

Outputs -> (list)

One or more artifacts that represent the output from running the job.

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

ProjectName -> (string)

The DataBrew project associated with this job.

ProfileConfiguration -> (structure)

Configuration for profile jobs. Used to select columns, do evaluations, and override default parameters of evaluations. When configuration is null, the profile job will run with default settings.

DatasetStatisticsConfiguration -> (structure)

Configuration for inter-column evaluations. Configuration can be used to select evaluations and override parameters of evaluations. When configuration is undefined, the profile job will run all supported inter-column evaluations.

IncludedStatistics -> (list)

List of included evaluations. When the list is undefined, all supported evaluations will be included.

(string)

Overrides -> (list)

List of overrides for evaluations.

(structure)

Override of a particular evaluation for a profile job.

Statistic -> (string)

The name of an evaluation

Parameters -> (map)

A map that includes overrides of an evaluationâs parameters.

key -> (string)

value -> (string)

ProfileColumns -> (list)

List of column selectors. ProfileColumns can be used to select columns from the dataset. When ProfileColumns is undefined, the profile job will profile all supported columns.

(structure)

Selector of a column from a dataset for profile job configuration. One selector includes either a column name or a regular expression.

Regex -> (string)

A regular expression for selecting a column from a dataset.

Name -> (string)

The name of a column from a dataset.

ColumnStatisticsConfigurations -> (list)

List of configurations for column evaluations. ColumnStatisticsConfigurations are used to select evaluations and override parameters of evaluations for particular columns. When ColumnStatisticsConfigurations is undefined, the profile job will profile all supported columns and run all supported evaluations.

(structure)

Configuration for column evaluations for a profile job. ColumnStatisticsConfiguration can be used to select evaluations and override parameters of evaluations for particular columns.

Selectors -> (list)

List of column selectors. Selectors can be used to select columns from the dataset. When selectors are undefined, configuration will be applied to all supported columns.

(structure)

Selector of a column from a dataset for profile job configuration. One selector includes either a column name or a regular expression.

Regex -> (string)

A regular expression for selecting a column from a dataset.

Name -> (string)

The name of a column from a dataset.

Statistics -> (structure)

Configuration for evaluations. Statistics can be used to select evaluations and override parameters of evaluations.

IncludedStatistics -> (list)

List of included evaluations. When the list is undefined, all supported evaluations will be included.

(string)

Overrides -> (list)

List of overrides for evaluations.

(structure)

Override of a particular evaluation for a profile job.

Statistic -> (string)

The name of an evaluation

Parameters -> (map)

A map that includes overrides of an evaluationâs parameters.

key -> (string)

value -> (string)

EntityDetectorConfiguration -> (structure)

Configuration of entity detection for a profile job. When undefined, entity detection is disabled.

EntityTypes -> (list)

Entity types to detect. Can be any of the following:

- USA_SSN
- EMAIL
- USA_ITIN
- USA_PASSPORT_NUMBER
- PHONE_NUMBER
- USA_DRIVING_LICENSE
- BANK_ACCOUNT
- CREDIT_CARD
- IP_ADDRESS
- MAC_ADDRESS
- USA_DEA_NUMBER
- USA_HCPCS_CODE
- USA_NATIONAL_PROVIDER_IDENTIFIER
- USA_NATIONAL_DRUG_CODE
- USA_HEALTH_INSURANCE_CLAIM_NUMBER
- USA_MEDICARE_BENEFICIARY_IDENTIFIER
- USA_CPT_CODE
- PERSON_NAME
- DATE

The Entity type group USA_ALL is also supported, and includes all of the above entity types except PERSON_NAME and DATE.

(string)

AllowedStatistics -> (list)

Configuration of statistics that are allowed to be run on columns that contain detected entities. When undefined, no statistics will be computed on columns that contain detected entities.

(structure)

Configuration of statistics that are allowed to be run on columns that contain detected entities. When undefined, no statistics will be computed on columns that contain detected entities.

Statistics -> (list)

One or more column statistics to allow for columns that contain detected entities.

(string)

ValidationConfigurations -> (list)

List of validation configurations that are applied to the profile job.

(structure)

Configuration for data quality validation. Used to select the Rulesets and Validation Mode to be used in the profile job. When ValidationConfiguration is null, the profile job will run without data quality validation.

RulesetArn -> (string)

The Amazon Resource Name (ARN) for the ruleset to be validated in the profile job. The TargetArn of the selected ruleset should be the same as the Amazon Resource Name (ARN) of the dataset that is associated with the profile job.

ValidationMode -> (string)

Mode of data quality validation. Default mode is âCHECK_ALLâ which verifies all rules defined in the selected ruleset.

RecipeReference -> (structure)

Represents the name and version of a DataBrew recipe.

Name -> (string)

The name of the recipe.

RecipeVersion -> (string)

The identifier for the version for the recipe.

ResourceArn -> (string)

The Amazon Resource Name (ARN) of the job.

RoleArn -> (string)

The ARN of the Identity and Access Management (IAM) role to be assumed when DataBrew runs the job.

Tags -> (map)

Metadata tags associated with this job.

key -> (string)

value -> (string)

Timeout -> (integer)

The jobâs timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of `TIMEOUT` .

JobSample -> (structure)

Sample configuration for profile jobs only. Determines the number of rows on which the profile job will be executed.

Mode -> (string)

A value that determines whether the profile job is run on the entire dataset or a specified number of rows. This value must be one of the following:

- FULL_DATASET - The profile job is run on the entire dataset.
- CUSTOM_ROWS - The profile job is run on the number of rows specified in the `Size` parameter.

Size -> (long)

The `Size` parameter is only required when the mode is CUSTOM_ROWS. The profile job is run on the specified number of rows. The maximum value for size is Long.MAX_VALUE.

Long.MAX_VALUE = 9223372036854775807