# describe-modelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/describe-model.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/describe-model.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutequipment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/index.html#cli-aws-lookoutequipment) ]

# describe-model

## Description

Provides a JSON containing the overall information about a specific machine learning model, including model name and ARN, dataset, training and evaluation information, status, and so on.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutequipment-2020-12-15/DescribeModel)

## Synopsis

```
describe-model
--model-name <value>
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

`--model-name` (string)

The name of the machine learning model to be described.

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

ModelName -> (string)

The name of the machine learning model being described.

ModelArn -> (string)

The Amazon Resource Name (ARN) of the machine learning model being described.

DatasetName -> (string)

The name of the dataset being used by the machine learning being described.

DatasetArn -> (string)

The Amazon Resouce Name (ARN) of the dataset used to create the machine learning model being described.

Schema -> (string)

A JSON description of the data that is in each time series dataset, including names, column names, and data types.

LabelsInputConfiguration -> (structure)

Specifies configuration information about the labels input, including its S3 location.

S3InputConfiguration -> (structure)

Contains location information for the S3 location being used for label data.

Bucket -> (string)

The name of the S3 bucket holding the label data.

Prefix -> (string)

The prefix for the S3 bucket used for the label data.

LabelGroupName -> (string)

The name of the label group to be used for label data.

TrainingDataStartTime -> (timestamp)

Indicates the time reference in the dataset that was used to begin the subset of training data for the machine learning model.

TrainingDataEndTime -> (timestamp)

Indicates the time reference in the dataset that was used to end the subset of training data for the machine learning model.

EvaluationDataStartTime -> (timestamp)

Indicates the time reference in the dataset that was used to begin the subset of evaluation data for the machine learning model.

EvaluationDataEndTime -> (timestamp)

Indicates the time reference in the dataset that was used to end the subset of evaluation data for the machine learning model.

RoleArn -> (string)

The Amazon Resource Name (ARN) of a role with permission to access the data source for the machine learning model being described.

DataPreProcessingConfiguration -> (structure)

The configuration is the `TargetSamplingRate` , which is the sampling rate of the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been collected at a 1 second level and you want the system to resample the data at a 1 minute rate before training, the `TargetSamplingRate` is 1 minute.

When providing a value for the `TargetSamplingRate` , you must attach the prefix âPTâ to the rate you want. The value for a 1 second rate is therefore *PT1S* , the value for a 15 minute rate is *PT15M* , and the value for a 1 hour rate is *PT1H*

TargetSamplingRate -> (string)

The sampling rate of the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been collected at a 1 second level and you want the system to resample the data at a 1 minute rate before training, the `TargetSamplingRate` is 1 minute.

When providing a value for the `TargetSamplingRate` , you must attach the prefix âPTâ to the rate you want. The value for a 1 second rate is therefore *PT1S* , the value for a 15 minute rate is *PT15M* , and the value for a 1 hour rate is *PT1H*

Status -> (string)

Specifies the current status of the model being described. Status describes the status of the most recent action of the model.

TrainingExecutionStartTime -> (timestamp)

Indicates the time at which the training of the machine learning model began.

TrainingExecutionEndTime -> (timestamp)

Indicates the time at which the training of the machine learning model was completed.

FailedReason -> (string)

If the training of the machine learning model failed, this indicates the reason for that failure.

ModelMetrics -> (string)

The Model Metrics show an aggregated summary of the modelâs performance within the evaluation time range. This is the JSON content of the metrics created when evaluating the model.

LastUpdatedTime -> (timestamp)

Indicates the last time the machine learning model was updated. The type of update is not specified.

CreatedAt -> (timestamp)

Indicates the time and date at which the machine learning model was created.

ServerSideKmsKeyId -> (string)

Provides the identifier of the KMS key used to encrypt model data by Amazon Lookout for Equipment.

OffCondition -> (string)

Indicates that the asset associated with this sensor has been shut off. As long as this condition is met, Lookout for Equipment will not use data from this asset for training, evaluation, or inference.

SourceModelVersionArn -> (string)

The Amazon Resource Name (ARN) of the source model version. This field appears if the active model version was imported.

ImportJobStartTime -> (timestamp)

The date and time when the import job was started. This field appears if the active model version was imported.

ImportJobEndTime -> (timestamp)

The date and time when the import job was completed. This field appears if the active model version was imported.

ActiveModelVersion -> (long)

The name of the model version used by the inference schedular when running a scheduled inference execution.

ActiveModelVersionArn -> (string)

The Amazon Resource Name (ARN) of the model version used by the inference scheduler when running a scheduled inference execution.

ModelVersionActivatedAt -> (timestamp)

The date the active model version was activated.

PreviousActiveModelVersion -> (long)

The model version that was set as the active model version prior to the current active model version.

PreviousActiveModelVersionArn -> (string)

The ARN of the model version that was set as the active model version prior to the current active model version.

PreviousModelVersionActivatedAt -> (timestamp)

The date and time when the previous active model version was activated.

PriorModelMetrics -> (string)

If the model version was retrained, this field shows a summary of the performance of the prior model on the new training range. You can use the information in this JSON-formatted object to compare the new model version and the prior model version.

LatestScheduledRetrainingFailedReason -> (string)

If the model version was generated by retraining and the training failed, this indicates the reason for that failure.

LatestScheduledRetrainingStatus -> (string)

Indicates the status of the most recent scheduled retraining run.

LatestScheduledRetrainingModelVersion -> (long)

Indicates the most recent model version that was generated by retraining.

LatestScheduledRetrainingStartTime -> (timestamp)

Indicates the start time of the most recent scheduled retraining run.

LatestScheduledRetrainingAvailableDataInDays -> (integer)

Indicates the number of days of data used in the most recent scheduled retraining run.

NextScheduledRetrainingStartDate -> (timestamp)

Indicates the date and time that the next scheduled retraining run will start on. Lookout for Equipment truncates the time you provide to the nearest UTC day.

AccumulatedInferenceDataStartTime -> (timestamp)

Indicates the start time of the inference data that has been accumulated.

AccumulatedInferenceDataEndTime -> (timestamp)

Indicates the end time of the inference data that has been accumulated.

RetrainingSchedulerStatus -> (string)

Indicates the status of the retraining scheduler.

ModelDiagnosticsOutputConfiguration -> (structure)

Configuration information for the modelâs pointwise model diagnostics.

S3OutputConfiguration -> (structure)

The Amazon S3 location for the pointwise model diagnostics.

Bucket -> (string)

The name of the Amazon S3 bucket where the pointwise model diagnostics are located. You must be the owner of the Amazon S3 bucket.

Prefix -> (string)

The Amazon S3 prefix for the location of the pointwise model diagnostics. The prefix specifies the folder and evaluation result file name. (`bucket` ).

When you call `CreateModel` or `UpdateModel` , specify the path within the bucket that you want Lookout for Equipment to save the model to. During training, Lookout for Equipment creates the model evaluation model as a compressed JSON file with the name `model_diagnostics_results.json.gz` .

When you call `DescribeModel` or `DescribeModelVersion` , `prefix` contains the file path and filename of the model evaluation file.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (KMS) key identifier to encrypt the pointwise model diagnostics files.

ModelQuality -> (string)

Provides a quality assessment for a model that uses labels. If Lookout for Equipment determines that the model quality is poor based on training metrics, the value is `POOR_QUALITY_DETECTED` . Otherwise, the value is `QUALITY_THRESHOLD_MET` .

If the model is unlabeled, the model quality canât be assessed and the value of `ModelQuality` is `CANNOT_DETERMINE_QUALITY` . In this situation, you can get a model quality assessment by adding labels to the input dataset and retraining the model.

For information about using labels with your models, see [Understanding labeling](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-labeling.html) .

For information about improving the quality of a model, see [Best practices with Amazon Lookout for Equipment](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/best-practices.html) .