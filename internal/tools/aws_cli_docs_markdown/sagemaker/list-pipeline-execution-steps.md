# list-pipeline-execution-stepsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-pipeline-execution-steps.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-pipeline-execution-steps.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# list-pipeline-execution-steps

## Description

Gets a list of `PipeLineExecutionStep` objects.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListPipelineExecutionSteps)

`list-pipeline-execution-steps` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `PipelineExecutionSteps`

## Synopsis

```
list-pipeline-execution-steps
[--pipeline-execution-arn <value>]
[--sort-order <value>]
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

`--pipeline-execution-arn` (string)

The Amazon Resource Name (ARN) of the pipeline execution.

`--sort-order` (string)

The field by which to sort results. The default is `CreatedTime` .

Possible values:

- `Ascending`
- `Descending`

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

PipelineExecutionSteps -> (list)

A list of `PipeLineExecutionStep` objects. Each `PipeLineExecutionStep` consists of StepName, StartTime, EndTime, StepStatus, and Metadata. Metadata is an object with properties for each job that contains relevant information about the job created by the step.

(structure)

An execution of a step in a pipeline.

StepName -> (string)

The name of the step that is executed.

StepDisplayName -> (string)

The display name of the step.

StepDescription -> (string)

The description of the step.

StartTime -> (timestamp)

The time that the step started executing.

EndTime -> (timestamp)

The time that the step stopped executing.

StepStatus -> (string)

The status of the step execution.

CacheHitResult -> (structure)

If this pipeline execution step was cached, details on the cache hit.

SourcePipelineExecutionArn -> (string)

The Amazon Resource Name (ARN) of the pipeline execution.

FailureReason -> (string)

The reason why the step failed execution. This is only returned if the step failed its execution.

Metadata -> (structure)

Metadata to run the pipeline step.

TrainingJob -> (structure)

The Amazon Resource Name (ARN) of the training job that was run by this step execution.

Arn -> (string)

The Amazon Resource Name (ARN) of the training job that was run by this step execution.

ProcessingJob -> (structure)

The Amazon Resource Name (ARN) of the processing job that was run by this step execution.

Arn -> (string)

The Amazon Resource Name (ARN) of the processing job.

TransformJob -> (structure)

The Amazon Resource Name (ARN) of the transform job that was run by this step execution.

Arn -> (string)

The Amazon Resource Name (ARN) of the transform job that was run by this step execution.

TuningJob -> (structure)

The Amazon Resource Name (ARN) of the tuning job that was run by this step execution.

Arn -> (string)

The Amazon Resource Name (ARN) of the tuning job that was run by this step execution.

Model -> (structure)

The Amazon Resource Name (ARN) of the model that was created by this step execution.

Arn -> (string)

The Amazon Resource Name (ARN) of the created model.

RegisterModel -> (structure)

The Amazon Resource Name (ARN) of the model package that the model was registered to by this step execution.

Arn -> (string)

The Amazon Resource Name (ARN) of the model package.

Condition -> (structure)

The outcome of the condition evaluation that was run by this step execution.

Outcome -> (string)

The outcome of the Condition step evaluation.

Callback -> (structure)

The URL of the Amazon SQS queue used by this step execution, the pipeline generated token, and a list of output parameters.

CallbackToken -> (string)

The pipeline generated token from the Amazon SQS queue.

SqsQueueUrl -> (string)

The URL of the Amazon Simple Queue Service (Amazon SQS) queue used by the callback step.

OutputParameters -> (list)

A list of the output parameters of the callback step.

(structure)

An output parameter of a pipeline step.

Name -> (string)

The name of the output parameter.

Value -> (string)

The value of the output parameter.

Lambda -> (structure)

The Amazon Resource Name (ARN) of the Lambda function that was run by this step execution and a list of output parameters.

Arn -> (string)

The Amazon Resource Name (ARN) of the Lambda function that was run by this step execution.

OutputParameters -> (list)

A list of the output parameters of the Lambda step.

(structure)

An output parameter of a pipeline step.

Name -> (string)

The name of the output parameter.

Value -> (string)

The value of the output parameter.

EMR -> (structure)

The configurations and outcomes of an Amazon EMR step execution.

ClusterId -> (string)

The identifier of the EMR cluster.

StepId -> (string)

The identifier of the EMR cluster step.

StepName -> (string)

The name of the EMR cluster step.

LogFilePath -> (string)

The path to the log file where the cluster stepâs failure root cause is recorded.

QualityCheck -> (structure)

The configurations and outcomes of the check step execution. This includes:

- The type of the check conducted.
- The Amazon S3 URIs of baseline constraints and statistics files to be used for the drift check.
- The Amazon S3 URIs of newly calculated baseline constraints and statistics.
- The model package group name provided.
- The Amazon S3 URI of the violation report if violations detected.
- The Amazon Resource Name (ARN) of check processing job initiated by the step execution.
- The Boolean flags indicating if the drift check is skipped.
- If step property `BaselineUsedForDriftCheck` is set the same as `CalculatedBaseline` .

CheckType -> (string)

The type of the Quality check step.

BaselineUsedForDriftCheckStatistics -> (string)

The Amazon S3 URI of the baseline statistics file used for the drift check.

BaselineUsedForDriftCheckConstraints -> (string)

The Amazon S3 URI of the baseline constraints file used for the drift check.

CalculatedBaselineStatistics -> (string)

The Amazon S3 URI of the newly calculated baseline statistics file.

CalculatedBaselineConstraints -> (string)

The Amazon S3 URI of the newly calculated baseline constraints file.

ModelPackageGroupName -> (string)

The model package group name.

ViolationReport -> (string)

The Amazon S3 URI of violation report if violations are detected.

CheckJobArn -> (string)

The Amazon Resource Name (ARN) of the Quality check processing job that was run by this step execution.

SkipCheck -> (boolean)

This flag indicates if the drift check against the previous baseline will be skipped or not. If it is set to `False` , the previous baseline of the configured check type must be available.

RegisterNewBaseline -> (boolean)

This flag indicates if a newly calculated baseline can be accessed through step properties `BaselineUsedForDriftCheckConstraints` and `BaselineUsedForDriftCheckStatistics` . If it is set to `False` , the previous baseline of the configured check type must also be available. These can be accessed through the `BaselineUsedForDriftCheckConstraints` and `BaselineUsedForDriftCheckStatistics` properties.

ClarifyCheck -> (structure)

Container for the metadata for a Clarify check step. The configurations and outcomes of the check step execution. This includes:

- The type of the check conducted,
- The Amazon S3 URIs of baseline constraints and statistics files to be used for the drift check.
- The Amazon S3 URIs of newly calculated baseline constraints and statistics.
- The model package group name provided.
- The Amazon S3 URI of the violation report if violations detected.
- The Amazon Resource Name (ARN) of check processing job initiated by the step execution.
- The boolean flags indicating if the drift check is skipped.
- If step property `BaselineUsedForDriftCheck` is set the same as `CalculatedBaseline` .

CheckType -> (string)

The type of the Clarify Check step

BaselineUsedForDriftCheckConstraints -> (string)

The Amazon S3 URI of baseline constraints file to be used for the drift check.

CalculatedBaselineConstraints -> (string)

The Amazon S3 URI of the newly calculated baseline constraints file.

ModelPackageGroupName -> (string)

The model package group name.

ViolationReport -> (string)

The Amazon S3 URI of the violation report if violations are detected.

CheckJobArn -> (string)

The Amazon Resource Name (ARN) of the check processing job that was run by this stepâs execution.

SkipCheck -> (boolean)

This flag indicates if the drift check against the previous baseline will be skipped or not. If it is set to `False` , the previous baseline of the configured check type must be available.

RegisterNewBaseline -> (boolean)

This flag indicates if a newly calculated baseline can be accessed through step properties `BaselineUsedForDriftCheckConstraints` and `BaselineUsedForDriftCheckStatistics` . If it is set to `False` , the previous baseline of the configured check type must also be available. These can be accessed through the `BaselineUsedForDriftCheckConstraints` property.

Fail -> (structure)

The configurations and outcomes of a Fail step execution.

ErrorMessage -> (string)

A message that you define and then is processed and rendered by the Fail step when the error occurs.

AutoMLJob -> (structure)

The Amazon Resource Name (ARN) of the AutoML job that was run by this step.

Arn -> (string)

The Amazon Resource Name (ARN) of the AutoML job.

Endpoint -> (structure)

The endpoint that was invoked during this step execution.

Arn -> (string)

The Amazon Resource Name (ARN) of the endpoint in the step.

EndpointConfig -> (structure)

The endpoint configuration used to create an endpoint during this step execution.

Arn -> (string)

The Amazon Resource Name (ARN) of the endpoint configuration used in the step.

AttemptCount -> (integer)

The current attempt of the execution step. For more information, see [Retry Policy for SageMaker Pipelines steps](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-retry-policy.html) .

SelectiveExecutionResult -> (structure)

The ARN from an execution of the current pipeline from which results are reused for this step.

SourcePipelineExecutionArn -> (string)

The ARN from an execution of the current pipeline.

NextToken -> (string)

If the result of the previous `ListPipelineExecutionSteps` request was truncated, the response includes a `NextToken` . To retrieve the next set of pipeline execution steps, use the token in the next request.