# create-datasetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-dataset.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-dataset.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# create-dataset

## Description

### Note

This operation applies only to Amazon Rekognition Custom Labels.

Creates a new Amazon Rekognition Custom Labels dataset. You can create a dataset by using an Amazon Sagemaker format manifest file or by copying an existing Amazon Rekognition Custom Labels dataset.

To create a training dataset for a project, specify `TRAIN` for the value of `DatasetType` . To create the test dataset for a project, specify `TEST` for the value of `DatasetType` .

The response from `CreateDataset` is the Amazon Resource Name (ARN) for the dataset. Creating a dataset takes a while to complete. Use  DescribeDataset to check the current status. The dataset created successfully if the value of `Status` is `CREATE_COMPLETE` .

To check if any non-terminal errors occurred, call  ListDatasetEntries and check for the presence of `errors` lists in the JSON Lines.

Dataset creation fails if a terminal error occurs (`Status` = `CREATE_FAILED` ). Currently, you canât access the terminal error information.

For more information, see Creating dataset in the *Amazon Rekognition Custom Labels Developer Guide* .

This operation requires permissions to perform the `rekognition:CreateDataset` action. If you want to copy an existing dataset, you also require permission to perform the `rekognition:ListDatasetEntries` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/CreateDataset)

## Synopsis

```
create-dataset
[--dataset-source <value>]
--dataset-type <value>
--project-arn <value>
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

`--dataset-source` (structure)

The source files for the dataset. You can specify the ARN of an existing dataset or specify the Amazon S3 bucket location of an Amazon Sagemaker format manifest file. If you donât specify `datasetSource` , an empty dataset is created. To add labeled images to the dataset, You can use the console or call  UpdateDatasetEntries .

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

DatasetArn -> (string)

The ARN of an Amazon Rekognition Custom Labels dataset that you want to copy.

Shorthand Syntax:

```
GroundTruthManifest={S3Object={Bucket=string,Name=string,Version=string}},DatasetArn=string
```

JSON Syntax:

```
{
  "GroundTruthManifest": {
    "S3Object": {
      "Bucket": "string",
      "Name": "string",
      "Version": "string"
    }
  },
  "DatasetArn": "string"
}
```

`--dataset-type` (string)

The type of the dataset. Specify `TRAIN` to create a training dataset. Specify `TEST` to create a test dataset.

Possible values:

- `TRAIN`
- `TEST`

`--project-arn` (string)

The ARN of the Amazon Rekognition Custom Labels project to which you want to asssign the dataset.

`--tags` (map)

A set of tags (key-value pairs) that you want to attach to the dataset.

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

DatasetArn -> (string)

The ARN of the created Amazon Rekognition Custom Labels dataset.