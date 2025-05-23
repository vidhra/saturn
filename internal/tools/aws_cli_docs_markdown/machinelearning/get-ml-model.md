# get-ml-modelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-ml-model.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-ml-model.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [machinelearning](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/index.html#cli-aws-machinelearning) ]

# get-ml-model

## Description

Returns an `MLModel` that includes detailed metadata, data source information, and the current status of the `MLModel` .

`GetMLModel` provides results in normal or verbose format.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/GetMLModel)

## Synopsis

```
get-ml-model
--ml-model-id <value>
[--verbose | --no-verbose]
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

`--ml-model-id` (string)

The ID assigned to the `MLModel` at creation.

`--verbose` | `--no-verbose` (boolean)

Specifies whether the `GetMLModel` operation should return `Recipe` .

If true, `Recipe` is returned.

If false, `Recipe` is not returned.

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

MLModelId -> (string)

The MLModel ID, which is same as the `MLModelId` in the request.

TrainingDataSourceId -> (string)

The ID of the training `DataSource` .

CreatedByIamUser -> (string)

The AWS user account from which the `MLModel` was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

CreatedAt -> (timestamp)

The time that the `MLModel` was created. The time is expressed in epoch time.

LastUpdatedAt -> (timestamp)

The time of the most recent edit to the `MLModel` . The time is expressed in epoch time.

Name -> (string)

A user-supplied name or description of the `MLModel` .

Status -> (string)

The current status of the `MLModel` . This element can have one of the following values:

- `PENDING` - Amazon Machine Learning (Amazon ML) submitted a request to describe a `MLModel` .
- `INPROGRESS` - The request is processing.
- `FAILED` - The request did not run to completion. The ML model isnât usable.
- `COMPLETED` - The request completed successfully.
- `DELETED` - The `MLModel` is marked as deleted. It isnât usable.

SizeInBytes -> (long)

Long integer type that is a 64-bit signed number.

EndpointInfo -> (structure)

The current endpoint of the `MLModel`

PeakRequestsPerSecond -> (integer)

The maximum processing rate for the real-time endpoint for `MLModel` , measured in incoming requests per second.

CreatedAt -> (timestamp)

The time that the request to create the real-time endpoint for the `MLModel` was received. The time is expressed in epoch time.

EndpointUrl -> (string)

The URI that specifies where to send real-time prediction requests for the `MLModel` .

**Note:** The application must wait until the real-time endpoint is ready before using this URI.

EndpointStatus -> (string)

The current status of the real-time endpoint for the `MLModel` . This element can have one of the following values:

- `NONE` - Endpoint does not exist or was previously deleted.
- `READY` - Endpoint is ready to be used for real-time predictions.
- `UPDATING` - Updating/creating the endpoint.

TrainingParameters -> (map)

A list of the training parameters in the `MLModel` . The list is implemented as a map of key-value pairs.

The following is the current set of training parameters:

- `sgd.maxMLModelSizeInBytes` - The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance. The value is an integer that ranges from `100000` to `2147483648` . The default value is `33554432` .
- `sgd.maxPasses` - The number of times that the training process traverses the observations to build the `MLModel` . The value is an integer that ranges from `1` to `10000` . The default value is `10` .
- `sgd.shuffleType` - Whether Amazon ML shuffles the training data. Shuffling data improves a modelâs ability to find the optimal solution for a variety of data types. The valid values are `auto` and `none` . The default value is `none` . We strongly recommend that you shuffle your data.
- `sgd.l1RegularizationAmount` - The coefficient regularization L1 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to zero, resulting in a sparse feature set. If you use this parameter, start by specifying a small value, such as `1.0E-08` . The value is a double that ranges from `0` to `MAX_DOUBLE` . The default is to not use L1 normalization. This parameter canât be used when `L2` is specified. Use this parameter sparingly.
- `sgd.l2RegularizationAmount` - The coefficient regularization L2 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as `1.0E-08` . The value is a double that ranges from `0` to `MAX_DOUBLE` . The default is to not use L2 normalization. This parameter canât be used when `L1` is specified. Use this parameter sparingly.

key -> (string)

String type.

value -> (string)

String type.

InputDataLocationS3 -> (string)

The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

MLModelType -> (string)

Identifies the `MLModel` category. The following are the available types:

- REGRESSION â Produces a numeric result. For example, âWhat price should a house be listed at?â
- BINARY â Produces one of two possible results. For example, âIs this an e-commerce website?â
- MULTICLASS â Produces one of several possible results. For example, âIs this a HIGH, LOW or MEDIUM risk trade?â

ScoreThreshold -> (float)

The scoring threshold is used in binary classification `MLModel` models. It marks the boundary between a positive prediction and a negative prediction.

Output values greater than or equal to the threshold receive a positive result from the MLModel, such as `true` . Output values less than the threshold receive a negative response from the MLModel, such as `false` .

ScoreThresholdLastUpdatedAt -> (timestamp)

The time of the most recent edit to the `ScoreThreshold` . The time is expressed in epoch time.

LogUri -> (string)

A link to the file that contains logs of the `CreateMLModel` operation.

Message -> (string)

A description of the most recent details about accessing the `MLModel` .

ComputeTime -> (long)

The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the `MLModel` , normalized and scaled on computation resources. `ComputeTime` is only available if the `MLModel` is in the `COMPLETED` state.

FinishedAt -> (timestamp)

The epoch time when Amazon Machine Learning marked the `MLModel` as `COMPLETED` or `FAILED` . `FinishedAt` is only available when the `MLModel` is in the `COMPLETED` or `FAILED` state.

StartedAt -> (timestamp)

The epoch time when Amazon Machine Learning marked the `MLModel` as `INPROGRESS` . `StartedAt` isnât available if the `MLModel` is in the `PENDING` state.

Recipe -> (string)

The recipe to use when training the `MLModel` . The `Recipe` provides detailed information about the observation data to use during training, and manipulations to perform on the observation data during training.

**Note:** This parameter is provided as part of the verbose format.

Schema -> (string)

The schema used by all of the data files referenced by the `DataSource` .

**Note:** This parameter is provided as part of the verbose format.