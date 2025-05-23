# describe-algorithmÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-algorithm.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-algorithm.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-algorithm

## Description

Returns a description of the specified algorithm that is in your account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeAlgorithm)

## Synopsis

```
describe-algorithm
--algorithm-name <value>
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

`--algorithm-name` (string)

The name of the algorithm to describe.

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

AlgorithmName -> (string)

The name of the algorithm being described.

AlgorithmArn -> (string)

The Amazon Resource Name (ARN) of the algorithm.

AlgorithmDescription -> (string)

A brief summary about the algorithm.

CreationTime -> (timestamp)

A timestamp specifying when the algorithm was created.

TrainingSpecification -> (structure)

Details about training jobs run by this algorithm.

TrainingImage -> (string)

The Amazon ECR registry path of the Docker image that contains the training algorithm.

TrainingImageDigest -> (string)

An MD5 hash of the training algorithm that identifies the Docker image used for training.

SupportedHyperParameters -> (list)

A list of the `HyperParameterSpecification` objects, that define the supported hyperparameters. This is required if the algorithm supports automatic model tuning.>

(structure)

Defines a hyperparameter to be used by an algorithm.

Name -> (string)

The name of this hyperparameter. The name must be unique.

Description -> (string)

A brief description of the hyperparameter.

Type -> (string)

The type of this hyperparameter. The valid types are `Integer` , `Continuous` , `Categorical` , and `FreeText` .

Range -> (structure)

The allowed range for this hyperparameter.

IntegerParameterRangeSpecification -> (structure)

A `IntegerParameterRangeSpecification` object that defines the possible values for an integer hyperparameter.

MinValue -> (string)

The minimum integer value allowed.

MaxValue -> (string)

The maximum integer value allowed.

ContinuousParameterRangeSpecification -> (structure)

A `ContinuousParameterRangeSpecification` object that defines the possible values for a continuous hyperparameter.

MinValue -> (string)

The minimum floating-point value allowed.

MaxValue -> (string)

The maximum floating-point value allowed.

CategoricalParameterRangeSpecification -> (structure)

A `CategoricalParameterRangeSpecification` object that defines the possible values for a categorical hyperparameter.

Values -> (list)

The allowed categories for the hyperparameter.

(string)

IsTunable -> (boolean)

Indicates whether this hyperparameter is tunable in a hyperparameter tuning job.

IsRequired -> (boolean)

Indicates whether this hyperparameter is required.

DefaultValue -> (string)

The default value for this hyperparameter. If a default value is specified, a hyperparameter cannot be required.

SupportedTrainingInstanceTypes -> (list)

A list of the instance types that this algorithm can use for training.

(string)

SupportsDistributedTraining -> (boolean)

Indicates whether the algorithm supports distributed training. If set to false, buyers canât request more than one instance during training.

MetricDefinitions -> (list)

A list of `MetricDefinition` objects, which are used for parsing metrics generated by the algorithm.

(structure)

Specifies a metric that the training algorithm writes to `stderr` or `stdout` . You can view these logs to understand how your training job performs and check for any errors encountered during training. SageMaker hyperparameter tuning captures all defined metrics. Specify one of the defined metrics to use as an objective metric using the [TuningObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-TuningObjective) parameter in the `HyperParameterTrainingJobDefinition` API to evaluate job performance during hyperparameter tuning.

Name -> (string)

The name of the metric.

Regex -> (string)

A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see [Defining metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) .

TrainingChannels -> (list)

A list of `ChannelSpecification` objects, which specify the input sources to be used by the algorithm.

(structure)

Defines a named input source, called a channel, to be used by an algorithm.

Name -> (string)

The name of the channel.

Description -> (string)

A brief description of the channel.

IsRequired -> (boolean)

Indicates whether the channel is required by the algorithm.

SupportedContentTypes -> (list)

The supported MIME types for the data.

(string)

SupportedCompressionTypes -> (list)

The allowed compression types, if data compression is used.

(string)

SupportedInputModes -> (list)

The allowed input mode, either FILE or PIPE.

In FILE mode, Amazon SageMaker copies the data from the input source onto the local Amazon Elastic Block Store (Amazon EBS) volumes before starting your training algorithm. This is the most commonly used input mode.

In PIPE mode, Amazon SageMaker streams input data from the source directly to your algorithm without using the EBS volume.

(string)

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

SupportedTuningJobObjectiveMetrics -> (list)

A list of the metrics that the algorithm emits that can be used as the objective metric in a hyperparameter tuning job.

(structure)

Defines the objective metric for a hyperparameter tuning job. Hyperparameter tuning uses the value of this metric to evaluate the training jobs it launches, and returns the training job that results in either the highest or lowest value for this metric, depending on the value you specify for the `Type` parameter. If you want to define a custom objective metric, see [Define metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) .

Type -> (string)

Whether to minimize or maximize the objective metric.

MetricName -> (string)

The name of the metric to use for the objective metric.

AdditionalS3DataSource -> (structure)

The additional data source used during the training job.

S3DataType -> (string)

The data type of the additional data source that you specify for use in inference or training.

S3Uri -> (string)

The uniform resource identifier (URI) used to identify an additional data source used in inference or training.

CompressionType -> (string)

The type of compression used for an additional data source used in inference or training. Specify `None` if your additional data source is not compressed.

ETag -> (string)

The ETag associated with S3 URI.

InferenceSpecification -> (structure)

Details about inference jobs that the algorithm runs.

Containers -> (list)

The Amazon ECR registry path of the Docker image that contains the inference code.

(structure)

Describes the Docker container for the model package.

ContainerHostname -> (string)

The DNS host name for the Docker container.

Image -> (string)

The Amazon Elastic Container Registry (Amazon ECR) path where inference code is stored.

If you are using your own custom algorithm instead of an algorithm provided by SageMaker, the inference code must meet SageMaker requirements. SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) .

ImageDigest -> (string)

An MD5 hash of the training algorithm that identifies the Docker image used for training.

ModelDataUrl -> (string)

The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single `gzip` compressed tar archive (`.tar.gz` suffix).

### Note

The model artifacts must be in an S3 bucket that is in the same region as the model package.

ModelDataSource -> (structure)

Specifies the location of ML model data to deploy during endpoint creation.

S3DataSource -> (structure)

Specifies the S3 location of ML model data to deploy.

S3Uri -> (string)

Specifies the S3 path of ML model data to deploy.

S3DataType -> (string)

Specifies the type of ML model data to deploy.

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix as part of the ML model data to deploy. A valid key name prefix identified by `S3Uri` always ends with a forward slash (/).

If you choose `S3Object` , `S3Uri` identifies an object that is the ML model data to deploy.

CompressionType -> (string)

Specifies how the ML model data is prepared.

If you choose `Gzip` and choose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that is a gzip-compressed TAR archive. SageMaker will attempt to decompress and untar the object during model deployment.

If you choose `None` and chooose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that represents an uncompressed ML model to deploy.

If you choose None and choose `S3Prefix` as the value of `S3DataType` , `S3Uri` identifies a key name prefix, under which all objects represents the uncompressed ML model to deploy.

If you choose None, then SageMaker will follow rules below when creating model data files under /opt/ml/model directory for use by your inference code:

- If you choose `S3Object` as the value of `S3DataType` , then SageMaker will split the key of the S3 object referenced by `S3Uri` by slash (/), and use the last part as the filename of the file holding the content of the S3 object.
- If you choose `S3Prefix` as the value of `S3DataType` , then for each S3 object under the key name pefix referenced by `S3Uri` , SageMaker will trim its key by the prefix, and use the remainder as the path (relative to `/opt/ml/model` ) of the file holding the content of the S3 object. SageMaker will split the remainder by slash (/), using intermediate parts as directory names and the last part as filename of the file holding the content of the S3 object.
- Do not use any of the following as file names or directory names:
- An empty or blank string
- A string which contains null bytes
- A string longer than 255 bytes
- A single dot (`.` )
- A double dot (`..` )
- Ambiguous file names will result in model deployment failure. For example, if your uncompressed ML model consists of two S3 objects `s3://mybucket/model/weights` and `s3://mybucket/model/weights/part1` and you specify `s3://mybucket/model/` as the value of `S3Uri` and `S3Prefix` as the value of `S3DataType` , then it will result in name clash between `/opt/ml/model/weights` (a regular file) and `/opt/ml/model/weights/` (a directory).
- Do not organize the model artifacts in [S3 console using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) . When you create a folder in S3 console, S3 creates a 0-byte object with a key set to the folder name you provide. They key of the 0-byte object ends with a slash (/) which violates SageMaker restrictions on model artifact file names, leading to model deployment failure.

ModelAccessConfig -> (structure)

Specifies the access configuration file for the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` . You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

Configuration information for hub access.

HubContentArn -> (string)

The ARN of the hub content for which deployment access is allowed.

ManifestS3Uri -> (string)

The Amazon S3 URI of the manifest file. The manifest file is a CSV file that stores the artifact locations.

ETag -> (string)

The ETag associated with S3 URI.

ManifestEtag -> (string)

The ETag associated with Manifest S3 URI.

ProductId -> (string)

The Amazon Web Services Marketplace product ID of the model package.

Environment -> (map)

The environment variables to set in the Docker container. Each key and value in the `Environment` string to string map can have length of up to 1024. We support up to 16 entries in the map.

key -> (string)

value -> (string)

ModelInput -> (structure)

A structure with Model Input details.

DataInputConfig -> (string)

The input configuration object for the model.

Framework -> (string)

The machine learning framework of the model package container image.

FrameworkVersion -> (string)

The framework version of the Model Package Container Image.

NearestModelName -> (string)

The name of a pre-trained machine learning benchmarked by Amazon SageMaker Inference Recommender model that matches your model. You can find a list of benchmarked models by calling `ListModelMetadata` .

AdditionalS3DataSource -> (structure)

The additional data source that is used during inference in the Docker container for your model package.

S3DataType -> (string)

The data type of the additional data source that you specify for use in inference or training.

S3Uri -> (string)

The uniform resource identifier (URI) used to identify an additional data source used in inference or training.

CompressionType -> (string)

The type of compression used for an additional data source used in inference or training. Specify `None` if your additional data source is not compressed.

ETag -> (string)

The ETag associated with S3 URI.

ModelDataETag -> (string)

The ETag associated with Model Data URL.

SupportedTransformInstanceTypes -> (list)

A list of the instance types on which a transformation job can be run or on which an endpoint can be deployed.

This parameter is required for unversioned models, and optional for versioned models.

(string)

SupportedRealtimeInferenceInstanceTypes -> (list)

A list of the instance types that are used to generate inferences in real-time.

This parameter is required for unversioned models, and optional for versioned models.

(string)

SupportedContentTypes -> (list)

The supported MIME types for the input data.

(string)

SupportedResponseMIMETypes -> (list)

The supported MIME types for the output data.

(string)

ValidationSpecification -> (structure)

Details about configurations for one or more training jobs that SageMaker runs to test the algorithm.

ValidationRole -> (string)

The IAM roles that SageMaker uses to run the training jobs.

ValidationProfiles -> (list)

An array of `AlgorithmValidationProfile` objects, each of which specifies a training job and batch transform job that SageMaker runs to validate your algorithm.

(structure)

Defines a training job and a batch transform job that SageMaker runs to validate your algorithm.

The data provided in the validation profile is made available to your buyers on Amazon Web Services Marketplace.

ProfileName -> (string)

The name of the profile for the algorithm. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).

TrainingJobDefinition -> (structure)

The `TrainingJobDefinition` object that describes the training job that SageMaker runs to validate your algorithm.

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

HyperParameters -> (map)

The hyperparameters used for the training job.

key -> (string)

value -> (string)

InputDataConfig -> (list)

An array of `Channel` objects, each of which specifies an input source.

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

the path to the S3 bucket where you want to store model artifacts. SageMaker creates subfolders for the artifacts.

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

The resources, including the ML compute instances and ML storage volumes, to use for model training.

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

StoppingCondition -> (structure)

Specifies a limit to how long a model training job can run. It also specifies how long a managed Spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.

To stop a job, SageMaker sends the algorithm the SIGTERM signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts.

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

TransformJobDefinition -> (structure)

The `TransformJobDefinition` object that describes the transform job that SageMaker runs to validate your algorithm.

MaxConcurrentTransforms -> (integer)

The maximum number of parallel requests that can be sent to each instance in a transform job. The default value is 1.

MaxPayloadInMB -> (integer)

The maximum payload size allowed, in MB. A payload is the data portion of a record (without metadata).

BatchStrategy -> (string)

A string that determines the number of records included in a single mini-batch.

`SingleRecord` means only one record is used per mini-batch. `MultiRecord` means a mini-batch is set to contain as many records that can fit within the `MaxPayloadInMB` limit.

Environment -> (map)

The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.

key -> (string)

value -> (string)

TransformInput -> (structure)

A description of the input source and the way the transform job consumes it.

DataSource -> (structure)

Describes the location of the channel data, which is, the S3 location of the input data that the model can consume.

S3DataSource -> (structure)

The S3 location of the data source that is associated with a channel.

S3DataType -> (string)

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform.

If you choose `ManifestFile` , `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform.

The following values are compatible: `ManifestFile` , `S3Prefix`

The following value is not compatible: `AugmentedManifestFile`

S3Uri -> (string)

Depending on the value specified for the `S3DataType` , identifies either a key name prefix or a manifest. For example:

- A key name prefix might look like this: `s3://bucketname/exampleprefix/` .
- A manifest might look like this: `s3://bucketname/example.manifest`   The manifest is an S3 object which is a JSON file with the following format:   `[ {"prefix": "s3://customer_bucket/some/prefix/"},` `"relative/path/to/custdata-1",` `"relative/path/custdata-2",` `...` `"relative/path/custdata-N"` `]`   The preceding JSON matches the following `S3Uris` :   `s3://customer_bucket/some/prefix/relative/path/to/custdata-1` `s3://customer_bucket/some/prefix/relative/path/custdata-2` `...` `s3://customer_bucket/some/prefix/relative/path/custdata-N`   The complete set of `S3Uris` in this manifest constitutes the input data for the channel for this datasource. The object that each `S3Uris` points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.

ContentType -> (string)

The multipurpose internet mail extension (MIME) type of the data. Amazon SageMaker uses the MIME type with each http call to transfer data to the transform job.

CompressionType -> (string)

If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is `None` .

SplitType -> (string)

The method to use to split the transform jobâs data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for `SplitType` is `None` , which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to `Line` to split records on a newline character boundary. `SplitType` also supports a number of record-oriented binary data formats. Currently, the supported record formats are:

- RecordIO
- TFRecord

When splitting is enabled, the size of a mini-batch depends on the values of the `BatchStrategy` and `MaxPayloadInMB` parameters. When the value of `BatchStrategy` is `MultiRecord` , Amazon SageMaker sends the maximum number of records in each request, up to the `MaxPayloadInMB` limit. If the value of `BatchStrategy` is `SingleRecord` , Amazon SageMaker sends individual records in each request.

### Note

Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of `BatchStrategy` is set to `SingleRecord` . Padding is not removed if the value of `BatchStrategy` is set to `MultiRecord` .

For more information about `RecordIO` , see [Create a Dataset Using RecordIO](https://mxnet.apache.org/api/faq/recordio) in the MXNet documentation. For more information about `TFRecord` , see [Consuming TFRecord data](https://www.tensorflow.org/guide/data#consuming_tfrecord_data) in the TensorFlow documentation.

TransformOutput -> (structure)

Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.

S3OutputPath -> (string)

The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, `s3://bucket-name/key-name-prefix` .

For every S3 object used as input for the transform job, batch transform stores the transformed data with an .``out`` suffix in a corresponding subfolder in the location in the output prefix. For example, for the input data stored at `s3://bucket-name/input-name-prefix/dataset01/data.csv` , batch transform stores the transformed data at `s3://bucket-name/output-name-prefix/input-name-prefix/data.csv.out` . Batch transform doesnât upload partially processed objects. For an input S3 object that contains multiple records, it creates an .``out`` file only if the transform job succeeds on the entire file. When the input contains multiple S3 objects, the batch transform job processes the listed S3 objects and uploads only the output for successfully processed objects. If any object fails in the transform job batch transform marks the job as failed to prompt investigation.

Accept -> (string)

The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.

AssembleWith -> (string)

Defines how to assemble the results of the transform job as a single S3 object. Choose a format that is most convenient to you. To concatenate the results in binary format, specify `None` . To add a newline character at the end of every transformed record, specify `Line` .

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The `KmsKeyId` can be any of the following formats:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`

If you donât provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your roleâs account. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide.*

The KMS key policy must grant permission to the IAM role that you specify in your [CreateModel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModel.html) request. For more information, see [Using Key Policies in Amazon Web Services KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *Amazon Web Services Key Management Service Developer Guide* .

TransformResources -> (structure)

Identifies the ML compute instances for the transform job.

InstanceType -> (string)

The ML compute instance type for the transform job. If you are using built-in algorithms to transform moderately sized datasets, we recommend using ml.m4.xlarge or `ml.m5.large` instance types.

InstanceCount -> (integer)

The number of ML compute instances to use in the transform job. The default value is `1` , and the maximum is `100` . For distributed transform jobs, specify a value greater than `1` .

VolumeKmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt model data on the storage volume attached to the ML compute instance(s) that run the batch transform job.

### Note

Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You canât request a `VolumeKmsKeyId` when using an instance type with local storage.

For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes) .

For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) .

The `VolumeKmsKeyId` can be any of the following formats:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`

TransformAmiVersion -> (string)

Specifies an option from a collection of preconfigured Amazon Machine Image (AMI) images. Each image is configured by Amazon Web Services with a set of software and driver versions.

al2-ami-sagemaker-batch-gpu-470

- Accelerator: GPU
- NVIDIA driver version: 470

al2-ami-sagemaker-batch-gpu-535
- Accelerator: GPU
- NVIDIA driver version: 535

AlgorithmStatus -> (string)

The current status of the algorithm.

AlgorithmStatusDetails -> (structure)

Details about the current status of the algorithm.

ValidationStatuses -> (list)

The status of algorithm validation.

(structure)

Represents the overall status of an algorithm.

Name -> (string)

The name of the algorithm for which the overall status is being reported.

Status -> (string)

The current status.

FailureReason -> (string)

if the overall status is `Failed` , the reason for the failure.

ImageScanStatuses -> (list)

The status of the scan of the algorithmâs Docker image container.

(structure)

Represents the overall status of an algorithm.

Name -> (string)

The name of the algorithm for which the overall status is being reported.

Status -> (string)

The current status.

FailureReason -> (string)

if the overall status is `Failed` , the reason for the failure.

ProductId -> (string)

The product identifier of the algorithm.

CertifyForMarketplace -> (boolean)

Whether the algorithm is certified to be listed in Amazon Web Services Marketplace.