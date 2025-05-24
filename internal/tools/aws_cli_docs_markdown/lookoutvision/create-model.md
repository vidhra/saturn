# create-modelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/create-model.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/create-model.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutvision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/index.html#cli-aws-lookoutvision) ]

# create-model

## Description

Creates a new version of a model within an an Amazon Lookout for Vision project. `CreateModel` is an asynchronous operation in which Amazon Lookout for Vision trains, tests, and evaluates a new version of a model.

To get the current status, check the `Status` field returned in the response from  DescribeModel .

If the project has a single dataset, Amazon Lookout for Vision internally splits the dataset to create a training and a test dataset. If the project has a training and a test dataset, Lookout for Vision uses the respective datasets to train and test the model.

After training completes, the evaluation metrics are stored at the location specified in `OutputConfig` .

This operation requires permissions to perform the `lookoutvision:CreateModel` operation. If you want to tag your model, you also require permission to the `lookoutvision:TagResource` operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutvision-2020-11-20/CreateModel)

## Synopsis

```
create-model
--project-name <value>
[--description <value>]
[--client-token <value>]
--output-config <value>
[--kms-key-id <value>]
[--tags <value>]
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

`--project-name` (string)

The name of the project in which you want to create a model version.

`--description` (string)

A description for the version of the model.

`--client-token` (string)

ClientToken is an idempotency token that ensures a call to `CreateModel` completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from `CreateModel` . In this case, safely retry your call to `CreateModel` by using the same `ClientToken` parameter value.

If you donât supply a value for `ClientToken` , the AWS SDK you are using inserts a value for you. This prevents retries after a network error from starting multiple training jobs. Youâll need to provide your own value for other use cases.

An error occurs if the other input parameters are not the same as in the first request. Using a different value for `ClientToken` is considered a new call to `CreateModel` . An idempotency token is active for 8 hours.

`--output-config` (structure)

The location where Amazon Lookout for Vision saves the training results.

S3Location -> (structure)

The S3 location for the output.

Bucket -> (string)

The S3 bucket that contains the training or model packaging job output. If you are training a model, the bucket must in your AWS account. If you use an S3 bucket for a model packaging job, the S3 bucket must be in the same AWS Region and AWS account in which you use AWS IoT Greengrass.

Prefix -> (string)

The path of the folder, within the S3 bucket, that contains the output.

Shorthand Syntax:

```
S3Location={Bucket=string,Prefix=string}
```

JSON Syntax:

```
{
  "S3Location": {
    "Bucket": "string",
    "Prefix": "string"
  }
}
```

`--kms-key-id` (string)

The identifier for your AWS KMS key. The key is used to encrypt training and test images copied into the service for model training. Your source images are unaffected. If this parameter is not specified, the copied images are encrypted by a key that AWS owns and manages.

`--tags` (list)

A set of tags (key-value pairs) that you want to attach to the model.

(structure)

A key and value pair that is attached to the specified Amazon Lookout for Vision model.

Key -> (string)

The key of the tag that is attached to the specified model.

Value -> (string)

The value of the tag that is attached to the specified model.

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

ModelMetadata -> (structure)

The response from a call to `CreateModel` .

CreationTimestamp -> (timestamp)

The unix timestamp for the date and time that the model was created.

ModelVersion -> (string)

The version of the model.

ModelArn -> (string)

The Amazon Resource Name (ARN) of the model.

Description -> (string)

The description for the model.

Status -> (string)

The status of the model.

StatusMessage -> (string)

The status message for the model.

Performance -> (structure)

Performance metrics for the model. Not available until training has successfully completed.

F1Score -> (float)

The overall F1 score metric for the trained model.

Recall -> (float)

The overall recall metric value for the trained model.

Precision -> (float)

The overall precision metric value for the trained model.