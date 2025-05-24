# create-datasetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/create-dataset.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/create-dataset.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutvision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/index.html#cli-aws-lookoutvision) ]

# create-dataset

## Description

Creates a new dataset in an Amazon Lookout for Vision project. `CreateDataset` can create a training or a test dataset from a valid dataset source (`DatasetSource` ).

If you want a single dataset project, specify `train` for the value of `DatasetType` .

To have a project with separate training and test datasets, call `CreateDataset` twice. On the first call, specify `train` for the value of `DatasetType` . On the second call, specify `test` for the value of `DatasetType` .

This operation requires permissions to perform the `lookoutvision:CreateDataset` operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutvision-2020-11-20/CreateDataset)

## Synopsis

```
create-dataset
--project-name <value>
--dataset-type <value>
[--dataset-source <value>]
[--client-token <value>]
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

The name of the project in which you want to create a dataset.

`--dataset-type` (string)

The type of the dataset. Specify `train` for a training dataset. Specify `test` for a test dataset.

`--dataset-source` (structure)

The location of the manifest file that Amazon Lookout for Vision uses to create the dataset.

If you donât specify `DatasetSource` , an empty dataset is created and the operation synchronously returns. Later, you can add JSON Lines by calling  UpdateDatasetEntries .

If you specify a value for `DataSource` , the manifest at the S3 location is validated and used to create the dataset. The call to `CreateDataset` is asynchronous and might take a while to complete. To find out the current status, Check the value of `Status` returned in a call to  DescribeDataset .

GroundTruthManifest -> (structure)

Location information for the manifest file.

S3Object -> (structure)

The S3 bucket location for the manifest file.

Bucket -> (string)

The Amazon S3 bucket that contains the manifest.

Key -> (string)

The name and location of the manifest file withiin the bucket.

VersionId -> (string)

The version ID of the bucket.

Shorthand Syntax:

```
GroundTruthManifest={S3Object={Bucket=string,Key=string,VersionId=string}}
```

JSON Syntax:

```
{
  "GroundTruthManifest": {
    "S3Object": {
      "Bucket": "string",
      "Key": "string",
      "VersionId": "string"
    }
  }
}
```

`--client-token` (string)

ClientToken is an idempotency token that ensures a call to `CreateDataset` completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from `CreateDataset` . In this case, safely retry your call to `CreateDataset` by using the same `ClientToken` parameter value.

If you donât supply a value for `ClientToken` , the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple dataset creation requests. Youâll need to provide your own value for other use cases.

An error occurs if the other input parameters are not the same as in the first request. Using a different value for `ClientToken` is considered a new call to `CreateDataset` . An idempotency token is active for 8 hours.

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

DatasetMetadata -> (structure)

Information about the dataset.

DatasetType -> (string)

The type of the dataset.

CreationTimestamp -> (timestamp)

The Unix timestamp for the date and time that the dataset was created.

Status -> (string)

The status for the dataset.

StatusMessage -> (string)

The status message for the dataset.