# get-experiment-resultsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/get-experiment-results.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/get-experiment-results.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [evidently](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/index.html#cli-aws-evidently) ]

# get-experiment-results

## Description

Retrieves the results of a running or completed experiment. No results are available until there have been 100 events for each variation and at least 10 minutes have passed since the start of the experiment. To increase the statistical power, Evidently performs an additional offline p-value analysis at the end of the experiment. Offline p-value analysis can detect statistical significance in some cases where the anytime p-values used during the experiment do not find statistical significance.

Experiment results are available up to 63 days after the start of the experiment. They are not available after that because of CloudWatch data retention policies.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/evidently-2021-02-01/GetExperimentResults)

## Synopsis

```
get-experiment-results
[--base-stat <value>]
[--end-time <value>]
--experiment <value>
--metric-names <value>
[--period <value>]
--project <value>
[--report-names <value>]
[--result-stats <value>]
[--start-time <value>]
--treatment-names <value>
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

`--base-stat` (string)

The statistic used to calculate experiment results. Currently the only valid value is `mean` , which uses the mean of the collected values as the statistic.

Possible values:

- `Mean`

`--end-time` (timestamp)

The date and time that the experiment ended, if it is completed. This must be no longer than 30 days after the experiment start time.

`--experiment` (string)

The name of the experiment to retrieve the results of.

`--metric-names` (list)

The names of the experiment metrics that you want to see the results of.

(string)

Syntax:

```
"string" "string" ...
```

`--period` (long)

In seconds, the amount of time to aggregate results together.

`--project` (string)

The name or ARN of the project that contains the experiment that you want to see the results of.

`--report-names` (list)

The names of the report types that you want to see. Currently, `BayesianInference` is the only valid value.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  BayesianInference
```

`--result-stats` (list)

The statistics that you want to see in the returned results.

- `PValue` specifies to use p-values for the results. A p-value is used in hypothesis testing to measure how often you are willing to make a mistake in rejecting the null hypothesis. A general practice is to reject the null hypothesis and declare that the results are statistically significant when the p-value is less than 0.05.
- `ConfidenceInterval` specifies a confidence interval for the results. The confidence interval represents the range of values for the chosen metric that is likely to contain the true difference between the `baseStat` of a variation and the baseline. Evidently returns the 95% confidence interval.
- `TreatmentEffect` is the difference in the statistic specified by the `baseStat` parameter between each variation and the default variation.
- `BaseStat` returns the statistical values collected for the metric for each variation. The statistic uses the same statistic specified in the `baseStat` parameter. Therefore, if `baseStat` is `mean` , this returns the mean of the values collected for each variation.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  BaseStat
  TreatmentEffect
  ConfidenceInterval
  PValue
```

`--start-time` (timestamp)

The date and time that the experiment started.

`--treatment-names` (list)

The names of the experiment treatments that you want to see the results for.

(string)

Syntax:

```
"string" "string" ...
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

details -> (string)

If the experiment doesnât yet have enough events to provide valid results, this field is returned with the message `Not enough events to generate results` . If there are enough events to provide valid results, this field is not returned.

reports -> (list)

An array of structures that include the reports that you requested.

(structure)

A structure that contains results of an experiment.

content -> (string)

The content of the report.

metricName -> (string)

The name of the metric that is analyzed in this experiment report.

reportName -> (string)

The type of analysis used for this report.

treatmentName -> (string)

The name of the variation that this report pertains to.

resultsData -> (list)

An array of structures that include experiment results including metric names and values.

(structure)

A structure that contains experiment results for one metric that is monitored in the experiment.

metricName -> (string)

The name of the metric.

resultStat -> (string)

The experiment statistic that these results pertain to.

treatmentName -> (string)

The treatment, or variation, that returned the `values` in this structure.

values -> (list)

The values for the `metricName` that were recorded in the experiment.

(double)

timestamps -> (list)

The timestamps of each result returned.

(timestamp)