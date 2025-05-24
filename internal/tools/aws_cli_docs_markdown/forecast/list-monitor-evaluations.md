# list-monitor-evaluationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-monitor-evaluations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-monitor-evaluations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [forecast](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/index.html#cli-aws-forecast) ]

# list-monitor-evaluations

## Description

Returns a list of the monitoring evaluation results and predictor events collected by the monitor resource during different windows of time.

For information about monitoring see  predictor-monitoring . For more information about retrieving monitoring results see [Viewing Monitoring Results](https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring-results.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/forecast-2018-06-26/ListMonitorEvaluations)

`list-monitor-evaluations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `PredictorMonitorEvaluations`

## Synopsis

```
list-monitor-evaluations
--monitor-arn <value>
[--filters <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--monitor-arn` (string)

The Amazon Resource Name (ARN) of the monitor resource to get results from.

`--filters` (list)

An array of filters. For each filter, provide a condition and a match statement. The condition is either `IS` or `IS_NOT` , which specifies whether to include or exclude the resources that match the statement from the list. The match statement consists of a key and a value.

**Filter properties**

- `Condition` - The condition to apply. Valid values are `IS` and `IS_NOT` .
- `Key` - The name of the parameter to filter on. The only valid value is `EvaluationState` .
- `Value` - The value to match. Valid values are only `SUCCESS` or `FAILURE` .

For example, to list only successful monitor evaluations, you would specify:

`"Filters": [ { "Condition": "IS", "Key": "EvaluationState", "Value": "SUCCESS" } ]`

(structure)

Describes a filter for choosing a subset of objects. Each filter consists of a condition and a match statement. The condition is either `IS` or `IS_NOT` , which specifies whether to include or exclude the objects that match the statement, respectively. The match statement consists of a key and a value.

Key -> (string)

The name of the parameter to filter on.

Value -> (string)

The value to match.

Condition -> (string)

The condition to apply. To include the objects that match the statement, specify `IS` . To exclude matching objects, specify `IS_NOT` .

Shorthand Syntax:

```
Key=string,Value=string,Condition=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string",
    "Condition": "IS"|"IS_NOT"
  }
  ...
]
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

NextToken -> (string)

If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.

PredictorMonitorEvaluations -> (list)

The monitoring results and predictor events collected by the monitor resource during different windows of time.

For information about monitoring see [Viewing Monitoring Results](https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring-results.html) . For more information about retrieving monitoring results see [Viewing Monitoring Results](https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring-results.html) .

(structure)

Describes the results of a monitor evaluation.

ResourceArn -> (string)

The Amazon Resource Name (ARN) of the resource to monitor.

MonitorArn -> (string)

The Amazon Resource Name (ARN) of the monitor resource.

EvaluationTime -> (timestamp)

The timestamp that indicates when the monitor evaluation was started.

EvaluationState -> (string)

The status of the monitor evaluation. The state can be `SUCCESS` or `FAILURE` .

WindowStartDatetime -> (timestamp)

The timestamp that indicates the start of the window that is used for monitor evaluation.

WindowEndDatetime -> (timestamp)

The timestamp that indicates the end of the window that is used for monitor evaluation.

PredictorEvent -> (structure)

Provides details about a predictor event, such as a retraining.

Detail -> (string)

The type of event. For example, `Retrain` . A retraining event denotes the timepoint when a predictor was retrained. Any monitor results from before the `Datetime` are from the previous predictor. Any new metrics are for the newly retrained predictor.

Datetime -> (timestamp)

The timestamp for when the event occurred.

MonitorDataSource -> (structure)

The source of the data the monitor resource used during the evaluation.

DatasetImportJobArn -> (string)

The Amazon Resource Name (ARN) of the dataset import job used to import the data that initiated the monitor evaluation.

ForecastArn -> (string)

The Amazon Resource Name (ARN) of the forecast the monitor used during the evaluation.

PredictorArn -> (string)

The Amazon Resource Name (ARN) of the predictor resource you are monitoring.

MetricResults -> (list)

A list of metrics Forecast calculated when monitoring a predictor. You can compare the value for each metric in the list to the metricâs value in the  Baseline to see how your predictorâs performance is changing.

(structure)

An individual metric Forecast calculated when monitoring predictor usage. You can compare the value for this metric to the metricâs value in the  Baseline to see how your predictorâs performance is changing.

For more information about metrics generated by Forecast see [Evaluating Predictor Accuracy](https://docs.aws.amazon.com/forecast/latest/dg/metrics.html)

MetricName -> (string)

The name of the metric.

MetricValue -> (double)

The value for the metric.

NumItemsEvaluated -> (long)

The number of items considered during the evaluation.

Message -> (string)

Information about any errors that may have occurred during the monitor evaluation.