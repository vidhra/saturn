# describe-auto-ml-job-v2Â¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-auto-ml-job-v2.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-auto-ml-job-v2.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-auto-ml-job-v2

## Description

Returns information about an AutoML job created by calling [CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html) or [CreateAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeAutoMLJobV2)

## Synopsis

```
describe-auto-ml-job-v2
--auto-ml-job-name <value>
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

Requests information about an AutoML job V2 using its unique name.

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

AutoMLJobName -> (string)

Returns the name of the AutoML job V2.

AutoMLJobArn -> (string)

Returns the Amazon Resource Name (ARN) of the AutoML job V2.

AutoMLJobInputDataConfig -> (list)

Returns an array of channel objects describing the input data and their location.

(structure)

A channel is a named input source that training algorithms can consume. This channel is used for AutoML jobs V2 (jobs created by calling [CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html) ).

ChannelType -> (string)

The type of channel. Defines whether the data are used for training or validation. The default value is `training` . Channels for `training` and `validation` must share the same `ContentType`

### Note

The type of channel defaults to `training` for the time-series forecasting problem type.

ContentType -> (string)

The content type of the data from the input source. The following are the allowed content types for different problems:

- For tabular problem types: `text/csv;header=present` or `x-application/vnd.amazon+parquet` . The default value is `text/csv;header=present` .
- For image classification: `image/png` , `image/jpeg` , or `image/*` . The default value is `image/*` .
- For text classification: `text/csv;header=present` or `x-application/vnd.amazon+parquet` . The default value is `text/csv;header=present` .
- For time-series forecasting: `text/csv;header=present` or `x-application/vnd.amazon+parquet` . The default value is `text/csv;header=present` .
- For text generation (LLMs fine-tuning): `text/csv;header=present` or `x-application/vnd.amazon+parquet` . The default value is `text/csv;header=present` .

CompressionType -> (string)

The allowed compression types depend on the input format and problem type. We allow the compression type `Gzip` for `S3Prefix` inputs on tabular data only. For all other inputs, the compression type should be `None` . If no compression type is provided, we default to `None` .

DataSource -> (structure)

The data source for an AutoML channel (Required).

S3DataSource -> (structure)

The Amazon S3 location of the input data.

S3DataType -> (string)

The data type.

- If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker AI uses all objects that match the specified key name prefix for model training. The `S3Prefix` should have the following format:  `s3://DOC-EXAMPLE-BUCKET/DOC-EXAMPLE-FOLDER-OR-FILE`
- If you choose `ManifestFile` , `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want SageMaker AI to use for model training. A `ManifestFile` should have the format shown below:  `[ {"prefix": "s3://DOC-EXAMPLE-BUCKET/DOC-EXAMPLE-FOLDER/DOC-EXAMPLE-PREFIX/"},` `"DOC-EXAMPLE-RELATIVE-PATH/DOC-EXAMPLE-FOLDER/DATA-1",` `"DOC-EXAMPLE-RELATIVE-PATH/DOC-EXAMPLE-FOLDER/DATA-2",` `... "DOC-EXAMPLE-RELATIVE-PATH/DOC-EXAMPLE-FOLDER/DATA-N" ]`
- If you choose `AugmentedManifestFile` , `S3Uri` identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. `AugmentedManifestFile` is available for V2 API jobs only (for example, for jobs created by calling `CreateAutoMLJobV2` ). Here is a minimal, single-record example of an `AugmentedManifestFile` :  `{"source-ref": "s3://DOC-EXAMPLE-BUCKET/DOC-EXAMPLE-FOLDER/cats/cat.jpg",` `"label-metadata": {"class-name": "cat"` } For more information on `AugmentedManifestFile` , see [Provide Dataset Metadata to Training Jobs with an Augmented Manifest File](https://docs.aws.amazon.com/sagemaker/latest/dg/augmented-manifest.html) .

S3Uri -> (string)

The URL to the Amazon S3 data source. The Uri refers to the Amazon S3 prefix or ManifestFile depending on the data type.

OutputDataConfig -> (structure)

Returns the jobâs output data config.

KmsKeyId -> (string)

The Key Management Service encryption key ID.

S3OutputPath -> (string)

The Amazon S3 output path. Must be 512 characters or less.

RoleArn -> (string)

The ARN of the IAM role that has read permission to the input data location and write permission to the output data location in Amazon S3.

AutoMLJobObjective -> (structure)

Returns the jobâs objective.

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

AutoMLProblemTypeConfig -> (tagged union structure)

Returns the configuration settings of the problem type set for the AutoML job V2.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ImageClassificationJobConfig`, `TextClassificationJobConfig`, `TimeSeriesForecastingJobConfig`, `TabularJobConfig`, `TextGenerationJobConfig`.

ImageClassificationJobConfig -> (structure)

Settings used to configure an AutoML job V2 for the image classification problem type.

CompletionCriteria -> (structure)

How long a job is allowed to run, or how many candidates a job is allowed to generate.

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

TextClassificationJobConfig -> (structure)

Settings used to configure an AutoML job V2 for the text classification problem type.

CompletionCriteria -> (structure)

How long a job is allowed to run, or how many candidates a job is allowed to generate.

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

ContentColumn -> (string)

The name of the column used to provide the sentences to be classified. It should not be the same as the target column.

TargetLabelColumn -> (string)

The name of the column used to provide the class labels. It should not be same as the content column.

TimeSeriesForecastingJobConfig -> (structure)

Settings used to configure an AutoML job V2 for the time-series forecasting problem type.

FeatureSpecificationS3Uri -> (string)

A URL to the Amazon S3 data source containing additional selected features that complement the target, itemID, timestamp, and grouped columns set in `TimeSeriesConfig` . When not provided, the AutoML job V2 includes all the columns from the original dataset that are not already declared in `TimeSeriesConfig` . If provided, the AutoML job V2 only considers these additional columns as a complement to the ones declared in `TimeSeriesConfig` .

You can input `FeatureAttributeNames` (optional) in JSON format as shown below:

`{ "FeatureAttributeNames":["col1", "col2", ...] }` .

You can also specify the data type of the feature (optional) in the format shown below:

`{ "FeatureDataTypes":{"col1":"numeric", "col2":"categorical" ... } }`

Autopilot supports the following data types: `numeric` , `categorical` , `text` , and `datetime` .

### Note

These column keys must not include any column set in `TimeSeriesConfig` .

CompletionCriteria -> (structure)

How long a job is allowed to run, or how many candidates a job is allowed to generate.

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

ForecastFrequency -> (string)

The frequency of predictions in a forecast.

Valid intervals are an integer followed by Y (Year), M (Month), W (Week), D (Day), H (Hour), and min (Minute). For example, `1D` indicates every day and `15min` indicates every 15 minutes. The value of a frequency must not overlap with the next larger frequency. For example, you must use a frequency of `1H` instead of `60min` .

The valid values for each frequency are the following:

- Minute - 1-59
- Hour - 1-23
- Day - 1-6
- Week - 1-4
- Month - 1-11
- Year - 1

ForecastHorizon -> (integer)

The number of time-steps that the model predicts. The forecast horizon is also called the prediction length. The maximum forecast horizon is the lesser of 500 time-steps or 1/4 of the time-steps in the dataset.

ForecastQuantiles -> (list)

The quantiles used to train the model for forecasts at a specified quantile. You can specify quantiles from `0.01` (p1) to `0.99` (p99), by increments of 0.01 or higher. Up to five forecast quantiles can be specified. When `ForecastQuantiles` is not provided, the AutoML job uses the quantiles p10, p50, and p90 as default.

(string)

Transformations -> (structure)

The transformations modifying specific attributes of the time-series, such as filling strategies for missing values.

Filling -> (map)

A key value pair defining the filling method for a column, where the key is the column name and the value is an object which defines the filling logic. You can specify multiple filling methods for a single column.

The supported filling methods and their corresponding options are:

- `frontfill` : `none` (Supported only for target column)
- `middlefill` : `zero` , `value` , `median` , `mean` , `min` , `max`
- `backfill` : `zero` , `value` , `median` , `mean` , `min` , `max`
- `futurefill` : `zero` , `value` , `median` , `mean` , `min` , `max`

To set a filling method to a specific value, set the fill parameter to the chosen filling method value (for example `"backfill" : "value"` ), and define the filling value in an additional parameter prefixed with â_valueâ. For example, to set `backfill` to a value of `2` , you must include two parameters: `"backfill": "value"` and `"backfill_value":"2"` .

key -> (string)

value -> (map)

key -> (string)

value -> (string)

Aggregation -> (map)

A key value pair defining the aggregation method for a column, where the key is the column name and the value is the aggregation method.

The supported aggregation methods are `sum` (default), `avg` , `first` , `min` , `max` .

### Note

Aggregation is only supported for the target column.

key -> (string)

value -> (string)

TimeSeriesConfig -> (structure)

The collection of components that defines the time-series.

TargetAttributeName -> (string)

The name of the column representing the target variable that you want to predict for each item in your dataset. The data type of the target variable must be numerical.

TimestampAttributeName -> (string)

The name of the column indicating a point in time at which the target value of a given item is recorded.

ItemIdentifierAttributeName -> (string)

The name of the column that represents the set of item identifiers for which you want to predict the target value.

GroupingAttributeNames -> (list)

A set of columns names that can be grouped with the item identifier column to create a composite key for which a target value is predicted.

(string)

HolidayConfig -> (list)

The collection of holiday featurization attributes used to incorporate national holiday information into your forecasting model.

(structure)

Stores the holiday featurization attributes applicable to each item of time-series datasets during the training of a forecasting model. This allows the model to identify patterns associated with specific holidays.

CountryCode -> (string)

The country code for the holiday calendar.

For the list of public holiday calendars supported by AutoML job V2, see [Country Codes](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-timeseries-forecasting-holiday-calendars.html#holiday-country-codes) . Use the country code corresponding to the country of your choice.

CandidateGenerationConfig -> (structure)

Stores the configuration information for how model candidates are generated using an AutoML job V2.

AlgorithmsConfig -> (list)

Your Autopilot job trains a default set of algorithms on your dataset. For tabular and time-series data, you can customize the algorithm list by selecting a subset of algorithms for your problem type.

`AlgorithmsConfig` stores the customized selection of algorithms to train on your data.

- **For the tabular problem type ``TabularJobConfig`` ,** the list of available algorithms to choose from depends on the training mode set in ` `AutoMLJobConfig.Mode` [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig).html`__ .
- `AlgorithmsConfig` should not be set when the training mode `AutoMLJobConfig.Mode` is set to `AUTO` .
- When `AlgorithmsConfig` is provided, one `AutoMLAlgorithms` attribute must be set and one only. If the list of algorithms provided as values for `AutoMLAlgorithms` is empty, `CandidateGenerationConfig` uses the full set of algorithms for the given training mode.
- When `AlgorithmsConfig` is not provided, `CandidateGenerationConfig` uses the full set of algorithms for the given training mode.

For the list of all algorithms per training mode, see [AlgorithmConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html) .

For more information on each algorithm, see the [Algorithm support](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support) section in the Autopilot developer guide.

- **For the time-series forecasting problem type ``TimeSeriesForecastingJobConfig`` ,** choose your algorithms from the list provided in [AlgorithmConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html) . For more information on each algorithm, see the [Algorithms support for time-series forecasting](https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-forecasting-algorithms.html) section in the Autopilot developer guide.
- When `AlgorithmsConfig` is provided, one `AutoMLAlgorithms` attribute must be set and one only. If the list of algorithms provided as values for `AutoMLAlgorithms` is empty, `CandidateGenerationConfig` uses the full set of algorithms for time-series forecasting.
- When `AlgorithmsConfig` is not provided, `CandidateGenerationConfig` uses the full set of algorithms for time-series forecasting.

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

TabularJobConfig -> (structure)

Settings used to configure an AutoML job V2 for the tabular problem type (regression, classification).

CandidateGenerationConfig -> (structure)

The configuration information of how model candidates are generated.

AlgorithmsConfig -> (list)

Your Autopilot job trains a default set of algorithms on your dataset. For tabular and time-series data, you can customize the algorithm list by selecting a subset of algorithms for your problem type.

`AlgorithmsConfig` stores the customized selection of algorithms to train on your data.

- **For the tabular problem type ``TabularJobConfig`` ,** the list of available algorithms to choose from depends on the training mode set in ` `AutoMLJobConfig.Mode` [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig).html`__ .
- `AlgorithmsConfig` should not be set when the training mode `AutoMLJobConfig.Mode` is set to `AUTO` .
- When `AlgorithmsConfig` is provided, one `AutoMLAlgorithms` attribute must be set and one only. If the list of algorithms provided as values for `AutoMLAlgorithms` is empty, `CandidateGenerationConfig` uses the full set of algorithms for the given training mode.
- When `AlgorithmsConfig` is not provided, `CandidateGenerationConfig` uses the full set of algorithms for the given training mode.

For the list of all algorithms per training mode, see [AlgorithmConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html) .

For more information on each algorithm, see the [Algorithm support](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support) section in the Autopilot developer guide.

- **For the time-series forecasting problem type ``TimeSeriesForecastingJobConfig`` ,** choose your algorithms from the list provided in [AlgorithmConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html) . For more information on each algorithm, see the [Algorithms support for time-series forecasting](https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-forecasting-algorithms.html) section in the Autopilot developer guide.
- When `AlgorithmsConfig` is provided, one `AutoMLAlgorithms` attribute must be set and one only. If the list of algorithms provided as values for `AutoMLAlgorithms` is empty, `CandidateGenerationConfig` uses the full set of algorithms for time-series forecasting.
- When `AlgorithmsConfig` is not provided, `CandidateGenerationConfig` uses the full set of algorithms for time-series forecasting.

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

CompletionCriteria -> (structure)

How long a job is allowed to run, or how many candidates a job is allowed to generate.

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

FeatureSpecificationS3Uri -> (string)

A URL to the Amazon S3 data source containing selected features from the input data source to run an Autopilot job V2. You can input `FeatureAttributeNames` (optional) in JSON format as shown below:

`{ "FeatureAttributeNames":["col1", "col2", ...] }` .

You can also specify the data type of the feature (optional) in the format shown below:

`{ "FeatureDataTypes":{"col1":"numeric", "col2":"categorical" ... } }`

### Note

These column keys may not include the target column.

In ensembling mode, Autopilot only supports the following data types: `numeric` , `categorical` , `text` , and `datetime` . In HPO mode, Autopilot can support `numeric` , `categorical` , `text` , `datetime` , and `sequence` .

If only `FeatureDataTypes` is provided, the column keys (`col1` , `col2` ,..) should be a subset of the column names in the input data.

If both `FeatureDataTypes` and `FeatureAttributeNames` are provided, then the column keys should be a subset of the column names provided in `FeatureAttributeNames` .

The key name `FeatureAttributeNames` is fixed. The values listed in `["col1", "col2", ...]` are case sensitive and should be a list of strings containing unique values that are a subset of the column names in the input data. The list of columns provided must not include the target column.

Mode -> (string)

The method that Autopilot uses to train the data. You can either specify the mode manually or let Autopilot choose for you based on the dataset size by selecting `AUTO` . In `AUTO` mode, Autopilot chooses `ENSEMBLING` for datasets smaller than 100 MB, and `HYPERPARAMETER_TUNING` for larger ones.

The `ENSEMBLING` mode uses a multi-stack ensemble model to predict classification and regression tasks directly from your dataset. This machine learning mode combines several base models to produce an optimal predictive model. It then uses a stacking ensemble method to combine predictions from contributing members. A multi-stack ensemble model can provide better performance over a single model by combining the predictive capabilities of multiple models. See [Autopilot algorithm support](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support) for a list of algorithms supported by `ENSEMBLING` mode.

The `HYPERPARAMETER_TUNING` (HPO) mode uses the best hyperparameters to train the best version of a model. HPO automatically selects an algorithm for the type of problem you want to solve. Then HPO finds the best hyperparameters according to your objective metric. See [Autopilot algorithm support](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support) for a list of algorithms supported by `HYPERPARAMETER_TUNING` mode.

GenerateCandidateDefinitionsOnly -> (boolean)

Generates possible candidates without training the models. A model candidate is a combination of data preprocessors, algorithms, and algorithm parameter settings.

ProblemType -> (string)

The type of supervised learning problem available for the model candidates of the AutoML job V2. For more information, see [SageMaker Autopilot problem types](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-datasets-problem-types.html#autopilot-problem-types) .

### Note

You must either specify the type of supervised learning problem in `ProblemType` and provide the [AutoMLJobObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLJobObjective) metric, or none at all.

TargetAttributeName -> (string)

The name of the target variable in supervised learning, usually represented by âyâ.

SampleWeightAttributeName -> (string)

If specified, this column name indicates which column of the dataset should be treated as sample weights for use by the objective metric during the training, evaluation, and the selection of the best model. This column is not considered as a predictive feature. For more information on Autopilot metrics, see [Metrics and validation](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html) .

Sample weights should be numeric, non-negative, with larger values indicating which rows are more important than others. Data points that have invalid or no weight value are excluded.

Support for sample weights is available in [Ensembling](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html) mode only.

TextGenerationJobConfig -> (structure)

Settings used to configure an AutoML job V2 for the text generation (LLMs fine-tuning) problem type.

### Note

The text generation models that support fine-tuning in Autopilot are currently accessible exclusively in regions supported by Canvas. Refer to the documentation of Canvas for the [full list of its supported Regions](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html) .

CompletionCriteria -> (structure)

How long a fine-tuning job is allowed to run. For `TextGenerationJobConfig` problem types, the `MaxRuntimePerTrainingJobInSeconds` attribute of `AutoMLJobCompletionCriteria` defaults to 72h (259200s).

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

BaseModelName -> (string)

The name of the base model to fine-tune. Autopilot supports fine-tuning a variety of large language models. For information on the list of supported models, see [Text generation models supporting fine-tuning in Autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-models.html#autopilot-llms-finetuning-supported-llms) . If no `BaseModelName` is provided, the default model used is **Falcon7BInstruct** .

TextGenerationHyperParameters -> (map)

The hyperparameters used to configure and optimize the learning process of the base model. You can set any combination of the following hyperparameters for all base models. For more information on each supported hyperparameter, see [Optimize the learning process of your text generation models with hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-set-hyperparameters.html) .

- `"epochCount"` : The number of times the model goes through the entire training dataset. Its value should be a string containing an integer value within the range of â1â to â10â.
- `"batchSize"` : The number of data samples used in each iteration of training. Its value should be a string containing an integer value within the range of â1â to â64â.
- `"learningRate"` : The step size at which a modelâs parameters are updated during training. Its value should be a string containing a floating-point value within the range of â0â to â1â.
- `"learningRateWarmupSteps"` : The number of training steps during which the learning rate gradually increases before reaching its target or maximum value. Its value should be a string containing an integer value within the range of â0â to â250â.

Here is an example where all four hyperparameters are configured.

`{ "epochCount":"5", "learningRate":"0.5", "batchSize": "32", "learningRateWarmupSteps": "10" }`

key -> (string)

value -> (string)

ModelAccessConfig -> (structure)

The access configuration file to control access to the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` .

- If you are a Jumpstart user, see the [End-user license agreements](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html#jumpstart-foundation-models-choose-eula) section for more details on accepting the EULA.
- If you are an AutoML user, see the *Optional Parameters* section of *Create an AutoML job to fine-tune text generation models using the API* for details on [How to set the EULA acceptance when fine-tuning a model using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-finetune-llms.html#autopilot-llms-finetuning-api-optional-params) .

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

AutoMLProblemTypeConfigName -> (string)

Returns the name of the problem type configuration set for the AutoML job V2.

CreationTime -> (timestamp)

Returns the creation time of the AutoML job V2.

EndTime -> (timestamp)

Returns the end time of the AutoML job V2.

LastModifiedTime -> (timestamp)

Returns the jobâs last modified time.

FailureReason -> (string)

Returns the reason for the failure of the AutoML job V2, when applicable.

PartialFailureReasons -> (list)

Returns a list of reasons for partial failures within an AutoML job V2.

(structure)

The reason for a partial failure of an AutoML job.

PartialFailureMessage -> (string)

The message containing the reason for a partial failure of an AutoML job.

BestCandidate -> (structure)

Information about the candidate produced by an AutoML training job V2, including its status, steps, and other properties.

CandidateName -> (string)

The name of the candidate.

FinalAutoMLJobObjectiveMetric -> (structure)

The best candidate result from an AutoML training job.

Type -> (string)

The type of metric with the best result.

MetricName -> (string)

The name of the metric with the best result. For a description of the possible objective metrics, see [AutoMLJobObjective$MetricName](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobObjective.html) .

Value -> (float)

The value of the metric with the best result.

StandardMetricName -> (string)

The name of the standard metric. For a description of the standard metrics, see [Autopilot candidate metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html#autopilot-metrics) .

ObjectiveStatus -> (string)

The objectiveâs status.

CandidateSteps -> (list)

Information about the candidateâs steps.

(structure)

Information about the steps for a candidate and what step it is working on.

CandidateStepType -> (string)

Whether the candidate is at the transform, training, or processing step.

CandidateStepArn -> (string)

The ARN for the candidateâs step.

CandidateStepName -> (string)

The name for the candidateâs step.

CandidateStatus -> (string)

The candidateâs status.

InferenceContainers -> (list)

Information about the recommended inference container definitions.

(structure)

A list of container definitions that describe the different containers that make up an AutoML candidate. For more information, see [ContainerDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html) .

Image -> (string)

The Amazon Elastic Container Registry (Amazon ECR) path of the container. For more information, see [ContainerDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html) .

ModelDataUrl -> (string)

The location of the model artifacts. For more information, see [ContainerDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html) .

Environment -> (map)

The environment variables to set in the container. For more information, see [ContainerDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html) .

key -> (string)

value -> (string)

CreationTime -> (timestamp)

The creation time.

EndTime -> (timestamp)

The end time.

LastModifiedTime -> (timestamp)

The last modified time.

FailureReason -> (string)

The failure reason.

CandidateProperties -> (structure)

The properties of an AutoML candidate job.

CandidateArtifactLocations -> (structure)

The Amazon S3 prefix to the artifacts generated for an AutoML candidate.

Explainability -> (string)

The Amazon S3 prefix to the explainability artifacts generated for the AutoML candidate.

ModelInsights -> (string)

The Amazon S3 prefix to the model insight artifacts generated for the AutoML candidate.

BacktestResults -> (string)

The Amazon S3 prefix to the accuracy metrics and the inference results observed over the testing window. Available only for the time-series forecasting problem type.

CandidateMetrics -> (list)

Information about the candidate metrics for an AutoML job.

(structure)

Information about the metric for a candidate produced by an AutoML job.

MetricName -> (string)

The name of the metric.

StandardMetricName -> (string)

The name of the standard metric.

### Note

For definitions of the standard metrics, see ` `Autopilot candidate metrics` [https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot)-metrics`__ .

Value -> (float)

The value of the metric.

Set -> (string)

The dataset split from which the AutoML job produced the metric.

InferenceContainerDefinitions -> (map)

The mapping of all supported processing unit (CPU, GPU, etcâ¦) to inference container definitions for the candidate. This field is populated for the AutoML jobs V2 (for example, for jobs created by calling `CreateAutoMLJobV2` ) related to image or text classification problem types only.

key -> (string)

Processing unit for an inference container. Currently Autopilot only supports `CPU` or `GPU` .

value -> (list)

Information about the recommended inference container definitions.

(structure)

A list of container definitions that describe the different containers that make up an AutoML candidate. For more information, see [ContainerDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html) .

Image -> (string)

The Amazon Elastic Container Registry (Amazon ECR) path of the container. For more information, see [ContainerDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html) .

ModelDataUrl -> (string)

The location of the model artifacts. For more information, see [ContainerDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html) .

Environment -> (map)

The environment variables to set in the container. For more information, see [ContainerDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html) .

key -> (string)

value -> (string)

AutoMLJobStatus -> (string)

Returns the status of the AutoML job V2.

AutoMLJobSecondaryStatus -> (string)

Returns the secondary status of the AutoML job V2.

AutoMLJobArtifacts -> (structure)

The artifacts that are generated during an AutoML job.

CandidateDefinitionNotebookLocation -> (string)

The URL of the notebook location.

DataExplorationNotebookLocation -> (string)

The URL of the notebook location.

ResolvedAttributes -> (structure)

Returns the resolved attributes used by the AutoML job V2.

AutoMLJobObjective -> (structure)

Specifies a metric to minimize or maximize as the objective of an AutoML job.

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

CompletionCriteria -> (structure)

How long a job is allowed to run, or how many candidates a job is allowed to generate.

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

AutoMLProblemTypeResolvedAttributes -> (tagged union structure)

Defines the resolved attributes specific to a problem type.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `TabularResolvedAttributes`, `TextGenerationResolvedAttributes`.

TabularResolvedAttributes -> (structure)

The resolved attributes for the tabular problem type.

ProblemType -> (string)

The type of supervised learning problem available for the model candidates of the AutoML job V2 (Binary Classification, Multiclass Classification, Regression). For more information, see [SageMaker Autopilot problem types](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-datasets-problem-types.html#autopilot-problem-types) .

TextGenerationResolvedAttributes -> (structure)

The resolved attributes for the text generation problem type.

BaseModelName -> (string)

The name of the base model to fine-tune.

ModelDeployConfig -> (structure)

Indicates whether the model was deployed automatically to an endpoint and the name of that endpoint if deployed automatically.

AutoGenerateEndpointName -> (boolean)

Set to `True` to automatically generate an endpoint name for a one-click Autopilot model deployment; set to `False` otherwise. The default value is `False` .

### Note

If you set `AutoGenerateEndpointName` to `True` , do not specify the `EndpointName` ; otherwise a 400 error is thrown.

EndpointName -> (string)

Specifies the endpoint name to use for a one-click Autopilot model deployment if the endpoint name is not generated automatically.

### Note

Specify the `EndpointName` if and only if you set `AutoGenerateEndpointName` to `False` ; otherwise a 400 error is thrown.

ModelDeployResult -> (structure)

Provides information about endpoint for the model deployment.

EndpointName -> (string)

The name of the endpoint to which the model has been deployed.

### Note

If model deployment fails, this field is omitted from the response.

DataSplitConfig -> (structure)

Returns the configuration settings of how the data are split into train and validation datasets.

ValidationFraction -> (float)

The validation fraction (optional) is a float that specifies the portion of the training dataset to be used for validation. The default value is 0.2, and values must be greater than 0 and less than 1. We recommend setting this value to be less than 0.5.

SecurityConfig -> (structure)

Returns the security configuration for traffic encryption or Amazon VPC settings.

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

AutoMLComputeConfig -> (structure)

The compute configuration used for the AutoML job V2.

EmrServerlessComputeConfig -> (structure)

The configuration for using [EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html) to run the AutoML job V2.

To allow your AutoML job V2 to automatically initiate a remote job on EMR Serverless when additional compute resources are needed to process large datasets, you need to provide an `EmrServerlessComputeConfig` object, which includes an `ExecutionRoleARN` attribute, to the `AutoMLComputeConfig` of the AutoML job V2 input request.

By seamlessly transitioning to EMR Serverless when required, the AutoML job can handle datasets that would otherwise exceed the initially provisioned resources, without any manual intervention from you.

EMR Serverless is available for the tabular and time series problem types. We recommend setting up this option for tabular datasets larger than 5 GB and time series datasets larger than 30 GB.

ExecutionRoleARN -> (string)

The ARN of the IAM role granting the AutoML job V2 the necessary permissions access policies to list, connect to, or manage EMR Serverless jobs. For detailed information about the required permissions of this role, see âHow to configure AutoML to initiate a remote job on EMR Serverless for large datasetsâ in [Create a regression or classification job for tabular data using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-create-experiment.html) or [Create an AutoML job for time-series forecasting using the API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-timeseries-forecasting.html#timeseries-forecasting-api-optional-params) .