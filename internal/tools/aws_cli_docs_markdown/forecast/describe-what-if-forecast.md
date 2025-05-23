# describe-what-if-forecastÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-what-if-forecast.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-what-if-forecast.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [forecast](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/index.html#cli-aws-forecast) ]

# describe-what-if-forecast

## Description

Describes the what-if forecast created using the  CreateWhatIfForecast operation.

In addition to listing the properties provided in the `CreateWhatIfForecast` request, this operation lists the following properties:

- `CreationTime`
- `LastModificationTime`
- `Message` - If an error occurred, information about the error.
- `Status`

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/forecast-2018-06-26/DescribeWhatIfForecast)

## Synopsis

```
describe-what-if-forecast
--what-if-forecast-arn <value>
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

`--what-if-forecast-arn` (string)

The Amazon Resource Name (ARN) of the what-if forecast that you are interested in.

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

WhatIfForecastName -> (string)

The name of the what-if forecast.

WhatIfForecastArn -> (string)

The Amazon Resource Name (ARN) of the what-if forecast.

WhatIfAnalysisArn -> (string)

The Amazon Resource Name (ARN) of the what-if analysis that contains this forecast.

EstimatedTimeRemainingInMinutes -> (long)

The approximate time remaining to complete the what-if forecast, in minutes.

Status -> (string)

The status of the what-if forecast. States include:

- `ACTIVE`
- `CREATE_PENDING` , `CREATE_IN_PROGRESS` , `CREATE_FAILED`
- `CREATE_STOPPING` , `CREATE_STOPPED`
- `DELETE_PENDING` , `DELETE_IN_PROGRESS` , `DELETE_FAILED`

### Note

The `Status` of the what-if forecast must be `ACTIVE` before you can access the forecast.

Message -> (string)

If an error occurred, an informational message about the error.

CreationTime -> (timestamp)

When the what-if forecast was created.

LastModificationTime -> (timestamp)

The last time the resource was modified. The timestamp depends on the status of the job:

- `CREATE_PENDING` - The `CreationTime` .
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or failed.

TimeSeriesTransformations -> (list)

An array of `Action` and `TimeSeriesConditions` elements that describe what transformations were applied to which time series.

(structure)

A transformation function is a pair of operations that select and modify the rows in a related time series. You select the rows that you want with a condition operation and you modify the rows with a transformation operation. All conditions are joined with an AND operation, meaning that all conditions must be true for the transformation to be applied. Transformations are applied in the order that they are listed.

Action -> (structure)

An array of actions that define a time series and how it is transformed. These transformations create a new time series that is used for the what-if analysis.

AttributeName -> (string)

The related time series that you are modifying. This value is case insensitive.

Operation -> (string)

The operation that is applied to the provided attribute. Operations include:

- `ADD` - adds `Value` to all rows of `AttributeName` .
- `SUBTRACT` - subtracts `Value` from all rows of `AttributeName` .
- `MULTIPLY` - multiplies all rows of `AttributeName` by `Value` .
- `DIVIDE` - divides all rows of `AttributeName` by `Value` .

Value -> (double)

The value that is applied for the chosen `Operation` .

TimeSeriesConditions -> (list)

An array of conditions that define which members of the related time series are transformed.

(structure)

Creates a subset of items within an attribute that are modified. For example, you can use this operation to create a subset of items that cost $5 or less. To do this, you specify `"AttributeName": "price"` , `"AttributeValue": "5"` , and `"Condition": "LESS_THAN"` . Pair this operation with the  Action operation within the  CreateWhatIfForecastRequest$TimeSeriesTransformations operation to define how the attribute is modified.

AttributeName -> (string)

The item_id, dimension name, IM name, or timestamp that you are modifying.

AttributeValue -> (string)

The value that is applied for the chosen `Condition` .

Condition -> (string)

The condition to apply. Valid values are `EQUALS` , `NOT_EQUALS` , `LESS_THAN` and `GREATER_THAN` .

TimeSeriesReplacementsDataSource -> (structure)

An array of `S3Config` , `Schema` , and `Format` elements that describe the replacement time series.

S3Config -> (structure)

The path to the file(s) in an Amazon Simple Storage Service (Amazon S3) bucket, and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the file(s). Optionally, includes an Key Management Service (KMS) key. This object is part of the  DataSource object that is submitted in the  CreateDatasetImportJob request, and part of the  DataDestination object.

Path -> (string)

The path to an Amazon Simple Storage Service (Amazon S3) bucket or file(s) in an Amazon S3 bucket.

RoleArn -> (string)

The ARN of the Identity and Access Management (IAM) role that Amazon Forecast can assume to access the Amazon S3 bucket or files. If you provide a value for the `KMSKeyArn` key, the role must allow access to the key.

Passing a role across Amazon Web Services accounts is not allowed. If you pass a role that isnât in your account, you get an `InvalidInputException` error.

KMSKeyArn -> (string)

The Amazon Resource Name (ARN) of an Key Management Service (KMS) key.

Schema -> (structure)

Defines the fields of a dataset.

Attributes -> (list)

An array of attributes specifying the name and type of each field in a dataset.

(structure)

An attribute of a schema, which defines a dataset field. A schema attribute is required for every field in a dataset. The [Schema](https://docs.aws.amazon.com/forecast/latest/dg/API_Schema.html) object contains an array of `SchemaAttribute` objects.

AttributeName -> (string)

The name of the dataset field.

AttributeType -> (string)

The data type of the field.

For a related time series dataset, other than date, item_id, and forecast dimensions attributes, all attributes should be of numerical type (integer/float).

Format -> (string)

The format of the replacement data, CSV or PARQUET.

TimestampFormat -> (string)

The timestamp format of the replacement data.

ForecastTypes -> (list)

The quantiles at which probabilistic forecasts are generated. You can specify up to five quantiles per what-if forecast in the  CreateWhatIfForecast operation. If you didnât specify quantiles, the default values are `["0.1", "0.5", "0.9"]` .

(string)