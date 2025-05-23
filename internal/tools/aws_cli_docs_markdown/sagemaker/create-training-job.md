# create-training-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-training-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-training-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-training-job

## Description

Starts a model training job. After training completes, SageMaker saves the resulting model artifacts to an Amazon S3 location that you specify.

If you choose to host your model using SageMaker hosting services, you can use the resulting model artifacts as part of the model. You can also use the artifacts in a machine learning service other than SageMaker, provided that you know how to use them for inference.

In the request body, you provide the following:

- `AlgorithmSpecification` - Identifies the training algorithm to use.
- `HyperParameters` - Specify these algorithm-specific parameters to enable the estimation of model parameters during training. Hyperparameters can be tuned to optimize this learning process. For a list of hyperparameters for each training algorithm provided by SageMaker, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) .

### Warning

Do not include any security-sensitive information including account access IDs, secrets, or tokens in any hyperparameter fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request hyperparameter variable or plain text fields.

- `InputDataConfig` - Describes the input required by the training job and the Amazon S3, EFS, or FSx location where it is stored.
- `OutputDataConfig` - Identifies the Amazon S3 bucket where you want SageMaker to save the results of model training.
- `ResourceConfig` - Identifies the resources, ML compute instances, and ML storage volumes to deploy for model training. In distributed training, you specify more than one instance.
- `EnableManagedSpotTraining` - Optimize the cost of training machine learning models by up to 80% by using Amazon EC2 Spot instances. For more information, see [Managed Spot Training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html) .
- `RoleArn` - The Amazon Resource Name (ARN) that SageMaker assumes to perform tasks on your behalf during model training. You must grant this role the necessary permissions so that SageMaker can successfully complete model training.
- `StoppingCondition` - To help cap training costs, use `MaxRuntimeInSeconds` to set a time limit for training. Use `MaxWaitTimeInSeconds` to specify how long a managed spot training job has to complete.
- `Environment` - The environment variables to set in the Docker container.

### Warning

Do not include any security-sensitive information including account access IDs, secrets, or tokens in any environment fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request environment variable or plain text fields.

- `RetryStrategy` - The number of times to retry the job when the job fails due to an `InternalServerError` .

For more information about SageMaker, see [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateTrainingJob)

## Synopsis

```
create-training-job
--training-job-name <value>
[--hyper-parameters <value>]
--algorithm-specification <value>
--role-arn <value>
[--input-data-config <value>]
--output-data-config <value>
--resource-config <value>
[--vpc-config <value>]
--stopping-condition <value>
[--tags <value>]
[--enable-network-isolation | --no-enable-network-isolation]
[--enable-inter-container-traffic-encryption | --no-enable-inter-container-traffic-encryption]
[--enable-managed-spot-training | --no-enable-managed-spot-training]
[--checkpoint-config <value>]
[--debug-hook-config <value>]
[--debug-rule-configurations <value>]
[--tensor-board-output-config <value>]
[--experiment-config <value>]
[--profiler-config <value>]
[--profiler-rule-configurations <value>]
[--environment <value>]
[--retry-strategy <value>]
[--remote-debug-config <value>]
[--infra-check-config <value>]
[--session-chaining-config <value>]
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

`--training-job-name` (string)

The name of the training job. The name must be unique within an Amazon Web Services Region in an Amazon Web Services account.

`--hyper-parameters` (map)

Algorithm-specific parameters that influence the quality of the model. You set hyperparameters before you start the learning process. For a list of hyperparameters for each training algorithm provided by SageMaker, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) .

You can specify a maximum of 100 hyperparameters. Each hyperparameter is a key-value pair. Each key and value is limited to 256 characters, as specified by the `Length Constraint` .

### Warning

Do not include any security-sensitive information including account access IDs, secrets, or tokens in any hyperparameter fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by any security-sensitive information included in the request hyperparameter variable or plain text fields.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--algorithm-specification` (structure)

The registry path of the Docker image that contains the training algorithm and algorithm-specific metadata, including the input mode. For more information about algorithms provided by SageMaker, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) . For information about providing your own algorithms, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) .

TrainingImage -> (string)

The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for SageMaker built-in algorithms, see [Docker Registry Paths and Example Code](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html) in the *Amazon SageMaker developer guide* . SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information about using your custom training container, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) .

### Note

You must specify either the algorithm name to the `AlgorithmName` parameter or the image URI of the algorithm container to the `TrainingImage` parameter.

For more information, see the note in the `AlgorithmName` parameter description.

AlgorithmName -> (string)

The name of the algorithm resource to use for the training job. This must be an algorithm resource that you created or subscribe to on Amazon Web Services Marketplace.

### Note

You must specify either the algorithm name to the `AlgorithmName` parameter or the image URI of the algorithm container to the `TrainingImage` parameter.

Note that the `AlgorithmName` parameter is mutually exclusive with the `TrainingImage` parameter. If you specify a value for the `AlgorithmName` parameter, you canât specify a value for `TrainingImage` , and vice versa.

If you specify values for both parameters, the training job might break; if you donât specify any value for both parameters, the training job might raise a `null` error.

TrainingInputMode -> (string)

The training input mode that the algorithm supports. For more information about input modes, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) .

**Pipe mode**

If an algorithm supports `Pipe` mode, Amazon SageMaker streams data directly from Amazon S3 to the container.

**File mode**

If an algorithm supports `File` mode, SageMaker downloads the training data from S3 to the provisioned ML storage volume, and mounts the directory to the Docker volume for the training container.

You must provision the ML storage volume with sufficient capacity to accommodate the data downloaded from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container uses the ML storage volume to also store intermediate information, if any.

For distributed algorithms, training data is distributed uniformly. Your training duration is predictable if the input data objects sizes are approximately the same. SageMaker does not split the files any further for model training. If the object sizes are skewed, training wonât be optimal as the data distribution is also skewed when one host in a training cluster is overloaded, thus becoming a bottleneck in training.

**FastFile mode**

If an algorithm supports `FastFile` mode, SageMaker streams data directly from S3 to the container with no code changes, and provides file system access to the data. Users can author their training script to interact with these files as if they were stored on disk.

`FastFile` mode works best when the data is read sequentially. Augmented manifest files arenât supported. The startup time is lower when there are fewer files in the S3 bucket provided.

MetricDefinitions -> (list)

A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. SageMaker publishes each metric to Amazon CloudWatch.

(structure)

Specifies a metric that the training algorithm writes to `stderr` or `stdout` . You can view these logs to understand how your training job performs and check for any errors encountered during training. SageMaker hyperparameter tuning captures all defined metrics. Specify one of the defined metrics to use as an objective metric using the [TuningObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-TuningObjective) parameter in the `HyperParameterTrainingJobDefinition` API to evaluate job performance during hyperparameter tuning.

Name -> (string)

The name of the metric.

Regex -> (string)

A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see [Defining metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) .

EnableSageMakerMetricsTimeSeries -> (boolean)

To generate and save time-series metrics during training, set to `true` . The default is `false` and time-series metrics arenât generated except in the following cases:

- You use one of the SageMaker built-in algorithms
- You use one of the following [Prebuilt SageMaker Docker Images](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.html) :
- Tensorflow (version >= 1.15)
- MXNet (version >= 1.6)
- PyTorch (version >= 1.3)
- You specify at least one [MetricDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDefinition.html)

ContainerEntrypoint -> (list)

The [entrypoint script for a Docker container](https://docs.docker.com/engine/reference/builder/) used to run a training job. This script takes precedence over the default train processing instructions. See [How Amazon SageMaker Runs Your Training Image](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html) for more information.

(string)

ContainerArguments -> (list)

The arguments for a container used to run a training job. See [How Amazon SageMaker Runs Your Training Image](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html) for additional information.

(string)

TrainingImageConfig -> (structure)

The configuration to use an image from a private Docker registry for a training job.

TrainingRepositoryAccessMode -> (string)

The method that your training job will use to gain access to the images in your private Docker registry. For access to an image in a private Docker registry, set to `Vpc` .

TrainingRepositoryAuthConfig -> (structure)

An object containing authentication information for a private Docker registry containing your training images.

TrainingRepositoryCredentialsProviderArn -> (string)

The Amazon Resource Name (ARN) of an Amazon Web Services Lambda function used to give SageMaker access credentials to your private Docker registry.

Shorthand Syntax:

```
TrainingImage=string,AlgorithmName=string,TrainingInputMode=string,MetricDefinitions=[{Name=string,Regex=string},{Name=string,Regex=string}],EnableSageMakerMetricsTimeSeries=boolean,ContainerEntrypoint=string,string,ContainerArguments=string,string,TrainingImageConfig={TrainingRepositoryAccessMode=string,TrainingRepositoryAuthConfig={TrainingRepositoryCredentialsProviderArn=string}}
```

JSON Syntax:

```
{
  "TrainingImage": "string",
  "AlgorithmName": "string",
  "TrainingInputMode": "Pipe"|"File"|"FastFile",
  "MetricDefinitions": [
    {
      "Name": "string",
      "Regex": "string"
    }
    ...
  ],
  "EnableSageMakerMetricsTimeSeries": true|false,
  "ContainerEntrypoint": ["string", ...],
  "ContainerArguments": ["string", ...],
  "TrainingImageConfig": {
    "TrainingRepositoryAccessMode": "Platform"|"Vpc",
    "TrainingRepositoryAuthConfig": {
      "TrainingRepositoryCredentialsProviderArn": "string"
    }
  }
}
```

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role that SageMaker can assume to perform tasks on your behalf.

During model training, SageMaker needs your permission to read input data from an S3 bucket, download a Docker image that contains training code, write model artifacts to an S3 bucket, write logs to Amazon CloudWatch Logs, and publish metrics to Amazon CloudWatch. You grant permissions for all of these tasks to an IAM role. For more information, see [SageMaker Roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html) .

### Note

To be able to pass this role to SageMaker, the caller of this API must have the `iam:PassRole` permission.

`--input-data-config` (list)

An array of `Channel` objects. Each channel is a named input source. `InputDataConfig` describes the input data and its location.

Algorithms can accept input data from one or more channels. For example, an algorithm might have two channels of input data, `training_data` and `validation_data` . The configuration for each channel provides the S3, EFS, or FSx location where the input data is stored. It also provides information about the stored data: the MIME type, compression method, and whether the data is wrapped in RecordIO format.

Depending on the input mode that the algorithm supports, SageMaker either copies input data files from an S3 bucket to a local directory in the Docker container, or makes it available as input streams. For example, if you specify an EFS location, input data files are available as input streams. They do not need to be downloaded.

Your input must be in the same Amazon Web Services region as your training job.

(structure)

A channel is a named input source that training algorithms can consume.

ChannelName -> (string)

The name of the channel.

DataSource -> (structure)

The location of the channel data.

S3DataSource -> (structure)

The S3 location of the data source that is associated with a channel.

S3DataType -> (string)

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix for model training.

If you choose `ManifestFile` , `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want SageMaker to use for model training.

If you choose `AugmentedManifestFile` , `S3Uri` identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. `AugmentedManifestFile` can only be used if the Channelâs input mode is `Pipe` .

S3Uri -> (string)

Depending on the value specified for the `S3DataType` , identifies either a key name prefix or a manifest. For example:

- A key name prefix might look like this: `s3://bucketname/exampleprefix/`
- A manifest might look like this: `s3://bucketname/example.manifest`   A manifest is an S3 object which is a JSON file consisting of an array of elements. The first element is a prefix which is followed by one or more suffixes. SageMaker appends the suffix elements to the prefix to get a full set of `S3Uri` . Note that the prefix must be a valid non-empty `S3Uri` that precludes users from specifying a manifest whose individual `S3Uri` is sourced from different S3 buckets. The following code example shows a valid manifest format:   `[ {"prefix": "s3://customer_bucket/some/prefix/"},` `"relative/path/to/custdata-1",` `"relative/path/custdata-2",` `...` `"relative/path/custdata-N"` `]`   This JSON is equivalent to the following `S3Uri` list:  `s3://customer_bucket/some/prefix/relative/path/to/custdata-1` `s3://customer_bucket/some/prefix/relative/path/custdata-2` `...` `s3://customer_bucket/some/prefix/relative/path/custdata-N`   The complete set of `S3Uri` in this manifest is the input data for the channel for this data source. The object that each `S3Uri` points to must be readable by the IAM role that SageMaker uses to perform tasks on your behalf.

Your input bucket must be located in same Amazon Web Services region as your training job.

S3DataDistributionType -> (string)

If you want SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify `FullyReplicated` .

If you want SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify `ShardedByS3Key` . If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data.

Donât choose more ML compute instances for training than available S3 objects. If you do, some nodes wonât get any data and you will pay for nodes that arenât getting any training data. This applies in both File and Pipe modes. Keep this in mind when developing algorithms.

In distributed training, where you use multiple ML compute EC2 instances, you might choose `ShardedByS3Key` . If the algorithm requires copying training data to the ML storage volume (when `TrainingInputMode` is set to `File` ), this copies 1/*n* of the number of objects.

AttributeNames -> (list)

A list of one or more attribute names to use that are found in a specified augmented manifest file.

(string)

InstanceGroupNames -> (list)

A list of names of instance groups that get data from the S3 data source.

(string)

ModelAccessConfig -> (structure)

The access configuration file to control access to the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` .

- If you are a Jumpstart user, see the [End-user license agreements](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html#jumpstart-foundation-models-choose-eula) section for more details on accepting the EULA.
- If you are an AutoML user, see the *Optional Parameters* section of *Create an AutoML job to fine-tune text generation models using the API* for details on [How to set the EULA acceptance when fine-tuning a model using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-finetune-llms.html#autopilot-llms-finetuning-api-optional-params) .

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

The configuration for a private hub model reference that points to a SageMaker JumpStart public hub model.

HubContentArn -> (string)

The ARN of your private model hub content. This should be a `ModelReference` resource type that points to a SageMaker JumpStart public hub model.

FileSystemDataSource -> (structure)

The file system that is associated with a channel.

FileSystemId -> (string)

The file system id.

FileSystemAccessMode -> (string)

The access mode of the mount of the directory associated with the channel. A directory can be mounted either in `ro` (read-only) or `rw` (read-write) mode.

FileSystemType -> (string)

The file system type.

DirectoryPath -> (string)

The full path to the directory to associate with the channel.

ContentType -> (string)

The MIME type of the data.

CompressionType -> (string)

If training data is compressed, the compression type. The default value is `None` . `CompressionType` is used only in Pipe input mode. In File mode, leave this field unset or set it to None.

RecordWrapperType -> (string)

Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format. In this case, SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you donât need to set this attribute. For more information, see [Create a Dataset Using RecordIO](https://mxnet.apache.org/api/architecture/note_data_loading#data-format) .

In File mode, leave this field unset or set it to None.

InputMode -> (string)

(Optional) The input mode to use for the data channel in a training job. If you donât set a value for `InputMode` , SageMaker uses the value set for `TrainingInputMode` . Use this parameter to override the `TrainingInputMode` setting in a [AlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html) request when you have a channel that needs a different input mode from the training jobâs general setting. To download the data from Amazon Simple Storage Service (Amazon S3) to the provisioned ML storage volume, and mount the directory to a Docker volume, use `File` input mode. To stream data directly from Amazon S3 to the container, choose `Pipe` input mode.

To use a model for incremental training, choose `File` input model.

ShuffleConfig -> (structure)

A configuration for a shuffle option for input data in a channel. If you use `S3Prefix` for `S3DataType` , this shuffles the results of the S3 key prefix matches. If you use `ManifestFile` , the order of the S3 object references in the `ManifestFile` is shuffled. If you use `AugmentedManifestFile` , the order of the JSON lines in the `AugmentedManifestFile` is shuffled. The shuffling order is determined using the `Seed` value.

For Pipe input mode, shuffling is done at the start of every epoch. With large datasets this ensures that the order of the training data is different for each epoch, it helps reduce bias and possible overfitting. In a multi-node training job when ShuffleConfig is combined with `S3DataDistributionType` of `ShardedByS3Key` , the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.

Seed -> (long)

Determines the shuffling order in `ShuffleConfig` value.

JSON Syntax:

```
[
  {
    "ChannelName": "string",
    "DataSource": {
      "S3DataSource": {
        "S3DataType": "ManifestFile"|"S3Prefix"|"AugmentedManifestFile",
        "S3Uri": "string",
        "S3DataDistributionType": "FullyReplicated"|"ShardedByS3Key",
        "AttributeNames": ["string", ...],
        "InstanceGroupNames": ["string", ...],
        "ModelAccessConfig": {
          "AcceptEula": true|false
        },
        "HubAccessConfig": {
          "HubContentArn": "string"
        }
      },
      "FileSystemDataSource": {
        "FileSystemId": "string",
        "FileSystemAccessMode": "rw"|"ro",
        "FileSystemType": "EFS"|"FSxLustre",
        "DirectoryPath": "string"
      }
    },
    "ContentType": "string",
    "CompressionType": "None"|"Gzip",
    "RecordWrapperType": "None"|"RecordIO",
    "InputMode": "Pipe"|"File"|"FastFile",
    "ShuffleConfig": {
      "Seed": long
    }
  }
  ...
]
```

`--output-data-config` (structure)

Specifies the path to the S3 location where you want to store model artifacts. SageMaker creates subfolders for the artifacts.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The `KmsKeyId` can be any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
- // KMS Key Alias  `"alias/ExampleAlias"`
- // Amazon Resource Name (ARN) of a KMS Key Alias  `"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"`

If you use a KMS key ID or an alias of your KMS key, the SageMaker execution role must include permissions to call `kms:Encrypt` . If you donât provide a KMS key ID, SageMaker uses the default KMS key for Amazon S3 for your roleâs account. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide* . If the output data is stored in Amazon S3 Express One Zone, it is encrypted with server-side encryption with Amazon S3 managed keys (SSE-S3). KMS key is not supported for Amazon S3 Express One Zone

The KMS key policy must grant permission to the IAM role that you specify in your `CreateTrainingJob` , `CreateTransformJob` , or `CreateHyperParameterTuningJob` requests. For more information, see [Using Key Policies in Amazon Web Services KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *Amazon Web Services Key Management Service Developer Guide* .

S3OutputPath -> (string)

Identifies the S3 path where you want SageMaker to store the model artifacts. For example, `s3://bucket-name/key-name-prefix` .

CompressionType -> (string)

The model output compression type. Select `None` to output an uncompressed model, recommended for large model outputs. Defaults to gzip.

Shorthand Syntax:

```
KmsKeyId=string,S3OutputPath=string,CompressionType=string
```

JSON Syntax:

```
{
  "KmsKeyId": "string",
  "S3OutputPath": "string",
  "CompressionType": "GZIP"|"NONE"
}
```

`--resource-config` (structure)

The resources, including the ML compute instances and ML storage volumes, to use for model training.

ML storage volumes store model artifacts and incremental states. Training algorithms might also use ML storage volumes for scratch space. If you want SageMaker to use the ML storage volume to store the training data, choose `File` as the `TrainingInputMode` in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.

InstanceType -> (string)

The ML compute instance type.

### Note

SageMaker Training on Amazon Elastic Compute Cloud (EC2) P4de instances is in preview release starting December 9th, 2022.

[Amazon EC2 P4de instances](http://aws.amazon.com/ec2/instance-types/p4/) (currently in preview) are powered by 8 NVIDIA A100 GPUs with 80GB high-performance HBM2e GPU memory, which accelerate the speed of training ML models that need to be trained on large datasets of high-resolution data. In this preview release, Amazon SageMaker supports ML training jobs on P4de instances (`ml.p4de.24xlarge` ) to reduce model training time. The `ml.p4de.24xlarge` instances are available in the following Amazon Web Services Regions.

- US East (N. Virginia) (us-east-1)
- US West (Oregon) (us-west-2)

To request quota limit increase and start using P4de instances, contact the SageMaker Training service team through your account team.

InstanceCount -> (integer)

The number of ML compute instances to use. For distributed training, provide a value greater than 1.

VolumeSizeInGB -> (integer)

The size of the ML storage volume that you want to provision.

ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose `File` as the `TrainingInputMode` in the algorithm specification.

When using an ML instance with [NVMe SSD volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#nvme-ssd-volumes) , SageMaker doesnât provision Amazon EBS General Purpose SSD (gp2) storage. Available storage is fixed to the NVMe-type instanceâs storage capacity. SageMaker configures storage paths for training datasets, checkpoints, model artifacts, and outputs to use the entire capacity of the instance storage. For example, ML instance families with the NVMe-type instance storage include `ml.p4d` , `ml.g4dn` , and `ml.g5` .

When using an ML instance with the EBS-only storage option and without instance storage, you must define the size of EBS volume through `VolumeSizeInGB` in the `ResourceConfig` API. For example, ML instance families that use EBS volumes include `ml.c5` and `ml.p2` .

To look up instance types and their instance storage types and volumes, see [Amazon EC2 Instance Types](http://aws.amazon.com/ec2/instance-types/) .

To find the default local paths defined by the SageMaker training platform, see [Amazon SageMaker Training Storage Folders for Training Datasets, Checkpoints, Model Artifacts, and Outputs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-train-storage.html) .

VolumeKmsKeyId -> (string)

The Amazon Web Services KMS key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job.

### Note

Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You canât request a `VolumeKmsKeyId` when using an instance type with local storage.

For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes) .

For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) .

The `VolumeKmsKeyId` can be in any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

KeepAlivePeriodInSeconds -> (integer)

The duration of time in seconds to retain configured resources in a warm pool for subsequent training jobs.

InstanceGroups -> (list)

The configuration of a heterogeneous cluster in JSON format.

(structure)

Defines an instance group for heterogeneous cluster training. When requesting a training job using the [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API, you can configure multiple instance groups .

InstanceType -> (string)

Specifies the instance type of the instance group.

InstanceCount -> (integer)

Specifies the number of instances of the instance group.

InstanceGroupName -> (string)

Specifies the name of the instance group.

TrainingPlanArn -> (string)

The Amazon Resource Name (ARN); of the training plan to use for this resource configuration.

Shorthand Syntax:

```
InstanceType=string,InstanceCount=integer,VolumeSizeInGB=integer,VolumeKmsKeyId=string,KeepAlivePeriodInSeconds=integer,InstanceGroups=[{InstanceType=string,InstanceCount=integer,InstanceGroupName=string},{InstanceType=string,InstanceCount=integer,InstanceGroupName=string}],TrainingPlanArn=string
```

JSON Syntax:

```
{
  "InstanceType": "ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.p3dn.24xlarge"|"ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.p5.48xlarge"|"ml.p5e.48xlarge"|"ml.p5en.48xlarge"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.c5n.xlarge"|"ml.c5n.2xlarge"|"ml.c5n.4xlarge"|"ml.c5n.9xlarge"|"ml.c5n.18xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.16xlarge"|"ml.g6.12xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.16xlarge"|"ml.g6e.12xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.trn2.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.8xlarge"|"ml.c6i.4xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.8xlarge"|"ml.r5d.12xlarge"|"ml.r5d.16xlarge"|"ml.r5d.24xlarge"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge",
  "InstanceCount": integer,
  "VolumeSizeInGB": integer,
  "VolumeKmsKeyId": "string",
  "KeepAlivePeriodInSeconds": integer,
  "InstanceGroups": [
    {
      "InstanceType": "ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.p3dn.24xlarge"|"ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.p5.48xlarge"|"ml.p5e.48xlarge"|"ml.p5en.48xlarge"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.c5n.xlarge"|"ml.c5n.2xlarge"|"ml.c5n.4xlarge"|"ml.c5n.9xlarge"|"ml.c5n.18xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.16xlarge"|"ml.g6.12xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.16xlarge"|"ml.g6e.12xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.trn2.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.8xlarge"|"ml.c6i.4xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.8xlarge"|"ml.r5d.12xlarge"|"ml.r5d.16xlarge"|"ml.r5d.24xlarge"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge",
      "InstanceCount": integer,
      "InstanceGroupName": "string"
    }
    ...
  ],
  "TrainingPlanArn": "string"
}
```

`--vpc-config` (structure)

A [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that you want your training job to connect to. Control access to and from your training container by configuring the VPC. For more information, see [Protect Training Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html) .

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

`--stopping-condition` (structure)

Specifies a limit to how long a model training job can run. It also specifies how long a managed Spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.

To stop a job, SageMaker sends the algorithm the `SIGTERM` signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost.

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

### Warning

Do not include any security-sensitive information including account access IDs, secrets, or tokens in any tags. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by any security-sensitive information included in the request tag variable or plain text fields.

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

`--enable-network-isolation` | `--no-enable-network-isolation` (boolean)

Isolates the training container. No inbound or outbound network calls can be made, except for calls between peers within a training cluster for distributed training. If you enable network isolation for training jobs that are configured to use a VPC, SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.

`--enable-inter-container-traffic-encryption` | `--no-enable-inter-container-traffic-encryption` (boolean)

To encrypt all communications between ML compute instances in distributed training, choose `True` . Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training. For more information, see [Protect Communications Between ML Compute Instances in a Distributed Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/train-encrypt.html) .

`--enable-managed-spot-training` | `--no-enable-managed-spot-training` (boolean)

To train models using managed spot training, choose `True` . Managed spot training provides a fully managed and scalable infrastructure for training machine learning models. this option is useful when training jobs can be interrupted and when there is flexibility when the training job is run.

The complete and intermediate results of jobs are stored in an Amazon S3 bucket, and can be used as a starting point to train models incrementally. Amazon SageMaker provides metrics and logs in CloudWatch. They can be used to see when managed spot training jobs are running, interrupted, resumed, or completed.

`--checkpoint-config` (structure)

Contains information about the output location for managed spot training checkpoint data.

S3Uri -> (string)

Identifies the S3 path where you want SageMaker to store checkpoints. For example, `s3://bucket-name/key-name-prefix` .

LocalPath -> (string)

(Optional) The local directory where checkpoints are written. The default directory is `/opt/ml/checkpoints/` .

Shorthand Syntax:

```
S3Uri=string,LocalPath=string
```

JSON Syntax:

```
{
  "S3Uri": "string",
  "LocalPath": "string"
}
```

`--debug-hook-config` (structure)

Configuration information for the Amazon SageMaker Debugger hook parameters, metric and tensor collections, and storage paths. To learn more about how to configure the `DebugHookConfig` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html) .

LocalPath -> (string)

Path to local storage location for metrics and tensors. Defaults to `/opt/ml/output/tensors/` .

S3OutputPath -> (string)

Path to Amazon S3 storage location for metrics and tensors.

HookParameters -> (map)

Configuration information for the Amazon SageMaker Debugger hook parameters.

key -> (string)

value -> (string)

CollectionConfigurations -> (list)

Configuration information for Amazon SageMaker Debugger tensor collections. To learn more about how to configure the `CollectionConfiguration` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html) .

(structure)

Configuration information for the Amazon SageMaker Debugger output tensor collections.

CollectionName -> (string)

The name of the tensor collection. The name must be unique relative to other rule configuration names.

CollectionParameters -> (map)

Parameter values for the tensor collection. The allowed parameters are `"name"` , `"include_regex"` , `"reduction_config"` , `"save_config"` , `"tensor_names"` , and `"save_histogram"` .

key -> (string)

value -> (string)

Shorthand Syntax:

```
LocalPath=string,S3OutputPath=string,HookParameters={KeyName1=string,KeyName2=string},CollectionConfigurations=[{CollectionName=string,CollectionParameters={KeyName1=string,KeyName2=string}},{CollectionName=string,CollectionParameters={KeyName1=string,KeyName2=string}}]
```

JSON Syntax:

```
{
  "LocalPath": "string",
  "S3OutputPath": "string",
  "HookParameters": {"string": "string"
    ...},
  "CollectionConfigurations": [
    {
      "CollectionName": "string",
      "CollectionParameters": {"string": "string"
        ...}
    }
    ...
  ]
}
```

`--debug-rule-configurations` (list)

Configuration information for Amazon SageMaker Debugger rules for debugging output tensors.

(structure)

Configuration information for SageMaker Debugger rules for debugging. To learn more about how to configure the `DebugRuleConfiguration` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html) .

RuleConfigurationName -> (string)

The name of the rule configuration. It must be unique relative to other rule configuration names.

LocalPath -> (string)

Path to local storage location for output of rules. Defaults to `/opt/ml/processing/output/rule/` .

S3OutputPath -> (string)

Path to Amazon S3 storage location for rules.

RuleEvaluatorImage -> (string)

The Amazon Elastic Container (ECR) Image for the managed rule evaluation.

InstanceType -> (string)

The instance type to deploy a custom rule for debugging a training job.

VolumeSizeInGB -> (integer)

The size, in GB, of the ML storage volume attached to the processing instance.

RuleParameters -> (map)

Runtime configuration for rule container.

key -> (string)

value -> (string)

Shorthand Syntax:

```
RuleConfigurationName=string,LocalPath=string,S3OutputPath=string,RuleEvaluatorImage=string,InstanceType=string,VolumeSizeInGB=integer,RuleParameters={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "RuleConfigurationName": "string",
    "LocalPath": "string",
    "S3OutputPath": "string",
    "RuleEvaluatorImage": "string",
    "InstanceType": "ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.8xlarge"|"ml.r5d.12xlarge"|"ml.r5d.16xlarge"|"ml.r5d.24xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge",
    "VolumeSizeInGB": integer,
    "RuleParameters": {"string": "string"
      ...}
  }
  ...
]
```

`--tensor-board-output-config` (structure)

Configuration of storage locations for the Amazon SageMaker Debugger TensorBoard output data.

LocalPath -> (string)

Path to local storage location for tensorBoard output. Defaults to `/opt/ml/output/tensorboard` .

S3OutputPath -> (string)

Path to Amazon S3 storage location for TensorBoard output.

Shorthand Syntax:

```
LocalPath=string,S3OutputPath=string
```

JSON Syntax:

```
{
  "LocalPath": "string",
  "S3OutputPath": "string"
}
```

`--experiment-config` (structure)

Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:

- [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
- [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
- [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)

ExperimentName -> (string)

The name of an existing experiment to associate with the trial component.

TrialName -> (string)

The name of an existing trial to associate the trial component with. If not specified, a new trial is created.

TrialComponentDisplayName -> (string)

The display name for the trial component. If this key isnât specified, the display name is the trial component name.

RunName -> (string)

The name of the experiment run to associate with the trial component.

Shorthand Syntax:

```
ExperimentName=string,TrialName=string,TrialComponentDisplayName=string,RunName=string
```

JSON Syntax:

```
{
  "ExperimentName": "string",
  "TrialName": "string",
  "TrialComponentDisplayName": "string",
  "RunName": "string"
}
```

`--profiler-config` (structure)

Configuration information for Amazon SageMaker Debugger system monitoring, framework profiling, and storage paths.

S3OutputPath -> (string)

Path to Amazon S3 storage location for system and framework metrics.

ProfilingIntervalInMilliseconds -> (long)

A time interval for capturing system metrics in milliseconds. Available values are 100, 200, 500, 1000 (1 second), 5000 (5 seconds), and 60000 (1 minute) milliseconds. The default value is 500 milliseconds.

ProfilingParameters -> (map)

Configuration information for capturing framework metrics. Available key strings for different profiling options are `DetailedProfilingConfig` , `PythonProfilingConfig` , and `DataLoaderProfilingConfig` . The following codes are configuration structures for the `ProfilingParameters` parameter. To learn more about how to configure the `ProfilingParameters` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html) .

key -> (string)

value -> (string)

DisableProfiler -> (boolean)

Configuration to turn off Amazon SageMaker Debuggerâs system monitoring and profiling functionality. To turn it off, set to `True` .

Shorthand Syntax:

```
S3OutputPath=string,ProfilingIntervalInMilliseconds=long,ProfilingParameters={KeyName1=string,KeyName2=string},DisableProfiler=boolean
```

JSON Syntax:

```
{
  "S3OutputPath": "string",
  "ProfilingIntervalInMilliseconds": long,
  "ProfilingParameters": {"string": "string"
    ...},
  "DisableProfiler": true|false
}
```

`--profiler-rule-configurations` (list)

Configuration information for Amazon SageMaker Debugger rules for profiling system and framework metrics.

(structure)

Configuration information for profiling rules.

RuleConfigurationName -> (string)

The name of the rule configuration. It must be unique relative to other rule configuration names.

LocalPath -> (string)

Path to local storage location for output of rules. Defaults to `/opt/ml/processing/output/rule/` .

S3OutputPath -> (string)

Path to Amazon S3 storage location for rules.

RuleEvaluatorImage -> (string)

The Amazon Elastic Container Registry Image for the managed rule evaluation.

InstanceType -> (string)

The instance type to deploy a custom rule for profiling a training job.

VolumeSizeInGB -> (integer)

The size, in GB, of the ML storage volume attached to the processing instance.

RuleParameters -> (map)

Runtime configuration for rule container.

key -> (string)

value -> (string)

Shorthand Syntax:

```
RuleConfigurationName=string,LocalPath=string,S3OutputPath=string,RuleEvaluatorImage=string,InstanceType=string,VolumeSizeInGB=integer,RuleParameters={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "RuleConfigurationName": "string",
    "LocalPath": "string",
    "S3OutputPath": "string",
    "RuleEvaluatorImage": "string",
    "InstanceType": "ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.8xlarge"|"ml.r5d.12xlarge"|"ml.r5d.16xlarge"|"ml.r5d.24xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge",
    "VolumeSizeInGB": integer,
    "RuleParameters": {"string": "string"
      ...}
  }
  ...
]
```

`--environment` (map)

The environment variables to set in the Docker container.

### Warning

Do not include any security-sensitive information including account access IDs, secrets, or tokens in any environment fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request environment variable or plain text fields.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--retry-strategy` (structure)

The number of times to retry the job when the job fails due to an `InternalServerError` .

MaximumRetryAttempts -> (integer)

The number of times to retry the job. When the job is retried, itâs `SecondaryStatus` is changed to `STARTING` .

Shorthand Syntax:

```
MaximumRetryAttempts=integer
```

JSON Syntax:

```
{
  "MaximumRetryAttempts": integer
}
```

`--remote-debug-config` (structure)

Configuration for remote debugging. To learn more about the remote debugging functionality of SageMaker, see [Access a training container through Amazon Web Services Systems Manager (SSM) for remote debugging](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-debugging.html) .

EnableRemoteDebug -> (boolean)

If set to True, enables remote debugging.

Shorthand Syntax:

```
EnableRemoteDebug=boolean
```

JSON Syntax:

```
{
  "EnableRemoteDebug": true|false
}
```

`--infra-check-config` (structure)

Contains information about the infrastructure health check configuration for the training job.

EnableInfraCheck -> (boolean)

Enables an infrastructure health check.

Shorthand Syntax:

```
EnableInfraCheck=boolean
```

JSON Syntax:

```
{
  "EnableInfraCheck": true|false
}
```

`--session-chaining-config` (structure)

Contains information about attribute-based access control (ABAC) for the training job.

EnableSessionTagChaining -> (boolean)

Set to `True` to allow SageMaker to extract session tags from a training job creation role and reuse these tags when assuming the training job execution role.

Shorthand Syntax:

```
EnableSessionTagChaining=boolean
```

JSON Syntax:

```
{
  "EnableSessionTagChaining": true|false
}
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

TrainingJobArn -> (string)

The Amazon Resource Name (ARN) of the training job.