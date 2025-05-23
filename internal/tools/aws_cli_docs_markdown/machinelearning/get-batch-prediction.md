# get-batch-predictionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-batch-prediction.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-batch-prediction.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [machinelearning](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/index.html#cli-aws-machinelearning) ]

# get-batch-prediction

## Description

Returns a `BatchPrediction` that includes detailed metadata, status, and data file information for a `Batch Prediction` request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/GetBatchPrediction)

## Synopsis

```
get-batch-prediction
--batch-prediction-id <value>
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

`--batch-prediction-id` (string)

An ID assigned to the `BatchPrediction` at creation.

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

BatchPredictionId -> (string)

An ID assigned to the `BatchPrediction` at creation. This value should be identical to the value of the `BatchPredictionID` in the request.

MLModelId -> (string)

The ID of the `MLModel` that generated predictions for the `BatchPrediction` request.

BatchPredictionDataSourceId -> (string)

The ID of the `DataSource` that was used to create the `BatchPrediction` .

InputDataLocationS3 -> (string)

The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

CreatedByIamUser -> (string)

The AWS user account that invoked the `BatchPrediction` . The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

CreatedAt -> (timestamp)

The time when the `BatchPrediction` was created. The time is expressed in epoch time.

LastUpdatedAt -> (timestamp)

The time of the most recent edit to `BatchPrediction` . The time is expressed in epoch time.

Name -> (string)

A user-supplied name or description of the `BatchPrediction` .

Status -> (string)

The status of the `BatchPrediction` , which can be one of the following values:

- `PENDING` - Amazon Machine Learning (Amazon ML) submitted a request to generate batch predictions.
- `INPROGRESS` - The batch predictions are in progress.
- `FAILED` - The request to perform a batch prediction did not run to completion. It is not usable.
- `COMPLETED` - The batch prediction process completed successfully.
- `DELETED` - The `BatchPrediction` is marked as deleted. It is not usable.

OutputUri -> (string)

The location of an Amazon S3 bucket or directory to receive the operation results.

LogUri -> (string)

A link to the file that contains logs of the `CreateBatchPrediction` operation.

Message -> (string)

A description of the most recent details about processing the batch prediction request.

ComputeTime -> (long)

The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the `BatchPrediction` , normalized and scaled on computation resources. `ComputeTime` is only available if the `BatchPrediction` is in the `COMPLETED` state.

FinishedAt -> (timestamp)

The epoch time when Amazon Machine Learning marked the `BatchPrediction` as `COMPLETED` or `FAILED` . `FinishedAt` is only available when the `BatchPrediction` is in the `COMPLETED` or `FAILED` state.

StartedAt -> (timestamp)

The epoch time when Amazon Machine Learning marked the `BatchPrediction` as `INPROGRESS` . `StartedAt` isnât available if the `BatchPrediction` is in the `PENDING` state.

TotalRecordCount -> (long)

The number of total records that Amazon Machine Learning saw while processing the `BatchPrediction` .

InvalidRecordCount -> (long)

The number of invalid records that Amazon Machine Learning saw while processing the `BatchPrediction` .