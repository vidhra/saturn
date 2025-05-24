# count-closed-workflow-executionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/count-closed-workflow-executions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/count-closed-workflow-executions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [swf](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/index.html#cli-aws-swf) ]

# count-closed-workflow-executions

## Description

Returns the number of closed workflow executions within the given domain that meet the specified filtering criteria.

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

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/swf-2012-01-25/CountClosedWorkflowExecutions)

## Synopsis

```
count-closed-workflow-executions
--domain <value>
[--start-time-filter <value>]
[--close-time-filter <value>]
[--execution-filter <value>]
[--type-filter <value>]
[--tag-filter <value>]
[--close-status-filter <value>]
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

`--domain` (string)

The name of the domain containing the workflow executions to count.

`--start-time-filter` (structure)

If specified, only workflow executions that meet the start time criteria of the filter are counted.

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

If specified, only workflow executions that meet the close time criteria of the filter are counted.

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

If specified, only workflow executions matching the `WorkflowId` in the filter are counted.

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

`--type-filter` (structure)

If specified, indicates the type of the workflow executions to be counted.

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

If specified, only executions that have a tag that matches the filter are counted.

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

`--close-status-filter` (structure)

If specified, only workflow executions that match this close status are counted. This filter has an affect only if `executionStatus` is specified as `CLOSED` .

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

**Counting Closed Workflow Executions**

You can use `swf count-closed-workflow-executions` to retrieve the number of closed workflow executions for a given domain. You can specify filters to count specific classes of executions.

The `--domain` and *either* `--close-time-filter` or `--start-time-filter` arguments are required. All other arguments are optional.

```
aws swf count-closed-workflow-executions \
    --domain DataFrobtzz \
    --close-time-filter "{ \"latestDate\" : 1377129600, \"oldestDate\" : 1370044800 }"
```

Output:

```
{
    "count": 2,
    "truncated": false
}
```

If âtruncatedâ is `true`, then âcountâ represents the maximum number that can be returned by Amazon SWF. Any further results are truncated.

To reduce the number of results returned, you can:

- **modify the `--close-time-filter` or `--start-time-filter` values to narrow the time range that is searched. Each**:
of these is mutually exclusive: You can specify *only one of these* in a request.
- **use the `--close-status-filter`, `--execution-filter`, `--tag-filter` or `--type-filter` arguments to further**:
filter the results. However, these arguments are also mutually exclusive.

### See Also

- [CountClosedWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountClosedWorkflowExecutions.html) in the *Amazon Simple Workflow Service API Reference*

## Output

count -> (integer)

The number of workflow executions.

truncated -> (boolean)

If set to true, indicates that the actual count was more than the maximum supported by this API and the count returned is the truncated value.