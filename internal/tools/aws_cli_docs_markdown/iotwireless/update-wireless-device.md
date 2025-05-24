# update-wireless-deviceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-wireless-device.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-wireless-device.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotwireless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/index.html#cli-aws-iotwireless) ]

# update-wireless-device

## Description

Updates properties of a wireless device.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotwireless-2020-11-22/UpdateWirelessDevice)

## Synopsis

```
update-wireless-device
--id <value>
[--destination-name <value>]
[--name <value>]
[--description <value>]
[--positioning <value>]
[--lorawan <value>]
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

`--id` (string)

The ID of the resource to update.

`--destination-name` (string)

The name of the new destination for the device.

`--name` (string)

The new name of the resource.

`--description` (string)

A new description of the resource.

`--positioning` (string)

FPort values for the GNSS, stream, and ClockSync functions of the positioning information.

Possible values:

- `Enabled`
- `Disabled`

`--lorawan` (structure)

The updated wireless deviceâs configuration.

DeviceProfileId -> (string)

The ID of the device profile for the wireless device.

ServiceProfileId -> (string)

The ID of the service profile.

AbpV1_1 -> (structure)

ABP device object for update APIs for v1.1

FCntStart -> (integer)

The FCnt init value.

AbpV1_0_x -> (structure)

ABP device object for update APIs for v1.0.x

FCntStart -> (integer)

The FCnt init value.

FPorts -> (structure)

FPorts object for the positioning information of the device.

Positioning -> (structure)

Positioning FPorts for the ClockSync, Stream, and GNSS functions.

ClockSync -> (integer)

The Fport value.

Stream -> (integer)

The Fport value.

Gnss -> (integer)

The Fport value.

Applications -> (list)

LoRaWAN application, which can be used for geolocation by activating positioning.

(structure)

LoRaWAN application configuration, which can be used to perform geolocation.

FPort -> (integer)

The Fport value.

Type -> (string)

Application type, which can be specified to obtain real-time position information of your LoRaWAN device.

DestinationName -> (string)

The name of the position data destination that describes the AWS IoT rule that processes the deviceâs position data for use by AWS IoT Core for LoRaWAN.

JSON Syntax:

```
{
  "DeviceProfileId": "string",
  "ServiceProfileId": "string",
  "AbpV1_1": {
    "FCntStart": integer
  },
  "AbpV1_0_x": {
    "FCntStart": integer
  },
  "FPorts": {
    "Positioning": {
      "ClockSync": integer,
      "Stream": integer,
      "Gnss": integer
    },
    "Applications": [
      {
        "FPort": integer,
        "Type": "SemtechGeolocation",
        "DestinationName": "string"
      }
      ...
    ]
  }
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

**To update the properties of a wireless device**

The following `update-wireless-device` example updates the properties of a wireless device registered to your AWS account.

```
aws iotwireless update-wireless-device \
    --id "1ffd32c8-8130-4194-96df-622f072a315f" \
    --destination-name IoTWirelessDestination2 \
    --description "Using my first LoRaWAN device"
```

This command produces no output.

For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html) in the *AWS IoT Developers Guide*.

## Output

None