# get-pipeline-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-pipeline-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-pipeline-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codepipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/index.html#cli-aws-codepipeline) ]

# get-pipeline-execution

## Description

Returns information about an execution of a pipeline, including details about artifacts, the pipeline execution ID, and the name, version, and status of the pipeline.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/GetPipelineExecution)

## Synopsis

```
get-pipeline-execution
--pipeline-name <value>
--pipeline-execution-id <value>
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

`--pipeline-name` (string)

The name of the pipeline about which you want to get execution details.

`--pipeline-execution-id` (string)

The ID of the pipeline execution about which you want to get execution details.

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

## Output

pipelineExecution -> (structure)

Represents information about the execution of a pipeline.

pipelineName -> (string)

The name of the pipeline with the specified pipeline execution.

pipelineVersion -> (integer)

The version number of the pipeline with the specified pipeline execution.

pipelineExecutionId -> (string)

The ID of the pipeline execution.

status -> (string)

The status of the pipeline execution.

- Cancelled: The pipelineâs definition was updated before the pipeline execution could be completed.
- InProgress: The pipeline execution is currently running.
- Stopped: The pipeline execution was manually stopped. For more information, see [Stopped Executions](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-executions-stopped) .
- Stopping: The pipeline execution received a request to be manually stopped. Depending on the selected stop mode, the execution is either completing or abandoning in-progress actions. For more information, see [Stopped Executions](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-executions-stopped) .
- Succeeded: The pipeline execution was completed successfully.
- Superseded: While this pipeline execution was waiting for the next stage to be completed, a newer pipeline execution advanced and continued through the pipeline instead. For more information, see [Superseded Executions](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-superseded) .
- Failed: The pipeline execution was not completed successfully.

statusSummary -> (string)

A summary that contains a description of the pipeline execution status.

artifactRevisions -> (list)

A list of `ArtifactRevision` objects included in a pipeline execution.

(structure)

Represents revision details of an artifact.

name -> (string)

The name of an artifact. This name might be system-generated, such as âMyAppâ, or defined by the user when an action is created.

revisionId -> (string)

The revision ID of the artifact.

revisionChangeIdentifier -> (string)

An additional identifier for a revision, such as a commit date or, for artifacts stored in Amazon S3 buckets, the ETag value.

revisionSummary -> (string)

Summary information about the most recent revision of the artifact. For GitHub and CodeCommit repositories, the commit message. For Amazon S3 buckets or actions, the user-provided content of a `codepipeline-artifact-revision-summary` key specified in the object metadata.

created -> (timestamp)

The date and time when the most recent revision of the artifact was created, in timestamp format.

revisionUrl -> (string)

The commit ID for the artifact revision. For artifacts stored in GitHub or CodeCommit repositories, the commit ID is linked to a commit details page.

variables -> (list)

A list of pipeline variables used for the pipeline execution.

(structure)

A pipeline-level variable used for a pipeline execution.

name -> (string)

The name of a pipeline-level variable.

resolvedValue -> (string)

The resolved value of a pipeline-level variable.

trigger -> (structure)

The interaction or event that started a pipeline execution.

triggerType -> (string)

The type of change-detection method, command, or user interaction that started a pipeline execution.

triggerDetail -> (string)

Detail related to the event that started a pipeline execution, such as the webhook ARN of the webhook that triggered the pipeline execution or the user ARN for a user-initiated `start-pipeline-execution` CLI command.

executionMode -> (string)

The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.

executionType -> (string)

The type of the pipeline execution.

rollbackMetadata -> (structure)

The metadata about the execution pertaining to stage rollback.

rollbackTargetPipelineExecutionId -> (string)

The pipeline execution ID to which the stage will be rolled back.