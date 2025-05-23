# get-ml-task-runsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-task-runs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-task-runs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# get-ml-task-runs

## Description

Gets a list of runs for a machine learning transform. Machine learning task runs are asynchronous tasks that Glue runs on your behalf as part of various machine learning workflows. You can get a sortable, filterable list of machine learning task runs by calling `GetMLTaskRuns` with their parent transformâs `TransformID` and other optional parameters as documented in this section.

This operation returns a list of historic runs and must be paginated.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetMLTaskRuns)

## Synopsis

```
get-ml-task-runs
--transform-id <value>
[--next-token <value>]
[--max-results <value>]
[--filter <value>]
[--sort <value>]
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

`--transform-id` (string)

The unique identifier of the machine learning transform.

`--next-token` (string)

A token for pagination of the results. The default is empty.

`--max-results` (integer)

The maximum number of results to return.

`--filter` (structure)

The filter criteria, in the `TaskRunFilterCriteria` structure, for the task run.

TaskRunType -> (string)

The type of task run.

Status -> (string)

The current status of the task run.

StartedBefore -> (timestamp)

Filter on task runs started before this date.

StartedAfter -> (timestamp)

Filter on task runs started after this date.

Shorthand Syntax:

```
TaskRunType=string,Status=string,StartedBefore=timestamp,StartedAfter=timestamp
```

JSON Syntax:

```
{
  "TaskRunType": "EVALUATION"|"LABELING_SET_GENERATION"|"IMPORT_LABELS"|"EXPORT_LABELS"|"FIND_MATCHES",
  "Status": "STARTING"|"RUNNING"|"STOPPING"|"STOPPED"|"SUCCEEDED"|"FAILED"|"TIMEOUT",
  "StartedBefore": timestamp,
  "StartedAfter": timestamp
}
```

`--sort` (structure)

The sorting criteria, in the `TaskRunSortCriteria` structure, for the task run.

Column -> (string)

The column to be used to sort the list of task runs for the machine learning transform.

SortDirection -> (string)

The sort direction to be used to sort the list of task runs for the machine learning transform.

Shorthand Syntax:

```
Column=string,SortDirection=string
```

JSON Syntax:

```
{
  "Column": "TASK_RUN_TYPE"|"STATUS"|"STARTED",
  "SortDirection": "DESCENDING"|"ASCENDING"
}
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

TaskRuns -> (list)

A list of task runs that are associated with the transform.

(structure)

The sampling parameters that are associated with the machine learning transform.

TransformId -> (string)

The unique identifier for the transform.

TaskRunId -> (string)

The unique identifier for this task run.

Status -> (string)

The current status of the requested task run.

LogGroupName -> (string)

The names of the log group for secure logging, associated with this task run.

Properties -> (structure)

Specifies configuration properties associated with this task run.

TaskType -> (string)

The type of task run.

ImportLabelsTaskRunProperties -> (structure)

The configuration properties for an importing labels task run.

InputS3Path -> (string)

The Amazon Simple Storage Service (Amazon S3) path from where you will import the labels.

Replace -> (boolean)

Indicates whether to overwrite your existing labels.

ExportLabelsTaskRunProperties -> (structure)

The configuration properties for an exporting labels task run.

OutputS3Path -> (string)

The Amazon Simple Storage Service (Amazon S3) path where you will export the labels.

LabelingSetGenerationTaskRunProperties -> (structure)

The configuration properties for a labeling set generation task run.

OutputS3Path -> (string)

The Amazon Simple Storage Service (Amazon S3) path where you will generate the labeling set.

FindMatchesTaskRunProperties -> (structure)

The configuration properties for a find matches task run.

JobId -> (string)

The job ID for the Find Matches task run.

JobName -> (string)

The name assigned to the job for the Find Matches task run.

JobRunId -> (string)

The job run ID for the Find Matches task run.

ErrorString -> (string)

The list of error strings associated with this task run.

StartedOn -> (timestamp)

The date and time that this task run started.

LastModifiedOn -> (timestamp)

The last point in time that the requested task run was updated.

CompletedOn -> (timestamp)

The last point in time that the requested task run was completed.

ExecutionTime -> (integer)

The amount of time (in seconds) that the task run consumed resources.

NextToken -> (string)

A pagination token, if more results are available.