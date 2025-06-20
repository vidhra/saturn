# describe-workflow-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-workflow-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-workflow-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [swf](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/index.html#cli-aws-swf) ]

# describe-workflow-type

## Description

Returns information about the specified *workflow type* . This includes configuration settings specified when the type was registered and other information such as creation date, current status, etc.

**Access Control**

You can use IAM policies to control this actionâs access to Amazon SWF resources as follows:

- Use a `Resource` element with the domain name to limit the action to only specified domains.
- Use an `Action` element to allow or deny permission to call this action.
- Constrain the following parameters by using a `Condition` element with the appropriate keys.
- `workflowType.name` : String constraint. The key is `swf:workflowType.name` .
- `workflowType.version` : String constraint. The key is `swf:workflowType.version` .

If the caller doesnât have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attributeâs `cause` parameter is set to `OPERATION_NOT_PERMITTED` . For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/swf-2012-01-25/DescribeWorkflowType)

## Synopsis

```
describe-workflow-type
--domain <value>
--workflow-type <value>
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

The name of the domain in which this workflow type is registered.

`--workflow-type` (structure)

The workflow type to describe.

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

typeInfo -> (structure)

General information about the workflow type.

The status of the workflow type (returned in the WorkflowTypeInfo structure) can be one of the following.

- `REGISTERED` â The type is registered and available. Workers supporting this type should be running.
- `DEPRECATED` â The type was deprecated using  DeprecateWorkflowType , but is still in use. You should keep workers supporting this type running. You cannot create new workflow executions of this type.

workflowType -> (structure)

The workflow type this information is about.

name -> (string)

The name of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

version -> (string)

The version of the workflow type.

### Note

The combination of workflow type name and version must be unique with in a domain.

status -> (string)

The current status of the workflow type.

description -> (string)

The description of the type registered through  RegisterWorkflowType .

creationDate -> (timestamp)

The date when this type was registered.

deprecationDate -> (timestamp)

If the type is in deprecated state, then it is set to the date when the type was deprecated.

configuration -> (structure)

Configuration settings of the workflow type registered through  RegisterWorkflowType

defaultTaskStartToCloseTimeout -> (string)

The default maximum duration, specified when registering the workflow type, that a decision task for executions of this workflow type might take before returning completion or failure. If the task doesnâtdo close in the specified time then the task is automatically timed out and rescheduled. If the decider eventually reports a completion or failure, it is ignored. This default can be overridden when starting a workflow execution using the  StartWorkflowExecution action or the `StartChildWorkflowExecution`   Decision .

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

defaultExecutionStartToCloseTimeout -> (string)

The default maximum duration, specified when registering the workflow type, for executions of this workflow type. This default can be overridden when starting a workflow execution using the  StartWorkflowExecution action or the `StartChildWorkflowExecution`   Decision .

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

defaultTaskList -> (structure)

The default task list, specified when registering the workflow type, for decisions tasks scheduled for workflow executions of this type. This default can be overridden when starting a workflow execution using the  StartWorkflowExecution action or the `StartChildWorkflowExecution`   Decision .

name -> (string)

The name of the task list.

defaultTaskPriority -> (string)

The default task priority, specified when registering the workflow type, for all decision tasks of this workflow type. This default can be overridden when starting a workflow execution using the  StartWorkflowExecution action or the `StartChildWorkflowExecution` decision.

Valid values are integers that range from Javaâs `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.

For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *Amazon SWF Developer Guide* .

defaultChildPolicy -> (string)

The default policy to use for the child workflow executions when a workflow execution of this type is terminated, by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout. This default can be overridden when starting a workflow execution using the  StartWorkflowExecution action or the `StartChildWorkflowExecution`   Decision .

The supported child policies are:

- `TERMINATE` â The child executions are terminated.
- `REQUEST_CANCEL` â A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
- `ABANDON` â No action is taken. The child executions continue to run.

defaultLambdaRole -> (string)

The default IAM role attached to this workflow type.

### Note

Executions of this workflow type need IAM roles to invoke Lambda functions. If you donât specify an IAM role when starting this workflow type, the default Lambda role is attached to the execution. For more information, see [https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html](https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html) in the *Amazon SWF Developer Guide* .