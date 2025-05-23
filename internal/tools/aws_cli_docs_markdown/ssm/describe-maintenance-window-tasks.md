# describe-maintenance-window-tasksÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-tasks.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-tasks.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# describe-maintenance-window-tasks

## Description

Lists the tasks in a maintenance window.

### Note

For maintenance window tasks without a specified target, you canât supply values for `--max-errors` and `--max-concurrency` . Instead, the system inserts a placeholder value of `1` , which may be reported in the response to this command. These values donât affect the running of your task and can be ignored.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowTasks)

`describe-maintenance-window-tasks` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Tasks`

## Synopsis

```
describe-maintenance-window-tasks
--window-id <value>
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

`--window-id` (string)

The ID of the maintenance window whose tasks should be retrieved.

`--filters` (list)

Optional filters used to narrow down the scope of the returned tasks. The supported filter keys are `WindowTaskId` , `TaskArn` , `Priority` , and `TaskType` .

(structure)

Filter used in the request. Supported filter keys depend on the API operation that includes the filter. API operations that use `MaintenanceWindowFilter>` include the following:

- DescribeMaintenanceWindowExecutions
- DescribeMaintenanceWindowExecutionTaskInvocations
- DescribeMaintenanceWindowExecutionTasks
- DescribeMaintenanceWindows
- DescribeMaintenanceWindowTargets
- DescribeMaintenanceWindowTasks

Key -> (string)

The name of the filter.

Values -> (list)

The filter values.

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

**Example 1: To list all tasks for a maintenance window**

The following `describe-maintenance-window-tasks` example lists all of the tasks for the specified maintenance window.

```
aws ssm describe-maintenance-window-tasks \
    --window-id "mw-06cf17cbefEXAMPLE"
```

Output:

```
{
    "Tasks": [
        {
            "WindowId": "mw-06cf17cbefEXAMPLE",
            "WindowTaskId": "018b31c3-2d77-4b9e-bd48-c91edEXAMPLE",
            "TaskArn": "AWS-RestartEC2Instance",
            "TaskParameters": {},
            "Type": "AUTOMATION",
            "Description": "Restarting EC2 Instance for maintenance",
            "MaxConcurrency": "1",
            "MaxErrors": "1",
            "Name": "My-Automation-Example-Task",
            "Priority": 0,
            "ServiceRoleArn": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM",
            "Targets": [
                {
                    "Key": "WindowTargetIds",
                    "Values": [
                        "da89dcc3-7f9c-481d-ba2b-edcb7EXAMPLE"
                    ]
                }
            ]
        },
        {
            "WindowId": "mw-06cf17cbefEXAMPLE",
            "WindowTaskId": "1943dee0-0a17-4978-9bf4-3cc2fEXAMPLE",
            "TaskArn": "AWS-DisableS3BucketPublicReadWrite",
            "TaskParameters": {},
            "Type": "AUTOMATION",
            "Description": "Automation task to disable read/write access on public S3 buckets",
            "MaxConcurrency": "10",
            "MaxErrors": "5",
            "Name": "My-Disable-S3-Public-Read-Write-Access-Automation-Task",
            "Priority": 0,
            "ServiceRoleArn": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM",
            "Targets": [
                {
                    "Key": "WindowTargetIds",
                    "Values": [
                        "da89dcc3-7f9c-481d-ba2b-edcb7EXAMPLE"
                    ]
                }
            ]
        }
    ]
}
```

**Example 2: To list all tasks for a maintenance window that invokes the AWS-RunPowerShellScript command document**

The following `describe-maintenance-window-tasks` example lists all of the tasks for the specified maintenance window that invokes the `AWS-RunPowerShellScript` command document.

```
aws ssm describe-maintenance-window-tasks \
    --window-id "mw-ab12cd34eEXAMPLE" \
    --filters "Key=TaskArn,Values=AWS-RunPowerShellScript"
```

Output:

```
{
    "Tasks": [
        {
            "WindowId": "mw-ab12cd34eEXAMPLE",
            "WindowTaskId": "0d36e6b4-3a4f-411e-adcb-3558eEXAMPLE",
            "TaskArn": "AWS-RunPowerShellScript",
            "Type": "RUN_COMMAND",
            "Targets": [
                {
                    "Key": "WindowTargetIds",
                    "Values": [
                        "da89dcc3-7f9c-481d-ba2b-edcb7EXAMPLE"
                    ]
                }
            ],
            "TaskParameters": {},
            "Priority": 1,
            "ServiceRoleArn": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM",
            "MaxConcurrency": "1",
            "MaxErrors": "1",
            "Name": "MyTask"
        }
    ]
}
```

**Example 3: To list all tasks for a maintenance window that have a Priority of 3**

The following `describe-maintenance-window-tasks` example lists all of the tasks for the specified maintenance window that have a `Priority` of `3`.

```
aws ssm describe-maintenance-window-tasks \
    --window-id "mw-ab12cd34eEXAMPLE" \
    --filters "Key=Priority,Values=3"
```

Output:

```
{
    "Tasks": [
        {
            "WindowId": "mw-ab12cd34eEXAMPLE",
            "WindowTaskId": "0d36e6b4-3a4f-411e-adcb-3558eEXAMPLE",
            "TaskArn": "AWS-RunPowerShellScript",
            "Type": "RUN_COMMAND",
            "Targets": [
                {
                    "Key": "WindowTargetIds",
                    "Values": [
                        "da89dcc3-7f9c-481d-ba2b-edcb7EXAMPLE"
                    ]
                }
            ],
            "TaskParameters": {},
            "Priority": 3,
            "ServiceRoleArn": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM",
            "MaxConcurrency": "1",
            "MaxErrors": "1",
            "Name": "MyRunCommandTask"
        },
        {
            "WindowId": "mw-ab12cd34eEXAMPLE",
            "WindowTaskId": "ee45feff-ad65-4a6c-b478-5cab8EXAMPLE",
            "TaskArn": "AWS-RestartEC2Instance",
            "Type": "AUTOMATION",
            "Targets": [
                {
                    "Key": "WindowTargetIds",
                    "Values": [
                        "da89dcc3-7f9c-481d-ba2b-edcb7EXAMPLE"
                    ]
                }
            ],
            "TaskParameters": {},
            "Priority": 3,
            "ServiceRoleArn": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM",
            "MaxConcurrency": "10",
            "MaxErrors": "5",
            "Name": "My-Automation-Task",
            "Description": "A description for my Automation task"
        }
    ]
}
```

**Example 4: To list all tasks for a maintenance window that have a Priority of 1 and use Run Command**

This `describe-maintenance-window-tasks` example lists all of the tasks for the specified maintenance window that have a `Priority` of `1` and use `Run Command`.

```
aws ssm describe-maintenance-window-tasks \
    --window-id "mw-ab12cd34eEXAMPLE" \
    --filters "Key=Priority,Values=1" "Key=TaskType,Values=RUN_COMMAND"
```

Output:

```
{
    "Tasks": [
        {
            "WindowId": "mw-ab12cd34eEXAMPLE",
            "WindowTaskId": "0d36e6b4-3a4f-411e-adcb-3558eEXAMPLE",
            "TaskArn": "AWS-RunPowerShellScript",
            "Type": "RUN_COMMAND",
            "Targets": [
                {
                    "Key": "WindowTargetIds",
                    "Values": [
                        "da89dcc3-7f9c-481d-ba2b-edcb7EXAMPLE"
                    ]
                }
            ],
            "TaskParameters": {},
            "Priority": 1,
            "ServiceRoleArn": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM",
            "MaxConcurrency": "1",
            "MaxErrors": "1",
            "Name": "MyRunCommandTask"
        }
    ]
}
```

For more information, see [View information about maintenance windows (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-describe.html) in the *AWS Systems Manager User Guide*.

## Output

Tasks -> (list)

Information about the tasks in the maintenance window.

(structure)

Information about a task defined for a maintenance window.

WindowId -> (string)

The ID of the maintenance window where the task is registered.

WindowTaskId -> (string)

The task ID.

TaskArn -> (string)

The resource that the task uses during execution. For `RUN_COMMAND` and `AUTOMATION` task types, `TaskArn` is the Amazon Web Services Systems Manager (SSM document) name or ARN. For `LAMBDA` tasks, itâs the function name or ARN. For `STEP_FUNCTIONS` tasks, itâs the state machine ARN.

Type -> (string)

The type of task.

Targets -> (list)

The targets (either managed nodes or tags). Managed nodes are specified using `Key=instanceids,Values=<instanceid1>,<instanceid2>` . Tags are specified using `Key=<tag name>,Values=<tag value>` .

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

TaskParameters -> (map)

The parameters that should be passed to the task when it is run.

### Note

`TaskParameters` has been deprecated. To specify parameters to pass to a task when it runs, instead use the `Parameters` option in the `TaskInvocationParameters` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .

key -> (string)

value -> (structure)

Defines the values for a task parameter.

Values -> (list)

This field contains an array of 0 or more strings, each 1 to 255 characters in length.

(string)

Priority -> (integer)

The priority of the task in the maintenance window. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.

LoggingInfo -> (structure)

Information about an S3 bucket to write task-level logs to.

### Note

`LoggingInfo` has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the `OutputS3BucketName` and `OutputS3KeyPrefix` options in the `TaskInvocationParameters` structure. For information about how Amazon Web Services Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .

S3BucketName -> (string)

The name of an S3 bucket where execution logs are stored.

S3KeyPrefix -> (string)

(Optional) The S3 bucket subfolder.

S3Region -> (string)

The Amazon Web Services Region where the S3 bucket is located.

ServiceRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM service role for Amazon Web Services Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run `RegisterTaskWithMaintenanceWindow` .

However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see [Setting up Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html) in the in the *Amazon Web Services Systems Manager User Guide* .

MaxConcurrency -> (string)

The maximum number of targets this task can be run for, in parallel.

### Note

Although this element is listed as âRequired: Noâ, a value can be omitted only when you are registering or updating a [targetless task](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) You must provide a value in all other cases.

For maintenance window tasks without a target specified, you canât supply a value for this option. Instead, the system inserts a placeholder value of `1` . This value doesnât affect the running of your task.

MaxErrors -> (string)

The maximum number of errors allowed before this task stops being scheduled.

### Note

Although this element is listed as âRequired: Noâ, a value can be omitted only when you are registering or updating a [targetless task](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) You must provide a value in all other cases.

For maintenance window tasks without a target specified, you canât supply a value for this option. Instead, the system inserts a placeholder value of `1` . This value doesnât affect the running of your task.

Name -> (string)

The task name.

Description -> (string)

A description of the task.

CutoffBehavior -> (string)

The specification for whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached.

AlarmConfiguration -> (structure)

The details for the CloudWatch alarm applied to your maintenance window task.

IgnorePollAlarmFailure -> (boolean)

When this value is *true* , your automation or command continues to run in cases where we canât retrieve alarm status information from CloudWatch. In cases where we successfully retrieve an alarm status of OK or INSUFFICIENT_DATA, the automation or command continues to run, regardless of this value. Default is *false* .

Alarms -> (list)

The name of the CloudWatch alarm specified in the configuration.

(structure)

A CloudWatch alarm you apply to an automation or command.

Name -> (string)

The name of your CloudWatch alarm.

NextToken -> (string)

The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.