# describe-model-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/describe-model-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/describe-model-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutequipment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/index.html#cli-aws-lookoutequipment) ]

# describe-model-version

## Description

Retrieves information about a specific machine learning model version.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutequipment-2020-12-15/DescribeModelVersion)

## Synopsis

```
describe-model-version
--model-name <value>
--model-version <value>
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

The name of the machine learning model that this version belongs to.

`--model-version` (long)

The version of the machine learning model.

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

The name of the machine learning model that this version belongs to.

ModelArn -> (string)

The Amazon Resource Name (ARN) of the parent machine learning model that this version belong to.

ModelVersion -> (long)

The version of the machine learning model.

ModelVersionArn -> (string)

The Amazon Resource Name (ARN) of the model version.

Status -> (string)

The current status of the model version.

SourceType -> (string)

Indicates whether this model version was created by training or by importing.

DatasetName -> (string)

The name of the dataset used to train the model version.

DatasetArn -> (string)

The Amazon Resource Name (ARN) of the dataset used to train the model version.

Schema -> (string)

The schema of the data used to train the model version.

LabelsInputConfiguration -> (structure)

Contains the configuration information for the S3 location being used to hold label data.

S3InputConfiguration -> (structure)

Contains location information for the S3 location being used for label data.

Bucket -> (string)

The name of the S3 bucket holding the label data.

Prefix -> (string)

The prefix for the S3 bucket used for the label data.

LabelGroupName -> (string)

The name of the label group to be used for label data.

TrainingDataStartTime -> (timestamp)

The date on which the training data began being gathered. If you imported the version, this is the date that the training data in the source version began being gathered.

TrainingDataEndTime -> (timestamp)

The date on which the training data finished being gathered. If you imported the version, this is the date that the training data in the source version finished being gathered.

EvaluationDataStartTime -> (timestamp)

The date on which the data in the evaluation set began being gathered. If you imported the version, this is the date that the evaluation set data in the source version began being gathered.

EvaluationDataEndTime -> (timestamp)

The date on which the data in the evaluation set began being gathered. If you imported the version, this is the date that the evaluation set data in the source version finished being gathered.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the role that was used to train the model version.

DataPreProcessingConfiguration -> (structure)

The configuration is the `TargetSamplingRate` , which is the sampling rate of the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been collected at a 1 second level and you want the system to resample the data at a 1 minute rate before training, the `TargetSamplingRate` is 1 minute.

When providing a value for the `TargetSamplingRate` , you must attach the prefix âPTâ to the rate you want. The value for a 1 second rate is therefore *PT1S* , the value for a 15 minute rate is *PT15M* , and the value for a 1 hour rate is *PT1H*

TargetSamplingRate -> (string)

The sampling rate of the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been collected at a 1 second level and you want the system to resample the data at a 1 minute rate before training, the `TargetSamplingRate` is 1 minute.

When providing a value for the `TargetSamplingRate` , you must attach the prefix âPTâ to the rate you want. The value for a 1 second rate is therefore *PT1S* , the value for a 15 minute rate is *PT15M* , and the value for a 1 hour rate is *PT1H*

TrainingExecutionStartTime -> (timestamp)

The time when the training of the version began.

TrainingExecutionEndTime -> (timestamp)

The time when the training of the version completed.

FailedReason -> (string)

The failure message if the training of the model version failed.

ModelMetrics -> (string)

Shows an aggregated summary, in JSON format, of the modelâs performance within the evaluation time range. These metrics are created when evaluating the model.

LastUpdatedTime -> (timestamp)

Indicates the last time the machine learning model version was updated.

CreatedAt -> (timestamp)

Indicates the time and date at which the machine learning model version was created.

ServerSideKmsKeyId -> (string)

The identifier of the KMS key key used to encrypt model version data by Amazon Lookout for Equipment.

OffCondition -> (string)

Indicates that the asset associated with this sensor has been shut off. As long as this condition is met, Lookout for Equipment will not use data from this asset for training, evaluation, or inference.

SourceModelVersionArn -> (string)

If model version was imported, then this field is the arn of the source model version.

ImportJobStartTime -> (timestamp)

The date and time when the import job began. This field appears if the model version was imported.

ImportJobEndTime -> (timestamp)

The date and time when the import job completed. This field appears if the model version was imported.

ImportedDataSizeInBytes -> (long)

The size in bytes of the imported data. This field appears if the model version was imported.

PriorModelMetrics -> (string)

If the model version was retrained, this field shows a summary of the performance of the prior model on the new training range. You can use the information in this JSON-formatted object to compare the new model version and the prior model version.

RetrainingAvailableDataInDays -> (integer)

Indicates the number of days of data used in the most recent scheduled retraining run.

AutoPromotionResult -> (string)

Indicates whether the model version was promoted to be the active version after retraining or if there was an error with or cancellation of the retraining.

AutoPromotionResultReason -> (string)

Indicates the reason for the `AutoPromotionResult` . For example, a model might not be promoted if its performance was worse than the active version, if there was an error during training, or if the retraining scheduler was using `MANUAL` promote mode. The model will be promoted in `MANAGED` promote mode if the performance is better than the previous model.

ModelDiagnosticsOutputConfiguration -> (structure)

The Amazon S3 location where Amazon Lookout for Equipment saves the pointwise model diagnostics for the model version.

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

ModelDiagnosticsResultsObject -> (structure)

The Amazon S3 output prefix for where Lookout for Equipment saves the pointwise model diagnostics for the model version.

Bucket -> (string)

The name of the specific S3 bucket.

Key -> (string)

The Amazon Web Services Key Management Service (KMS key) key being used to encrypt the S3 object. Without this key, data in the bucket is not accessible.

ModelQuality -> (string)

Provides a quality assessment for a model that uses labels. If Lookout for Equipment determines that the model quality is poor based on training metrics, the value is `POOR_QUALITY_DETECTED` . Otherwise, the value is `QUALITY_THRESHOLD_MET` .

If the model is unlabeled, the model quality canât be assessed and the value of `ModelQuality` is `CANNOT_DETERMINE_QUALITY` . In this situation, you can get a model quality assessment by adding labels to the input dataset and retraining the model.

For information about using labels with your models, see [Understanding labeling](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-labeling.html) .

For information about improving the quality of a model, see [Best practices with Amazon Lookout for Equipment](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/best-practices.html) .