# list-action-executionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-action-executions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-action-executions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codepipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/index.html#cli-aws-codepipeline) ]

# list-action-executions

## Description

Lists the action executions that have occurred in a pipeline.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListActionExecutions)

`list-action-executions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `actionExecutionDetails`

## Synopsis

```
list-action-executions
--pipeline-name <value>
[--filter <value>]
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

`--pipeline-name` (string)

The name of the pipeline for which you want to list action execution history.

`--filter` (structure)

Input information used to filter action execution history.

pipelineExecutionId -> (string)

The pipeline execution ID used to filter action execution history.

latestInPipelineExecution -> (structure)

The latest execution in the pipeline.

### Note

Filtering on the latest execution is available for executions run on or after February 08, 2024.

pipelineExecutionId -> (string)

The execution ID for the latest execution in the pipeline.

startTimeRange -> (string)

The start time to filter on for the latest execution in the pipeline. Valid options:

- All
- Latest

Shorthand Syntax:

```
pipelineExecutionId=string,latestInPipelineExecution={pipelineExecutionId=string,startTimeRange=string}
```

JSON Syntax:

```
{
  "pipelineExecutionId": "string",
  "latestInPipelineExecution": {
    "pipelineExecutionId": "string",
    "startTimeRange": "Latest"|"All"
  }
}
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

**To list action executions**

The following `list-action-executions` example views action execution details for a pipeline, such as action execution ID, input artifacts, output artifacts, execution result, and status.

```
aws codepipeline list-action-executions \
    --pipeline-name myPipeline
```

Output:

```
{
    "actionExecutionDetails": [
        {
            "pipelineExecutionId": "EXAMPLE0-adfc-488e-bf4c-1111111720d3",
            "actionExecutionId": "EXAMPLE4-2ee8-4853-bd6a-111111158148",
            "pipelineVersion": 12,
            "stageName": "Deploy",
            "actionName": "Deploy",
            "startTime": 1598572628.6,
            "lastUpdateTime": 1598572661.255,
            "status": "Succeeded",
            "input": {
                "actionTypeId": {
                    "category": "Deploy",
                    "owner": "AWS",
                    "provider": "CodeDeploy",
                    "version": "1"
                },
                "configuration": {
                    "ApplicationName": "my-application",
                    "DeploymentGroupName": "my-deployment-group"
                },
                "resolvedConfiguration": {
                    "ApplicationName": "my-application",
                    "DeploymentGroupName": "my-deployment-group"
                },
                "region": "us-east-1",
                "inputArtifacts": [
                    {
                        "name": "SourceArtifact",
                        "s3location": {
                            "bucket": "artifact-bucket",
                            "key": "myPipeline/SourceArti/key"
                        }
                    }
                ],
                "namespace": "DeployVariables"
            },
            "output": {
                "outputArtifacts": [],
                "executionResult": {
                    "externalExecutionId": "d-EXAMPLEE5",
                    "externalExecutionSummary": "Deployment Succeeded",
                    "externalExecutionUrl": "https://myaddress.com"
                },
                "outputVariables": {}
            }
        },
        {
            "pipelineExecutionId": "EXAMPLE0-adfc-488e-bf4c-1111111720d3",
            "actionExecutionId": "EXAMPLE5-abb4-4192-9031-11111113a7b0",
            "pipelineVersion": 12,
            "stageName": "Source",
            "actionName": "Source",
            "startTime": 1598572624.387,
            "lastUpdateTime": 1598572628.16,
            "status": "Succeeded",
            "input": {
                "actionTypeId": {
                    "category": "Source",
                    "owner": "AWS",
                    "provider": "CodeCommit",
                    "version": "1"
                },
                "configuration": {
                    "BranchName": "production",
                    "PollForSourceChanges": "false",
                    "RepositoryName": "my-repo"
                },
                "resolvedConfiguration": {
                    "BranchName": "production",
                    "PollForSourceChanges": "false",
                    "RepositoryName": "my-repo"
                },
                "region": "us-east-1",
                "inputArtifacts": [],
                "namespace": "SourceVariables"
            },
            "output": {
                "outputArtifacts": [
                    {
                        "name": "SourceArtifact",
                        "s3location": {
                            "bucket": "amzn-s3-demo-bucket",
                            "key": "myPipeline/SourceArti/key"
                        }
                    }
                ],
                "executionResult": {
                    "externalExecutionId": "1111111ad99dcd35914c00b7fbea13995EXAMPLE",
                    "externalExecutionSummary": "Edited template.yml",
                    "externalExecutionUrl": "https://myaddress.com"
                },
                "outputVariables": {
                    "AuthorDate": "2020-05-08T17:45:43Z",
                    "BranchName": "production",
                    "CommitId": "EXAMPLEad99dcd35914c00b7fbea139951111111",
                    "CommitMessage": "Edited template.yml",
                    "CommitterDate": "2020-05-08T17:45:43Z",
                    "RepositoryName": "my-repo"
                }
            }
        },
. . . .
```

For more information, see [View action executions (CLI)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-view-cli.html#pipelines-action-executions-cli) in the *AWS CodePipeline User Guide*.

## Output

actionExecutionDetails -> (list)

The details for a list of recent executions, such as action execution ID.

(structure)

Returns information about an execution of an action, including the action execution ID, and the name, version, and timing of the action.

pipelineExecutionId -> (string)

The pipeline execution ID for the action execution.

actionExecutionId -> (string)

The action execution ID.

pipelineVersion -> (integer)

The version of the pipeline where the action was run.

stageName -> (string)

The name of the stage that contains the action.

actionName -> (string)

The name of the action.

startTime -> (timestamp)

The start time of the action execution.

lastUpdateTime -> (timestamp)

The last update time of the action execution.

updatedBy -> (string)

The ARN of the user who changed the pipeline execution details.

status -> (string)

The status of the action execution. Status categories are `InProgress` , `Succeeded` , and `Failed` .

input -> (structure)

Input details for the action execution, such as role ARN, Region, and input artifacts.

actionTypeId -> (structure)

Represents information about an action type.

category -> (string)

A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.

- Source
- Build
- Test
- Deploy
- Invoke
- Approval
- Compute

owner -> (string)

The creator of the action being called. There are three valid values for the `Owner` field in the action category section within your pipeline structure: `AWS` , `ThirdParty` , and `Custom` . For more information, see [Valid Action Types and Providers in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers) .

provider -> (string)

The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of CodeDeploy, which would be specified as `CodeDeploy` . For more information, see [Valid Action Types and Providers in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers) .

version -> (string)

A string that describes the action version.

configuration -> (map)

Configuration data for an action execution.

key -> (string)

value -> (string)

resolvedConfiguration -> (map)

Configuration data for an action execution with all variable references replaced with their real values for the execution.

key -> (string)

value -> (string)

roleArn -> (string)

The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn for the pipeline.

region -> (string)

The Amazon Web Services Region for the action, such as us-east-1.

inputArtifacts -> (list)

Details of input artifacts of the action that correspond to the action execution.

(structure)

Artifact details for the action execution, such as the artifact location.

name -> (string)

The artifact object name for the action execution.

s3location -> (structure)

The Amazon S3 artifact location for the action execution.

bucket -> (string)

The Amazon S3 artifact bucket for an actionâs artifacts.

key -> (string)

The artifact name.

namespace -> (string)

The variable namespace associated with the action. All variables produced as output by this action fall under this namespace.

output -> (structure)

Output details for the action execution, such as the action execution result.

outputArtifacts -> (list)

Details of output artifacts of the action that correspond to the action execution.

(structure)

Artifact details for the action execution, such as the artifact location.

name -> (string)

The artifact object name for the action execution.

s3location -> (structure)

The Amazon S3 artifact location for the action execution.

bucket -> (string)

The Amazon S3 artifact bucket for an actionâs artifacts.

key -> (string)

The artifact name.

executionResult -> (structure)

Execution result information listed in the output details for an action execution.

externalExecutionId -> (string)

The action providerâs external ID for the action execution.

externalExecutionSummary -> (string)

The action providerâs summary for the action execution.

externalExecutionUrl -> (string)

The deepest external link to the external resource (for example, a repository URL or deployment endpoint) that is used when running the action.

errorDetails -> (structure)

Represents information about an error in CodePipeline.

code -> (string)

The system ID or number code of the error.

message -> (string)

The text of the error message.

logStreamARN -> (string)

The Amazon Resource Name (ARN) of the log stream for the action compute.

outputVariables -> (map)

The outputVariables field shows the key-value pairs that were output as part of that execution.

key -> (string)

value -> (string)

nextToken -> (string)

If the amount of returned information is significantly large, an identifier is also returned and can be used in a subsequent `ListActionExecutions` call to return the next set of action executions in the list.