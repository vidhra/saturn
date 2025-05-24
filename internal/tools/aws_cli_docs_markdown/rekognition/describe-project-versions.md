# describe-project-versionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-project-versions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-project-versions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# describe-project-versions

## Description

Lists and describes the versions of an Amazon Rekognition project. You can specify up to 10 model or adapter versions in `ProjectVersionArns` . If you donât specify a value, descriptions for all model/adapter versions in the project are returned.

This operation requires permissions to perform the `rekognition:DescribeProjectVersions` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DescribeProjectVersions)

`describe-project-versions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ProjectVersionDescriptions`

## Synopsis

```
describe-project-versions
--project-arn <value>
[--version-names <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--project-arn` (string)

The Amazon Resource Name (ARN) of the project that contains the model/adapter you want to describe.

`--version-names` (list)

A list of model or project version names that you want to describe. You can add up to 10 model or project version names to the list. If you donât specify a value, all project version descriptions are returned. A version name is part of a project version ARN. For example, `my-model.2020-01-21T09.10.15` is the version name in the following ARN. `arn:aws:rekognition:us-east-1:123456789012:project/getting-started/version/*my-model.2020-01-21T09.10.15* /1234567890123` .

(string)

Syntax:

```
"string" "string" ...
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

ProjectVersionDescriptions -> (list)

A list of project version descriptions. The list is sorted by the creation date and time of the project versions, latest to earliest.

(structure)

A description of a version of a Amazon Rekognition project version.

ProjectVersionArn -> (string)

The Amazon Resource Name (ARN) of the project version.

CreationTimestamp -> (timestamp)

The Unix datetime for the date and time that training started.

MinInferenceUnits -> (integer)

The minimum number of inference units used by the model. Applies only to Custom Labels projects. For more information, see  StartProjectVersion .

Status -> (string)

The current status of the model version.

StatusMessage -> (string)

A descriptive message for an error or warning that occurred.

BillableTrainingTimeInSeconds -> (long)

The duration, in seconds, that you were billed for a successful training of the model version. This value is only returned if the model version has been successfully trained.

TrainingEndTimestamp -> (timestamp)

The Unix date and time that training of the model ended.

OutputConfig -> (structure)

The location where training results are saved.

S3Bucket -> (string)

The S3 bucket where training output is placed.

S3KeyPrefix -> (string)

The prefix applied to the training output files.

TrainingDataResult -> (structure)

Contains information about the training results.

Input -> (structure)

The training data that you supplied.

Assets -> (list)

A manifest file that contains references to the training images and ground-truth annotations.

(structure)

Assets are the images that you use to train and evaluate a model version. Assets can also contain validation information that you use to debug a failed model training.

GroundTruthManifest -> (structure)

The S3 bucket that contains an Amazon Sagemaker Ground Truth format manifest file.

S3Object -> (structure)

Provides the S3 bucket name and object name.

The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.

For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see How Amazon Rekognition works with IAM in the Amazon Rekognition Developer Guide.

Bucket -> (string)

Name of the S3 bucket.

Name -> (string)

S3 object key name.

Version -> (string)

If the bucket is versioning enabled, you can specify the object version.

Output -> (structure)

Reference to images (assets) that were actually used during training with trained model predictions.

Assets -> (list)

A manifest file that contains references to the training images and ground-truth annotations.

(structure)

Assets are the images that you use to train and evaluate a model version. Assets can also contain validation information that you use to debug a failed model training.

GroundTruthManifest -> (structure)

The S3 bucket that contains an Amazon Sagemaker Ground Truth format manifest file.

S3Object -> (structure)

Provides the S3 bucket name and object name.

The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.

For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see How Amazon Rekognition works with IAM in the Amazon Rekognition Developer Guide.

Bucket -> (string)

Name of the S3 bucket.

Name -> (string)

S3 object key name.

Version -> (string)

If the bucket is versioning enabled, you can specify the object version.

Validation -> (structure)

A manifest that you supplied for training, with validation results for each line.

Assets -> (list)

The assets that comprise the validation data.

(structure)

Assets are the images that you use to train and evaluate a model version. Assets can also contain validation information that you use to debug a failed model training.

GroundTruthManifest -> (structure)

The S3 bucket that contains an Amazon Sagemaker Ground Truth format manifest file.

S3Object -> (structure)

Provides the S3 bucket name and object name.

The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.

For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see How Amazon Rekognition works with IAM in the Amazon Rekognition Developer Guide.

Bucket -> (string)

Name of the S3 bucket.

Name -> (string)

S3 object key name.

Version -> (string)

If the bucket is versioning enabled, you can specify the object version.

TestingDataResult -> (structure)

Contains information about the testing results.

Input -> (structure)

The testing dataset that was supplied for training.

Assets -> (list)

The assets used for testing.

(structure)

Assets are the images that you use to train and evaluate a model version. Assets can also contain validation information that you use to debug a failed model training.

GroundTruthManifest -> (structure)

The S3 bucket that contains an Amazon Sagemaker Ground Truth format manifest file.

S3Object -> (structure)

Provides the S3 bucket name and object name.

The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.

For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see How Amazon Rekognition works with IAM in the Amazon Rekognition Developer Guide.

Bucket -> (string)

Name of the S3 bucket.

Name -> (string)

S3 object key name.

Version -> (string)

If the bucket is versioning enabled, you can specify the object version.

AutoCreate -> (boolean)

If specified, Rekognition splits training dataset to create a test dataset for the training job.

Output -> (structure)

The subset of the dataset that was actually tested. Some images (assets) might not be tested due to file formatting and other issues.

Assets -> (list)

The assets used for testing.

(structure)

Assets are the images that you use to train and evaluate a model version. Assets can also contain validation information that you use to debug a failed model training.

GroundTruthManifest -> (structure)

The S3 bucket that contains an Amazon Sagemaker Ground Truth format manifest file.

S3Object -> (structure)

Provides the S3 bucket name and object name.

The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.

For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see How Amazon Rekognition works with IAM in the Amazon Rekognition Developer Guide.

Bucket -> (string)

Name of the S3 bucket.

Name -> (string)

S3 object key name.

Version -> (string)

If the bucket is versioning enabled, you can specify the object version.

AutoCreate -> (boolean)

If specified, Rekognition splits training dataset to create a test dataset for the training job.

Validation -> (structure)

The location of the data validation manifest. The data validation manifest is created for the test dataset during model training.

Assets -> (list)

The assets that comprise the validation data.

(structure)

Assets are the images that you use to train and evaluate a model version. Assets can also contain validation information that you use to debug a failed model training.

GroundTruthManifest -> (structure)

The S3 bucket that contains an Amazon Sagemaker Ground Truth format manifest file.

S3Object -> (structure)

Provides the S3 bucket name and object name.

The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.

For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see How Amazon Rekognition works with IAM in the Amazon Rekognition Developer Guide.

Bucket -> (string)

Name of the S3 bucket.

Name -> (string)

S3 object key name.

Version -> (string)

If the bucket is versioning enabled, you can specify the object version.

EvaluationResult -> (structure)

The training results. `EvaluationResult` is only returned if training is successful.

F1Score -> (float)

The F1 score for the evaluation of all labels. The F1 score metric evaluates the overall precision and recall performance of the model as a single value. A higher value indicates better precision and recall performance. A lower score indicates that precision, recall, or both are performing poorly.

Summary -> (structure)

The S3 bucket that contains the training summary.

S3Object -> (structure)

Provides the S3 bucket name and object name.

The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.

For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see How Amazon Rekognition works with IAM in the Amazon Rekognition Developer Guide.

Bucket -> (string)

Name of the S3 bucket.

Name -> (string)

S3 object key name.

Version -> (string)

If the bucket is versioning enabled, you can specify the object version.

ManifestSummary -> (structure)

The location of the summary manifest. The summary manifest provides aggregate data validation results for the training and test datasets.

S3Object -> (structure)

Provides the S3 bucket name and object name.

The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.

For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see How Amazon Rekognition works with IAM in the Amazon Rekognition Developer Guide.

Bucket -> (string)

Name of the S3 bucket.

Name -> (string)

S3 object key name.

Version -> (string)

If the bucket is versioning enabled, you can specify the object version.

KmsKeyId -> (string)

The identifer for the AWS Key Management Service key (AWS KMS key) that was used to encrypt the model during training.

MaxInferenceUnits -> (integer)

The maximum number of inference units Amazon Rekognition uses to auto-scale the model. Applies only to Custom Labels projects. For more information, see  StartProjectVersion .

SourceProjectVersionArn -> (string)

If the model version was copied from a different project, `SourceProjectVersionArn` contains the ARN of the source model version.

VersionDescription -> (string)

A user-provided description of the project version.

Feature -> (string)

The feature that was customized.

BaseModelVersion -> (string)

The base detection model version used to create the project version.

FeatureConfig -> (structure)

Feature specific configuration that was applied during training.

ContentModeration -> (structure)

Configuration options for Custom Moderation training.

ConfidenceThreshold -> (float)

The confidence level you plan to use to identify if unsafe content is present during inference.

NextToken -> (string)

If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.