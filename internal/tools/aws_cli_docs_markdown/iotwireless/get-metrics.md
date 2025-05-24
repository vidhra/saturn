# get-metricsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-metrics.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-metrics.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotwireless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/index.html#cli-aws-iotwireless) ]

# get-metrics

## Description

Get the summary metrics for this AWS account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotwireless-2020-11-22/GetMetrics)

## Synopsis

```
get-metrics
[--summary-metric-queries <value>]
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

`--summary-metric-queries` (list)

The list of queries to retrieve the summary metrics.

(structure)

The summary metric query object.

QueryId -> (string)

The id of the summary metric query.

MetricName -> (string)

The name of the metric.

Dimensions -> (list)

The dimensions of the summary metric.

(structure)

The required list of dimensions for the metric.

name -> (string)

The name of the dimension.

value -> (string)

The dimensionâs value.

AggregationPeriod -> (string)

The aggregation period of the summary metric.

StartTimestamp -> (timestamp)

The start timestamp for the summary metric query.

EndTimestamp -> (timestamp)

The end timestamp for the summary metric query.

Shorthand Syntax:

```
QueryId=string,MetricName=string,Dimensions=[{name=string,value=string},{name=string,value=string}],AggregationPeriod=string,StartTimestamp=timestamp,EndTimestamp=timestamp ...
```

JSON Syntax:

```
[
  {
    "QueryId": "string",
    "MetricName": "DeviceRSSI"|"DeviceSNR"|"DeviceRoamingRSSI"|"DeviceRoamingSNR"|"DeviceUplinkCount"|"DeviceDownlinkCount"|"DeviceUplinkLostCount"|"DeviceUplinkLostRate"|"DeviceJoinRequestCount"|"DeviceJoinAcceptCount"|"DeviceRoamingUplinkCount"|"DeviceRoamingDownlinkCount"|"GatewayUpTime"|"GatewayDownTime"|"GatewayRSSI"|"GatewaySNR"|"GatewayUplinkCount"|"GatewayDownlinkCount"|"GatewayJoinRequestCount"|"GatewayJoinAcceptCount"|"AwsAccountUplinkCount"|"AwsAccountDownlinkCount"|"AwsAccountUplinkLostCount"|"AwsAccountUplinkLostRate"|"AwsAccountJoinRequestCount"|"AwsAccountJoinAcceptCount"|"AwsAccountRoamingUplinkCount"|"AwsAccountRoamingDownlinkCount"|"AwsAccountDeviceCount"|"AwsAccountGatewayCount"|"AwsAccountActiveDeviceCount"|"AwsAccountActiveGatewayCount",
    "Dimensions": [
      {
        "name": "DeviceId"|"GatewayId",
        "value": "string"
      }
      ...
    ],
    "AggregationPeriod": "OneHour"|"OneDay"|"OneWeek",
    "StartTimestamp": timestamp,
    "EndTimestamp": timestamp
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

SummaryMetricQueryResults -> (list)

The list of summary metrics that were retrieved.

(structure)

The result of the summary metrics aggregation operation.

QueryId -> (string)

The ID of the summary metric results query operation.

QueryStatus -> (string)

The status of the summary metric query result.

Error -> (string)

The error message for the summary metric query result.

MetricName -> (string)

The name of the summary metric query result.

Dimensions -> (list)

The dimensions of the metric.

(structure)

The required list of dimensions for the metric.

name -> (string)

The name of the dimension.

value -> (string)

The dimensionâs value.

AggregationPeriod -> (string)

The aggregation period of the metric.

StartTimestamp -> (timestamp)

The start timestamp for the summary metric query.

EndTimestamp -> (timestamp)

The end timestamp for the summary metric query.

Timestamps -> (list)

The timestamp of each aggregation result.

(timestamp)

Values -> (list)

The list of aggregated summary metric query results.

(structure)

The aggregated values of the metric.

Min -> (double)

The minimum of the values of all data points collected during the aggregation period.

Max -> (double)

The maximum of the values of all the data points collected during the aggregation period.

Sum -> (double)

The sum of the values of all data points collected during the aggregation period.

Avg -> (double)

The average of the values of all data points collected during the aggregation period.

Std -> (double)

The standard deviation of the values of all data points collected during the aggregation period.

P90 -> (double)

The 90th percentile of the values of all data points collected during the aggregation period.

Unit -> (string)

The units of measurement to be used for interpreting the aggregation result.