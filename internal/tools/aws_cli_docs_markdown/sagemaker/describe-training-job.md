# describe-training-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-training-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-training-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-training-job

## Description

Returns information about a training job.

Some of the attributes below only appear if the training job successfully starts. If the training job fails, `TrainingJobStatus` is `Failed` and, depending on the `FailureReason` , attributes like `TrainingStartTime` , `TrainingTimeInSeconds` , `TrainingEndTime` , and `BillableTimeInSeconds` may not be present in the response.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeTrainingJob)

## Synopsis

```
describe-training-job
--training-job-name <value>
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

The name of the training job.

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

TrainingJobName -> (string)

Name of the model training job.

TrainingJobArn -> (string)

The Amazon Resource Name (ARN) of the training job.

TuningJobArn -> (string)

The Amazon Resource Name (ARN) of the associated hyperparameter tuning job if the training job was launched by a hyperparameter tuning job.

LabelingJobArn -> (string)

The Amazon Resource Name (ARN) of the SageMaker Ground Truth labeling job that created the transform or training job.

AutoMLJobArn -> (string)

The Amazon Resource Name (ARN) of an AutoML job.

ModelArtifacts -> (structure)

Information about the Amazon S3 location that is configured for storing model artifacts.

S3ModelArtifacts -> (string)

The path of the S3 object that contains the model artifacts. For example, `s3://bucket-name/keynameprefix/model.tar.gz` .

TrainingJobStatus -> (string)

The status of the training job.

SageMaker provides the following training job statuses:

- `InProgress` - The training is in progress.
- `Completed` - The training job has completed.
- `Failed` - The training job has failed. To see the reason for the failure, see the `FailureReason` field in the response to a `DescribeTrainingJobResponse` call.
- `Stopping` - The training job is stopping.
- `Stopped` - The training job has stopped.

For more detailed information, see `SecondaryStatus` .

SecondaryStatus -> (string)

Provides detailed information about the state of the training job. For detailed information on the secondary status of the training job, see `StatusMessage` under [SecondaryStatusTransition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SecondaryStatusTransition.html) .

SageMaker provides primary statuses and secondary statuses that apply to each of them:

InProgress

- `Starting` - Starting the training job.
- `Downloading` - An optional stage for algorithms that support `File` training input mode. It indicates that data is being downloaded to the ML storage volumes.
- `Training` - Training is in progress.
- `Interrupted` - The job stopped because the managed spot training instances were interrupted.
- `Uploading` - Training is complete and the model artifacts are being uploaded to the S3 location.

Completed
- `Completed` - The training job has completed.

Failed
- `Failed` - The training job has failed. The reason for the failure is returned in the `FailureReason` field of `DescribeTrainingJobResponse` .

Stopped
- `MaxRuntimeExceeded` - The job stopped because it exceeded the maximum allowed runtime.
- `MaxWaitTimeExceeded` - The job stopped because it exceeded the maximum allowed wait time.
- `Stopped` - The training job has stopped.

Stopping
- `Stopping` - Stopping the training job.

### Warning

Valid values for `SecondaryStatus` are subject to change.

We no longer support the following secondary statuses:

- `LaunchingMLInstances`
- `PreparingTraining`
- `DownloadingTrainingImage`

FailureReason -> (string)

If the training job failed, the reason it failed.

HyperParameters -> (map)

Algorithm-specific parameters.

key -> (string)

value -> (string)

AlgorithmSpecification -> (structure)

Information about the algorithm used for training, and algorithm metadata.

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

RoleArn -> (string)

The Amazon Web Services Identity and Access Management (IAM) role configured for the training job.

InputDataConfig -> (list)

An array of `Channel` objects that describes each data input channel.

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

OutputDataConfig -> (structure)

The S3 path where model artifacts that you configured when creating the job are stored. SageMaker creates subfolders for model artifacts.

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

ResourceConfig -> (structure)

Resources, including ML compute instances and ML storage volumes, that are configured for model training.

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

WarmPoolStatus -> (structure)

The status of the warm pool associated with the training job.

Status -> (string)

The status of the warm pool.

- `InUse` : The warm pool is in use for the training job.
- `Available` : The warm pool is available to reuse for a matching training job.
- `Reused` : The warm pool moved to a matching training job for reuse.
- `Terminated` : The warm pool is no longer available. Warm pools are unavailable if they are terminated by a user, terminated for a patch update, or terminated for exceeding the specified `KeepAlivePeriodInSeconds` .

ResourceRetainedBillableTimeInSeconds -> (integer)

The billable time in seconds used by the warm pool. Billable time refers to the absolute wall-clock time.

Multiply `ResourceRetainedBillableTimeInSeconds` by the number of instances (`InstanceCount` ) in your training cluster to get the total compute time SageMaker bills you if you run warm pool training. The formula is as follows: `ResourceRetainedBillableTimeInSeconds * InstanceCount` .

ReusedByJob -> (string)

The name of the matching training job that reused the warm pool.

VpcConfig -> (structure)

A [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that this training job has access to. For more information, see [Protect Training Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

StoppingCondition -> (structure)

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

CreationTime -> (timestamp)

A timestamp that indicates when the training job was created.

TrainingStartTime -> (timestamp)

Indicates the time when the training job starts on training instances. You are billed for the time interval between this time and the value of `TrainingEndTime` . The start time in CloudWatch Logs might be later than this time. The difference is due to the time it takes to download the training data and to the size of the training container.

TrainingEndTime -> (timestamp)

Indicates the time when the training job ends on training instances. You are billed for the time interval between the value of `TrainingStartTime` and this time. For successful jobs and stopped jobs, this is the time after model artifacts are uploaded. For failed jobs, this is the time when SageMaker detects a job failure.

LastModifiedTime -> (timestamp)

A timestamp that indicates when the status of the training job was last modified.

SecondaryStatusTransitions -> (list)

A history of all of the secondary statuses that the training job has transitioned through.

(structure)

An array element of `SecondaryStatusTransitions` for [DescribeTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html) . It provides additional details about a status that the training job has transitioned through. A training job can be in one of several states, for example, starting, downloading, training, or uploading. Within each state, there are a number of intermediate states. For example, within the starting state, SageMaker could be starting the training job or launching the ML instances. These transitional states are referred to as the jobâs secondary status.

Status -> (string)

Contains a secondary status information from a training job.

Status might be one of the following secondary statuses:

InProgress

- `Starting` - Starting the training job.
- `Downloading` - An optional stage for algorithms that support `File` training input mode. It indicates that data is being downloaded to the ML storage volumes.
- `Training` - Training is in progress.
- `Uploading` - Training is complete and the model artifacts are being uploaded to the S3 location.

Completed
- `Completed` - The training job has completed.

Failed
- `Failed` - The training job has failed. The reason for the failure is returned in the `FailureReason` field of `DescribeTrainingJobResponse` .

Stopped
- `MaxRuntimeExceeded` - The job stopped because it exceeded the maximum allowed runtime.
- `Stopped` - The training job has stopped.

Stopping
- `Stopping` - Stopping the training job.

We no longer support the following secondary statuses:

- `LaunchingMLInstances`
- `PreparingTrainingStack`
- `DownloadingTrainingImage`

StartTime -> (timestamp)

A timestamp that shows when the training job transitioned to the current secondary status state.

EndTime -> (timestamp)

A timestamp that shows when the training job transitioned out of this secondary status state into another secondary status state or when the training job has ended.

StatusMessage -> (string)

A detailed description of the progress within a secondary status.

SageMaker provides secondary statuses and status messages that apply to each of them:

Starting

- Starting the training job.
- Launching requested ML instances.
- Insufficient capacity error from EC2 while launching instances, retrying!
- Launched instance was unhealthy, replacing it!
- Preparing the instances for training.

Training
- Training image download completed. Training in progress.

### Warning

Status messages are subject to change. Therefore, we recommend not including them in code that programmatically initiates actions. For examples, donât use status messages in if statements.

To have an overview of your training jobâs progress, view `TrainingJobStatus` and `SecondaryStatus` in [DescribeTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html) , and `StatusMessage` together. For example, at the start of a training job, you might see the following:

- `TrainingJobStatus` - InProgress
- `SecondaryStatus` - Training
- `StatusMessage` - Downloading the training image

FinalMetricDataList -> (list)

A collection of `MetricData` objects that specify the names, values, and dates and times that the training algorithm emitted to Amazon CloudWatch.

(structure)

The name, value, and date and time of a metric that was emitted to Amazon CloudWatch.

MetricName -> (string)

The name of the metric.

Value -> (float)

The value of the metric.

Timestamp -> (timestamp)

The date and time that the algorithm emitted the metric.

EnableNetworkIsolation -> (boolean)

If you want to allow inbound or outbound network calls, except for calls between peers within a training cluster for distributed training, choose `True` . If you enable network isolation for training jobs that are configured to use a VPC, SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.

EnableInterContainerTrafficEncryption -> (boolean)

To encrypt all communications between ML compute instances in distributed training, choose `True` . Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithms in distributed training.

EnableManagedSpotTraining -> (boolean)

A Boolean indicating whether managed spot training is enabled (`True` ) or not (`False` ).

CheckpointConfig -> (structure)

Contains information about the output location for managed spot training checkpoint data.

S3Uri -> (string)

Identifies the S3 path where you want SageMaker to store checkpoints. For example, `s3://bucket-name/key-name-prefix` .

LocalPath -> (string)

(Optional) The local directory where checkpoints are written. The default directory is `/opt/ml/checkpoints/` .

TrainingTimeInSeconds -> (integer)

The training time in seconds.

BillableTimeInSeconds -> (integer)

The billable time in seconds. Billable time refers to the absolute wall-clock time.

Multiply `BillableTimeInSeconds` by the number of instances (`InstanceCount` ) in your training cluster to get the total compute time SageMaker bills you if you run distributed training. The formula is as follows: `BillableTimeInSeconds * InstanceCount` .

You can calculate the savings from using managed spot training using the formula `(1 - BillableTimeInSeconds / TrainingTimeInSeconds) * 100` . For example, if `BillableTimeInSeconds` is 100 and `TrainingTimeInSeconds` is 500, the savings is 80%.

DebugHookConfig -> (structure)

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

ExperimentConfig -> (structure)

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

DebugRuleConfigurations -> (list)

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

TensorBoardOutputConfig -> (structure)

Configuration of storage locations for the Amazon SageMaker Debugger TensorBoard output data.

LocalPath -> (string)

Path to local storage location for tensorBoard output. Defaults to `/opt/ml/output/tensorboard` .

S3OutputPath -> (string)

Path to Amazon S3 storage location for TensorBoard output.

DebugRuleEvaluationStatuses -> (list)

Evaluation status of Amazon SageMaker Debugger rules for debugging on a training job.

(structure)

Information about the status of the rule evaluation.

RuleConfigurationName -> (string)

The name of the rule configuration.

RuleEvaluationJobArn -> (string)

The Amazon Resource Name (ARN) of the rule evaluation job.

RuleEvaluationStatus -> (string)

Status of the rule evaluation.

StatusDetails -> (string)

Details from the rule evaluation.

LastModifiedTime -> (timestamp)

Timestamp when the rule evaluation status was last modified.

ProfilerConfig -> (structure)

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

ProfilerRuleConfigurations -> (list)

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

ProfilerRuleEvaluationStatuses -> (list)

Evaluation status of Amazon SageMaker Debugger rules for profiling on a training job.

(structure)

Information about the status of the rule evaluation.

RuleConfigurationName -> (string)

The name of the rule configuration.

RuleEvaluationJobArn -> (string)

The Amazon Resource Name (ARN) of the rule evaluation job.

RuleEvaluationStatus -> (string)

Status of the rule evaluation.

StatusDetails -> (string)

Details from the rule evaluation.

LastModifiedTime -> (timestamp)

Timestamp when the rule evaluation status was last modified.

ProfilingStatus -> (string)

Profiling status of a training job.

Environment -> (map)

The environment variables to set in the Docker container.

### Warning

Do not include any security-sensitive information including account access IDs, secrets, or tokens in any environment fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request environment variable or plain text fields.

key -> (string)

value -> (string)

RetryStrategy -> (structure)

The number of times to retry the job when the job fails due to an `InternalServerError` .

MaximumRetryAttempts -> (integer)

The number of times to retry the job. When the job is retried, itâs `SecondaryStatus` is changed to `STARTING` .

RemoteDebugConfig -> (structure)

Configuration for remote debugging. To learn more about the remote debugging functionality of SageMaker, see [Access a training container through Amazon Web Services Systems Manager (SSM) for remote debugging](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-debugging.html) .

EnableRemoteDebug -> (boolean)

If set to True, enables remote debugging.

InfraCheckConfig -> (structure)

Contains information about the infrastructure health check configuration for the training job.

EnableInfraCheck -> (boolean)

Enables an infrastructure health check.