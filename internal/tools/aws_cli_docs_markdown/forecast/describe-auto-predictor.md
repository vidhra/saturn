# describe-auto-predictorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-auto-predictor.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-auto-predictor.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [forecast](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/index.html#cli-aws-forecast) ]

# describe-auto-predictor

## Description

Describes a predictor created using the CreateAutoPredictor operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/forecast-2018-06-26/DescribeAutoPredictor)

## Synopsis

```
describe-auto-predictor
--predictor-arn <value>
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

`--predictor-arn` (string)

The Amazon Resource Name (ARN) of the predictor.

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

The Amazon Resource Name (ARN) of the predictor

PredictorName -> (string)

The name of the predictor.

ForecastHorizon -> (integer)

The number of time-steps that the model predicts. The forecast horizon is also called the prediction length.

ForecastTypes -> (list)

The forecast types used during predictor training. Default value is [â0.1â,â0.5â,â0.9â].

(string)

ForecastFrequency -> (string)

The frequency of predictions in a forecast.

Valid intervals are Y (Year), M (Month), W (Week), D (Day), H (Hour), 30min (30 minutes), 15min (15 minutes), 10min (10 minutes), 5min (5 minutes), and 1min (1 minute). For example, âYâ indicates every year and â5minâ indicates every five minutes.

ForecastDimensions -> (list)

An array of dimension (field) names that specify the attributes used to group your time series.

(string)

DatasetImportJobArns -> (list)

An array of the ARNs of the dataset import jobs used to import training data for the predictor.

(string)

DataConfig -> (structure)

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

EncryptionConfig -> (structure)

An Key Management Service (KMS) key and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key. You can specify this optional object in the  CreateDataset and  CreatePredictor requests.

RoleArn -> (string)

The ARN of the IAM role that Amazon Forecast can assume to access the KMS key.

Passing a role across Amazon Web Services accounts is not allowed. If you pass a role that isnât in your account, you get an `InvalidInputException` error.

KMSKeyArn -> (string)

The Amazon Resource Name (ARN) of the KMS key.

ReferencePredictorSummary -> (structure)

The ARN and state of the reference predictor. This parameter is only valid for retrained or upgraded predictors.

Arn -> (string)

The ARN of the reference predictor.

State -> (string)

Whether the reference predictor is `Active` or `Deleted` .

EstimatedTimeRemainingInMinutes -> (long)

The estimated time remaining in minutes for the predictor training job to complete.

Status -> (string)

The status of the predictor. States include:

- `ACTIVE`
- `CREATE_PENDING` , `CREATE_IN_PROGRESS` , `CREATE_FAILED`
- `CREATE_STOPPING` , `CREATE_STOPPED`
- `DELETE_PENDING` , `DELETE_IN_PROGRESS` , `DELETE_FAILED`

Message -> (string)

In the event of an error, a message detailing the cause of the error.

CreationTime -> (timestamp)

The timestamp of the CreateAutoPredictor request.

LastModificationTime -> (timestamp)

The last time the resource was modified. The timestamp depends on the status of the job:

- `CREATE_PENDING` - The `CreationTime` .
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or failed.

OptimizationMetric -> (string)

The accuracy metric used to optimize the predictor.

ExplainabilityInfo -> (structure)

Provides the status and ARN of the Predictor Explainability.

ExplainabilityArn -> (string)

The Amazon Resource Name (ARN) of the Explainability.

Status -> (string)

The status of the Explainability. States include:

- `ACTIVE`
- `CREATE_PENDING` , `CREATE_IN_PROGRESS` , `CREATE_FAILED`
- `CREATE_STOPPING` , `CREATE_STOPPED`
- `DELETE_PENDING` , `DELETE_IN_PROGRESS` , `DELETE_FAILED`

MonitorInfo -> (structure)

A object with the Amazon Resource Name (ARN) and status of the monitor resource.

MonitorArn -> (string)

The Amazon Resource Name (ARN) of the monitor resource.

Status -> (string)

The status of the monitor. States include:

- `ACTIVE`
- `ACTIVE_STOPPING` , `ACTIVE_STOPPED`
- `UPDATE_IN_PROGRESS`
- `CREATE_PENDING` , `CREATE_IN_PROGRESS` , `CREATE_FAILED`
- `DELETE_PENDING` , `DELETE_IN_PROGRESS` , `DELETE_FAILED`

TimeAlignmentBoundary -> (structure)

The time boundary Forecast uses when aggregating data.

Month -> (string)

The month to use for time alignment during aggregation. The month must be in uppercase.

DayOfMonth -> (integer)

The day of the month to use for time alignment during aggregation.

DayOfWeek -> (string)

The day of week to use for time alignment during aggregation. The day must be in uppercase.

Hour -> (integer)

The hour of day to use for time alignment during aggregation.