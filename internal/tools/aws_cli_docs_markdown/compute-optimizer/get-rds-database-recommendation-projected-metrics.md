# get-rds-database-recommendation-projected-metricsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-rds-database-recommendation-projected-metrics.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-rds-database-recommendation-projected-metrics.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# get-rds-database-recommendation-projected-metrics

## Description

Returns the projected metrics of Amazon RDS recommendations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendationProjectedMetrics)

## Synopsis

```
get-rds-database-recommendation-projected-metrics
--resource-arn <value>
--stat <value>
--period <value>
--start-time <value>
--end-time <value>
[--recommendation-preferences <value>]
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

`--resource-arn` (string)

The ARN that identifies the Amazon RDS.

The following is the format of the ARN:

`arn:aws:rds:{region}:{accountId}:db:{resourceName}`

`--stat` (string)

The statistic of the projected metrics.

Possible values:

- `Maximum`
- `Average`

`--period` (integer)

The granularity, in seconds, of the projected metrics data points.

`--start-time` (timestamp)

The timestamp of the first projected metrics data point to return.

`--end-time` (timestamp)

The timestamp of the last projected metrics data point to return.

`--recommendation-preferences` (structure)

Describes the recommendation preferences to return in the response of a  GetAutoScalingGroupRecommendations ,  GetEC2InstanceRecommendations ,  GetEC2RecommendationProjectedMetrics ,  GetRDSDatabaseRecommendations , and  GetRDSDatabaseRecommendationProjectedMetrics request.

cpuVendorArchitectures -> (list)

Specifies the CPU vendor and architecture for Amazon EC2 instance and Auto Scaling group recommendations.

For example, when you specify `AWS_ARM64` with:

- A  GetEC2InstanceRecommendations or  GetAutoScalingGroupRecommendations request, Compute Optimizer returns recommendations that consist of Graviton instance types only.
- A  GetEC2RecommendationProjectedMetrics request, Compute Optimizer returns projected utilization metrics for Graviton instance type recommendations only.
- A  ExportEC2InstanceRecommendations or  ExportAutoScalingGroupRecommendations request, Compute Optimizer exports recommendations that consist of Graviton instance types only.

(string)

Shorthand Syntax:

```
cpuVendorArchitectures=string,string
```

JSON Syntax:

```
{
  "cpuVendorArchitectures": ["AWS_ARM64"|"CURRENT", ...]
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

recommendedOptionProjectedMetrics -> (list)

An array of objects that describes the projected metrics.

(structure)

Describes the projected metrics of an Amazon RDS recommendation option.

To determine the performance difference between your current Amazon RDS and the recommended option, compare the metric data of your service against its projected metric data.

recommendedDBInstanceClass -> (string)

The recommended DB instance class for the Amazon RDS.

rank -> (integer)

The rank identifier of the RDS instance recommendation option.

projectedMetrics -> (list)

An array of objects that describe the projected metric.

(structure)

Describes the projected metrics of an Amazon RDS recommendation option.

To determine the performance difference between your current Amazon RDS and the recommended option, compare the metric data of your service against its projected metric data.

name -> (string)

The name of the projected metric.

timestamps -> (list)

The timestamps of the projected metric.

(timestamp)

values -> (list)

The values for the projected metric.

(double)