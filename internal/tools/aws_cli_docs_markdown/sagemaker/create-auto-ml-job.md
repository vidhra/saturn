# create-auto-ml-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-auto-ml-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-auto-ml-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-auto-ml-job

## Description

Creates an Autopilot job also referred to as Autopilot experiment or AutoML job.

An AutoML job in SageMaker AI is a fully automated process that allows you to build machine learning models with minimal effort and machine learning expertise. When initiating an AutoML job, you provide your data and optionally specify parameters tailored to your use case. SageMaker AI then automates the entire model development lifecycle, including data preprocessing, model training, tuning, and evaluation. AutoML jobs are designed to simplify and accelerate the model building process by automating various tasks and exploring different combinations of machine learning algorithms, data preprocessing techniques, and hyperparameter values. The output of an AutoML job comprises one or more trained models ready for deployment and inference. Additionally, SageMaker AI AutoML jobs generate a candidate model leaderboard, allowing you to select the best-performing model for deployment.

For more information about AutoML jobs, see [https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html) in the SageMaker AI developer guide.

### Note

We recommend using the new versions [CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html) and [DescribeAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html) , which offer backward compatibility.

`CreateAutoMLJobV2` can manage tabular problem types identical to those of its previous version `CreateAutoMLJob` , as well as time-series forecasting, non-tabular problem types such as image or text classification, and text generation (LLMs fine-tuning).

Find guidelines about how to migrate a `CreateAutoMLJob` to `CreateAutoMLJobV2` in [Migrate a CreateAutoMLJob to CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-create-experiment.html#autopilot-create-experiment-api-migrate-v1-v2) .

You can find the best-performing model after you run an AutoML job by calling [DescribeAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html) (recommended) or [DescribeAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJob.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateAutoMLJob)

## Synopsis

```
create-auto-ml-job
--auto-ml-job-name <value>
--input-data-config <value>
--output-data-config <value>
[--problem-type <value>]
[--auto-ml-job-objective <value>]
[--auto-ml-job-config <value>]
--role-arn <value>
[--generate-candidate-definitions-only | --no-generate-candidate-definitions-only]
[--tags <value>]
[--model-deploy-config <value>]
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

`--auto-ml-job-name` (string)

Identifies an Autopilot job. The name must be unique to your account and is case insensitive.

`--input-data-config` (list)

An array of channel objects that describes the input data and its location. Each channel is a named input source. Similar to `InputDataConfig` supported by [HyperParameterTrainingJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html) . Format(s) supported: CSV, Parquet. A minimum of 500 rows is required for the training dataset. There is not a minimum number of rows required for the validation dataset.

(structure)

A channel is a named input source that training algorithms can consume. The validation dataset size is limited to less than 2 GB. The training dataset size must be less than 100 GB. For more information, see [Channel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Channel.html) .

### Note

A validation dataset must contain the same headers as the training dataset.

DataSource -> (structure)

The data source for an AutoML channel.

S3DataSource -> (structure)

The Amazon S3 location of the input data.

S3DataType -> (string)

The data type.

- If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker AI uses all objects that match the specified key name prefix for model training. The `S3Prefix` should have the following format:  `s3://DOC-EXAMPLE-BUCKET/DOC-EXAMPLE-FOLDER-OR-FILE`
- If you choose `ManifestFile` , `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want SageMaker AI to use for model training. A `ManifestFile` should have the format shown below:  `[ {"prefix": "s3://DOC-EXAMPLE-BUCKET/DOC-EXAMPLE-FOLDER/DOC-EXAMPLE-PREFIX/"},` `"DOC-EXAMPLE-RELATIVE-PATH/DOC-EXAMPLE-FOLDER/DATA-1",` `"DOC-EXAMPLE-RELATIVE-PATH/DOC-EXAMPLE-FOLDER/DATA-2",` `... "DOC-EXAMPLE-RELATIVE-PATH/DOC-EXAMPLE-FOLDER/DATA-N" ]`
- If you choose `AugmentedManifestFile` , `S3Uri` identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. `AugmentedManifestFile` is available for V2 API jobs only (for example, for jobs created by calling `CreateAutoMLJobV2` ). Here is a minimal, single-record example of an `AugmentedManifestFile` :  `{"source-ref": "s3://DOC-EXAMPLE-BUCKET/DOC-EXAMPLE-FOLDER/cats/cat.jpg",` `"label-metadata": {"class-name": "cat"` } For more information on `AugmentedManifestFile` , see [Provide Dataset Metadata to Training Jobs with an Augmented Manifest File](https://docs.aws.amazon.com/sagemaker/latest/dg/augmented-manifest.html) .

S3Uri -> (string)

The URL to the Amazon S3 data source. The Uri refers to the Amazon S3 prefix or ManifestFile depending on the data type.

CompressionType -> (string)

You can use `Gzip` or `None` . The default value is `None` .

TargetAttributeName -> (string)

The name of the target variable in supervised learning, usually represented by âyâ.

ContentType -> (string)

The content type of the data from the input source. You can use `text/csv;header=present` or `x-application/vnd.amazon+parquet` . The default value is `text/csv;header=present` .

ChannelType -> (string)

The channel type (optional) is an `enum` string. The default value is `training` . Channels for training and validation must share the same `ContentType` and `TargetAttributeName` . For information on specifying training and validation channel types, see [How to specify training and validation datasets](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-datasets-problem-types.html#autopilot-data-sources-training-or-validation) .

SampleWeightAttributeName -> (string)

If specified, this column name indicates which column of the dataset should be treated as sample weights for use by the objective metric during the training, evaluation, and the selection of the best model. This column is not considered as a predictive feature. For more information on Autopilot metrics, see [Metrics and validation](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html) .

Sample weights should be numeric, non-negative, with larger values indicating which rows are more important than others. Data points that have invalid or no weight value are excluded.

Support for sample weights is available in [Ensembling](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html) mode only.

Shorthand Syntax:

```
DataSource={S3DataSource={S3DataType=string,S3Uri=string}},CompressionType=string,TargetAttributeName=string,ContentType=string,ChannelType=string,SampleWeightAttributeName=string ...
```

JSON Syntax:

```
[
  {
    "DataSource": {
      "S3DataSource": {
        "S3DataType": "ManifestFile"|"S3Prefix"|"AugmentedManifestFile",
        "S3Uri": "string"
      }
    },
    "CompressionType": "None"|"Gzip",
    "TargetAttributeName": "string",
    "ContentType": "string",
    "ChannelType": "training"|"validation",
    "SampleWeightAttributeName": "string"
  }
  ...
]
```

`--output-data-config` (structure)

Provides information about encryption and the Amazon S3 output path needed to store artifacts from an AutoML job. Format(s) supported: CSV.

KmsKeyId -> (string)

The Key Management Service encryption key ID.

S3OutputPath -> (string)

The Amazon S3 output path. Must be 512 characters or less.

Shorthand Syntax:

```
KmsKeyId=string,S3OutputPath=string
```

JSON Syntax:

```
{
  "KmsKeyId": "string",
  "S3OutputPath": "string"
}
```

`--problem-type` (string)

Defines the type of supervised learning problem available for the candidates. For more information, see [SageMaker Autopilot problem types](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-datasets-problem-types.html#autopilot-problem-types) .

Possible values:

- `BinaryClassification`
- `MulticlassClassification`
- `Regression`

`--auto-ml-job-objective` (structure)

Specifies a metric to minimize or maximize as the objective of a job. If not specified, the default objective metric depends on the problem type. See [AutoMLJobObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobObjective.html) for the default values.

MetricName -> (string)

The name of the objective metric used to measure the predictive quality of a machine learning system. During training, the modelâs parameters are updated iteratively to optimize its performance based on the feedback provided by the objective metric when evaluating the model on the validation dataset.

The list of available metrics supported by Autopilot and the default metric applied when you do not specify a metric name explicitly depend on the problem type.

- For tabular problem types:

- List of available metrics:
- Regression: `MAE` , `MSE` , `R2` , `RMSE`
- Binary classification: `Accuracy` , `AUC` , `BalancedAccuracy` , `F1` , `Precision` , `Recall`
- Multiclass classification: `Accuracy` , `BalancedAccuracy` , `F1macro` , `PrecisionMacro` , `RecallMacro`

For a description of each metric, see [Autopilot metrics for classification and regression](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html#autopilot-metrics) .

- Default objective metrics:
- Regression: `MSE` .
- Binary classification: `F1` .
- Multiclass classification: `Accuracy` .
- For image or text classification problem types:

- List of available metrics: `Accuracy`   For a description of each metric, see [Autopilot metrics for text and image classification](https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-data-format-and-metric.html) .
- Default objective metrics: `Accuracy`
- For time-series forecasting problem types:

- List of available metrics: `RMSE` , `wQL` , `Average wQL` , `MASE` , `MAPE` , `WAPE`   For a description of each metric, see [Autopilot metrics for time-series forecasting](https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-objective-metric.html) .
- Default objective metrics: `AverageWeightedQuantileLoss`
- For text generation problem types (LLMs fine-tuning): Fine-tuning language models in Autopilot does not require setting the `AutoMLJobObjective` field. Autopilot fine-tunes LLMs without requiring multiple candidates to be trained and evaluated. Instead, using your dataset, Autopilot directly fine-tunes your target model to enhance a default objective metric, the cross-entropy loss. After fine-tuning a language model, you can evaluate the quality of its generated text using different metrics. For a list of the available metrics, see [Metrics for fine-tuning LLMs in Autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-metrics.html) .

Shorthand Syntax:

```
MetricName=string
```

JSON Syntax:

```
{
  "MetricName": "Accuracy"|"MSE"|"F1"|"F1macro"|"AUC"|"RMSE"|"BalancedAccuracy"|"R2"|"Recall"|"RecallMacro"|"Precision"|"PrecisionMacro"|"MAE"|"MAPE"|"MASE"|"WAPE"|"AverageWeightedQuantileLoss"
}
```

`--auto-ml-job-config` (structure)

A collection of settings used to configure an AutoML job.

CompletionCriteria -> (structure)

How long an AutoML job is allowed to run, or how many candidates a job is allowed to generate.

MaxCandidates -> (integer)

The maximum number of times a training job is allowed to run.

For text and image classification, time-series forecasting, as well as text generation (LLMs fine-tuning) problem types, the supported value is 1. For tabular problem types, the maximum value is 750.

MaxRuntimePerTrainingJobInSeconds -> (integer)

The maximum time, in seconds, that each training job executed inside hyperparameter tuning is allowed to run as part of a hyperparameter tuning job. For more information, see the [StoppingCondition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StoppingCondition.html) used by the [CreateHyperParameterTuningJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHyperParameterTuningJob.html) action.

For job V2s (jobs created by calling `CreateAutoMLJobV2` ), this field controls the runtime of the job candidate.

For [TextGenerationJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TextClassificationJobConfig.html) problem types, the maximum time defaults to 72 hours (259200 seconds).

MaxAutoMLJobRuntimeInSeconds -> (integer)

The maximum runtime, in seconds, an AutoML job has to complete.

If an AutoML job exceeds the maximum runtime, the job is stopped automatically and its processing is ended gracefully. The AutoML job identifies the best model whose training was completed and marks it as the best-performing model. Any unfinished steps of the job, such as automatic one-click Autopilot model deployment, are not completed.

SecurityConfig -> (structure)

The security configuration for traffic encryption or Amazon VPC settings.

VolumeKmsKeyId -> (string)

The key used to encrypt stored data.

EnableInterContainerTrafficEncryption -> (boolean)

Whether to use traffic encryption between the container layers.

VpcConfig -> (structure)

The VPC configuration.

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

CandidateGenerationConfig -> (structure)

The configuration for generating a candidate for an AutoML job (optional).

FeatureSpecificationS3Uri -> (string)

A URL to the Amazon S3 data source containing selected features from the input data source to run an Autopilot job. You can input `FeatureAttributeNames` (optional) in JSON format as shown below:

`{ "FeatureAttributeNames":["col1", "col2", ...] }` .

You can also specify the data type of the feature (optional) in the format shown below:

`{ "FeatureDataTypes":{"col1":"numeric", "col2":"categorical" ... } }`

### Note

These column keys may not include the target column.

In ensembling mode, Autopilot only supports the following data types: `numeric` , `categorical` , `text` , and `datetime` . In HPO mode, Autopilot can support `numeric` , `categorical` , `text` , `datetime` , and `sequence` .

If only `FeatureDataTypes` is provided, the column keys (`col1` , `col2` ,..) should be a subset of the column names in the input data.

If both `FeatureDataTypes` and `FeatureAttributeNames` are provided, then the column keys should be a subset of the column names provided in `FeatureAttributeNames` .

The key name `FeatureAttributeNames` is fixed. The values listed in `["col1", "col2", ...]` are case sensitive and should be a list of strings containing unique values that are a subset of the column names in the input data. The list of columns provided must not include the target column.

AlgorithmsConfig -> (list)

Stores the configuration information for the selection of algorithms trained on tabular data.

The list of available algorithms to choose from depends on the training mode set in ` `TabularJobConfig.Mode` [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig).html`__ .

- `AlgorithmsConfig` should not be set if the training mode is set on `AUTO` .
- When `AlgorithmsConfig` is provided, one `AutoMLAlgorithms` attribute must be set and one only. If the list of algorithms provided as values for `AutoMLAlgorithms` is empty, `CandidateGenerationConfig` uses the full set of algorithms for the given training mode.
- When `AlgorithmsConfig` is not provided, `CandidateGenerationConfig` uses the full set of algorithms for the given training mode.

For the list of all algorithms per problem type and training mode, see [AutoMLAlgorithmConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html) .

For more information on each algorithm, see the [Algorithm support](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support) section in Autopilot developer guide.

(structure)

The selection of algorithms trained on your dataset to generate the model candidates for an Autopilot job.

AutoMLAlgorithms -> (list)

The selection of algorithms trained on your dataset to generate the model candidates for an Autopilot job.

- **For the tabular problem type ``TabularJobConfig`` :**

### Note

Selected algorithms must belong to the list corresponding to the training mode set in [AutoMLJobConfig.Mode](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig.html#sagemaker-Type-AutoMLJobConfig-Mode) (`ENSEMBLING` or `HYPERPARAMETER_TUNING` ). Choose a minimum of 1 algorithm.

- In `ENSEMBLING` mode:
- âcatboostâ
- âextra-treesâ
- âfastaiâ
- âlightgbmâ
- âlinear-learnerâ
- ânn-torchâ
- ârandomforestâ
- âxgboostâ
- In `HYPERPARAMETER_TUNING` mode:
- âlinear-learnerâ
- âmlpâ
- âxgboostâ

- **For the time-series forecasting problem type ``TimeSeriesForecastingJobConfig`` :**
- Choose your algorithms from this list.
- âcnn-qrâ
- âdeeparâ
- âprophetâ
- âarimaâ
- ânptsâ
- âetsâ

(string)

DataSplitConfig -> (structure)

The configuration for splitting the input training dataset.

Type: AutoMLDataSplitConfig

ValidationFraction -> (float)

The validation fraction (optional) is a float that specifies the portion of the training dataset to be used for validation. The default value is 0.2, and values must be greater than 0 and less than 1. We recommend setting this value to be less than 0.5.

Mode -> (string)

The method that Autopilot uses to train the data. You can either specify the mode manually or let Autopilot choose for you based on the dataset size by selecting `AUTO` . In `AUTO` mode, Autopilot chooses `ENSEMBLING` for datasets smaller than 100 MB, and `HYPERPARAMETER_TUNING` for larger ones.

The `ENSEMBLING` mode uses a multi-stack ensemble model to predict classification and regression tasks directly from your dataset. This machine learning mode combines several base models to produce an optimal predictive model. It then uses a stacking ensemble method to combine predictions from contributing members. A multi-stack ensemble model can provide better performance over a single model by combining the predictive capabilities of multiple models. See [Autopilot algorithm support](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support) for a list of algorithms supported by `ENSEMBLING` mode.

The `HYPERPARAMETER_TUNING` (HPO) mode uses the best hyperparameters to train the best version of a model. HPO automatically selects an algorithm for the type of problem you want to solve. Then HPO finds the best hyperparameters according to your objective metric. See [Autopilot algorithm support](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support) for a list of algorithms supported by `HYPERPARAMETER_TUNING` mode.

JSON Syntax:

```
{
  "CompletionCriteria": {
    "MaxCandidates": integer,
    "MaxRuntimePerTrainingJobInSeconds": integer,
    "MaxAutoMLJobRuntimeInSeconds": integer
  },
  "SecurityConfig": {
    "VolumeKmsKeyId": "string",
    "EnableInterContainerTrafficEncryption": true|false,
    "VpcConfig": {
      "SecurityGroupIds": ["string", ...],
      "Subnets": ["string", ...]
    }
  },
  "CandidateGenerationConfig": {
    "FeatureSpecificationS3Uri": "string",
    "AlgorithmsConfig": [
      {
        "AutoMLAlgorithms": ["xgboost"|"linear-learner"|"mlp"|"lightgbm"|"catboost"|"randomforest"|"extra-trees"|"nn-torch"|"fastai"|"cnn-qr"|"deepar"|"prophet"|"npts"|"arima"|"ets", ...]
      }
      ...
    ]
  },
  "DataSplitConfig": {
    "ValidationFraction": float
  },
  "Mode": "AUTO"|"ENSEMBLING"|"HYPERPARAMETER_TUNING"
}
```

`--role-arn` (string)

The ARN of the role that is used to access the data.

`--generate-candidate-definitions-only` | `--no-generate-candidate-definitions-only` (boolean)

Generates possible candidates without training the models. A candidate is a combination of data preprocessors, algorithms, and algorithm parameter settings.

`--tags` (list)

An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging Amazon Web ServicesResources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . Tag keys must be unique per resource.

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

`--model-deploy-config` (structure)

Specifies how to generate the endpoint name for an automatic one-click Autopilot model deployment.

AutoGenerateEndpointName -> (boolean)

Set to `True` to automatically generate an endpoint name for a one-click Autopilot model deployment; set to `False` otherwise. The default value is `False` .

### Note

If you set `AutoGenerateEndpointName` to `True` , do not specify the `EndpointName` ; otherwise a 400 error is thrown.

EndpointName -> (string)

Specifies the endpoint name to use for a one-click Autopilot model deployment if the endpoint name is not generated automatically.

### Note

Specify the `EndpointName` if and only if you set `AutoGenerateEndpointName` to `False` ; otherwise a 400 error is thrown.

Shorthand Syntax:

```
AutoGenerateEndpointName=boolean,EndpointName=string
```

JSON Syntax:

```
{
  "AutoGenerateEndpointName": true|false,
  "EndpointName": "string"
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

AutoMLJobArn -> (string)

The unique ARN assigned to the AutoML job when it is created.