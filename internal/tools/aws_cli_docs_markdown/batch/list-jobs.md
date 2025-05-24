# list-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/list-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/list-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [batch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/index.html#cli-aws-batch) ]

# list-jobs

## Description

Returns a list of Batch jobs.

You must specify only one of the following items:

- A job queue ID to return a list of jobs in that job queue
- A multi-node parallel job ID to return a list of nodes for that job
- An array job ID to return a list of the children for that job

You can filter the results by job status with the `jobStatus` parameter. If you donât specify a status, only `RUNNING` jobs are returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/ListJobs)

`list-jobs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `jobSummaryList`

## Synopsis

```
list-jobs
[--job-queue <value>]
[--array-job-id <value>]
[--multi-node-job-id <value>]
[--job-status <value>]
[--filters <value>]
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

`--job-queue` (string)

The name or full Amazon Resource Name (ARN) of the job queue used to list jobs.

`--array-job-id` (string)

The job ID for an array job. Specifying an array job ID with this parameter lists all child jobs from within the specified array.

`--multi-node-job-id` (string)

The job ID for a multi-node parallel job. Specifying a multi-node parallel job ID with this parameter lists all nodes that are associated with the specified job.

`--job-status` (string)

The job status used to filter jobs in the specified queue. If the `filters` parameter is specified, the `jobStatus` parameter is ignored and jobs with any status are returned. If you donât specify a status, only `RUNNING` jobs are returned.

Possible values:

- `SUBMITTED`
- `PENDING`
- `RUNNABLE`
- `STARTING`
- `RUNNING`
- `SUCCEEDED`
- `FAILED`

`--filters` (list)

The filter to apply to the query. Only one filter can be used at a time. When the filter is used, `jobStatus` is ignored. The filter doesnât apply to child jobs in an array or multi-node parallel (MNP) jobs. The results are sorted by the `createdAt` field, with the most recent jobs being first.

JOB_NAME

The value of the filter is a case-insensitive match for the job name. If the value ends with an asterisk (*), the filter matches any job name that begins with the string before the â*â. This corresponds to the `jobName` value. For example, `test1` matches both `Test1` and `test1` , and `test1*` matches both `test1` and `Test10` . When the `JOB_NAME` filter is used, the results are grouped by the job name and version.

JOB_DEFINITION

The value for the filter is the name or Amazon Resource Name (ARN) of the job definition. This corresponds to the `jobDefinition` value. The value is case sensitive. When the value for the filter is the job definition name, the results include all the jobs that used any revision of that job definition name. If the value ends with an asterisk (*), the filter matches any job definition name that begins with the string before the â*â. For example, `jd1` matches only `jd1` , and `jd1*` matches both `jd1` and `jd1A` . The version of the job definition thatâs used doesnât affect the sort order. When the `JOB_DEFINITION` filter is used and the ARN is used (which is in the form `arn:${Partition}:batch:${Region}:${Account}:job-definition/${JobDefinitionName}:${Revision}` ), the results include jobs that used the specified revision of the job definition. Asterisk (*) isnât supported when the ARN is used.

BEFORE_CREATED_AT

The value for the filter is the time thatâs before the job was created. This corresponds to the `createdAt` value. The value is a string representation of the number of milliseconds since 00:00:00 UTC (midnight) on January 1, 1970.

AFTER_CREATED_AT

The value for the filter is the time thatâs after the job was created. This corresponds to the `createdAt` value. The value is a string representation of the number of milliseconds since 00:00:00 UTC (midnight) on January 1, 1970.

(structure)

A filter name and value pair thatâs used to return a more specific list of results from a `ListJobs` or `ListJobsByConsumableResource` API operation.

name -> (string)

The name of the filter. Filter names are case sensitive.

values -> (list)

The filter values.

(string)

Shorthand Syntax:

```
name=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "values": ["string", ...]
  }
  ...
]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To list running jobs**

This example lists the running jobs in the HighPriority job queue.

Command:

```
aws batch list-jobs --job-queue HighPriority
```

Output:

```
{
    "jobSummaryList": [
        {
            "jobName": "example",
            "jobId": "e66ff5fd-a1ff-4640-b1a2-0b0a142f49bb"
        }
    ]
}
```

**To list submitted jobs**

This example lists jobs in the HighPriority job queue that are in the SUBMITTED job status.

Command:

```
aws batch list-jobs --job-queue HighPriority --job-status SUBMITTED
```

Output:

```
{
    "jobSummaryList": [
        {
            "jobName": "example",
            "jobId": "68f0c163-fbd4-44e6-9fd1-25b14a434786"
        }
    ]
}
```

## Output

jobSummaryList -> (list)

A list of job summaries that match the request.

(structure)

An object that represents summary details of a job.

jobArn -> (string)

The Amazon Resource Name (ARN) of the job.

jobId -> (string)

The job ID.

jobName -> (string)

The job name.

createdAt -> (long)

The Unix timestamp (in milliseconds) for when the job was created. For non-array jobs and parent array jobs, this is when the job entered the `SUBMITTED` state (at the time [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) was called). For array child jobs, this is when the child job was spawned by its parent and entered the `PENDING` state.

status -> (string)

The current status for the job.

statusReason -> (string)

A short, human-readable string to provide more details for the current status of the job.

startedAt -> (long)

The Unix timestamp for when the job was started. More specifically, itâs when the job transitioned from the `STARTING` state to the `RUNNING` state.

stoppedAt -> (long)

The Unix timestamp for when the job was stopped. More specifically, itâs when the job transitioned from the `RUNNING` state to a terminal state, such as `SUCCEEDED` or `FAILED` .

container -> (structure)

An object that represents the details of the container thatâs associated with the job.

exitCode -> (integer)

The exit code to return upon completion.

reason -> (string)

A short (255 max characters) human-readable string to provide additional details for a running or stopped container.

arrayProperties -> (structure)

The array properties of the job, if itâs an array job.

size -> (integer)

The size of the array job. This parameter is returned for parent array jobs.

index -> (integer)

The job index within the array thatâs associated with this job. This parameter is returned for children of array jobs.

nodeProperties -> (structure)

The node properties for a single node in a job summary list.

### Note

This isnât applicable to jobs that are running on Fargate resources.

isMainNode -> (boolean)

Specifies whether the current node is the main node for a multi-node parallel job.

numNodes -> (integer)

The number of nodes that are associated with a multi-node parallel job.

nodeIndex -> (integer)

The node index for the node. Node index numbering begins at zero. This index is also available on the node with the `AWS_BATCH_JOB_NODE_INDEX` environment variable.

jobDefinition -> (string)

The Amazon Resource Name (ARN) of the job definition.

nextToken -> (string)

The `nextToken` value to include in a future `ListJobs` request. When the results of a `ListJobs` request exceed `maxResults` , this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.