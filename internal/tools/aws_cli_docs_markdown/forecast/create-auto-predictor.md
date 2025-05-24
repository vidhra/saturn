# create-auto-predictorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-auto-predictor.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-auto-predictor.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [forecast](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/index.html#cli-aws-forecast) ]

# create-auto-predictor

## Description

Creates an Amazon Forecast predictor.

Amazon Forecast creates predictors with AutoPredictor, which involves applying the optimal combination of algorithms to each time series in your datasets. You can use  CreateAutoPredictor to create new predictors or upgrade/retrain existing predictors.

**Creating new predictors**

The following parameters are required when creating a new predictor:

- `PredictorName` - A unique name for the predictor.
- `DatasetGroupArn` - The ARN of the dataset group used to train the predictor.
- `ForecastFrequency` - The granularity of your forecasts (hourly, daily, weekly, etc).
- `ForecastHorizon` - The number of time-steps that the model predicts. The forecast horizon is also called the prediction length.

When creating a new predictor, do not specify a value for `ReferencePredictorArn` .

**Upgrading and retraining predictors**

The following parameters are required when retraining or upgrading a predictor:

- `PredictorName` - A unique name for the predictor.
- `ReferencePredictorArn` - The ARN of the predictor to retrain or upgrade.

When upgrading or retraining a predictor, only specify values for the `ReferencePredictorArn` and `PredictorName` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/forecast-2018-06-26/CreateAutoPredictor)

## Synopsis

```
create-auto-predictor
--predictor-name <value>
[--forecast-horizon <value>]
[--forecast-types <value>]
[--forecast-dimensions <value>]
[--forecast-frequency <value>]
[--data-config <value>]
[--encryption-config <value>]
[--reference-predictor-arn <value>]
[--optimization-metric <value>]
[--explain-predictor | --no-explain-predictor]
[--tags <value>]
[--monitor-config <value>]
[--time-alignment-boundary <value>]
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

`--predictor-name` (string)

A unique name for the predictor

`--forecast-horizon` (integer)

The number of time-steps that the model predicts. The forecast horizon is also called the prediction length.

The maximum forecast horizon is the lesser of 500 time-steps or 1/4 of the TARGET_TIME_SERIES dataset length. If you are retraining an existing AutoPredictor, then the maximum forecast horizon is the lesser of 500 time-steps or 1/3 of the TARGET_TIME_SERIES dataset length.

If you are upgrading to an AutoPredictor or retraining an existing AutoPredictor, you cannot update the forecast horizon parameter. You can meet this requirement by providing longer time-series in the dataset.

`--forecast-types` (list)

The forecast types used to train a predictor. You can specify up to five forecast types. Forecast types can be quantiles from 0.01 to 0.99, by increments of 0.01 or higher. You can also specify the mean forecast with `mean` .

(string)

Syntax:

```
"string" "string" ...
```

`--forecast-dimensions` (list)

An array of dimension (field) names that specify how to group the generated forecast.

For example, if you are generating forecasts for item sales across all your stores, and your dataset contains a `store_id` field, you would specify `store_id` as a dimension to group sales forecasts for each store.

(string)

Syntax:

```
"string" "string" ...
```

`--forecast-frequency` (string)

The frequency of predictions in a forecast.

Valid intervals are an integer followed by Y (Year), M (Month), W (Week), D (Day), H (Hour), and min (Minute). For example, â1Dâ indicates every day and â15minâ indicates every 15 minutes. You cannot specify a value that would overlap with the next larger frequency. That means, for example, you cannot specify a frequency of 60 minutes, because that is equivalent to 1 hour. The valid values for each frequency are the following:

- Minute - 1-59
- Hour - 1-23
- Day - 1-6
- Week - 1-4
- Month - 1-11
- Year - 1

Thus, if you want every other week forecasts, specify â2Wâ. Or, if you want quarterly forecasts, you specify â3Mâ.

The frequency must be greater than or equal to the TARGET_TIME_SERIES dataset frequency.

When a RELATED_TIME_SERIES dataset is provided, the frequency must be equal to the RELATED_TIME_SERIES dataset frequency.

`--data-config` (structure)

The data configuration for your dataset group and any additional datasets.

DatasetGroupArn -> (string)

The ARN of the dataset group used to train the predictor.

AttributeConfigs -> (list)

Aggregation and filling options for attributes in your dataset group.

(structure)

Provides information about the method used to transform attributes.

The following is an example using the RETAIL domain:

`{`

`"AttributeName": "demand",`

`"Transformations": {"aggregation": "sum", "middlefill": "zero", "backfill": "zero"}`

`}`

AttributeName -> (string)

The name of the attribute as specified in the schema. Amazon Forecast supports the target field of the target time series and the related time series datasets. For example, for the RETAIL domain, the target is `demand` .

Transformations -> (map)

The method parameters (key-value pairs), which are a map of override parameters. Specify these parameters to override the default values. Related Time Series attributes do not accept aggregation parameters.

The following list shows the parameters and their valid values for the âfillingâ featurization method for a **Target Time Series** dataset. Default values are bolded.

- `aggregation` : **sum** , `avg` , `first` , `min` , `max`
- `frontfill` : **none**
- `middlefill` : **zero** , `nan` (not a number), `value` , `median` , `mean` , `min` , `max`
- `backfill` : **zero** , `nan` , `value` , `median` , `mean` , `min` , `max`

The following list shows the parameters and their valid values for a **Related Time Series** featurization method (there are no defaults):

- `middlefill` : `zero` , `value` , `median` , `mean` , `min` , `max`
- `backfill` : `zero` , `value` , `median` , `mean` , `min` , `max`
- `futurefill` : `zero` , `value` , `median` , `mean` , `min` , `max`

To set a filling method to a specific value, set the fill parameter to `value` and define the value in a corresponding `_value` parameter. For example, to set backfilling to a value of 2, include the following: `"backfill": "value"` and `"backfill_value":"2"` .

key -> (string)

value -> (string)

AdditionalDatasets -> (list)

Additional built-in datasets like Holidays and the Weather Index.

(structure)

Describes an additional dataset. This object is part of the  DataConfig object. Forecast supports the Weather Index and Holidays additional datasets.

**Weather Index**

The Amazon Forecast Weather Index is a built-in dataset that incorporates historical and projected weather information into your model. The Weather Index supplements your datasets with over two years of historical weather data and up to 14 days of projected weather data. For more information, see [Amazon Forecast Weather Index](https://docs.aws.amazon.com/forecast/latest/dg/weather.html) .

**Holidays**

Holidays is a built-in dataset that incorporates national holiday information into your model. It provides native support for the holiday calendars of 66 countries. To view the holiday calendars, refer to the [Jollyday](http://jollyday.sourceforge.net/data.html) library. For more information, see [Holidays Featurization](https://docs.aws.amazon.com/forecast/latest/dg/holidays.html) .

Name -> (string)

The name of the additional dataset. Valid names: `"holiday"` and `"weather"` .

Configuration -> (map)

**Weather Index**

To enable the Weather Index, do not specify a value for `Configuration` .

**Holidays**

**Holidays**

To enable Holidays, set `CountryCode` to one of the following two-letter country codes:

- âALâ - ALBANIA
- âARâ - ARGENTINA
- âATâ - AUSTRIA
- âAUâ - AUSTRALIA
- âBAâ - BOSNIA HERZEGOVINA
- âBEâ - BELGIUM
- âBGâ - BULGARIA
- âBOâ - BOLIVIA
- âBRâ - BRAZIL
- âBYâ - BELARUS
- âCAâ - CANADA
- âCLâ - CHILE
- âCOâ - COLOMBIA
- âCRâ - COSTA RICA
- âHRâ - CROATIA
- âCZâ - CZECH REPUBLIC
- âDKâ - DENMARK
- âECâ - ECUADOR
- âEEâ - ESTONIA
- âETâ - ETHIOPIA
- âFIâ - FINLAND
- âFRâ - FRANCE
- âDEâ - GERMANY
- âGRâ - GREECE
- âHUâ - HUNGARY
- âISâ - ICELAND
- âINâ - INDIA
- âIEâ - IRELAND
- âITâ - ITALY
- âJPâ - JAPAN
- âKZâ - KAZAKHSTAN
- âKRâ - KOREA
- âLVâ - LATVIA
- âLIâ - LIECHTENSTEIN
- âLTâ - LITHUANIA
- âLUâ - LUXEMBOURG
- âMKâ - MACEDONIA
- âMTâ - MALTA
- âMXâ - MEXICO
- âMDâ - MOLDOVA
- âMEâ - MONTENEGRO
- âNLâ - NETHERLANDS
- âNZâ - NEW ZEALAND
- âNIâ - NICARAGUA
- âNGâ - NIGERIA
- âNOâ - NORWAY
- âPAâ - PANAMA
- âPYâ - PARAGUAY
- âPEâ - PERU
- âPLâ - POLAND
- âPTâ - PORTUGAL
- âROâ - ROMANIA
- âRUâ - RUSSIA
- âRSâ - SERBIA
- âSKâ - SLOVAKIA
- âSIâ - SLOVENIA
- âZAâ - SOUTH AFRICA
- âESâ - SPAIN
- âSEâ - SWEDEN
- âCHâ - SWITZERLAND
- âUAâ - UKRAINE
- âAEâ - UNITED ARAB EMIRATES
- âUSâ - UNITED STATES
- âUKâ - UNITED KINGDOM
- âUYâ - URUGUAY
- âVEâ - VENEZUELA

key -> (string)

value -> (list)

(string)

JSON Syntax:

```
{
  "DatasetGroupArn": "string",
  "AttributeConfigs": [
    {
      "AttributeName": "string",
      "Transformations": {"string": "string"
        ...}
    }
    ...
  ],
  "AdditionalDatasets": [
    {
      "Name": "string",
      "Configuration": {"string": ["string", ...]
        ...}
    }
    ...
  ]
}
```

`--encryption-config` (structure)

An Key Management Service (KMS) key and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key. You can specify this optional object in the  CreateDataset and  CreatePredictor requests.

RoleArn -> (string)

The ARN of the IAM role that Amazon Forecast can assume to access the KMS key.

Passing a role across Amazon Web Services accounts is not allowed. If you pass a role that isnât in your account, you get an `InvalidInputException` error.

KMSKeyArn -> (string)

The Amazon Resource Name (ARN) of the KMS key.

Shorthand Syntax:

```
RoleArn=string,KMSKeyArn=string
```

JSON Syntax:

```
{
  "RoleArn": "string",
  "KMSKeyArn": "string"
}
```

`--reference-predictor-arn` (string)

The ARN of the predictor to retrain or upgrade. This parameter is only used when retraining or upgrading a predictor. When creating a new predictor, do not specify a value for this parameter.

When upgrading or retraining a predictor, only specify values for the `ReferencePredictorArn` and `PredictorName` . The value for `PredictorName` must be a unique predictor name.

`--optimization-metric` (string)

The accuracy metric used to optimize the predictor.

Possible values:

- `WAPE`
- `RMSE`
- `AverageWeightedQuantileLoss`
- `MASE`
- `MAPE`

`--explain-predictor` | `--no-explain-predictor` (boolean)

Create an Explainability resource for the predictor.

`--tags` (list)

Optional metadata to help you categorize and organize your predictors. Each tag consists of a key and an optional value, both of which you define. Tag keys and values are case sensitive.

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

`--monitor-config` (structure)

The configuration details for predictor monitoring. Provide a name for the monitor resource to enable predictor monitoring.

Predictor monitoring allows you to see how your predictorâs performance changes over time. For more information, see [Predictor Monitoring](https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring.html) .

MonitorName -> (string)

The name of the monitor resource.

Shorthand Syntax:

```
MonitorName=string
```

JSON Syntax:

```
{
  "MonitorName": "string"
}
```

`--time-alignment-boundary` (structure)

The time boundary Forecast uses to align and aggregate any data that doesnât align with your forecast frequency. Provide the unit of time and the time boundary as a key value pair. For more information on specifying a time boundary, see [Specifying a Time Boundary](https://docs.aws.amazon.com/forecast/latest/dg/data-aggregation.html#specifying-time-boundary) . If you donât provide a time boundary, Forecast uses a set of [Default Time Boundaries](https://docs.aws.amazon.com/forecast/latest/dg/data-aggregation.html#default-time-boundaries) .

Month -> (string)

The month to use for time alignment during aggregation. The month must be in uppercase.

DayOfMonth -> (integer)

The day of the month to use for time alignment during aggregation.

DayOfWeek -> (string)

The day of week to use for time alignment during aggregation. The day must be in uppercase.

Hour -> (integer)

The hour of day to use for time alignment during aggregation.

Shorthand Syntax:

```
Month=string,DayOfMonth=integer,DayOfWeek=string,Hour=integer
```

JSON Syntax:

```
{
  "Month": "JANUARY"|"FEBRUARY"|"MARCH"|"APRIL"|"MAY"|"JUNE"|"JULY"|"AUGUST"|"SEPTEMBER"|"OCTOBER"|"NOVEMBER"|"DECEMBER",
  "DayOfMonth": integer,
  "DayOfWeek": "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY"|"SATURDAY"|"SUNDAY",
  "Hour": integer
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

PredictorArn -> (string)

The Amazon Resource Name (ARN) of the predictor.