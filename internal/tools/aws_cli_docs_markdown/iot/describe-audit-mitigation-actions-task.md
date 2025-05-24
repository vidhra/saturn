# describe-audit-mitigation-actions-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-audit-mitigation-actions-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-audit-mitigation-actions-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# describe-audit-mitigation-actions-task

## Description

Gets information about an audit mitigation task that is used to apply mitigation actions to a set of audit findings. Properties include the actions being applied, the audit checks to which theyâre being applied, the task status, and aggregated task statistics.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeAuditMitigationActionsTask)

## Synopsis

```
describe-audit-mitigation-actions-task
--task-id <value>
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

`--task-id` (string)

The unique identifier for the audit mitigation task.

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

**To show the details of an audit mitigation actions task**

The following `describe-audit-mitigation-actions-task` example shows the details for the specified task, where the `ResetPolicyVersionAction` was applied to a finding. The results include when the task started and ended, how many findings were targeted (and the outcome), and the definition of the action that is applied as part of this task.

```
aws iot describe-audit-mitigation-actions-task \
    --task-id ResetPolicyTask01
```

Output:

```
{
    "taskStatus": "COMPLETED",
    "startTime": "2019-12-10T15:13:19.457000-08:00",
    "endTime": "2019-12-10T15:13:19.947000-08:00",
    "taskStatistics": {
        "IOT_POLICY_OVERLY_PERMISSIVE_CHECK": {
            "totalFindingsCount": 1,
            "failedFindingsCount": 0,
            "succeededFindingsCount": 1,
            "skippedFindingsCount": 0,
            "canceledFindingsCount": 0
        }
    },
    "target": {
        "findingIds": [
            "ef4826b8-e55a-44b9-b460-5c485355371b"
        ]
    },
    "auditCheckToActionsMapping": {
        "IOT_POLICY_OVERLY_PERMISSIVE_CHECK": [
            "ResetPolicyVersionAction"
        ]
    },
    "actionsDefinition": [
        {
            "name": "ResetPolicyVersionAction",
            "id": "1ea0b415-bef1-4a01-bd13-72fb63c59afb",
            "roleArn": "arn:aws:iam::123456789012:role/service-role/ReplacePolicyVersionRole",
            "actionParams": {
                "replaceDefaultPolicyVersionParams": {
                    "templateName": "BLANK_POLICY"
                }
            }
        }
    ]
}
```

For more information, see [DescribeAuditMitigationActionsTask (Mitigation Action Commands)](https://docs.aws.amazon.com/iot/latest/developerguide/mitigation-action-commands.html#dd-api-iot-DescribeAuditMitigationActionsTask) in the *AWS IoT Developer Guide*.

## Output

taskStatus -> (string)

The current status of the task.

startTime -> (timestamp)

The date and time when the task was started.

endTime -> (timestamp)

The date and time when the task was completed or canceled.

taskStatistics -> (map)

Aggregate counts of the results when the mitigation tasks were applied to the findings for this audit mitigation actions task.

key -> (string)

An audit check name. Checks must be enabled for your account. (Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are enabled or use `UpdateAccountAuditConfiguration` to select which checks are enabled.)

value -> (structure)

Provides summary counts of how many tasks for findings are in a particular state. This information is included in the response from DescribeAuditMitigationActionsTask.

totalFindingsCount -> (long)

The total number of findings to which a task is being applied.

failedFindingsCount -> (long)

The number of findings for which at least one of the actions failed when applied.

succeededFindingsCount -> (long)

The number of findings for which all mitigation actions succeeded when applied.

skippedFindingsCount -> (long)

The number of findings skipped because of filter conditions provided in the parameters to the command.

canceledFindingsCount -> (long)

The number of findings to which the mitigation action task was canceled when applied.

target -> (structure)

Identifies the findings to which the mitigation actions are applied. This can be by audit checks, by audit task, or a set of findings.

auditTaskId -> (string)

If the task will apply a mitigation action to findings from a specific audit, this value uniquely identifies the audit.

findingIds -> (list)

If the task will apply a mitigation action to one or more listed findings, this value uniquely identifies those findings.

(string)

auditCheckToReasonCodeFilter -> (map)

Specifies a filter in the form of an audit check and set of reason codes that identify the findings from the audit to which the audit mitigation actions task apply.

key -> (string)

An audit check name. Checks must be enabled for your account. (Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are enabled or use `UpdateAccountAuditConfiguration` to select which checks are enabled.)

value -> (list)

(string)

auditCheckToActionsMapping -> (map)

Specifies the mitigation actions that should be applied to specific audit checks.

key -> (string)

An audit check name. Checks must be enabled for your account. (Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are enabled or use `UpdateAccountAuditConfiguration` to select which checks are enabled.)

value -> (list)

(string)

actionsDefinition -> (list)

Specifies the mitigation actions and their parameters that are applied as part of this task.

(structure)

Describes which changes should be applied as part of a mitigation action.

name -> (string)

A user-friendly name for the mitigation action.

id -> (string)

A unique identifier for the mitigation action.

roleArn -> (string)

The IAM role ARN used to apply this mitigation action.

actionParams -> (structure)

The set of parameters for this mitigation action. The parameters vary, depending on the kind of action you apply.

updateDeviceCertificateParams -> (structure)

Parameters to define a mitigation action that changes the state of the device certificate to inactive.

action -> (string)

The action that you want to apply to the device certificate. The only supported value is `DEACTIVATE` .

updateCACertificateParams -> (structure)

Parameters to define a mitigation action that changes the state of the CA certificate to inactive.

action -> (string)

The action that you want to apply to the CA certificate. The only supported value is `DEACTIVATE` .

addThingsToThingGroupParams -> (structure)

Parameters to define a mitigation action that moves devices associated with a certificate to one or more specified thing groups, typically for quarantine.

thingGroupNames -> (list)

The list of groups to which you want to add the things that triggered the mitigation action. You can add a thing to a maximum of 10 groups, but you canât add a thing to more than one group in the same hierarchy.

(string)

overrideDynamicGroups -> (boolean)

Specifies if this mitigation action can move the things that triggered the mitigation action even if they are part of one or more dynamic thing groups.

replaceDefaultPolicyVersionParams -> (structure)

Parameters to define a mitigation action that adds a blank policy to restrict permissions.

templateName -> (string)

The name of the template to be applied. The only supported value is `BLANK_POLICY` .

enableIoTLoggingParams -> (structure)

Parameters to define a mitigation action that enables Amazon Web Services IoT Core logging at a specified level of detail.

roleArnForLogging -> (string)

The Amazon Resource Name (ARN) of the IAM role used for logging.

logLevel -> (string)

Specifies the type of information to be logged.

publishFindingToSnsParams -> (structure)

Parameters to define a mitigation action that publishes findings to Amazon Simple Notification Service (Amazon SNS. You can implement your own custom actions in response to the Amazon SNS messages.

topicArn -> (string)

The ARN of the topic to which you want to publish the findings.