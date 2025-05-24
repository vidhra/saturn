# get-crawlerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-crawler.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-crawler.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# get-crawler

## Description

Retrieves metadata for a specified crawler.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetCrawler)

## Synopsis

```
get-crawler
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

The name of the crawler to retrieve metadata for.

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

Crawler -> (structure)

The metadata for the specified crawler.

Name -> (string)

The name of the crawler.

Role -> (string)

The Amazon Resource Name (ARN) of an IAM role thatâs used to access customer resources, such as Amazon Simple Storage Service (Amazon S3) data.

Targets -> (structure)

A collection of targets to crawl.

S3Targets -> (list)

Specifies Amazon Simple Storage Service (Amazon S3) targets.

(structure)

Specifies a data store in Amazon Simple Storage Service (Amazon S3).

Path -> (string)

The path to the Amazon S3 target.

Exclusions -> (list)

A list of glob patterns used to exclude from the crawl. For more information, see [Catalog Tables with a Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) .

(string)

ConnectionName -> (string)

The name of a connection which allows a job or crawler to access data in Amazon S3 within an Amazon Virtual Private Cloud environment (Amazon VPC).

SampleSize -> (integer)

Sets the number of files in each leaf folder to be crawled when crawling sample files in a dataset. If not set, all the files are crawled. A valid value is an integer between 1 and 249.

EventQueueArn -> (string)

A valid Amazon SQS ARN. For example, `arn:aws:sqs:region:account:sqs` .

DlqEventQueueArn -> (string)

A valid Amazon dead-letter SQS ARN. For example, `arn:aws:sqs:region:account:deadLetterQueue` .

JdbcTargets -> (list)

Specifies JDBC targets.

(structure)

Specifies a JDBC data store to crawl.

ConnectionName -> (string)

The name of the connection to use to connect to the JDBC target.

Path -> (string)

The path of the JDBC target.

Exclusions -> (list)

A list of glob patterns used to exclude from the crawl. For more information, see [Catalog Tables with a Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) .

(string)

EnableAdditionalMetadata -> (list)

Specify a value of `RAWTYPES` or `COMMENTS` to enable additional metadata in table responses. `RAWTYPES` provides the native-level datatype. `COMMENTS` provides comments associated with a column or table in the database.

If you do not need additional metadata, keep the field empty.

(string)

MongoDBTargets -> (list)

Specifies Amazon DocumentDB or MongoDB targets.

(structure)

Specifies an Amazon DocumentDB or MongoDB data store to crawl.

ConnectionName -> (string)

The name of the connection to use to connect to the Amazon DocumentDB or MongoDB target.

Path -> (string)

The path of the Amazon DocumentDB or MongoDB target (database/collection).

ScanAll -> (boolean)

Indicates whether to scan all the records, or to sample rows from the table. Scanning all the records can take a long time when the table is not a high throughput table.

A value of `true` means to scan all records, while a value of `false` means to sample the records. If no value is specified, the value defaults to `true` .

DynamoDBTargets -> (list)

Specifies Amazon DynamoDB targets.

(structure)

Specifies an Amazon DynamoDB table to crawl.

Path -> (string)

The name of the DynamoDB table to crawl.

scanAll -> (boolean)

Indicates whether to scan all the records, or to sample rows from the table. Scanning all the records can take a long time when the table is not a high throughput table.

A value of `true` means to scan all records, while a value of `false` means to sample the records. If no value is specified, the value defaults to `true` .

scanRate -> (double)

The percentage of the configured read capacity units to use by the Glue crawler. Read capacity units is a term defined by DynamoDB, and is a numeric value that acts as rate limiter for the number of reads that can be performed on that table per second.

The valid values are null or a value between 0.1 to 1.5. A null value is used when user does not provide a value, and defaults to 0.5 of the configured Read Capacity Unit (for provisioned tables), or 0.25 of the max configured Read Capacity Unit (for tables using on-demand mode).

CatalogTargets -> (list)

Specifies Glue Data Catalog targets.

(structure)

Specifies an Glue Data Catalog target.

DatabaseName -> (string)

The name of the database to be synchronized.

Tables -> (list)

A list of the tables to be synchronized.

(string)

ConnectionName -> (string)

The name of the connection for an Amazon S3-backed Data Catalog table to be a target of the crawl when using a `Catalog` connection type paired with a `NETWORK` Connection type.

EventQueueArn -> (string)

A valid Amazon SQS ARN. For example, `arn:aws:sqs:region:account:sqs` .

DlqEventQueueArn -> (string)

A valid Amazon dead-letter SQS ARN. For example, `arn:aws:sqs:region:account:deadLetterQueue` .

DeltaTargets -> (list)

Specifies Delta data store targets.

(structure)

Specifies a Delta data store to crawl one or more Delta tables.

DeltaTables -> (list)

A list of the Amazon S3 paths to the Delta tables.

(string)

ConnectionName -> (string)

The name of the connection to use to connect to the Delta table target.

WriteManifest -> (boolean)

Specifies whether to write the manifest files to the Delta table path.

CreateNativeDeltaTable -> (boolean)

Specifies whether the crawler will create native tables, to allow integration with query engines that support querying of the Delta transaction log directly.

IcebergTargets -> (list)

Specifies Apache Iceberg data store targets.

(structure)

Specifies an Apache Iceberg data source where Iceberg tables are stored in Amazon S3.

Paths -> (list)

One or more Amazon S3 paths that contains Iceberg metadata folders as `s3://bucket/prefix` .

(string)

ConnectionName -> (string)

The name of the connection to use to connect to the Iceberg target.

Exclusions -> (list)

A list of glob patterns used to exclude from the crawl. For more information, see [Catalog Tables with a Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) .

(string)

MaximumTraversalDepth -> (integer)

The maximum depth of Amazon S3 paths that the crawler can traverse to discover the Iceberg metadata folder in your Amazon S3 path. Used to limit the crawler run time.

HudiTargets -> (list)

Specifies Apache Hudi data store targets.

(structure)

Specifies an Apache Hudi data source.

Paths -> (list)

An array of Amazon S3 location strings for Hudi, each indicating the root folder with which the metadata files for a Hudi table resides. The Hudi folder may be located in a child folder of the root folder.

The crawler will scan all folders underneath a path for a Hudi folder.

(string)

ConnectionName -> (string)

The name of the connection to use to connect to the Hudi target. If your Hudi files are stored in buckets that require VPC authorization, you can set their connection properties here.

Exclusions -> (list)

A list of glob patterns used to exclude from the crawl. For more information, see [Catalog Tables with a Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) .

(string)

MaximumTraversalDepth -> (integer)

The maximum depth of Amazon S3 paths that the crawler can traverse to discover the Hudi metadata folder in your Amazon S3 path. Used to limit the crawler run time.

DatabaseName -> (string)

The name of the database in which the crawlerâs output is stored.

Description -> (string)

A description of the crawler.

Classifiers -> (list)

A list of UTF-8 strings that specify the custom classifiers that are associated with the crawler.

(string)

RecrawlPolicy -> (structure)

A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run.

RecrawlBehavior -> (string)

Specifies whether to crawl the entire dataset again or to crawl only folders that were added since the last crawler run.

A value of `CRAWL_EVERYTHING` specifies crawling the entire dataset again.

A value of `CRAWL_NEW_FOLDERS_ONLY` specifies crawling only folders that were added since the last crawler run.

A value of `CRAWL_EVENT_MODE` specifies crawling only the changes identified by Amazon S3 events.

SchemaChangePolicy -> (structure)

The policy that specifies update and delete behaviors for the crawler.

UpdateBehavior -> (string)

The update behavior when the crawler finds a changed schema.

DeleteBehavior -> (string)

The deletion behavior when the crawler finds a deleted object.

LineageConfiguration -> (structure)

A configuration that specifies whether data lineage is enabled for the crawler.

CrawlerLineageSettings -> (string)

Specifies whether data lineage is enabled for the crawler. Valid values are:

- ENABLE: enables data lineage for the crawler
- DISABLE: disables data lineage for the crawler

State -> (string)

Indicates whether the crawler is running, or whether a run is pending.

TablePrefix -> (string)

The prefix added to the names of tables that are created.

Schedule -> (structure)

For scheduled crawlers, the schedule when the crawler runs.

ScheduleExpression -> (string)

A `cron` expression used to specify the schedule (see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html) . For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)` .

State -> (string)

The state of the schedule.

CrawlElapsedTime -> (long)

If the crawler is running, contains the total time elapsed since the last crawl began.

CreationTime -> (timestamp)

The time that the crawler was created.

LastUpdated -> (timestamp)

The time that the crawler was last updated.

LastCrawl -> (structure)

The status of the last crawl, and potentially error information if an error occurred.

Status -> (string)

Status of the last crawl.

ErrorMessage -> (string)

If an error occurred, the error information about the last crawl.

LogGroup -> (string)

The log group for the last crawl.

LogStream -> (string)

The log stream for the last crawl.

MessagePrefix -> (string)

The prefix for a message about this crawl.

StartTime -> (timestamp)

The time at which the crawl started.

Version -> (long)

The version of the crawler.

Configuration -> (string)

Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawlerâs behavior. For more information, see [Setting crawler configuration options](https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html) .

CrawlerSecurityConfiguration -> (string)

The name of the `SecurityConfiguration` structure to be used by this crawler.

LakeFormationConfiguration -> (structure)

Specifies whether the crawler should use Lake Formation credentials for the crawler instead of the IAM role credentials.

UseLakeFormationCredentials -> (boolean)

Specifies whether to use Lake Formation credentials for the crawler instead of the IAM role credentials.

AccountId -> (string)

Required for cross account crawls. For same account crawls as the target data, this can be left as null.