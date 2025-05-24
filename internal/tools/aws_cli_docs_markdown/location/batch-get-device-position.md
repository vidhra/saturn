# batch-get-device-positionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/batch-get-device-position.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/batch-get-device-position.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [location](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/index.html#cli-aws-location) ]

# batch-get-device-position

## Description

Lists the latest device positions for requested devices.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/location-2020-11-19/BatchGetDevicePosition)

## Synopsis

```
batch-get-device-position
--tracker-name <value>
--device-ids <value>
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

`--tracker-name` (string)

The tracker resource retrieving the device position.

`--device-ids` (list)

Devices whose position you want to retrieve.

- For example, for two devices: `device-ids=DeviceId1&device-ids=DeviceId2`

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

Errors -> (list)

Contains error details for each device that failed to send its position to the tracker resource.

(structure)

Contains error details for each device that didnât return a position.

DeviceId -> (string)

The ID of the device that didnât return a position.

Error -> (structure)

Contains details related to the error code.

Code -> (string)

The error code associated with the batch request error.

Message -> (string)

A message with the reason for the batch request error.

DevicePositions -> (list)

Contains device position details such as the device ID, position, and timestamps for when the position was received and sampled.

(structure)

Contains the device position details.

DeviceId -> (string)

The device whose position you retrieved.

SampleTime -> (timestamp)

The timestamp at which the deviceâs position was determined. Uses [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ` .

ReceivedTime -> (timestamp)

The timestamp for when the tracker resource received the device position in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ` .

Position -> (list)

The last known device position.

(double)

Accuracy -> (structure)

The accuracy of the device position.

Horizontal -> (double)

Estimated maximum distance, in meters, between the measured position and the true position of a device, along the Earthâs surface.

PositionProperties -> (map)

The properties associated with the position.

key -> (string)

value -> (string)