# create-wireless-deviceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-wireless-device.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-wireless-device.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotwireless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/index.html#cli-aws-iotwireless) ]

# create-wireless-device

## Description

Provisions a wireless device.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotwireless-2020-11-22/CreateWirelessDevice)

## Synopsis

```
create-wireless-device
--type <value>
[--name <value>]
[--description <value>]
--destination-name <value>
[--client-request-token <value>]
[--tags <value>]
[--positioning <value>]
[--sidewalk <value>]
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

`--type` (string)

The wireless device type.

Possible values:

- `Sidewalk`
- `LoRaWAN`

`--name` (string)

The name of the new resource.

`--description` (string)

The description of the new resource.

`--destination-name` (string)

The name of the destination to assign to the new wireless device.

`--client-request-token` (string)

Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see [Ensuring idempotency in Amazon EC2 API requests](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html) .

`--tags` (list)

The tags to attach to the new wireless device. Tags are metadata that you can use to manage a resource.

(structure)

A simple label consisting of a customer-defined key-value pair

Key -> (string)

The tagâs key value.

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

`--positioning` (string)

FPort values for the GNSS, stream, and ClockSync functions of the positioning information.

Possible values:

- `Enabled`
- `Disabled`

`--sidewalk` (structure)

The device configuration information to use to create the Sidewalk device.

DeviceProfileId -> (string)

The ID of the Sidewalk device profile.

Shorthand Syntax:

```
DeviceProfileId=string
```

JSON Syntax:

```
{
  "DeviceProfileId": "string"
}
```

`--lorawan` (structure)

The device configuration information to use to create the wireless device.

DevEui -> (string)

The DevEUI value.

DeviceProfileId -> (string)

The ID of the device profile for the new wireless device.

ServiceProfileId -> (string)

The ID of the service profile.

OtaaV1_1 -> (structure)

OTAA device object for v1.1 for create APIs

AppKey -> (string)

The AppKey value.

NwkKey -> (string)

The NwkKey value.

JoinEui -> (string)

The JoinEUI value.

OtaaV1_0_x -> (structure)

OTAA device object for create APIs for v1.0.x

AppKey -> (string)

The AppKey value.

AppEui -> (string)

The AppEUI value. You specify this value when using LoRaWAN versions v1.0.2 or v1.0.3.

JoinEui -> (string)

The JoinEUI value. You specify this value instead of the AppEUI when using LoRaWAN version v1.0.4.

GenAppKey -> (string)

The GenAppKey value.

AbpV1_1 -> (structure)

ABP device object for create APIs for v1.1

DevAddr -> (string)

The DevAddr value.

SessionKeys -> (structure)

Session keys for ABP v1.1

FNwkSIntKey -> (string)

The FNwkSIntKey value.

SNwkSIntKey -> (string)

The SNwkSIntKey value.

NwkSEncKey -> (string)

The NwkSEncKey value.

AppSKey -> (string)

The AppSKey value.

FCntStart -> (integer)

The FCnt init value.

AbpV1_0_x -> (structure)

LoRaWAN object for create APIs

DevAddr -> (string)

The DevAddr value.

SessionKeys -> (structure)

Session keys for ABP v1.0.x

NwkSKey -> (string)

The NwkSKey value.

AppSKey -> (string)

The AppSKey value.

FCntStart -> (integer)

The FCnt init value.

FPorts -> (structure)

List of FPort assigned for different LoRaWAN application packages to use

Fuota -> (integer)

The Fport value.

Multicast -> (integer)

The Fport value.

ClockSync -> (integer)

The Fport value.

Positioning -> (structure)

FPort values for the GNSS, stream, and ClockSync functions of the positioning information.

ClockSync -> (integer)

The Fport value.

Stream -> (integer)

The Fport value.

Gnss -> (integer)

The Fport value.

Applications -> (list)

Optional LoRaWAN application information, which can be used for geolocation.

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
  "DevEui": "string",
  "DeviceProfileId": "string",
  "ServiceProfileId": "string",
  "OtaaV1_1": {
    "AppKey": "string",
    "NwkKey": "string",
    "JoinEui": "string"
  },
  "OtaaV1_0_x": {
    "AppKey": "string",
    "AppEui": "string",
    "JoinEui": "string",
    "GenAppKey": "string"
  },
  "AbpV1_1": {
    "DevAddr": "string",
    "SessionKeys": {
      "FNwkSIntKey": "string",
      "SNwkSIntKey": "string",
      "NwkSEncKey": "string",
      "AppSKey": "string"
    },
    "FCntStart": integer
  },
  "AbpV1_0_x": {
    "DevAddr": "string",
    "SessionKeys": {
      "NwkSKey": "string",
      "AppSKey": "string"
    },
    "FCntStart": integer
  },
  "FPorts": {
    "Fuota": integer,
    "Multicast": integer,
    "ClockSync": integer,
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

**To create an IoT wireless device**

The following `create-wireless-device` example creates a wireless device resource of the type LoRaWAN.

```
aws iotwireless create-wireless-device \
    --cli-input-json file://input.json
```

Contents of `input.json`:

```
{
    "Description": "My LoRaWAN wireless device"
    "DestinationName": "IoTWirelessDestination"
    "LoRaWAN": {
        "DeviceProfileId": "ab0c23d3-b001-45ef-6a01-2bc3de4f5333",
        "ServiceProfileId": "fe98dc76-cd12-001e-2d34-5550432da100",
        "OtaaV1_1": {
            "AppKey": "3f4ca100e2fc675ea123f4eb12c4a012",
            "JoinEui": "b4c231a359bc2e3d",
            "NwkKey": "01c3f004a2d6efffe32c4eda14bcd2b4"
        },
        "DevEui": "ac12efc654d23fc2"
    },
    "Name": "SampleIoTWirelessThing"
    "Type": LoRaWAN
}
```

Output:

```
{
    "Arn": "arn:aws:iotwireless:us-east-1:123456789012:WirelessDevice/1ffd32c8-8130-4194-96df-622f072a315f",
    "Id": "1ffd32c8-8130-4194-96df-622f072a315f"
}
```

For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html) in the *AWS IoT Developers Guide*.

## Output

Arn -> (string)

The Amazon Resource Name of the new resource.

Id -> (string)

The ID of the new wireless device.