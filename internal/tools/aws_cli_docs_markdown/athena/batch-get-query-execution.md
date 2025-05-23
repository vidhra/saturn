# batch-get-query-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/batch-get-query-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/batch-get-query-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [athena](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/index.html#cli-aws-athena) ]

# batch-get-query-execution

## Description

Returns the details of a single query execution or a list of up to 50 query executions, which you provide as an array of query execution ID strings. Requires you to have access to the workgroup in which the queries ran. To get a list of query execution IDs, use  ListQueryExecutionsInput$WorkGroup . Query executions differ from named (saved) queries. Use  BatchGetNamedQueryInput to get details about named queries.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/BatchGetQueryExecution)

## Synopsis

```
batch-get-query-execution
--query-execution-ids <value>
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

`--query-execution-ids` (list)

An array of query execution IDs.

(string)

Syntax:

```
"string" "string" ...
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

**To return information about one or more query executions**

The following `batch-get-query-execution` example returns query execution information for the queries that have the specified query IDs.

```
aws athena batch-get-query-execution \
    --query-execution-ids a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 a1b2c3d4-5678-90ab-cdef-EXAMPLE22222
```

Output:

```
{
    "QueryExecutions": [
        {
            "QueryExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "Query": "create database if not exists webdata",
            "StatementType": "DDL",
            "ResultConfiguration": {
                "OutputLocation": "s3://amzn-s3-demo-bucket/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111.txt"
            },
            "QueryExecutionContext": {},
            "Status": {
                "State": "SUCCEEDED",
                "SubmissionDateTime": 1593470720.592,
                "CompletionDateTime": 1593470720.902
            },
            "Statistics": {
                "EngineExecutionTimeInMillis": 232,
                "DataScannedInBytes": 0,
                "TotalExecutionTimeInMillis": 310,
            "ResultConfiguration": {

                "QueryQueueTimeInMillis": 50,
                "ServiceProcessingTimeInMillis": 28
            },
            "WorkGroup": "AthenaAdmin"
        },
        {
            "QueryExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "Query": "select date, location, browser, uri, status from cloudfront_logs where method = 'GET' and status = 200 and location like 'SFO%' limit 10",
            "StatementType": "DML",
            "ResultConfiguration": {
                "OutputLocation": "s3://amzn-s3-demo-bucket/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222.csv"
            },
            "QueryExecutionContext": {
                "Database": "mydatabase",
                "Catalog": "awsdatacatalog"
            },
            "Status": {
                "State": "SUCCEEDED",
                "SubmissionDateTime": 1593469842.665,
                "CompletionDateTime": 1593469846.486
            },
            "Statistics": {
                "EngineExecutionTimeInMillis": 3600,
                "DataScannedInBytes": 203089,
                "TotalExecutionTimeInMillis": 3821,
                "QueryQueueTimeInMillis": 267,
                "QueryPlanningTimeInMillis": 1175
            },
            "WorkGroup": "AthenaAdmin"
        }
    ],
    "UnprocessedQueryExecutionIds": []
}
```

For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html) in the *Amazon Athena User Guide*.

## Output

QueryExecutions -> (list)

Information about a query execution.

(structure)

Information about a single instance of a query execution.

QueryExecutionId -> (string)

The unique identifier for each query execution.

Query -> (string)

The SQL query statements which the query execution ran.

StatementType -> (string)

The type of query statement that was run. `DDL` indicates DDL query statements. `DML` indicates DML (Data Manipulation Language) query statements, such as `CREATE TABLE AS SELECT` . `UTILITY` indicates query statements other than DDL and DML, such as `SHOW CREATE TABLE` , `EXPLAIN` , `DESCRIBE` , or `SHOW TABLES` .

ResultConfiguration -> (structure)

The location in Amazon S3 where query and calculation results are stored and the encryption option, if any, used for query results. These are known as âclient-side settingsâ. If workgroup settings override client-side settings, then the query uses the location for the query results and the encryption configuration that are specified for the workgroup.

OutputLocation -> (string)

The location in Amazon S3 where your query and calculation results are stored, such as `s3://path/to/query/bucket/` . To run the query, you must specify the query results location using one of the ways: either for individual queries using either this setting (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is set, Athena issues an error that no output location is provided. If workgroup settings override client-side settings, then the query uses the settings specified for the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

EncryptionConfiguration -> (structure)

If query and calculation results are encrypted in Amazon S3, indicates the encryption option used (for example, `SSE_KMS` or `CSE_KMS` ) and key information. This is a client-side setting. If workgroup settings override client-side settings, then the query uses the encryption configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration and [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html) .

EncryptionOption -> (string)

Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (`SSE_S3` ), server-side encryption with KMS-managed keys (`SSE_KMS` ), or client-side encryption with KMS-managed keys (`CSE_KMS` ) is used.

If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroupâs setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.

KmsKey -> (string)

For `SSE_KMS` and `CSE_KMS` , this is the KMS key ARN or ID.

ExpectedBucketOwner -> (string)

The Amazon Web Services account ID that you expect to be the owner of the Amazon S3 bucket specified by  ResultConfiguration$OutputLocation . If set, Athena uses the value for `ExpectedBucketOwner` when it makes Amazon S3 calls to your specified output location. If the `ExpectedBucketOwner` Amazon Web Services account ID does not match the actual owner of the Amazon S3 bucket, the call fails with a permissions error.

This is a client-side setting. If workgroup settings override client-side settings, then the query uses the `ExpectedBucketOwner` setting that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration and [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html) .

AclConfiguration -> (structure)

Indicates that an Amazon S3 canned ACL should be set to control ownership of stored query results. Currently the only supported canned ACL is `BUCKET_OWNER_FULL_CONTROL` . This is a client-side setting. If workgroup settings override client-side settings, then the query uses the ACL configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. For more information, see  WorkGroupConfiguration$EnforceWorkGroupConfiguration and [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html) .

S3AclOption -> (string)

The Amazon S3 canned ACL that Athena should specify when storing query results, including data files inserted by Athena as the result of statements like CTAS or INSERT INTO. Currently the only supported canned ACL is `BUCKET_OWNER_FULL_CONTROL` . If a query runs in a workgroup and the workgroup overrides client-side settings, then the Amazon S3 canned ACL specified in the workgroupâs settings is used for all queries that run in the workgroup. For more information about Amazon S3 canned ACLs, see [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl) in the *Amazon S3 User Guide* .

ResultReuseConfiguration -> (structure)

Specifies the query result reuse behavior that was used for the query.

ResultReuseByAgeConfiguration -> (structure)

Specifies whether previous query results are reused, and if so, their maximum age.

Enabled -> (boolean)

True if previous query results can be reused when the query is run; otherwise, false. The default is false.

MaxAgeInMinutes -> (integer)

Specifies, in minutes, the maximum age of a previous query result that Athena should consider for reuse. The default is 60.

QueryExecutionContext -> (structure)

The database in which the query execution occurred.

Database -> (string)

The name of the database used in the query execution. The database must exist in the catalog.

Catalog -> (string)

The name of the data catalog used in the query execution.

Status -> (structure)

The completion date, current state, submission time, and state change reason (if applicable) for the query execution.

State -> (string)

The state of query execution. `QUEUED` indicates that the query has been submitted to the service, and Athena will execute the query as soon as resources are available. `RUNNING` indicates that the query is in execution phase. `SUCCEEDED` indicates that the query completed without errors. `FAILED` indicates that the query experienced an error and did not complete processing. `CANCELLED` indicates that a user input interrupted query execution.

### Note

Athena automatically retries your queries in cases of certain transient errors. As a result, you may see the query state transition from `RUNNING` or `FAILED` to `QUEUED` .

StateChangeReason -> (string)

Further detail about the status of the query.

SubmissionDateTime -> (timestamp)

The date and time that the query was submitted.

CompletionDateTime -> (timestamp)

The date and time that the query completed.

AthenaError -> (structure)

Provides information about an Athena query error.

ErrorCategory -> (integer)

An integer value that specifies the category of a query failure error. The following list shows the category for each integer value.

**1** - System

**2** - User

**3** - Other

ErrorType -> (integer)

An integer value that provides specific information about an Athena query error. For the meaning of specific values, see the [Error Type Reference](https://docs.aws.amazon.com/athena/latest/ug/error-reference.html#error-reference-error-type-reference) in the *Amazon Athena User Guide* .

Retryable -> (boolean)

True if the query might succeed if resubmitted.

ErrorMessage -> (string)

Contains a short description of the error that occurred.

Statistics -> (structure)

Query execution statistics, such as the amount of data scanned, the amount of time that the query took to process, and the type of statement that was run.

EngineExecutionTimeInMillis -> (long)

The number of milliseconds that the query took to execute.

DataScannedInBytes -> (long)

The number of bytes in the data that was queried.

DataManifestLocation -> (string)

The location and file name of a data manifest file. The manifest file is saved to the Athena query results location in Amazon S3. The manifest file tracks files that the query wrote to Amazon S3. If the query fails, the manifest file also tracks files that the query intended to write. The manifest is useful for identifying orphaned files resulting from a failed query. For more information, see [Working with Query Results, Output Files, and Query History](https://docs.aws.amazon.com/athena/latest/ug/querying.html) in the *Amazon Athena User Guide* .

TotalExecutionTimeInMillis -> (long)

The number of milliseconds that Athena took to run the query.

QueryQueueTimeInMillis -> (long)

The number of milliseconds that the query was in your query queue waiting for resources. Note that if transient errors occur, Athena might automatically add the query back to the queue.

ServicePreProcessingTimeInMillis -> (long)

The number of milliseconds that Athena took to preprocess the query before submitting the query to the query engine.

QueryPlanningTimeInMillis -> (long)

The number of milliseconds that Athena took to plan the query processing flow. This includes the time spent retrieving table partitions from the data source. Note that because the query engine performs the query planning, query planning time is a subset of engine processing time.

ServiceProcessingTimeInMillis -> (long)

The number of milliseconds that Athena took to finalize and publish the query results after the query engine finished running the query.

ResultReuseInformation -> (structure)

Contains information about whether previous query results were reused for the query.

ReusedPreviousResult -> (boolean)

True if a previous query result was reused; false if the result was generated from a new run of the query.

WorkGroup -> (string)

The name of the workgroup in which the query ran.

EngineVersion -> (structure)

The engine version that executed the query.

SelectedEngineVersion -> (string)

The engine version requested by the user. Possible values are determined by the output of `ListEngineVersions` , including AUTO. The default is AUTO.

EffectiveEngineVersion -> (string)

Read only. The engine version on which the query runs. If the user requests a valid engine version other than Auto, the effective engine version is the same as the engine version that the user requested. If the user requests Auto, the effective engine version is chosen by Athena. When a request to update the engine version is made by a `CreateWorkGroup` or `UpdateWorkGroup` operation, the `EffectiveEngineVersion` field is ignored.

ExecutionParameters -> (list)

A list of values for the parameters in a query. The values are applied sequentially to the parameters in the query in the order in which the parameters occur. The list of parameters is not returned in the response.

(string)

SubstatementType -> (string)

The kind of query statement that was run.

QueryResultsS3AccessGrantsConfiguration -> (structure)

Specifies whether Amazon S3 access grants are enabled for query results.

EnableS3AccessGrants -> (boolean)

Specifies whether Amazon S3 access grants are enabled for query results.

CreateUserLevelPrefix -> (boolean)

When enabled, appends the user ID as an Amazon S3 path prefix to the query result output location.

AuthenticationType -> (string)

The authentication type used for Amazon S3 access grants. Currently, only `DIRECTORY_IDENTITY` is supported.

UnprocessedQueryExecutionIds -> (list)

Information about the query executions that failed to run.

(structure)

Describes a query execution that failed to process.

QueryExecutionId -> (string)

The unique identifier of the query execution.

ErrorCode -> (string)

The error code returned when the query execution failed to process, if applicable.

ErrorMessage -> (string)

The error message returned when the query execution failed to process, if applicable.