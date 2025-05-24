# get-log-levels-by-resource-typesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-log-levels-by-resource-types.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-log-levels-by-resource-types.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotwireless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/index.html#cli-aws-iotwireless) ]

# get-log-levels-by-resource-types

## Description

Returns current default log levels or log levels by resource types. Based on the resource type, log levels can be returned for wireless device, wireless gateway, or FUOTA task log options.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotwireless-2020-11-22/GetLogLevelsByResourceTypes)

## Synopsis

```
get-log-levels-by-resource-types
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

DefaultLogLevel -> (string)

The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.

WirelessGatewayLogOptions -> (list)

The list of wireless gateway log options.

(structure)

The log options for wireless gateways and can be used to set log levels for a specific type of wireless gateway.

Type -> (string)

The wireless gateway type.

LogLevel -> (string)

The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.

Events -> (list)

The list of wireless gateway event log options.

(structure)

The log options for a wireless gateway event and can be used to set log levels for a specific wireless gateway event.

For a LoRaWAN gateway, possible events for a log message are `CUPS_Request` and `Certificate` .

Event -> (string)

The event for a log message, if the log message is tied to a wireless gateway.

LogLevel -> (string)

The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.

WirelessDeviceLogOptions -> (list)

The list of wireless device log options.

(structure)

The log options for wireless devices and can be used to set log levels for a specific type of wireless device.

Type -> (string)

The wireless device type.

LogLevel -> (string)

The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.

Events -> (list)

The list of wireless device event log options.

(structure)

The log options for a wireless device event and can be used to set log levels for a specific wireless device event.

For a LoRaWAN device, possible events for a log messsage are: `Join` , `Rejoin` , `Downlink_Data` , and `Uplink_Data` . For a Sidewalk device, possible events for a log message are `Registration` , `Downlink_Data` , and `Uplink_Data` .

Event -> (string)

The event for a log message, if the log message is tied to a wireless device.

LogLevel -> (string)

The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.

FuotaTaskLogOptions -> (list)

The list of FUOTA task log options.

(structure)

The log options for FUOTA tasks and can be used to set log levels for a specific type of FUOTA task.

Type -> (string)

The FUOTA task type.

LogLevel -> (string)

The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.

Events -> (list)

The list of FUOTA task event log options.

(structure)

The log options for a FUOTA task event and can be used to set log levels for a specific FUOTA task event.

For a LoRaWAN FUOTA task, the only possible event for a log message is `Fuota` .

Event -> (string)

The event for a log message, if the log message is tied to a FUOTA task.

LogLevel -> (string)

The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs.