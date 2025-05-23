# put-alarmÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/put-alarm.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/put-alarm.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# put-alarm

## Description

Creates or updates an alarm, and associates it with the specified metric.

An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see [Alarms in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-alarms) .

When this action creates an alarm, the alarm state is immediately set to `INSUFFICIENT_DATA` . The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.

When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm. The alarm is then evaluated with the updated configuration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/PutAlarm)

## Synopsis

```
put-alarm
--alarm-name <value>
--metric-name <value>
--monitored-resource-name <value>
--comparison-operator <value>
--threshold <value>
--evaluation-periods <value>
[--datapoints-to-alarm <value>]
[--treat-missing-data <value>]
[--contact-protocols <value>]
[--notification-triggers <value>]
[--notification-enabled | --no-notification-enabled]
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

The name for the alarm. Specify the name of an existing alarm to update, and overwrite the previous configuration of the alarm.

`--metric-name` (string)

The name of the metric to associate with the alarm.

You can configure up to two alarms per metric.

The following metrics are available for each resource type:

- **Instances** : `BurstCapacityPercentage` , `BurstCapacityTime` , `CPUUtilization` , `NetworkIn` , `NetworkOut` , `StatusCheckFailed` , `StatusCheckFailed_Instance` , and `StatusCheckFailed_System` .
- **Load balancers** : `ClientTLSNegotiationErrorCount` , `HealthyHostCount` , `UnhealthyHostCount` , `HTTPCode_LB_4XX_Count` , `HTTPCode_LB_5XX_Count` , `HTTPCode_Instance_2XX_Count` , `HTTPCode_Instance_3XX_Count` , `HTTPCode_Instance_4XX_Count` , `HTTPCode_Instance_5XX_Count` , `InstanceResponseTime` , `RejectedConnectionCount` , and `RequestCount` .
- **Relational databases** : `CPUUtilization` , `DatabaseConnections` , `DiskQueueDepth` , `FreeStorageSpace` , `NetworkReceiveThroughput` , and `NetworkTransmitThroughput` .

For more information about these metrics, see [Metrics available in Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-resource-health-metrics#available-metrics) .

Possible values:

- `CPUUtilization`
- `NetworkIn`
- `NetworkOut`
- `StatusCheckFailed`
- `StatusCheckFailed_Instance`
- `StatusCheckFailed_System`
- `ClientTLSNegotiationErrorCount`
- `HealthyHostCount`
- `UnhealthyHostCount`
- `HTTPCode_LB_4XX_Count`
- `HTTPCode_LB_5XX_Count`
- `HTTPCode_Instance_2XX_Count`
- `HTTPCode_Instance_3XX_Count`
- `HTTPCode_Instance_4XX_Count`
- `HTTPCode_Instance_5XX_Count`
- `InstanceResponseTime`
- `RejectedConnectionCount`
- `RequestCount`
- `DatabaseConnections`
- `DiskQueueDepth`
- `FreeStorageSpace`
- `NetworkReceiveThroughput`
- `NetworkTransmitThroughput`
- `BurstCapacityTime`
- `BurstCapacityPercentage`

`--monitored-resource-name` (string)

The name of the Lightsail resource that will be monitored.

Instances, load balancers, and relational databases are the only Lightsail resources that can currently be monitored by alarms.

`--comparison-operator` (string)

The arithmetic operation to use when comparing the specified statistic to the threshold. The specified statistic value is used as the first operand.

Possible values:

- `GreaterThanOrEqualToThreshold`
- `GreaterThanThreshold`
- `LessThanThreshold`
- `LessThanOrEqualToThreshold`

`--threshold` (double)

The value against which the specified statistic is compared.

`--evaluation-periods` (integer)

The number of most recent periods over which data is compared to the specified threshold. If you are setting an âM out of Nâ alarm, this value (`evaluationPeriods` ) is the N.

If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies the rolling period of time in which data points are evaluated.

Each evaluation period is five minutes long. For example, specify an evaluation period of 24 to evaluate a metric over a rolling period of two hours.

You can specify a minimum valuation period of 1 (5 minutes), and a maximum evaluation period of 288 (24 hours).

`--datapoints-to-alarm` (integer)

The number of data points that must be not within the specified threshold to trigger the alarm. If you are setting an âM out of Nâ alarm, this value (`datapointsToAlarm` ) is the M.

`--treat-missing-data` (string)

Sets how this alarm will handle missing data points.

An alarm can treat missing data in the following ways:

- `breaching` - Assume the missing data is not within the threshold. Missing data counts towards the number of times the metric is not within the threshold.
- `notBreaching` - Assume the missing data is within the threshold. Missing data does not count towards the number of times the metric is not within the threshold.
- `ignore` - Ignore the missing data. Maintains the current alarm state.
- `missing` - Missing data is treated as missing.

If `treatMissingData` is not specified, the default behavior of `missing` is used.

Possible values:

- `breaching`
- `notBreaching`
- `ignore`
- `missing`

`--contact-protocols` (list)

The contact protocols to use for the alarm, such as `Email` , `SMS` (text messaging), or both.

A notification is sent via the specified contact protocol if notifications are enabled for the alarm, and when the alarm is triggered.

A notification is not sent if a contact protocol is not specified, if the specified contact protocol is not configured in the Amazon Web Services Region, or if notifications are not enabled for the alarm using the `notificationEnabled` paramater.

Use the `CreateContactMethod` action to configure a contact protocol in an Amazon Web Services Region.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  Email
  SMS
```

`--notification-triggers` (list)

The alarm states that trigger a notification.

An alarm has the following possible states:

- `ALARM` - The metric is outside of the defined threshold.
- `INSUFFICIENT_DATA` - The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.
- `OK` - The metric is within the defined threshold.

When you specify a notification trigger, the `ALARM` state must be specified. The `INSUFFICIENT_DATA` and `OK` states can be specified in addition to the `ALARM` state.

- If you specify `OK` as an alarm trigger, a notification is sent when the alarm switches from an `ALARM` or `INSUFFICIENT_DATA` alarm state to an `OK` state. This can be thought of as an *all clear* alarm notification.
- If you specify `INSUFFICIENT_DATA` as the alarm trigger, a notification is sent when the alarm switches from an `OK` or `ALARM` alarm state to an `INSUFFICIENT_DATA` state.

The notification trigger defaults to `ALARM` if you donât specify this parameter.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  OK
  ALARM
  INSUFFICIENT_DATA
```

`--notification-enabled` | `--no-notification-enabled` (boolean)

Indicates whether the alarm is enabled.

Notifications are enabled by default if you donât specify this parameter.

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

operations -> (list)

An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(structure)

Describes the API operation.

id -> (string)

The ID of the operation.

resourceName -> (string)

The resource name.

resourceType -> (string)

The resource type.

createdAt -> (timestamp)

The timestamp when the operation was initialized (`1479816991.349` ).

location -> (structure)

The Amazon Web Services Region and Availability Zone.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

isTerminal -> (boolean)

A Boolean value indicating whether the operation is terminal.

operationDetails -> (string)

Details about the operation (`Debian-1GB-Ohio-1` ).

operationType -> (string)

The type of operation.

status -> (string)

The status of the operation.

statusChangedAt -> (timestamp)

The timestamp when the status was changed (`1479816991.349` ).

errorCode -> (string)

The error code.

errorDetails -> (string)

The error details.