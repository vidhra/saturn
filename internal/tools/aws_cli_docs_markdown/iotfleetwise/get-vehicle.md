# get-vehicleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotfleetwise/get-vehicle.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotfleetwise/get-vehicle.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotfleetwise](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotfleetwise/index.html#cli-aws-iotfleetwise) ]

# get-vehicle

## Description

Retrieves information about a vehicle.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotfleetwise-2021-06-17/GetVehicle)

## Synopsis

```
get-vehicle
--vehicle-name <value>
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

`--vehicle-name` (string)

The ID of the vehicle to retrieve information about.

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

vehicleName -> (string)

The ID of the vehicle.

arn -> (string)

The Amazon Resource Name (ARN) of the vehicle to retrieve information about.

modelManifestArn -> (string)

The ARN of a vehicle model (model manifest) associated with the vehicle.

decoderManifestArn -> (string)

The ARN of a decoder manifest associated with the vehicle.

attributes -> (map)

Static information about a vehicle in a key-value pair. For example:

`"engineType"` : `"1.3 L R2"`

key -> (string)

value -> (string)

stateTemplates -> (list)

State templates associated with the vehicle.

(structure)

The state template associated with a vehicle. State templates contain state properties, which are signals that belong to a signal catalog that is synchronized between the Amazon Web Services IoT FleetWise Edge and the Amazon Web Services Cloud.

### Warning

Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see [Amazon Web Services Region and feature availability](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html) in the *Amazon Web Services IoT FleetWise Developer Guide* .

identifier -> (string)

The unique ID of the state template.

stateTemplateUpdateStrategy -> (tagged union structure)

The update strategy for the state template. Vehicles associated with the state template can stream telemetry data with either an `onChange` or `periodic` update strategy.

### Warning

Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see [Amazon Web Services Region and feature availability](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html) in the *Amazon Web Services IoT FleetWise Developer Guide* .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `periodic`, `onChange`.

periodic -> (structure)

Vehicles associated with the state template will stream telemetry data during a specified time period.

stateTemplateUpdateRate -> (structure)

The length of time between state template updates.

unit -> (string)

A unit of time.

value -> (integer)

A number of time units.

onChange -> (structure)

Vehicles associated with the state template will stream telemetry data when there is a change.

creationTime -> (timestamp)

The time the vehicle was created in seconds since epoch (January 1, 1970 at midnight UTC time).

lastModificationTime -> (timestamp)

The time the vehicle was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).