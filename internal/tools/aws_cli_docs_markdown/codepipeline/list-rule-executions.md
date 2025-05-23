# list-rule-executionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-rule-executions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-rule-executions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codepipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/index.html#cli-aws-codepipeline) ]

# list-rule-executions

## Description

Lists the rule executions that have occurred in a pipeline configured for conditions with rules.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListRuleExecutions)

`list-rule-executions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ruleExecutionDetails`

## Synopsis

```
list-rule-executions
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

The name of the pipeline for which you want to get execution summary information.

`--filter` (structure)

Input information used to filter rule execution history.

pipelineExecutionId -> (string)

The pipeline execution ID used to filter rule execution history.

latestInPipelineExecution -> (structure)

The field that specifies to filter on the latest execution in the pipeline.

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

## Output

ruleExecutionDetails -> (list)

Details about the output for listing rule executions.

(structure)

The details of the runs for a rule and the results produced on an artifact as it passes through stages in the pipeline.

pipelineExecutionId -> (string)

The ID of the pipeline execution in the stage where the rule was run. Use the  GetPipelineState action to retrieve the current pipelineExecutionId of the stage.

ruleExecutionId -> (string)

The ID of the run for the rule.

pipelineVersion -> (integer)

The version number of the pipeline with the stage where the rule was run.

stageName -> (string)

The name of the stage where the rule was run.

ruleName -> (string)

The name of the rule that was run in the stage.

startTime -> (timestamp)

The start time of the rule execution.

lastUpdateTime -> (timestamp)

The date and time of the last change to the rule execution, in timestamp format.

updatedBy -> (string)

The ARN of the user who changed the rule execution details.

status -> (string)

The status of the rule execution. Status categories are `InProgress` , `Succeeded` , and `Failed` .

input -> (structure)

Input details for the rule execution, such as role ARN, Region, and input artifacts.

ruleTypeId -> (structure)

The ID for the rule type, which is made up of the combined values for category, owner, provider, and version. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) . For more information about rules, see the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

category -> (string)

A category defines what kind of rule can be run in the stage, and constrains the provider type for the rule. The valid category is `Rule` .

owner -> (string)

The creator of the rule being called. The valid value for the `Owner` field in the rule category is `AWS` .

provider -> (string)

The rule provider, such as the `DeploymentWindow` rule. For a list of rule provider names, see the rules listed in the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

version -> (string)

A string that describes the rule version.

configuration -> (map)

Configuration data for a rule execution, such as the resolved values for that run.

key -> (string)

value -> (string)

resolvedConfiguration -> (map)

Configuration data for a rule execution with all variable references replaced with their real values for the execution.

key -> (string)

value -> (string)

roleArn -> (string)

The ARN of the IAM service role that performs the declared rule. This is assumed through the roleArn for the pipeline.

region -> (string)

The Amazon Web Services Region for the rule, such as us-east-1.

inputArtifacts -> (list)

Details of input artifacts of the rule that correspond to the rule execution.

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

output -> (structure)

Output details for the rule execution, such as the rule execution result.

executionResult -> (structure)

Execution result information listed in the output details for a rule execution.

externalExecutionId -> (string)

The external ID for the rule execution.

externalExecutionSummary -> (string)

The external provider summary for the rule execution.

externalExecutionUrl -> (string)

The deepest external link to the external resource (for example, a repository URL or deployment endpoint) that is used when running the rule.

errorDetails -> (structure)

Represents information about an error in CodePipeline.

code -> (string)

The system ID or number code of the error.

message -> (string)

The text of the error message.

nextToken -> (string)

A token that can be used in the next `ListRuleExecutions` call. To view all items in the list, continue to call this operation with each subsequent token until no more nextToken values are returned.