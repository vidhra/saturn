# describe-inference-recommendations-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-inference-recommendations-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-inference-recommendations-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-inference-recommendations-job

## Description

Provides the results of the Inference Recommender job. One or more recommendation jobs are returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeInferenceRecommendationsJob)

## Synopsis

```
describe-inference-recommendations-job
--job-name <value>
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

`--job-name` (string)

The name of the job. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.

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

JobName -> (string)

The name of the job. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.

JobDescription -> (string)

The job description that you provided when you initiated the job.

JobType -> (string)

The job type that you provided when you initiated the job.

JobArn -> (string)

The Amazon Resource Name (ARN) of the job.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) role you provided when you initiated the job.

Status -> (string)

The status of the job.

CreationTime -> (timestamp)

A timestamp that shows when the job was created.

CompletionTime -> (timestamp)

A timestamp that shows when the job completed.

LastModifiedTime -> (timestamp)

A timestamp that shows when the job was last modified.

FailureReason -> (string)

If the job fails, provides information why the job failed.

InputConfig -> (structure)

Returns information about the versioned model package Amazon Resource Name (ARN), the traffic pattern, and endpoint configurations you provided when you initiated the job.

ModelPackageVersionArn -> (string)

The Amazon Resource Name (ARN) of a versioned model package.

ModelName -> (string)

The name of the created model.

JobDurationInSeconds -> (integer)

Specifies the maximum duration of the job, in seconds. The maximum value is 18,000 seconds.

TrafficPattern -> (structure)

Specifies the traffic pattern of the job.

TrafficType -> (string)

Defines the traffic patterns. Choose either `PHASES` or `STAIRS` .

Phases -> (list)

Defines the phases traffic specification.

(structure)

Defines the traffic pattern.

InitialNumberOfUsers -> (integer)

Specifies how many concurrent users to start with. The value should be between 1 and 3.

SpawnRate -> (integer)

Specified how many new users to spawn in a minute.

DurationInSeconds -> (integer)

Specifies how long a traffic phase should be. For custom load tests, the value should be between 120 and 3600. This value should not exceed `JobDurationInSeconds` .

Stairs -> (structure)

Defines the stairs traffic pattern.

DurationInSeconds -> (integer)

Defines how long each traffic step should be.

NumberOfSteps -> (integer)

Specifies how many steps to perform during traffic.

UsersPerStep -> (integer)

Specifies how many new users to spawn in each step.

ResourceLimit -> (structure)

Defines the resource limit of the job.

MaxNumberOfTests -> (integer)

Defines the maximum number of load tests.

MaxParallelOfTests -> (integer)

Defines the maximum number of parallel load tests.

EndpointConfigurations -> (list)

Specifies the endpoint configuration to use for a job.

(structure)

The endpoint configuration for the load test.

InstanceType -> (string)

The instance types to use for the load test.

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

InferenceSpecificationName -> (string)

The inference specification name in the model package version.

EnvironmentParameterRanges -> (structure)

The parameter you want to benchmark against.

CategoricalParameterRanges -> (list)

Specified a list of parameters for each category.

(structure)

Environment parameters you want to benchmark your load test against.

Name -> (string)

The Name of the environment variable.

Value -> (list)

The list of values you can pass.

(string)

VolumeKmsKeyId -> (string)

The Amazon Resource Name (ARN) of a Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint. This key will be passed to SageMaker Hosting for endpoint creation.

The SageMaker execution role must have `kms:CreateGrant` permission in order to encrypt data on the storage volume of the endpoints created for inference recommendation. The inference recommendation job will fail asynchronously during endpoint configuration creation if the role passed does not have `kms:CreateGrant` permission.

The `KmsKeyId` can be any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:<region>:<account>:key/<key-id-12ab-34cd-56ef-1234567890ab>"`
- // KMS Key Alias  `"alias/ExampleAlias"`
- // Amazon Resource Name (ARN) of a KMS Key Alias  `"arn:aws:kms:<region>:<account>:alias/<ExampleAlias>"`

For more information about key identifiers, see [Key identifiers (KeyID)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id) in the Amazon Web Services Key Management Service (Amazon Web Services KMS) documentation.

ContainerConfig -> (structure)

Specifies mandatory fields for running an Inference Recommender job. The fields specified in `ContainerConfig` override the corresponding fields in the model package.

Domain -> (string)

The machine learning domain of the model and its components.

Valid Values: `COMPUTER_VISION | NATURAL_LANGUAGE_PROCESSING | MACHINE_LEARNING`

Task -> (string)

The machine learning task that the model accomplishes.

Valid Values: `IMAGE_CLASSIFICATION | OBJECT_DETECTION | TEXT_GENERATION | IMAGE_SEGMENTATION | FILL_MASK | CLASSIFICATION | REGRESSION | OTHER`

Framework -> (string)

The machine learning framework of the container image.

Valid Values: `TENSORFLOW | PYTORCH | XGBOOST | SAGEMAKER-SCIKIT-LEARN`

FrameworkVersion -> (string)

The framework version of the container image.

PayloadConfig -> (structure)

Specifies the `SamplePayloadUrl` and all other sample payload-related fields.

SamplePayloadUrl -> (string)

The Amazon Simple Storage Service (Amazon S3) path where the sample payload is stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).

SupportedContentTypes -> (list)

The supported MIME types for the input data.

(string)

NearestModelName -> (string)

The name of a pre-trained machine learning model benchmarked by Amazon SageMaker Inference Recommender that matches your model.

Valid Values: `efficientnetb7 | unet | xgboost | faster-rcnn-resnet101 | nasnetlarge | vgg16 | inception-v3 | mask-rcnn | sagemaker-scikit-learn | densenet201-gluon | resnet18v2-gluon | xception | densenet201 | yolov4 | resnet152 | bert-base-cased | xceptionV1-keras | resnet50 | retinanet`

SupportedInstanceTypes -> (list)

A list of the instance types that are used to generate inferences in real-time.

(string)

SupportedEndpointType -> (string)

The endpoint type to receive recommendations for. By default this is null, and the results of the inference recommendation job return a combined list of both real-time and serverless benchmarks. By specifying a value for this field, you can receive a longer list of benchmarks for the desired endpoint type.

DataInputConfig -> (string)

Specifies the name and shape of the expected data inputs for your trained model with a JSON dictionary form. This field is used for optimizing your model using SageMaker Neo. For more information, see [DataInputConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InputConfig.html#sagemaker-Type-InputConfig-DataInputConfig) .

SupportedResponseMIMETypes -> (list)

The supported MIME types for the output data.

(string)

Endpoints -> (list)

Existing customer endpoints on which to run an Inference Recommender job.

(structure)

Details about a customer endpoint that was compared in an Inference Recommender job.

EndpointName -> (string)

The name of a customerâs endpoint.

VpcConfig -> (structure)

Inference Recommender provisions SageMaker endpoints with access to VPC in the inference recommendation job.

SecurityGroupIds -> (list)

The VPC security group IDs. IDs have the form of `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your model.

(string)

StoppingConditions -> (structure)

The stopping conditions that you provided when you initiated the job.

MaxInvocations -> (integer)

The maximum number of requests per minute expected for the endpoint.

ModelLatencyThresholds -> (list)

The interval of time taken by a model to respond as viewed from SageMaker. The interval includes the local communication time taken to send the request and to fetch the response from the container of a model and the time taken to complete the inference in the container.

(structure)

The model latency threshold.

Percentile -> (string)

The model latency percentile threshold. Acceptable values are `P95` and `P99` . For custom load tests, specify the value as `P95` .

ValueInMilliseconds -> (integer)

The model latency percentile value in milliseconds.

FlatInvocations -> (string)

Stops a load test when the number of invocations (TPS) peaks and flattens, which means that the instance has reached capacity. The default value is `Stop` . If you want the load test to continue after invocations have flattened, set the value to `Continue` .

InferenceRecommendations -> (list)

The recommendations made by Inference Recommender.

(structure)

A list of recommendations made by Amazon SageMaker Inference Recommender.

RecommendationId -> (string)

The recommendation ID which uniquely identifies each recommendation.

Metrics -> (structure)

The metrics used to decide what recommendation to make.

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

EndpointConfiguration -> (structure)

Defines the endpoint configuration parameters.

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

Defines the model configuration.

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

InvocationEndTime -> (timestamp)

A timestamp that shows when the benchmark completed.

InvocationStartTime -> (timestamp)

A timestamp that shows when the benchmark started.

EndpointPerformances -> (list)

The performance results from running an Inference Recommender job on an existing endpoint.

(structure)

The performance results from running an Inference Recommender job on an existing endpoint.

Metrics -> (structure)

The metrics for an existing endpoint.

MaxInvocations -> (integer)

The expected maximum number of requests per minute for the instance.

ModelLatency -> (integer)

The expected model latency at maximum invocations per minute for the instance.

EndpointInfo -> (structure)

Details about a customer endpoint that was compared in an Inference Recommender job.

EndpointName -> (string)

The name of a customerâs endpoint.