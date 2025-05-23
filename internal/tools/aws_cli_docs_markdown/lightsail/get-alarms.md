# get-alarmsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-alarms.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-alarms.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# get-alarms

## Description

Returns information about the configured alarms. Specify an alarm name in your request to return information about a specific alarm, or specify a monitored resource name to return information about all alarms for a specific resource.

An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see [Alarms in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-alarms) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetAlarms)

## Synopsis

```
get-alarms
[--alarm-name <value>]
[--page-token <value>]
[--monitored-resource-name <value>]
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

`--alarm-name` (string)

The name of the alarm.

Specify an alarm name to return information about a specific alarm.

`--page-token` (string)

The token to advance to the next page of results from your request.

To get a page token, perform an initial `GetAlarms` request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.

`--monitored-resource-name` (string)

The name of the Lightsail resource being monitored by the alarm.

Specify a monitored resource name to return information about all alarms for a specific resource.

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

alarms -> (list)

An array of objects that describe the alarms.

(structure)

Describes an alarm.

An alarm is a way to monitor your Lightsail resource metrics. For more information, see [Alarms in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-alarms) .

name -> (string)

The name of the alarm.

arn -> (string)

The Amazon Resource Name (ARN) of the alarm.

createdAt -> (timestamp)

The timestamp when the alarm was created.

location -> (structure)

An object that lists information about the location of the alarm.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

resourceType -> (string)

The Lightsail resource type of the alarm.

supportCode -> (string)

The support code. Include this code in your email to support when you have questions about your Lightsail alarm. This code enables our support team to look up your Lightsail information more easily.

monitoredResourceInfo -> (structure)

An object that lists information about the resource monitored by the alarm.

arn -> (string)

The Amazon Resource Name (ARN) of the resource being monitored.

name -> (string)

The name of the Lightsail resource being monitored.

resourceType -> (string)

The Lightsail resource type of the resource being monitored.

Instances, load balancers, and relational databases are the only Lightsail resources that can currently be monitored by alarms.

comparisonOperator -> (string)

The arithmetic operation used when comparing the specified statistic and threshold.

evaluationPeriods -> (integer)

The number of periods over which data is compared to the specified threshold.

period -> (integer)

The period, in seconds, over which the statistic is applied.

threshold -> (double)

The value against which the specified statistic is compared.

datapointsToAlarm -> (integer)

The number of data points that must not within the specified threshold to trigger the alarm.

treatMissingData -> (string)

Specifies how the alarm handles missing data points.

An alarm can treat missing data in the following ways:

- `breaching` - Assume the missing data is not within the threshold. Missing data counts towards the number of times the metric is not within the threshold.
- `notBreaching` - Assume the missing data is within the threshold. Missing data does not count towards the number of times the metric is not within the threshold.
- `ignore` - Ignore the missing data. Maintains the current alarm state.
- `missing` - Missing data is treated as missing.

statistic -> (string)

The statistic for the metric associated with the alarm.

The following statistics are available:

- `Minimum` - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.
- `Maximum` - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.
- `Sum` - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.
- `Average` - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum values, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum values. This comparison helps you to know when to increase or decrease your resources.
- `SampleCount` - The count, or number, of data points used for the statistical calculation.

metricName -> (string)

The name of the metric associated with the alarm.

state -> (string)

The current state of the alarm.

An alarm has the following possible states:

- `ALARM` - The metric is outside of the defined threshold.
- `INSUFFICIENT_DATA` - The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.
- `OK` - The metric is within the defined threshold.

unit -> (string)

The unit of the metric associated with the alarm.

contactProtocols -> (list)

The contact protocols for the alarm, such as `Email` , `SMS` (text messaging), or both.

(string)

notificationTriggers -> (list)

The alarm states that trigger a notification.

(string)

notificationEnabled -> (boolean)

Indicates whether the alarm is enabled.

nextPageToken -> (string)

The token to advance to the next page of results from your request.

A next page token is not returned if there are no more results to display.

To get the next page of results, perform another `GetAlarms` request and specify the next page token using the `pageToken` parameter.