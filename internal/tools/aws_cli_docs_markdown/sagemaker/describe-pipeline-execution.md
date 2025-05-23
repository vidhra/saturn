# describe-pipeline-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-pipeline-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-pipeline-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-pipeline-execution

## Description

Describes the details of a pipeline execution.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribePipelineExecution)

## Synopsis

```
describe-pipeline-execution
--pipeline-execution-arn <value>
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

`--pipeline-execution-arn` (string)

The Amazon Resource Name (ARN) of the pipeline execution.

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

PipelineArn -> (string)

The Amazon Resource Name (ARN) of the pipeline.

PipelineExecutionArn -> (string)

The Amazon Resource Name (ARN) of the pipeline execution.

PipelineExecutionDisplayName -> (string)

The display name of the pipeline execution.

PipelineExecutionStatus -> (string)

The status of the pipeline execution.

PipelineExecutionDescription -> (string)

The description of the pipeline execution.

PipelineExperimentConfig -> (structure)

Specifies the names of the experiment and trial created by a pipeline.

ExperimentName -> (string)

The name of the experiment.

TrialName -> (string)

The name of the trial.

FailureReason -> (string)

If the execution failed, a message describing why.

CreationTime -> (timestamp)

The time when the pipeline execution was created.

LastModifiedTime -> (timestamp)

The time when the pipeline execution was modified last.

CreatedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

LastModifiedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

ParallelismConfiguration -> (structure)

The parallelism configuration applied to the pipeline.

MaxParallelExecutionSteps -> (integer)

The max number of steps that can be executed in parallel.

SelectiveExecutionConfig -> (structure)

The selective execution configuration applied to the pipeline run.

SourcePipelineExecutionArn -> (string)

The ARN from a reference execution of the current pipeline. Used to copy input collaterals needed for the selected steps to run. The execution status of the pipeline can be either `Failed` or `Success` .

This field is required if the steps you specify for `SelectedSteps` depend on output collaterals from any non-specified pipeline steps. For more information, see [Selective Execution for Pipeline Steps](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-selective-ex.html) .

SelectedSteps -> (list)

A list of pipeline steps to run. All step(s) in all path(s) between two selected steps should be included.

(structure)

A step selected to run in selective execution mode.

StepName -> (string)

The name of the pipeline step.