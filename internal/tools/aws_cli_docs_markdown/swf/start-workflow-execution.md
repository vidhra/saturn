# start-workflow-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/start-workflow-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/start-workflow-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [swf](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/index.html#cli-aws-swf) ]

# start-workflow-execution

## Description

Starts an execution of the workflow type in the specified domain using the provided `workflowId` and input data.

This action returns the newly started workflow execution.

**Access Control**

You can use IAM policies to control this actionâs access to Amazon SWF resources as follows:

- Use a `Resource` element with the domain name to limit the action to only specified domains.
- Use an `Action` element to allow or deny permission to call this action.
- Constrain the following parameters by using a `Condition` element with the appropriate keys.
- `tagList.member.0` : The key is `swf:tagList.member.0` .
- `tagList.member.1` : The key is `swf:tagList.member.1` .
- `tagList.member.2` : The key is `swf:tagList.member.2` .
- `tagList.member.3` : The key is `swf:tagList.member.3` .
- `tagList.member.4` : The key is `swf:tagList.member.4` .
- `taskList` : String constraint. The key is `swf:taskList.name` .
- `workflowType.name` : String constraint. The key is `swf:workflowType.name` .
- `workflowType.version` : String constraint. The key is `swf:workflowType.version` .

If the caller doesnât have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attributeâs `cause` parameter is set to `OPERATION_NOT_PERMITTED` . For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/swf-2012-01-25/StartWorkflowExecution)

## Synopsis

```
start-workflow-execution
--domain <value>
--workflow-id <value>
--workflow-type <value>
[--task-list <value>]
[--task-priority <value>]
[--input <value>]
[--execution-start-to-close-timeout <value>]
[--tag-list <value>]
[--task-start-to-close-timeout <value>]
[--child-policy <value>]
[--lambda-role <value>]
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

The name of the domain in which the workflow execution is created.

The specified string must not contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control characters (`\u0000-\u001f` | `\u007f-\u009f` ). Also, it must *not* be the literal string `arn` .

`--workflow-id` (string)

The user defined identifier associated with the workflow execution. You can use this to associate a custom identifier with the workflow execution. You may specify the same identifier if a workflow execution is logically a *restart* of a previous execution. You cannot have two open workflow executions with the same `workflowId` at the same time within the same domain.

The specified string must not contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control characters (`\u0000-\u001f` | `\u007f-\u009f` ). Also, it must *not* be the literal string `arn` .

`--workflow-type` (structure)

The type of the workflow to start.

name -> (string)

The name of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

version -> (string)

The version of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

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

`--task-list` (structure)

The task list to use for the decision tasks generated for this workflow execution. This overrides the `defaultTaskList` specified when registering the workflow type.

### Note

A task list for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task list was specified at registration time then a fault is returned.

The specified string must not contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control characters (`\u0000-\u001f` | `\u007f-\u009f` ). Also, it must *not* be the literal string `arn` .

name -> (string)

The name of the task list.

Shorthand Syntax:

```
name=string
```

JSON Syntax:

```
{
  "name": "string"
}
```

`--task-priority` (string)

The task priority to use for this workflow execution. This overrides any default priority that was assigned when the workflow type was registered. If not set, then the default task priority for the workflow type is used. Valid values are integers that range from Javaâs `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.

For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *Amazon SWF Developer Guide* .

`--input` (string)

The input for the workflow execution. This is a free form string which should be meaningful to the workflow you are starting. This `input` is made available to the new workflow execution in the `WorkflowExecutionStarted` history event.

`--execution-start-to-close-timeout` (string)

The total duration for this workflow execution. This overrides the defaultExecutionStartToCloseTimeout specified when registering the workflow type.

The duration is specified in seconds; an integer greater than or equal to `0` . Exceeding this limit causes the workflow execution to time out. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of âNONEâ for this timeout; there is a one-year max limit on the time that a workflow execution can run.

### Note

An execution start-to-close timeout must be specified either through this parameter or as a default when the workflow type is registered. If neither this parameter nor a default execution start-to-close timeout is specified, a fault is returned.

`--tag-list` (list)

The list of tags to associate with the workflow execution. You can specify a maximum of 5 tags. You can list workflow executions with a specific tag by calling  ListOpenWorkflowExecutions or  ListClosedWorkflowExecutions and specifying a  TagFilter .

(string)

Syntax:

```
"string" "string" ...
```

`--task-start-to-close-timeout` (string)

Specifies the maximum duration of decision tasks for this workflow execution. This parameter overrides the `defaultTaskStartToCloseTimout` specified when registering the workflow type using  RegisterWorkflowType .

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

### Note

A task start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task start-to-close timeout was specified at registration time then a fault is returned.

`--child-policy` (string)

If set, specifies the policy to use for the child workflow executions of this workflow execution if it is terminated, by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout. This policy overrides the default child policy specified when registering the workflow type using  RegisterWorkflowType .

The supported child policies are:

- `TERMINATE` â The child executions are terminated.
- `REQUEST_CANCEL` â A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
- `ABANDON` â No action is taken. The child executions continue to run.

### Note

A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault is returned.

Possible values:

- `TERMINATE`
- `REQUEST_CANCEL`
- `ABANDON`

`--lambda-role` (string)

The IAM role to attach to this workflow execution.

### Note

Executions of this workflow type need IAM roles to invoke Lambda functions. If you donât attach an IAM role, any attempt to schedule a Lambda task fails. This results in a `ScheduleLambdaFunctionFailed` history event. For more information, see [https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html](https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html) in the *Amazon SWF Developer Guide* .

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

runId -> (string)

The `runId` of a workflow execution. This ID is generated by the service and can be used to uniquely identify the workflow execution within a domain.