# describe-inference-experimentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-inference-experiment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-inference-experiment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-inference-experiment

## Description

Returns details about an inference experiment.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeInferenceExperiment)

## Synopsis

```
describe-inference-experiment
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

The name of the inference experiment to describe.

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

Arn -> (string)

The ARN of the inference experiment being described.

Name -> (string)

The name of the inference experiment.

Type -> (string)

The type of the inference experiment.

Schedule -> (structure)

The duration for which the inference experiment ran or will run.

StartTime -> (timestamp)

The timestamp at which the inference experiment started or will start.

EndTime -> (timestamp)

The timestamp at which the inference experiment ended or will end.

Status -> (string)

The status of the inference experiment. The following are the possible statuses for an inference experiment:

- `Creating` - Amazon SageMaker is creating your experiment.
- `Created` - Amazon SageMaker has finished the creation of your experiment and will begin the experiment at the scheduled time.
- `Updating` - When you make changes to your experiment, your experiment shows as updating.
- `Starting` - Amazon SageMaker is beginning your experiment.
- `Running` - Your experiment is in progress.
- `Stopping` - Amazon SageMaker is stopping your experiment.
- `Completed` - Your experiment has completed.
- `Cancelled` - When you conclude your experiment early using the [StopInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopInferenceExperiment.html) API, or if any operation fails with an unexpected error, it shows as cancelled.

StatusReason -> (string)

The error message or client-specified `Reason` from the [StopInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopInferenceExperiment.html) API, that explains the status of the inference experiment.

Description -> (string)

The description of the inference experiment.

CreationTime -> (timestamp)

The timestamp at which you created the inference experiment.

CompletionTime -> (timestamp)

The timestamp at which the inference experiment was completed.

LastModifiedTime -> (timestamp)

The timestamp at which you last modified the inference experiment.

RoleArn -> (string)

The ARN of the IAM role that Amazon SageMaker can assume to access model artifacts and container images, and manage Amazon SageMaker Inference endpoints for model deployment.

EndpointMetadata -> (structure)

The metadata of the endpoint on which the inference experiment ran.

EndpointName -> (string)

The name of the endpoint.

EndpointConfigName -> (string)

The name of the endpoint configuration.

EndpointStatus -> (string)

The status of the endpoint. For possible values of the status of an endpoint, see [EndpointSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EndpointSummary.html) .

FailureReason -> (string)

If the status of the endpoint is `Failed` , or the status is `InService` but update operation fails, this provides the reason why it failed.

ModelVariants -> (list)

An array of `ModelVariantConfigSummary` objects. There is one for each variant in the inference experiment. Each `ModelVariantConfigSummary` object in the array describes the infrastructure configuration for deploying the corresponding variant.

(structure)

Summary of the deployment configuration of a model.

ModelName -> (string)

The name of the Amazon SageMaker Model entity.

VariantName -> (string)

The name of the variant.

InfrastructureConfig -> (structure)

The configuration of the infrastructure that the model has been deployed to.

InfrastructureType -> (string)

The inference option to which to deploy your model. Possible values are the following:

- `RealTime` : Deploy to real-time inference.

RealTimeInferenceConfig -> (structure)

The infrastructure configuration for deploying the model to real-time inference.

InstanceType -> (string)

The instance type the model is deployed to.

InstanceCount -> (integer)

The number of instances of the type specified by `InstanceType` .

Status -> (string)

The status of deployment for the model variant on the hosted inference endpoint.

- `Creating` - Amazon SageMaker is preparing the model variant on the hosted inference endpoint.
- `InService` - The model variant is running on the hosted inference endpoint.
- `Updating` - Amazon SageMaker is updating the model variant on the hosted inference endpoint.
- `Deleting` - Amazon SageMaker is deleting the model variant on the hosted inference endpoint.
- `Deleted` - The model variant has been deleted on the hosted inference endpoint. This can only happen after stopping the experiment.

DataStorageConfig -> (structure)

The Amazon S3 location and configuration for storing inference request and response data.

Destination -> (string)

The Amazon S3 bucket where the inference request and response data is stored.

KmsKey -> (string)

The Amazon Web Services Key Management Service key that Amazon SageMaker uses to encrypt captured data at rest using Amazon S3 server-side encryption.

ContentType -> (structure)

Configuration specifying how to treat different headers. If no headers are specified Amazon SageMaker AI will by default base64 encode when capturing the data.

CsvContentTypes -> (list)

The list of all content type headers that Amazon SageMaker AI will treat as CSV and capture accordingly.

(string)

JsonContentTypes -> (list)

The list of all content type headers that SageMaker AI will treat as JSON and capture accordingly.

(string)

ShadowModeConfig -> (structure)

The configuration of `ShadowMode` inference experiment type, which shows the production variant that takes all the inference requests, and the shadow variant to which Amazon SageMaker replicates a percentage of the inference requests. For the shadow variant it also shows the percentage of requests that Amazon SageMaker replicates.

SourceModelVariantName -> (string)

The name of the production variant, which takes all the inference requests.

ShadowModelVariants -> (list)

List of shadow variant configurations.

(structure)

The name and sampling percentage of a shadow variant.

ShadowModelVariantName -> (string)

The name of the shadow variant.

SamplingPercentage -> (integer)

The percentage of inference requests that Amazon SageMaker replicates from the production variant to the shadow variant.

KmsKey -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint. For more information, see [CreateInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceExperiment.html) .