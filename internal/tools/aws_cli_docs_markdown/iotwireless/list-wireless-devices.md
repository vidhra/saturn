# list-wireless-devicesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-wireless-devices.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-wireless-devices.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotwireless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/index.html#cli-aws-iotwireless) ]

# list-wireless-devices

## Description

Lists the wireless devices registered to your AWS account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotwireless-2020-11-22/ListWirelessDevices)

## Synopsis

```
list-wireless-devices
[--max-results <value>]
[--next-token <value>]
[--destination-name <value>]
[--device-profile-id <value>]
[--service-profile-id <value>]
[--wireless-device-type <value>]
[--fuota-task-id <value>]
[--multicast-group-id <value>]
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

`--max-results` (integer)

The maximum number of results to return in this operation.

`--next-token` (string)

To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.

`--destination-name` (string)

A filter to list only the wireless devices that use this destination.

`--device-profile-id` (string)

A filter to list only the wireless devices that use this device profile.

`--service-profile-id` (string)

A filter to list only the wireless devices that use this service profile.

`--wireless-device-type` (string)

A filter to list only the wireless devices that use this wireless device type.

Possible values:

- `Sidewalk`
- `LoRaWAN`

`--fuota-task-id` (string)

The ID of a FUOTA task.

`--multicast-group-id` (string)

The ID of the multicast group.

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

**To list the available wireless devices**

The following `list-wireless-devices` example lists the available wireless devices registered to your AWS account.

```
aws iotwireless list-wireless-devices
```

Output:

```
{
    "WirelessDeviceList": [
        {
            "Name": "myLoRaWANDevice",
            "DestinationName": "IoTWirelessDestination",
            "Id": "1ffd32c8-8130-4194-96df-622f072a315f",
            "Type": "LoRaWAN",
            "LoRaWAN": {
                "DevEui": "ac12efc654d23fc2"
            },
            "Arn": "arn:aws:iotwireless:us-east-1:123456789012:WirelessDevice/1ffd32c8-8130-4194-96df-622f072a315f"
        }
    ]
}
```

For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html) in the *AWS IoT Developers Guide*.

## Output

NextToken -> (string)

The token to use to get the next set of results, or **null** if there are no additional results.

WirelessDeviceList -> (list)

The ID of the wireless device.

(structure)

Information about a wireless deviceâs operation.

Arn -> (string)

The Amazon Resource Name of the resource.

Id -> (string)

The ID of the wireless device reporting the data.

Type -> (string)

The wireless device type.

Name -> (string)

The name of the resource.

DestinationName -> (string)

The name of the destination to which the device is assigned.

LastUplinkReceivedAt -> (string)

The date and time when the most recent uplink was received.

### Note

Theis value is only valid for 3 months.

LoRaWAN -> (structure)

LoRaWAN device info.

DevEui -> (string)

The DevEUI value.

Sidewalk -> (structure)

The Sidewalk account credentials.

AmazonId -> (string)

The Sidewalk Amazon ID.

SidewalkId -> (string)

The sidewalk device identification.

SidewalkManufacturingSn -> (string)

The Sidewalk manufacturing series number.

DeviceCertificates -> (list)

The sidewalk device certificates for Ed25519 and P256r1.

(structure)

List of sidewalk certificates.

SigningAlg -> (string)

The certificate chain algorithm provided by sidewalk.

Value -> (string)

The value of the chosen sidewalk certificate.

DeviceProfileId -> (string)

Sidewalk object used by list functions.

Status -> (string)

The status of the Sidewalk devices, such as provisioned or registered.

FuotaDeviceStatus -> (string)

The status of a wireless device in a FUOTA task.

MulticastDeviceStatus -> (string)

The status of the wireless device in the multicast group.

McGroupId -> (integer)

Id of the multicast group.