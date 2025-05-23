# create-compilation-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-compilation-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-compilation-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-compilation-job

## Description

Starts a model compilation job. After the model has been compiled, Amazon SageMaker AI saves the resulting model artifacts to an Amazon Simple Storage Service (Amazon S3) bucket that you specify.

If you choose to host your model using Amazon SageMaker AI hosting services, you can use the resulting model artifacts as part of the model. You can also use the artifacts with Amazon Web Services IoT Greengrass. In that case, deploy them as an ML resource.

In the request body, you provide the following:

- A name for the compilation job
- Information about the input model artifacts
- The output location for the compiled model and the device (target) that the model runs on
- The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker AI assumes to perform the model compilation job.

You can also provide a `Tag` to track the model compilation jobâs resource use and costs. The response body contains the `CompilationJobArn` for the compiled job.

To stop a model compilation job, use [StopCompilationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopCompilationJob.html) . To get information about a particular model compilation job, use [DescribeCompilationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeCompilationJob.html) . To get information about multiple model compilation jobs, use [ListCompilationJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListCompilationJobs.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateCompilationJob)

## Synopsis

```
create-compilation-job
--compilation-job-name <value>
--role-arn <value>
[--model-package-version-arn <value>]
[--input-config <value>]
--output-config <value>
[--vpc-config <value>]
--stopping-condition <value>
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

`--compilation-job-name` (string)

A name for the model compilation job. The name must be unique within the Amazon Web Services Region and within your Amazon Web Services account.

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker AI to perform tasks on your behalf.

During model compilation, Amazon SageMaker AI needs your permission to:

- Read input data from an S3 bucket
- Write model artifacts to an S3 bucket
- Write logs to Amazon CloudWatch Logs
- Publish metrics to Amazon CloudWatch

You grant permissions for all of these tasks to an IAM role. To pass this role to Amazon SageMaker AI, the caller of this API must have the `iam:PassRole` permission. For more information, see [Amazon SageMaker AI Roles.](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html)

`--model-package-version-arn` (string)

The Amazon Resource Name (ARN) of a versioned model package. Provide either a `ModelPackageVersionArn` or an `InputConfig` object in the request syntax. The presence of both objects in the `CreateCompilationJob` request will return an exception.

`--input-config` (structure)

Provides information about the location of input model artifacts, the name and shape of the expected data inputs, and the framework in which the model was trained.

S3Uri -> (string)

The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).

DataInputConfig -> (string)

Specifies the name and shape of the expected data inputs for your trained model with a JSON dictionary form. The data inputs are `Framework` specific.

- `TensorFlow` : You must specify the name and shape (NHWC format) of the expected data inputs using a dictionary format for your trained model. The dictionary formats required for the console and CLI are different.
- Examples for one input:
- If using the console, `{"input":[1,1024,1024,3]}`
- If using the CLI, `{\"input\":[1,1024,1024,3]}`
- Examples for two inputs:
- If using the console, `{"data1": [1,28,28,1], "data2":[1,28,28,1]}`
- If using the CLI, `{\"data1\": [1,28,28,1], \"data2\":[1,28,28,1]}`
- `KERAS` : You must specify the name and shape (NCHW format) of expected data inputs using a dictionary format for your trained model. Note that while Keras model artifacts should be uploaded in NHWC (channel-last) format, `DataInputConfig` should be specified in NCHW (channel-first) format. The dictionary formats required for the console and CLI are different.
- Examples for one input:
- If using the console, `{"input_1":[1,3,224,224]}`
- If using the CLI, `{\"input_1\":[1,3,224,224]}`
- Examples for two inputs:
- If using the console, `{"input_1": [1,3,224,224], "input_2":[1,3,224,224]}`
- If using the CLI, `{\"input_1\": [1,3,224,224], \"input_2\":[1,3,224,224]}`
- `MXNET/ONNX/DARKNET` : You must specify the name and shape (NCHW format) of the expected data inputs in order using a dictionary format for your trained model. The dictionary formats required for the console and CLI are different.
- Examples for one input:
- If using the console, `{"data":[1,3,1024,1024]}`
- If using the CLI, `{\"data\":[1,3,1024,1024]}`
- Examples for two inputs:
- If using the console, `{"var1": [1,1,28,28], "var2":[1,1,28,28]}`
- If using the CLI, `{\"var1\": [1,1,28,28], \"var2\":[1,1,28,28]}`
- `PyTorch` : You can either specify the name and shape (NCHW format) of expected data inputs in order using a dictionary format for your trained model or you can specify the shape only using a list format. The dictionary formats required for the console and CLI are different. The list formats for the console and CLI are the same.
- Examples for one input in dictionary format:
- If using the console, `{"input0":[1,3,224,224]}`
- If using the CLI, `{\"input0\":[1,3,224,224]}`
- Example for one input in list format: `[[1,3,224,224]]`
- Examples for two inputs in dictionary format:
- If using the console, `{"input0":[1,3,224,224], "input1":[1,3,224,224]}`
- If using the CLI, `{\"input0\":[1,3,224,224], \"input1\":[1,3,224,224]}`
- Example for two inputs in list format: `[[1,3,224,224], [1,3,224,224]]`
- `XGBOOST` : input data name and shape are not needed.

`DataInputConfig` supports the following parameters for `CoreML` `TargetDevice` (ML Model format):

- `shape` : Input shape, for example `{"input_1": {"shape": [1,224,224,3]}}` . In addition to static input shapes, CoreML converter supports Flexible input shapes:
- Range Dimension. You can use the Range Dimension feature if you know the input shape will be within some specific interval in that dimension, for example: `{"input_1": {"shape": ["1..10", 224, 224, 3]}}`
- Enumerated shapes. Sometimes, the models are trained to work only on a select set of inputs. You can enumerate all supported input shapes, for example: `{"input_1": {"shape": [[1, 224, 224, 3], [1, 160, 160, 3]]}}`
- `default_shape` : Default input shape. You can set a default shape during conversion for both Range Dimension and Enumerated Shapes. For example `{"input_1": {"shape": ["1..10", 224, 224, 3], "default_shape": [1, 224, 224, 3]}}`
- `type` : Input type. Allowed values: `Image` and `Tensor` . By default, the converter generates an ML Model with inputs of type Tensor (MultiArray). User can set input type to be Image. Image input type requires additional input parameters such as `bias` and `scale` .
- `bias` : If the input type is an Image, you need to provide the bias vector.
- `scale` : If the input type is an Image, you need to provide a scale factor.

CoreML `ClassifierConfig` parameters can be specified using [OutputConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OutputConfig.html) `CompilerOptions` . CoreML converter supports Tensorflow and PyTorch models. CoreML conversion examples:

- Tensor type input:
- `"DataInputConfig": {"input_1": {"shape": [[1,224,224,3], [1,160,160,3]], "default_shape": [1,224,224,3]}}`
- Tensor type input without input name (PyTorch):
- `"DataInputConfig": [{"shape": [[1,3,224,224], [1,3,160,160]], "default_shape": [1,3,224,224]}]`
- Image type input:
- `"DataInputConfig": {"input_1": {"shape": [[1,224,224,3], [1,160,160,3]], "default_shape": [1,224,224,3], "type": "Image", "bias": [-1,-1,-1], "scale": 0.007843137255}}`
- `"CompilerOptions": {"class_labels": "imagenet_labels_1000.txt"}`
- Image type input without input name (PyTorch):
- `"DataInputConfig": [{"shape": [[1,3,224,224], [1,3,160,160]], "default_shape": [1,3,224,224], "type": "Image", "bias": [-1,-1,-1], "scale": 0.007843137255}]`
- `"CompilerOptions": {"class_labels": "imagenet_labels_1000.txt"}`

Depending on the model format, `DataInputConfig` requires the following parameters for `ml_eia2` [OutputConfig:TargetDevice](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OutputConfig.html#sagemaker-Type-OutputConfig-TargetDevice) .

- For TensorFlow models saved in the SavedModel format, specify the input names from `signature_def_key` and the input model shapes for `DataInputConfig` . Specify the `signature_def_key` in ` `OutputConfig:CompilerOptions` [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OutputConfig.html#sagemaker-Type-OutputConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OutputConfig.html#sagemaker-Type-OutputConfig)-CompilerOptions`__ if the model does not use TensorFlowâs default signature def key. For example:
- `"DataInputConfig": {"inputs": [1, 224, 224, 3]}`
- `"CompilerOptions": {"signature_def_key": "serving_custom"}`
- For TensorFlow models saved as a frozen graph, specify the input tensor names and shapes in `DataInputConfig` and the output tensor names for `output_names` in ` `OutputConfig:CompilerOptions` [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OutputConfig.html#sagemaker-Type-OutputConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OutputConfig.html#sagemaker-Type-OutputConfig)-CompilerOptions`__ . For example:
- `"DataInputConfig": {"input_tensor:0": [1, 224, 224, 3]}`
- `"CompilerOptions": {"output_names": ["output_tensor:0"]}`

Framework -> (string)

Identifies the framework in which the model was trained. For example: TENSORFLOW.

FrameworkVersion -> (string)

Specifies the framework version to use. This API field is only supported for the MXNet, PyTorch, TensorFlow and TensorFlow Lite frameworks.

For information about framework versions supported for cloud targets and edge devices, see [Cloud Supported Instance Types and Frameworks](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-supported-cloud.html) and [Edge Supported Frameworks](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-supported-devices-edge-frameworks.html) .

Shorthand Syntax:

```
S3Uri=string,DataInputConfig=string,Framework=string,FrameworkVersion=string
```

JSON Syntax:

```
{
  "S3Uri": "string",
  "DataInputConfig": "string",
  "Framework": "TENSORFLOW"|"KERAS"|"MXNET"|"ONNX"|"PYTORCH"|"XGBOOST"|"TFLITE"|"DARKNET"|"SKLEARN",
  "FrameworkVersion": "string"
}
```

`--output-config` (structure)

Provides information about the output location for the compiled model and the target device the model runs on.

S3OutputLocation -> (string)

Identifies the S3 bucket where you want Amazon SageMaker AI to store the model artifacts. For example, `s3://bucket-name/key-name-prefix` .

TargetDevice -> (string)

Identifies the target device or the machine learning instance that you want to run your model on after the compilation has completed. Alternatively, you can specify OS, architecture, and accelerator using [TargetPlatform](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TargetPlatform.html) fields. It can be used instead of `TargetPlatform` .

### Note

Currently `ml_trn1` is available only in US East (N. Virginia) Region, and `ml_inf2` is available only in US East (Ohio) Region.

TargetPlatform -> (structure)

Contains information about a target platform that you want your model to run on, such as OS, architecture, and accelerators. It is an alternative of `TargetDevice` .

The following examples show how to configure the `TargetPlatform` and `CompilerOptions` JSON strings for popular target platforms:

- Raspberry Pi 3 Model B+  `"TargetPlatform": {"Os": "LINUX", "Arch": "ARM_EABIHF"},` `"CompilerOptions": {'mattr': ['+neon']}`
- Jetson TX2  `"TargetPlatform": {"Os": "LINUX", "Arch": "ARM64", "Accelerator": "NVIDIA"},` `"CompilerOptions": {'gpu-code': 'sm_62', 'trt-ver': '6.0.1', 'cuda-ver': '10.0'}`
- EC2 m5.2xlarge instance OS  `"TargetPlatform": {"Os": "LINUX", "Arch": "X86_64", "Accelerator": "NVIDIA"},` `"CompilerOptions": {'mcpu': 'skylake-avx512'}`
- RK3399  `"TargetPlatform": {"Os": "LINUX", "Arch": "ARM64", "Accelerator": "MALI"}`
- ARMv7 phone (CPU)  `"TargetPlatform": {"Os": "ANDROID", "Arch": "ARM_EABI"},` `"CompilerOptions": {'ANDROID_PLATFORM': 25, 'mattr': ['+neon']}`
- ARMv8 phone (CPU)  `"TargetPlatform": {"Os": "ANDROID", "Arch": "ARM64"},` `"CompilerOptions": {'ANDROID_PLATFORM': 29}`

Os -> (string)

Specifies a target platform OS.

- `LINUX` : Linux-based operating systems.
- `ANDROID` : Android operating systems. Android API level can be specified using the `ANDROID_PLATFORM` compiler option. For example, `"CompilerOptions": {'ANDROID_PLATFORM': 28}`

Arch -> (string)

Specifies a target platform architecture.

- `X86_64` : 64-bit version of the x86 instruction set.
- `X86` : 32-bit version of the x86 instruction set.
- `ARM64` : ARMv8 64-bit CPU.
- `ARM_EABIHF` : ARMv7 32-bit, Hard Float.
- `ARM_EABI` : ARMv7 32-bit, Soft Float. Used by Android 32-bit ARM platform.

Accelerator -> (string)

Specifies a target platform accelerator (optional).

- `NVIDIA` : Nvidia graphics processing unit. It also requires `gpu-code` , `trt-ver` , `cuda-ver` compiler options
- `MALI` : ARM Mali graphics processor
- `INTEL_GRAPHICS` : Integrated Intel graphics

CompilerOptions -> (string)

Specifies additional parameters for compiler options in JSON format. The compiler options are `TargetPlatform` specific. It is required for NVIDIA accelerators and highly recommended for CPU compilations. For any other cases, it is optional to specify `CompilerOptions.`

- `DTYPE` : Specifies the data type for the input. When compiling for `ml_*` (except for `ml_inf` ) instances using PyTorch framework, provide the data type (dtype) of the modelâs input. `"float32"` is used if `"DTYPE"` is not specified. Options for data type are:
- float32: Use either `"float"` or `"float32"` .
- int64: Use either `"int64"` or `"long"` .

For example, `{"dtype" : "float32"}` .

- `CPU` : Compilation for CPU supports the following compiler options.
- `mcpu` : CPU micro-architecture. For example, `{'mcpu': 'skylake-avx512'}`
- `mattr` : CPU flags. For example, `{'mattr': ['+neon', '+vfpv4']}`
- `ARM` : Details of ARM CPU compilations.
- `NEON` : NEON is an implementation of the Advanced SIMD extension used in ARMv7 processors. For example, add `{'mattr': ['+neon']}` to the compiler options if compiling for ARM 32-bit platform with the NEON support.
- `NVIDIA` : Compilation for NVIDIA GPU supports the following compiler options.
- `gpu_code` : Specifies the targeted architecture.
- `trt-ver` : Specifies the TensorRT versions in x.y.z. format.
- `cuda-ver` : Specifies the CUDA version in x.y format.

For example, `{'gpu-code': 'sm_72', 'trt-ver': '6.0.1', 'cuda-ver': '10.1'}`

- `ANDROID` : Compilation for the Android OS supports the following compiler options:
- `ANDROID_PLATFORM` : Specifies the Android API levels. Available levels range from 21 to 29. For example, `{'ANDROID_PLATFORM': 28}` .
- `mattr` : Add `{'mattr': ['+neon']}` to compiler options if compiling for ARM 32-bit platform with NEON support.
- `INFERENTIA` : Compilation for target ml_inf1 uses compiler options passed in as a JSON string. For example, `"CompilerOptions": "\"--verbose 1 --num-neuroncores 2 -O2\""` .  For information about supported compiler options, see [Neuron Compiler CLI Reference Guide](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/compiler/neuronx-cc/api-reference-guide/neuron-compiler-cli-reference-guide.html) .
- `CoreML` : Compilation for the CoreML [OutputConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OutputConfig.html) `TargetDevice` supports the following compiler options:
- `class_labels` : Specifies the classification labels file name inside input tar.gz file. For example, `{"class_labels": "imagenet_labels_1000.txt"}` . Labels inside the txt file should be separated by newlines.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service key (Amazon Web Services KMS) that Amazon SageMaker AI uses to encrypt your output models with Amazon S3 server-side encryption after compilation job. If you donât provide a KMS key ID, Amazon SageMaker AI uses the default KMS key for Amazon S3 for your roleâs account. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide.*

The KmsKeyId can be any of the following formats:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`

Shorthand Syntax:

```
S3OutputLocation=string,TargetDevice=string,TargetPlatform={Os=string,Arch=string,Accelerator=string},CompilerOptions=string,KmsKeyId=string
```

JSON Syntax:

```
{
  "S3OutputLocation": "string",
  "TargetDevice": "lambda"|"ml_m4"|"ml_m5"|"ml_m6g"|"ml_c4"|"ml_c5"|"ml_c6g"|"ml_p2"|"ml_p3"|"ml_g4dn"|"ml_inf1"|"ml_inf2"|"ml_trn1"|"ml_eia2"|"jetson_tx1"|"jetson_tx2"|"jetson_nano"|"jetson_xavier"|"rasp3b"|"rasp4b"|"imx8qm"|"deeplens"|"rk3399"|"rk3288"|"aisage"|"sbe_c"|"qcs605"|"qcs603"|"sitara_am57x"|"amba_cv2"|"amba_cv22"|"amba_cv25"|"x86_win32"|"x86_win64"|"coreml"|"jacinto_tda4vm"|"imx8mplus",
  "TargetPlatform": {
    "Os": "ANDROID"|"LINUX",
    "Arch": "X86_64"|"X86"|"ARM64"|"ARM_EABI"|"ARM_EABIHF",
    "Accelerator": "INTEL_GRAPHICS"|"MALI"|"NVIDIA"|"NNA"
  },
  "CompilerOptions": "string",
  "KmsKeyId": "string"
}
```

`--vpc-config` (structure)

A [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that you want your compilation job to connect to. Control access to your models by configuring the VPC. For more information, see [Protect Compilation Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-vpc.html) .

SecurityGroupIds -> (list)

The VPC security group IDs. IDs have the form of `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC that you want to connect the compilation job to for accessing the model in Amazon S3.

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

`--stopping-condition` (structure)

Specifies a limit to how long a model compilation job can run. When the job reaches the time limit, Amazon SageMaker AI ends the compilation job. Use this API to cap model training costs.

MaxRuntimeInSeconds -> (integer)

The maximum length of time, in seconds, that a training or compilation job can run before it is stopped.

For compilation jobs, if the job does not complete during this time, a `TimeOut` error is generated. We recommend starting with 900 seconds and increasing as necessary based on your model.

For all other jobs, if the job does not complete during this time, SageMaker ends the job. When `RetryStrategy` is specified in the job request, `MaxRuntimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt. The default value is 1 day. The maximum value is 28 days.

The maximum time that a `TrainingJob` can run in total, including any time spent publishing metrics or archiving and uploading models after it has been stopped, is 30 days.

MaxWaitTimeInSeconds -> (integer)

The maximum length of time, in seconds, that a managed Spot training job has to complete. It is the amount of time spent waiting for Spot capacity plus the amount of time the job can run. It must be equal to or greater than `MaxRuntimeInSeconds` . If the job does not complete during this time, SageMaker ends the job.

When `RetryStrategy` is specified in the job request, `MaxWaitTimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt.

MaxPendingTimeInSeconds -> (integer)

The maximum length of time, in seconds, that a training or compilation job can be pending before it is stopped.

### Note

When working with training jobs that use capacity from [training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html) , not all `Pending` job states count against the `MaxPendingTimeInSeconds` limit. The following scenarios do not increment the `MaxPendingTimeInSeconds` counter:

- The plan is in a `Scheduled` state: Jobs queued (in `Pending` status) before a planâs start date (waiting for scheduled start time)
- Between capacity reservations: Jobs temporarily back to `Pending` status between two capacity reservation periods

`MaxPendingTimeInSeconds` only increments when jobs are actively waiting for capacity in an `Active` plan.

Shorthand Syntax:

```
MaxRuntimeInSeconds=integer,MaxWaitTimeInSeconds=integer,MaxPendingTimeInSeconds=integer
```

JSON Syntax:

```
{
  "MaxRuntimeInSeconds": integer,
  "MaxWaitTimeInSeconds": integer,
  "MaxPendingTimeInSeconds": integer
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

CompilationJobArn -> (string)

If the action is successful, the service sends back an HTTP 200 response. Amazon SageMaker AI returns the following data in JSON format:

- `CompilationJobArn` : The Amazon Resource Name (ARN) of the compiled job.