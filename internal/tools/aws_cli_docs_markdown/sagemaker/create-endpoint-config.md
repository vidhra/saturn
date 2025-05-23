# create-endpoint-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-endpoint-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-endpoint-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-endpoint-config

## Description

Creates an endpoint configuration that SageMaker hosting services uses to deploy models. In the configuration, you identify one or more models, created using the `CreateModel` API, to deploy and the resources that you want SageMaker to provision. Then you call the [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) API.

### Note

Use this API if you want to use SageMaker hosting services to deploy models into production.

In the request, you define a `ProductionVariant` , for each model that you want to deploy. Each `ProductionVariant` parameter also describes the resources that you want SageMaker to provision. This includes the number and type of ML compute instances to deploy.

If you are hosting multiple models, you also assign a `VariantWeight` to specify how much traffic you want to allocate to each model. For example, suppose that you want to host two models, A and B, and you assign traffic weight 2 for model A and 1 for model B. SageMaker distributes two-thirds of the traffic to Model A, and one-third to model B.

### Note

When you call [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) , a load call is made to DynamoDB to verify that your endpoint configuration exists. When you read data from a DynamoDB table supporting ` `Eventually Consistent Reads` [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency).html`__ , the response might not reflect the results of a recently completed write operation. The response might include some stale data. If the dependent entities are not yet in DynamoDB, this causes a validation error. If you repeat your read request after a short time, the response should return the latest data. So retry logic is recommended to handle these possible issues. We also recommend that customers call [DescribeEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpointConfig.html) before calling [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) to minimize the potential impact of a DynamoDB eventually consistent read.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateEndpointConfig)

## Synopsis

```
create-endpoint-config
--endpoint-config-name <value>
--production-variants <value>
[--data-capture-config <value>]
[--tags <value>]
[--kms-key-id <value>]
[--async-inference-config <value>]
[--explainer-config <value>]
[--shadow-production-variants <value>]
[--execution-role-arn <value>]
[--vpc-config <value>]
[--enable-network-isolation | --no-enable-network-isolation]
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

`--endpoint-config-name` (string)

The name of the endpoint configuration. You specify this name in a [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) request.

`--production-variants` (list)

An array of `ProductionVariant` objects, one for each model that you want to host at this endpoint.

(structure)

Identifies a model that you want to host and the resources chosen to deploy for hosting it. If you are deploying multiple models, tell SageMaker how to distribute traffic among the models by specifying variant weights. For more information on production variants, check [Production variants](https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html) .

VariantName -> (string)

The name of the production variant.

ModelName -> (string)

The name of the model that you want to host. This is the name that you specified when creating the model.

InitialInstanceCount -> (integer)

Number of instances to launch initially.

InstanceType -> (string)

The ML compute instance type.

InitialVariantWeight -> (float)

Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. The traffic to a production variant is determined by the ratio of the `VariantWeight` to the sum of all `VariantWeight` values across all ProductionVariants. If unspecified, it defaults to 1.0.

AcceleratorType -> (string)

This parameter is no longer supported. Elastic Inference (EI) is no longer available.

This parameter was used to specify the size of the EI instance to use for the production variant.

CoreDumpConfig -> (structure)

Specifies configuration for a core dump from the model container when the process crashes.

DestinationS3Uri -> (string)

The Amazon S3 bucket to send the core dump to.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that SageMaker uses to encrypt the core dump data at rest using Amazon S3 server-side encryption. The `KmsKeyId` can be any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
- // KMS Key Alias  `"alias/ExampleAlias"`
- // Amazon Resource Name (ARN) of a KMS Key Alias  `"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"`

If you use a KMS key ID or an alias of your KMS key, the SageMaker execution role must include permissions to call `kms:Encrypt` . If you donât provide a KMS key ID, SageMaker uses the default KMS key for Amazon S3 for your roleâs account. SageMaker uses server-side encryption with KMS-managed keys for `OutputDataConfig` . If you use a bucket policy with an `s3:PutObject` permission that only allows objects with server-side encryption, set the condition key of `s3:x-amz-server-side-encryption` to `"aws:kms"` . For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide.*

The KMS key policy must grant permission to the IAM role that you specify in your `CreateEndpoint` and `UpdateEndpoint` requests. For more information, see [Using Key Policies in Amazon Web Services KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *Amazon Web Services Key Management Service Developer Guide* .

ServerlessConfig -> (structure)

The serverless configuration for an endpoint. Specifies a serverless endpoint configuration instead of an instance-based endpoint configuration.

MemorySizeInMB -> (integer)

The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.

MaxConcurrency -> (integer)

The maximum number of concurrent invocations your serverless endpoint can process.

ProvisionedConcurrency -> (integer)

The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency` .

### Note

This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) .

VolumeSizeInGB -> (integer)

The size, in GB, of the ML storage volume attached to individual inference instance associated with the production variant. Currently only Amazon EBS gp2 storage volumes are supported.

ModelDataDownloadTimeoutInSeconds -> (integer)

The timeout value, in seconds, to download and extract the model that you want to host from Amazon S3 to the individual inference instance associated with this production variant.

ContainerStartupHealthCheckTimeoutInSeconds -> (integer)

The timeout value, in seconds, for your inference container to pass health check by SageMaker Hosting. For more information about health check, see [How Your Container Should Respond to Health Check (Ping) Requests](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-algo-ping-requests) .

EnableSSMAccess -> (boolean)

You can use this parameter to turn on native Amazon Web Services Systems Manager (SSM) access for a production variant behind an endpoint. By default, SSM access is disabled for all production variants behind an endpoint. You can turn on or turn off SSM access for a production variant behind an existing endpoint by creating a new endpoint configuration and calling `UpdateEndpoint` .

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

InferenceAmiVersion -> (string)

Specifies an option from a collection of preconfigured Amazon Machine Image (AMI) images. Each image is configured by Amazon Web Services with a set of software and driver versions. Amazon Web Services optimizes these configurations for different machine learning workloads.

By selecting an AMI version, you can ensure that your inference environment is compatible with specific software requirements, such as CUDA driver versions, Linux kernel versions, or Amazon Web Services Neuron driver versions.

The AMI version names, and their configurations, are the following:

al2-ami-sagemaker-inference-gpu-2

- Accelerator: GPU
- NVIDIA driver version: 535
- CUDA version: 12.2

al2-ami-sagemaker-inference-gpu-2-1
- Accelerator: GPU
- NVIDIA driver version: 535
- CUDA version: 12.2
- NVIDIA Container Toolkit with disabled CUDA-compat mounting

al2-ami-sagemaker-inference-gpu-3-1
- Accelerator: GPU
- NVIDIA driver version: 550
- CUDA version: 12.4
- NVIDIA Container Toolkit with disabled CUDA-compat mounting

al2-ami-sagemaker-inference-neuron-2
- Accelerator: Inferentia2 and Trainium
- Neuron driver version: 2.19

Shorthand Syntax:

```
VariantName=string,ModelName=string,InitialInstanceCount=integer,InstanceType=string,InitialVariantWeight=float,AcceleratorType=string,CoreDumpConfig={DestinationS3Uri=string,KmsKeyId=string},ServerlessConfig={MemorySizeInMB=integer,MaxConcurrency=integer,ProvisionedConcurrency=integer},VolumeSizeInGB=integer,ModelDataDownloadTimeoutInSeconds=integer,ContainerStartupHealthCheckTimeoutInSeconds=integer,EnableSSMAccess=boolean,ManagedInstanceScaling={Status=string,MinInstanceCount=integer,MaxInstanceCount=integer},RoutingConfig={RoutingStrategy=string},InferenceAmiVersion=string ...
```

JSON Syntax:

```
[
  {
    "VariantName": "string",
    "ModelName": "string",
    "InitialInstanceCount": integer,
    "InstanceType": "ml.t2.medium"|"ml.t2.large"|"ml.t2.xlarge"|"ml.t2.2xlarge"|"ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.m5d.large"|"ml.m5d.xlarge"|"ml.m5d.2xlarge"|"ml.m5d.4xlarge"|"ml.m5d.12xlarge"|"ml.m5d.24xlarge"|"ml.c4.large"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.c5.large"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.c5d.large"|"ml.c5d.xlarge"|"ml.c5d.2xlarge"|"ml.c5d.4xlarge"|"ml.c5d.9xlarge"|"ml.c5d.18xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.12xlarge"|"ml.r5.24xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.12xlarge"|"ml.r5d.24xlarge"|"ml.inf1.xlarge"|"ml.inf1.2xlarge"|"ml.inf1.6xlarge"|"ml.inf1.24xlarge"|"ml.dl1.24xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.12xlarge"|"ml.g5.16xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.r8g.medium"|"ml.r8g.large"|"ml.r8g.xlarge"|"ml.r8g.2xlarge"|"ml.r8g.4xlarge"|"ml.r8g.8xlarge"|"ml.r8g.12xlarge"|"ml.r8g.16xlarge"|"ml.r8g.24xlarge"|"ml.r8g.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.p4d.24xlarge"|"ml.c7g.large"|"ml.c7g.xlarge"|"ml.c7g.2xlarge"|"ml.c7g.4xlarge"|"ml.c7g.8xlarge"|"ml.c7g.12xlarge"|"ml.c7g.16xlarge"|"ml.m6g.large"|"ml.m6g.xlarge"|"ml.m6g.2xlarge"|"ml.m6g.4xlarge"|"ml.m6g.8xlarge"|"ml.m6g.12xlarge"|"ml.m6g.16xlarge"|"ml.m6gd.large"|"ml.m6gd.xlarge"|"ml.m6gd.2xlarge"|"ml.m6gd.4xlarge"|"ml.m6gd.8xlarge"|"ml.m6gd.12xlarge"|"ml.m6gd.16xlarge"|"ml.c6g.large"|"ml.c6g.xlarge"|"ml.c6g.2xlarge"|"ml.c6g.4xlarge"|"ml.c6g.8xlarge"|"ml.c6g.12xlarge"|"ml.c6g.16xlarge"|"ml.c6gd.large"|"ml.c6gd.xlarge"|"ml.c6gd.2xlarge"|"ml.c6gd.4xlarge"|"ml.c6gd.8xlarge"|"ml.c6gd.12xlarge"|"ml.c6gd.16xlarge"|"ml.c6gn.large"|"ml.c6gn.xlarge"|"ml.c6gn.2xlarge"|"ml.c6gn.4xlarge"|"ml.c6gn.8xlarge"|"ml.c6gn.12xlarge"|"ml.c6gn.16xlarge"|"ml.r6g.large"|"ml.r6g.xlarge"|"ml.r6g.2xlarge"|"ml.r6g.4xlarge"|"ml.r6g.8xlarge"|"ml.r6g.12xlarge"|"ml.r6g.16xlarge"|"ml.r6gd.large"|"ml.r6gd.xlarge"|"ml.r6gd.2xlarge"|"ml.r6gd.4xlarge"|"ml.r6gd.8xlarge"|"ml.r6gd.12xlarge"|"ml.r6gd.16xlarge"|"ml.p4de.24xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.trn2.48xlarge"|"ml.inf2.xlarge"|"ml.inf2.8xlarge"|"ml.inf2.24xlarge"|"ml.inf2.48xlarge"|"ml.p5.48xlarge"|"ml.p5e.48xlarge"|"ml.p5en.48xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge",
    "InitialVariantWeight": float,
    "AcceleratorType": "ml.eia1.medium"|"ml.eia1.large"|"ml.eia1.xlarge"|"ml.eia2.medium"|"ml.eia2.large"|"ml.eia2.xlarge",
    "CoreDumpConfig": {
      "DestinationS3Uri": "string",
      "KmsKeyId": "string"
    },
    "ServerlessConfig": {
      "MemorySizeInMB": integer,
      "MaxConcurrency": integer,
      "ProvisionedConcurrency": integer
    },
    "VolumeSizeInGB": integer,
    "ModelDataDownloadTimeoutInSeconds": integer,
    "ContainerStartupHealthCheckTimeoutInSeconds": integer,
    "EnableSSMAccess": true|false,
    "ManagedInstanceScaling": {
      "Status": "ENABLED"|"DISABLED",
      "MinInstanceCount": integer,
      "MaxInstanceCount": integer
    },
    "RoutingConfig": {
      "RoutingStrategy": "LEAST_OUTSTANDING_REQUESTS"|"RANDOM"
    },
    "InferenceAmiVersion": "al2-ami-sagemaker-inference-gpu-2"|"al2-ami-sagemaker-inference-gpu-2-1"|"al2-ami-sagemaker-inference-gpu-3-1"|"al2-ami-sagemaker-inference-neuron-2"
  }
  ...
]
```

`--data-capture-config` (structure)

Configuration to control how SageMaker AI captures inference data.

EnableCapture -> (boolean)

Whether data capture should be enabled or disabled (defaults to enabled).

InitialSamplingPercentage -> (integer)

The percentage of requests SageMaker AI will capture. A lower value is recommended for Endpoints with high traffic.

DestinationS3Uri -> (string)

The Amazon S3 location used to capture the data.

KmsKeyId -> (string)

The Amazon Resource Name (ARN) of an Key Management Service key that SageMaker AI uses to encrypt the captured data at rest using Amazon S3 server-side encryption.

The KmsKeyId can be any of the following formats:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`

CaptureOptions -> (list)

Specifies data Model Monitor will capture. You can configure whether to collect only input, only output, or both

(structure)

Specifies data Model Monitor will capture.

CaptureMode -> (string)

Specify the boundary of data to capture.

CaptureContentTypeHeader -> (structure)

Configuration specifying how to treat different headers. If no headers are specified SageMaker AI will by default base64 encode when capturing the data.

CsvContentTypes -> (list)

The list of all content type headers that Amazon SageMaker AI will treat as CSV and capture accordingly.

(string)

JsonContentTypes -> (list)

The list of all content type headers that SageMaker AI will treat as JSON and capture accordingly.

(string)

Shorthand Syntax:

```
EnableCapture=boolean,InitialSamplingPercentage=integer,DestinationS3Uri=string,KmsKeyId=string,CaptureOptions=[{CaptureMode=string},{CaptureMode=string}],CaptureContentTypeHeader={CsvContentTypes=[string,string],JsonContentTypes=[string,string]}
```

JSON Syntax:

```
{
  "EnableCapture": true|false,
  "InitialSamplingPercentage": integer,
  "DestinationS3Uri": "string",
  "KmsKeyId": "string",
  "CaptureOptions": [
    {
      "CaptureMode": "Input"|"Output"|"InputAndOutput"
    }
    ...
  ],
  "CaptureContentTypeHeader": {
    "CsvContentTypes": ["string", ...],
    "JsonContentTypes": ["string", ...]
  }
}
```

`--tags` (list)

An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--kms-key-id` (string)

The Amazon Resource Name (ARN) of a Amazon Web Services Key Management Service key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.

The KmsKeyId can be any of the following formats:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`

The KMS key policy must grant permission to the IAM role that you specify in your `CreateEndpoint` , `UpdateEndpoint` requests. For more information, refer to the Amazon Web Services Key Management Service section`Using Key Policies in Amazon Web Services KMS <[https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html)>`__

### Note

Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You canât request a `KmsKeyId` when using an instance type with local storage. If any of the models that you specify in the `ProductionVariants` parameter use nitro-based instances with local storage, do not specify a value for the `KmsKeyId` parameter. If you specify a value for `KmsKeyId` when using any nitro-based instances with local storage, the call to `CreateEndpointConfig` fails.

For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes) .

For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) .

`--async-inference-config` (structure)

Specifies configuration for how an endpoint performs asynchronous inference. This is a required field in order for your Endpoint to be invoked using [InvokeEndpointAsync](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpointAsync.html) .

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

JSON Syntax:

```
{
  "ClientConfig": {
    "MaxConcurrentInvocationsPerInstance": integer
  },
  "OutputConfig": {
    "KmsKeyId": "string",
    "S3OutputPath": "string",
    "NotificationConfig": {
      "SuccessTopic": "string",
      "ErrorTopic": "string",
      "IncludeInferenceResponseIn": ["SUCCESS_NOTIFICATION_TOPIC"|"ERROR_NOTIFICATION_TOPIC", ...]
    },
    "S3FailurePath": "string"
  }
}
```

`--explainer-config` (structure)

A member of `CreateEndpointConfig` that enables explainers.

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

Specifies the language of the text features in [`ISO 639-1 < https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-endpoint-config.html#id1) or [ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3) code of a supported language.

### Note

For a mix of multiple languages, use code `'xx'` .

Granularity -> (string)

The unit of granularity for the analysis of text features. For example, if the unit is `'token'` , then each token (like a word in English) of the text is treated as a feature. SHAP values are computed for each unit/feature.

JSON Syntax:

```
{
  "ClarifyExplainerConfig": {
    "EnableExplanations": "string",
    "InferenceConfig": {
      "FeaturesAttribute": "string",
      "ContentTemplate": "string",
      "MaxRecordCount": integer,
      "MaxPayloadInMB": integer,
      "ProbabilityIndex": integer,
      "LabelIndex": integer,
      "ProbabilityAttribute": "string",
      "LabelAttribute": "string",
      "LabelHeaders": ["string", ...],
      "FeatureHeaders": ["string", ...],
      "FeatureTypes": ["numerical"|"categorical"|"text", ...]
    },
    "ShapConfig": {
      "ShapBaselineConfig": {
        "MimeType": "string",
        "ShapBaseline": "string",
        "ShapBaselineUri": "string"
      },
      "NumberOfSamples": integer,
      "UseLogit": true|false,
      "Seed": integer,
      "TextConfig": {
        "Language": "af"|"sq"|"ar"|"hy"|"eu"|"bn"|"bg"|"ca"|"zh"|"hr"|"cs"|"da"|"nl"|"en"|"et"|"fi"|"fr"|"de"|"el"|"gu"|"he"|"hi"|"hu"|"is"|"id"|"ga"|"it"|"kn"|"ky"|"lv"|"lt"|"lb"|"mk"|"ml"|"mr"|"ne"|"nb"|"fa"|"pl"|"pt"|"ro"|"ru"|"sa"|"sr"|"tn"|"si"|"sk"|"sl"|"es"|"sv"|"tl"|"ta"|"tt"|"te"|"tr"|"uk"|"ur"|"yo"|"lij"|"xx",
        "Granularity": "token"|"sentence"|"paragraph"
      }
    }
  }
}
```

`--shadow-production-variants` (list)

An array of `ProductionVariant` objects, one for each model that you want to host at this endpoint in shadow mode with production traffic replicated from the model specified on `ProductionVariants` . If you use this field, you can only specify one variant for `ProductionVariants` and one variant for `ShadowProductionVariants` .

(structure)

Identifies a model that you want to host and the resources chosen to deploy for hosting it. If you are deploying multiple models, tell SageMaker how to distribute traffic among the models by specifying variant weights. For more information on production variants, check [Production variants](https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html) .

VariantName -> (string)

The name of the production variant.

ModelName -> (string)

The name of the model that you want to host. This is the name that you specified when creating the model.

InitialInstanceCount -> (integer)

Number of instances to launch initially.

InstanceType -> (string)

The ML compute instance type.

InitialVariantWeight -> (float)

Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. The traffic to a production variant is determined by the ratio of the `VariantWeight` to the sum of all `VariantWeight` values across all ProductionVariants. If unspecified, it defaults to 1.0.

AcceleratorType -> (string)

This parameter is no longer supported. Elastic Inference (EI) is no longer available.

This parameter was used to specify the size of the EI instance to use for the production variant.

CoreDumpConfig -> (structure)

Specifies configuration for a core dump from the model container when the process crashes.

DestinationS3Uri -> (string)

The Amazon S3 bucket to send the core dump to.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that SageMaker uses to encrypt the core dump data at rest using Amazon S3 server-side encryption. The `KmsKeyId` can be any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
- // KMS Key Alias  `"alias/ExampleAlias"`
- // Amazon Resource Name (ARN) of a KMS Key Alias  `"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"`

If you use a KMS key ID or an alias of your KMS key, the SageMaker execution role must include permissions to call `kms:Encrypt` . If you donât provide a KMS key ID, SageMaker uses the default KMS key for Amazon S3 for your roleâs account. SageMaker uses server-side encryption with KMS-managed keys for `OutputDataConfig` . If you use a bucket policy with an `s3:PutObject` permission that only allows objects with server-side encryption, set the condition key of `s3:x-amz-server-side-encryption` to `"aws:kms"` . For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide.*

The KMS key policy must grant permission to the IAM role that you specify in your `CreateEndpoint` and `UpdateEndpoint` requests. For more information, see [Using Key Policies in Amazon Web Services KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *Amazon Web Services Key Management Service Developer Guide* .

ServerlessConfig -> (structure)

The serverless configuration for an endpoint. Specifies a serverless endpoint configuration instead of an instance-based endpoint configuration.

MemorySizeInMB -> (integer)

The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.

MaxConcurrency -> (integer)

The maximum number of concurrent invocations your serverless endpoint can process.

ProvisionedConcurrency -> (integer)

The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency` .

### Note

This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) .

VolumeSizeInGB -> (integer)

The size, in GB, of the ML storage volume attached to individual inference instance associated with the production variant. Currently only Amazon EBS gp2 storage volumes are supported.

ModelDataDownloadTimeoutInSeconds -> (integer)

The timeout value, in seconds, to download and extract the model that you want to host from Amazon S3 to the individual inference instance associated with this production variant.

ContainerStartupHealthCheckTimeoutInSeconds -> (integer)

The timeout value, in seconds, for your inference container to pass health check by SageMaker Hosting. For more information about health check, see [How Your Container Should Respond to Health Check (Ping) Requests](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-algo-ping-requests) .

EnableSSMAccess -> (boolean)

You can use this parameter to turn on native Amazon Web Services Systems Manager (SSM) access for a production variant behind an endpoint. By default, SSM access is disabled for all production variants behind an endpoint. You can turn on or turn off SSM access for a production variant behind an existing endpoint by creating a new endpoint configuration and calling `UpdateEndpoint` .

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

InferenceAmiVersion -> (string)

Specifies an option from a collection of preconfigured Amazon Machine Image (AMI) images. Each image is configured by Amazon Web Services with a set of software and driver versions. Amazon Web Services optimizes these configurations for different machine learning workloads.

By selecting an AMI version, you can ensure that your inference environment is compatible with specific software requirements, such as CUDA driver versions, Linux kernel versions, or Amazon Web Services Neuron driver versions.

The AMI version names, and their configurations, are the following:

al2-ami-sagemaker-inference-gpu-2

- Accelerator: GPU
- NVIDIA driver version: 535
- CUDA version: 12.2

al2-ami-sagemaker-inference-gpu-2-1
- Accelerator: GPU
- NVIDIA driver version: 535
- CUDA version: 12.2
- NVIDIA Container Toolkit with disabled CUDA-compat mounting

al2-ami-sagemaker-inference-gpu-3-1
- Accelerator: GPU
- NVIDIA driver version: 550
- CUDA version: 12.4
- NVIDIA Container Toolkit with disabled CUDA-compat mounting

al2-ami-sagemaker-inference-neuron-2
- Accelerator: Inferentia2 and Trainium
- Neuron driver version: 2.19

Shorthand Syntax:

```
VariantName=string,ModelName=string,InitialInstanceCount=integer,InstanceType=string,InitialVariantWeight=float,AcceleratorType=string,CoreDumpConfig={DestinationS3Uri=string,KmsKeyId=string},ServerlessConfig={MemorySizeInMB=integer,MaxConcurrency=integer,ProvisionedConcurrency=integer},VolumeSizeInGB=integer,ModelDataDownloadTimeoutInSeconds=integer,ContainerStartupHealthCheckTimeoutInSeconds=integer,EnableSSMAccess=boolean,ManagedInstanceScaling={Status=string,MinInstanceCount=integer,MaxInstanceCount=integer},RoutingConfig={RoutingStrategy=string},InferenceAmiVersion=string ...
```

JSON Syntax:

```
[
  {
    "VariantName": "string",
    "ModelName": "string",
    "InitialInstanceCount": integer,
    "InstanceType": "ml.t2.medium"|"ml.t2.large"|"ml.t2.xlarge"|"ml.t2.2xlarge"|"ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.m5d.large"|"ml.m5d.xlarge"|"ml.m5d.2xlarge"|"ml.m5d.4xlarge"|"ml.m5d.12xlarge"|"ml.m5d.24xlarge"|"ml.c4.large"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.c5.large"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.c5d.large"|"ml.c5d.xlarge"|"ml.c5d.2xlarge"|"ml.c5d.4xlarge"|"ml.c5d.9xlarge"|"ml.c5d.18xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.12xlarge"|"ml.r5.24xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.12xlarge"|"ml.r5d.24xlarge"|"ml.inf1.xlarge"|"ml.inf1.2xlarge"|"ml.inf1.6xlarge"|"ml.inf1.24xlarge"|"ml.dl1.24xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.12xlarge"|"ml.g5.16xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.r8g.medium"|"ml.r8g.large"|"ml.r8g.xlarge"|"ml.r8g.2xlarge"|"ml.r8g.4xlarge"|"ml.r8g.8xlarge"|"ml.r8g.12xlarge"|"ml.r8g.16xlarge"|"ml.r8g.24xlarge"|"ml.r8g.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.p4d.24xlarge"|"ml.c7g.large"|"ml.c7g.xlarge"|"ml.c7g.2xlarge"|"ml.c7g.4xlarge"|"ml.c7g.8xlarge"|"ml.c7g.12xlarge"|"ml.c7g.16xlarge"|"ml.m6g.large"|"ml.m6g.xlarge"|"ml.m6g.2xlarge"|"ml.m6g.4xlarge"|"ml.m6g.8xlarge"|"ml.m6g.12xlarge"|"ml.m6g.16xlarge"|"ml.m6gd.large"|"ml.m6gd.xlarge"|"ml.m6gd.2xlarge"|"ml.m6gd.4xlarge"|"ml.m6gd.8xlarge"|"ml.m6gd.12xlarge"|"ml.m6gd.16xlarge"|"ml.c6g.large"|"ml.c6g.xlarge"|"ml.c6g.2xlarge"|"ml.c6g.4xlarge"|"ml.c6g.8xlarge"|"ml.c6g.12xlarge"|"ml.c6g.16xlarge"|"ml.c6gd.large"|"ml.c6gd.xlarge"|"ml.c6gd.2xlarge"|"ml.c6gd.4xlarge"|"ml.c6gd.8xlarge"|"ml.c6gd.12xlarge"|"ml.c6gd.16xlarge"|"ml.c6gn.large"|"ml.c6gn.xlarge"|"ml.c6gn.2xlarge"|"ml.c6gn.4xlarge"|"ml.c6gn.8xlarge"|"ml.c6gn.12xlarge"|"ml.c6gn.16xlarge"|"ml.r6g.large"|"ml.r6g.xlarge"|"ml.r6g.2xlarge"|"ml.r6g.4xlarge"|"ml.r6g.8xlarge"|"ml.r6g.12xlarge"|"ml.r6g.16xlarge"|"ml.r6gd.large"|"ml.r6gd.xlarge"|"ml.r6gd.2xlarge"|"ml.r6gd.4xlarge"|"ml.r6gd.8xlarge"|"ml.r6gd.12xlarge"|"ml.r6gd.16xlarge"|"ml.p4de.24xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.trn2.48xlarge"|"ml.inf2.xlarge"|"ml.inf2.8xlarge"|"ml.inf2.24xlarge"|"ml.inf2.48xlarge"|"ml.p5.48xlarge"|"ml.p5e.48xlarge"|"ml.p5en.48xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge",
    "InitialVariantWeight": float,
    "AcceleratorType": "ml.eia1.medium"|"ml.eia1.large"|"ml.eia1.xlarge"|"ml.eia2.medium"|"ml.eia2.large"|"ml.eia2.xlarge",
    "CoreDumpConfig": {
      "DestinationS3Uri": "string",
      "KmsKeyId": "string"
    },
    "ServerlessConfig": {
      "MemorySizeInMB": integer,
      "MaxConcurrency": integer,
      "ProvisionedConcurrency": integer
    },
    "VolumeSizeInGB": integer,
    "ModelDataDownloadTimeoutInSeconds": integer,
    "ContainerStartupHealthCheckTimeoutInSeconds": integer,
    "EnableSSMAccess": true|false,
    "ManagedInstanceScaling": {
      "Status": "ENABLED"|"DISABLED",
      "MinInstanceCount": integer,
      "MaxInstanceCount": integer
    },
    "RoutingConfig": {
      "RoutingStrategy": "LEAST_OUTSTANDING_REQUESTS"|"RANDOM"
    },
    "InferenceAmiVersion": "al2-ami-sagemaker-inference-gpu-2"|"al2-ami-sagemaker-inference-gpu-2-1"|"al2-ami-sagemaker-inference-gpu-3-1"|"al2-ami-sagemaker-inference-neuron-2"
  }
  ...
]
```

`--execution-role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform actions on your behalf. For more information, see [SageMaker AI Roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html) .

### Note

To be able to pass this role to Amazon SageMaker AI, the caller of this action must have the `iam:PassRole` permission.

`--vpc-config` (structure)

Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

Shorthand Syntax:

```
SecurityGroupIds=string,string,Subnets=string,string
```

JSON Syntax:

```
{
  "SecurityGroupIds": ["string", ...],
  "Subnets": ["string", ...]
}
```

`--enable-network-isolation` | `--no-enable-network-isolation` (boolean)

Sets whether all model containers deployed to the endpoint are isolated. If they are, no inbound or outbound network calls can be made to or from the model containers.

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

EndpointConfigArn -> (string)

The Amazon Resource Name (ARN) of the endpoint configuration.