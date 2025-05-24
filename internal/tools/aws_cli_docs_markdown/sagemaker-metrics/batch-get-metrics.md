# batch-get-metricsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-metrics/batch-get-metrics.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-metrics/batch-get-metrics.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker-metrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-metrics/index.html#cli-aws-sagemaker-metrics) ]

# batch-get-metrics

## Description

Used to retrieve training metrics from SageMaker.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-metrics-2022-09-30/BatchGetMetrics)

## Synopsis

```
batch-get-metrics
--metric-queries <value>
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

`--metric-queries` (list)

Queries made to retrieve training metrics from SageMaker.

(structure)

Specifies a query to retrieve training metrics from SageMaker.

MetricName -> (string)

The name of the metric to retrieve.

ResourceArn -> (string)

The ARN of the SageMaker resource to retrieve metrics for.

MetricStat -> (string)

The metrics stat type of metrics to retrieve.

Period -> (string)

The time period of metrics to retrieve.

XAxisType -> (string)

The x-axis type of metrics to retrieve.

Start -> (long)

The start time of metrics to retrieve.

End -> (long)

The end time of metrics to retrieve.

Shorthand Syntax:

```
MetricName=string,ResourceArn=string,MetricStat=string,Period=string,XAxisType=string,Start=long,End=long ...
```

JSON Syntax:

```
[
  {
    "MetricName": "string",
    "ResourceArn": "string",
    "MetricStat": "Min"|"Max"|"Avg"|"Count"|"StdDev"|"Last",
    "Period": "OneMinute"|"FiveMinute"|"OneHour"|"IterationNumber",
    "XAxisType": "IterationNumber"|"Timestamp",
    "Start": long,
    "End": long
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

MetricQueryResults -> (list)

The results of a query to retrieve training metrics from SageMaker.

(structure)

The result of a query to retrieve training metrics from SageMaker.

Status -> (string)

The status of the metric query.

Message -> (string)

A message describing the status of the metric query.

XAxisValues -> (list)

The values for the x-axis of the metrics.

(long)

MetricValues -> (list)

The metric values retrieved by the query.

(double)