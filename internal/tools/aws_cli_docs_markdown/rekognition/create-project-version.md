# create-project-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-project-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-project-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# create-project-version

## Description

Creates a new version of Amazon Rekognition project (like a Custom Labels model or a custom adapter) and begins training. Models and adapters are managed as part of a Rekognition project. The response from `CreateProjectVersion` is an Amazon Resource Name (ARN) for the project version.

The FeatureConfig operation argument allows you to configure specific model or adapter settings. You can provide a description to the project version by using the VersionDescription argment. Training can take a while to complete. You can get the current status by calling  DescribeProjectVersions . Training completed successfully if the value of the `Status` field is `TRAINING_COMPLETED` . Once training has successfully completed, call  DescribeProjectVersions to get the training results and evaluate the model.

This operation requires permissions to perform the `rekognition:CreateProjectVersion` action.

### Note

*The following applies only to projects with Amazon Rekognition Custom Labels as the chosen feature:*

You can train a model in a project that doesnât have associated datasets by specifying manifest files in the `TrainingData` and `TestingData` fields.

If you open the console after training a model with manifest files, Amazon Rekognition Custom Labels creates the datasets for you using the most recent manifest files. You can no longer train a model version for the project by specifying manifest files.

Instead of training with a project without associated datasets, we recommend that you use the manifest files to create training and test datasets for the project.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/CreateProjectVersion)

## Synopsis

```
create-project-version
--project-arn <value>
--version-name <value>
--output-config <value>
[--training-data <value>]
[--testing-data <value>]
[--tags <value>]
[--kms-key-id <value>]
[--version-description <value>]
[--feature-config <value>]
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

`--project-arn` (string)

The ARN of the Amazon Rekognition project that will manage the project version you want to train.

`--version-name` (string)

A name for the version of the project version. This value must be unique.

`--output-config` (structure)

The Amazon S3 bucket location to store the results of training. The bucket can be any S3 bucket in your AWS account. You need `s3:PutObject` permission on the bucket.

S3Bucket -> (string)

The S3 bucket where training output is placed.

S3KeyPrefix -> (string)

The prefix applied to the training output files.

Shorthand Syntax:

```
S3Bucket=string,S3KeyPrefix=string
```

JSON Syntax:

```
{
  "S3Bucket": "string",
  "S3KeyPrefix": "string"
}
```

`--training-data` (structure)

Specifies an external manifest that the services uses to train the project version. If you specify `TrainingData` you must also specify `TestingData` . The project must not have any associated datasets.

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

JSON Syntax:

```
{
  "Assets": [
    {
      "GroundTruthManifest": {
        "S3Object": {
          "Bucket": "string",
          "Name": "string",
          "Version": "string"
        }
      }
    }
    ...
  ]
}
```

`--testing-data` (structure)

Specifies an external manifest that the service uses to test the project version. If you specify `TestingData` you must also specify `TrainingData` . The project must not have any associated datasets.

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

JSON Syntax:

```
{
  "Assets": [
    {
      "GroundTruthManifest": {
        "S3Object": {
          "Bucket": "string",
          "Name": "string",
          "Version": "string"
        }
      }
    }
    ...
  ],
  "AutoCreate": true|false
}
```

`--tags` (map)

A set of tags (key-value pairs) that you want to attach to the project version.

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

`--kms-key-id` (string)

The identifier for your AWS Key Management Service key (AWS KMS key). You can supply the Amazon Resource Name (ARN) of your KMS key, the ID of your KMS key, an alias for your KMS key, or an alias ARN. The key is used to encrypt training images, test images, and manifest files copied into the service for the project version. Your source images are unaffected. The key is also used to encrypt training results and manifest files written to the output Amazon S3 bucket (`OutputConfig` ).

If you choose to use your own KMS key, you need the following permissions on the KMS key.

- kms:CreateGrant
- kms:DescribeKey
- kms:GenerateDataKey
- kms:Decrypt

If you donât specify a value for `KmsKeyId` , images copied into the service are encrypted using a key that AWS owns and manages.

`--version-description` (string)

A description applied to the project version being created.

`--feature-config` (structure)

Feature-specific configuration of the training job. If the job configuration does not match the feature type associated with the project, an InvalidParameterException is returned.

ContentModeration -> (structure)

Configuration options for Custom Moderation training.

ConfidenceThreshold -> (float)

The confidence level you plan to use to identify if unsafe content is present during inference.

Shorthand Syntax:

```
ContentModeration={ConfidenceThreshold=float}
```

JSON Syntax:

```
{
  "ContentModeration": {
    "ConfidenceThreshold": float
  }
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

ProjectVersionArn -> (string)

The ARN of the model or the project version that was created. Use `DescribeProjectVersion` to get the current status of the training operation.