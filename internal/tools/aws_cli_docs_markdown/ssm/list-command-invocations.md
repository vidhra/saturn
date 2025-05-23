# list-command-invocationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-command-invocations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-command-invocations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# list-command-invocations

## Description

An invocation is copy of a command sent to a specific managed node. A command can apply to one or more managed nodes. A command invocation applies to one managed node. For example, if a user runs `SendCommand` against three managed nodes, then a command invocation is created for each requested managed node ID. `ListCommandInvocations` provide status about command execution.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListCommandInvocations)

`list-command-invocations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `CommandInvocations`

## Synopsis

```
list-command-invocations
[--command-id <value>]
[--instance-id <value>]
[--filters <value>]
[--details | --no-details]
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

`--command-id` (string)

(Optional) The invocations for a specific command ID.

`--instance-id` (string)

(Optional) The command execution details for a specific managed node ID.

`--filters` (list)

(Optional) One or more filters. Use a filter to return a more specific list of results.

(structure)

Describes a command filter.

### Note

A managed node ID canât be specified when a command status is `Pending` because the command hasnât run on the node yet.

key -> (string)

The name of the filter.

### Note

The `ExecutionStage` filter canât be used with the `ListCommandInvocations` operation, only with `ListCommands` .

value -> (string)

The filter value. Valid values for each filter key are as follows:

- **InvokedAfter** : Specify a timestamp to limit your results. For example, specify `2024-07-07T00:00:00Z` to see a list of command executions occurring July 7, 2021, and later.
- **InvokedBefore** : Specify a timestamp to limit your results. For example, specify `2024-07-07T00:00:00Z` to see a list of command executions from before July 7, 2021.
- **Status** : Specify a valid command status to see a list of all command executions with that status. The status choices depend on the API you call. The status values you can specify for `ListCommands` are:
- `Pending`
- `InProgress`
- `Success`
- `Cancelled`
- `Failed`
- `TimedOut` (this includes both Delivery and Execution time outs)
- `AccessDenied`
- `DeliveryTimedOut`
- `ExecutionTimedOut`
- `Incomplete`
- `NoInstancesInTag`
- `LimitExceeded`

The status values you can specify for `ListCommandInvocations` are:

- `Pending`
- `InProgress`
- `Delayed`
- `Success`
- `Cancelled`
- `Failed`
- `TimedOut` (this includes both Delivery and Execution time outs)
- `AccessDenied`
- `DeliveryTimedOut`
- `ExecutionTimedOut`
- `Undeliverable`
- `InvalidPlatform`
- `Terminated`

- **DocumentName** : Specify name of the Amazon Web Services Systems Manager document (SSM document) for which you want to see command execution results. For example, specify `AWS-RunPatchBaseline` to see command executions that used this SSM document to perform security patching operations on managed nodes.
- **ExecutionStage** : Specify one of the following values (`ListCommands` operations only):
- `Executing` : Returns a list of command executions that are currently still running.
- `Complete` : Returns a list of command executions that have already completed.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "InvokedAfter"|"InvokedBefore"|"Status"|"ExecutionStage"|"DocumentName",
    "value": "string"
  }
  ...
]
```

`--details` | `--no-details` (boolean)

(Optional) If set this returns the response of the command executions and any command output. The default value is `false` .

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

**To list the invocations of a specific command**

The following `list-command-invocations` example lists all the invocations of a command.

```
aws ssm list-command-invocations \
    --command-id "ef7fdfd8-9b57-4151-a15c-db9a12345678" \
    --details
```

Output:

```
{
    "CommandInvocations": [
        {
            "CommandId": "ef7fdfd8-9b57-4151-a15c-db9a12345678",
            "InstanceId": "i-02573cafcfEXAMPLE",
            "InstanceName": "",
            "Comment": "b48291dd-ba76-43e0-b9df-13e11ddaac26:6960febb-2907-4b59-8e1a-d6ce8EXAMPLE",
            "DocumentName": "AWS-UpdateSSMAgent",
            "DocumentVersion": "",
            "RequestedDateTime": 1582136283.089,
            "Status": "Success",
            "StatusDetails": "Success",
            "StandardOutputUrl": "",
            "StandardErrorUrl": "",
            "CommandPlugins": [
                {
                    "Name": "aws:updateSsmAgent",
                    "Status": "Success",
                    "StatusDetails": "Success",
                    "ResponseCode": 0,
                    "ResponseStartDateTime": 1582136283.419,
                    "ResponseFinishDateTime": 1582136283.51,
                    "Output": "Updating amazon-ssm-agent from 2.3.842.0 to latest\nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/ssm-agent-manifest.json\namazon-ssm-agent 2.3.842.0 has already been installed, update skipped\n",
                    "StandardOutputUrl": "",
                    "StandardErrorUrl": "",
                    "OutputS3Region": "us-east-2",
                    "OutputS3BucketName": "",
                    "OutputS3KeyPrefix": ""
                }
            ],
            "ServiceRole": "",
            "NotificationConfig": {
                "NotificationArn": "",
                "NotificationEvents": [],
                "NotificationType": ""
            },
            "CloudWatchOutputConfig": {
                "CloudWatchLogGroupName": "",
                "CloudWatchOutputEnabled": false
            }
        },
        {
            "CommandId": "ef7fdfd8-9b57-4151-a15c-db9a12345678",
            "InstanceId": "i-0471e04240EXAMPLE",
            "InstanceName": "",
            "Comment": "b48291dd-ba76-43e0-b9df-13e11ddaac26:6960febb-2907-4b59-8e1a-d6ce8EXAMPLE",
            "DocumentName": "AWS-UpdateSSMAgent",
            "DocumentVersion": "",
            "RequestedDateTime": 1582136283.02,
            "Status": "Success",
            "StatusDetails": "Success",
            "StandardOutputUrl": "",
            "StandardErrorUrl": "",
            "CommandPlugins": [
                {
                    "Name": "aws:updateSsmAgent",
                    "Status": "Success",
                    "StatusDetails": "Success",
                    "ResponseCode": 0,
                    "ResponseStartDateTime": 1582136283.812,
                    "ResponseFinishDateTime": 1582136295.031,
                    "Output": "Updating amazon-ssm-agent from 2.3.672.0 to latest\nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/ssm-agent-manifest.json\nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/amazon-ssm-agent-updater/2.3.842.0/amazon-ssm-agent-updater-snap-amd64.tar.gz\nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/amazon-ssm-agent/2.3.672.0/amazon-ssm-agent-snap-amd64.tar.gz\nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/amazon-ssm-agent/2.3.842.0/amazon-ssm-agent-snap-amd64.tar.gz\nInitiating amazon-ssm-agent update to 2.3.842.0\namazon-ssm-agent updated successfully to 2.3.842.0",
                    "StandardOutputUrl": "",
                    "StandardErrorUrl": "",
                    "OutputS3Region": "us-east-2",
                    "OutputS3BucketName": "",
                    "OutputS3KeyPrefix": "8bee3135-398c-4d31-99b6-e42d2EXAMPLE/i-0471e04240EXAMPLE/awsupdateSsmAgent"
                }
            ],
            "ServiceRole": "",
            "NotificationConfig": {
                "NotificationArn": "",
                "NotificationEvents": [],
                "NotificationType": ""
            },
            "CloudWatchOutputConfig": {
                "CloudWatchLogGroupName": "",
                "CloudWatchOutputEnabled": false
            }
        }
    ]
}
```

For more information, see [Understanding Command Statuses](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html) in the *AWS Systems Manager User Guide*.

## Output

CommandInvocations -> (list)

(Optional) A list of all invocations.

(structure)

An invocation is a copy of a command sent to a specific managed node. A command can apply to one or more managed nodes. A command invocation applies to one managed node. For example, if a user runs `SendCommand` against three managed nodes, then a command invocation is created for each requested managed node ID. A command invocation returns status and detail information about a command you ran.

CommandId -> (string)

The command against which this invocation was requested.

InstanceId -> (string)

The managed node ID in which this invocation was requested.

InstanceName -> (string)

The fully qualified host name of the managed node.

Comment -> (string)

User-specified information about the command, such as a brief description of what the command should do.

DocumentName -> (string)

The document name that was requested for execution.

DocumentVersion -> (string)

The Systems Manager document (SSM document) version.

RequestedDateTime -> (timestamp)

The time and date the request was sent to this managed node.

Status -> (string)

Whether or not the invocation succeeded, failed, or is pending.

StatusDetails -> (string)

A detailed status of the command execution for each invocation (each managed node targeted by the command). StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see [Understanding command statuses](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html) in the *Amazon Web Services Systems Manager User Guide* . StatusDetails can be one of the following values:

- Pending: The command hasnât been sent to the managed node.
- In Progress: The command has been sent to the managed node but hasnât reached a terminal state.
- Success: The execution of the command or plugin was successfully completed. This is a terminal state.
- Delivery Timed Out: The command wasnât delivered to the managed node before the delivery timeout expired. Delivery timeouts donât count against the parent commandâs `MaxErrors` limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
- Execution Timed Out: Command execution started on the managed node, but the execution wasnât complete before the execution timeout expired. Execution timeouts count against the `MaxErrors` limit of the parent command. This is a terminal state.
- Failed: The command wasnât successful on the managed node. For a plugin, this indicates that the result code wasnât zero. For a command invocation, this indicates that the result code for one or more plugins wasnât zero. Invocation failures count against the `MaxErrors` limit of the parent command. This is a terminal state.
- Cancelled: The command was terminated before it was completed. This is a terminal state.
- Undeliverable: The command canât be delivered to the managed node. The managed node might not exist or might not be responding. Undeliverable invocations donât count against the parent commandâs MaxErrors limit and donât contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
- Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.
- Delayed: The system attempted to send the command to the managed node but wasnât successful. The system retries again.

TraceOutput -> (string)

Gets the trace output sent by the agent.

StandardOutputUrl -> (string)

The URL to the pluginâs StdOut file in Amazon Simple Storage Service (Amazon S3), if the S3 bucket was defined for the parent command. For an invocation, `StandardOutputUrl` is populated if there is just one plugin defined for the command, and the S3 bucket was defined for the command.

StandardErrorUrl -> (string)

The URL to the pluginâs StdErr file in Amazon Simple Storage Service (Amazon S3), if the S3 bucket was defined for the parent command. For an invocation, `StandardErrorUrl` is populated if there is just one plugin defined for the command, and the S3 bucket was defined for the command.

CommandPlugins -> (list)

Plugins processed by the command.

(structure)

Describes plugin details.

Name -> (string)

The name of the plugin. Must be one of the following: `aws:updateAgent` , `aws:domainjoin` , `aws:applications` , `aws:runPowerShellScript` , `aws:psmodule` , `aws:cloudWatch` , `aws:runShellScript` , or `aws:updateSSMAgent` .

Status -> (string)

The status of this plugin. You can run a document with multiple plugins.

StatusDetails -> (string)

A detailed status of the plugin execution. `StatusDetails` includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see [Understanding command statuses](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html) in the *Amazon Web Services Systems Manager User Guide* . StatusDetails can be one of the following values:

- Pending: The command hasnât been sent to the managed node.
- In Progress: The command has been sent to the managed node but hasnât reached a terminal state.
- Success: The execution of the command or plugin was successfully completed. This is a terminal state.
- Delivery Timed Out: The command wasnât delivered to the managed node before the delivery timeout expired. Delivery timeouts donât count against the parent commandâs `MaxErrors` limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
- Execution Timed Out: Command execution started on the managed node, but the execution wasnât complete before the execution timeout expired. Execution timeouts count against the `MaxErrors` limit of the parent command. This is a terminal state.
- Failed: The command wasnât successful on the managed node. For a plugin, this indicates that the result code wasnât zero. For a command invocation, this indicates that the result code for one or more plugins wasnât zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.
- Cancelled: The command was terminated before it was completed. This is a terminal state.
- Undeliverable: The command canât be delivered to the managed node. The managed node might not exist, or it might not be responding. Undeliverable invocations donât count against the parent commandâs MaxErrors limit, and they donât contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
- Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.

ResponseCode -> (integer)

A numeric response code generated after running the plugin.

ResponseStartDateTime -> (timestamp)

The time the plugin started running.

ResponseFinishDateTime -> (timestamp)

The time the plugin stopped running. Could stop prematurely if, for example, a cancel command was sent.

Output -> (string)

Output of the plugin execution.

StandardOutputUrl -> (string)

The URL for the complete text written by the plugin to stdout in Amazon S3. If the S3 bucket for the command wasnât specified, then this string is empty.

StandardErrorUrl -> (string)

The URL for the complete text written by the plugin to stderr. If execution isnât yet complete, then this string is empty.

OutputS3Region -> (string)

(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Amazon Web Services Systems Manager automatically determines the S3 bucket region.

OutputS3BucketName -> (string)

The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:

`amzn-s3-demo-bucket/my-prefix/i-02573cafcfEXAMPLE/awsrunShellScript`

`amzn-s3-demo-bucket` is the name of the S3 bucket;

`my-prefix` is the name of the S3 prefix;

`i-02573cafcfEXAMPLE` is the managed node ID;

`awsrunShellScript` is the name of the plugin.

OutputS3KeyPrefix -> (string)

The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:

`amzn-s3-demo-bucket/my-prefix/i-02573cafcfEXAMPLE/awsrunShellScript`

`amzn-s3-demo-bucket` is the name of the S3 bucket;

`my-prefix` is the name of the S3 prefix;

`i-02573cafcfEXAMPLE` is the managed node ID;

`awsrunShellScript` is the name of the plugin.

ServiceRole -> (string)

The Identity and Access Management (IAM) service role that Run Command, a tool in Amazon Web Services Systems Manager, uses to act on your behalf when sending notifications about command status changes on a per managed node basis.

NotificationConfig -> (structure)

Configurations for sending notifications about command status changes on a per managed node basis.

NotificationArn -> (string)

An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic. Run Command pushes notifications about command status changes to this topic.

NotificationEvents -> (list)

The different events for which you can receive notifications. To learn more about these events, see [Monitoring Systems Manager status changes using Amazon SNS notifications](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-notifications.html) in the *Amazon Web Services Systems Manager User Guide* .

(string)

NotificationType -> (string)

The type of notification.

- `Command` : Receive notification when the status of a command changes.
- `Invocation` : For commands sent to multiple managed nodes, receive notification on a per-node basis when the status of a command changes.

CloudWatchOutputConfig -> (structure)

Amazon CloudWatch Logs information where you want Amazon Web Services Systems Manager to send the command output.

CloudWatchLogGroupName -> (string)

The name of the CloudWatch Logs log group where you want to send command output. If you donât specify a group name, Amazon Web Services Systems Manager automatically creates a log group for you. The log group uses the following naming format:

[``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-command-invocations.html#id1)aws/ssm/*SystemsManagerDocumentName* ``

CloudWatchOutputEnabled -> (boolean)

Enables Systems Manager to send command output to CloudWatch Logs.

NextToken -> (string)

(Optional) The token for the next set of items to return. (You received this token from a previous call.)