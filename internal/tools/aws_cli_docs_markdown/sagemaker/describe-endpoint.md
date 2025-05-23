# describe-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-endpoint

## Description

Returns the description of an endpoint.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeEndpoint)

## Synopsis

```
describe-endpoint
--endpoint-name <value>
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

`--endpoint-name` (string)

The name of the endpoint.

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

EndpointName -> (string)

Name of the endpoint.

EndpointArn -> (string)

The Amazon Resource Name (ARN) of the endpoint.

EndpointConfigName -> (string)

The name of the endpoint configuration associated with this endpoint.

ProductionVariants -> (list)

An array of [ProductionVariantSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantSummary.html) objects, one for each model hosted behind this endpoint.

(structure)

Describes weight and capacities for a production variant associated with an endpoint. If you sent a request to the `UpdateEndpointWeightsAndCapacities` API and the endpoint status is `Updating` , you get different desired and current values.

VariantName -> (string)

The name of the variant.

DeployedImages -> (list)

An array of `DeployedImage` objects that specify the Amazon EC2 Container Registry paths of the inference images deployed on instances of this `ProductionVariant` .

(structure)

Gets the Amazon EC2 Container Registry path of the docker image of the model that is hosted in this [ProductionVariant](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariant.html) .

If you used the `registry/repository[:tag]` form to specify the image path of the primary container when you created the model hosted in this `ProductionVariant` , the path resolves to a path of the form `registry/repository[@digest]` . A digest is a hash value that identifies a specific version of an image. For information about Amazon ECR paths, see [Pulling an Image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html) in the *Amazon ECR User Guide* .

SpecifiedImage -> (string)

The image path you specified when you created the model.

ResolvedImage -> (string)

The specific digest path of the image hosted in this `ProductionVariant` .

ResolutionTime -> (timestamp)

The date and time when the image path for the model resolved to the `ResolvedImage`

CurrentWeight -> (float)

The weight associated with the variant.

DesiredWeight -> (float)

The requested weight, as specified in the `UpdateEndpointWeightsAndCapacities` request.

CurrentInstanceCount -> (integer)

The number of instances associated with the variant.

DesiredInstanceCount -> (integer)

The number of instances requested in the `UpdateEndpointWeightsAndCapacities` request.

VariantStatus -> (list)

The endpoint variant status which describes the current deployment stage status or operational status.

(structure)

Describes the status of the production variant.

Status -> (string)

The endpoint variant status which describes the current deployment stage status or operational status.

- `Creating` : Creating inference resources for the production variant.
- `Deleting` : Terminating inference resources for the production variant.
- `Updating` : Updating capacity for the production variant.
- `ActivatingTraffic` : Turning on traffic for the production variant.
- `Baking` : Waiting period to monitor the CloudWatch alarms in the automatic rollback configuration.

StatusMessage -> (string)

A message that describes the status of the production variant.

StartTime -> (timestamp)

The start time of the current status change.

CurrentServerlessConfig -> (structure)

The serverless configuration for the endpoint.

MemorySizeInMB -> (integer)

The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.

MaxConcurrency -> (integer)

The maximum number of concurrent invocations your serverless endpoint can process.

ProvisionedConcurrency -> (integer)

The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency` .

### Note

This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) .

DesiredServerlessConfig -> (structure)

The serverless configuration requested for the endpoint update.

MemorySizeInMB -> (integer)

The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.

MaxConcurrency -> (integer)

The maximum number of concurrent invocations your serverless endpoint can process.

ProvisionedConcurrency -> (integer)

The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency` .

### Note

This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) .

ManagedInstanceScaling -> (structure)

Settings that control the range in the number of instances that the endpoint provisions as it scales up or down to accommodate traffic.

Status -> (string)

Indicates whether managed instance scaling is enabled.

MinInstanceCount -> (integer)

The minimum number of instances that the endpoint must retain when it scales down to accommodate a decrease in traffic.

MaxInstanceCount -> (integer)

The maximum number of instances that the endpoint can provision when it scales up to accommodate an increase in traffic.

RoutingConfig -> (structure)

Settings that control how the endpoint routes incoming traffic to the instances that the endpoint hosts.

RoutingStrategy -> (string)

Sets how the endpoint routes incoming traffic:

- `LEAST_OUTSTANDING_REQUESTS` : The endpoint routes requests to the specific instances that have more capacity to process them.
- `RANDOM` : The endpoint routes each request to a randomly chosen instance.

DataCaptureConfig -> (structure)

The currently active data capture configuration used by your Endpoint.

EnableCapture -> (boolean)

Whether data capture is enabled or disabled.

CaptureStatus -> (string)

Whether data capture is currently functional.

CurrentSamplingPercentage -> (integer)

The percentage of requests being captured by your Endpoint.

DestinationS3Uri -> (string)

The Amazon S3 location being used to capture the data.

KmsKeyId -> (string)

The KMS key being used to encrypt the data in Amazon S3.

EndpointStatus -> (string)

The status of the endpoint.

- `OutOfService` : Endpoint is not available to take incoming requests.
- `Creating` : [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) is executing.
- `Updating` : [UpdateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html) or [UpdateEndpointWeightsAndCapacities](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpointWeightsAndCapacities.html) is executing.
- `SystemUpdating` : Endpoint is undergoing maintenance and cannot be updated or deleted or re-scaled until it has completed. This maintenance operation does not change any customer-specified values such as VPC config, KMS encryption, model, instance type, or instance count.
- `RollingBack` : Endpoint fails to scale up or down or change its variant weight and is in the process of rolling back to its previous configuration. Once the rollback completes, endpoint returns to an `InService` status. This transitional status only applies to an endpoint that has autoscaling enabled and is undergoing variant weight or capacity changes as part of an [UpdateEndpointWeightsAndCapacities](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpointWeightsAndCapacities.html) call or when the [UpdateEndpointWeightsAndCapacities](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpointWeightsAndCapacities.html) operation is called explicitly.
- `InService` : Endpoint is available to process incoming requests.
- `Deleting` : [DeleteEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteEndpoint.html) is executing.
- `Failed` : Endpoint could not be created, updated, or re-scaled. Use the `FailureReason` value returned by [DescribeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html) for information about the failure. [DeleteEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteEndpoint.html) is the only operation that can be performed on a failed endpoint.
- `UpdateRollbackFailed` : Both the rolling deployment and auto-rollback failed. Your endpoint is in service with a mix of the old and new endpoint configurations. For information about how to remedy this issue and restore the endpointâs status to `InService` , see [Rolling Deployments](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-rolling.html) .

FailureReason -> (string)

If the status of the endpoint is `Failed` , the reason why it failed.

CreationTime -> (timestamp)

A timestamp that shows when the endpoint was created.

LastModifiedTime -> (timestamp)

A timestamp that shows when the endpoint was last modified.

LastDeploymentConfig -> (structure)

The most recent deployment configuration for the endpoint.

BlueGreenUpdatePolicy -> (structure)

Update policy for a blue/green deployment. If this update policy is specified, SageMaker creates a new fleet during the deployment while maintaining the old fleet. SageMaker flips traffic to the new fleet according to the specified traffic routing configuration. Only one update policy should be used in the deployment configuration. If no update policy is specified, SageMaker uses a blue/green deployment strategy with all at once traffic shifting by default.

TrafficRoutingConfiguration -> (structure)

Defines the traffic routing strategy to shift traffic from the old fleet to the new fleet during an endpoint deployment.

Type -> (string)

Traffic routing strategy type.

- `ALL_AT_ONCE` : Endpoint traffic shifts to the new fleet in a single step.
- `CANARY` : Endpoint traffic shifts to the new fleet in two steps. The first step is the canary, which is a small portion of the traffic. The second step is the remainder of the traffic.
- `LINEAR` : Endpoint traffic shifts to the new fleet in n steps of a configurable size.

WaitIntervalInSeconds -> (integer)

The waiting time (in seconds) between incremental steps to turn on traffic on the new endpoint fleet.

CanarySize -> (structure)

Batch size for the first step to turn on traffic on the new endpoint fleet. `Value` must be less than or equal to 50% of the variantâs total instance count.

Type -> (string)

Specifies the endpoint capacity type.

- `INSTANCE_COUNT` : The endpoint activates based on the number of instances.
- `CAPACITY_PERCENT` : The endpoint activates based on the specified percentage of capacity.

Value -> (integer)

Defines the capacity size, either as a number of instances or a capacity percentage.

LinearStepSize -> (structure)

Batch size for each step to turn on traffic on the new endpoint fleet. `Value` must be 10-50% of the variantâs total instance count.

Type -> (string)

Specifies the endpoint capacity type.

- `INSTANCE_COUNT` : The endpoint activates based on the number of instances.
- `CAPACITY_PERCENT` : The endpoint activates based on the specified percentage of capacity.

Value -> (integer)

Defines the capacity size, either as a number of instances or a capacity percentage.

TerminationWaitInSeconds -> (integer)

Additional waiting time in seconds after the completion of an endpoint deployment before terminating the old endpoint fleet. Default is 0.

MaximumExecutionTimeoutInSeconds -> (integer)

Maximum execution timeout for the deployment. Note that the timeout value should be larger than the total waiting time specified in `TerminationWaitInSeconds` and `WaitIntervalInSeconds` .

RollingUpdatePolicy -> (structure)

Specifies a rolling deployment strategy for updating a SageMaker endpoint.

MaximumBatchSize -> (structure)

Batch size for each rolling step to provision capacity and turn on traffic on the new endpoint fleet, and terminate capacity on the old endpoint fleet. Value must be between 5% to 50% of the variantâs total instance count.

Type -> (string)

Specifies the endpoint capacity type.

- `INSTANCE_COUNT` : The endpoint activates based on the number of instances.
- `CAPACITY_PERCENT` : The endpoint activates based on the specified percentage of capacity.

Value -> (integer)

Defines the capacity size, either as a number of instances or a capacity percentage.

WaitIntervalInSeconds -> (integer)

The length of the baking period, during which SageMaker monitors alarms for each batch on the new fleet.

MaximumExecutionTimeoutInSeconds -> (integer)

The time limit for the total deployment. Exceeding this limit causes a timeout.

RollbackMaximumBatchSize -> (structure)

Batch size for rollback to the old endpoint fleet. Each rolling step to provision capacity and turn on traffic on the old endpoint fleet, and terminate capacity on the new endpoint fleet. If this field is absent, the default value will be set to 100% of total capacity which means to bring up the whole capacity of the old fleet at once during rollback.

Type -> (string)

Specifies the endpoint capacity type.

- `INSTANCE_COUNT` : The endpoint activates based on the number of instances.
- `CAPACITY_PERCENT` : The endpoint activates based on the specified percentage of capacity.

Value -> (integer)

Defines the capacity size, either as a number of instances or a capacity percentage.

AutoRollbackConfiguration -> (structure)

Automatic rollback configuration for handling endpoint deployment failures and recovery.

Alarms -> (list)

List of CloudWatch alarms in your account that are configured to monitor metrics on an endpoint. If any alarms are tripped during a deployment, SageMaker rolls back the deployment.

(structure)

An Amazon CloudWatch alarm configured to monitor metrics on an endpoint.

AlarmName -> (string)

The name of a CloudWatch alarm in your account.

AsyncInferenceConfig -> (structure)

Returns the description of an endpoint configuration created using the ` `CreateEndpointConfig` [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig).html`__ API.

ClientConfig -> (structure)

Configures the behavior of the client used by SageMaker to interact with the model container during asynchronous inference.

MaxConcurrentInvocationsPerInstance -> (integer)

The maximum number of concurrent requests sent by the SageMaker client to the model container. If no value is provided, SageMaker chooses an optimal value.

OutputConfig -> (structure)

Specifies the configuration for asynchronous inference invocation outputs.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that SageMaker uses to encrypt the asynchronous inference output in Amazon S3.

S3OutputPath -> (string)

The Amazon S3 location to upload inference responses to.

NotificationConfig -> (structure)

Specifies the configuration for notifications of inference results for asynchronous inference.

SuccessTopic -> (string)

Amazon SNS topic to post a notification to when inference completes successfully. If no topic is provided, no notification is sent on success.

ErrorTopic -> (string)

Amazon SNS topic to post a notification to when inference fails. If no topic is provided, no notification is sent on failure.

IncludeInferenceResponseIn -> (list)

The Amazon SNS topics where you want the inference response to be included.

### Note

The inference response is included only if the response size is less than or equal to 128 KB.

(string)

S3FailurePath -> (string)

The Amazon S3 location to upload failure inference responses to.

PendingDeploymentSummary -> (structure)

Returns the summary of an in-progress deployment. This field is only returned when the endpoint is creating or updating with a new endpoint configuration.

EndpointConfigName -> (string)

The name of the endpoint configuration used in the deployment.

ProductionVariants -> (list)

An array of [PendingProductionVariantSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PendingProductionVariantSummary.html) objects, one for each model hosted behind this endpoint for the in-progress deployment.

(structure)

The production variant summary for a deployment when an endpoint is creating or updating with the [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) or [UpdateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html) operations. Describes the `VariantStatus` , weight and capacity for a production variant associated with an endpoint.

VariantName -> (string)

The name of the variant.

DeployedImages -> (list)

An array of `DeployedImage` objects that specify the Amazon EC2 Container Registry paths of the inference images deployed on instances of this `ProductionVariant` .

(structure)

Gets the Amazon EC2 Container Registry path of the docker image of the model that is hosted in this [ProductionVariant](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariant.html) .

If you used the `registry/repository[:tag]` form to specify the image path of the primary container when you created the model hosted in this `ProductionVariant` , the path resolves to a path of the form `registry/repository[@digest]` . A digest is a hash value that identifies a specific version of an image. For information about Amazon ECR paths, see [Pulling an Image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html) in the *Amazon ECR User Guide* .

SpecifiedImage -> (string)

The image path you specified when you created the model.

ResolvedImage -> (string)

The specific digest path of the image hosted in this `ProductionVariant` .

ResolutionTime -> (timestamp)

The date and time when the image path for the model resolved to the `ResolvedImage`

CurrentWeight -> (float)

The weight associated with the variant.

DesiredWeight -> (float)

The requested weight for the variant in this deployment, as specified in the endpoint configuration for the endpoint. The value is taken from the request to the [CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html) operation.

CurrentInstanceCount -> (integer)

The number of instances associated with the variant.

DesiredInstanceCount -> (integer)

The number of instances requested in this deployment, as specified in the endpoint configuration for the endpoint. The value is taken from the request to the [CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html) operation.

InstanceType -> (string)

The type of instances associated with the variant.

AcceleratorType -> (string)

This parameter is no longer supported. Elastic Inference (EI) is no longer available.

This parameter was used to specify the size of the EI instance to use for the production variant.

VariantStatus -> (list)

The endpoint variant status which describes the current deployment stage status or operational status.

(structure)

Describes the status of the production variant.

Status -> (string)

The endpoint variant status which describes the current deployment stage status or operational status.

- `Creating` : Creating inference resources for the production variant.
- `Deleting` : Terminating inference resources for the production variant.
- `Updating` : Updating capacity for the production variant.
- `ActivatingTraffic` : Turning on traffic for the production variant.
- `Baking` : Waiting period to monitor the CloudWatch alarms in the automatic rollback configuration.

StatusMessage -> (string)

A message that describes the status of the production variant.

StartTime -> (timestamp)

The start time of the current status change.

CurrentServerlessConfig -> (structure)

The serverless configuration for the endpoint.

MemorySizeInMB -> (integer)

The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.

MaxConcurrency -> (integer)

The maximum number of concurrent invocations your serverless endpoint can process.

ProvisionedConcurrency -> (integer)

The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency` .

### Note

This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) .

DesiredServerlessConfig -> (structure)

The serverless configuration requested for this deployment, as specified in the endpoint configuration for the endpoint.

MemorySizeInMB -> (integer)

The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.

MaxConcurrency -> (integer)

The maximum number of concurrent invocations your serverless endpoint can process.

ProvisionedConcurrency -> (integer)

The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency` .

### Note

This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) .

ManagedInstanceScaling -> (structure)

Settings that control the range in the number of instances that the endpoint provisions as it scales up or down to accommodate traffic.

Status -> (string)

Indicates whether managed instance scaling is enabled.

MinInstanceCount -> (integer)

The minimum number of instances that the endpoint must retain when it scales down to accommodate a decrease in traffic.

MaxInstanceCount -> (integer)

The maximum number of instances that the endpoint can provision when it scales up to accommodate an increase in traffic.

RoutingConfig -> (structure)

Settings that control how the endpoint routes incoming traffic to the instances that the endpoint hosts.

RoutingStrategy -> (string)

Sets how the endpoint routes incoming traffic:

- `LEAST_OUTSTANDING_REQUESTS` : The endpoint routes requests to the specific instances that have more capacity to process them.
- `RANDOM` : The endpoint routes each request to a randomly chosen instance.

StartTime -> (timestamp)

The start time of the deployment.

ShadowProductionVariants -> (list)

An array of [PendingProductionVariantSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PendingProductionVariantSummary.html) objects, one for each model hosted behind this endpoint in shadow mode with production traffic replicated from the model specified on `ProductionVariants` for the in-progress deployment.

(structure)

The production variant summary for a deployment when an endpoint is creating or updating with the [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) or [UpdateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html) operations. Describes the `VariantStatus` , weight and capacity for a production variant associated with an endpoint.

VariantName -> (string)

The name of the variant.

DeployedImages -> (list)

An array of `DeployedImage` objects that specify the Amazon EC2 Container Registry paths of the inference images deployed on instances of this `ProductionVariant` .

(structure)

Gets the Amazon EC2 Container Registry path of the docker image of the model that is hosted in this [ProductionVariant](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariant.html) .

If you used the `registry/repository[:tag]` form to specify the image path of the primary container when you created the model hosted in this `ProductionVariant` , the path resolves to a path of the form `registry/repository[@digest]` . A digest is a hash value that identifies a specific version of an image. For information about Amazon ECR paths, see [Pulling an Image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html) in the *Amazon ECR User Guide* .

SpecifiedImage -> (string)

The image path you specified when you created the model.

ResolvedImage -> (string)

The specific digest path of the image hosted in this `ProductionVariant` .

ResolutionTime -> (timestamp)

The date and time when the image path for the model resolved to the `ResolvedImage`

CurrentWeight -> (float)

The weight associated with the variant.

DesiredWeight -> (float)

The requested weight for the variant in this deployment, as specified in the endpoint configuration for the endpoint. The value is taken from the request to the [CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html) operation.

CurrentInstanceCount -> (integer)

The number of instances associated with the variant.

DesiredInstanceCount -> (integer)

The number of instances requested in this deployment, as specified in the endpoint configuration for the endpoint. The value is taken from the request to the [CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html) operation.

InstanceType -> (string)

The type of instances associated with the variant.

AcceleratorType -> (string)

This parameter is no longer supported. Elastic Inference (EI) is no longer available.

This parameter was used to specify the size of the EI instance to use for the production variant.

VariantStatus -> (list)

The endpoint variant status which describes the current deployment stage status or operational status.

(structure)

Describes the status of the production variant.

Status -> (string)

The endpoint variant status which describes the current deployment stage status or operational status.

- `Creating` : Creating inference resources for the production variant.
- `Deleting` : Terminating inference resources for the production variant.
- `Updating` : Updating capacity for the production variant.
- `ActivatingTraffic` : Turning on traffic for the production variant.
- `Baking` : Waiting period to monitor the CloudWatch alarms in the automatic rollback configuration.

StatusMessage -> (string)

A message that describes the status of the production variant.

StartTime -> (timestamp)

The start time of the current status change.

CurrentServerlessConfig -> (structure)

The serverless configuration for the endpoint.

MemorySizeInMB -> (integer)

The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.

MaxConcurrency -> (integer)

The maximum number of concurrent invocations your serverless endpoint can process.

ProvisionedConcurrency -> (integer)

The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency` .

### Note

This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) .

DesiredServerlessConfig -> (structure)

The serverless configuration requested for this deployment, as specified in the endpoint configuration for the endpoint.

MemorySizeInMB -> (integer)

The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.

MaxConcurrency -> (integer)

The maximum number of concurrent invocations your serverless endpoint can process.

ProvisionedConcurrency -> (integer)

The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency` .

### Note

This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) .

ManagedInstanceScaling -> (structure)

Settings that control the range in the number of instances that the endpoint provisions as it scales up or down to accommodate traffic.

Status -> (string)

Indicates whether managed instance scaling is enabled.

MinInstanceCount -> (integer)

The minimum number of instances that the endpoint must retain when it scales down to accommodate a decrease in traffic.

MaxInstanceCount -> (integer)

The maximum number of instances that the endpoint can provision when it scales up to accommodate an increase in traffic.

RoutingConfig -> (structure)

Settings that control how the endpoint routes incoming traffic to the instances that the endpoint hosts.

RoutingStrategy -> (string)

Sets how the endpoint routes incoming traffic:

- `LEAST_OUTSTANDING_REQUESTS` : The endpoint routes requests to the specific instances that have more capacity to process them.
- `RANDOM` : The endpoint routes each request to a randomly chosen instance.

ExplainerConfig -> (structure)

The configuration parameters for an explainer.

ClarifyExplainerConfig -> (structure)

A member of `ExplainerConfig` that contains configuration parameters for the SageMaker Clarify explainer.

EnableExplanations -> (string)

A JMESPath boolean expression used to filter which records to explain. Explanations are activated by default. See ` `EnableExplanations` [https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html#clarify-online-explainability-create-endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html#clarify-online-explainability-create-endpoint)-enable`__ for additional information.

InferenceConfig -> (structure)

The inference configuration parameter for the model container.

FeaturesAttribute -> (string)

Provides the JMESPath expression to extract the features from a model container input in JSON Lines format. For example, if `FeaturesAttribute` is the JMESPath expression `'myfeatures'` , it extracts a list of features `[1,2,3]` from request data `'{"myfeatures":[1,2,3]}'` .

ContentTemplate -> (string)

A template string used to format a JSON record into an acceptable model container input. For example, a `ContentTemplate` string `'{"myfeatures":$features}'` will format a list of features `[1,2,3]` into the record string `'{"myfeatures":[1,2,3]}'` . Required only when the model container input is in JSON Lines format.

MaxRecordCount -> (integer)

The maximum number of records in a request that the model container can process when querying the model container for the predictions of a [synthetic dataset](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html#clarify-online-explainability-create-endpoint-synthetic) . A record is a unit of input data that inference can be made on, for example, a single line in CSV data. If `MaxRecordCount` is `1` , the model container expects one record per request. A value of 2 or greater means that the model expects batch requests, which can reduce overhead and speed up the inferencing process. If this parameter is not provided, the explainer will tune the record count per request according to the model containerâs capacity at runtime.

MaxPayloadInMB -> (integer)

The maximum payload size (MB) allowed of a request from the explainer to the model container. Defaults to `6` MB.

ProbabilityIndex -> (integer)

A zero-based index used to extract a probability value (score) or list from model container output in CSV format. If this value is not provided, the entire model container output will be treated as a probability value (score) or list.

**Example for a single class model:** If the model container output consists of a string-formatted prediction label followed by its probability: `'1,0.6'` , set `ProbabilityIndex` to `1` to select the probability value `0.6` .

**Example for a multiclass model:** If the model container output consists of a string-formatted prediction label followed by its probability: `'"[\'cat\',\'dog\',\'fish\']","[0.1,0.6,0.3]"'` , set `ProbabilityIndex` to `1` to select the probability values `[0.1,0.6,0.3]` .

LabelIndex -> (integer)

A zero-based index used to extract a label header or list of label headers from model container output in CSV format.

**Example for a multiclass model:** If the model container output consists of label headers followed by probabilities: `'"[\'cat\',\'dog\',\'fish\']","[0.1,0.6,0.3]"'` , set `LabelIndex` to `0` to select the label headers `['cat','dog','fish']` .

ProbabilityAttribute -> (string)

A JMESPath expression used to extract the probability (or score) from the model container output if the model container is in JSON Lines format.

**Example** : If the model container output of a single request is `'{"predicted_label":1,"probability":0.6}'` , then set `ProbabilityAttribute` to `'probability'` .

LabelAttribute -> (string)

A JMESPath expression used to locate the list of label headers in the model container output.

**Example** : If the model container output of a batch request is `'{"labels":["cat","dog","fish"],"probability":[0.6,0.3,0.1]}'` , then set `LabelAttribute` to `'labels'` to extract the list of label headers `["cat","dog","fish"]`

LabelHeaders -> (list)

For multiclass classification problems, the label headers are the names of the classes. Otherwise, the label header is the name of the predicted label. These are used to help readability for the output of the `InvokeEndpoint` API. See the [response](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-invoke-endpoint.html#clarify-online-explainability-response) section under **Invoke the endpoint** in the Developer Guide for more information. If there are no label headers in the model container output, provide them manually using this parameter.

(string)

FeatureHeaders -> (list)

The names of the features. If provided, these are included in the endpoint response payload to help readability of the `InvokeEndpoint` output. See the [Response](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-invoke-endpoint.html#clarify-online-explainability-response) section under **Invoke the endpoint** in the Developer Guide for more information.

(string)

FeatureTypes -> (list)

A list of data types of the features (optional). Applicable only to NLP explainability. If provided, `FeatureTypes` must have at least one `'text'` string (for example, `['text']` ). If `FeatureTypes` is not provided, the explainer infers the feature types based on the baseline data. The feature types are included in the endpoint response payload. For additional information see the [response](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-invoke-endpoint.html#clarify-online-explainability-response) section under **Invoke the endpoint** in the Developer Guide for more information.

(string)

ShapConfig -> (structure)

The configuration for SHAP analysis.

ShapBaselineConfig -> (structure)

The configuration for the SHAP baseline of the Kernal SHAP algorithm.

MimeType -> (string)

The MIME type of the baseline data. Choose from `'text/csv'` or `'application/jsonlines'` . Defaults to `'text/csv'` .

ShapBaseline -> (string)

The inline SHAP baseline data in string format. `ShapBaseline` can have one or multiple records to be used as the baseline dataset. The format of the SHAP baseline file should be the same format as the training dataset. For example, if the training dataset is in CSV format and each record contains four features, and all features are numerical, then the format of the baseline data should also share these characteristics. For natural language processing (NLP) of text columns, the baseline value should be the value used to replace the unit of text specified by the `Granularity` of the `TextConfig` parameter. The size limit for `ShapBasline` is 4 KB. Use the `ShapBaselineUri` parameter if you want to provide more than 4 KB of baseline data.

ShapBaselineUri -> (string)

The uniform resource identifier (URI) of the S3 bucket where the SHAP baseline file is stored. The format of the SHAP baseline file should be the same format as the format of the training dataset. For example, if the training dataset is in CSV format, and each record in the training dataset has four features, and all features are numerical, then the baseline file should also have this same format. Each record should contain only the features. If you are using a virtual private cloud (VPC), the `ShapBaselineUri` should be accessible to the VPC. For more information about setting up endpoints with Amazon Virtual Private Cloud, see [Give SageMaker access to Resources in your Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html) .

NumberOfSamples -> (integer)

The number of samples to be used for analysis by the Kernal SHAP algorithm.

### Note

The number of samples determines the size of the synthetic dataset, which has an impact on latency of explainability requests. For more information, see the **Synthetic data** of [Configure and create an endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html) .

UseLogit -> (boolean)

A Boolean toggle to indicate if you want to use the logit function (true) or log-odds units (false) for model predictions. Defaults to false.

Seed -> (integer)

The starting value used to initialize the random number generator in the explainer. Provide a value for this parameter to obtain a deterministic SHAP result.

TextConfig -> (structure)

A parameter that indicates if text features are treated as text and explanations are provided for individual units of text. Required for natural language processing (NLP) explainability only.

Language -> (string)

Specifies the language of the text features in [`ISO 639-1 < https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-endpoint.html#id1) or [ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3) code of a supported language.

### Note

For a mix of multiple languages, use code `'xx'` .

Granularity -> (string)

The unit of granularity for the analysis of text features. For example, if the unit is `'token'` , then each token (like a word in English) of the text is treated as a feature. SHAP values are computed for each unit/feature.

ShadowProductionVariants -> (list)

An array of [ProductionVariantSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantSummary.html) objects, one for each model that you want to host at this endpoint in shadow mode with production traffic replicated from the model specified on `ProductionVariants` .

(structure)

Describes weight and capacities for a production variant associated with an endpoint. If you sent a request to the `UpdateEndpointWeightsAndCapacities` API and the endpoint status is `Updating` , you get different desired and current values.

VariantName -> (string)

The name of the variant.

DeployedImages -> (list)

An array of `DeployedImage` objects that specify the Amazon EC2 Container Registry paths of the inference images deployed on instances of this `ProductionVariant` .

(structure)

Gets the Amazon EC2 Container Registry path of the docker image of the model that is hosted in this [ProductionVariant](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariant.html) .

If you used the `registry/repository[:tag]` form to specify the image path of the primary container when you created the model hosted in this `ProductionVariant` , the path resolves to a path of the form `registry/repository[@digest]` . A digest is a hash value that identifies a specific version of an image. For information about Amazon ECR paths, see [Pulling an Image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html) in the *Amazon ECR User Guide* .

SpecifiedImage -> (string)

The image path you specified when you created the model.

ResolvedImage -> (string)

The specific digest path of the image hosted in this `ProductionVariant` .

ResolutionTime -> (timestamp)

The date and time when the image path for the model resolved to the `ResolvedImage`

CurrentWeight -> (float)

The weight associated with the variant.

DesiredWeight -> (float)

The requested weight, as specified in the `UpdateEndpointWeightsAndCapacities` request.

CurrentInstanceCount -> (integer)

The number of instances associated with the variant.

DesiredInstanceCount -> (integer)

The number of instances requested in the `UpdateEndpointWeightsAndCapacities` request.

VariantStatus -> (list)

The endpoint variant status which describes the current deployment stage status or operational status.

(structure)

Describes the status of the production variant.

Status -> (string)

The endpoint variant status which describes the current deployment stage status or operational status.

- `Creating` : Creating inference resources for the production variant.
- `Deleting` : Terminating inference resources for the production variant.
- `Updating` : Updating capacity for the production variant.
- `ActivatingTraffic` : Turning on traffic for the production variant.
- `Baking` : Waiting period to monitor the CloudWatch alarms in the automatic rollback configuration.

StatusMessage -> (string)

A message that describes the status of the production variant.

StartTime -> (timestamp)

The start time of the current status change.

CurrentServerlessConfig -> (structure)

The serverless configuration for the endpoint.

MemorySizeInMB -> (integer)

The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.

MaxConcurrency -> (integer)

The maximum number of concurrent invocations your serverless endpoint can process.

ProvisionedConcurrency -> (integer)

The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency` .

### Note

This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) .

DesiredServerlessConfig -> (structure)

The serverless configuration requested for the endpoint update.

MemorySizeInMB -> (integer)

The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.

MaxConcurrency -> (integer)

The maximum number of concurrent invocations your serverless endpoint can process.

ProvisionedConcurrency -> (integer)

The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency` .

### Note

This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) .

ManagedInstanceScaling -> (structure)

Settings that control the range in the number of instances that the endpoint provisions as it scales up or down to accommodate traffic.

Status -> (string)

Indicates whether managed instance scaling is enabled.

MinInstanceCount -> (integer)

The minimum number of instances that the endpoint must retain when it scales down to accommodate a decrease in traffic.

MaxInstanceCount -> (integer)

The maximum number of instances that the endpoint can provision when it scales up to accommodate an increase in traffic.

RoutingConfig -> (structure)

Settings that control how the endpoint routes incoming traffic to the instances that the endpoint hosts.

RoutingStrategy -> (string)

Sets how the endpoint routes incoming traffic:

- `LEAST_OUTSTANDING_REQUESTS` : The endpoint routes requests to the specific instances that have more capacity to process them.
- `RANDOM` : The endpoint routes each request to a randomly chosen instance.