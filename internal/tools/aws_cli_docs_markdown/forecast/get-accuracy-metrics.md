# get-accuracy-metricsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/get-accuracy-metrics.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/get-accuracy-metrics.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [forecast](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/index.html#cli-aws-forecast) ]

# get-accuracy-metrics

## Description

Provides metrics on the accuracy of the models that were trained by the  CreatePredictor operation. Use metrics to see how well the model performed and to decide whether to use the predictor to generate a forecast. For more information, see [Predictor Metrics](https://docs.aws.amazon.com/forecast/latest/dg/metrics.html) .

This operation generates metrics for each backtest window that was evaluated. The number of backtest windows (`NumberOfBacktestWindows` ) is specified using the  EvaluationParameters object, which is optionally included in the `CreatePredictor` request. If `NumberOfBacktestWindows` isnât specified, the number defaults to one.

The parameters of the `filling` method determine which items contribute to the metrics. If you want all items to contribute, specify `zero` . If you want only those items that have complete data in the range being evaluated to contribute, specify `nan` . For more information, see  FeaturizationMethod .

### Note

Before you can get accuracy metrics, the `Status` of the predictor must be `ACTIVE` , signifying that training has completed. To get the status, use the  DescribePredictor operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/forecast-2018-06-26/GetAccuracyMetrics)

## Synopsis

```
get-accuracy-metrics
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

The Amazon Resource Name (ARN) of the predictor to get metrics for.

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

PredictorEvaluationResults -> (list)

An array of results from evaluating the predictor.

(structure)

The results of evaluating an algorithm. Returned as part of the  GetAccuracyMetrics response.

AlgorithmArn -> (string)

The Amazon Resource Name (ARN) of the algorithm that was evaluated.

TestWindows -> (list)

The array of test windows used for evaluating the algorithm. The `NumberOfBacktestWindows` from the  EvaluationParameters object determines the number of windows in the array.

(structure)

The metrics for a time range within the evaluation portion of a dataset. This object is part of the  EvaluationResult object.

The `TestWindowStart` and `TestWindowEnd` parameters are determined by the `BackTestWindowOffset` parameter of the  EvaluationParameters object.

TestWindowStart -> (timestamp)

The timestamp that defines the start of the window.

TestWindowEnd -> (timestamp)

The timestamp that defines the end of the window.

ItemCount -> (integer)

The number of data points within the window.

EvaluationType -> (string)

The type of evaluation.

- `SUMMARY` - The average metrics across all windows.
- `COMPUTED` - The metrics for the specified window.

Metrics -> (structure)

Provides metrics used to evaluate the performance of a predictor.

RMSE -> (double)

The root-mean-square error (RMSE).

WeightedQuantileLosses -> (list)

An array of weighted quantile losses. Quantiles divide a probability distribution into regions of equal probability. The distribution in this case is the loss function.

(structure)

The weighted loss value for a quantile. This object is part of the  Metrics object.

Quantile -> (double)

The quantile. Quantiles divide a probability distribution into regions of equal probability. For example, if the distribution was divided into 5 regions of equal probability, the quantiles would be 0.2, 0.4, 0.6, and 0.8.

LossValue -> (double)

The difference between the predicted value and the actual value over the quantile, weighted (normalized) by dividing by the sum over all quantiles.

ErrorMetrics -> (list)

Provides detailed error metrics for each forecast type. Metrics include root-mean square-error (RMSE), mean absolute percentage error (MAPE), mean absolute scaled error (MASE), and weighted average percentage error (WAPE).

(structure)

Provides detailed error metrics to evaluate the performance of a predictor. This object is part of the  Metrics object.

ForecastType -> (string)

The Forecast type used to compute WAPE, MAPE, MASE, and RMSE.

WAPE -> (double)

The weighted absolute percentage error (WAPE).

RMSE -> (double)

The root-mean-square error (RMSE).

MASE -> (double)

The Mean Absolute Scaled Error (MASE)

MAPE -> (double)

The Mean Absolute Percentage Error (MAPE)

AverageWeightedQuantileLoss -> (double)

The average value of all weighted quantile losses.

IsAutoPredictor -> (boolean)

Whether the predictor was created with  CreateAutoPredictor .

AutoMLOverrideStrategy -> (string)

### Note

The `LatencyOptimized` AutoML override strategy is only available in private beta. Contact Amazon Web Services Support or your account manager to learn more about access privileges.

The AutoML strategy used to train the predictor. Unless `LatencyOptimized` is specified, the AutoML strategy optimizes predictor accuracy.

This parameter is only valid for predictors trained using AutoML.

OptimizationMetric -> (string)

The accuracy metric used to optimize the predictor.