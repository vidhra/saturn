# create-ml-modelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-ml-model.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-ml-model.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [machinelearning](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/index.html#cli-aws-machinelearning) ]

# create-ml-model

## Description

Creates a new `MLModel` using the `DataSource` and the recipe as information sources.

An `MLModel` is nearly immutable. Users can update only the `MLModelName` and the `ScoreThreshold` in an `MLModel` without creating a new `MLModel` .

`CreateMLModel` is an asynchronous operation. In response to `CreateMLModel` , Amazon Machine Learning (Amazon ML) immediately returns and sets the `MLModel` status to `PENDING` . After the `MLModel` has been created and ready is for use, Amazon ML sets the status to `COMPLETED` .

You can use the `GetMLModel` operation to check the progress of the `MLModel` during the creation operation.

`CreateMLModel` requires a `DataSource` with computed statistics, which can be created by setting `ComputeStatistics` to `true` in `CreateDataSourceFromRDS` , `CreateDataSourceFromS3` , or `CreateDataSourceFromRedshift` operations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/CreateMLModel)

## Synopsis

```
create-ml-model
--ml-model-id <value>
[--ml-model-name <value>]
--ml-model-type <value>
[--parameters <value>]
--training-data-source-id <value>
[--recipe <value>]
[--recipe-uri <value>]
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

A user-supplied ID that uniquely identifies the `MLModel` .

`--ml-model-name` (string)

A user-supplied name or description of the `MLModel` .

`--ml-model-type` (string)

The category of supervised learning that this `MLModel` will address. Choose from the following types:

- Choose `REGRESSION` if the `MLModel` will be used to predict a numeric value.
- Choose `BINARY` if the `MLModel` result has two possible values.
- Choose `MULTICLASS` if the `MLModel` result has a limited number of values.

For more information, see the [Amazon Machine Learning Developer Guide](https://docs.aws.amazon.com/machine-learning/latest/dg) .

Possible values:

- `REGRESSION`
- `BINARY`
- `MULTICLASS`

`--parameters` (map)

A list of the training parameters in the `MLModel` . The list is implemented as a map of key-value pairs.

The following is the current set of training parameters:

- `sgd.maxMLModelSizeInBytes` - The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance. The value is an integer that ranges from `100000` to `2147483648` . The default value is `33554432` .
- `sgd.maxPasses` - The number of times that the training process traverses the observations to build the `MLModel` . The value is an integer that ranges from `1` to `10000` . The default value is `10` .
- `sgd.shuffleType` - Whether Amazon ML shuffles the training data. Shuffling the data improves a modelâs ability to find the optimal solution for a variety of data types. The valid values are `auto` and `none` . The default value is `none` . We strongly recommend that you shuffle your data.
- `sgd.l1RegularizationAmount` - The coefficient regularization L1 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to zero, resulting in a sparse feature set. If you use this parameter, start by specifying a small value, such as `1.0E-08` . The value is a double that ranges from `0` to `MAX_DOUBLE` . The default is to not use L1 normalization. This parameter canât be used when `L2` is specified. Use this parameter sparingly.
- `sgd.l2RegularizationAmount` - The coefficient regularization L2 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as `1.0E-08` . The value is a double that ranges from `0` to `MAX_DOUBLE` . The default is to not use L2 normalization. This parameter canât be used when `L1` is specified. Use this parameter sparingly.

key -> (string)

String type.

value -> (string)

String type.

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--training-data-source-id` (string)

The `DataSource` that points to the training data.

`--recipe` (string)

The data recipe for creating the `MLModel` . You must specify either the recipe or its URI. If you donât specify a recipe or its URI, Amazon ML creates a default.

`--recipe-uri` (string)

The Amazon Simple Storage Service (Amazon S3) location and file name that contains the `MLModel` recipe. You must specify either the recipe or its URI. If you donât specify a recipe or its URI, Amazon ML creates a default.

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

A user-supplied ID that uniquely identifies the `MLModel` . This value should be identical to the value of the `MLModelId` in the request.