# describe-automation-step-executionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-automation-step-executions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-automation-step-executions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# describe-automation-step-executions

## Description

Information about all active and terminated step executions in an Automation workflow.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAutomationStepExecutions)

`describe-automation-step-executions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `StepExecutions`

## Synopsis

```
describe-automation-step-executions
--automation-execution-id <value>
[--filters <value>]
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

`--automation-execution-id` (string)

The Automation execution ID for which you want step execution descriptions.

`--filters` (list)

One or more filters to limit the number of step executions returned by the request.

(structure)

A filter to limit the amount of step execution information returned by the call.

Key -> (string)

One or more keys to limit the results.

Values -> (list)

The values of the filter key.

(string)

Shorthand Syntax:

```
Key=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Key": "StartTimeBefore"|"StartTimeAfter"|"StepExecutionStatus"|"StepExecutionId"|"StepName"|"Action"|"ParentStepExecutionId"|"ParentStepIteration"|"ParentStepIteratorValue",
    "Values": ["string", ...]
  }
  ...
]
```

`--reverse-order` | `--no-reverse-order` (boolean)

Indicates whether to list step executions in reverse order by start time. The default value is âfalseâ.

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

**Example 1: To describe all steps for an automation execution**

The following `describe-automation-step-executions` example displays details about the steps of an Automation execution.

```
aws ssm describe-automation-step-executions \
    --automation-execution-id 73c8eef8-f4ee-4a05-820c-e354fEXAMPLE
```

Output:

```
{
    "StepExecutions": [
        {
            "StepName": "startInstances",
            "Action": "aws:changeInstanceState",
            "ExecutionStartTime": 1583737234.134,
            "ExecutionEndTime": 1583737234.672,
            "StepStatus": "Success",
            "Inputs": {
                "DesiredState": "\"running\"",
                "InstanceIds": "[\"i-0cb99161f6EXAMPLE\"]"
            },
            "Outputs": {
                "InstanceStates": [
                    "running"
                ]
            },
            "StepExecutionId": "95e70479-cf20-4d80-8018-7e4e2EXAMPLE",
            "OverriddenParameters": {}
        }
    ]
}
```

**Example 2: To describe a specific step for an automation execution**

The following `describe-automation-step-executions` example displays details about a specific step of an Automation execution.

```
aws ssm describe-automation-step-executions \
    --automation-execution-id 73c8eef8-f4ee-4a05-820c-e354fEXAMPLE \
    --filters Key=StepExecutionId,Values=95e70479-cf20-4d80-8018-7e4e2EXAMPLE
```

For more information, see [Running an Automation Workflow Step by Step (Command Line)](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing-manually.html#automation-working-executing-manually-commandline) in the *AWS Systems Manager User Guide*.

## Output

StepExecutions -> (list)

A list of details about the current state of all steps that make up an execution.

(structure)

Detailed information about an the execution state of an Automation step.

StepName -> (string)

The name of this execution step.

Action -> (string)

The action this step performs. The action determines the behavior of the step.

TimeoutSeconds -> (long)

The timeout seconds of the step.

OnFailure -> (string)

The action to take if the step fails. The default value is `Abort` .

MaxAttempts -> (integer)

The maximum number of tries to run the action of the step. The default value is `1` .

ExecutionStartTime -> (timestamp)

If a step has begun execution, this contains the time the step started. If the step is in Pending status, this field isnât populated.

ExecutionEndTime -> (timestamp)

If a step has finished execution, this contains the time the execution ended. If the step hasnât yet concluded, this field isnât populated.

StepStatus -> (string)

The execution status for this step.

ResponseCode -> (string)

The response code returned by the execution of the step.

Inputs -> (map)

Fully-resolved values passed into the step before execution.

key -> (string)

value -> (string)

Outputs -> (map)

Returned values from the execution of the step.

key -> (string)

value -> (list)

(string)

Response -> (string)

A message associated with the response code for an execution.

FailureMessage -> (string)

If a step failed, this message explains why the execution failed.

FailureDetails -> (structure)

Information about the Automation failure.

FailureStage -> (string)

The stage of the Automation execution when the failure occurred. The stages include the following: InputValidation, PreVerification, Invocation, PostVerification.

FailureType -> (string)

The type of Automation failure. Failure types include the following: Action, Permission, Throttling, Verification, Internal.

Details -> (map)

Detailed information about the Automation step failure.

key -> (string)

value -> (list)

(string)

StepExecutionId -> (string)

The unique ID of a step execution.

OverriddenParameters -> (map)

A user-specified list of parameters to override when running a step.

key -> (string)

value -> (list)

(string)

IsEnd -> (boolean)

The flag which can be used to end automation no matter whether the step succeeds or fails.

NextStep -> (string)

The next step after the step succeeds.

IsCritical -> (boolean)

The flag which can be used to help decide whether the failure of current step leads to the Automation failure.

ValidNextSteps -> (list)

Strategies used when step fails, we support Continue and Abort. Abort will fail the automation when the step fails. Continue will ignore the failure of current step and allow automation to run the next step. With conditional branching, we add step:stepName to support the automation to go to another specific step.

(string)

Targets -> (list)

The targets for the step execution.

(structure)

An array of search criteria that targets managed nodes using a key-value pair that you specify.

### Note

One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, Lambda, and Step Functions). For more information about running tasks that donât specify targets, see [Registering maintenance window tasks without targets](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) in the *Amazon Web Services Systems Manager User Guide* .

Supported formats include the following.

**For all Systems Manager tools:**

- `Key=tag-key,Values=tag-value-1,tag-value-2`

**For Automation and Change Manager:**

- `Key=tag:tag-key,Values=tag-value`
- `Key=ResourceGroup,Values=resource-group-name`
- `Key=ParameterValues,Values=value-1,value-2,value-3`
- To target all instances in the Amazon Web Services Region:
- `Key=AWS::EC2::Instance,Values=*`
- `Key=InstanceIds,Values=*`

**For Run Command and Maintenance Windows:**

- `Key=InstanceIds,Values=instance-id-1,instance-id-2,instance-id-3`
- `Key=tag:tag-key,Values=tag-value-1,tag-value-2`
- `Key=resource-groups:Name,Values=resource-group-name`
- Additionally, Maintenance Windows support targeting resource types:
- `Key=resource-groups:ResourceTypeFilters,Values=resource-type-1,resource-type-2`

**For State Manager:**

- `Key=InstanceIds,Values=instance-id-1,instance-id-2,instance-id-3`
- `Key=tag:tag-key,Values=tag-value-1,tag-value-2`
- To target all instances in the Amazon Web Services Region:
- `Key=InstanceIds,Values=*`

For more information about how to send commands that target managed nodes using `Key,Value` parameters, see [Targeting multiple managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting) in the *Amazon Web Services Systems Manager User Guide* .

Key -> (string)

User-defined criteria for sending commands that target managed nodes that meet the criteria.

Values -> (list)

User-defined criteria that maps to `Key` . For example, if you specified `tag:ServerRole` , you could specify `value:WebServer` to run a command on instances that include EC2 tags of `ServerRole,WebServer` .

Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.

(string)

TargetLocation -> (structure)

The combination of Amazon Web Services Regions and Amazon Web Services accounts targeted by the current Automation execution.

Accounts -> (list)

The Amazon Web Services accounts targeted by the current Automation execution.

(string)

Regions -> (list)

The Amazon Web Services Regions targeted by the current Automation execution.

(string)

TargetLocationMaxConcurrency -> (string)

The maximum number of Amazon Web Services Regions and Amazon Web Services accounts allowed to run the Automation concurrently.

TargetLocationMaxErrors -> (string)

The maximum number of errors allowed before the system stops queueing additional Automation executions for the currently running Automation.

ExecutionRoleName -> (string)

The Automation execution role used by the currently running Automation. If not specified, the default value is `AWS-SystemsManager-AutomationExecutionRole` .

TargetLocationAlarmConfiguration -> (structure)

The details for the CloudWatch alarm you want to apply to an automation or command.

IgnorePollAlarmFailure -> (boolean)

When this value is *true* , your automation or command continues to run in cases where we canât retrieve alarm status information from CloudWatch. In cases where we successfully retrieve an alarm status of OK or INSUFFICIENT_DATA, the automation or command continues to run, regardless of this value. Default is *false* .

Alarms -> (list)

The name of the CloudWatch alarm specified in the configuration.

(structure)

A CloudWatch alarm you apply to an automation or command.

Name -> (string)

The name of your CloudWatch alarm.

IncludeChildOrganizationUnits -> (boolean)

Indicates whether to include child organizational units (OUs) that are children of the targeted OUs. The default is `false` .

ExcludeAccounts -> (list)

Amazon Web Services accounts or organizational units to exclude as expanded targets.

(string)

Targets -> (list)

A list of key-value mappings to target resources. If you specify values for this data type, you must also specify a value for `TargetParameterName` .

This `Targets` parameter takes precedence over the `StartAutomationExecution:Targets` parameter if both are supplied.

(structure)

An array of search criteria that targets managed nodes using a key-value pair that you specify.

### Note

One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, Lambda, and Step Functions). For more information about running tasks that donât specify targets, see [Registering maintenance window tasks without targets](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) in the *Amazon Web Services Systems Manager User Guide* .

Supported formats include the following.

**For all Systems Manager tools:**

- `Key=tag-key,Values=tag-value-1,tag-value-2`

**For Automation and Change Manager:**

- `Key=tag:tag-key,Values=tag-value`
- `Key=ResourceGroup,Values=resource-group-name`
- `Key=ParameterValues,Values=value-1,value-2,value-3`
- To target all instances in the Amazon Web Services Region:
- `Key=AWS::EC2::Instance,Values=*`
- `Key=InstanceIds,Values=*`

**For Run Command and Maintenance Windows:**

- `Key=InstanceIds,Values=instance-id-1,instance-id-2,instance-id-3`
- `Key=tag:tag-key,Values=tag-value-1,tag-value-2`
- `Key=resource-groups:Name,Values=resource-group-name`
- Additionally, Maintenance Windows support targeting resource types:
- `Key=resource-groups:ResourceTypeFilters,Values=resource-type-1,resource-type-2`

**For State Manager:**

- `Key=InstanceIds,Values=instance-id-1,instance-id-2,instance-id-3`
- `Key=tag:tag-key,Values=tag-value-1,tag-value-2`
- To target all instances in the Amazon Web Services Region:
- `Key=InstanceIds,Values=*`

For more information about how to send commands that target managed nodes using `Key,Value` parameters, see [Targeting multiple managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting) in the *Amazon Web Services Systems Manager User Guide* .

Key -> (string)

User-defined criteria for sending commands that target managed nodes that meet the criteria.

Values -> (list)

User-defined criteria that maps to `Key` . For example, if you specified `tag:ServerRole` , you could specify `value:WebServer` to run a command on instances that include EC2 tags of `ServerRole,WebServer` .

Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.

(string)

TargetsMaxConcurrency -> (string)

The maximum number of targets allowed to run this task in parallel. This `TargetsMaxConcurrency` takes precedence over the `StartAutomationExecution:MaxConcurrency` parameter if both are supplied.

TargetsMaxErrors -> (string)

The maximum number of errors that are allowed before the system stops running the automation on additional targets. This `TargetsMaxErrors` parameter takes precedence over the `StartAutomationExecution:MaxErrors` parameter if both are supplied.

TriggeredAlarms -> (list)

The CloudWatch alarms that were invoked by the automation.

(structure)

The details about the state of your CloudWatch alarm.

Name -> (string)

The name of your CloudWatch alarm.

State -> (string)

The state of your CloudWatch alarm.

ParentStepDetails -> (structure)

Information about the parent step.

StepExecutionId -> (string)

The unique ID of a step execution.

StepName -> (string)

The name of the step.

Action -> (string)

The name of the automation action.

Iteration -> (integer)

The current repetition of the loop represented by an integer.

IteratorValue -> (string)

The current value of the specified iterator in the loop.

NextToken -> (string)

The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.