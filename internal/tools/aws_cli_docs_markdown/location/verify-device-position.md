# verify-device-positionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/verify-device-position.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/verify-device-position.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [location](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/index.html#cli-aws-location) ]

# verify-device-position

## Description

Verifies the integrity of the deviceâs position by determining if it was reported behind a proxy, and by comparing it to an inferred position estimated based on the deviceâs state.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/location-2020-11-19/VerifyDevicePosition)

## Synopsis

```
verify-device-position
--tracker-name <value>
--device-state <value>
[--distance-unit <value>]
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

The name of the tracker resource to be associated with verification request.

`--device-state` (structure)

The deviceâs state, including position, IP address, cell signals and Wi-Fi access points.

DeviceId -> (string)

The device identifier.

SampleTime -> (timestamp)

The timestamp at which the deviceâs position was determined. Uses [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ` .

Position -> (list)

The last known device position.

(double)

Accuracy -> (structure)

Defines the level of certainty of the position.

Horizontal -> (double)

Estimated maximum distance, in meters, between the measured position and the true position of a device, along the Earthâs surface.

Ipv4Address -> (string)

The deviceâs Ipv4 address.

WiFiAccessPoints -> (list)

The Wi-Fi access points the device is using.

(structure)

Wi-Fi access point.

MacAddress -> (string)

Medium access control address (Mac).

Rss -> (integer)

Received signal strength (dBm) of the WLAN measurement data.

CellSignals -> (structure)

The cellular network infrastructure that the device is connected to.

LteCellDetails -> (list)

Information about the Long-Term Evolution (LTE) network the device is connected to.

(structure)

Details about the Long-Term Evolution (LTE) network.

CellId -> (integer)

The E-UTRAN Cell Identifier (ECI).

Mcc -> (integer)

The Mobile Country Code (MCC).

Mnc -> (integer)

The Mobile Network Code (MNC)

LocalId -> (structure)

The LTE local identification information (local ID).

Earfcn -> (integer)

E-UTRA (Evolved Universal Terrestrial Radio Access) absolute radio frequency channel number (EARFCN).

Pci -> (integer)

Physical Cell ID (PCI).

NetworkMeasurements -> (list)

The network measurements.

(structure)

LTE network measurements.

Earfcn -> (integer)

E-UTRA (Evolved Universal Terrestrial Radio Access) absolute radio frequency channel number (EARFCN).

CellId -> (integer)

E-UTRAN Cell Identifier (ECI).

Pci -> (integer)

Physical Cell ID (PCI).

Rsrp -> (integer)

Signal power of the reference signal received, measured in dBm (decibel-milliwatts).

Rsrq -> (float)

Signal quality of the reference Signal received, measured in decibels (dB).

TimingAdvance -> (integer)

Timing Advance (TA).

NrCapable -> (boolean)

Indicates whether the LTE object is capable of supporting NR (new radio).

Rsrp -> (integer)

Signal power of the reference signal received, measured in decibel-milliwatts (dBm).

Rsrq -> (float)

Signal quality of the reference Signal received, measured in decibels (dB).

Tac -> (integer)

LTE Tracking Area Code (TAC).

JSON Syntax:

```
{
  "DeviceId": "string",
  "SampleTime": timestamp,
  "Position": [double, ...],
  "Accuracy": {
    "Horizontal": double
  },
  "Ipv4Address": "string",
  "WiFiAccessPoints": [
    {
      "MacAddress": "string",
      "Rss": integer
    }
    ...
  ],
  "CellSignals": {
    "LteCellDetails": [
      {
        "CellId": integer,
        "Mcc": integer,
        "Mnc": integer,
        "LocalId": {
          "Earfcn": integer,
          "Pci": integer
        },
        "NetworkMeasurements": [
          {
            "Earfcn": integer,
            "CellId": integer,
            "Pci": integer,
            "Rsrp": integer,
            "Rsrq": float
          }
          ...
        ],
        "TimingAdvance": integer,
        "NrCapable": true|false,
        "Rsrp": integer,
        "Rsrq": float,
        "Tac": integer
      }
      ...
    ]
  }
}
```

`--distance-unit` (string)

The distance unit for the verification request.

Default Value: `Kilometers`

Possible values:

- `Kilometers`
- `Miles`

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

InferredState -> (structure)

The inferred state of the device, given the provided position, IP address, cellular signals, and Wi-Fi- access points.

Position -> (list)

The device position inferred by the provided position, IP address, cellular signals, and Wi-Fi- access points.

(double)

Accuracy -> (structure)

The level of certainty of the inferred position.

Horizontal -> (double)

Estimated maximum distance, in meters, between the measured position and the true position of a device, along the Earthâs surface.

DeviationDistance -> (double)

The distance between the inferred position and the deviceâs self-reported position.

ProxyDetected -> (boolean)

Indicates if a proxy was used.

DeviceId -> (string)

The device identifier.

SampleTime -> (timestamp)

The timestamp at which the deviceâs position was determined. Uses [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ` .

ReceivedTime -> (timestamp)

The timestamp for when the tracker resource received the device position in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ` .

DistanceUnit -> (string)

The distance unit for the verification response.