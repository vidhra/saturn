# get-query-runtime-statisticsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-query-runtime-statistics.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-query-runtime-statistics.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [athena](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/index.html#cli-aws-athena) ]

# get-query-runtime-statistics

## Description

Returns query execution runtime statistics related to a single execution of a query if you have access to the workgroup in which the query ran. Statistics from the `Timeline` section of the response object are available as soon as  QueryExecutionStatus$State is in a SUCCEEDED or FAILED state. The remaining non-timeline statistics in the response (like stage-level input and output row count and data size) are updated asynchronously and may not be available immediately after a query completes. The non-timeline statistics are also not included when a query has row-level filters defined in Lake Formation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/GetQueryRuntimeStatistics)

## Synopsis

```
get-query-runtime-statistics
--query-execution-id <value>
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

`--query-execution-id` (string)

The unique ID of the query execution.

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

QueryRuntimeStatistics -> (structure)

Runtime statistics about the query execution.

Timeline -> (structure)

Timeline statistics such as query queue time, planning time, execution time, service processing time, and total execution time.

QueryQueueTimeInMillis -> (long)

The number of milliseconds that the query was in your query queue waiting for resources. Note that if transient errors occur, Athena might automatically add the query back to the queue.

ServicePreProcessingTimeInMillis -> (long)

The number of milliseconds that Athena spends on preprocessing before it submits the query to the engine.

QueryPlanningTimeInMillis -> (long)

The number of milliseconds that Athena took to plan the query processing flow. This includes the time spent retrieving table partitions from the data source. Note that because the query engine performs the query planning, query planning time is a subset of engine processing time.

EngineExecutionTimeInMillis -> (long)

The number of milliseconds that the query took to execute.

ServiceProcessingTimeInMillis -> (long)

The number of milliseconds that Athena took to finalize and publish the query results after the query engine finished running the query.

TotalExecutionTimeInMillis -> (long)

The number of milliseconds that Athena took to run the query.

Rows -> (structure)

Statistics such as input rows and bytes read by the query, rows and bytes output by the query, and the number of rows written by the query.

InputRows -> (long)

The number of rows read to execute the query.

InputBytes -> (long)

The number of bytes read to execute the query.

OutputBytes -> (long)

The number of bytes returned by the query.

OutputRows -> (long)

The number of rows returned by the query.

OutputStage -> (structure)

Stage statistics such as input and output rows and bytes, execution time, and stage state. This information also includes substages and the query stage plan.

StageId -> (long)

The identifier for a stage.

State -> (string)

State of the stage after query execution.

OutputBytes -> (long)

The number of bytes output from the stage after execution.

OutputRows -> (long)

The number of rows output from the stage after execution.

InputBytes -> (long)

The number of bytes input into the stage for execution.

InputRows -> (long)

The number of rows input into the stage for execution.

ExecutionTime -> (long)

Time taken to execute this stage.

QueryStagePlan -> (structure)

Stage plan information such as name, identifier, sub plans, and source stages.

Name -> (string)

Name of the query stage plan that describes the operation this stage is performing as part of query execution.

Identifier -> (string)

Information about the operation this query stage plan node is performing.

Children -> (list)

Stage plan information such as name, identifier, sub plans, and remote sources of child plan nodes/

(structure)

Stage plan information such as name, identifier, sub plans, and remote sources.

Name -> (string)

Name of the query stage plan that describes the operation this stage is performing as part of query execution.

Identifier -> (string)

Information about the operation this query stage plan node is performing.

Children -> (list)

Stage plan information such as name, identifier, sub plans, and remote sources of child plan nodes/

( â¦ recursive â¦ )

RemoteSources -> (list)

Source plan node IDs.

(string)

RemoteSources -> (list)

Source plan node IDs.

(string)

SubStages -> (list)

List of sub query stages that form this stage execution plan.

(structure)

Stage statistics such as input and output rows and bytes, execution time and stage state. This information also includes substages and the query stage plan.

StageId -> (long)

The identifier for a stage.

State -> (string)

State of the stage after query execution.

OutputBytes -> (long)

The number of bytes output from the stage after execution.

OutputRows -> (long)

The number of rows output from the stage after execution.

InputBytes -> (long)

The number of bytes input into the stage for execution.

InputRows -> (long)

The number of rows input into the stage for execution.

ExecutionTime -> (long)

Time taken to execute this stage.

QueryStagePlan -> (structure)

Stage plan information such as name, identifier, sub plans, and source stages.

Name -> (string)

Name of the query stage plan that describes the operation this stage is performing as part of query execution.

Identifier -> (string)

Information about the operation this query stage plan node is performing.

Children -> (list)

Stage plan information such as name, identifier, sub plans, and remote sources of child plan nodes/

(structure)

Stage plan information such as name, identifier, sub plans, and remote sources.

Name -> (string)

Name of the query stage plan that describes the operation this stage is performing as part of query execution.

Identifier -> (string)

Information about the operation this query stage plan node is performing.

Children -> (list)

Stage plan information such as name, identifier, sub plans, and remote sources of child plan nodes/

( â¦ recursive â¦ )

RemoteSources -> (list)

Source plan node IDs.

(string)

RemoteSources -> (list)

Source plan node IDs.

(string)

SubStages -> (list)

List of sub query stages that form this stage execution plan.

( â¦ recursive â¦ )