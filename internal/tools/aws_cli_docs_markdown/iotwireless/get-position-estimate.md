# get-position-estimateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-position-estimate.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-position-estimate.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotwireless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/index.html#cli-aws-iotwireless) ]

# get-position-estimate

## Description

Get estimated position information as a payload in GeoJSON format. The payload measurement data is resolved using solvers that are provided by third-party vendors.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotwireless-2020-11-22/GetPositionEstimate)

## Synopsis

```
get-position-estimate
[--wi-fi-access-points <value>]
[--cell-towers <value>]
[--ip <value>]
[--gnss <value>]
[--timestamp <value>]
<outfile>
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

`--wi-fi-access-points` (list)

Retrieves an estimated device position by resolving WLAN measurement data. The position is resolved using HEREâs Wi-Fi based solver.

(structure)

Wi-Fi access point.

MacAddress -> (string)

Wi-Fi MAC Address.

Rss -> (integer)

Received signal strength (dBm) of the WLAN measurement data.

Shorthand Syntax:

```
MacAddress=string,Rss=integer ...
```

JSON Syntax:

```
[
  {
    "MacAddress": "string",
    "Rss": integer
  }
  ...
]
```

`--cell-towers` (structure)

Retrieves an estimated device position by resolving measurement data from cellular radio towers. The position is resolved using HEREâs cellular-based solver.

Gsm -> (list)

GSM object information.

(structure)

GSM object.

Mcc -> (integer)

Mobile Country Code.

Mnc -> (integer)

Mobile Network Code.

Lac -> (integer)

Location area code.

GeranCid -> (integer)

GERAN (GSM EDGE Radio Access Network) Cell Global Identifier.

GsmLocalId -> (structure)

GSM local identification (local ID) information.

Bsic -> (integer)

GSM base station identity code (BSIC).

Bcch -> (integer)

GSM broadcast control channel.

GsmTimingAdvance -> (integer)

Timing advance value, which corresponds to the length of time a signal takes to reach the base station from a mobile phone.

RxLevel -> (integer)

Rx level, which is the received signal power, measured in dBm (decibel-milliwatts).

GsmNmr -> (list)

GSM object for network measurement reports.

(structure)

GSM object for network measurement reports.

Bsic -> (integer)

GSM base station identity code (BSIC).

Bcch -> (integer)

GSM broadcast control channel.

RxLevel -> (integer)

Rx level, which is the received signal power, measured in dBm (decibel-milliwatts).

GlobalIdentity -> (structure)

Global identity information of the GSM object.

Lac -> (integer)

Location area code of the global identity.

GeranCid -> (integer)

GERAN (GSM EDGE Radio Access Network) cell global identifier.

Wcdma -> (list)

WCDMA object information.

(structure)

WCDMA.

Mcc -> (integer)

Mobile Country Code.

Mnc -> (integer)

Mobile Network Code.

Lac -> (integer)

Location Area Code.

UtranCid -> (integer)

UTRAN (UMTS Terrestrial Radio Access Network) Cell Global Identifier.

WcdmaLocalId -> (structure)

WCDMA local ID information.

Uarfcndl -> (integer)

WCDMA UTRA Absolute RF Channel Number downlink.

Psc -> (integer)

Primary Scrambling Code.

Rscp -> (integer)

Received Signal Code Power (signal power) (dBm).

PathLoss -> (integer)

Path loss, or path attenuation, is the reduction in power density of an electromagnetic wave as it propagates through space.

WcdmaNmr -> (list)

WCDMA object for network measurement reports.

(structure)

Network Measurement Reports.

Uarfcndl -> (integer)

WCDMA UTRA Absolute RF Channel Number downlink.

Psc -> (integer)

Primary Scrambling Code.

UtranCid -> (integer)

UTRAN (UMTS Terrestrial Radio Access Network) Cell Global Identifier.

Rscp -> (integer)

Received Signal Code Power (signal power) (dBm)

PathLoss -> (integer)

Path loss, or path attenuation, is the reduction in power density of an electromagnetic wave as it propagates through space.

Tdscdma -> (list)

TD-SCDMA object information.

(structure)

TD-SCDMA object.

Mcc -> (integer)

Mobile Country Code.

Mnc -> (integer)

Mobile Network Code.

Lac -> (integer)

Location Area Code.

UtranCid -> (integer)

UTRAN (UMTS Terrestrial Radio Access Network) Cell Global Identifier.

TdscdmaLocalId -> (structure)

TD-SCDMA local identification (local ID) information.

Uarfcn -> (integer)

TD-SCDMA UTRA (Universal Terrestrial Radio Access Network) absolute RF channel number (UARFCN).

CellParams -> (integer)

Cell parameters for TD-SCDMA.

TdscdmaTimingAdvance -> (integer)

TD-SCDMA Timing advance.

Rscp -> (integer)

Signal power of the received signal (Received Signal Code Power), measured in decibel-milliwatts (dBm).

PathLoss -> (integer)

Path loss, or path attenuation, is the reduction in power density of an electromagnetic wave as it propagates through space.

TdscdmaNmr -> (list)

TD-SCDMA object for network measurement reports.

(structure)

TD-SCDMA object for network measurement reports.

Uarfcn -> (integer)

TD-SCDMA UTRA (Universal Terrestrial Radio Access Network) absolute RF channel number.

CellParams -> (integer)

Cell parameters for TD-SCDMA network measurement reports object.

UtranCid -> (integer)

UTRAN (UMTS Terrestrial Radio Access Network) cell global identifier.

Rscp -> (integer)

Code power of the received signal, measured in decibel-milliwatts (dBm).

PathLoss -> (integer)

Path loss, or path attenuation, is the reduction in power density of an electromagnetic wave as it propagates through space.

Lte -> (list)

LTE object information.

(structure)

LTE object.

Mcc -> (integer)

Mobile Country Code.

Mnc -> (integer)

Mobile Network Code.

EutranCid -> (integer)

E-UTRAN (Evolved Universal Terrestrial Radio Access Network) Cell Global Identifier.

Tac -> (integer)

LTE tracking area code.

LteLocalId -> (structure)

LTE local identification (local ID) information.

Pci -> (integer)

Physical cell ID.

Earfcn -> (integer)

Evolved universal terrestrial radio access (E-UTRA) absolute radio frequency channel number (FCN).

LteTimingAdvance -> (integer)

LTE timing advance.

Rsrp -> (integer)

Signal power of the reference signal received, measured in dBm (decibel-milliwatts).

Rsrq -> (float)

Signal quality of the reference Signal received, measured in decibels (dB).

NrCapable -> (boolean)

Parameter that determines whether the LTE object is capable of supporting NR (new radio).

LteNmr -> (list)

LTE object for network measurement reports.

(structure)

LTE object for network measurement reports.

Pci -> (integer)

Physical cell ID.

Earfcn -> (integer)

E-UTRA (Evolved universal terrestrial Radio Access) absolute radio frequency channel Number (EARFCN).

EutranCid -> (integer)

E-UTRAN (Evolved Universal Terrestrial Radio Access Network) cell global identifier (EUTRANCID).

Rsrp -> (integer)

Signal power of the reference signal received, measured in dBm (decibel-milliwatts).

Rsrq -> (float)

Signal quality of the reference Signal received, measured in decibels (dB).

Cdma -> (list)

CDMA object information.

(structure)

CDMA (Code-division multiple access) object.

SystemId -> (integer)

CDMA system ID (SID).

NetworkId -> (integer)

CDMA network ID (NID).

BaseStationId -> (integer)

CDMA base station ID (BSID).

RegistrationZone -> (integer)

CDMA registration zone (RZ).

CdmaLocalId -> (structure)

CDMA local identification (local ID) parameters.

PnOffset -> (integer)

Pseudo-noise offset, which is a characteristic of the signal from a cell on a radio tower.

CdmaChannel -> (integer)

CDMA channel information.

PilotPower -> (integer)

Transmit power level of the pilot signal, measured in dBm (decibel-milliwatts).

BaseLat -> (float)

CDMA base station latitude in degrees.

BaseLng -> (float)

CDMA base station longitude in degrees.

CdmaNmr -> (list)

CDMA network measurement reports.

(structure)

CDMA object for network measurement reports.

PnOffset -> (integer)

Pseudo-noise offset, which is a characteristic of the signal from a cell on a radio tower.

CdmaChannel -> (integer)

CDMA channel information.

PilotPower -> (integer)

Transmit power level of the pilot signal, measured in dBm (decibel-milliwatts).

BaseStationId -> (integer)

CDMA base station ID (BSID).

JSON Syntax:

```
{
  "Gsm": [
    {
      "Mcc": integer,
      "Mnc": integer,
      "Lac": integer,
      "GeranCid": integer,
      "GsmLocalId": {
        "Bsic": integer,
        "Bcch": integer
      },
      "GsmTimingAdvance": integer,
      "RxLevel": integer,
      "GsmNmr": [
        {
          "Bsic": integer,
          "Bcch": integer,
          "RxLevel": integer,
          "GlobalIdentity": {
            "Lac": integer,
            "GeranCid": integer
          }
        }
        ...
      ]
    }
    ...
  ],
  "Wcdma": [
    {
      "Mcc": integer,
      "Mnc": integer,
      "Lac": integer,
      "UtranCid": integer,
      "WcdmaLocalId": {
        "Uarfcndl": integer,
        "Psc": integer
      },
      "Rscp": integer,
      "PathLoss": integer,
      "WcdmaNmr": [
        {
          "Uarfcndl": integer,
          "Psc": integer,
          "UtranCid": integer,
          "Rscp": integer,
          "PathLoss": integer
        }
        ...
      ]
    }
    ...
  ],
  "Tdscdma": [
    {
      "Mcc": integer,
      "Mnc": integer,
      "Lac": integer,
      "UtranCid": integer,
      "TdscdmaLocalId": {
        "Uarfcn": integer,
        "CellParams": integer
      },
      "TdscdmaTimingAdvance": integer,
      "Rscp": integer,
      "PathLoss": integer,
      "TdscdmaNmr": [
        {
          "Uarfcn": integer,
          "CellParams": integer,
          "UtranCid": integer,
          "Rscp": integer,
          "PathLoss": integer
        }
        ...
      ]
    }
    ...
  ],
  "Lte": [
    {
      "Mcc": integer,
      "Mnc": integer,
      "EutranCid": integer,
      "Tac": integer,
      "LteLocalId": {
        "Pci": integer,
        "Earfcn": integer
      },
      "LteTimingAdvance": integer,
      "Rsrp": integer,
      "Rsrq": float,
      "NrCapable": true|false,
      "LteNmr": [
        {
          "Pci": integer,
          "Earfcn": integer,
          "EutranCid": integer,
          "Rsrp": integer,
          "Rsrq": float
        }
        ...
      ]
    }
    ...
  ],
  "Cdma": [
    {
      "SystemId": integer,
      "NetworkId": integer,
      "BaseStationId": integer,
      "RegistrationZone": integer,
      "CdmaLocalId": {
        "PnOffset": integer,
        "CdmaChannel": integer
      },
      "PilotPower": integer,
      "BaseLat": float,
      "BaseLng": float,
      "CdmaNmr": [
        {
          "PnOffset": integer,
          "CdmaChannel": integer,
          "PilotPower": integer,
          "BaseStationId": integer
        }
        ...
      ]
    }
    ...
  ]
}
```

`--ip` (structure)

Retrieves an estimated device position by resolving the IP address information from the device. The position is resolved using MaxMindâs IP-based solver.

IpAddress -> (string)

IP address information.

Shorthand Syntax:

```
IpAddress=string
```

JSON Syntax:

```
{
  "IpAddress": "string"
}
```

`--gnss` (structure)

Retrieves an estimated device position by resolving the global navigation satellite system (GNSS) scan data. The position is resolved using the GNSS solver powered by LoRa Cloud.

Payload -> (string)

Payload that contains the GNSS scan result, or NAV message, in hexadecimal notation.

CaptureTime -> (float)

Optional parameter that gives an estimate of the time when the GNSS scan information is taken, in seconds GPS time (GPST). If capture time is not specified, the local server time is used.

CaptureTimeAccuracy -> (float)

Optional value that gives the capture time estimate accuracy, in seconds. If capture time accuracy is not specified, default value of 300 is used.

AssistPosition -> (list)

Optional assistance position information, specified using latitude and longitude values in degrees. The coordinates are inside the WGS84 reference frame.

(float)

AssistAltitude -> (float)

Optional assistance altitude, which is the altitude of the device at capture time, specified in meters above the WGS84 reference ellipsoid.

Use2DSolver -> (boolean)

Optional parameter that forces 2D solve, which modifies the positioning algorithm to a 2D solution problem. When this parameter is specified, the assistance altitude should have an accuracy of at least 10 meters.

Shorthand Syntax:

```
Payload=string,CaptureTime=float,CaptureTimeAccuracy=float,AssistPosition=float,float,AssistAltitude=float,Use2DSolver=boolean
```

JSON Syntax:

```
{
  "Payload": "string",
  "CaptureTime": float,
  "CaptureTimeAccuracy": float,
  "AssistPosition": [float, ...],
  "AssistAltitude": float,
  "Use2DSolver": true|false
}
```

`--timestamp` (timestamp)

Optional information that specifies the time when the position information will be resolved. It uses the Unix timestamp format. If not specified, the time at which the request was received will be used.

`outfile` (string)
Filename where the content will be saved

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

GeoJsonPayload -> (blob)

The position information of the resource, displayed as a JSON payload. The payload is of type blob and uses the [GeoJSON](https://geojson.org/) format, which a format thatâs used to encode geographic data structures. A sample payload contains the timestamp information, the WGS84 coordinates of the location, and the accuracy and confidence level. For more information and examples, see [Resolve device location (console)](https://docs.aws.amazon.com/iot/latest/developerguide/location-resolve-console.html) .