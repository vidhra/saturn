# start-change-request-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-change-request-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-change-request-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# start-change-request-execution

## Description

Creates a change request for Change Manager. The Automation runbooks specified in the change request run only after all required approvals for the change request have been received.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/StartChangeRequestExecution)

## Synopsis

```
start-change-request-execution
[--scheduled-time <value>]
--document-name <value>
[--document-version <value>]
[--parameters <value>]
[--change-request-name <value>]
[--client-token <value>]
[--auto-approve | --no-auto-approve]
--runbooks <value>
[--tags <value>]
[--scheduled-end-time <value>]
[--change-details <value>]
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

`--scheduled-time` (timestamp)

The date and time specified in the change request to run the Automation runbooks.

### Note

The Automation runbooks specified for the runbook workflow canât run until all required approvals for the change request have been received.

`--document-name` (string)

The name of the change template document to run during the runbook workflow.

`--document-version` (string)

The version of the change template document to run during the runbook workflow.

`--parameters` (map)

A key-value map of parameters that match the declared parameters in the change template document.

key -> (string)

value -> (list)

(string)

Shorthand Syntax:

```
KeyName1=string,string,KeyName2=string,string
```

JSON Syntax:

```
{"string": ["string", ...]
  ...}
```

`--change-request-name` (string)

The name of the change request associated with the runbook workflow to be run.

`--client-token` (string)

The user-provided idempotency token. The token must be unique, is case insensitive, enforces the UUID format, and canât be reused.

`--auto-approve` | `--no-auto-approve` (boolean)

Indicates whether the change request can be approved automatically without the need for manual approvals.

If `AutoApprovable` is enabled in a change template, then setting `AutoApprove` to `true` in `StartChangeRequestExecution` creates a change request that bypasses approver review.

### Note

Change Calendar restrictions are not bypassed in this scenario. If the state of an associated calendar is `CLOSED` , change freeze approvers must still grant permission for this change request to run. If they donât, the change wonât be processed until the calendar state is again `OPEN` .

`--runbooks` (list)

Information about the Automation runbooks that are run during the runbook workflow.

### Note

The Automation runbooks specified for the runbook workflow canât run until all required approvals for the change request have been received.

(structure)

Information about an Automation runbook used in a runbook workflow in Change Manager.

### Note

The Automation runbooks specified for the runbook workflow canât run until all required approvals for the change request have been received.

DocumentName -> (string)

The name of the Automation runbook used in a runbook workflow.

DocumentVersion -> (string)

The version of the Automation runbook used in a runbook workflow.

Parameters -> (map)

The key-value map of execution parameters, which were supplied when calling `StartChangeRequestExecution` .

key -> (string)

value -> (list)

(string)

TargetParameterName -> (string)

The name of the parameter used as the target resource for the rate-controlled runbook workflow. Required if you specify `Targets` .

Targets -> (list)

A key-value mapping to target resources that the runbook operation performs tasks on. Required if you specify `TargetParameterName` .

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

TargetMaps -> (list)

A key-value mapping of runbook parameters to target resources. Both Targets and TargetMaps canât be specified together.

(map)

key -> (string)

value -> (list)

(string)

MaxConcurrency -> (string)

The `MaxConcurrency` value specified by the user when the operation started, indicating the maximum number of resources that the runbook operation can run on at the same time.

MaxErrors -> (string)

The `MaxErrors` value specified by the user when the execution started, indicating the maximum number of errors that can occur during the operation before the updates are stopped or rolled back.

TargetLocations -> (list)

Information about the Amazon Web Services Regions and Amazon Web Services accounts targeted by the current Runbook operation.

(structure)

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

JSON Syntax:

```
[
  {
    "DocumentName": "string",
    "DocumentVersion": "string",
    "Parameters": {"string": ["string", ...]
      ...},
    "TargetParameterName": "string",
    "Targets": [
      {
        "Key": "string",
        "Values": ["string", ...]
      }
      ...
    ],
    "TargetMaps": [
      {"string": ["string", ...]
        ...}
      ...
    ],
    "MaxConcurrency": "string",
    "MaxErrors": "string",
    "TargetLocations": [
      {
        "Accounts": ["string", ...],
        "Regions": ["string", ...],
        "TargetLocationMaxConcurrency": "string",
        "TargetLocationMaxErrors": "string",
        "ExecutionRoleName": "string",
        "TargetLocationAlarmConfiguration": {
          "IgnorePollAlarmFailure": true|false,
          "Alarms": [
            {
              "Name": "string"
            }
            ...
          ]
        },
        "IncludeChildOrganizationUnits": true|false,
        "ExcludeAccounts": ["string", ...],
        "Targets": [
          {
            "Key": "string",
            "Values": ["string", ...]
          }
          ...
        ],
        "TargetsMaxConcurrency": "string",
        "TargetsMaxErrors": "string"
      }
      ...
    ]
  }
  ...
]
```

`--tags` (list)

Optional metadata that you assign to a resource. You can specify a maximum of five tags for a change request. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a change request to identify an environment or target Amazon Web Services Region. In this case, you could specify the following key-value pairs:

- `Key=Environment,Value=Production`
- `Key=Region,Value=us-east-2`

### Note

The `Array Members` maximum value is reported as 1000. This number includes capacity reserved for internal operations. When calling the `StartChangeRequestExecution` action, you can specify a maximum of 5 tags. You can, however, use the  AddTagsToResource action to add up to a total of 50 tags to an existing change request configuration.

(structure)

Metadata that you assign to your Amazon Web Services resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Amazon Web Services Systems Manager, you can apply tags to Systems Manager documents (SSM documents), managed nodes, maintenance windows, parameters, patch baselines, OpsItems, and OpsMetadata.

Key -> (string)

The name of the tag.

Value -> (string)

The value of the tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--scheduled-end-time` (timestamp)

The time that the requester expects the runbook workflow related to the change request to complete. The time is an estimate only that the requester provides for reviewers.

`--change-details` (string)

User-provided details about the change. If no details are provided, content specified in the **Template information** section of the associated change template is added.

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

**Example 1: To start a change request**

The following `start-change-request-execution` example starts a change request with minimal options specified.

```
aws ssm start-change-request-execution \
    --change-request-name MyChangeRequest \
    --document-name AWS-HelloWorldChangeTemplate \
    --runbooks '[{"DocumentName": "AWS-HelloWorld","Parameters": {"AutomationAssumeRole": ["arn:aws:iam:us-east-2:1112223233444:role/MyChangeManagerAssumeRole"]}}]' \
    --parameters Approver="JohnDoe",ApproverType="IamUser",ApproverSnsTopicArn="arn:aws:sns:us-east-2:1112223233444:MyNotificationTopic"
```

Output:

```
{
  "AutomationExecutionId": "9d32a4fc-f944-11e6-4105-0a1b2EXAMPLE"
}
```

**Example 2: To start a change request using an external JSON file**

The following `start-automation-execution` example starts a change request with multiple options specified in a JSON file.

```
aws ssm start-change-request-execution \
    --cli-input-json file://MyChangeRequest.json
```

Contents of `MyChangeRequest.json`:

```
{
    "ChangeRequestName": "MyChangeRequest",
    "DocumentName": "AWS-HelloWorldChangeTemplate",
    "DocumentVersion": "$DEFAULT",
    "ScheduledTime": "2021-12-30T03:00:00",
    "ScheduledEndTime": "2021-12-30T03:05:00",
    "Tags": [
        {
            "Key": "Purpose",
            "Value": "Testing"
        }
    ],
    "Parameters": {
        "Approver": [
            "JohnDoe"
        ],
        "ApproverType": [
            "IamUser"
        ],
        "ApproverSnsTopicArn": [
            "arn:aws:sns:us-east-2:111222333444;:MyNotificationTopic
        ]
    },
    "Runbooks": [
        {
            "DocumentName": "AWS-HelloWorld",
            "DocumentVersion": "1",
            "MaxConcurrency": "1",
            "MaxErrors": "1",
            "Parameters": {
                "AutomationAssumeRole": [
                    "arn:aws:iam::111222333444:role/MyChangeManagerAssumeRole"
                ]
            }
        }
    ],
    "ChangeDetails": "### Document Name: HelloWorldChangeTemplate\n\n## What does this document do?\nThis change template demonstrates the feature set available for creating change templates for Change Manager. This template starts a Runbook workflow for the Automation document called AWS-HelloWorld.\n\n## Input Parameters\n* ApproverSnsTopicArn: (Required) Amazon Simple Notification Service ARN for approvers.\n* Approver: (Required) The name of the approver to send this request to.\n* ApproverType: (Required) The type of reviewer.\n  * Allowed Values: IamUser, IamGroup, IamRole, SSOGroup, SSOUser\n\n## Output Parameters\nThis document has no outputs \n"
}
```

Output:

```
{
  "AutomationExecutionId": "9d32a4fc-f944-11e6-4105-0a1b2EXAMPLE"
}
```

For more information, see [Creating change requests](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-requests-create.html) in the *AWS Systems Manager User Guide*.

## Output

AutomationExecutionId -> (string)

The unique ID of a runbook workflow operation. (A runbook workflow is a type of Automation operation.)