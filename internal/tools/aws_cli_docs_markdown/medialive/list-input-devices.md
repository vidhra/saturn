# list-input-devicesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-input-devices.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-input-devices.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [medialive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/index.html#cli-aws-medialive) ]

# list-input-devices

## Description

List input devices

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/ListInputDevices)

`list-input-devices` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `InputDevices`

## Synopsis

```
list-input-devices
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

InputDevices -> (list)

The list of input devices.

(structure)

Details of the input device.

Arn -> (string)

The unique ARN of the input device.

ConnectionState -> (string)

The state of the connection between the input device and AWS.

DeviceSettingsSyncState -> (string)

The status of the action to synchronize the device configuration. If you change the configuration of the input device (for example, the maximum bitrate), MediaLive sends the new data to the device. The device might not update itself immediately. SYNCED means the device has updated its configuration. SYNCING means that it has not updated its configuration.

DeviceUpdateStatus -> (string)

The status of software on the input device.

HdDeviceSettings -> (structure)

Settings that describe an input device that is type HD.

ActiveInput -> (string)

If you specified Auto as the configured input, specifies which of the sources is currently active (SDI or HDMI).

ConfiguredInput -> (string)

The source at the input device that is currently active. You can specify this source.

DeviceState -> (string)

The state of the input device.

Framerate -> (double)

The frame rate of the video source.

Height -> (integer)

The height of the video source, in pixels.

MaxBitrate -> (integer)

The current maximum bitrate for ingesting this source, in bits per second. You can specify this maximum.

ScanType -> (string)

The scan type of the video source.

Width -> (integer)

The width of the video source, in pixels.

LatencyMs -> (integer)

The Link deviceâs buffer size (latency) in milliseconds (ms). You can specify this value.

Id -> (string)

The unique ID of the input device.

MacAddress -> (string)

The network MAC address of the input device.

Name -> (string)

A name that you specify for the input device.

NetworkSettings -> (structure)

Network settings for the input device.

DnsAddresses -> (list)

The DNS addresses of the input device.

(string)

Placeholder documentation for __string

Gateway -> (string)

The network gateway IP address.

IpAddress -> (string)

The IP address of the input device.

IpScheme -> (string)

Specifies whether the input device has been configured (outside of MediaLive) to use a dynamic IP address assignment (DHCP) or a static IP address.

SubnetMask -> (string)

The subnet mask of the input device.

SerialNumber -> (string)

The unique serial number of the input device.

Type -> (string)

The type of the input device.

UhdDeviceSettings -> (structure)

Settings that describe an input device that is type UHD.

ActiveInput -> (string)

If you specified Auto as the configured input, specifies which of the sources is currently active (SDI or HDMI).

ConfiguredInput -> (string)

The source at the input device that is currently active. You can specify this source.

DeviceState -> (string)

The state of the input device.

Framerate -> (double)

The frame rate of the video source.

Height -> (integer)

The height of the video source, in pixels.

MaxBitrate -> (integer)

The current maximum bitrate for ingesting this source, in bits per second. You can specify this maximum.

ScanType -> (string)

The scan type of the video source.

Width -> (integer)

The width of the video source, in pixels.

LatencyMs -> (integer)

The Link deviceâs buffer size (latency) in milliseconds (ms). You can specify this value.

Codec -> (string)

The codec for the video that the device produces.

MediaconnectSettings -> (structure)

Information about the MediaConnect flow attached to the device. Returned only if the outputType is MEDIACONNECT_FLOW.

FlowArn -> (string)

The ARN of the MediaConnect flow.

RoleArn -> (string)

The ARN for the role that MediaLive assumes to access the attached flow and secret.

SecretArn -> (string)

The ARN of the secret used to encrypt the stream.

SourceName -> (string)

The name of the MediaConnect flow source.

AudioChannelPairs -> (list)

An array of eight audio configurations, one for each audio pair in the source. Each audio configuration specifies either to exclude the pair, or to format it and include it in the output from the UHD device. Applies only when the device is configured as the source for a MediaConnect flow.

(structure)

One audio configuration that specifies the format for one audio pair that the device produces as output.

Id -> (integer)

The ID for one audio pair configuration, a value from 1 to 8.

Profile -> (string)

The profile for one audio pair configuration. This property describes one audio configuration in the format (rate control algorithm)-(codec)_(quality)-(bitrate in bytes). For example, CBR-AAC_HQ-192000. Or DISABLED, in which case the device wonât produce audio for this pair.

InputResolution -> (string)

The resolution of the Link deviceâs source (HD or UHD). This value determines MediaLive resource allocation and billing for this input.

Tags -> (map)

A collection of key-value pairs.

key -> (string)

Placeholder documentation for __string

value -> (string)

Placeholder documentation for __string

AvailabilityZone -> (string)

The Availability Zone associated with this input device.

MedialiveInputArns -> (list)

An array of the ARNs for the MediaLive inputs attached to the device. Returned only if the outputType is MEDIALIVE_INPUT.

(string)

Placeholder documentation for __string

OutputType -> (string)

The output attachment type of the input device. Specifies MEDIACONNECT_FLOW if this device is the source for a MediaConnect flow. Specifies MEDIALIVE_INPUT if this device is the source for a MediaLive input.

NextToken -> (string)

A token to get additional list results.