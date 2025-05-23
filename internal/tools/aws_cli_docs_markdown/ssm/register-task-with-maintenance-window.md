# register-task-with-maintenance-windowÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-task-with-maintenance-window.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-task-with-maintenance-window.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# register-task-with-maintenance-window

## Description

Adds a new task to a maintenance window.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/RegisterTaskWithMaintenanceWindow)

## Synopsis

```
register-task-with-maintenance-window
--window-id <value>
[--targets <value>]
--task-arn <value>
[--service-role-arn <value>]
--task-type <value>
[--task-parameters <value>]
[--task-invocation-parameters <value>]
[--priority <value>]
[--max-concurrency <value>]
[--max-errors <value>]
[--logging-info <value>]
[--name <value>]
[--description <value>]
[--client-token <value>]
[--cutoff-behavior <value>]
[--alarm-configuration <value>]
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

`--window-id` (string)

The ID of the maintenance window the task should be added to.

`--targets` (list)

The targets (either managed nodes or maintenance window targets).

### Note

One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, Lambda, and Step Functions). For more information about running tasks that donât specify targets, see [Registering maintenance window tasks without targets](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) in the *Amazon Web Services Systems Manager User Guide* .

Specify managed nodes using the following format:

`Key=InstanceIds,Values=<instance-id-1>,<instance-id-2>`

Specify maintenance window targets using the following format:

`Key=WindowTargetIds,Values=<window-target-id-1>,<window-target-id-2>`

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

Shorthand Syntax:

```
Key=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Values": ["string", ...]
  }
  ...
]
```

`--task-arn` (string)

The ARN of the task to run.

`--service-role-arn` (string)

The Amazon Resource Name (ARN) of the IAM service role for Amazon Web Services Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run `RegisterTaskWithMaintenanceWindow` .

However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see [Setting up Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html) in the in the *Amazon Web Services Systems Manager User Guide* .

`--task-type` (string)

The type of task being registered.

Possible values:

- `RUN_COMMAND`
- `AUTOMATION`
- `STEP_FUNCTIONS`
- `LAMBDA`

`--task-parameters` (map)

The parameters that should be passed to the task when it is run.

### Note

`TaskParameters` has been deprecated. To specify parameters to pass to a task when it runs, instead use the `Parameters` option in the `TaskInvocationParameters` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .

key -> (string)

value -> (structure)

Defines the values for a task parameter.

Values -> (list)

This field contains an array of 0 or more strings, each 1 to 255 characters in length.

(string)

Shorthand Syntax:

```
KeyName1=Values=string,string,KeyName2=Values=string,string
```

JSON Syntax:

```
{"string": {
      "Values": ["string", ...]
    }
  ...}
```

`--task-invocation-parameters` (structure)

The parameters that the task should use during execution. Populate only the fields that match the task type. All other fields should be empty.

RunCommand -> (structure)

The parameters for a `RUN_COMMAND` task type.

Comment -> (string)

Information about the commands to run.

CloudWatchOutputConfig -> (structure)

Configuration options for sending command output to Amazon CloudWatch Logs.

CloudWatchLogGroupName -> (string)

The name of the CloudWatch Logs log group where you want to send command output. If you donât specify a group name, Amazon Web Services Systems Manager automatically creates a log group for you. The log group uses the following naming format:

[``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-task-with-maintenance-window.html#id1)aws/ssm/*SystemsManagerDocumentName* ``

CloudWatchOutputEnabled -> (boolean)

Enables Systems Manager to send command output to CloudWatch Logs.

DocumentHash -> (string)

The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.

DocumentHashType -> (string)

SHA-256 or SHA-1. SHA-1 hashes have been deprecated.

DocumentVersion -> (string)

The Amazon Web Services Systems Manager document (SSM document) version to use in the request. You can specify `$DEFAULT` , `$LATEST` , or a specific version number. If you run commands by using the Amazon Web Services CLI, then you must escape the first two options by using a backslash. If you specify a version number, then you donât need to use the backslash. For example:

`--document-version "\$DEFAULT"`

`--document-version "\$LATEST"`

`--document-version "3"`

NotificationConfig -> (structure)

Configurations for sending notifications about command status changes on a per-managed node basis.

NotificationArn -> (string)

An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic. Run Command pushes notifications about command status changes to this topic.

NotificationEvents -> (list)

The different events for which you can receive notifications. To learn more about these events, see [Monitoring Systems Manager status changes using Amazon SNS notifications](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-notifications.html) in the *Amazon Web Services Systems Manager User Guide* .

(string)

NotificationType -> (string)

The type of notification.

- `Command` : Receive notification when the status of a command changes.
- `Invocation` : For commands sent to multiple managed nodes, receive notification on a per-node basis when the status of a command changes.

OutputS3BucketName -> (string)

The name of the Amazon Simple Storage Service (Amazon S3) bucket.

OutputS3KeyPrefix -> (string)

The S3 bucket subfolder.

Parameters -> (map)

The parameters for the `RUN_COMMAND` task execution.

key -> (string)

value -> (list)

(string)

ServiceRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM service role for Amazon Web Services Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run `RegisterTaskWithMaintenanceWindow` .

However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see [Setting up Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html) in the in the *Amazon Web Services Systems Manager User Guide* .

TimeoutSeconds -> (integer)

If this time is reached and the command hasnât already started running, it doesnât run.

Automation -> (structure)

The parameters for an `AUTOMATION` task type.

DocumentVersion -> (string)

The version of an Automation runbook to use during task execution.

Parameters -> (map)

The parameters for the `AUTOMATION` task.

For information about specifying and updating task parameters, see  RegisterTaskWithMaintenanceWindow and  UpdateMaintenanceWindowTask .

### Note

`LoggingInfo` has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the `TaskInvocationParameters` structure. For information about how Amazon Web Services Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .

`TaskParameters` has been deprecated. To specify parameters to pass to a task when it runs, instead use the `Parameters` option in the `TaskInvocationParameters` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .

For `AUTOMATION` task types, Amazon Web Services Systems Manager ignores any values specified for these parameters.

key -> (string)

value -> (list)

(string)

StepFunctions -> (structure)

The parameters for a `STEP_FUNCTIONS` task type.

Input -> (string)

The inputs for the `STEP_FUNCTIONS` task.

Name -> (string)

The name of the `STEP_FUNCTIONS` task.

Lambda -> (structure)

The parameters for a `LAMBDA` task type.

ClientContext -> (string)

Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.

Qualifier -> (string)

(Optional) Specify an Lambda function version or alias name. If you specify a function version, the operation uses the qualified function Amazon Resource Name (ARN) to invoke a specific Lambda function. If you specify an alias name, the operation uses the alias ARN to invoke the Lambda function version to which the alias points.

Payload -> (blob)

JSON to provide to your Lambda function as input.

JSON Syntax:

```
{
  "RunCommand": {
    "Comment": "string",
    "CloudWatchOutputConfig": {
      "CloudWatchLogGroupName": "string",
      "CloudWatchOutputEnabled": true|false
    },
    "DocumentHash": "string",
    "DocumentHashType": "Sha256"|"Sha1",
    "DocumentVersion": "string",
    "NotificationConfig": {
      "NotificationArn": "string",
      "NotificationEvents": ["All"|"InProgress"|"Success"|"TimedOut"|"Cancelled"|"Failed", ...],
      "NotificationType": "Command"|"Invocation"
    },
    "OutputS3BucketName": "string",
    "OutputS3KeyPrefix": "string",
    "Parameters": {"string": ["string", ...]
      ...},
    "ServiceRoleArn": "string",
    "TimeoutSeconds": integer
  },
  "Automation": {
    "DocumentVersion": "string",
    "Parameters": {"string": ["string", ...]
      ...}
  },
  "StepFunctions": {
    "Input": "string",
    "Name": "string"
  },
  "Lambda": {
    "ClientContext": "string",
    "Qualifier": "string",
    "Payload": blob
  }
}
```

`--priority` (integer)

The priority of the task in the maintenance window, the lower the number the higher the priority. Tasks in a maintenance window are scheduled in priority order with tasks that have the same priority scheduled in parallel.

`--max-concurrency` (string)

The maximum number of targets this task can be run for, in parallel.

### Note

Although this element is listed as âRequired: Noâ, a value can be omitted only when you are registering or updating a [targetless task](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) You must provide a value in all other cases.

For maintenance window tasks without a target specified, you canât supply a value for this option. Instead, the system inserts a placeholder value of `1` . This value doesnât affect the running of your task.

`--max-errors` (string)

The maximum number of errors allowed before this task stops being scheduled.

### Note

Although this element is listed as âRequired: Noâ, a value can be omitted only when you are registering or updating a [targetless task](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) You must provide a value in all other cases.

For maintenance window tasks without a target specified, you canât supply a value for this option. Instead, the system inserts a placeholder value of `1` . This value doesnât affect the running of your task.

`--logging-info` (structure)

A structure containing information about an Amazon Simple Storage Service (Amazon S3) bucket to write managed node-level logs to.

### Note

`LoggingInfo` has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the `TaskInvocationParameters` structure. For information about how Amazon Web Services Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .

S3BucketName -> (string)

The name of an S3 bucket where execution logs are stored.

S3KeyPrefix -> (string)

(Optional) The S3 bucket subfolder.

S3Region -> (string)

The Amazon Web Services Region where the S3 bucket is located.

Shorthand Syntax:

```
S3BucketName=string,S3KeyPrefix=string,S3Region=string
```

JSON Syntax:

```
{
  "S3BucketName": "string",
  "S3KeyPrefix": "string",
  "S3Region": "string"
}
```

`--name` (string)

An optional name for the task.

`--description` (string)

An optional description for the task.

`--client-token` (string)

User-provided idempotency token.

`--cutoff-behavior` (string)

Indicates whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached.

- `CONTINUE_TASK` : When the cutoff time is reached, any tasks that are running continue. The default value.
- `CANCEL_TASK` :
- For Automation, Lambda, Step Functions tasks: When the cutoff time is reached, any task invocations that are already running continue, but no new task invocations are started.
- For Run Command tasks: When the cutoff time is reached, the system sends a  CancelCommand operation that attempts to cancel the command associated with the task. However, there is no guarantee that the command will be terminated and the underlying process stopped.

The status for tasks that are not completed is `TIMED_OUT` .

Possible values:

- `CONTINUE_TASK`
- `CANCEL_TASK`

`--alarm-configuration` (structure)

The CloudWatch alarm you want to apply to your maintenance window task.

IgnorePollAlarmFailure -> (boolean)

When this value is *true* , your automation or command continues to run in cases where we canât retrieve alarm status information from CloudWatch. In cases where we successfully retrieve an alarm status of OK or INSUFFICIENT_DATA, the automation or command continues to run, regardless of this value. Default is *false* .

Alarms -> (list)

The name of the CloudWatch alarm specified in the configuration.

(structure)

A CloudWatch alarm you apply to an automation or command.

Name -> (string)

The name of your CloudWatch alarm.

Shorthand Syntax:

```
IgnorePollAlarmFailure=boolean,Alarms=[{Name=string},{Name=string}]
```

JSON Syntax:

```
{
  "IgnorePollAlarmFailure": true|false,
  "Alarms": [
    {
      "Name": "string"
    }
    ...
  ]
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

**Example 1: To register an Automation task with a maintenance window**

The following `register-task-with-maintenance-window` example registers an Automation task with a maintenance window that is targeted at an instance.

```
aws ssm register-task-with-maintenance-window \
    --cli-binary-format raw-in-base64-out \
    --window-id "mw-082dcd7649EXAMPLE" \
    --targets Key=InstanceIds,Values=i-1234520122EXAMPLE \
    --task-arn AWS-RestartEC2Instance \
    --service-role-arn arn:aws:iam::111222333444:role/SSM --task-type AUTOMATION \
    --task-invocation-parameters "{\"Automation\":{\"DocumentVersion\":\"\$LATEST\",\"Parameters\":{\"InstanceId\":[\"{{RESOURCE_ID}}\"]}}}" \
    --priority 0 \
    --max-concurrency 1 \
    --max-errors 1 \
    --name "AutomationExample" \
    --description "Restarting EC2 Instance for maintenance"
```

Output:

```
{
    "WindowTaskId":"11144444-5555-6666-7777-88888888"
}
```

For more information, see [Register a Task with the Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-tasks.html) in the *AWS Systems Manager User Guide*.

**Example 2: To register a Lambda task with a Maintenance Window**

The following `register-task-with-maintenance-window` example registers a Lambda task with a Maintenance Window that is targeted at an instance.

```
aws ssm register-task-with-maintenance-window \
    --cli-binary-format raw-in-base64-out \
    --window-id "mw-082dcd7649dee04e4" \
    --targets Key=InstanceIds,Values=i-12344d305eEXAMPLE \
    --task-arn arn:aws:lambda:us-east-1:111222333444:function:SSMTestLAMBDA \
    --service-role-arn arn:aws:iam::111222333444:role/SSM \
    --task-type LAMBDA \
    --task-invocation-parameters '{"Lambda":{"Payload":"{\"InstanceId\":\"{{RESOURCE_ID}}\",\"targetType\":\"{{TARGET_TYPE}}\"}","Qualifier":"$LATEST"}}' \
    --priority 0 \
    --max-concurrency 10 \
    --max-errors 5 \
    --name "Lambda_Example" \
    --description "My Lambda Example"
```

Output:

```
{
    "WindowTaskId":"22244444-5555-6666-7777-88888888"
}
```

For more information, see [Register a Task with the Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-tasks.html) in the *AWS Systems Manager User Guide*.

**Example 3: To register a Run Command task with a maintenance window**

The following `register-task-with-maintenance-window` example registers a Run Command task with a maintenance window that is targeted at an instance.

```
aws ssm register-task-with-maintenance-window \
    --cli-binary-format raw-in-base64-out \
    --window-id "mw-082dcd7649dee04e4" \
    --targets "Key=InstanceIds,Values=i-12344d305eEXAMPLE" \
    --service-role-arn "arn:aws:iam::111222333444:role/SSM" \
    --task-type "RUN_COMMAND" \
    --name "SSMInstallPowerShellModule" \
    --task-arn "AWS-InstallPowerShellModule" \
    --task-invocation-parameters "{\"RunCommand\":{\"Comment\":\"\",\"OutputS3BucketName\":\"runcommandlogs\",\"Parameters\":{\"commands\":[\"Get-Module -ListAvailable\"],\"executionTimeout\":[\"3600\"],\"source\":[\"https:\/\/gallery.technet.microsoft.com\/EZOut-33ae0fb7\/file\/110351\/1\/EZOut.zip\"],\"workingDirectory\":[\"\\\\\"]},\"TimeoutSeconds\":600}}" \
    --max-concurrency 1 \
    --max-errors 1 \
    --priority 10
```

Output:

```
{
    "WindowTaskId":"33344444-5555-6666-7777-88888888"
}
```

For more information, see [Register a Task with the Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-tasks.html) in the *AWS Systems Manager User Guide*.

**Example 4: To register a Step Functions task with a maintenance window**

The following `register-task-with-maintenance-window` example registers a Step Functions task with a maintenance window that is targeted at an instance.

```
aws ssm register-task-with-maintenance-window \
    --cli-binary-format raw-in-base64-out \
    --window-id "mw-1234d787d6EXAMPLE" \
    --targets Key=WindowTargetIds,Values=12347414-69c3-49f8-95b8-ed2dcEXAMPLE \
    --task-arn arn:aws:states:us-east-1:111222333444:stateMachine:SSMTestStateMachine \
    --service-role-arn arn:aws:iam::111222333444:role/MaintenanceWindows \
    --task-type STEP_FUNCTIONS \
    --task-invocation-parameters '{"StepFunctions":{"Input":"{\"InstanceId\":\"{{RESOURCE_ID}}\"}"}}' \
    --priority 0 \
    --max-concurrency 10 \
    --max-errors 5 \
    --name "Step_Functions_Example" \
    --description "My Step Functions Example"
```

Output:

```
{
    "WindowTaskId":"44444444-5555-6666-7777-88888888"
}
```

For more information, see [Register a Task with the Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-tasks.html) in the *AWS Systems Manager User Guide*.

**Example 5: To register a task using a maintenance windows target ID**

The following `register-task-with-maintenance-window` example registers a task using a maintenance window target ID. The maintenance window target ID was in the output of the `aws ssm register-target-with-maintenance-window` command. You can also retrieve it from the output of the `aws ssm describe-maintenance-window-targets` command.

```
aws ssm register-task-with-maintenance-window \
    --cli-binary-format raw-in-base64-out \
    --targets "Key=WindowTargetIds,Values=350d44e6-28cc-44e2-951f-4b2c9EXAMPLE" \
    --task-arn "AWS-RunShellScript" \
    --service-role-arn "arn:aws:iam::111222333444:role/MaintenanceWindowsRole" \
    --window-id "mw-ab12cd34eEXAMPLE" \
    --task-type "RUN_COMMAND" \
    --task-parameters  "{\"commands\":{\"Values\":[\"df\"]}}" \
    --max-concurrency 1 \
    --max-errors 1 \
    --priority 10
```

Output:

```
{
    "WindowTaskId":"33344444-5555-6666-7777-88888888"
}
```

For more information, see [Register a Task with the Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-tasks.html) in the *AWS Systems Manager User Guide*.

## Output

WindowTaskId -> (string)

The ID of the task in the maintenance window.