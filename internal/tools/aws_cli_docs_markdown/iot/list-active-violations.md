# list-active-violationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-active-violations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-active-violations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# list-active-violations

## Description

Lists the active violations for a given Device Defender security profile.

Requires permission to access the [ListActiveViolations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListActiveViolations)

`list-active-violations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `activeViolations`

## Synopsis

```
list-active-violations
[--thing-name <value>]
[--security-profile-name <value>]
[--behavior-criteria-type <value>]
[--list-suppressed-alerts | --no-list-suppressed-alerts]
[--verification-state <value>]
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

`--thing-name` (string)

The name of the thing whose active violations are listed.

`--security-profile-name` (string)

The name of the Device Defender security profile for which violations are listed.

`--behavior-criteria-type` (string)

The criteria for a behavior.

Possible values:

- `STATIC`
- `STATISTICAL`
- `MACHINE_LEARNING`

`--list-suppressed-alerts` | `--no-list-suppressed-alerts` (boolean)

A list of all suppressed alerts.

`--verification-state` (string)

The verification state of the violation (detect alarm).

Possible values:

- `FALSE_POSITIVE`
- `BENIGN_POSITIVE`
- `TRUE_POSITIVE`
- `UNKNOWN`

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To list the active violations**

The following `list-active-violations` example lists all violations for the specified security profile.

```
aws iot list-active-violations \
    --security-profile-name Testprofile
```

Output:

```
{
    "activeViolations": [
        {
            "violationId": "174db59167fa474c80a652ad1583fd44",
            "thingName": "iotconsole-1560269126751-1",
            "securityProfileName": "Testprofile",
            "behavior": {
                "name": "Authorization",
                "metric": "aws:num-authorization-failures",
                "criteria": {
                    "comparisonOperator": "greater-than",
                    "value": {
                        "count": 10
                    },
                    "durationSeconds": 300,
                    "consecutiveDatapointsToAlarm": 1,
                    "consecutiveDatapointsToClear": 1
                }
            },
            "lastViolationValue": {
                "count": 0
            },
            "lastViolationTime": 1560293700.0,
            "violationStartTime": 1560279000.0
        },
        {
            "violationId": "c8a9466a093d3b7b35cd44ca58bdbeab",
            "thingName": "TvnQoEoU",
            "securityProfileName": "Testprofile",
            "behavior": {
                "name": "CellularBandwidth",
                "metric": "aws:message-byte-size",
                "criteria": {
                    "comparisonOperator": "greater-than",
                    "value": {
                        "count": 128
                    },
                    "consecutiveDatapointsToAlarm": 1,
                    "consecutiveDatapointsToClear": 1
                }
            },
            "lastViolationValue": {
                "count": 110
            },
            "lastViolationTime": 1560369000.0,
            "violationStartTime": 1560276600.0
        },
        {
            "violationId": "74aa393adea02e6648f3ac362beed55e",
            "thingName": "iotconsole-1560269232412-2",
            "securityProfileName": "Testprofile",
            "behavior": {
                "name": "Authorization",
                "metric": "aws:num-authorization-failures",
                "criteria": {
                    "comparisonOperator": "greater-than",
                    "value": {
                        "count": 10
                    },
                    "durationSeconds": 300,
                    "consecutiveDatapointsToAlarm": 1,
                    "consecutiveDatapointsToClear": 1
                }
            },
            "lastViolationValue": {
                "count": 0
            },
            "lastViolationTime": 1560276600.0,
            "violationStartTime": 1560276600.0
        },
        {
            "violationId": "1e6ab5f7cf39a1466fcd154e1377e406",
            "thingName": "TvnQoEoU",
            "securityProfileName": "Testprofile",
            "behavior": {
                "name": "Authorization",
                "metric": "aws:num-authorization-failures",
                "criteria": {
                    "comparisonOperator": "greater-than",
                    "value": {
                        "count": 10
                    },
                    "durationSeconds": 300,
                    "consecutiveDatapointsToAlarm": 1,
                    "consecutiveDatapointsToClear": 1
                }
            },
            "lastViolationValue": {
                "count": 0
            },
            "lastViolationTime": 1560369000.0,
            "violationStartTime": 1560276600.0
        }
    ]
}
```

## Output

activeViolations -> (list)

The list of active violations.

(structure)

Information about an active Device Defender security profile behavior violation.

violationId -> (string)

The ID of the active violation.

thingName -> (string)

The name of the thing responsible for the active violation.

securityProfileName -> (string)

The security profile with the behavior is in violation.

behavior -> (structure)

The behavior that is being violated.

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

lastViolationValue -> (structure)

The value of the metric (the measurement) that caused the most recent violation.

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

violationEventAdditionalInfo -> (structure)

The details of a violation event.

confidenceLevel -> (string)

The sensitivity of anomalous behavior evaluation. Can be `Low` , `Medium` , or `High` .

verificationState -> (string)

The verification state of the violation (detect alarm).

verificationStateDescription -> (string)

The description of the verification state of the violation.

lastViolationTime -> (timestamp)

The time the most recent violation occurred.

violationStartTime -> (timestamp)

The time the violation started.

nextToken -> (string)

A token that can be used to retrieve the next set of results, or `null` if there are no additional results.