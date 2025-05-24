# get-device-profileÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-device-profile.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-device-profile.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotwireless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/index.html#cli-aws-iotwireless) ]

# get-device-profile

## Description

Gets information about a device profile.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotwireless-2020-11-22/GetDeviceProfile)

## Synopsis

```
get-device-profile
--id <value>
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

The ID of the resource to get.

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

**To get information about a device profile**

The following `get-device-profile` example gets information about the device profile with the specified ID that you created.

```
aws iotwireless get-device-profile \
    --id "12345678-a1b2-3c45-67d8-e90fa1b2c34d"
```

Output:

```
{
    "Arn": "arn:aws:iotwireless:us-east-1:123456789012:DeviceProfile/12345678-a1b2-3c45-67d8-e90fa1b2c34d",
    "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d",
    "LoRaWAN": {
    "MacVersion": "1.0.3",
    "MaxDutyCycle": 10,
    "Supports32BitFCnt": false,
    "RegParamsRevision": "RP002-1.0.1",
    "SupportsJoin": true,
    "RfRegion": "US915",
    "MaxEirp": 13,
    "SupportsClassB": false,
    "SupportsClassC": false
    }
}
```

For more information, see [Add profiles to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-define-profiles.html) in the *AWS IoT Developers Guide*.

## Output

Arn -> (string)

The Amazon Resource Name of the resource.

Name -> (string)

The name of the resource.

Id -> (string)

The ID of the device profile.

LoRaWAN -> (structure)

Information about the device profile.

SupportsClassB -> (boolean)

The SupportsClassB value.

ClassBTimeout -> (integer)

The ClassBTimeout value.

PingSlotPeriod -> (integer)

The PingSlotPeriod value.

PingSlotDr -> (integer)

The PingSlotDR value.

PingSlotFreq -> (integer)

The PingSlotFreq value.

SupportsClassC -> (boolean)

The SupportsClassC value.

ClassCTimeout -> (integer)

The ClassCTimeout value.

MacVersion -> (string)

The MAC version (such as OTAA 1.1 or OTAA 1.0.3) to use with this device profile.

RegParamsRevision -> (string)

The version of regional parameters.

RxDelay1 -> (integer)

The RXDelay1 value.

RxDrOffset1 -> (integer)

The RXDROffset1 value.

RxDataRate2 -> (integer)

The RXDataRate2 value.

RxFreq2 -> (integer)

The RXFreq2 value.

FactoryPresetFreqsList -> (list)

The list of values that make up the FactoryPresetFreqs value.

(integer)

MaxEirp -> (integer)

The MaxEIRP value.

MaxDutyCycle -> (integer)

The MaxDutyCycle value. It ranges from 0 to 15.

RfRegion -> (string)

The frequency band (RFRegion) value.

SupportsJoin -> (boolean)

The SupportsJoin value.

Supports32BitFCnt -> (boolean)

The Supports32BitFCnt value.

Sidewalk -> (structure)

Information about the Sidewalk parameters in the device profile.

ApplicationServerPublicKey -> (string)

The Sidewalk application server public key.

QualificationStatus -> (boolean)

Gets information about the certification status of a Sidewalk device profile.

DakCertificateMetadata -> (list)

The DAK certificate information of the Sidewalk device profile.

(structure)

The device attestation key (DAK) information.

CertificateId -> (string)

The certificate ID for the DAK.

MaxAllowedSignature -> (integer)

The maximum number of signatures that the DAK can sign. A value of `-1` indicates that thereâs no device limit.

FactorySupport -> (boolean)

Whether factory support has been enabled.

ApId -> (string)

The advertised product ID (APID) thatâs used for pre-production and production applications.

DeviceTypeId -> (string)

The device type ID thatâs used for prototyping applications.