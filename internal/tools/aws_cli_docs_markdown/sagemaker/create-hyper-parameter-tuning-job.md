# create-hyper-parameter-tuning-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-hyper-parameter-tuning-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-hyper-parameter-tuning-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-hyper-parameter-tuning-job

## Description

Starts a hyperparameter tuning job. A hyperparameter tuning job finds the best version of a model by running many training jobs on your dataset using the algorithm you choose and values for hyperparameters within ranges that you specify. It then chooses the hyperparameter values that result in a model that performs the best, as measured by an objective metric that you choose.

A hyperparameter tuning job automatically creates Amazon SageMaker experiments, trials, and trial components for each training job that it runs. You can view these entities in Amazon SageMaker Studio. For more information, see [View Experiments, Trials, and Trial Components](https://docs.aws.amazon.com/sagemaker/latest/dg/experiments-view-compare.html#experiments-view) .

### Warning

Do not include any security-sensitive information including account access IDs, secrets, or tokens in any hyperparameter fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by any security-sensitive information included in the request hyperparameter variable or plain text fields..

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateHyperParameterTuningJob)

## Synopsis

```
create-hyper-parameter-tuning-job
--hyper-parameter-tuning-job-name <value>
--hyper-parameter-tuning-job-config <value>
[--training-job-definition <value>]
[--training-job-definitions <value>]
[--warm-start-config <value>]
[--tags <value>]
[--autotune <value>]
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

`--hyper-parameter-tuning-job-name` (string)

The name of the tuning job. This name is the prefix for the names of all training jobs that this tuning job launches. The name must be unique within the same Amazon Web Services account and Amazon Web Services Region. The name must have 1 to 32 characters. Valid characters are a-z, A-Z, 0-9, and : + = @ _ % - (hyphen). The name is not case sensitive.

`--hyper-parameter-tuning-job-config` (structure)

The [HyperParameterTuningJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html) object that describes the tuning job, including the search strategy, the objective metric used to evaluate training jobs, ranges of parameters to search, and resource limits for the tuning job. For more information, see [How Hyperparameter Tuning Works](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html) .

Strategy -> (string)

Specifies how hyperparameter tuning chooses the combinations of hyperparameter values to use for the training job it launches. For information about search strategies, see [How Hyperparameter Tuning Works](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html) .

StrategyConfig -> (structure)

The configuration for the `Hyperband` optimization strategy. This parameter should be provided only if `Hyperband` is selected as the strategy for `HyperParameterTuningJobConfig` .

HyperbandStrategyConfig -> (structure)

The configuration for the object that specifies the `Hyperband` strategy. This parameter is only supported for the `Hyperband` selection for `Strategy` within the `HyperParameterTuningJobConfig` API.

MinResource -> (integer)

The minimum number of resources (such as epochs) that can be used by a training job launched by a hyperparameter tuning job. If the value for `MinResource` has not been reached, the training job is not stopped by `Hyperband` .

MaxResource -> (integer)

The maximum number of resources (such as epochs) that can be used by a training job launched by a hyperparameter tuning job. Once a job reaches the `MaxResource` value, it is stopped. If a value for `MaxResource` is not provided, and `Hyperband` is selected as the hyperparameter tuning strategy, `HyperbandTraining` attempts to infer `MaxResource` from the following keys (if present) in [StaticsHyperParameters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-StaticHyperParameters) :

- `epochs`
- `numepochs`
- `n-epochs`
- `n_epochs`
- `num_epochs`

If `HyperbandStrategyConfig` is unable to infer a value for `MaxResource` , it generates a validation error. The maximum value is 20,000 epochs. All metrics that correspond to an objective metric are used to derive [early stopping decisions](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html) . For [distributed](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html) training jobs, ensure that duplicate metrics are not printed in the logs across the individual nodes in a training job. If multiple nodes are publishing duplicate or incorrect metrics, training jobs may make an incorrect stopping decision and stop the job prematurely.

HyperParameterTuningJobObjective -> (structure)

The [HyperParameterTuningJobObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobObjective.html) specifies the objective metric used to evaluate the performance of training jobs launched by this tuning job.

Type -> (string)

Whether to minimize or maximize the objective metric.

MetricName -> (string)

The name of the metric to use for the objective metric.

ResourceLimits -> (structure)

The [ResourceLimits](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html) object that specifies the maximum number of training and parallel training jobs that can be used for this hyperparameter tuning job.

MaxNumberOfTrainingJobs -> (integer)

The maximum number of training jobs that a hyperparameter tuning job can launch.

MaxParallelTrainingJobs -> (integer)

The maximum number of concurrent training jobs that a hyperparameter tuning job can launch.

MaxRuntimeInSeconds -> (integer)

The maximum time in seconds that a hyperparameter tuning job can run.

ParameterRanges -> (structure)

The [ParameterRanges](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ParameterRanges.html) object that specifies the ranges of hyperparameters that this tuning job searches over to find the optimal configuration for the highest model performance against your chosen objective metric.

IntegerParameterRanges -> (list)

The array of [IntegerParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IntegerParameterRange.html) objects that specify ranges of integer hyperparameters that a hyperparameter tuning job searches.

(structure)

For a hyperparameter of the integer type, specifies the range that a hyperparameter tuning job searches.

Name -> (string)

The name of the hyperparameter to search.

MinValue -> (string)

The minimum value of the hyperparameter to search.

MaxValue -> (string)

The maximum value of the hyperparameter to search.

ScalingType -> (string)

The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see [Hyperparameter Scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type) . One of the following values:

Auto

SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.

Linear

Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.

Logarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.

Logarithmic scaling works only for ranges that have only values greater than 0.

ContinuousParameterRanges -> (list)

The array of [ContinuousParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContinuousParameterRange.html) objects that specify ranges of continuous hyperparameters that a hyperparameter tuning job searches.

(structure)

A list of continuous hyperparameters to tune.

Name -> (string)

The name of the continuous hyperparameter to tune.

MinValue -> (string)

The minimum value for the hyperparameter. The tuning job uses floating-point values between this value and `MaxValue` for tuning.

MaxValue -> (string)

The maximum value for the hyperparameter. The tuning job uses floating-point values between `MinValue` value and this value for tuning.

ScalingType -> (string)

The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see [Hyperparameter Scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type) . One of the following values:

Auto

SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.

Linear

Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.

Logarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.

Logarithmic scaling works only for ranges that have only values greater than 0.

ReverseLogarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a reverse logarithmic scale.

Reverse logarithmic scaling works only for ranges that are entirely within the range 0<=x<1.0.

CategoricalParameterRanges -> (list)

The array of [CategoricalParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CategoricalParameterRange.html) objects that specify ranges of categorical hyperparameters that a hyperparameter tuning job searches.

(structure)

A list of categorical hyperparameters to tune.

Name -> (string)

The name of the categorical hyperparameter to tune.

Values -> (list)

A list of the categories for the hyperparameter.

(string)

AutoParameters -> (list)

A list containing hyperparameter names and example values to be used by Autotune to determine optimal ranges for your tuning job.

(structure)

The name and an example value of the hyperparameter that you want to use in Autotune. If Automatic model tuning (AMT) determines that your hyperparameter is eligible for Autotune, an optimal hyperparameter range is selected for you.

Name -> (string)

The name of the hyperparameter to optimize using Autotune.

ValueHint -> (string)

An example value of the hyperparameter to optimize using Autotune.

TrainingJobEarlyStoppingType -> (string)

Specifies whether to use early stopping for training jobs launched by the hyperparameter tuning job. Because the `Hyperband` strategy has its own advanced internal early stopping mechanism, `TrainingJobEarlyStoppingType` must be `OFF` to use `Hyperband` . This parameter can take on one of the following values (the default value is `OFF` ):

OFF

Training jobs launched by the hyperparameter tuning job do not use early stopping.

AUTO

SageMaker stops training jobs launched by the hyperparameter tuning job when they are unlikely to perform better than previously completed training jobs. For more information, see [Stop Training Jobs Early](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html) .

TuningJobCompletionCriteria -> (structure)

The tuning jobâs completion criteria.

TargetObjectiveMetricValue -> (float)

The value of the objective metric.

BestObjectiveNotImproving -> (structure)

A flag to stop your hyperparameter tuning job if model performance fails to improve as evaluated against an objective function.

MaxNumberOfTrainingJobsNotImproving -> (integer)

The number of training jobs that have failed to improve model performance by 1% or greater over prior training jobs as evaluated against an objective function.

ConvergenceDetected -> (structure)

A flag to top your hyperparameter tuning job if automatic model tuning (AMT) has detected that your model has converged as evaluated against your objective function.

CompleteOnConvergence -> (string)

A flag to stop a tuning job once AMT has detected that the job has converged.

RandomSeed -> (integer)

A value used to initialize a pseudo-random number generator. Setting a random seed and using the same seed later for the same tuning job will allow hyperparameter optimization to find more a consistent hyperparameter configuration between the two runs.

JSON Syntax:

```
{
  "Strategy": "Bayesian"|"Random"|"Hyperband"|"Grid",
  "StrategyConfig": {
    "HyperbandStrategyConfig": {
      "MinResource": integer,
      "MaxResource": integer
    }
  },
  "HyperParameterTuningJobObjective": {
    "Type": "Maximize"|"Minimize",
    "MetricName": "string"
  },
  "ResourceLimits": {
    "MaxNumberOfTrainingJobs": integer,
    "MaxParallelTrainingJobs": integer,
    "MaxRuntimeInSeconds": integer
  },
  "ParameterRanges": {
    "IntegerParameterRanges": [
      {
        "Name": "string",
        "MinValue": "string",
        "MaxValue": "string",
        "ScalingType": "Auto"|"Linear"|"Logarithmic"|"ReverseLogarithmic"
      }
      ...
    ],
    "ContinuousParameterRanges": [
      {
        "Name": "string",
        "MinValue": "string",
        "MaxValue": "string",
        "ScalingType": "Auto"|"Linear"|"Logarithmic"|"ReverseLogarithmic"
      }
      ...
    ],
    "CategoricalParameterRanges": [
      {
        "Name": "string",
        "Values": ["string", ...]
      }
      ...
    ],
    "AutoParameters": [
      {
        "Name": "string",
        "ValueHint": "string"
      }
      ...
    ]
  },
  "TrainingJobEarlyStoppingType": "Off"|"Auto",
  "TuningJobCompletionCriteria": {
    "TargetObjectiveMetricValue": float,
    "BestObjectiveNotImproving": {
      "MaxNumberOfTrainingJobsNotImproving": integer
    },
    "ConvergenceDetected": {
      "CompleteOnConvergence": "Disabled"|"Enabled"
    }
  },
  "RandomSeed": integer
}
```

`--training-job-definition` (structure)

The [HyperParameterTrainingJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html) object that describes the training jobs that this tuning job launches, including static hyperparameters, input data configuration, output data configuration, resource configuration, and stopping condition.

DefinitionName -> (string)

The job definition name.

TuningObjective -> (structure)

Defines the objective metric for a hyperparameter tuning job. Hyperparameter tuning uses the value of this metric to evaluate the training jobs it launches, and returns the training job that results in either the highest or lowest value for this metric, depending on the value you specify for the `Type` parameter. If you want to define a custom objective metric, see [Define metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) .

Type -> (string)

Whether to minimize or maximize the objective metric.

MetricName -> (string)

The name of the metric to use for the objective metric.

HyperParameterRanges -> (structure)

Specifies ranges of integer, continuous, and categorical hyperparameters that a hyperparameter tuning job searches. The hyperparameter tuning job launches training jobs with hyperparameter values within these ranges to find the combination of values that result in the training job with the best performance as measured by the objective metric of the hyperparameter tuning job.

### Note

The maximum number of items specified for `Array Members` refers to the maximum number of hyperparameters for each range and also the maximum for the hyperparameter tuning job itself. That is, the sum of the number of hyperparameters for all the ranges canât exceed the maximum number specified.

IntegerParameterRanges -> (list)

The array of [IntegerParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IntegerParameterRange.html) objects that specify ranges of integer hyperparameters that a hyperparameter tuning job searches.

(structure)

For a hyperparameter of the integer type, specifies the range that a hyperparameter tuning job searches.

Name -> (string)

The name of the hyperparameter to search.

MinValue -> (string)

The minimum value of the hyperparameter to search.

MaxValue -> (string)

The maximum value of the hyperparameter to search.

ScalingType -> (string)

The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see [Hyperparameter Scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type) . One of the following values:

Auto

SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.

Linear

Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.

Logarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.

Logarithmic scaling works only for ranges that have only values greater than 0.

ContinuousParameterRanges -> (list)

The array of [ContinuousParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContinuousParameterRange.html) objects that specify ranges of continuous hyperparameters that a hyperparameter tuning job searches.

(structure)

A list of continuous hyperparameters to tune.

Name -> (string)

The name of the continuous hyperparameter to tune.

MinValue -> (string)

The minimum value for the hyperparameter. The tuning job uses floating-point values between this value and `MaxValue` for tuning.

MaxValue -> (string)

The maximum value for the hyperparameter. The tuning job uses floating-point values between `MinValue` value and this value for tuning.

ScalingType -> (string)

The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see [Hyperparameter Scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type) . One of the following values:

Auto

SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.

Linear

Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.

Logarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.

Logarithmic scaling works only for ranges that have only values greater than 0.

ReverseLogarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a reverse logarithmic scale.

Reverse logarithmic scaling works only for ranges that are entirely within the range 0<=x<1.0.

CategoricalParameterRanges -> (list)

The array of [CategoricalParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CategoricalParameterRange.html) objects that specify ranges of categorical hyperparameters that a hyperparameter tuning job searches.

(structure)

A list of categorical hyperparameters to tune.

Name -> (string)

The name of the categorical hyperparameter to tune.

Values -> (list)

A list of the categories for the hyperparameter.

(string)

AutoParameters -> (list)

A list containing hyperparameter names and example values to be used by Autotune to determine optimal ranges for your tuning job.

(structure)

The name and an example value of the hyperparameter that you want to use in Autotune. If Automatic model tuning (AMT) determines that your hyperparameter is eligible for Autotune, an optimal hyperparameter range is selected for you.

Name -> (string)

The name of the hyperparameter to optimize using Autotune.

ValueHint -> (string)

An example value of the hyperparameter to optimize using Autotune.

StaticHyperParameters -> (map)

Specifies the values of hyperparameters that do not change for the tuning job.

key -> (string)

value -> (string)

AlgorithmSpecification -> (structure)

The [HyperParameterAlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterAlgorithmSpecification.html) object that specifies the resource algorithm to use for the training jobs that the tuning job launches.

TrainingImage -> (string)

The registry path of the Docker image that contains the training algorithm. For information about Docker registry paths for built-in algorithms, see [Algorithms Provided by Amazon SageMaker: Common Parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html) . SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) .

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

AlgorithmName -> (string)

The name of the resource algorithm to use for the hyperparameter tuning job. If you specify a value for this parameter, do not specify a value for `TrainingImage` .

MetricDefinitions -> (list)

An array of [MetricDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDefinition.html) objects that specify the metrics that the algorithm emits.

(structure)

Specifies a metric that the training algorithm writes to `stderr` or `stdout` . You can view these logs to understand how your training job performs and check for any errors encountered during training. SageMaker hyperparameter tuning captures all defined metrics. Specify one of the defined metrics to use as an objective metric using the [TuningObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-TuningObjective) parameter in the `HyperParameterTrainingJobDefinition` API to evaluate job performance during hyperparameter tuning.

Name -> (string)

The name of the metric.

Regex -> (string)

A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see [Defining metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) .

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role associated with the training jobs that the tuning job launches.

InputDataConfig -> (list)

An array of [Channel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Channel.html) objects that specify the input for the training jobs that the tuning job launches.

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

VpcConfig -> (structure)

The [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that you want the training jobs that this hyperparameter tuning job launches to connect to. Control access to and from your training container by configuring the VPC. For more information, see [Protect Training Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

OutputDataConfig -> (structure)

Specifies the path to the Amazon S3 bucket where you store model artifacts from the training jobs that the tuning job launches.

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

The resources, including the compute instances and storage volumes, to use for the training jobs that the tuning job launches.

Storage volumes store model artifacts and incremental states. Training algorithms might also use storage volumes for scratch space. If you want SageMaker to use the storage volume to store the training data, choose `File` as the `TrainingInputMode` in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.

### Note

If you want to use hyperparameter optimization with instance type flexibility, use `HyperParameterTuningResourceConfig` instead.

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

HyperParameterTuningResourceConfig -> (structure)

The configuration for the hyperparameter tuning resources, including the compute instances and storage volumes, used for training jobs launched by the tuning job. By default, storage volumes hold model artifacts and incremental states. Choose `File` for `TrainingInputMode` in the `AlgorithmSpecification` parameter to additionally store training data in the storage volume (optional).

InstanceType -> (string)

The instance type used to run hyperparameter optimization tuning jobs. See [descriptions of instance types](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-instance-types.html) for more information.

InstanceCount -> (integer)

The number of compute instances of type `InstanceType` to use. For [distributed training](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-use-api.html) , select a value greater than 1.

VolumeSizeInGB -> (integer)

The volume size in GB for the storage volume to be used in processing hyperparameter optimization jobs (optional). These volumes store model artifacts, incremental states and optionally, scratch space for training algorithms. Do not provide a value for this parameter if a value for `InstanceConfigs` is also specified.

Some instance types have a fixed total local storage size. If you select one of these instances for training, `VolumeSizeInGB` cannot be greater than this total size. For a list of instance types with local instance storage and their sizes, see [instance store volumes](http://aws.amazon.com/releasenotes/host-instance-storage-volumes-table/) .

### Note

SageMaker supports only the [General Purpose SSD (gp2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) storage volume type.

VolumeKmsKeyId -> (string)

A key used by Amazon Web Services Key Management Service to encrypt data on the storage volume attached to the compute instances used to run the training job. You can use either of the following formats to specify a key.

KMS Key ID:

`"1234abcd-12ab-34cd-56ef-1234567890ab"`

Amazon Resource Name (ARN) of a KMS key:

`"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

Some instances use local storage, which use a [hardware module to encrypt](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) storage volumes. If you choose one of these instance types, you cannot request a `VolumeKmsKeyId` . For a list of instance types that use local storage, see [instance store volumes](http://aws.amazon.com/releasenotes/host-instance-storage-volumes-table/) . For more information about Amazon Web Services Key Management Service, see [KMS encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-kms-permissions.html) for more information.

AllocationStrategy -> (string)

The strategy that determines the order of preference for resources specified in `InstanceConfigs` used in hyperparameter optimization.

InstanceConfigs -> (list)

A list containing the configuration(s) for one or more resources for processing hyperparameter jobs. These resources include compute instances and storage volumes to use in model training jobs launched by hyperparameter tuning jobs. The `AllocationStrategy` controls the order in which multiple configurations provided in `InstanceConfigs` are used.

### Note

If you only want to use a single instance configuration inside the `HyperParameterTuningResourceConfig` API, do not provide a value for `InstanceConfigs` . Instead, use `InstanceType` , `VolumeSizeInGB` and `InstanceCount` . If you use `InstanceConfigs` , do not provide values for `InstanceType` , `VolumeSizeInGB` or `InstanceCount` .

(structure)

The configuration for hyperparameter tuning resources for use in training jobs launched by the tuning job. These resources include compute instances and storage volumes. Specify one or more compute instance configurations and allocation strategies to select resources (optional).

InstanceType -> (string)

The instance type used for processing of hyperparameter optimization jobs. Choose from general purpose (no GPUs) instance types: ml.m5.xlarge, ml.m5.2xlarge, and ml.m5.4xlarge or compute optimized (no GPUs) instance types: ml.c5.xlarge and ml.c5.2xlarge. For more information about instance types, see [instance type descriptions](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-instance-types.html) .

InstanceCount -> (integer)

The number of instances of the type specified by `InstanceType` . Choose an instance count larger than 1 for distributed training algorithms. See [Step 2: Launch a SageMaker Distributed Training Job Using the SageMaker Python SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-use-api.html) for more information.

VolumeSizeInGB -> (integer)

The volume size in GB of the data to be processed for hyperparameter optimization (optional).

StoppingCondition -> (structure)

Specifies a limit to how long a model hyperparameter training job can run. It also specifies how long a managed spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.

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

EnableNetworkIsolation -> (boolean)

Isolates the training container. No inbound or outbound network calls can be made, except for calls between peers within a training cluster for distributed training. If network isolation is used for training jobs that are configured to use a VPC, SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.

EnableInterContainerTrafficEncryption -> (boolean)

To encrypt all communications between ML compute instances in distributed training, choose `True` . Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training.

EnableManagedSpotTraining -> (boolean)

A Boolean indicating whether managed spot training is enabled (`True` ) or not (`False` ).

CheckpointConfig -> (structure)

Contains information about the output location for managed spot training checkpoint data.

S3Uri -> (string)

Identifies the S3 path where you want SageMaker to store checkpoints. For example, `s3://bucket-name/key-name-prefix` .

LocalPath -> (string)

(Optional) The local directory where checkpoints are written. The default directory is `/opt/ml/checkpoints/` .

RetryStrategy -> (structure)

The number of times to retry the job when the job fails due to an `InternalServerError` .

MaximumRetryAttempts -> (integer)

The number of times to retry the job. When the job is retried, itâs `SecondaryStatus` is changed to `STARTING` .

Environment -> (map)

An environment variable that you can pass into the SageMaker [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API. You can use an existing [environment variable from the training container](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html#sagemaker-CreateTrainingJob-request-Environment) or use your own. See [Define metrics and variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) for more information.

### Note

The maximum number of items specified for `Map Entries` refers to the maximum number of environment variables for each `TrainingJobDefinition` and also the maximum for the hyperparameter tuning job itself. That is, the sum of the number of environment variables for all the training job definitions canât exceed the maximum number specified.

key -> (string)

value -> (string)

JSON Syntax:

```
{
  "DefinitionName": "string",
  "TuningObjective": {
    "Type": "Maximize"|"Minimize",
    "MetricName": "string"
  },
  "HyperParameterRanges": {
    "IntegerParameterRanges": [
      {
        "Name": "string",
        "MinValue": "string",
        "MaxValue": "string",
        "ScalingType": "Auto"|"Linear"|"Logarithmic"|"ReverseLogarithmic"
      }
      ...
    ],
    "ContinuousParameterRanges": [
      {
        "Name": "string",
        "MinValue": "string",
        "MaxValue": "string",
        "ScalingType": "Auto"|"Linear"|"Logarithmic"|"ReverseLogarithmic"
      }
      ...
    ],
    "CategoricalParameterRanges": [
      {
        "Name": "string",
        "Values": ["string", ...]
      }
      ...
    ],
    "AutoParameters": [
      {
        "Name": "string",
        "ValueHint": "string"
      }
      ...
    ]
  },
  "StaticHyperParameters": {"string": "string"
    ...},
  "AlgorithmSpecification": {
    "TrainingImage": "string",
    "TrainingInputMode": "Pipe"|"File"|"FastFile",
    "AlgorithmName": "string",
    "MetricDefinitions": [
      {
        "Name": "string",
        "Regex": "string"
      }
      ...
    ]
  },
  "RoleArn": "string",
  "InputDataConfig": [
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
  ],
  "VpcConfig": {
    "SecurityGroupIds": ["string", ...],
    "Subnets": ["string", ...]
  },
  "OutputDataConfig": {
    "KmsKeyId": "string",
    "S3OutputPath": "string",
    "CompressionType": "GZIP"|"NONE"
  },
  "ResourceConfig": {
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
  },
  "HyperParameterTuningResourceConfig": {
    "InstanceType": "ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.p3dn.24xlarge"|"ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.p5.48xlarge"|"ml.p5e.48xlarge"|"ml.p5en.48xlarge"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.c5n.xlarge"|"ml.c5n.2xlarge"|"ml.c5n.4xlarge"|"ml.c5n.9xlarge"|"ml.c5n.18xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.16xlarge"|"ml.g6.12xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.16xlarge"|"ml.g6e.12xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.trn2.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.8xlarge"|"ml.c6i.4xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.8xlarge"|"ml.r5d.12xlarge"|"ml.r5d.16xlarge"|"ml.r5d.24xlarge"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge",
    "InstanceCount": integer,
    "VolumeSizeInGB": integer,
    "VolumeKmsKeyId": "string",
    "AllocationStrategy": "Prioritized",
    "InstanceConfigs": [
      {
        "InstanceType": "ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.p3dn.24xlarge"|"ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.p5.48xlarge"|"ml.p5e.48xlarge"|"ml.p5en.48xlarge"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.c5n.xlarge"|"ml.c5n.2xlarge"|"ml.c5n.4xlarge"|"ml.c5n.9xlarge"|"ml.c5n.18xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.16xlarge"|"ml.g6.12xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.16xlarge"|"ml.g6e.12xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.trn2.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.8xlarge"|"ml.c6i.4xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.8xlarge"|"ml.r5d.12xlarge"|"ml.r5d.16xlarge"|"ml.r5d.24xlarge"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge",
        "InstanceCount": integer,
        "VolumeSizeInGB": integer
      }
      ...
    ]
  },
  "StoppingCondition": {
    "MaxRuntimeInSeconds": integer,
    "MaxWaitTimeInSeconds": integer,
    "MaxPendingTimeInSeconds": integer
  },
  "EnableNetworkIsolation": true|false,
  "EnableInterContainerTrafficEncryption": true|false,
  "EnableManagedSpotTraining": true|false,
  "CheckpointConfig": {
    "S3Uri": "string",
    "LocalPath": "string"
  },
  "RetryStrategy": {
    "MaximumRetryAttempts": integer
  },
  "Environment": {"string": "string"
    ...}
}
```

`--training-job-definitions` (list)

A list of the [HyperParameterTrainingJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html) objects launched for this tuning job.

(structure)

Defines the training jobs launched by a hyperparameter tuning job.

DefinitionName -> (string)

The job definition name.

TuningObjective -> (structure)

Defines the objective metric for a hyperparameter tuning job. Hyperparameter tuning uses the value of this metric to evaluate the training jobs it launches, and returns the training job that results in either the highest or lowest value for this metric, depending on the value you specify for the `Type` parameter. If you want to define a custom objective metric, see [Define metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) .

Type -> (string)

Whether to minimize or maximize the objective metric.

MetricName -> (string)

The name of the metric to use for the objective metric.

HyperParameterRanges -> (structure)

Specifies ranges of integer, continuous, and categorical hyperparameters that a hyperparameter tuning job searches. The hyperparameter tuning job launches training jobs with hyperparameter values within these ranges to find the combination of values that result in the training job with the best performance as measured by the objective metric of the hyperparameter tuning job.

### Note

The maximum number of items specified for `Array Members` refers to the maximum number of hyperparameters for each range and also the maximum for the hyperparameter tuning job itself. That is, the sum of the number of hyperparameters for all the ranges canât exceed the maximum number specified.

IntegerParameterRanges -> (list)

The array of [IntegerParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IntegerParameterRange.html) objects that specify ranges of integer hyperparameters that a hyperparameter tuning job searches.

(structure)

For a hyperparameter of the integer type, specifies the range that a hyperparameter tuning job searches.

Name -> (string)

The name of the hyperparameter to search.

MinValue -> (string)

The minimum value of the hyperparameter to search.

MaxValue -> (string)

The maximum value of the hyperparameter to search.

ScalingType -> (string)

The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see [Hyperparameter Scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type) . One of the following values:

Auto

SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.

Linear

Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.

Logarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.

Logarithmic scaling works only for ranges that have only values greater than 0.

ContinuousParameterRanges -> (list)

The array of [ContinuousParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContinuousParameterRange.html) objects that specify ranges of continuous hyperparameters that a hyperparameter tuning job searches.

(structure)

A list of continuous hyperparameters to tune.

Name -> (string)

The name of the continuous hyperparameter to tune.

MinValue -> (string)

The minimum value for the hyperparameter. The tuning job uses floating-point values between this value and `MaxValue` for tuning.

MaxValue -> (string)

The maximum value for the hyperparameter. The tuning job uses floating-point values between `MinValue` value and this value for tuning.

ScalingType -> (string)

The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see [Hyperparameter Scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type) . One of the following values:

Auto

SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.

Linear

Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.

Logarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.

Logarithmic scaling works only for ranges that have only values greater than 0.

ReverseLogarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a reverse logarithmic scale.

Reverse logarithmic scaling works only for ranges that are entirely within the range 0<=x<1.0.

CategoricalParameterRanges -> (list)

The array of [CategoricalParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CategoricalParameterRange.html) objects that specify ranges of categorical hyperparameters that a hyperparameter tuning job searches.

(structure)

A list of categorical hyperparameters to tune.

Name -> (string)

The name of the categorical hyperparameter to tune.

Values -> (list)

A list of the categories for the hyperparameter.

(string)

AutoParameters -> (list)

A list containing hyperparameter names and example values to be used by Autotune to determine optimal ranges for your tuning job.

(structure)

The name and an example value of the hyperparameter that you want to use in Autotune. If Automatic model tuning (AMT) determines that your hyperparameter is eligible for Autotune, an optimal hyperparameter range is selected for you.

Name -> (string)

The name of the hyperparameter to optimize using Autotune.

ValueHint -> (string)

An example value of the hyperparameter to optimize using Autotune.

StaticHyperParameters -> (map)

Specifies the values of hyperparameters that do not change for the tuning job.

key -> (string)

value -> (string)

AlgorithmSpecification -> (structure)

The [HyperParameterAlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterAlgorithmSpecification.html) object that specifies the resource algorithm to use for the training jobs that the tuning job launches.

TrainingImage -> (string)

The registry path of the Docker image that contains the training algorithm. For information about Docker registry paths for built-in algorithms, see [Algorithms Provided by Amazon SageMaker: Common Parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html) . SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) .

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

AlgorithmName -> (string)

The name of the resource algorithm to use for the hyperparameter tuning job. If you specify a value for this parameter, do not specify a value for `TrainingImage` .

MetricDefinitions -> (list)

An array of [MetricDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDefinition.html) objects that specify the metrics that the algorithm emits.

(structure)

Specifies a metric that the training algorithm writes to `stderr` or `stdout` . You can view these logs to understand how your training job performs and check for any errors encountered during training. SageMaker hyperparameter tuning captures all defined metrics. Specify one of the defined metrics to use as an objective metric using the [TuningObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-TuningObjective) parameter in the `HyperParameterTrainingJobDefinition` API to evaluate job performance during hyperparameter tuning.

Name -> (string)

The name of the metric.

Regex -> (string)

A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see [Defining metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) .

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role associated with the training jobs that the tuning job launches.

InputDataConfig -> (list)

An array of [Channel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Channel.html) objects that specify the input for the training jobs that the tuning job launches.

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

VpcConfig -> (structure)

The [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that you want the training jobs that this hyperparameter tuning job launches to connect to. Control access to and from your training container by configuring the VPC. For more information, see [Protect Training Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

OutputDataConfig -> (structure)

Specifies the path to the Amazon S3 bucket where you store model artifacts from the training jobs that the tuning job launches.

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

The resources, including the compute instances and storage volumes, to use for the training jobs that the tuning job launches.

Storage volumes store model artifacts and incremental states. Training algorithms might also use storage volumes for scratch space. If you want SageMaker to use the storage volume to store the training data, choose `File` as the `TrainingInputMode` in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.

### Note

If you want to use hyperparameter optimization with instance type flexibility, use `HyperParameterTuningResourceConfig` instead.

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

HyperParameterTuningResourceConfig -> (structure)

The configuration for the hyperparameter tuning resources, including the compute instances and storage volumes, used for training jobs launched by the tuning job. By default, storage volumes hold model artifacts and incremental states. Choose `File` for `TrainingInputMode` in the `AlgorithmSpecification` parameter to additionally store training data in the storage volume (optional).

InstanceType -> (string)

The instance type used to run hyperparameter optimization tuning jobs. See [descriptions of instance types](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-instance-types.html) for more information.

InstanceCount -> (integer)

The number of compute instances of type `InstanceType` to use. For [distributed training](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-use-api.html) , select a value greater than 1.

VolumeSizeInGB -> (integer)

The volume size in GB for the storage volume to be used in processing hyperparameter optimization jobs (optional). These volumes store model artifacts, incremental states and optionally, scratch space for training algorithms. Do not provide a value for this parameter if a value for `InstanceConfigs` is also specified.

Some instance types have a fixed total local storage size. If you select one of these instances for training, `VolumeSizeInGB` cannot be greater than this total size. For a list of instance types with local instance storage and their sizes, see [instance store volumes](http://aws.amazon.com/releasenotes/host-instance-storage-volumes-table/) .

### Note

SageMaker supports only the [General Purpose SSD (gp2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) storage volume type.

VolumeKmsKeyId -> (string)

A key used by Amazon Web Services Key Management Service to encrypt data on the storage volume attached to the compute instances used to run the training job. You can use either of the following formats to specify a key.

KMS Key ID:

`"1234abcd-12ab-34cd-56ef-1234567890ab"`

Amazon Resource Name (ARN) of a KMS key:

`"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

Some instances use local storage, which use a [hardware module to encrypt](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) storage volumes. If you choose one of these instance types, you cannot request a `VolumeKmsKeyId` . For a list of instance types that use local storage, see [instance store volumes](http://aws.amazon.com/releasenotes/host-instance-storage-volumes-table/) . For more information about Amazon Web Services Key Management Service, see [KMS encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-kms-permissions.html) for more information.

AllocationStrategy -> (string)

The strategy that determines the order of preference for resources specified in `InstanceConfigs` used in hyperparameter optimization.

InstanceConfigs -> (list)

A list containing the configuration(s) for one or more resources for processing hyperparameter jobs. These resources include compute instances and storage volumes to use in model training jobs launched by hyperparameter tuning jobs. The `AllocationStrategy` controls the order in which multiple configurations provided in `InstanceConfigs` are used.

### Note

If you only want to use a single instance configuration inside the `HyperParameterTuningResourceConfig` API, do not provide a value for `InstanceConfigs` . Instead, use `InstanceType` , `VolumeSizeInGB` and `InstanceCount` . If you use `InstanceConfigs` , do not provide values for `InstanceType` , `VolumeSizeInGB` or `InstanceCount` .

(structure)

The configuration for hyperparameter tuning resources for use in training jobs launched by the tuning job. These resources include compute instances and storage volumes. Specify one or more compute instance configurations and allocation strategies to select resources (optional).

InstanceType -> (string)

The instance type used for processing of hyperparameter optimization jobs. Choose from general purpose (no GPUs) instance types: ml.m5.xlarge, ml.m5.2xlarge, and ml.m5.4xlarge or compute optimized (no GPUs) instance types: ml.c5.xlarge and ml.c5.2xlarge. For more information about instance types, see [instance type descriptions](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-instance-types.html) .

InstanceCount -> (integer)

The number of instances of the type specified by `InstanceType` . Choose an instance count larger than 1 for distributed training algorithms. See [Step 2: Launch a SageMaker Distributed Training Job Using the SageMaker Python SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-use-api.html) for more information.

VolumeSizeInGB -> (integer)

The volume size in GB of the data to be processed for hyperparameter optimization (optional).

StoppingCondition -> (structure)

Specifies a limit to how long a model hyperparameter training job can run. It also specifies how long a managed spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.

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

EnableNetworkIsolation -> (boolean)

Isolates the training container. No inbound or outbound network calls can be made, except for calls between peers within a training cluster for distributed training. If network isolation is used for training jobs that are configured to use a VPC, SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.

EnableInterContainerTrafficEncryption -> (boolean)

To encrypt all communications between ML compute instances in distributed training, choose `True` . Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training.

EnableManagedSpotTraining -> (boolean)

A Boolean indicating whether managed spot training is enabled (`True` ) or not (`False` ).

CheckpointConfig -> (structure)

Contains information about the output location for managed spot training checkpoint data.

S3Uri -> (string)

Identifies the S3 path where you want SageMaker to store checkpoints. For example, `s3://bucket-name/key-name-prefix` .

LocalPath -> (string)

(Optional) The local directory where checkpoints are written. The default directory is `/opt/ml/checkpoints/` .

RetryStrategy -> (structure)

The number of times to retry the job when the job fails due to an `InternalServerError` .

MaximumRetryAttempts -> (integer)

The number of times to retry the job. When the job is retried, itâs `SecondaryStatus` is changed to `STARTING` .

Environment -> (map)

An environment variable that you can pass into the SageMaker [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API. You can use an existing [environment variable from the training container](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html#sagemaker-CreateTrainingJob-request-Environment) or use your own. See [Define metrics and variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) for more information.

### Note

The maximum number of items specified for `Map Entries` refers to the maximum number of environment variables for each `TrainingJobDefinition` and also the maximum for the hyperparameter tuning job itself. That is, the sum of the number of environment variables for all the training job definitions canât exceed the maximum number specified.

key -> (string)

value -> (string)

JSON Syntax:

```
[
  {
    "DefinitionName": "string",
    "TuningObjective": {
      "Type": "Maximize"|"Minimize",
      "MetricName": "string"
    },
    "HyperParameterRanges": {
      "IntegerParameterRanges": [
        {
          "Name": "string",
          "MinValue": "string",
          "MaxValue": "string",
          "ScalingType": "Auto"|"Linear"|"Logarithmic"|"ReverseLogarithmic"
        }
        ...
      ],
      "ContinuousParameterRanges": [
        {
          "Name": "string",
          "MinValue": "string",
          "MaxValue": "string",
          "ScalingType": "Auto"|"Linear"|"Logarithmic"|"ReverseLogarithmic"
        }
        ...
      ],
      "CategoricalParameterRanges": [
        {
          "Name": "string",
          "Values": ["string", ...]
        }
        ...
      ],
      "AutoParameters": [
        {
          "Name": "string",
          "ValueHint": "string"
        }
        ...
      ]
    },
    "StaticHyperParameters": {"string": "string"
      ...},
    "AlgorithmSpecification": {
      "TrainingImage": "string",
      "TrainingInputMode": "Pipe"|"File"|"FastFile",
      "AlgorithmName": "string",
      "MetricDefinitions": [
        {
          "Name": "string",
          "Regex": "string"
        }
        ...
      ]
    },
    "RoleArn": "string",
    "InputDataConfig": [
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
    ],
    "VpcConfig": {
      "SecurityGroupIds": ["string", ...],
      "Subnets": ["string", ...]
    },
    "OutputDataConfig": {
      "KmsKeyId": "string",
      "S3OutputPath": "string",
      "CompressionType": "GZIP"|"NONE"
    },
    "ResourceConfig": {
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
    },
    "HyperParameterTuningResourceConfig": {
      "InstanceType": "ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.p3dn.24xlarge"|"ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.p5.48xlarge"|"ml.p5e.48xlarge"|"ml.p5en.48xlarge"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.c5n.xlarge"|"ml.c5n.2xlarge"|"ml.c5n.4xlarge"|"ml.c5n.9xlarge"|"ml.c5n.18xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.16xlarge"|"ml.g6.12xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.16xlarge"|"ml.g6e.12xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.trn2.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.8xlarge"|"ml.c6i.4xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.8xlarge"|"ml.r5d.12xlarge"|"ml.r5d.16xlarge"|"ml.r5d.24xlarge"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge",
      "InstanceCount": integer,
      "VolumeSizeInGB": integer,
      "VolumeKmsKeyId": "string",
      "AllocationStrategy": "Prioritized",
      "InstanceConfigs": [
        {
          "InstanceType": "ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.p3dn.24xlarge"|"ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.p5.48xlarge"|"ml.p5e.48xlarge"|"ml.p5en.48xlarge"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.c5n.xlarge"|"ml.c5n.2xlarge"|"ml.c5n.4xlarge"|"ml.c5n.9xlarge"|"ml.c5n.18xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.16xlarge"|"ml.g6.12xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.16xlarge"|"ml.g6e.12xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.trn2.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.8xlarge"|"ml.c6i.4xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.8xlarge"|"ml.r5d.12xlarge"|"ml.r5d.16xlarge"|"ml.r5d.24xlarge"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge",
          "InstanceCount": integer,
          "VolumeSizeInGB": integer
        }
        ...
      ]
    },
    "StoppingCondition": {
      "MaxRuntimeInSeconds": integer,
      "MaxWaitTimeInSeconds": integer,
      "MaxPendingTimeInSeconds": integer
    },
    "EnableNetworkIsolation": true|false,
    "EnableInterContainerTrafficEncryption": true|false,
    "EnableManagedSpotTraining": true|false,
    "CheckpointConfig": {
      "S3Uri": "string",
      "LocalPath": "string"
    },
    "RetryStrategy": {
      "MaximumRetryAttempts": integer
    },
    "Environment": {"string": "string"
      ...}
  }
  ...
]
```

`--warm-start-config` (structure)

Specifies the configuration for starting the hyperparameter tuning job using one or more previous tuning jobs as a starting point. The results of previous tuning jobs are used to inform which combinations of hyperparameters to search over in the new tuning job.

All training jobs launched by the new hyperparameter tuning job are evaluated by using the objective metric. If you specify `IDENTICAL_DATA_AND_ALGORITHM` as the `WarmStartType` value for the warm start configuration, the training job that performs the best in the new tuning job is compared to the best training jobs from the parent tuning jobs. From these, the training job that performs the best as measured by the objective metric is returned as the overall best training job.

### Note

All training jobs launched by parent hyperparameter tuning jobs and the new hyperparameter tuning jobs count against the limit of training jobs for the tuning job.

ParentHyperParameterTuningJobs -> (list)

An array of hyperparameter tuning jobs that are used as the starting point for the new hyperparameter tuning job. For more information about warm starting a hyperparameter tuning job, see [Using a Previous Hyperparameter Tuning Job as a Starting Point](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-warm-start.html) .

Hyperparameter tuning jobs created before October 1, 2018 cannot be used as parent jobs for warm start tuning jobs.

(structure)

A previously completed or stopped hyperparameter tuning job to be used as a starting point for a new hyperparameter tuning job.

HyperParameterTuningJobName -> (string)

The name of the hyperparameter tuning job to be used as a starting point for a new hyperparameter tuning job.

WarmStartType -> (string)

Specifies one of the following:

IDENTICAL_DATA_AND_ALGORITHM

The new hyperparameter tuning job uses the same input data and training image as the parent tuning jobs. You can change the hyperparameter ranges to search and the maximum number of training jobs that the hyperparameter tuning job launches. You cannot use a new version of the training algorithm, unless the changes in the new version do not affect the algorithm itself. For example, changes that improve logging or adding support for a different data format are allowed. You can also change hyperparameters from tunable to static, and from static to tunable, but the total number of static plus tunable hyperparameters must remain the same as it is in all parent jobs. The objective metric for the new tuning job must be the same as for all parent jobs.

TRANSFER_LEARNING

The new hyperparameter tuning job can include input data, hyperparameter ranges, maximum number of concurrent training jobs, and maximum number of training jobs that are different than those of its parent hyperparameter tuning jobs. The training image can also be a different version from the version used in the parent hyperparameter tuning job. You can also change hyperparameters from tunable to static, and from static to tunable, but the total number of static plus tunable hyperparameters must remain the same as it is in all parent jobs. The objective metric for the new tuning job must be the same as for all parent jobs.

Shorthand Syntax:

```
ParentHyperParameterTuningJobs=[{HyperParameterTuningJobName=string},{HyperParameterTuningJobName=string}],WarmStartType=string
```

JSON Syntax:

```
{
  "ParentHyperParameterTuningJobs": [
    {
      "HyperParameterTuningJobName": "string"
    }
    ...
  ],
  "WarmStartType": "IdenticalDataAndAlgorithm"|"TransferLearning"
}
```

`--tags` (list)

An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) .

Tags that you specify for the tuning job are also added to all training jobs that the tuning job launches.

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

`--autotune` (structure)

Configures SageMaker Automatic model tuning (AMT) to automatically find optimal parameters for the following fields:

- [ParameterRanges](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-ParameterRanges) : The names and ranges of parameters that a hyperparameter tuning job can optimize.
- [ResourceLimits](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html) : The maximum resources that can be used for a training job. These resources include the maximum number of training jobs, the maximum runtime of a tuning job, and the maximum number of training jobs to run at the same time.
- [TrainingJobEarlyStoppingType](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-TrainingJobEarlyStoppingType) : A flag that specifies whether or not to use early stopping for training jobs launched by a hyperparameter tuning job.
- [RetryStrategy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-RetryStrategy) : The number of times to retry a training job.
- [Strategy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html) : Specifies how hyperparameter tuning chooses the combinations of hyperparameter values to use for the training jobs that it launches.
- [ConvergenceDetected](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ConvergenceDetected.html) : A flag to indicate that Automatic model tuning (AMT) has detected model convergence.

Mode -> (string)

Set `Mode` to `Enabled` if you want to use Autotune.

Shorthand Syntax:

```
Mode=string
```

JSON Syntax:

```
{
  "Mode": "Enabled"
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

HyperParameterTuningJobArn -> (string)

The Amazon Resource Name (ARN) of the tuning job. SageMaker assigns an ARN to a hyperparameter tuning job when you create it.