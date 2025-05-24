# create-predictorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-predictor.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-predictor.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [forecast](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/index.html#cli-aws-forecast) ]

# create-predictor

## Description

### Note

This operation creates a legacy predictor that does not include all the predictor functionalities provided by Amazon Forecast. To create a predictor that is compatible with all aspects of Forecast, use  CreateAutoPredictor .

Creates an Amazon Forecast predictor.

In the request, provide a dataset group and either specify an algorithm or let Amazon Forecast choose an algorithm for you using AutoML. If you specify an algorithm, you also can override algorithm-specific hyperparameters.

Amazon Forecast uses the algorithm to train a predictor using the latest version of the datasets in the specified dataset group. You can then generate a forecast using the  CreateForecast operation.

To see the evaluation metrics, use the  GetAccuracyMetrics operation.

You can specify a featurization configuration to fill and aggregate the data fields in the `TARGET_TIME_SERIES` dataset to improve model training. For more information, see  FeaturizationConfig .

For RELATED_TIME_SERIES datasets, `CreatePredictor` verifies that the `DataFrequency` specified when the dataset was created matches the `ForecastFrequency` . TARGET_TIME_SERIES datasets donât have this restriction. Amazon Forecast also verifies the delimiter and timestamp format. For more information, see  howitworks-datasets-groups .

By default, predictors are trained and evaluated at the 0.1 (P10), 0.5 (P50), and 0.9 (P90) quantiles. You can choose custom forecast types to train and evaluate your predictor by setting the `ForecastTypes` .

**AutoML**

If you want Amazon Forecast to evaluate each algorithm and choose the one that minimizes the `objective function` , set `PerformAutoML` to `true` . The `objective function` is defined as the mean of the weighted losses over the forecast types. By default, these are the p10, p50, and p90 quantile losses. For more information, see  EvaluationResult .

When AutoML is enabled, the following properties are disallowed:

- `AlgorithmArn`
- `HPOConfig`
- `PerformHPO`
- `TrainingParameters`

To get a list of all of your predictors, use the  ListPredictors operation.

### Note

Before you can use the predictor to create a forecast, the `Status` of the predictor must be `ACTIVE` , signifying that training has completed. To get the status, use the  DescribePredictor operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/forecast-2018-06-26/CreatePredictor)

## Synopsis

```
create-predictor
--predictor-name <value>
[--algorithm-arn <value>]
--forecast-horizon <value>
[--forecast-types <value>]
[--perform-auto-ml | --no-perform-auto-ml]
[--auto-ml-override-strategy <value>]
[--perform-hpo | --no-perform-hpo]
[--training-parameters <value>]
[--evaluation-parameters <value>]
[--hpo-config <value>]
--input-data-config <value>
--featurization-config <value>
[--encryption-config <value>]
[--tags <value>]
[--optimization-metric <value>]
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

A name for the predictor.

`--algorithm-arn` (string)

The Amazon Resource Name (ARN) of the algorithm to use for model training. Required if `PerformAutoML` is not set to `true` .

**Supported algorithms:**

- `arn:aws:forecast:::algorithm/ARIMA`
- `arn:aws:forecast:::algorithm/CNN-QR`
- `arn:aws:forecast:::algorithm/Deep_AR_Plus`
- `arn:aws:forecast:::algorithm/ETS`
- `arn:aws:forecast:::algorithm/NPTS`
- `arn:aws:forecast:::algorithm/Prophet`

`--forecast-horizon` (integer)

Specifies the number of time-steps that the model is trained to predict. The forecast horizon is also called the prediction length.

For example, if you configure a dataset for daily data collection (using the `DataFrequency` parameter of the  CreateDataset operation) and set the forecast horizon to 10, the model returns predictions for 10 days.

The maximum forecast horizon is the lesser of 500 time-steps or 1/3 of the TARGET_TIME_SERIES dataset length.

`--forecast-types` (list)

Specifies the forecast types used to train a predictor. You can specify up to five forecast types. Forecast types can be quantiles from 0.01 to 0.99, by increments of 0.01 or higher. You can also specify the mean forecast with `mean` .

The default value is `["0.10", "0.50", "0.9"]` .

(string)

Syntax:

```
"string" "string" ...
```

`--perform-auto-ml` | `--no-perform-auto-ml` (boolean)

Whether to perform AutoML. When Amazon Forecast performs AutoML, it evaluates the algorithms it provides and chooses the best algorithm and configuration for your training dataset.

The default value is `false` . In this case, you are required to specify an algorithm.

Set `PerformAutoML` to `true` to have Amazon Forecast perform AutoML. This is a good option if you arenât sure which algorithm is suitable for your training data. In this case, `PerformHPO` must be false.

`--auto-ml-override-strategy` (string)

### Note

The `LatencyOptimized` AutoML override strategy is only available in private beta. Contact Amazon Web Services Support or your account manager to learn more about access privileges.

Used to overide the default AutoML strategy, which is to optimize predictor accuracy. To apply an AutoML strategy that minimizes training time, use `LatencyOptimized` .

This parameter is only valid for predictors trained using AutoML.

Possible values:

- `LatencyOptimized`
- `AccuracyOptimized`

`--perform-hpo` | `--no-perform-hpo` (boolean)

Whether to perform hyperparameter optimization (HPO). HPO finds optimal hyperparameter values for your training data. The process of performing HPO is known as running a hyperparameter tuning job.

The default value is `false` . In this case, Amazon Forecast uses default hyperparameter values from the chosen algorithm.

To override the default values, set `PerformHPO` to `true` and, optionally, supply the  HyperParameterTuningJobConfig object. The tuning job specifies a metric to optimize, which hyperparameters participate in tuning, and the valid range for each tunable hyperparameter. In this case, you are required to specify an algorithm and `PerformAutoML` must be false.

The following algorithms support HPO:

- DeepAR+
- CNN-QR

`--training-parameters` (map)

The hyperparameters to override for model training. The hyperparameters that you can override are listed in the individual algorithms. For the list of supported algorithms, see  aws-forecast-choosing-recipes .

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

`--evaluation-parameters` (structure)

Used to override the default evaluation parameters of the specified algorithm. Amazon Forecast evaluates a predictor by splitting a dataset into training data and testing data. The evaluation parameters define how to perform the split and the number of iterations.

NumberOfBacktestWindows -> (integer)

The number of times to split the input data. The default is 1. Valid values are 1 through 5.

BackTestWindowOffset -> (integer)

The point from the end of the dataset where you want to split the data for model training and testing (evaluation). Specify the value as the number of data points. The default is the value of the forecast horizon. `BackTestWindowOffset` can be used to mimic a past virtual forecast start date. This value must be greater than or equal to the forecast horizon and less than half of the TARGET_TIME_SERIES dataset length.

`ForecastHorizon` <= `BackTestWindowOffset` < 1/2 * TARGET_TIME_SERIES dataset length

Shorthand Syntax:

```
NumberOfBacktestWindows=integer,BackTestWindowOffset=integer
```

JSON Syntax:

```
{
  "NumberOfBacktestWindows": integer,
  "BackTestWindowOffset": integer
}
```

`--hpo-config` (structure)

Provides hyperparameter override values for the algorithm. If you donât provide this parameter, Amazon Forecast uses default values. The individual algorithms specify which hyperparameters support hyperparameter optimization (HPO). For more information, see  aws-forecast-choosing-recipes .

If you included the `HPOConfig` object, you must set `PerformHPO` to true.

ParameterRanges -> (structure)

Specifies the ranges of valid values for the hyperparameters.

CategoricalParameterRanges -> (list)

Specifies the tunable range for each categorical hyperparameter.

(structure)

Specifies a categorical hyperparameter and itâs range of tunable values. This object is part of the  ParameterRanges object.

Name -> (string)

The name of the categorical hyperparameter to tune.

Values -> (list)

A list of the tunable categories for the hyperparameter.

(string)

ContinuousParameterRanges -> (list)

Specifies the tunable range for each continuous hyperparameter.

(structure)

Specifies a continuous hyperparameter and itâs range of tunable values. This object is part of the  ParameterRanges object.

Name -> (string)

The name of the hyperparameter to tune.

MaxValue -> (double)

The maximum tunable value of the hyperparameter.

MinValue -> (double)

The minimum tunable value of the hyperparameter.

ScalingType -> (string)

The scale that hyperparameter tuning uses to search the hyperparameter range. Valid values:

Auto

Amazon Forecast hyperparameter tuning chooses the best scale for the hyperparameter.

Linear

Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.

Logarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.

Logarithmic scaling works only for ranges that have values greater than 0.

ReverseLogarithmic

hyperparameter tuning searches the values in the hyperparameter range by using a reverse logarithmic scale.

Reverse logarithmic scaling works only for ranges that are entirely within the range 0 <= x < 1.0.

For information about choosing a hyperparameter scale, see [Hyperparameter Scaling](http://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type) . One of the following values:

IntegerParameterRanges -> (list)

Specifies the tunable range for each integer hyperparameter.

(structure)

Specifies an integer hyperparameter and itâs range of tunable values. This object is part of the  ParameterRanges object.

Name -> (string)

The name of the hyperparameter to tune.

MaxValue -> (integer)

The maximum tunable value of the hyperparameter.

MinValue -> (integer)

The minimum tunable value of the hyperparameter.

ScalingType -> (string)

The scale that hyperparameter tuning uses to search the hyperparameter range. Valid values:

Auto

Amazon Forecast hyperparameter tuning chooses the best scale for the hyperparameter.

Linear

Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.

Logarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.

Logarithmic scaling works only for ranges that have values greater than 0.

ReverseLogarithmic

Not supported for `IntegerParameterRange` .

Reverse logarithmic scaling works only for ranges that are entirely within the range 0 <= x < 1.0.

For information about choosing a hyperparameter scale, see [Hyperparameter Scaling](http://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type) . One of the following values:

JSON Syntax:

```
{
  "ParameterRanges": {
    "CategoricalParameterRanges": [
      {
        "Name": "string",
        "Values": ["string", ...]
      }
      ...
    ],
    "ContinuousParameterRanges": [
      {
        "Name": "string",
        "MaxValue": double,
        "MinValue": double,
        "ScalingType": "Auto"|"Linear"|"Logarithmic"|"ReverseLogarithmic"
      }
      ...
    ],
    "IntegerParameterRanges": [
      {
        "Name": "string",
        "MaxValue": integer,
        "MinValue": integer,
        "ScalingType": "Auto"|"Linear"|"Logarithmic"|"ReverseLogarithmic"
      }
      ...
    ]
  }
}
```

`--input-data-config` (structure)

Describes the dataset group that contains the data to use to train the predictor.

DatasetGroupArn -> (string)

The Amazon Resource Name (ARN) of the dataset group.

SupplementaryFeatures -> (list)

An array of supplementary features. The only supported feature is a holiday calendar.

(structure)

### Note

This object belongs to the  CreatePredictor operation. If you created your predictor with  CreateAutoPredictor , see  AdditionalDataset .

Describes a supplementary feature of a dataset group. This object is part of the  InputDataConfig object. Forecast supports the Weather Index and Holidays built-in featurizations.

**Weather Index**

The Amazon Forecast Weather Index is a built-in featurization that incorporates historical and projected weather information into your model. The Weather Index supplements your datasets with over two years of historical weather data and up to 14 days of projected weather data. For more information, see [Amazon Forecast Weather Index](https://docs.aws.amazon.com/forecast/latest/dg/weather.html) .

**Holidays**

Holidays is a built-in featurization that incorporates a feature-engineered dataset of national holiday information into your model. It provides native support for the holiday calendars of 66 countries. To view the holiday calendars, refer to the [Jollyday](http://jollyday.sourceforge.net/data.html) library. For more information, see [Holidays Featurization](https://docs.aws.amazon.com/forecast/latest/dg/holidays.html) .

Name -> (string)

The name of the feature. Valid values: `"holiday"` and `"weather"` .

Value -> (string)

**Weather Index**

To enable the Weather Index, set the value to `"true"`

**Holidays**

To enable Holidays, specify a country with one of the following two-letter country codes:

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

Shorthand Syntax:

```
DatasetGroupArn=string,SupplementaryFeatures=[{Name=string,Value=string},{Name=string,Value=string}]
```

JSON Syntax:

```
{
  "DatasetGroupArn": "string",
  "SupplementaryFeatures": [
    {
      "Name": "string",
      "Value": "string"
    }
    ...
  ]
}
```

`--featurization-config` (structure)

The featurization configuration.

ForecastFrequency -> (string)

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

When a RELATED_TIME_SERIES dataset is provided, the frequency must be equal to the TARGET_TIME_SERIES dataset frequency.

ForecastDimensions -> (list)

An array of dimension (field) names that specify how to group the generated forecast.

For example, suppose that you are generating a forecast for item sales across all of your stores, and your dataset contains a `store_id` field. If you want the sales forecast for each item by store, you would specify `store_id` as the dimension.

All forecast dimensions specified in the `TARGET_TIME_SERIES` dataset donât need to be specified in the `CreatePredictor` request. All forecast dimensions specified in the `RELATED_TIME_SERIES` dataset must be specified in the `CreatePredictor` request.

(string)

Featurizations -> (list)

An array of featurization (transformation) information for the fields of a dataset.

(structure)

### Note

This object belongs to the  CreatePredictor operation. If you created your predictor with  CreateAutoPredictor , see  AttributeConfig .

Provides featurization (transformation) information for a dataset field. This object is part of the  FeaturizationConfig object.

For example:

`{`

`"AttributeName": "demand",`

`FeaturizationPipeline [ {`

`"FeaturizationMethodName": "filling",`

`"FeaturizationMethodParameters": {"aggregation": "avg", "backfill": "nan"}`

`} ]`

`}`

AttributeName -> (string)

The name of the schema attribute that specifies the data field to be featurized. Amazon Forecast supports the target field of the `TARGET_TIME_SERIES` and the `RELATED_TIME_SERIES` datasets. For example, for the `RETAIL` domain, the target is `demand` , and for the `CUSTOM` domain, the target is `target_value` . For more information, see  howitworks-missing-values .

FeaturizationPipeline -> (list)

An array of one `FeaturizationMethod` object that specifies the feature transformation method.

(structure)

Provides information about the method that featurizes (transforms) a dataset field. The method is part of the `FeaturizationPipeline` of the  Featurization object.

The following is an example of how you specify a `FeaturizationMethod` object.

`{`

`"FeaturizationMethodName": "filling",`

`"FeaturizationMethodParameters": {"aggregation": "sum", "middlefill": "zero", "backfill": "zero"}`

`}`

FeaturizationMethodName -> (string)

The name of the method. The âfillingâ method is the only supported method.

FeaturizationMethodParameters -> (map)

The method parameters (key-value pairs), which are a map of override parameters. Specify these parameters to override the default values. Related Time Series attributes do not accept aggregation parameters.

The following list shows the parameters and their valid values for the âfillingâ featurization method for a **Target Time Series** dataset. Bold signifies the default value.

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

JSON Syntax:

```
{
  "ForecastFrequency": "string",
  "ForecastDimensions": ["string", ...],
  "Featurizations": [
    {
      "AttributeName": "string",
      "FeaturizationPipeline": [
        {
          "FeaturizationMethodName": "filling",
          "FeaturizationMethodParameters": {"string": "string"
            ...}
        }
        ...
      ]
    }
    ...
  ]
}
```

`--encryption-config` (structure)

An Key Management Service (KMS) key and the Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key.

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

`--tags` (list)

The optional metadata that you apply to the predictor to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.

The following basic restrictions apply to tags:

- Maximum number of tags per resource - 50.
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length - 128 Unicode characters in UTF-8.
- Maximum value length - 256 Unicode characters in UTF-8.
- If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
- Tag keys and values are case sensitive.
- Do not use `aws:` , `AWS:` , or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has `aws` as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of `aws` do not count against your tags per resource limit.

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

`--optimization-metric` (string)

The accuracy metric used to optimize the predictor.

Possible values:

- `WAPE`
- `RMSE`
- `AverageWeightedQuantileLoss`
- `MASE`
- `MAPE`

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