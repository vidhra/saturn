# describe-workflow-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-workflow-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-workflow-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [swf](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/index.html#cli-aws-swf) ]

# describe-workflow-execution

## Description

Returns information about the specified workflow execution including its type and some statistics.

### Note

This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.

**Access Control**

You can use IAM policies to control this actionâs access to Amazon SWF resources as follows:

- Use a `Resource` element with the domain name to limit the action to only specified domains.
- Use an `Action` element to allow or deny permission to call this action.
- You cannot use an IAM policy to constrain this actionâs parameters.

If the caller doesnât have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attributeâs `cause` parameter is set to `OPERATION_NOT_PERMITTED` . For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/swf-2012-01-25/DescribeWorkflowExecution)

## Synopsis

```
describe-workflow-execution
--domain <value>
--execution <value>
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

The name of the domain containing the workflow execution.

`--execution` (structure)

The workflow execution to describe.

workflowId -> (string)

The user defined identifier associated with the workflow execution.

runId -> (string)

A system-generated unique identifier for the workflow execution.

Shorthand Syntax:

```
workflowId=string,runId=string
```

JSON Syntax:

```
{
  "workflowId": "string",
  "runId": "string"
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

executionInfo -> (structure)

Information about the workflow execution.

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

executionConfiguration -> (structure)

The configuration settings for this workflow execution including timeout values, tasklist etc.

taskStartToCloseTimeout -> (string)

The maximum duration allowed for decision tasks for this workflow execution.

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

executionStartToCloseTimeout -> (string)

The total duration for this workflow execution.

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

taskList -> (structure)

The task list used for the decision tasks generated for this workflow execution.

name -> (string)

The name of the task list.

taskPriority -> (string)

The priority assigned to decision tasks for this workflow execution. Valid values are integers that range from Javaâs `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.

For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *Amazon SWF Developer Guide* .

childPolicy -> (string)

The policy to use for the child workflow executions if this workflow execution is terminated, by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout.

The supported child policies are:

- `TERMINATE` â The child executions are terminated.
- `REQUEST_CANCEL` â A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
- `ABANDON` â No action is taken. The child executions continue to run.

lambdaRole -> (string)

The IAM role attached to the child workflow execution.

openCounts -> (structure)

The number of tasks for this workflow execution. This includes open and closed tasks of all types.

openActivityTasks -> (integer)

The count of activity tasks whose status is `OPEN` .

openDecisionTasks -> (integer)

The count of decision tasks whose status is OPEN. A workflow execution can have at most one open decision task.

openTimers -> (integer)

The count of timers started by this workflow execution that have not fired yet.

openChildWorkflowExecutions -> (integer)

The count of child workflow executions whose status is `OPEN` .

openLambdaFunctions -> (integer)

The count of Lambda tasks whose status is `OPEN` .

latestActivityTaskTimestamp -> (timestamp)

The time when the last activity task was scheduled for this workflow execution. You can use this information to determine if the workflow has not made progress for an unusually long period of time and might require a corrective action.

latestExecutionContext -> (string)

The latest executionContext provided by the decider for this workflow execution. A decider can provide an executionContext (a free-form string) when closing a decision task using  RespondDecisionTaskCompleted .