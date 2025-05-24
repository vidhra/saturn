# create-inference-recommendations-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-inference-recommendations-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-inference-recommendations-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-inference-recommendations-job

## Description

Starts a recommendation job. You can create either an instance recommendation or load test job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateInferenceRecommendationsJob)

## Synopsis

```
create-inference-recommendations-job
--job-name <value>
--job-type <value>
--role-arn <value>
--input-config <value>
[--job-description <value>]
[--stopping-conditions <value>]
[--output-config <value>]
[--tags <value>]
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

A name for the recommendation job. The name must be unique within the Amazon Web Services Region and within your Amazon Web Services account. The job name is passed down to the resources created by the recommendation job. The names of resources (such as the model, endpoint configuration, endpoint, and compilation) that are prefixed with the job name are truncated at 40 characters.

`--job-type` (string)

Defines the type of recommendation job. Specify `Default` to initiate an instance recommendation and `Advanced` to initiate a load test. If left unspecified, Amazon SageMaker Inference Recommender will run an instance recommendation (`DEFAULT` ) job.

Possible values:

- `Default`
- `Advanced`

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to perform tasks on your behalf.

`--input-config` (structure)

Provides information about the versioned model package Amazon Resource Name (ARN), the traffic pattern, and endpoint configurations.

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

JSON Syntax:

```
{
  "ModelPackageVersionArn": "string",
  "ModelName": "string",
  "JobDurationInSeconds": integer,
  "TrafficPattern": {
    "TrafficType": "PHASES"|"STAIRS",
    "Phases": [
      {
        "InitialNumberOfUsers": integer,
        "SpawnRate": integer,
        "DurationInSeconds": integer
      }
      ...
    ],
    "Stairs": {
      "DurationInSeconds": integer,
      "NumberOfSteps": integer,
      "UsersPerStep": integer
    }
  },
  "ResourceLimit": {
    "MaxNumberOfTests": integer,
    "MaxParallelOfTests": integer
  },
  "EndpointConfigurations": [
    {
      "InstanceType": "ml.t2.medium"|"ml.t2.large"|"ml.t2.xlarge"|"ml.t2.2xlarge"|"ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.m5d.large"|"ml.m5d.xlarge"|"ml.m5d.2xlarge"|"ml.m5d.4xlarge"|"ml.m5d.12xlarge"|"ml.m5d.24xlarge"|"ml.c4.large"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.c5.large"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.c5d.large"|"ml.c5d.xlarge"|"ml.c5d.2xlarge"|"ml.c5d.4xlarge"|"ml.c5d.9xlarge"|"ml.c5d.18xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.12xlarge"|"ml.r5.24xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.12xlarge"|"ml.r5d.24xlarge"|"ml.inf1.xlarge"|"ml.inf1.2xlarge"|"ml.inf1.6xlarge"|"ml.inf1.24xlarge"|"ml.dl1.24xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.12xlarge"|"ml.g5.16xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.r8g.medium"|"ml.r8g.large"|"ml.r8g.xlarge"|"ml.r8g.2xlarge"|"ml.r8g.4xlarge"|"ml.r8g.8xlarge"|"ml.r8g.12xlarge"|"ml.r8g.16xlarge"|"ml.r8g.24xlarge"|"ml.r8g.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.p4d.24xlarge"|"ml.c7g.large"|"ml.c7g.xlarge"|"ml.c7g.2xlarge"|"ml.c7g.4xlarge"|"ml.c7g.8xlarge"|"ml.c7g.12xlarge"|"ml.c7g.16xlarge"|"ml.m6g.large"|"ml.m6g.xlarge"|"ml.m6g.2xlarge"|"ml.m6g.4xlarge"|"ml.m6g.8xlarge"|"ml.m6g.12xlarge"|"ml.m6g.16xlarge"|"ml.m6gd.large"|"ml.m6gd.xlarge"|"ml.m6gd.2xlarge"|"ml.m6gd.4xlarge"|"ml.m6gd.8xlarge"|"ml.m6gd.12xlarge"|"ml.m6gd.16xlarge"|"ml.c6g.large"|"ml.c6g.xlarge"|"ml.c6g.2xlarge"|"ml.c6g.4xlarge"|"ml.c6g.8xlarge"|"ml.c6g.12xlarge"|"ml.c6g.16xlarge"|"ml.c6gd.large"|"ml.c6gd.xlarge"|"ml.c6gd.2xlarge"|"ml.c6gd.4xlarge"|"ml.c6gd.8xlarge"|"ml.c6gd.12xlarge"|"ml.c6gd.16xlarge"|"ml.c6gn.large"|"ml.c6gn.xlarge"|"ml.c6gn.2xlarge"|"ml.c6gn.4xlarge"|"ml.c6gn.8xlarge"|"ml.c6gn.12xlarge"|"ml.c6gn.16xlarge"|"ml.r6g.large"|"ml.r6g.xlarge"|"ml.r6g.2xlarge"|"ml.r6g.4xlarge"|"ml.r6g.8xlarge"|"ml.r6g.12xlarge"|"ml.r6g.16xlarge"|"ml.r6gd.large"|"ml.r6gd.xlarge"|"ml.r6gd.2xlarge"|"ml.r6gd.4xlarge"|"ml.r6gd.8xlarge"|"ml.r6gd.12xlarge"|"ml.r6gd.16xlarge"|"ml.p4de.24xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.trn2.48xlarge"|"ml.inf2.xlarge"|"ml.inf2.8xlarge"|"ml.inf2.24xlarge"|"ml.inf2.48xlarge"|"ml.p5.48xlarge"|"ml.p5e.48xlarge"|"ml.p5en.48xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge",
      "ServerlessConfig": {
        "MemorySizeInMB": integer,
        "MaxConcurrency": integer,
        "ProvisionedConcurrency": integer
      },
      "InferenceSpecificationName": "string",
      "EnvironmentParameterRanges": {
        "CategoricalParameterRanges": [
          {
            "Name": "string",
            "Value": ["string", ...]
          }
          ...
        ]
      }
    }
    ...
  ],
  "VolumeKmsKeyId": "string",
  "ContainerConfig": {
    "Domain": "string",
    "Task": "string",
    "Framework": "string",
    "FrameworkVersion": "string",
    "PayloadConfig": {
      "SamplePayloadUrl": "string",
      "SupportedContentTypes": ["string", ...]
    },
    "NearestModelName": "string",
    "SupportedInstanceTypes": ["string", ...],
    "SupportedEndpointType": "RealTime"|"Serverless",
    "DataInputConfig": "string",
    "SupportedResponseMIMETypes": ["string", ...]
  },
  "Endpoints": [
    {
      "EndpointName": "string"
    }
    ...
  ],
  "VpcConfig": {
    "SecurityGroupIds": ["string", ...],
    "Subnets": ["string", ...]
  }
}
```

`--job-description` (string)

Description of the recommendation job.

`--stopping-conditions` (structure)

A set of conditions for stopping a recommendation job. If any of the conditions are met, the job is automatically stopped.

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

Shorthand Syntax:

```
MaxInvocations=integer,ModelLatencyThresholds=[{Percentile=string,ValueInMilliseconds=integer},{Percentile=string,ValueInMilliseconds=integer}],FlatInvocations=string
```

JSON Syntax:

```
{
  "MaxInvocations": integer,
  "ModelLatencyThresholds": [
    {
      "Percentile": "string",
      "ValueInMilliseconds": integer
    }
    ...
  ],
  "FlatInvocations": "Continue"|"Stop"
}
```

`--output-config` (structure)

Provides information about the output artifacts and the KMS key to use for Amazon S3 server-side encryption.

KmsKeyId -> (string)

The Amazon Resource Name (ARN) of a Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt your output artifacts with Amazon S3 server-side encryption. The SageMaker execution role must have `kms:GenerateDataKey` permission.

The `KmsKeyId` can be any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:<region>:<account>:key/<key-id-12ab-34cd-56ef-1234567890ab>"`
- // KMS Key Alias  `"alias/ExampleAlias"`
- // Amazon Resource Name (ARN) of a KMS Key Alias  `"arn:aws:kms:<region>:<account>:alias/<ExampleAlias>"`

For more information about key identifiers, see [Key identifiers (KeyID)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id) in the Amazon Web Services Key Management Service (Amazon Web Services KMS) documentation.

CompiledOutputConfig -> (structure)

Provides information about the output configuration for the compiled model.

S3OutputUri -> (string)

Identifies the Amazon S3 bucket where you want SageMaker to store the compiled model artifacts.

Shorthand Syntax:

```
KmsKeyId=string,CompiledOutputConfig={S3OutputUri=string}
```

JSON Syntax:

```
{
  "KmsKeyId": "string",
  "CompiledOutputConfig": {
    "S3OutputUri": "string"
  }
}
```

`--tags` (list)

The metadata that you apply to Amazon Web Services resources to help you categorize and organize them. Each tag consists of a key and a value, both of which you define. For more information, see [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the Amazon Web Services General Reference.

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

JobArn -> (string)

The Amazon Resource Name (ARN) of the recommendation job.