# list-inference-recommendations-job-stepsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-inference-recommendations-job-steps.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-inference-recommendations-job-steps.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# list-inference-recommendations-job-steps

## Description

Returns a list of the subtasks for an Inference Recommender job.

The supported subtasks are benchmarks, which evaluate the performance of your model on different instance types.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListInferenceRecommendationsJobSteps)

`list-inference-recommendations-job-steps` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Steps`

## Synopsis

```
list-inference-recommendations-job-steps
--job-name <value>
[--status <value>]
[--step-type <value>]
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

`--job-name` (string)

The name for the Inference Recommender job.

`--status` (string)

A filter to return benchmarks of a specified status. If this field is left empty, then all benchmarks are returned.

Possible values:

- `PENDING`
- `IN_PROGRESS`
- `COMPLETED`
- `FAILED`
- `STOPPING`
- `STOPPED`
- `DELETING`
- `DELETED`

`--step-type` (string)

A filter to return details about the specified type of subtask.

`BENCHMARK` : Evaluate the performance of your model on different instance types.

Possible values:

- `BENCHMARK`

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

Steps -> (list)

A list of all subtask details in Inference Recommender.

(structure)

A returned array object for the `Steps` response field in the [ListInferenceRecommendationsJobSteps](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListInferenceRecommendationsJobSteps.html) API command.

StepType -> (string)

The type of the subtask.

`BENCHMARK` : Evaluate the performance of your model on different instance types.

JobName -> (string)

The name of the Inference Recommender job.

Status -> (string)

The current status of the benchmark.

InferenceBenchmark -> (structure)

The details for a specific benchmark.

Metrics -> (structure)

The metrics of recommendations.

CostPerHour -> (float)

Defines the cost per hour for the instance.

CostPerInference -> (float)

Defines the cost per inference for the instance .

MaxInvocations -> (integer)

The expected maximum number of requests per minute for the instance.

ModelLatency -> (integer)

The expected model latency at maximum invocation per minute for the instance.

CpuUtilization -> (float)

The expected CPU utilization at maximum invocations per minute for the instance.

`NaN` indicates that the value is not available.

MemoryUtilization -> (float)

The expected memory utilization at maximum invocations per minute for the instance.

`NaN` indicates that the value is not available.

ModelSetupTime -> (integer)

The time it takes to launch new compute resources for a serverless endpoint. The time can vary depending on the model size, how long it takes to download the model, and the start-up time of the container.

`NaN` indicates that the value is not available.

EndpointMetrics -> (structure)

The metrics for an existing endpoint compared in an Inference Recommender job.

MaxInvocations -> (integer)

The expected maximum number of requests per minute for the instance.

ModelLatency -> (integer)

The expected model latency at maximum invocations per minute for the instance.

EndpointConfiguration -> (structure)

The endpoint configuration made by Inference Recommender during a recommendation job.

EndpointName -> (string)

The name of the endpoint made during a recommendation job.

VariantName -> (string)

The name of the production variant (deployed model) made during a recommendation job.

InstanceType -> (string)

The instance type recommended by Amazon SageMaker Inference Recommender.

InitialInstanceCount -> (integer)

The number of instances recommended to launch initially.

ServerlessConfig -> (structure)

Specifies the serverless configuration for an endpoint variant.

MemorySizeInMB -> (integer)

The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.

MaxConcurrency -> (integer)

The maximum number of concurrent invocations your serverless endpoint can process.

ProvisionedConcurrency -> (integer)

The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency` .

### Note

This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) .

ModelConfiguration -> (structure)

Defines the model configuration. Includes the specification name and environment parameters.

InferenceSpecificationName -> (string)

The inference specification name in the model package version.

EnvironmentParameters -> (list)

Defines the environment parameters that includes key, value types, and values.

(structure)

A list of environment parameters suggested by the Amazon SageMaker Inference Recommender.

Key -> (string)

The environment key suggested by the Amazon SageMaker Inference Recommender.

ValueType -> (string)

The value type suggested by the Amazon SageMaker Inference Recommender.

Value -> (string)

The value suggested by the Amazon SageMaker Inference Recommender.

CompilationJobName -> (string)

The name of the compilation job used to create the recommended model artifacts.

FailureReason -> (string)

The reason why a benchmark failed.

InvocationEndTime -> (timestamp)

A timestamp that shows when the benchmark completed.

InvocationStartTime -> (timestamp)

A timestamp that shows when the benchmark started.

NextToken -> (string)

A token that you can specify in your next request to return more results from the list.