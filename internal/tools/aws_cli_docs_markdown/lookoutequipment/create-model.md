# create-modelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/create-model.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/create-model.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutequipment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/index.html#cli-aws-lookoutequipment) ]

# create-model

## Description

Creates a machine learning model for data inference.

A machine-learning (ML) model is a mathematical model that finds patterns in your data. In Amazon Lookout for Equipment, the model learns the patterns of normal behavior and detects abnormal behavior that could be potential equipment failure (or maintenance events). The models are made by analyzing normal data and abnormalities in machine behavior that have already occurred.

Your model is trained using a portion of the data from your dataset and uses that data to learn patterns of normal behavior and abnormal patterns that lead to equipment failure. Another portion of the data is used to evaluate the modelâs accuracy.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutequipment-2020-12-15/CreateModel)

## Synopsis

```
create-model
--model-name <value>
--dataset-name <value>
[--dataset-schema <value>]
[--labels-input-configuration <value>]
[--client-token <value>]
[--training-data-start-time <value>]
[--training-data-end-time <value>]
[--evaluation-data-start-time <value>]
[--evaluation-data-end-time <value>]
[--role-arn <value>]
[--data-pre-processing-configuration <value>]
[--server-side-kms-key-id <value>]
[--tags <value>]
[--off-condition <value>]
[--model-diagnostics-output-configuration <value>]
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

The name for the machine learning model to be created.

`--dataset-name` (string)

The name of the dataset for the machine learning model being created.

`--dataset-schema` (structure)

The data schema for the machine learning model being created.

InlineDataSchema -> (string)

The data schema used within the given dataset.

Shorthand Syntax:

```
InlineDataSchema=string
```

JSON Syntax:

```
{
  "InlineDataSchema": "string"
}
```

`--labels-input-configuration` (structure)

The input configuration for the labels being used for the machine learning model thatâs being created.

S3InputConfiguration -> (structure)

Contains location information for the S3 location being used for label data.

Bucket -> (string)

The name of the S3 bucket holding the label data.

Prefix -> (string)

The prefix for the S3 bucket used for the label data.

LabelGroupName -> (string)

The name of the label group to be used for label data.

Shorthand Syntax:

```
S3InputConfiguration={Bucket=string,Prefix=string},LabelGroupName=string
```

JSON Syntax:

```
{
  "S3InputConfiguration": {
    "Bucket": "string",
    "Prefix": "string"
  },
  "LabelGroupName": "string"
}
```

`--client-token` (string)

A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one.

`--training-data-start-time` (timestamp)

Indicates the time reference in the dataset that should be used to begin the subset of training data for the machine learning model.

`--training-data-end-time` (timestamp)

Indicates the time reference in the dataset that should be used to end the subset of training data for the machine learning model.

`--evaluation-data-start-time` (timestamp)

Indicates the time reference in the dataset that should be used to begin the subset of evaluation data for the machine learning model.

`--evaluation-data-end-time` (timestamp)

Indicates the time reference in the dataset that should be used to end the subset of evaluation data for the machine learning model.

`--role-arn` (string)

The Amazon Resource Name (ARN) of a role with permission to access the data source being used to create the machine learning model.

`--data-pre-processing-configuration` (structure)

The configuration is the `TargetSamplingRate` , which is the sampling rate of the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been collected at a 1 second level and you want the system to resample the data at a 1 minute rate before training, the `TargetSamplingRate` is 1 minute.

When providing a value for the `TargetSamplingRate` , you must attach the prefix âPTâ to the rate you want. The value for a 1 second rate is therefore *PT1S* , the value for a 15 minute rate is *PT15M* , and the value for a 1 hour rate is *PT1H*

TargetSamplingRate -> (string)

The sampling rate of the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been collected at a 1 second level and you want the system to resample the data at a 1 minute rate before training, the `TargetSamplingRate` is 1 minute.

When providing a value for the `TargetSamplingRate` , you must attach the prefix âPTâ to the rate you want. The value for a 1 second rate is therefore *PT1S* , the value for a 15 minute rate is *PT15M* , and the value for a 1 hour rate is *PT1H*

Shorthand Syntax:

```
TargetSamplingRate=string
```

JSON Syntax:

```
{
  "TargetSamplingRate": "PT1S"|"PT5S"|"PT10S"|"PT15S"|"PT30S"|"PT1M"|"PT5M"|"PT10M"|"PT15M"|"PT30M"|"PT1H"
}
```

`--server-side-kms-key-id` (string)

Provides the identifier of the KMS key used to encrypt model data by Amazon Lookout for Equipment.

`--tags` (list)

Any tags associated with the machine learning model being created.

(structure)

A tag is a key-value pair that can be added to a resource as metadata.

Key -> (string)

The key for the specified tag.

Value -> (string)

The value for the specified tag.

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

`--off-condition` (string)

Indicates that the asset associated with this sensor has been shut off. As long as this condition is met, Lookout for Equipment will not use data from this asset for training, evaluation, or inference.

`--model-diagnostics-output-configuration` (structure)

The Amazon S3 location where you want Amazon Lookout for Equipment to save the pointwise model diagnostics. You must also specify the `RoleArn` request parameter.

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

Shorthand Syntax:

```
S3OutputConfiguration={Bucket=string,Prefix=string},KmsKeyId=string
```

JSON Syntax:

```
{
  "S3OutputConfiguration": {
    "Bucket": "string",
    "Prefix": "string"
  },
  "KmsKeyId": "string"
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

ModelArn -> (string)

The Amazon Resource Name (ARN) of the model being created.

Status -> (string)

Indicates the status of the `CreateModel` operation.