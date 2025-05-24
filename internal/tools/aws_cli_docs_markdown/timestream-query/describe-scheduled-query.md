# describe-scheduled-queryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-query/describe-scheduled-query.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-query/describe-scheduled-query.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [timestream-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-query/index.html#cli-aws-timestream-query) ]

# describe-scheduled-query

## Description

Provides detailed information about a scheduled query.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/timestream-query-2018-11-01/DescribeScheduledQuery)

## Synopsis

```
describe-scheduled-query
--scheduled-query-arn <value>
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

`--scheduled-query-arn` (string)

The ARN of the scheduled query.

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

ScheduledQuery -> (structure)

The scheduled query.

Arn -> (string)

Scheduled query ARN.

Name -> (string)

Name of the scheduled query.

QueryString -> (string)

The query to be run.

CreationTime -> (timestamp)

Creation time of the scheduled query.

State -> (string)

State of the scheduled query.

PreviousInvocationTime -> (timestamp)

Last time the query was run.

NextInvocationTime -> (timestamp)

The next time the scheduled query is scheduled to run.

ScheduleConfiguration -> (structure)

Schedule configuration.

ScheduleExpression -> (string)

An expression that denotes when to trigger the scheduled query run. This can be a cron expression or a rate expression.

NotificationConfiguration -> (structure)

Notification configuration.

SnsConfiguration -> (structure)

Details about the Amazon Simple Notification Service (SNS) configuration. This field is visible only when SNS Topic is provided when updating the account settings.

TopicArn -> (string)

SNS topic ARN that the scheduled query status notifications will be sent to.

TargetConfiguration -> (structure)

Scheduled query target store configuration.

TimestreamConfiguration -> (structure)

Configuration needed to write data into the Timestream database and table.

DatabaseName -> (string)

Name of Timestream database to which the query result will be written.

TableName -> (string)

Name of Timestream table that the query result will be written to. The table should be within the same database that is provided in Timestream configuration.

TimeColumn -> (string)

Column from query result that should be used as the time column in destination table. Column type for this should be TIMESTAMP.

DimensionMappings -> (list)

This is to allow mapping column(s) from the query result to the dimension in the destination table.

(structure)

This type is used to map column(s) from the query result to a dimension in the destination table.

Name -> (string)

Column name from query result.

DimensionValueType -> (string)

Type for the dimension.

MultiMeasureMappings -> (structure)

Multi-measure mappings.

TargetMultiMeasureName -> (string)

The name of the target multi-measure name in the derived table. This input is required when measureNameColumn is not provided. If MeasureNameColumn is provided, then value from that column will be used as multi-measure name.

MultiMeasureAttributeMappings -> (list)

Required. Attribute mappings to be used for mapping query results to ingest data for multi-measure attributes.

(structure)

Attribute mapping for MULTI value measures.

SourceColumn -> (string)

Source column from where the attribute value is to be read.

TargetMultiMeasureAttributeName -> (string)

Custom name to be used for attribute name in derived table. If not provided, source column name would be used.

MeasureValueType -> (string)

Type of the attribute to be read from the source column.

MixedMeasureMappings -> (list)

Specifies how to map measures to multi-measure records.

(structure)

MixedMeasureMappings are mappings that can be used to ingest data into a mixture of narrow and multi measures in the derived table.

MeasureName -> (string)

Refers to the value of measure_name in a result row. This field is required if MeasureNameColumn is provided.

SourceColumn -> (string)

This field refers to the source column from which measure-value is to be read for result materialization.

TargetMeasureName -> (string)

Target measure name to be used. If not provided, the target measure name by default would be measure-name if provided, or sourceColumn otherwise.

MeasureValueType -> (string)

Type of the value that is to be read from sourceColumn. If the mapping is for MULTI, use MeasureValueType.MULTI.

MultiMeasureAttributeMappings -> (list)

Required when measureValueType is MULTI. Attribute mappings for MULTI value measures.

(structure)

Attribute mapping for MULTI value measures.

SourceColumn -> (string)

Source column from where the attribute value is to be read.

TargetMultiMeasureAttributeName -> (string)

Custom name to be used for attribute name in derived table. If not provided, source column name would be used.

MeasureValueType -> (string)

Type of the attribute to be read from the source column.

MeasureNameColumn -> (string)

Name of the measure column.

ScheduledQueryExecutionRoleArn -> (string)

IAM role that Timestream uses to run the schedule query.

KmsKeyId -> (string)

A customer provided KMS key used to encrypt the scheduled query resource.

ErrorReportConfiguration -> (structure)

Error-reporting configuration for the scheduled query.

S3Configuration -> (structure)

The S3 configuration for the error reports.

BucketName -> (string)

Name of the S3 bucket under which error reports will be created.

ObjectKeyPrefix -> (string)

Prefix for the error report key. Timestream by default adds the following prefix to the error report path.

EncryptionOption -> (string)

Encryption at rest options for the error reports. If no encryption option is specified, Timestream will choose SSE_S3 as default.

LastRunSummary -> (structure)

Runtime summary for the last scheduled query run.

InvocationTime -> (timestamp)

InvocationTime for this run. This is the time at which the query is scheduled to run. Parameter `@scheduled_runtime` can be used in the query to get the value.

TriggerTime -> (timestamp)

The actual time when the query was run.

RunStatus -> (string)

The status of a scheduled query run.

ExecutionStats -> (structure)

Runtime statistics for a scheduled run.

ExecutionTimeInMillis -> (long)

Total time, measured in milliseconds, that was needed for the scheduled query run to complete.

DataWrites -> (long)

Data writes metered for records ingested in a single scheduled query run.

BytesMetered -> (long)

Bytes metered for a single scheduled query run.

CumulativeBytesScanned -> (long)

Bytes scanned for a single scheduled query run.

RecordsIngested -> (long)

The number of records ingested for a single scheduled query run.

QueryResultRows -> (long)

Number of rows present in the output from running a query before ingestion to destination data source.

QueryInsightsResponse -> (structure)

Provides various insights and metrics related to the run summary of the scheduled query.

QuerySpatialCoverage -> (structure)

Provides insights into the spatial coverage of the query, including the table with sub-optimal (max) spatial pruning. This information can help you identify areas for improvement in your partitioning strategy to enhance spatial pruning.

Max -> (structure)

Provides insights into the spatial coverage of the executed query and the table with the most inefficient spatial pruning.

- `Value` â The maximum ratio of spatial coverage.
- `TableArn` â The Amazon Resource Name (ARN) of the table with sub-optimal spatial pruning.
- `PartitionKey` â The partition key used for partitioning, which can be a default `measure_name` or a CDPK.

Value -> (double)

The maximum ratio of spatial coverage.

TableArn -> (string)

The Amazon Resource Name (ARN) of the table with the most sub-optimal spatial pruning.

PartitionKey -> (list)

The partition key used for partitioning, which can be a default `measure_name` or a [customer defined partition key](https://docs.aws.amazon.com/timestream/latest/developerguide/customer-defined-partition-keys.html) .

(string)

QueryTemporalRange -> (structure)

Provides insights into the temporal range of the query, including the table with the largest (max) time range. Following are some of the potential options for optimizing time-based pruning:

- Add missing time-predicates.
- Remove functions around the time predicates.
- Add time predicates to all the sub-queries.

Max -> (structure)

Encapsulates the following properties that provide insights into the most sub-optimal performing table on the temporal axis:

- `Value` â The maximum duration in nanoseconds between the start and end of the query.
- `TableArn` â The Amazon Resource Name (ARN) of the table which is queried with the largest time range.

Value -> (long)

The maximum duration in nanoseconds between the start and end of the query.

TableArn -> (string)

The Amazon Resource Name (ARN) of the table which is queried with the largest time range.

QueryTableCount -> (long)

Indicates the number of tables in the query.

OutputRows -> (long)

Indicates the total number of rows returned as part of the query result set. You can use this data to validate if the number of rows in the result set have changed as part of the query tuning exercise.

OutputBytes -> (long)

Indicates the size of query result set in bytes. You can use this data to validate if the result set has changed as part of the query tuning exercise.

ErrorReportLocation -> (structure)

S3 location for error report.

S3ReportLocation -> (structure)

The S3 location where error reports are written.

BucketName -> (string)

S3 bucket name.

ObjectKey -> (string)

S3 key.

FailureReason -> (string)

Error message for the scheduled query in case of failure. You might have to look at the error report to get more detailed error reasons.

RecentlyFailedRuns -> (list)

Runtime summary for the last five failed scheduled query runs.

(structure)

Run summary for the scheduled query

InvocationTime -> (timestamp)

InvocationTime for this run. This is the time at which the query is scheduled to run. Parameter `@scheduled_runtime` can be used in the query to get the value.

TriggerTime -> (timestamp)

The actual time when the query was run.

RunStatus -> (string)

The status of a scheduled query run.

ExecutionStats -> (structure)

Runtime statistics for a scheduled run.

ExecutionTimeInMillis -> (long)

Total time, measured in milliseconds, that was needed for the scheduled query run to complete.

DataWrites -> (long)

Data writes metered for records ingested in a single scheduled query run.

BytesMetered -> (long)

Bytes metered for a single scheduled query run.

CumulativeBytesScanned -> (long)

Bytes scanned for a single scheduled query run.

RecordsIngested -> (long)

The number of records ingested for a single scheduled query run.

QueryResultRows -> (long)

Number of rows present in the output from running a query before ingestion to destination data source.

QueryInsightsResponse -> (structure)

Provides various insights and metrics related to the run summary of the scheduled query.

QuerySpatialCoverage -> (structure)

Provides insights into the spatial coverage of the query, including the table with sub-optimal (max) spatial pruning. This information can help you identify areas for improvement in your partitioning strategy to enhance spatial pruning.

Max -> (structure)

Provides insights into the spatial coverage of the executed query and the table with the most inefficient spatial pruning.

- `Value` â The maximum ratio of spatial coverage.
- `TableArn` â The Amazon Resource Name (ARN) of the table with sub-optimal spatial pruning.
- `PartitionKey` â The partition key used for partitioning, which can be a default `measure_name` or a CDPK.

Value -> (double)

The maximum ratio of spatial coverage.

TableArn -> (string)

The Amazon Resource Name (ARN) of the table with the most sub-optimal spatial pruning.

PartitionKey -> (list)

The partition key used for partitioning, which can be a default `measure_name` or a [customer defined partition key](https://docs.aws.amazon.com/timestream/latest/developerguide/customer-defined-partition-keys.html) .

(string)

QueryTemporalRange -> (structure)

Provides insights into the temporal range of the query, including the table with the largest (max) time range. Following are some of the potential options for optimizing time-based pruning:

- Add missing time-predicates.
- Remove functions around the time predicates.
- Add time predicates to all the sub-queries.

Max -> (structure)

Encapsulates the following properties that provide insights into the most sub-optimal performing table on the temporal axis:

- `Value` â The maximum duration in nanoseconds between the start and end of the query.
- `TableArn` â The Amazon Resource Name (ARN) of the table which is queried with the largest time range.

Value -> (long)

The maximum duration in nanoseconds between the start and end of the query.

TableArn -> (string)

The Amazon Resource Name (ARN) of the table which is queried with the largest time range.

QueryTableCount -> (long)

Indicates the number of tables in the query.

OutputRows -> (long)

Indicates the total number of rows returned as part of the query result set. You can use this data to validate if the number of rows in the result set have changed as part of the query tuning exercise.

OutputBytes -> (long)

Indicates the size of query result set in bytes. You can use this data to validate if the result set has changed as part of the query tuning exercise.

ErrorReportLocation -> (structure)

S3 location for error report.

S3ReportLocation -> (structure)

The S3 location where error reports are written.

BucketName -> (string)

S3 bucket name.

ObjectKey -> (string)

S3 key.

FailureReason -> (string)

Error message for the scheduled query in case of failure. You might have to look at the error report to get more detailed error reasons.