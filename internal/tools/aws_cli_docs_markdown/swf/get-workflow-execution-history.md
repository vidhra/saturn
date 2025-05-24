# get-workflow-execution-historyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/get-workflow-execution-history.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/get-workflow-execution-history.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [swf](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/index.html#cli-aws-swf) ]

# get-workflow-execution-history

## Description

Returns the history of the specified workflow execution. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the `nextPageToken` returned by the initial call.

### Note

This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.

**Access Control**

You can use IAM policies to control this actionâs access to Amazon SWF resources as follows:

- Use a `Resource` element with the domain name to limit the action to only specified domains.
- Use an `Action` element to allow or deny permission to call this action.
- You cannot use an IAM policy to constrain this actionâs parameters.

If the caller doesnât have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attributeâs `cause` parameter is set to `OPERATION_NOT_PERMITTED` . For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/swf-2012-01-25/GetWorkflowExecutionHistory)

`get-workflow-execution-history` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `events`

## Synopsis

```
get-workflow-execution-history
--domain <value>
--execution <value>
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

The name of the domain containing the workflow execution.

`--execution` (structure)

Specifies the workflow execution for which to return the history.

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

`--reverse-order` | `--no-reverse-order` (boolean)

When set to `true` , returns the events in reverse order. By default the results are returned in ascending order of the `eventTimeStamp` of the events.

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

events -> (list)

The list of history events.

(structure)

Event within a workflow execution. A history event can be one of these types:

- `ActivityTaskCancelRequested` â A `RequestCancelActivityTask` decision was received by the system.
- `ActivityTaskCanceled` â The activity task was successfully canceled.
- `ActivityTaskCompleted` â An activity worker successfully completed an activity task by calling  RespondActivityTaskCompleted .
- `ActivityTaskFailed` â An activity worker failed an activity task by calling  RespondActivityTaskFailed .
- `ActivityTaskScheduled` â An activity task was scheduled for execution.
- `ActivityTaskStarted` â The scheduled activity task was dispatched to a worker.
- `ActivityTaskTimedOut` â The activity task timed out.
- `CancelTimerFailed` â Failed to process CancelTimer decision. This happens when the decision isnât configured properly, for example no timer exists with the specified timer Id.
- `CancelWorkflowExecutionFailed` â A request to cancel a workflow execution failed.
- `ChildWorkflowExecutionCanceled` â A child workflow execution, started by this workflow execution, was canceled and closed.
- `ChildWorkflowExecutionCompleted` â A child workflow execution, started by this workflow execution, completed successfully and was closed.
- `ChildWorkflowExecutionFailed` â A child workflow execution, started by this workflow execution, failed to complete successfully and was closed.
- `ChildWorkflowExecutionStarted` â A child workflow execution was successfully started.
- `ChildWorkflowExecutionTerminated` â A child workflow execution, started by this workflow execution, was terminated.
- `ChildWorkflowExecutionTimedOut` â A child workflow execution, started by this workflow execution, timed out and was closed.
- `CompleteWorkflowExecutionFailed` â The workflow execution failed to complete.
- `ContinueAsNewWorkflowExecutionFailed` â The workflow execution failed to complete after being continued as a new workflow execution.
- `DecisionTaskCompleted` â The decider successfully completed a decision task by calling  RespondDecisionTaskCompleted .
- `DecisionTaskScheduled` â A decision task was scheduled for the workflow execution.
- `DecisionTaskStarted` â The decision task was dispatched to a decider.
- `DecisionTaskTimedOut` â The decision task timed out.
- `ExternalWorkflowExecutionCancelRequested` â Request to cancel an external workflow execution was successfully delivered to the target execution.
- `ExternalWorkflowExecutionSignaled` â A signal, requested by this workflow execution, was successfully delivered to the target external workflow execution.
- `FailWorkflowExecutionFailed` â A request to mark a workflow execution as failed, itself failed.
- `MarkerRecorded` â A marker was recorded in the workflow history as the result of a `RecordMarker` decision.
- `RecordMarkerFailed` â A `RecordMarker` decision was returned as failed.
- `RequestCancelActivityTaskFailed` â Failed to process RequestCancelActivityTask decision. This happens when the decision isnât configured properly.
- `RequestCancelExternalWorkflowExecutionFailed` â Request to cancel an external workflow execution failed.
- `RequestCancelExternalWorkflowExecutionInitiated` â A request was made to request the cancellation of an external workflow execution.
- `ScheduleActivityTaskFailed` â Failed to process ScheduleActivityTask decision. This happens when the decision isnât configured properly, for example the activity type specified isnât registered.
- `SignalExternalWorkflowExecutionFailed` â The request to signal an external workflow execution failed.
- `SignalExternalWorkflowExecutionInitiated` â A request to signal an external workflow was made.
- `StartActivityTaskFailed` â A scheduled activity task failed to start.
- `StartChildWorkflowExecutionFailed` â Failed to process StartChildWorkflowExecution decision. This happens when the decision isnât configured properly, for example the workflow type specified isnât registered.
- `StartChildWorkflowExecutionInitiated` â A request was made to start a child workflow execution.
- `StartTimerFailed` â Failed to process StartTimer decision. This happens when the decision isnât configured properly, for example a timer already exists with the specified timer Id.
- `TimerCanceled` â A timer, previously started for this workflow execution, was successfully canceled.
- `TimerFired` â A timer, previously started for this workflow execution, fired.
- `TimerStarted` â A timer was started for the workflow execution due to a `StartTimer` decision.
- `WorkflowExecutionCancelRequested` â A request to cancel this workflow execution was made.
- `WorkflowExecutionCanceled` â The workflow execution was successfully canceled and closed.
- `WorkflowExecutionCompleted` â The workflow execution was closed due to successful completion.
- `WorkflowExecutionContinuedAsNew` â The workflow execution was closed and a new execution of the same type was created with the same workflowId.
- `WorkflowExecutionFailed` â The workflow execution closed due to a failure.
- `WorkflowExecutionSignaled` â An external signal was received for the workflow execution.
- `WorkflowExecutionStarted` â The workflow execution was started.
- `WorkflowExecutionTerminated` â The workflow execution was terminated.
- `WorkflowExecutionTimedOut` â The workflow execution was closed because a time out was exceeded.

eventTimestamp -> (timestamp)

The date and time when the event occurred.

eventType -> (string)

The type of the history event.

eventId -> (long)

The system generated ID of the event. This ID uniquely identifies the event with in the workflow execution history.

workflowExecutionStartedEventAttributes -> (structure)

If the event is of type `WorkflowExecutionStarted` then this member is set and provides detailed information about the event. It isnât set for other event types.

input -> (string)

The input provided to the workflow execution.

executionStartToCloseTimeout -> (string)

The maximum duration for this workflow execution.

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

taskStartToCloseTimeout -> (string)

The maximum duration of decision tasks for this workflow type.

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

childPolicy -> (string)

The policy to use for the child workflow executions if this workflow execution is terminated, by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout.

The supported child policies are:

- `TERMINATE` â The child executions are terminated.
- `REQUEST_CANCEL` â A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
- `ABANDON` â No action is taken. The child executions continue to run.

taskList -> (structure)

The name of the task list for scheduling the decision tasks for this workflow execution.

name -> (string)

The name of the task list.

taskPriority -> (string)

The priority of the decision tasks in the workflow execution.

workflowType -> (structure)

The workflow type of this execution.

name -> (string)

The name of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

version -> (string)

The version of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

tagList -> (list)

The list of tags associated with this workflow execution. An execution can have up to 5 tags.

(string)

continuedExecutionRunId -> (string)

If this workflow execution was started due to a `ContinueAsNewWorkflowExecution` decision, then it contains the `runId` of the previous workflow execution that was closed and continued as this execution.

parentWorkflowExecution -> (structure)

The source workflow execution that started this workflow execution. The member isnât set if the workflow execution was not started by a workflow.

workflowId -> (string)

The user defined identifier associated with the workflow execution.

runId -> (string)

A system-generated unique identifier for the workflow execution.

parentInitiatedEventId -> (long)

The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to the `StartChildWorkflowExecution`   Decision to start this workflow execution. The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

lambdaRole -> (string)

The IAM role attached to the workflow execution.

workflowExecutionCompletedEventAttributes -> (structure)

If the event is of type `WorkflowExecutionCompleted` then this member is set and provides detailed information about the event. It isnât set for other event types.

result -> (string)

The result produced by the workflow execution upon successful completion.

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `CompleteWorkflowExecution` decision to complete this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

completeWorkflowExecutionFailedEventAttributes -> (structure)

If the event is of type `CompleteWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isnât set for other event types.

cause -> (string)

The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

### Note

If `cause` is set to `OPERATION_NOT_PERMITTED` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `CompleteWorkflowExecution` decision to complete this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

workflowExecutionFailedEventAttributes -> (structure)

If the event is of type `WorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isnât set for other event types.

reason -> (string)

The descriptive reason provided for the failure.

details -> (string)

The details of the failure.

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `FailWorkflowExecution` decision to fail this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

failWorkflowExecutionFailedEventAttributes -> (structure)

If the event is of type `FailWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isnât set for other event types.

cause -> (string)

The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

### Note

If `cause` is set to `OPERATION_NOT_PERMITTED` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `FailWorkflowExecution` decision to fail this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

workflowExecutionTimedOutEventAttributes -> (structure)

If the event is of type `WorkflowExecutionTimedOut` then this member is set and provides detailed information about the event. It isnât set for other event types.

timeoutType -> (string)

The type of timeout that caused this event.

childPolicy -> (string)

The policy used for the child workflow executions of this workflow execution.

The supported child policies are:

- `TERMINATE` â The child executions are terminated.
- `REQUEST_CANCEL` â A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
- `ABANDON` â No action is taken. The child executions continue to run.

workflowExecutionCanceledEventAttributes -> (structure)

If the event is of type `WorkflowExecutionCanceled` then this member is set and provides detailed information about the event. It isnât set for other event types.

details -> (string)

The details of the cancellation.

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `CancelWorkflowExecution` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

cancelWorkflowExecutionFailedEventAttributes -> (structure)

If the event is of type `CancelWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isnât set for other event types.

cause -> (string)

The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

### Note

If `cause` is set to `OPERATION_NOT_PERMITTED` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `CancelWorkflowExecution` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

workflowExecutionContinuedAsNewEventAttributes -> (structure)

If the event is of type `WorkflowExecutionContinuedAsNew` then this member is set and provides detailed information about the event. It isnât set for other event types.

input -> (string)

The input provided to the new workflow execution.

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `ContinueAsNewWorkflowExecution` decision that started this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

newExecutionRunId -> (string)

The `runId` of the new workflow execution.

executionStartToCloseTimeout -> (string)

The total duration allowed for the new workflow execution.

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

taskList -> (structure)

The task list to use for the decisions of the new (continued) workflow execution.

name -> (string)

The name of the task list.

taskPriority -> (string)

The priority of the task to use for the decisions of the new (continued) workflow execution.

taskStartToCloseTimeout -> (string)

The maximum duration of decision tasks for the new workflow execution.

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

childPolicy -> (string)

The policy to use for the child workflow executions of the new execution if it is terminated by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout.

The supported child policies are:

- `TERMINATE` â The child executions are terminated.
- `REQUEST_CANCEL` â A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
- `ABANDON` â No action is taken. The child executions continue to run.

tagList -> (list)

The list of tags associated with the new workflow execution.

(string)

workflowType -> (structure)

The workflow type of this execution.

name -> (string)

The name of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

version -> (string)

The version of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

lambdaRole -> (string)

The IAM role to attach to the new (continued) workflow execution.

continueAsNewWorkflowExecutionFailedEventAttributes -> (structure)

If the event is of type `ContinueAsNewWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isnât set for other event types.

cause -> (string)

The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

### Note

If `cause` is set to `OPERATION_NOT_PERMITTED` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `ContinueAsNewWorkflowExecution` decision that started this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

workflowExecutionTerminatedEventAttributes -> (structure)

If the event is of type `WorkflowExecutionTerminated` then this member is set and provides detailed information about the event. It isnât set for other event types.

reason -> (string)

The reason provided for the termination.

details -> (string)

The details provided for the termination.

childPolicy -> (string)

The policy used for the child workflow executions of this workflow execution.

The supported child policies are:

- `TERMINATE` â The child executions are terminated.
- `REQUEST_CANCEL` â A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
- `ABANDON` â No action is taken. The child executions continue to run.

cause -> (string)

If set, indicates that the workflow execution was automatically terminated, and specifies the cause. This happens if the parent workflow execution times out or is terminated and the child policy is set to terminate child executions.

workflowExecutionCancelRequestedEventAttributes -> (structure)

If the event is of type `WorkflowExecutionCancelRequested` then this member is set and provides detailed information about the event. It isnât set for other event types.

externalWorkflowExecution -> (structure)

The external workflow execution for which the cancellation was requested.

workflowId -> (string)

The user defined identifier associated with the workflow execution.

runId -> (string)

A system-generated unique identifier for the workflow execution.

externalInitiatedEventId -> (long)

The ID of the `RequestCancelExternalWorkflowExecutionInitiated` event corresponding to the `RequestCancelExternalWorkflowExecution` decision to cancel this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

cause -> (string)

If set, indicates that the request to cancel the workflow execution was automatically generated, and specifies the cause. This happens if the parent workflow execution times out or is terminated, and the child policy is set to cancel child executions.

decisionTaskScheduledEventAttributes -> (structure)

If the event is of type `DecisionTaskScheduled` then this member is set and provides detailed information about the event. It isnât set for other event types.

taskList -> (structure)

The name of the task list in which the decision task was scheduled.

name -> (string)

The name of the task list.

taskPriority -> (string)

A task priority that, if set, specifies the priority for this decision task. Valid values are integers that range from Javaâs `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.

For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *Amazon SWF Developer Guide* .

startToCloseTimeout -> (string)

The maximum duration for this decision task. The task is considered timed out if it doesnât completed within this duration.

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

scheduleToStartTimeout -> (string)

The maximum amount of time the decision task can wait to be assigned to a worker.

decisionTaskStartedEventAttributes -> (structure)

If the event is of type `DecisionTaskStarted` then this member is set and provides detailed information about the event. It isnât set for other event types.

identity -> (string)

Identity of the decider making the request. This enables diagnostic tracing when problems arise. The form of this identity is user defined.

scheduledEventId -> (long)

The ID of the `DecisionTaskScheduled` event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

decisionTaskCompletedEventAttributes -> (structure)

If the event is of type `DecisionTaskCompleted` then this member is set and provides detailed information about the event. It isnât set for other event types.

executionContext -> (string)

User defined context for the workflow execution.

scheduledEventId -> (long)

The ID of the `DecisionTaskScheduled` event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId -> (long)

The ID of the `DecisionTaskStarted` event recorded when this decision task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

taskList -> (structure)

Represents a task list.

name -> (string)

The name of the task list.

taskListScheduleToStartTimeout -> (string)

The maximum amount of time the decision task can wait to be assigned to a worker.

decisionTaskTimedOutEventAttributes -> (structure)

If the event is of type `DecisionTaskTimedOut` then this member is set and provides detailed information about the event. It isnât set for other event types.

timeoutType -> (string)

The type of timeout that expired before the decision task could be completed.

scheduledEventId -> (long)

The ID of the `DecisionTaskScheduled` event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId -> (long)

The ID of the `DecisionTaskStarted` event recorded when this decision task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

activityTaskScheduledEventAttributes -> (structure)

If the event is of type `ActivityTaskScheduled` then this member is set and provides detailed information about the event. It isnât set for other event types.

activityType -> (structure)

The type of the activity task.

name -> (string)

The name of this activity.

### Note

The combination of activity type name and version must be unique within a domain.

version -> (string)

The version of this activity.

### Note

The combination of activity type name and version must be unique with in a domain.

activityId -> (string)

The unique ID of the activity task.

input -> (string)

The input provided to the activity task.

control -> (string)

Data attached to the event that can be used by the decider in subsequent workflow tasks. This data isnât sent to the activity.

scheduleToStartTimeout -> (string)

The maximum amount of time the activity task can wait to be assigned to a worker.

scheduleToCloseTimeout -> (string)

The maximum amount of time for this activity task.

startToCloseTimeout -> (string)

The maximum amount of time a worker may take to process the activity task.

taskList -> (structure)

The task list in which the activity task has been scheduled.

name -> (string)

The name of the task list.

taskPriority -> (string)

The priority to assign to the scheduled activity task. If set, this overrides any default priority value that was assigned when the activity type was registered.

Valid values are integers that range from Javaâs `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.

For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *Amazon SWF Developer Guide* .

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision that resulted in the scheduling of this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

heartbeatTimeout -> (string)

The maximum time before which the worker processing this task must report progress by calling  RecordActivityTaskHeartbeat . If the timeout is exceeded, the activity task is automatically timed out. If the worker subsequently attempts to record a heartbeat or return a result, it is ignored.

activityTaskStartedEventAttributes -> (structure)

If the event is of type `ActivityTaskStarted` then this member is set and provides detailed information about the event. It isnât set for other event types.

identity -> (string)

Identity of the worker that was assigned this task. This aids diagnostics when problems arise. The form of this identity is user defined.

scheduledEventId -> (long)

The ID of the `ActivityTaskScheduled` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

activityTaskCompletedEventAttributes -> (structure)

If the event is of type `ActivityTaskCompleted` then this member is set and provides detailed information about the event. It isnât set for other event types.

result -> (string)

The results of the activity task.

scheduledEventId -> (long)

The ID of the `ActivityTaskScheduled` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId -> (long)

The ID of the `ActivityTaskStarted` event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

activityTaskFailedEventAttributes -> (structure)

If the event is of type `ActivityTaskFailed` then this member is set and provides detailed information about the event. It isnât set for other event types.

reason -> (string)

The reason provided for the failure.

details -> (string)

The details of the failure.

scheduledEventId -> (long)

The ID of the `ActivityTaskScheduled` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId -> (long)

The ID of the `ActivityTaskStarted` event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

activityTaskTimedOutEventAttributes -> (structure)

If the event is of type `ActivityTaskTimedOut` then this member is set and provides detailed information about the event. It isnât set for other event types.

timeoutType -> (string)

The type of the timeout that caused this event.

scheduledEventId -> (long)

The ID of the `ActivityTaskScheduled` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId -> (long)

The ID of the `ActivityTaskStarted` event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

details -> (string)

Contains the content of the `details` parameter for the last call made by the activity to `RecordActivityTaskHeartbeat` .

activityTaskCanceledEventAttributes -> (structure)

If the event is of type `ActivityTaskCanceled` then this member is set and provides detailed information about the event. It isnât set for other event types.

details -> (string)

Details of the cancellation.

scheduledEventId -> (long)

The ID of the `ActivityTaskScheduled` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId -> (long)

The ID of the `ActivityTaskStarted` event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

latestCancelRequestedEventId -> (long)

If set, contains the ID of the last `ActivityTaskCancelRequested` event recorded for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

activityTaskCancelRequestedEventAttributes -> (structure)

If the event is of type `ActivityTaskcancelRequested` then this member is set and provides detailed information about the event. It isnât set for other event types.

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `RequestCancelActivityTask` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

activityId -> (string)

The unique ID of the task.

workflowExecutionSignaledEventAttributes -> (structure)

If the event is of type `WorkflowExecutionSignaled` then this member is set and provides detailed information about the event. It isnât set for other event types.

signalName -> (string)

The name of the signal received. The decider can use the signal name and inputs to determine how to the process the signal.

input -> (string)

The inputs provided with the signal. The decider can use the signal name and inputs to determine how to process the signal.

externalWorkflowExecution -> (structure)

The workflow execution that sent the signal. This is set only of the signal was sent by another workflow execution.

workflowId -> (string)

The user defined identifier associated with the workflow execution.

runId -> (string)

A system-generated unique identifier for the workflow execution.

externalInitiatedEventId -> (long)

The ID of the `SignalExternalWorkflowExecutionInitiated` event corresponding to the `SignalExternalWorkflow` decision to signal this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event. This field is set only if the signal was initiated by another workflow execution.

markerRecordedEventAttributes -> (structure)

If the event is of type `MarkerRecorded` then this member is set and provides detailed information about the event. It isnât set for other event types.

markerName -> (string)

The name of the marker.

details -> (string)

The details of the marker.

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `RecordMarker` decision that requested this marker. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

recordMarkerFailedEventAttributes -> (structure)

If the event is of type `DecisionTaskFailed` then this member is set and provides detailed information about the event. It isnât set for other event types.

markerName -> (string)

The markerâs name.

cause -> (string)

The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

### Note

If `cause` is set to `OPERATION_NOT_PERMITTED` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `RecordMarkerFailed` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

timerStartedEventAttributes -> (structure)

If the event is of type `TimerStarted` then this member is set and provides detailed information about the event. It isnât set for other event types.

timerId -> (string)

The unique ID of the timer that was started.

control -> (string)

Data attached to the event that can be used by the decider in subsequent workflow tasks.

startToFireTimeout -> (string)

The duration of time after which the timer fires.

The duration is specified in seconds, an integer greater than or equal to `0` .

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `StartTimer` decision for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

timerFiredEventAttributes -> (structure)

If the event is of type `TimerFired` then this member is set and provides detailed information about the event. It isnât set for other event types.

timerId -> (string)

The unique ID of the timer that fired.

startedEventId -> (long)

The ID of the `TimerStarted` event that was recorded when this timer was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

timerCanceledEventAttributes -> (structure)

If the event is of type `TimerCanceled` then this member is set and provides detailed information about the event. It isnât set for other event types.

timerId -> (string)

The unique ID of the timer that was canceled.

startedEventId -> (long)

The ID of the `TimerStarted` event that was recorded when this timer was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `CancelTimer` decision to cancel this timer. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startChildWorkflowExecutionInitiatedEventAttributes -> (structure)

If the event is of type `StartChildWorkflowExecutionInitiated` then this member is set and provides detailed information about the event. It isnât set for other event types.

workflowId -> (string)

The `workflowId` of the child workflow execution.

workflowType -> (structure)

The type of the child workflow execution.

name -> (string)

The name of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

version -> (string)

The version of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

control -> (string)

Data attached to the event that can be used by the decider in subsequent decision tasks. This data isnât sent to the activity.

input -> (string)

The inputs provided to the child workflow execution.

executionStartToCloseTimeout -> (string)

The maximum duration for the child workflow execution. If the workflow execution isnât closed within this duration, it is timed out and force-terminated.

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

taskList -> (structure)

The name of the task list used for the decision tasks of the child workflow execution.

name -> (string)

The name of the task list.

taskPriority -> (string)

The priority assigned for the decision tasks for this workflow execution. Valid values are integers that range from Javaâs `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.

For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *Amazon SWF Developer Guide* .

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `StartChildWorkflowExecution`   Decision to request this child workflow execution. This information can be useful for diagnosing problems by tracing back the cause of events.

childPolicy -> (string)

The policy to use for the child workflow executions if this execution gets terminated by explicitly calling the  TerminateWorkflowExecution action or due to an expired timeout.

The supported child policies are:

- `TERMINATE` â The child executions are terminated.
- `REQUEST_CANCEL` â A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
- `ABANDON` â No action is taken. The child executions continue to run.

taskStartToCloseTimeout -> (string)

The maximum duration allowed for the decision tasks for this workflow execution.

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

tagList -> (list)

The list of tags to associated with the child workflow execution.

(string)

lambdaRole -> (string)

The IAM role to attach to the child workflow execution.

childWorkflowExecutionStartedEventAttributes -> (structure)

If the event is of type `ChildWorkflowExecutionStarted` then this member is set and provides detailed information about the event. It isnât set for other event types.

workflowExecution -> (structure)

The child workflow execution that was started.

workflowId -> (string)

The user defined identifier associated with the workflow execution.

runId -> (string)

A system-generated unique identifier for the workflow execution.

workflowType -> (structure)

The type of the child workflow execution.

name -> (string)

The name of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

version -> (string)

The version of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

initiatedEventId -> (long)

The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to the `StartChildWorkflowExecution`   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

childWorkflowExecutionCompletedEventAttributes -> (structure)

If the event is of type `ChildWorkflowExecutionCompleted` then this member is set and provides detailed information about the event. It isnât set for other event types.

workflowExecution -> (structure)

The child workflow execution that was completed.

workflowId -> (string)

The user defined identifier associated with the workflow execution.

runId -> (string)

A system-generated unique identifier for the workflow execution.

workflowType -> (structure)

The type of the child workflow execution.

name -> (string)

The name of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

version -> (string)

The version of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

result -> (string)

The result of the child workflow execution.

initiatedEventId -> (long)

The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to the `StartChildWorkflowExecution`   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId -> (long)

The ID of the `ChildWorkflowExecutionStarted` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

childWorkflowExecutionFailedEventAttributes -> (structure)

If the event is of type `ChildWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isnât set for other event types.

workflowExecution -> (structure)

The child workflow execution that failed.

workflowId -> (string)

The user defined identifier associated with the workflow execution.

runId -> (string)

A system-generated unique identifier for the workflow execution.

workflowType -> (structure)

The type of the child workflow execution.

name -> (string)

The name of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

version -> (string)

The version of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

reason -> (string)

The reason for the failure (if provided).

details -> (string)

The details of the failure (if provided).

initiatedEventId -> (long)

The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to the `StartChildWorkflowExecution`   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId -> (long)

The ID of the `ChildWorkflowExecutionStarted` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

childWorkflowExecutionTimedOutEventAttributes -> (structure)

If the event is of type `ChildWorkflowExecutionTimedOut` then this member is set and provides detailed information about the event. It isnât set for other event types.

workflowExecution -> (structure)

The child workflow execution that timed out.

workflowId -> (string)

The user defined identifier associated with the workflow execution.

runId -> (string)

A system-generated unique identifier for the workflow execution.

workflowType -> (structure)

The type of the child workflow execution.

name -> (string)

The name of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

version -> (string)

The version of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

timeoutType -> (string)

The type of the timeout that caused the child workflow execution to time out.

initiatedEventId -> (long)

The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to the `StartChildWorkflowExecution`   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId -> (long)

The ID of the `ChildWorkflowExecutionStarted` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

childWorkflowExecutionCanceledEventAttributes -> (structure)

If the event is of type `ChildWorkflowExecutionCanceled` then this member is set and provides detailed information about the event. It isnât set for other event types.

workflowExecution -> (structure)

The child workflow execution that was canceled.

workflowId -> (string)

The user defined identifier associated with the workflow execution.

runId -> (string)

A system-generated unique identifier for the workflow execution.

workflowType -> (structure)

The type of the child workflow execution.

name -> (string)

The name of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

version -> (string)

The version of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

details -> (string)

Details of the cancellation (if provided).

initiatedEventId -> (long)

The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to the `StartChildWorkflowExecution`   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId -> (long)

The ID of the `ChildWorkflowExecutionStarted` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

childWorkflowExecutionTerminatedEventAttributes -> (structure)

If the event is of type `ChildWorkflowExecutionTerminated` then this member is set and provides detailed information about the event. It isnât set for other event types.

workflowExecution -> (structure)

The child workflow execution that was terminated.

workflowId -> (string)

The user defined identifier associated with the workflow execution.

runId -> (string)

A system-generated unique identifier for the workflow execution.

workflowType -> (structure)

The type of the child workflow execution.

name -> (string)

The name of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

version -> (string)

The version of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

initiatedEventId -> (long)

The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to the `StartChildWorkflowExecution`   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId -> (long)

The ID of the `ChildWorkflowExecutionStarted` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

signalExternalWorkflowExecutionInitiatedEventAttributes -> (structure)

If the event is of type `SignalExternalWorkflowExecutionInitiated` then this member is set and provides detailed information about the event. It isnât set for other event types.

workflowId -> (string)

The `workflowId` of the external workflow execution.

runId -> (string)

The `runId` of the external workflow execution to send the signal to.

signalName -> (string)

The name of the signal.

input -> (string)

The input provided to the signal.

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `SignalExternalWorkflowExecution` decision for this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

control -> (string)

Data attached to the event that can be used by the decider in subsequent decision tasks.

externalWorkflowExecutionSignaledEventAttributes -> (structure)

If the event is of type `ExternalWorkflowExecutionSignaled` then this member is set and provides detailed information about the event. It isnât set for other event types.

workflowExecution -> (structure)

The external workflow execution that the signal was delivered to.

workflowId -> (string)

The user defined identifier associated with the workflow execution.

runId -> (string)

A system-generated unique identifier for the workflow execution.

initiatedEventId -> (long)

The ID of the `SignalExternalWorkflowExecutionInitiated` event corresponding to the `SignalExternalWorkflowExecution` decision to request this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

signalExternalWorkflowExecutionFailedEventAttributes -> (structure)

If the event is of type `SignalExternalWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isnât set for other event types.

workflowId -> (string)

The `workflowId` of the external workflow execution that the signal was being delivered to.

runId -> (string)

The `runId` of the external workflow execution that the signal was being delivered to.

cause -> (string)

The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

### Note

If `cause` is set to `OPERATION_NOT_PERMITTED` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

initiatedEventId -> (long)

The ID of the `SignalExternalWorkflowExecutionInitiated` event corresponding to the `SignalExternalWorkflowExecution` decision to request this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `SignalExternalWorkflowExecution` decision for this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

control -> (string)

The data attached to the event that the decider can use in subsequent workflow tasks. This data isnât sent to the workflow execution.

externalWorkflowExecutionCancelRequestedEventAttributes -> (structure)

If the event is of type `ExternalWorkflowExecutionCancelRequested` then this member is set and provides detailed information about the event. It isnât set for other event types.

workflowExecution -> (structure)

The external workflow execution to which the cancellation request was delivered.

workflowId -> (string)

The user defined identifier associated with the workflow execution.

runId -> (string)

A system-generated unique identifier for the workflow execution.

initiatedEventId -> (long)

The ID of the `RequestCancelExternalWorkflowExecutionInitiated` event corresponding to the `RequestCancelExternalWorkflowExecution` decision to cancel this external workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

requestCancelExternalWorkflowExecutionInitiatedEventAttributes -> (structure)

If the event is of type `RequestCancelExternalWorkflowExecutionInitiated` then this member is set and provides detailed information about the event. It isnât set for other event types.

workflowId -> (string)

The `workflowId` of the external workflow execution to be canceled.

runId -> (string)

The `runId` of the external workflow execution to be canceled.

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `RequestCancelExternalWorkflowExecution` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

control -> (string)

Data attached to the event that can be used by the decider in subsequent workflow tasks.

requestCancelExternalWorkflowExecutionFailedEventAttributes -> (structure)

If the event is of type `RequestCancelExternalWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isnât set for other event types.

workflowId -> (string)

The `workflowId` of the external workflow to which the cancel request was to be delivered.

runId -> (string)

The `runId` of the external workflow execution.

cause -> (string)

The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

### Note

If `cause` is set to `OPERATION_NOT_PERMITTED` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

initiatedEventId -> (long)

The ID of the `RequestCancelExternalWorkflowExecutionInitiated` event corresponding to the `RequestCancelExternalWorkflowExecution` decision to cancel this external workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `RequestCancelExternalWorkflowExecution` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

control -> (string)

The data attached to the event that the decider can use in subsequent workflow tasks. This data isnât sent to the workflow execution.

scheduleActivityTaskFailedEventAttributes -> (structure)

If the event is of type `ScheduleActivityTaskFailed` then this member is set and provides detailed information about the event. It isnât set for other event types.

activityType -> (structure)

The activity type provided in the `ScheduleActivityTask` decision that failed.

name -> (string)

The name of this activity.

### Note

The combination of activity type name and version must be unique within a domain.

version -> (string)

The version of this activity.

### Note

The combination of activity type name and version must be unique with in a domain.

activityId -> (string)

The activityId provided in the `ScheduleActivityTask` decision that failed.

cause -> (string)

The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

### Note

If `cause` is set to `OPERATION_NOT_PERMITTED` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision that resulted in the scheduling of this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

requestCancelActivityTaskFailedEventAttributes -> (structure)

If the event is of type `RequestCancelActivityTaskFailed` then this member is set and provides detailed information about the event. It isnât set for other event types.

activityId -> (string)

The activityId provided in the `RequestCancelActivityTask` decision that failed.

cause -> (string)

The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

### Note

If `cause` is set to `OPERATION_NOT_PERMITTED` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `RequestCancelActivityTask` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startTimerFailedEventAttributes -> (structure)

If the event is of type `StartTimerFailed` then this member is set and provides detailed information about the event. It isnât set for other event types.

timerId -> (string)

The timerId provided in the `StartTimer` decision that failed.

cause -> (string)

The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

### Note

If `cause` is set to `OPERATION_NOT_PERMITTED` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `StartTimer` decision for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

cancelTimerFailedEventAttributes -> (structure)

If the event is of type `CancelTimerFailed` then this member is set and provides detailed information about the event. It isnât set for other event types.

timerId -> (string)

The timerId provided in the `CancelTimer` decision that failed.

cause -> (string)

The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

### Note

If `cause` is set to `OPERATION_NOT_PERMITTED` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `CancelTimer` decision to cancel this timer. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startChildWorkflowExecutionFailedEventAttributes -> (structure)

If the event is of type `StartChildWorkflowExecutionFailed` then this member is set and provides detailed information about the event. It isnât set for other event types.

workflowType -> (structure)

The workflow type provided in the `StartChildWorkflowExecution`   Decision that failed.

name -> (string)

The name of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

version -> (string)

The version of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

cause -> (string)

The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

### Note

When `cause` is set to `OPERATION_NOT_PERMITTED` , the decision fails because it lacks sufficient permissions. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

workflowId -> (string)

The `workflowId` of the child workflow execution.

initiatedEventId -> (long)

When the `cause` is `WORKFLOW_ALREADY_RUNNING` , `initiatedEventId` is the ID of the `StartChildWorkflowExecutionInitiated` event that corresponds to the `StartChildWorkflowExecution`   Decision to start the workflow execution. You can use this information to diagnose problems by tracing back the chain of events leading up to this event.

When the `cause` isnât `WORKFLOW_ALREADY_RUNNING` , `initiatedEventId` is set to `0` because the `StartChildWorkflowExecutionInitiated` event doesnât exist.

decisionTaskCompletedEventId -> (long)

The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `StartChildWorkflowExecution`   Decision to request this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events.

control -> (string)

The data attached to the event that the decider can use in subsequent workflow tasks. This data isnât sent to the child workflow execution.

lambdaFunctionScheduledEventAttributes -> (structure)

Provides the details of the `LambdaFunctionScheduled` event. It isnât set for other event types.

id -> (string)

The unique ID of the Lambda task.

name -> (string)

The name of the Lambda function.

control -> (string)

Data attached to the event that the decider can use in subsequent workflow tasks. This data isnât sent to the Lambda task.

input -> (string)

The input provided to the Lambda task.

startToCloseTimeout -> (string)

The maximum amount of time a worker can take to process the Lambda task.

decisionTaskCompletedEventId -> (long)

The ID of the `LambdaFunctionCompleted` event corresponding to the decision that resulted in scheduling this activity task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

lambdaFunctionStartedEventAttributes -> (structure)

Provides the details of the `LambdaFunctionStarted` event. It isnât set for other event types.

scheduledEventId -> (long)

The ID of the `LambdaFunctionScheduled` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

lambdaFunctionCompletedEventAttributes -> (structure)

Provides the details of the `LambdaFunctionCompleted` event. It isnât set for other event types.

scheduledEventId -> (long)

The ID of the `LambdaFunctionScheduled` event that was recorded when this Lambda task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

startedEventId -> (long)

The ID of the `LambdaFunctionStarted` event recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

result -> (string)

The results of the Lambda task.

lambdaFunctionFailedEventAttributes -> (structure)

Provides the details of the `LambdaFunctionFailed` event. It isnât set for other event types.

scheduledEventId -> (long)

The ID of the `LambdaFunctionScheduled` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

startedEventId -> (long)

The ID of the `LambdaFunctionStarted` event recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

reason -> (string)

The reason provided for the failure.

details -> (string)

The details of the failure.

lambdaFunctionTimedOutEventAttributes -> (structure)

Provides the details of the `LambdaFunctionTimedOut` event. It isnât set for other event types.

scheduledEventId -> (long)

The ID of the `LambdaFunctionScheduled` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

startedEventId -> (long)

The ID of the `ActivityTaskStarted` event that was recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

timeoutType -> (string)

The type of the timeout that caused this event.

scheduleLambdaFunctionFailedEventAttributes -> (structure)

Provides the details of the `ScheduleLambdaFunctionFailed` event. It isnât set for other event types.

id -> (string)

The ID provided in the `ScheduleLambdaFunction` decision that failed.

name -> (string)

The name of the Lambda function.

cause -> (string)

The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

### Note

If `cause` is set to `OPERATION_NOT_PERMITTED` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

decisionTaskCompletedEventId -> (long)

The ID of the `LambdaFunctionCompleted` event corresponding to the decision that resulted in scheduling this Lambda task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

startLambdaFunctionFailedEventAttributes -> (structure)

Provides the details of the `StartLambdaFunctionFailed` event. It isnât set for other event types.

scheduledEventId -> (long)

The ID of the `ActivityTaskScheduled` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

cause -> (string)

The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

### Note

If `cause` is set to `OPERATION_NOT_PERMITTED` , the decision failed because the IAM role attached to the execution lacked sufficient permissions. For details and example IAM policies, see [Lambda Tasks](https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html) in the *Amazon SWF Developer Guide* .

message -> (string)

A description that can help diagnose the cause of the fault.

nextPageToken -> (string)

If a `NextPageToken` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in `nextPageToken` . Keep all other arguments unchanged.

The configured `maximumPageSize` determines how many results can be returned in a single call.