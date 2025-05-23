# get-pipeline-stateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-pipeline-state.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-pipeline-state.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codepipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/index.html#cli-aws-codepipeline) ]

# get-pipeline-state

## Description

Returns information about the state of a pipeline, including the stages and actions.

### Note

Values returned in the `revisionId` and `revisionUrl` fields indicate the source revision information, such as the commit ID, for the current state.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/GetPipelineState)

## Synopsis

```
get-pipeline-state
--name <value>
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

`--name` (string)

The name of the pipeline about which you want to get information.

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

**To get information about the state of a pipeline**

This example returns the most recent state of a pipeline named MyFirstPipeline.

Command:

```
aws codepipeline get-pipeline-state --name MyFirstPipeline
```

Output:

```
{
 "created": 1446137312.204,
 "pipelineName": "MyFirstPipeline",
 "pipelineVersion": 1,
 "stageStates": [
  {
    "actionStates": [
      {
        "actionName": "Source",
        "entityUrl": "https://console.aws.amazon.com/s3/home?#",
        "latestExecution": {
          "lastStatusChange": 1446137358.328,
          "status": "Succeeded"
        }
      }
    ],
    "stageName": "Source"
  },
  {
    "actionStates": [
      {
        "actionName": "CodePipelineDemoFleet",
        "entityUrl": "https://console.aws.amazon.com/codedeploy/home?#/applications/CodePipelineDemoApplication/deployment-groups/CodePipelineDemoFleet",
        "latestExecution": {
          "externalExecutionId": "d-EXAMPLE",
          "externalExecutionUrl": "https://console.aws.amazon.com/codedeploy/home?#/deployments/d-EXAMPLE",
          "lastStatusChange": 1446137493.131,
          "status": "Succeeded",
          "summary": "Deployment Succeeded"
        }
      }
    ],
    "inboundTransitionState": {
      "enabled": true
    },
    "stageName": "Beta"
  }
 ],
 "updated": 1446137312.204
}
```

## Output

pipelineName -> (string)

The name of the pipeline for which you want to get the state.

pipelineVersion -> (integer)

The version number of the pipeline.

### Note

A newly created pipeline is always assigned a version number of `1` .

stageStates -> (list)

A list of the pipeline stage output information, including stage name, state, most recent run details, whether the stage is disabled, and other data.

(structure)

Represents information about the state of the stage.

stageName -> (string)

The name of the stage.

inboundExecution -> (structure)

Represents information about the run of a stage.

pipelineExecutionId -> (string)

The ID of the pipeline execution associated with the stage.

status -> (string)

The status of the stage, or for a completed stage, the last status of the stage.

### Note

A status of cancelled means that the pipelineâs definition was updated before the stage execution could be completed.

type -> (string)

The type of pipeline execution for the stage, such as a rollback pipeline execution.

inboundExecutions -> (list)

The inbound executions for a stage.

(structure)

Represents information about the run of a stage.

pipelineExecutionId -> (string)

The ID of the pipeline execution associated with the stage.

status -> (string)

The status of the stage, or for a completed stage, the last status of the stage.

### Note

A status of cancelled means that the pipelineâs definition was updated before the stage execution could be completed.

type -> (string)

The type of pipeline execution for the stage, such as a rollback pipeline execution.

inboundTransitionState -> (structure)

The state of the inbound transition, which is either enabled or disabled.

enabled -> (boolean)

Whether the transition between stages is enabled (true) or disabled (false).

lastChangedBy -> (string)

The ID of the user who last changed the transition state.

lastChangedAt -> (timestamp)

The timestamp when the transition state was last changed.

disabledReason -> (string)

The user-specified reason why the transition between two stages of a pipeline was disabled.

actionStates -> (list)

The state of the stage.

(structure)

Represents information about the state of an action.

actionName -> (string)

The name of the action.

currentRevision -> (structure)

Represents information about the version (or revision) of an action.

revisionId -> (string)

The system-generated unique ID that identifies the revision number of the action.

revisionChangeId -> (string)

The unique identifier of the change that set the state to this revision (for example, a deployment ID or timestamp).

created -> (timestamp)

The date and time when the most recent version of the action was created, in timestamp format.

latestExecution -> (structure)

Represents information about the run of an action.

actionExecutionId -> (string)

ID of the workflow action execution in the current stage. Use the  GetPipelineState action to retrieve the current action execution details of the current stage.

### Note

For older executions, this field might be empty. The action execution ID is available for executions run on or after March 2020.

status -> (string)

The status of the action, or for a completed action, the last status of the action.

summary -> (string)

A summary of the run of the action.

lastStatusChange -> (timestamp)

The last status change of the action.

token -> (string)

The system-generated token used to identify a unique approval request. The token for each open approval request can be obtained using the `GetPipelineState` command. It is used to validate that the approval request corresponding to this token is still valid.

lastUpdatedBy -> (string)

The ARN of the user who last changed the pipeline.

externalExecutionId -> (string)

The external ID of the run of the action.

externalExecutionUrl -> (string)

The URL of a resource external to Amazon Web Services that is used when running the action (for example, an external repository URL).

percentComplete -> (integer)

A percentage of completeness of the action as it runs.

errorDetails -> (structure)

The details of an error returned by a URL external to Amazon Web Services.

code -> (string)

The system ID or number code of the error.

message -> (string)

The text of the error message.

logStreamARN -> (string)

The Amazon Resource Name (ARN) of the log stream for the action compute.

entityUrl -> (string)

A URL link for more information about the state of the action, such as a deployment group details page.

revisionUrl -> (string)

A URL link for more information about the revision, such as a commit details page.

latestExecution -> (structure)

Information about the latest execution in the stage, including its ID and status.

pipelineExecutionId -> (string)

The ID of the pipeline execution associated with the stage.

status -> (string)

The status of the stage, or for a completed stage, the last status of the stage.

### Note

A status of cancelled means that the pipelineâs definition was updated before the stage execution could be completed.

type -> (string)

The type of pipeline execution for the stage, such as a rollback pipeline execution.

beforeEntryConditionState -> (structure)

The state of the entry conditions for a stage.

latestExecution -> (structure)

Represents information about the latest run of a condition for a stage.

status -> (string)

The status of a run of a condition for a stage.

summary -> (string)

A summary of the run of the condition for a stage.

conditionStates -> (list)

The states of the conditions for a run of a condition for a stage.

(structure)

Information about the state of the condition.

latestExecution -> (structure)

The state of the latest run of the rule.

status -> (string)

The status of the run for a condition.

summary -> (string)

The summary of information about a run for a condition.

lastStatusChange -> (timestamp)

The last status change of the condition.

ruleStates -> (list)

The state of the rules for the condition.

(structure)

Returns information about the state of a rule.

### Note

Values returned in the `revisionId` field indicate the rule revision information, such as the commit ID, for the current state.

ruleName -> (string)

The name of the rule.

currentRevision -> (structure)

The ID of the current revision of the artifact successfully worked on by the job.

revisionId -> (string)

The system-generated unique ID that identifies the revision number of the rule.

revisionChangeId -> (string)

The unique identifier of the change that set the state to this revision (for example, a deployment ID or timestamp).

created -> (timestamp)

The date and time when the most recent version of the rule was created, in timestamp format.

latestExecution -> (structure)

Represents information about the latest run of an rule.

ruleExecutionId -> (string)

The execution ID for the run of the rule.

status -> (string)

The status of the run of the rule, such as FAILED.

summary -> (string)

A summary of the run of the rule.

lastStatusChange -> (timestamp)

The last status change of the rule.

token -> (string)

The system-generated token used to identify a unique request.

lastUpdatedBy -> (string)

The ARN of the user who last changed the rule.

externalExecutionId -> (string)

The external ID of the run of the rule.

externalExecutionUrl -> (string)

The URL of a resource external to Amazon Web Services that is used when running the rule (for example, an external repository URL).

errorDetails -> (structure)

Represents information about an error in CodePipeline.

code -> (string)

The system ID or number code of the error.

message -> (string)

The text of the error message.

entityUrl -> (string)

A URL link for more information about the state of the action, such as a details page.

revisionUrl -> (string)

A URL link for more information about the revision, such as a commit details page.

onSuccessConditionState -> (structure)

The state of the success conditions for a stage.

latestExecution -> (structure)

Represents information about the latest run of a condition for a stage.

status -> (string)

The status of a run of a condition for a stage.

summary -> (string)

A summary of the run of the condition for a stage.

conditionStates -> (list)

The states of the conditions for a run of a condition for a stage.

(structure)

Information about the state of the condition.

latestExecution -> (structure)

The state of the latest run of the rule.

status -> (string)

The status of the run for a condition.

summary -> (string)

The summary of information about a run for a condition.

lastStatusChange -> (timestamp)

The last status change of the condition.

ruleStates -> (list)

The state of the rules for the condition.

(structure)

Returns information about the state of a rule.

### Note

Values returned in the `revisionId` field indicate the rule revision information, such as the commit ID, for the current state.

ruleName -> (string)

The name of the rule.

currentRevision -> (structure)

The ID of the current revision of the artifact successfully worked on by the job.

revisionId -> (string)

The system-generated unique ID that identifies the revision number of the rule.

revisionChangeId -> (string)

The unique identifier of the change that set the state to this revision (for example, a deployment ID or timestamp).

created -> (timestamp)

The date and time when the most recent version of the rule was created, in timestamp format.

latestExecution -> (structure)

Represents information about the latest run of an rule.

ruleExecutionId -> (string)

The execution ID for the run of the rule.

status -> (string)

The status of the run of the rule, such as FAILED.

summary -> (string)

A summary of the run of the rule.

lastStatusChange -> (timestamp)

The last status change of the rule.

token -> (string)

The system-generated token used to identify a unique request.

lastUpdatedBy -> (string)

The ARN of the user who last changed the rule.

externalExecutionId -> (string)

The external ID of the run of the rule.

externalExecutionUrl -> (string)

The URL of a resource external to Amazon Web Services that is used when running the rule (for example, an external repository URL).

errorDetails -> (structure)

Represents information about an error in CodePipeline.

code -> (string)

The system ID or number code of the error.

message -> (string)

The text of the error message.

entityUrl -> (string)

A URL link for more information about the state of the action, such as a details page.

revisionUrl -> (string)

A URL link for more information about the revision, such as a commit details page.

onFailureConditionState -> (structure)

The state of the failure conditions for a stage.

latestExecution -> (structure)

Represents information about the latest run of a condition for a stage.

status -> (string)

The status of a run of a condition for a stage.

summary -> (string)

A summary of the run of the condition for a stage.

conditionStates -> (list)

The states of the conditions for a run of a condition for a stage.

(structure)

Information about the state of the condition.

latestExecution -> (structure)

The state of the latest run of the rule.

status -> (string)

The status of the run for a condition.

summary -> (string)

The summary of information about a run for a condition.

lastStatusChange -> (timestamp)

The last status change of the condition.

ruleStates -> (list)

The state of the rules for the condition.

(structure)

Returns information about the state of a rule.

### Note

Values returned in the `revisionId` field indicate the rule revision information, such as the commit ID, for the current state.

ruleName -> (string)

The name of the rule.

currentRevision -> (structure)

The ID of the current revision of the artifact successfully worked on by the job.

revisionId -> (string)

The system-generated unique ID that identifies the revision number of the rule.

revisionChangeId -> (string)

The unique identifier of the change that set the state to this revision (for example, a deployment ID or timestamp).

created -> (timestamp)

The date and time when the most recent version of the rule was created, in timestamp format.

latestExecution -> (structure)

Represents information about the latest run of an rule.

ruleExecutionId -> (string)

The execution ID for the run of the rule.

status -> (string)

The status of the run of the rule, such as FAILED.

summary -> (string)

A summary of the run of the rule.

lastStatusChange -> (timestamp)

The last status change of the rule.

token -> (string)

The system-generated token used to identify a unique request.

lastUpdatedBy -> (string)

The ARN of the user who last changed the rule.

externalExecutionId -> (string)

The external ID of the run of the rule.

externalExecutionUrl -> (string)

The URL of a resource external to Amazon Web Services that is used when running the rule (for example, an external repository URL).

errorDetails -> (structure)

Represents information about an error in CodePipeline.

code -> (string)

The system ID or number code of the error.

message -> (string)

The text of the error message.

entityUrl -> (string)

A URL link for more information about the state of the action, such as a details page.

revisionUrl -> (string)

A URL link for more information about the revision, such as a commit details page.

retryStageMetadata -> (structure)

he details of a specific automatic retry on stage failure, including the attempt number and trigger.

autoStageRetryAttempt -> (integer)

The number of attempts for a specific stage with automatic retry on stage failure. One attempt is allowed for automatic stage retry on failure.

manualStageRetryAttempt -> (integer)

The number of attempts for a specific stage where manual retries have been made upon stage failure.

latestRetryTrigger -> (string)

The latest trigger for a specific stage where manual or automatic retries have been made upon stage failure.

created -> (timestamp)

The date and time the pipeline was created, in timestamp format.

updated -> (timestamp)

The date and time the pipeline was last updated, in timestamp format.