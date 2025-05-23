# create-what-if-forecastÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-what-if-forecast.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-what-if-forecast.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [forecast](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/index.html#cli-aws-forecast) ]

# create-what-if-forecast

## Description

A what-if forecast is a forecast that is created from a modified version of the baseline forecast. Each what-if forecast incorporates either a replacement dataset or a set of transformations to the original dataset.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/forecast-2018-06-26/CreateWhatIfForecast)

## Synopsis

```
create-what-if-forecast
--what-if-forecast-name <value>
--what-if-analysis-arn <value>
[--time-series-transformations <value>]
[--time-series-replacements-data-source <value>]
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

`--what-if-forecast-name` (string)

The name of the what-if forecast. Names must be unique within each what-if analysis.

`--what-if-analysis-arn` (string)

The Amazon Resource Name (ARN) of the what-if analysis.

`--time-series-transformations` (list)

The transformations that are applied to the baseline time series. Each transformation contains an action and a set of conditions. An action is applied only when all conditions are met. If no conditions are provided, the action is applied to all items.

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

Shorthand Syntax:

```
Action={AttributeName=string,Operation=string,Value=double},TimeSeriesConditions=[{AttributeName=string,AttributeValue=string,Condition=string},{AttributeName=string,AttributeValue=string,Condition=string}] ...
```

JSON Syntax:

```
[
  {
    "Action": {
      "AttributeName": "string",
      "Operation": "ADD"|"SUBTRACT"|"MULTIPLY"|"DIVIDE",
      "Value": double
    },
    "TimeSeriesConditions": [
      {
        "AttributeName": "string",
        "AttributeValue": "string",
        "Condition": "EQUALS"|"NOT_EQUALS"|"LESS_THAN"|"GREATER_THAN"
      }
      ...
    ]
  }
  ...
]
```

`--time-series-replacements-data-source` (structure)

The replacement time series dataset, which contains the rows that you want to change in the related time series dataset. A replacement time series does not need to contain all rows that are in the baseline related time series. Include only the rows (measure-dimension combinations) that you want to include in the what-if forecast.

This dataset is merged with the original time series to create a transformed dataset that is used for the what-if analysis.

This dataset should contain the items to modify (such as item_id or workforce_type), any relevant dimensions, the timestamp column, and at least one of the related time series columns. This file should not contain duplicate timestamps for the same time series.

Timestamps and item_ids not included in this dataset are not included in the what-if analysis.

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

JSON Syntax:

```
{
  "S3Config": {
    "Path": "string",
    "RoleArn": "string",
    "KMSKeyArn": "string"
  },
  "Schema": {
    "Attributes": [
      {
        "AttributeName": "string",
        "AttributeType": "string"|"integer"|"float"|"timestamp"|"geolocation"
      }
      ...
    ]
  },
  "Format": "string",
  "TimestampFormat": "string"
}
```

`--tags` (list)

A list of [tags](https://docs.aws.amazon.com/forecast/latest/dg/tagging-forecast-resources.html) to apply to the what if forecast.

(structure)

The optional metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.

The following basic restrictions apply to tags:

- Maximum number of tags per resource - 50.
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length - 128 Unicode characters in UTF-8.
- Maximum value length - 256 Unicode characters in UTF-8.
- If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
- Tag keys and values are case sensitive.
- Do not use `aws:` , `AWS:` , or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has `aws` as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of `aws` do not count against your tags per resource limit.

Key -> (string)

One part of a key-value pair that makes up a tag. A `key` is a general label that acts like a category for more specific tag values.

Value -> (string)

The optional part of a key-value pair that makes up a tag. A `value` acts as a descriptor within a tag category (key).

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

WhatIfForecastArn -> (string)

The Amazon Resource Name (ARN) of the what-if forecast.