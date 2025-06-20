# list-closed-workflow-executionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-closed-workflow-executions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-closed-workflow-executions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [swf](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/index.html#cli-aws-swf) ]

# list-closed-workflow-executions

## Description

Returns a list of closed workflow executions in the specified domain that meet the filtering criteria. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.

### Note

This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.

**Access Control**

You can use IAM policies to control this actionâs access to Amazon SWF resources as follows:

- Use a `Resource` element with the domain name to limit the action to only specified domains.
- Use an `Action` element to allow or deny permission to call this action.
- Constrain the following parameters by using a `Condition` element with the appropriate keys.
- `tagFilter.tag` : String constraint. The key is `swf:tagFilter.tag` .
- `typeFilter.name` : String constraint. The key is `swf:typeFilter.name` .
- `typeFilter.version` : String constraint. The key is `swf:typeFilter.version` .

If the caller doesnât have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attributeâs `cause` parameter is set to `OPERATION_NOT_PERMITTED` . For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/swf-2012-01-25/ListClosedWorkflowExecutions)

`list-closed-workflow-executions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `executionInfos`

## Synopsis

```
list-closed-workflow-executions
--domain <value>
[--start-time-filter <value>]
[--close-time-filter <value>]
[--execution-filter <value>]
[--close-status-filter <value>]
[--type-filter <value>]
[--tag-filter <value>]
[--reverse-order | --no-reverse-order]
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

`--domain` (string)

The name of the domain that contains the workflow executions to list.

`--start-time-filter` (structure)

If specified, the workflow executions are included in the returned results based on whether their start times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their start times.

### Note

`startTimeFilter` and `closeTimeFilter` are mutually exclusive. You must specify one of these in a request but not both.

oldestDate -> (timestamp)

Specifies the oldest start or close date and time to return.

latestDate -> (timestamp)

Specifies the latest start or close date and time to return.

Shorthand Syntax:

```
oldestDate=timestamp,latestDate=timestamp
```

JSON Syntax:

```
{
  "oldestDate": timestamp,
  "latestDate": timestamp
}
```

`--close-time-filter` (structure)

If specified, the workflow executions are included in the returned results based on whether their close times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their close times.

### Note

`startTimeFilter` and `closeTimeFilter` are mutually exclusive. You must specify one of these in a request but not both.

oldestDate -> (timestamp)

Specifies the oldest start or close date and time to return.

latestDate -> (timestamp)

Specifies the latest start or close date and time to return.

Shorthand Syntax:

```
oldestDate=timestamp,latestDate=timestamp
```

JSON Syntax:

```
{
  "oldestDate": timestamp,
  "latestDate": timestamp
}
```

`--execution-filter` (structure)

If specified, only workflow executions matching the workflow ID specified in the filter are returned.

### Note

`closeStatusFilter` , `executionFilter` , `typeFilter` and `tagFilter` are mutually exclusive. You can specify at most one of these in a request.

workflowId -> (string)

The workflowId to pass of match the criteria of this filter.

Shorthand Syntax:

```
workflowId=string
```

JSON Syntax:

```
{
  "workflowId": "string"
}
```

`--close-status-filter` (structure)

If specified, only workflow executions that match this *close status* are listed. For example, if TERMINATED is specified, then only TERMINATED workflow executions are listed.

### Note

`closeStatusFilter` , `executionFilter` , `typeFilter` and `tagFilter` are mutually exclusive. You can specify at most one of these in a request.

status -> (string)

The close status that must match the close status of an execution for it to meet the criteria of this filter.

Shorthand Syntax:

```
status=string
```

JSON Syntax:

```
{
  "status": "COMPLETED"|"FAILED"|"CANCELED"|"TERMINATED"|"CONTINUED_AS_NEW"|"TIMED_OUT"
}
```

`--type-filter` (structure)

If specified, only executions of the type specified in the filter are returned.

### Note

`closeStatusFilter` , `executionFilter` , `typeFilter` and `tagFilter` are mutually exclusive. You can specify at most one of these in a request.

name -> (string)

Name of the workflow type.

version -> (string)

Version of the workflow type.

Shorthand Syntax:

```
name=string,version=string
```

JSON Syntax:

```
{
  "name": "string",
  "version": "string"
}
```

`--tag-filter` (structure)

If specified, only executions that have the matching tag are listed.

### Note

`closeStatusFilter` , `executionFilter` , `typeFilter` and `tagFilter` are mutually exclusive. You can specify at most one of these in a request.

tag -> (string)

Specifies the tag that must be associated with the execution for it to meet the filter criteria.

Tags may only contain unicode letters, digits, whitespace, or these symbols: `_ . : / = + - @` .

Shorthand Syntax:

```
tag=string
```

JSON Syntax:

```
{
  "tag": "string"
}
```

`--reverse-order` | `--no-reverse-order` (boolean)

When set to `true` , returns the results in reverse order. By default the results are returned in descending order of the start or the close time of the executions.

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

executionInfos -> (list)

The list of workflow information structures.

(structure)

Contains information about a workflow execution.

execution -> (structure)

The workflow execution this information is about.

workflowId -> (string)

The user defined identifier associated with the workflow execution.

runId -> (string)

A system-generated unique identifier for the workflow execution.

workflowType -> (structure)

The type of the workflow execution.

name -> (string)

The name of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

version -> (string)

The version of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

startTimestamp -> (timestamp)

The time when the execution was started.

closeTimestamp -> (timestamp)

The time when the workflow execution was closed. Set only if the execution status is CLOSED.

executionStatus -> (string)

The current status of the execution.

closeStatus -> (string)

If the execution status is closed then this specifies how the execution was closed:

- `COMPLETED` â the execution was successfully completed.
- `CANCELED` â the execution was canceled.Cancellation allows the implementation to gracefully clean up before the execution is closed.
- `TERMINATED` â the execution was force terminated.
- `FAILED` â the execution failed to complete.
- `TIMED_OUT` â the execution did not complete in the alloted time and was automatically timed out.
- `CONTINUED_AS_NEW` â the execution is logically continued. This means the current execution was completed and a new execution was started to carry on the workflow.

parent -> (structure)

If this workflow execution is a child of another execution then contains the workflow execution that started this execution.

workflowId -> (string)

The user defined identifier associated with the workflow execution.

runId -> (string)

A system-generated unique identifier for the workflow execution.

tagList -> (list)

The list of tags associated with the workflow execution. Tags can be used to identify and list workflow executions of interest through the visibility APIs. A workflow execution can have a maximum of 5 tags.

(string)

cancelRequested -> (boolean)

Set to true if a cancellation is requested for this workflow execution.

nextPageToken -> (string)

If a `NextPageToken` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in `nextPageToken` . Keep all other arguments unchanged.

The configured `maximumPageSize` determines how many results can be returned in a single call.