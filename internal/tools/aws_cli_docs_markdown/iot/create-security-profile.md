# create-security-profileÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-security-profile.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-security-profile.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# create-security-profile

## Description

Creates a Device Defender security profile.

Requires permission to access the [CreateSecurityProfile](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateSecurityProfile)

## Synopsis

```
create-security-profile
--security-profile-name <value>
[--security-profile-description <value>]
[--behaviors <value>]
[--alert-targets <value>]
[--additional-metrics-to-retain <value>]
[--additional-metrics-to-retain-v2 <value>]
[--tags <value>]
[--metrics-export-config <value>]
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

`--security-profile-name` (string)

The name you are giving to the security profile.

`--security-profile-description` (string)

A description of the security profile.

`--behaviors` (list)

Specifies the behaviors that, when violated by a device (thing), cause an alert.

(structure)

A Device Defender security profile behavior.

name -> (string)

The name youâve given to the behavior.

metric -> (string)

What is measured by the behavior.

metricDimension -> (structure)

The dimension for a metric in your behavior. For example, using a `TOPIC_FILTER` dimension, you can narrow down the scope of the metric to only MQTT topics where the name matches the pattern specified in the dimension. This canât be used with custom metrics.

dimensionName -> (string)

A unique identifier for the dimension.

operator -> (string)

Defines how the `dimensionValues` of a dimension are interpreted. For example, for dimension type TOPIC_FILTER, the `IN` operator, a message will be counted only if its topic matches one of the topic filters. With `NOT_IN` operator, a message will be counted only if it doesnât match any of the topic filters. The operator is optional: if itâs not provided (is `null` ), it will be interpreted as `IN` .

criteria -> (structure)

The criteria that determine if a device is behaving normally in regard to the `metric` .

### Note

In the IoT console, you can choose to be sent an alert through Amazon SNS when IoT Device Defender detects that a device is behaving anomalously.

comparisonOperator -> (string)

The operator that relates the thing measured (`metric` ) to the criteria (containing a `value` or `statisticalThreshold` ). Valid operators include:

- `string-list` : `in-set` and `not-in-set`
- `number-list` : `in-set` and `not-in-set`
- `ip-address-list` : `in-cidr-set` and `not-in-cidr-set`
- `number` : `less-than` , `less-than-equals` , `greater-than` , and `greater-than-equals`

value -> (structure)

The value to be compared with the `metric` .

count -> (long)

If the `comparisonOperator` calls for a numeric value, use this to specify that numeric value to be compared with the `metric` .

cidrs -> (list)

If the `comparisonOperator` calls for a set of CIDRs, use this to specify that set to be compared with the `metric` .

(string)

ports -> (list)

If the `comparisonOperator` calls for a set of ports, use this to specify that set to be compared with the `metric` .

(integer)

number -> (double)

The numeral value of a metric.

numbers -> (list)

The numeral values of a metric.

(double)

strings -> (list)

The string values of a metric.

(string)

durationSeconds -> (integer)

Use this to specify the time duration over which the behavior is evaluated, for those criteria that have a time dimension (for example, `NUM_MESSAGES_SENT` ). For a `statisticalThreshhold` metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank. Cannot be used with list-based metric datatypes.

consecutiveDatapointsToAlarm -> (integer)

If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.

consecutiveDatapointsToClear -> (integer)

If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.

statisticalThreshold -> (structure)

A statistical ranking (percentile)that indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.

statistic -> (string)

The percentile that resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (`durationSeconds` ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (`comparisonOperator` ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.

mlDetectionConfig -> (structure)

The configuration of an ML Detect

confidenceLevel -> (string)

The sensitivity of anomalous behavior evaluation. Can be `Low` , `Medium` , or `High` .

suppressAlerts -> (boolean)

Suppresses alerts.

exportMetric -> (boolean)

Value indicates exporting metrics related to the behavior when it is true.

JSON Syntax:

```
[
  {
    "name": "string",
    "metric": "string",
    "metricDimension": {
      "dimensionName": "string",
      "operator": "IN"|"NOT_IN"
    },
    "criteria": {
      "comparisonOperator": "less-than"|"less-than-equals"|"greater-than"|"greater-than-equals"|"in-cidr-set"|"not-in-cidr-set"|"in-port-set"|"not-in-port-set"|"in-set"|"not-in-set",
      "value": {
        "count": long,
        "cidrs": ["string", ...],
        "ports": [integer, ...],
        "number": double,
        "numbers": [double, ...],
        "strings": ["string", ...]
      },
      "durationSeconds": integer,
      "consecutiveDatapointsToAlarm": integer,
      "consecutiveDatapointsToClear": integer,
      "statisticalThreshold": {
        "statistic": "string"
      },
      "mlDetectionConfig": {
        "confidenceLevel": "LOW"|"MEDIUM"|"HIGH"
      }
    },
    "suppressAlerts": true|false,
    "exportMetric": true|false
  }
  ...
]
```

`--alert-targets` (map)

Specifies the destinations to which alerts are sent. (Alerts are always sent to the console.) Alerts are generated when a device (thing) violates a behavior.

key -> (string)

The type of alert target: one of âSNSâ.

value -> (structure)

A structure containing the alert target ARN and the role ARN.

alertTargetArn -> (string)

The Amazon Resource Name (ARN) of the notification target to which alerts are sent.

roleArn -> (string)

The ARN of the role that grants permission to send alerts to the notification target.

Shorthand Syntax:

```
KeyName1=alertTargetArn=string,roleArn=string,KeyName2=alertTargetArn=string,roleArn=string

Where valid key names are:
  SNS
```

JSON Syntax:

```
{"SNS": {
      "alertTargetArn": "string",
      "roleArn": "string"
    }
  ...}
```

`--additional-metrics-to-retain` (list)

*Please use  CreateSecurityProfileRequest$additionalMetricsToRetainV2 instead.*

A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profileâs `behaviors` , but it is also retained for any metric specified here. Can be used with custom metrics; cannot be used with dimensions.

(string)

Syntax:

```
"string" "string" ...
```

`--additional-metrics-to-retain-v2` (list)

A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profileâs `behaviors` , but it is also retained for any metric specified here. Can be used with custom metrics; cannot be used with dimensions.

(structure)

The metric you want to retain. Dimensions are optional.

metric -> (string)

What is measured by the behavior.

metricDimension -> (structure)

The dimension of a metric. This canât be used with custom metrics.

dimensionName -> (string)

A unique identifier for the dimension.

operator -> (string)

Defines how the `dimensionValues` of a dimension are interpreted. For example, for dimension type TOPIC_FILTER, the `IN` operator, a message will be counted only if its topic matches one of the topic filters. With `NOT_IN` operator, a message will be counted only if it doesnât match any of the topic filters. The operator is optional: if itâs not provided (is `null` ), it will be interpreted as `IN` .

exportMetric -> (boolean)

The value indicates exporting metrics related to the `MetricToRetain` when itâs true.

Shorthand Syntax:

```
metric=string,metricDimension={dimensionName=string,operator=string},exportMetric=boolean ...
```

JSON Syntax:

```
[
  {
    "metric": "string",
    "metricDimension": {
      "dimensionName": "string",
      "operator": "IN"|"NOT_IN"
    },
    "exportMetric": true|false
  }
  ...
]
```

`--tags` (list)

Metadata that can be used to manage the security profile.

(structure)

A set of key/value pairs that are used to manage the resource.

Key -> (string)

The tagâs key.

Value -> (string)

The tagâs value.

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

`--metrics-export-config` (structure)

Specifies the MQTT topic and role ARN required for metric export.

mqttTopic -> (string)

The MQTT topic that Device Defender Detect should publish messages to for metrics export.

roleArn -> (string)

This role ARN has permission to publish MQTT messages, after which Device Defender Detect can assume the role and publish messages on your behalf.

Shorthand Syntax:

```
mqttTopic=string,roleArn=string
```

JSON Syntax:

```
{
  "mqttTopic": "string",
  "roleArn": "string"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a security profile**

The following `create-security-profile` example creates a security profile that checks if cellular bandwidth exceeds a threshold or if more than 10 authorization failures occur within a five-minute period.

```
aws iot create-security-profile \
    --security-profile-name PossibleIssue \
    --security-profile-description "Check to see if authorization fails 10 times in 5 minutes or if cellular bandwidth exceeds 128"  \
    --behaviors "[{\"name\":\"CellularBandwidth\",\"metric\":\"aws:message-byte-size\",\"criteria\":{\"comparisonOperator\":\"greater-than\",\"value\":{\"count\":128},\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}},{\"name\":\"Authorization\",\"metric\":\"aws:num-authorization-failures\",\"criteria\":{\"comparisonOperator\":\"less-than\",\"value\":{\"count\":10},\"durationSeconds\":300,\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}}]"
```

Output:

```
{
    "securityProfileName": "PossibleIssue",
    "securityProfileArn": "arn:aws:iot:us-west-2:123456789012:securityprofile/PossibleIssue"
}
```

For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html) in the *AWS IoT Developer Guide*.

## Output

securityProfileName -> (string)

The name you gave to the security profile.

securityProfileArn -> (string)

The ARN of the security profile.