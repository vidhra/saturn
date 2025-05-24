# get-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/get-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/get-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [groundstation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/index.html#cli-aws-groundstation) ]

# get-config

## Description

Returns `Config` information.

Only one `Config` response can be returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/GetConfig)

## Synopsis

```
get-config
--config-id <value>
--config-type <value>
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

`--config-id` (string)

UUID of a `Config` .

`--config-type` (string)

Type of a `Config` .

Possible values:

- `antenna-downlink`
- `antenna-downlink-demod-decode`
- `tracking`
- `dataflow-endpoint`
- `antenna-uplink`
- `uplink-echo`
- `s3-recording`

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

configArn -> (string)

ARN of a `Config`

configData -> (tagged union structure)

Data elements in a `Config` .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `antennaDownlinkConfig`, `antennaDownlinkDemodDecodeConfig`, `antennaUplinkConfig`, `dataflowEndpointConfig`, `s3RecordingConfig`, `trackingConfig`, `uplinkEchoConfig`.

antennaDownlinkConfig -> (structure)

Information about how AWS Ground Station should configure an antenna for downlink during a contact.

spectrumConfig -> (structure)

Object that describes a spectral `Config` .

bandwidth -> (structure)

Bandwidth of a spectral `Config` . AWS Ground Station currently has the following bandwidth limitations:

- For `AntennaDownlinkDemodDecodeconfig` , valid values are between 125 kHz to 650 MHz.
- For `AntennaDownlinkconfig` valid values are between 10 kHz to 54 MHz.
- For `AntennaUplinkConfig` , valid values are between 10 kHz to 54 MHz.

units -> (string)

Frequency bandwidth units.

value -> (double)

Frequency bandwidth value. AWS Ground Station currently has the following bandwidth limitations:

- For `AntennaDownlinkDemodDecodeconfig` , valid values are between 125 kHz to 650 MHz.
- For `AntennaDownlinkconfig` , valid values are between 10 kHz to 54 MHz.
- For `AntennaUplinkConfig` , valid values are between 10 kHz to 54 MHz.

centerFrequency -> (structure)

Center frequency of a spectral `Config` . Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.

units -> (string)

Frequency units.

value -> (double)

Frequency value. Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.

polarization -> (string)

Polarization of a spectral `Config` . Capturing both `"RIGHT_HAND"` and `"LEFT_HAND"` polarization requires two separate configs.

antennaDownlinkDemodDecodeConfig -> (structure)

Information about how AWS Ground Station should conï¬gure an antenna for downlink demod decode during a contact.

decodeConfig -> (structure)

Information about the decode `Config` .

unvalidatedJSON -> (string)

Unvalidated JSON of a decode `Config` .

demodulationConfig -> (structure)

Information about the demodulation `Config` .

unvalidatedJSON -> (string)

Unvalidated JSON of a demodulation `Config` .

spectrumConfig -> (structure)

Information about the spectral `Config` .

bandwidth -> (structure)

Bandwidth of a spectral `Config` . AWS Ground Station currently has the following bandwidth limitations:

- For `AntennaDownlinkDemodDecodeconfig` , valid values are between 125 kHz to 650 MHz.
- For `AntennaDownlinkconfig` valid values are between 10 kHz to 54 MHz.
- For `AntennaUplinkConfig` , valid values are between 10 kHz to 54 MHz.

units -> (string)

Frequency bandwidth units.

value -> (double)

Frequency bandwidth value. AWS Ground Station currently has the following bandwidth limitations:

- For `AntennaDownlinkDemodDecodeconfig` , valid values are between 125 kHz to 650 MHz.
- For `AntennaDownlinkconfig` , valid values are between 10 kHz to 54 MHz.
- For `AntennaUplinkConfig` , valid values are between 10 kHz to 54 MHz.

centerFrequency -> (structure)

Center frequency of a spectral `Config` . Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.

units -> (string)

Frequency units.

value -> (double)

Frequency value. Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.

polarization -> (string)

Polarization of a spectral `Config` . Capturing both `"RIGHT_HAND"` and `"LEFT_HAND"` polarization requires two separate configs.

antennaUplinkConfig -> (structure)

Information about how AWS Ground Station should conï¬gure an antenna for uplink during a contact.

spectrumConfig -> (structure)

Information about the uplink spectral `Config` .

centerFrequency -> (structure)

Center frequency of an uplink spectral `Config` . Valid values are between 2025 to 2120 MHz.

units -> (string)

Frequency units.

value -> (double)

Frequency value. Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.

polarization -> (string)

Polarization of an uplink spectral `Config` . Capturing both `"RIGHT_HAND"` and `"LEFT_HAND"` polarization requires two separate configs.

targetEirp -> (structure)

EIRP of the target.

units -> (string)

Units of an EIRP.

value -> (double)

Value of an EIRP. Valid values are between 20.0 to 50.0 dBW.

transmitDisabled -> (boolean)

Whether or not uplink transmit is disabled.

dataflowEndpointConfig -> (structure)

Information about the dataflow endpoint `Config` .

dataflowEndpointName -> (string)

Name of a dataflow endpoint.

dataflowEndpointRegion -> (string)

Region of a dataflow endpoint.

s3RecordingConfig -> (structure)

Information about an S3 recording `Config` .

bucketArn -> (string)

ARN of the bucket to record to.

prefix -> (string)

S3 Key prefix to prefice data files.

roleArn -> (string)

ARN of the role Ground Station assumes to write data to the bucket.

trackingConfig -> (structure)

Object that determines whether tracking should be used during a contact executed with this `Config` in the mission profile.

autotrack -> (string)

Current setting for autotrack.

uplinkEchoConfig -> (structure)

Information about an uplink echo `Config` .

Parameters from the `AntennaUplinkConfig` , corresponding to the specified `AntennaUplinkConfigArn` , are used when this `UplinkEchoConfig` is used in a contact.

antennaUplinkConfigArn -> (string)

ARN of an uplink `Config` .

enabled -> (boolean)

Whether or not an uplink `Config` is enabled.

configId -> (string)

UUID of a `Config` .

configType -> (string)

Type of a `Config` .

name -> (string)

Name of a `Config` .

tags -> (map)

Tags assigned to a `Config` .

key -> (string)

value -> (string)