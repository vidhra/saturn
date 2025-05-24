# list-modelsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/list-models.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/list-models.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutequipment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/index.html#cli-aws-lookoutequipment) ]

# list-models

## Description

Generates a list of all models in the account, including model name and ARN, dataset, and status.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutequipment-2020-12-15/ListModels)

## Synopsis

```
list-models
[--next-token <value>]
[--max-results <value>]
[--status <value>]
[--model-name-begins-with <value>]
[--dataset-name-begins-with <value>]
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

`--next-token` (string)

An opaque pagination token indicating where to continue the listing of machine learning models.

`--max-results` (integer)

Specifies the maximum number of machine learning models to list.

`--status` (string)

The status of the machine learning model.

Possible values:

- `IN_PROGRESS`
- `SUCCESS`
- `FAILED`
- `IMPORT_IN_PROGRESS`

`--model-name-begins-with` (string)

The beginning of the name of the machine learning models being listed.

`--dataset-name-begins-with` (string)

The beginning of the name of the dataset of the machine learning models to be listed.

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

NextToken -> (string)

An opaque pagination token indicating where to continue the listing of machine learning models.

ModelSummaries -> (list)

Provides information on the specified model, including created time, model and dataset ARNs, and status.

(structure)

Provides information about the specified machine learning model, including dataset and model names and ARNs, as well as status.

ModelName -> (string)

The name of the machine learning model.

ModelArn -> (string)

The Amazon Resource Name (ARN) of the machine learning model.

DatasetName -> (string)

The name of the dataset being used for the machine learning model.

DatasetArn -> (string)

The Amazon Resource Name (ARN) of the dataset used to create the model.

Status -> (string)

Indicates the status of the machine learning model.

CreatedAt -> (timestamp)

The time at which the specific model was created.

ActiveModelVersion -> (long)

The model version that the inference scheduler uses to run an inference execution.

ActiveModelVersionArn -> (string)

The Amazon Resource Name (ARN) of the model version that is set as active. The active model version is the model version that the inference scheduler uses to run an inference execution.

LatestScheduledRetrainingStatus -> (string)

Indicates the status of the most recent scheduled retraining run.

LatestScheduledRetrainingModelVersion -> (long)

Indicates the most recent model version that was generated by retraining.

LatestScheduledRetrainingStartTime -> (timestamp)

Indicates the start time of the most recent scheduled retraining run.

NextScheduledRetrainingStartDate -> (timestamp)

Indicates the date that the next scheduled retraining run will start on. Lookout for Equipment truncates the time you provide to [the nearest UTC day](https://docs.aws.amazon.com/https:/docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp) .

RetrainingSchedulerStatus -> (string)

Indicates the status of the retraining scheduler.

ModelDiagnosticsOutputConfiguration -> (structure)

Output configuration information for the pointwise model diagnostics for an Amazon Lookout for Equipment model.

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