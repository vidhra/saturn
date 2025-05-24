# create-explainabilityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-explainability.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-explainability.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [forecast](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/index.html#cli-aws-forecast) ]

# create-explainability

## Description

### Note

Explainability is only available for Forecasts and Predictors generated from an AutoPredictor ( CreateAutoPredictor )

Creates an Amazon Forecast Explainability.

Explainability helps you better understand how the attributes in your datasets impact forecast. Amazon Forecast uses a metric called Impact scores to quantify the relative impact of each attribute and determine whether they increase or decrease forecast values.

To enable Forecast Explainability, your predictor must include at least one of the following: related time series, item metadata, or additional datasets like Holidays and the Weather Index.

CreateExplainability accepts either a Predictor ARN or Forecast ARN. To receive aggregated Impact scores for all time series and time points in your datasets, provide a Predictor ARN. To receive Impact scores for specific time series and time points, provide a Forecast ARN.

**CreateExplainability with a Predictor ARN**

### Note

You can only have one Explainability resource per predictor. If you already enabled `ExplainPredictor` in  CreateAutoPredictor , that predictor already has an Explainability resource.

The following parameters are required when providing a Predictor ARN:

- `ExplainabilityName` - A unique name for the Explainability.
- `ResourceArn` - The Arn of the predictor.
- `TimePointGranularity` - Must be set to âALLâ.
- `TimeSeriesGranularity` - Must be set to âALLâ.

Do not specify a value for the following parameters:

- `DataSource` - Only valid when TimeSeriesGranularity is âSPECIFICâ.
- `Schema` - Only valid when TimeSeriesGranularity is âSPECIFICâ.
- `StartDateTime` - Only valid when TimePointGranularity is âSPECIFICâ.
- `EndDateTime` - Only valid when TimePointGranularity is âSPECIFICâ.

**CreateExplainability with a Forecast ARN**

### Note

You can specify a maximum of 50 time series and 500 time points.

The following parameters are required when providing a Predictor ARN:

- `ExplainabilityName` - A unique name for the Explainability.
- `ResourceArn` - The Arn of the forecast.
- `TimePointGranularity` - Either âALLâ or âSPECIFICâ.
- `TimeSeriesGranularity` - Either âALLâ or âSPECIFICâ.

If you set TimeSeriesGranularity to âSPECIFICâ, you must also provide the following:

- `DataSource` - The S3 location of the CSV file specifying your time series.
- `Schema` - The Schema defines the attributes and attribute types listed in the Data Source.

If you set TimePointGranularity to âSPECIFICâ, you must also provide the following:

- `StartDateTime` - The first timestamp in the range of time points.
- `EndDateTime` - The last timestamp in the range of time points.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/forecast-2018-06-26/CreateExplainability)

## Synopsis

```
create-explainability
--explainability-name <value>
--resource-arn <value>
--explainability-config <value>
[--data-source <value>]
[--schema <value>]
[--enable-visualization | --no-enable-visualization]
[--start-date-time <value>]
[--end-date-time <value>]
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

`--explainability-name` (string)

A unique name for the Explainability.

`--resource-arn` (string)

The Amazon Resource Name (ARN) of the Predictor or Forecast used to create the Explainability.

`--explainability-config` (structure)

The configuration settings that define the granularity of time series and time points for the Explainability.

TimeSeriesGranularity -> (string)

To create an Explainability for all time series in your datasets, use `ALL` . To create an Explainability for specific time series in your datasets, use `SPECIFIC` .

Specify time series by uploading a CSV or Parquet file to an Amazon S3 bucket and set the location within the  DataDestination data type.

TimePointGranularity -> (string)

To create an Explainability for all time points in your forecast horizon, use `ALL` . To create an Explainability for specific time points in your forecast horizon, use `SPECIFIC` .

Specify time points with the `StartDateTime` and `EndDateTime` parameters within the  CreateExplainability operation.

Shorthand Syntax:

```
TimeSeriesGranularity=string,TimePointGranularity=string
```

JSON Syntax:

```
{
  "TimeSeriesGranularity": "ALL"|"SPECIFIC",
  "TimePointGranularity": "ALL"|"SPECIFIC"
}
```

`--data-source` (structure)

The source of your data, an Identity and Access Management (IAM) role that allows Amazon Forecast to access the data and, optionally, an Key Management Service (KMS) key.

S3Config -> (structure)

The path to the data stored in an Amazon Simple Storage Service (Amazon S3) bucket along with the credentials to access the data.

Path -> (string)

The path to an Amazon Simple Storage Service (Amazon S3) bucket or file(s) in an Amazon S3 bucket.

RoleArn -> (string)

The ARN of the Identity and Access Management (IAM) role that Amazon Forecast can assume to access the Amazon S3 bucket or files. If you provide a value for the `KMSKeyArn` key, the role must allow access to the key.

Passing a role across Amazon Web Services accounts is not allowed. If you pass a role that isnât in your account, you get an `InvalidInputException` error.

KMSKeyArn -> (string)

The Amazon Resource Name (ARN) of an Key Management Service (KMS) key.

Shorthand Syntax:

```
S3Config={Path=string,RoleArn=string,KMSKeyArn=string}
```

JSON Syntax:

```
{
  "S3Config": {
    "Path": "string",
    "RoleArn": "string",
    "KMSKeyArn": "string"
  }
}
```

`--schema` (structure)

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

Shorthand Syntax:

```
Attributes=[{AttributeName=string,AttributeType=string},{AttributeName=string,AttributeType=string}]
```

JSON Syntax:

```
{
  "Attributes": [
    {
      "AttributeName": "string",
      "AttributeType": "string"|"integer"|"float"|"timestamp"|"geolocation"
    }
    ...
  ]
}
```

`--enable-visualization` | `--no-enable-visualization` (boolean)

Create an Explainability visualization that is viewable within the Amazon Web Services console.

`--start-date-time` (string)

If `TimePointGranularity` is set to `SPECIFIC` , define the first point for the Explainability.

Use the following timestamp format: yyyy-MM-ddTHH:mm:ss (example: 2015-01-01T20:00:00)

`--end-date-time` (string)

If `TimePointGranularity` is set to `SPECIFIC` , define the last time point for the Explainability.

Use the following timestamp format: yyyy-MM-ddTHH:mm:ss (example: 2015-01-01T20:00:00)

`--tags` (list)

Optional metadata to help you categorize and organize your resources. Each tag consists of a key and an optional value, both of which you define. Tag keys and values are case sensitive.

The following restrictions apply to tags:

- For each resource, each tag key must be unique and each tag key must have one value.
- Maximum number of tags per resource: 50.
- Maximum key length: 128 Unicode characters in UTF-8.
- Maximum value length: 256 Unicode characters in UTF-8.
- Accepted characters: all letters and numbers, spaces representable in UTF-8, and + - = . _ : / @. If your tagging schema is used across other services and resources, the character restrictions of those services also apply.
- Key prefixes cannot include any upper or lowercase combination of `aws:` or `AWS:` . Values can have this prefix. If a tag value has `aws` as its prefix but the key does not, Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of `aws` do not count against your tags per resource limit. You cannot edit or delete tag keys with this prefix.

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

ExplainabilityArn -> (string)

The Amazon Resource Name (ARN) of the Explainability.