# get-execution-historyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/get-execution-history.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/get-execution-history.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [stepfunctions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/index.html#cli-aws-stepfunctions) ]

# get-execution-history

## Description

Returns the history of the specified execution as a list of events. By default, the results are returned in ascending order of the `timeStamp` of the events. Use the `reverseOrder` parameter to get the latest events first.

If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.

This API action is not supported by `EXPRESS` state machines.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/GetExecutionHistory)

`get-execution-history` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `events`

## Synopsis

```
get-execution-history
--execution-arn <value>
[--reverse-order | --no-reverse-order]
[--include-execution-data | --no-include-execution-data]
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

`--execution-arn` (string)

The Amazon Resource Name (ARN) of the execution.

`--reverse-order` | `--no-reverse-order` (boolean)

Lists events in descending order of their `timeStamp` .

`--include-execution-data` | `--no-include-execution-data` (boolean)

You can select whether execution data (input or output of a history event) is returned. The default is `true` .

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

The list of events that occurred in the execution.

(structure)

Contains details about the events of an execution.

timestamp -> (timestamp)

The date and time the event occurred.

type -> (string)

The type of the event.

id -> (long)

The id of the event. Events are numbered sequentially, starting at one.

previousEventId -> (long)

The id of the previous event.

activityFailedEventDetails -> (structure)

Contains details about an activity that failed during an execution.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the failure.

activityScheduleFailedEventDetails -> (structure)

Contains details about an activity schedule event that failed during an execution.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the failure.

activityScheduledEventDetails -> (structure)

Contains details about an activity scheduled during an execution.

resource -> (string)

The Amazon Resource Name (ARN) of the scheduled activity.

input -> (string)

The JSON data input to the activity task. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.

inputDetails -> (structure)

Contains details about the input for an execution history event.

truncated -> (boolean)

Indicates whether input or output was truncated in the response. Always `false` for API calls. In CloudWatch logs, the value will be true if the data is truncated due to size limits.

timeoutInSeconds -> (long)

The maximum allowed duration of the activity task.

heartbeatInSeconds -> (long)

The maximum allowed duration between two heartbeats for the activity task.

activityStartedEventDetails -> (structure)

Contains details about the start of an activity during an execution.

workerName -> (string)

The name of the worker that the task is assigned to. These names are provided by the workers when calling  GetActivityTask .

activitySucceededEventDetails -> (structure)

Contains details about an activity that successfully terminated during an execution.

output -> (string)

The JSON data output by the activity task. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.

outputDetails -> (structure)

Contains details about the output of an execution history event.

truncated -> (boolean)

Indicates whether input or output was truncated in the response. Always `false` for API calls. In CloudWatch logs, the value will be true if the data is truncated due to size limits.

activityTimedOutEventDetails -> (structure)

Contains details about an activity timeout that occurred during an execution.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the timeout.

taskFailedEventDetails -> (structure)

Contains details about the failure of a task.

resourceType -> (string)

The service name of the resource in a task state.

resource -> (string)

The action of the resource called by a task state.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the failure.

taskScheduledEventDetails -> (structure)

Contains details about a task that was scheduled.

resourceType -> (string)

The service name of the resource in a task state.

resource -> (string)

The action of the resource called by a task state.

region -> (string)

The region of the scheduled task

parameters -> (string)

The JSON data passed to the resource referenced in a task state. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.

timeoutInSeconds -> (long)

The maximum allowed duration of the task.

heartbeatInSeconds -> (long)

The maximum allowed duration between two heartbeats for the task.

taskCredentials -> (structure)

The credentials that Step Functions uses for the task.

roleArn -> (string)

The ARN of an IAM role that Step Functions assumes for the task. The role can allow cross-account access to resources.

taskStartFailedEventDetails -> (structure)

Contains details about a task that failed to start.

resourceType -> (string)

The service name of the resource in a task state.

resource -> (string)

The action of the resource called by a task state.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the failure.

taskStartedEventDetails -> (structure)

Contains details about a task that was started.

resourceType -> (string)

The service name of the resource in a task state.

resource -> (string)

The action of the resource called by a task state.

taskSubmitFailedEventDetails -> (structure)

Contains details about a task that where the submit failed.

resourceType -> (string)

The service name of the resource in a task state.

resource -> (string)

The action of the resource called by a task state.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the failure.

taskSubmittedEventDetails -> (structure)

Contains details about a submitted task.

resourceType -> (string)

The service name of the resource in a task state.

resource -> (string)

The action of the resource called by a task state.

output -> (string)

The response from a resource when a task has started. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.

outputDetails -> (structure)

Contains details about the output of an execution history event.

truncated -> (boolean)

Indicates whether input or output was truncated in the response. Always `false` for API calls. In CloudWatch logs, the value will be true if the data is truncated due to size limits.

taskSucceededEventDetails -> (structure)

Contains details about a task that succeeded.

resourceType -> (string)

The service name of the resource in a task state.

resource -> (string)

The action of the resource called by a task state.

output -> (string)

The full JSON response from a resource when a task has succeeded. This response becomes the output of the related task. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.

outputDetails -> (structure)

Contains details about the output of an execution history event.

truncated -> (boolean)

Indicates whether input or output was truncated in the response. Always `false` for API calls. In CloudWatch logs, the value will be true if the data is truncated due to size limits.

taskTimedOutEventDetails -> (structure)

Contains details about a task that timed out.

resourceType -> (string)

The service name of the resource in a task state.

resource -> (string)

The action of the resource called by a task state.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the failure.

executionFailedEventDetails -> (structure)

Contains details about an execution failure event.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the failure.

executionStartedEventDetails -> (structure)

Contains details about the start of the execution.

input -> (string)

The JSON data input to the execution. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.

inputDetails -> (structure)

Contains details about the input for an execution history event.

truncated -> (boolean)

Indicates whether input or output was truncated in the response. Always `false` for API calls. In CloudWatch logs, the value will be true if the data is truncated due to size limits.

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role used for executing Lambda tasks.

stateMachineAliasArn -> (string)

The Amazon Resource Name (ARN) that identifies a state machine alias used for starting the state machine execution.

stateMachineVersionArn -> (string)

The Amazon Resource Name (ARN) that identifies a state machine version used for starting the state machine execution.

executionSucceededEventDetails -> (structure)

Contains details about the successful termination of the execution.

output -> (string)

The JSON data output by the execution. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.

outputDetails -> (structure)

Contains details about the output of an execution history event.

truncated -> (boolean)

Indicates whether input or output was truncated in the response. Always `false` for API calls. In CloudWatch logs, the value will be true if the data is truncated due to size limits.

executionAbortedEventDetails -> (structure)

Contains details about an abort of an execution.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the failure.

executionTimedOutEventDetails -> (structure)

Contains details about the execution timeout that occurred during the execution.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the timeout.

executionRedrivenEventDetails -> (structure)

Contains details about the redrive attempt of an execution.

redriveCount -> (integer)

The number of times youâve redriven an execution. If you have not yet redriven an execution, the `redriveCount` is 0. This count is not updated for redrives that failed to start or are pending to be redriven.

mapStateStartedEventDetails -> (structure)

Contains details about Map state that was started.

length -> (integer)

The size of the array for Map state iterations.

mapIterationStartedEventDetails -> (structure)

Contains details about an iteration of a Map state that was started.

name -> (string)

The name of the iterationâs parent Map state.

index -> (integer)

The index of the array belonging to the Map state iteration.

mapIterationSucceededEventDetails -> (structure)

Contains details about an iteration of a Map state that succeeded.

name -> (string)

The name of the iterationâs parent Map state.

index -> (integer)

The index of the array belonging to the Map state iteration.

mapIterationFailedEventDetails -> (structure)

Contains details about an iteration of a Map state that failed.

name -> (string)

The name of the iterationâs parent Map state.

index -> (integer)

The index of the array belonging to the Map state iteration.

mapIterationAbortedEventDetails -> (structure)

Contains details about an iteration of a Map state that was aborted.

name -> (string)

The name of the iterationâs parent Map state.

index -> (integer)

The index of the array belonging to the Map state iteration.

lambdaFunctionFailedEventDetails -> (structure)

Contains details about a Lambda function that failed during an execution.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the failure.

lambdaFunctionScheduleFailedEventDetails -> (structure)

Contains details about a failed Lambda function schedule event that occurred during an execution.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the failure.

lambdaFunctionScheduledEventDetails -> (structure)

Contains details about a Lambda function scheduled during an execution.

resource -> (string)

The Amazon Resource Name (ARN) of the scheduled Lambda function.

input -> (string)

The JSON data input to the Lambda function. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.

inputDetails -> (structure)

Contains details about input for an execution history event.

truncated -> (boolean)

Indicates whether input or output was truncated in the response. Always `false` for API calls. In CloudWatch logs, the value will be true if the data is truncated due to size limits.

timeoutInSeconds -> (long)

The maximum allowed duration of the Lambda function.

taskCredentials -> (structure)

The credentials that Step Functions uses for the task.

roleArn -> (string)

The ARN of an IAM role that Step Functions assumes for the task. The role can allow cross-account access to resources.

lambdaFunctionStartFailedEventDetails -> (structure)

Contains details about a lambda function that failed to start during an execution.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the failure.

lambdaFunctionSucceededEventDetails -> (structure)

Contains details about a Lambda function that terminated successfully during an execution.

output -> (string)

The JSON data output by the Lambda function. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.

outputDetails -> (structure)

Contains details about the output of an execution history event.

truncated -> (boolean)

Indicates whether input or output was truncated in the response. Always `false` for API calls. In CloudWatch logs, the value will be true if the data is truncated due to size limits.

lambdaFunctionTimedOutEventDetails -> (structure)

Contains details about a Lambda function timeout that occurred during an execution.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the timeout.

stateEnteredEventDetails -> (structure)

Contains details about a state entered during an execution.

name -> (string)

The name of the state.

input -> (string)

The string that contains the JSON input data for the state. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.

inputDetails -> (structure)

Contains details about the input for an execution history event.

truncated -> (boolean)

Indicates whether input or output was truncated in the response. Always `false` for API calls. In CloudWatch logs, the value will be true if the data is truncated due to size limits.

stateExitedEventDetails -> (structure)

Contains details about an exit from a state during an execution.

name -> (string)

The name of the state.

A name must *not* contain:

- white space
- brackets `< > { } [ ]`
- wildcard characters `? *`
- special characters `" # % \ ^ | ~ ` $ & , ; : /`
- control characters (`U+0000-001F` , `U+007F-009F` )

To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.

output -> (string)

The JSON output data of the state. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.

outputDetails -> (structure)

Contains details about the output of an execution history event.

truncated -> (boolean)

Indicates whether input or output was truncated in the response. Always `false` for API calls. In CloudWatch logs, the value will be true if the data is truncated due to size limits.

assignedVariables -> (map)

Map of variable name and value as a serialized JSON representation.

key -> (string)

value -> (string)

assignedVariablesDetails -> (structure)

Provides details about input or output in an execution history event.

truncated -> (boolean)

Indicates whether assigned variables were truncated in the response. Always `false` for API calls. In CloudWatch logs, the value will be true if the data is truncated due to size limits.

mapRunStartedEventDetails -> (structure)

Contains details, such as `mapRunArn` , and the start date and time of a Map Run. `mapRunArn` is the Amazon Resource Name (ARN) of the Map Run that was started.

mapRunArn -> (string)

The Amazon Resource Name (ARN) of a Map Run that was started.

mapRunFailedEventDetails -> (structure)

Contains error and cause details about a Map Run that failed.

error -> (string)

The error code of the Map Run failure.

cause -> (string)

A more detailed explanation of the cause of the failure.

mapRunRedrivenEventDetails -> (structure)

Contains details about the redrive attempt of a Map Run.

mapRunArn -> (string)

The Amazon Resource Name (ARN) of a Map Run that was redriven.

redriveCount -> (integer)

The number of times the Map Run has been redriven at this point in the executionâs history including this event. The redrive count for a redriven Map Run is always greater than 0.

evaluationFailedEventDetails -> (structure)

Contains details about an evaluation failure that occurred while processing a state.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the failure.

location -> (string)

The location of the field in the state in which the evaluation error occurred.

state -> (string)

The name of the state in which the evaluation error occurred.

nextToken -> (string)

If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.