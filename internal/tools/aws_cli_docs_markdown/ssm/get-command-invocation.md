# get-command-invocationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-command-invocation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-command-invocation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# get-command-invocation

## Description

Returns detailed information about command execution for an invocation or plugin. The Run Command API follows an eventual consistency model, due to the distributed nature of the system supporting the API. This means that the result of an API command you run that affects your resources might not be immediately visible to all subsequent commands you run. You should keep this in mind when you carry out an API command that immediately follows a previous API command.

`GetCommandInvocation` only gives the execution status of a plugin in a document. To get the command execution status on a specific managed node, use  ListCommandInvocations . To get the command execution status across managed nodes, use  ListCommands .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetCommandInvocation)

## Synopsis

```
get-command-invocation
--command-id <value>
--instance-id <value>
[--plugin-name <value>]
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

`--command-id` (string)

(Required) The parent command ID of the invocation plugin.

`--instance-id` (string)

(Required) The ID of the managed node targeted by the command. A *managed node* can be an Amazon Elastic Compute Cloud (Amazon EC2) instance, edge device, and on-premises server or VM in your hybrid environment that is configured for Amazon Web Services Systems Manager.

`--plugin-name` (string)

The name of the step for which you want detailed results. If the document contains only one step, you can omit the name and details for that step. If the document contains more than one step, you must specify the name of the step for which you want to view details. Be sure to specify the name of the step, not the name of a plugin like `aws:RunShellScript` .

To find the `PluginName` , check the document content and find the name of the step you want details for. Alternatively, use  ListCommandInvocations with the `CommandId` and `Details` parameters. The `PluginName` is the `Name` attribute of the `CommandPlugin` object in the `CommandPlugins` list.

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

**To display the details of a command invocation**

The following `get-command-invocation` example lists all the invocations of the specified command on the specified instance.

```
aws ssm get-command-invocation \
    --command-id "ef7fdfd8-9b57-4151-a15c-db9a12345678" \
    --instance-id "i-1234567890abcdef0"
```

Output:

```
{
    "CommandId": "ef7fdfd8-9b57-4151-a15c-db9a12345678",
    "InstanceId": "i-1234567890abcdef0",
    "Comment": "b48291dd-ba76-43e0-b9df-13e11ddaac26:6960febb-2907-4b59-8e1a-d6ce8EXAMPLE",
    "DocumentName": "AWS-UpdateSSMAgent",
    "DocumentVersion": "",
    "PluginName": "aws:updateSsmAgent",
    "ResponseCode": 0,
    "ExecutionStartDateTime": "2020-02-19T18:18:03.419Z",
    "ExecutionElapsedTime": "PT0.091S",
    "ExecutionEndDateTime": "2020-02-19T18:18:03.419Z",
    "Status": "Success",
    "StatusDetails": "Success",
    "StandardOutputContent": "Updating amazon-ssm-agent from 2.3.842.0 to latest\nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/ssm-agent-manifest.json\namazon-ssm-agent 2.3.842.0 has already been installed, update skipped\n",
    "StandardOutputUrl": "",
    "StandardErrorContent": "",
    "StandardErrorUrl": "",
    "CloudWatchOutputConfig": {
        "CloudWatchLogGroupName": "",
        "CloudWatchOutputEnabled": false
    }
}
```

For more information, see [Understanding Command Statuses](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html) in the *AWS Systems Manager User Guide*.

## Output

CommandId -> (string)

The parent command ID of the invocation plugin.

InstanceId -> (string)

The ID of the managed node targeted by the command. A *managed node* can be an Amazon Elastic Compute Cloud (Amazon EC2) instance, edge device, or on-premises server or VM in your hybrid environment that is configured for Amazon Web Services Systems Manager.

Comment -> (string)

The comment text for the command.

DocumentName -> (string)

The name of the document that was run. For example, `AWS-RunShellScript` .

DocumentVersion -> (string)

The Systems Manager document (SSM document) version used in the request.

PluginName -> (string)

The name of the plugin, or *step name* , for which details are reported. For example, `aws:RunShellScript` is a plugin.

ResponseCode -> (integer)

The error level response code for the plugin script. If the response code is `-1` , then the command hasnât started running on the managed node, or it wasnât received by the node.

ExecutionStartDateTime -> (string)

The date and time the plugin started running. Date and time are written in ISO 8601 format. For example, June 7, 2017 is represented as 2017-06-7. The following sample Amazon Web Services CLI command uses the `InvokedBefore` filter.

`aws ssm list-commands --filters key=InvokedBefore,value=2017-06-07T00:00:00Z`

If the plugin hasnât started to run, the string is empty.

ExecutionElapsedTime -> (string)

Duration since `ExecutionStartDateTime` .

ExecutionEndDateTime -> (string)

The date and time the plugin finished running. Date and time are written in ISO 8601 format. For example, June 7, 2017 is represented as 2017-06-7. The following sample Amazon Web Services CLI command uses the `InvokedAfter` filter.

`aws ssm list-commands --filters key=InvokedAfter,value=2017-06-07T00:00:00Z`

If the plugin hasnât started to run, the string is empty.

Status -> (string)

The status of this invocation plugin. This status can be different than `StatusDetails` .

StatusDetails -> (string)

A detailed status of the command execution for an invocation. `StatusDetails` includes more information than `Status` because it includes states resulting from error and concurrency control parameters. `StatusDetails` can show different results than `Status` . For more information about these statuses, see [Understanding command statuses](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html) in the *Amazon Web Services Systems Manager User Guide* . `StatusDetails` can be one of the following values:

- Pending: The command hasnât been sent to the managed node.
- In Progress: The command has been sent to the managed node but hasnât reached a terminal state.
- Delayed: The system attempted to send the command to the target, but the target wasnât available. The managed node might not be available because of network issues, because the node was stopped, or for similar reasons. The system will try to send the command again.
- Success: The command or plugin ran successfully. This is a terminal state.
- Delivery Timed Out: The command wasnât delivered to the managed node before the delivery timeout expired. Delivery timeouts donât count against the parent commandâs `MaxErrors` limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
- Execution Timed Out: The command started to run on the managed node, but the execution wasnât complete before the timeout expired. Execution timeouts count against the `MaxErrors` limit of the parent command. This is a terminal state.
- Failed: The command wasnât run successfully on the managed node. For a plugin, this indicates that the result code wasnât zero. For a command invocation, this indicates that the result code for one or more plugins wasnât zero. Invocation failures count against the `MaxErrors` limit of the parent command. This is a terminal state.
- Cancelled: The command was terminated before it was completed. This is a terminal state.
- Undeliverable: The command canât be delivered to the managed node. The node might not exist or might not be responding. Undeliverable invocations donât count against the parent commandâs `MaxErrors` limit and donât contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
- Terminated: The parent command exceeded its `MaxErrors` limit and subsequent command invocations were canceled by the system. This is a terminal state.

StandardOutputContent -> (string)

The first 24,000 characters written by the plugin to `stdout` . If the command hasnât finished running, if `ExecutionStatus` is neither Succeeded nor Failed, then this string is empty.

StandardOutputUrl -> (string)

The URL for the complete text written by the plugin to `stdout` in Amazon Simple Storage Service (Amazon S3). If an S3 bucket wasnât specified, then this string is empty.

StandardErrorContent -> (string)

The first 8,000 characters written by the plugin to `stderr` . If the command hasnât finished running, then this string is empty.

StandardErrorUrl -> (string)

The URL for the complete text written by the plugin to `stderr` . If the command hasnât finished running, then this string is empty.

CloudWatchOutputConfig -> (structure)

Amazon CloudWatch Logs information where Systems Manager sent the command output.

CloudWatchLogGroupName -> (string)

The name of the CloudWatch Logs log group where you want to send command output. If you donât specify a group name, Amazon Web Services Systems Manager automatically creates a log group for you. The log group uses the following naming format:

[``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-command-invocation.html#id1)aws/ssm/*SystemsManagerDocumentName* ``

CloudWatchOutputEnabled -> (boolean)

Enables Systems Manager to send command output to CloudWatch Logs.