# batch-update-vehicleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotfleetwise/batch-update-vehicle.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotfleetwise/batch-update-vehicle.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotfleetwise](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotfleetwise/index.html#cli-aws-iotfleetwise) ]

# batch-update-vehicle

## Description

Updates a group, or batch, of vehicles.

### Note

You must specify a decoder manifest and a vehicle model (model manifest) for each vehicle.

For more information, see [Update multiple vehicles (AWS CLI)](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-vehicles-cli.html) in the *Amazon Web Services IoT FleetWise Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotfleetwise-2021-06-17/BatchUpdateVehicle)

## Synopsis

```
batch-update-vehicle
--vehicles <value>
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

`--vehicles` (list)

A list of information about the vehicles to update. For more information, see the API data type.

(structure)

Information about the vehicle to update.

### Warning

Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see [Amazon Web Services Region and feature availability](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html) in the *Amazon Web Services IoT FleetWise Developer Guide* .

vehicleName -> (string)

The unique ID of the vehicle to update.

modelManifestArn -> (string)

The ARN of the vehicle model (model manifest) associated with the vehicle to update.

decoderManifestArn -> (string)

The ARN of the signal decoder manifest associated with the vehicle to update.

attributes -> (map)

Static information about a vehicle in a key-value pair. For example:

`"engineType"` : `"1.3 L R2"`

key -> (string)

value -> (string)

attributeUpdateMode -> (string)

The method the specified attributes will update the existing attributes on the vehicle. Use``Overwite`` to replace the vehicle attributes with the specified attributes. Or use `Merge` to combine all attributes.

This is required if attributes are present in the input.

stateTemplatesToAdd -> (list)

Associate additional state templates to track the state of the vehicle. State templates determine which signal updates the vehicle sends to the cloud.

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

stateTemplatesToRemove -> (list)

Remove existing state template associations from the vehicle.

(string)

stateTemplatesToUpdate -> (list)

Change the `stateTemplateUpdateStrategy` of state templates already associated with the vehicle.

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

JSON Syntax:

```
[
  {
    "vehicleName": "string",
    "modelManifestArn": "string",
    "decoderManifestArn": "string",
    "attributes": {"string": "string"
      ...},
    "attributeUpdateMode": "Overwrite"|"Merge",
    "stateTemplatesToAdd": [
      {
        "identifier": "string",
        "stateTemplateUpdateStrategy": {
          "periodic": {
            "stateTemplateUpdateRate": {
              "unit": "MILLISECOND"|"SECOND"|"MINUTE"|"HOUR",
              "value": integer
            }
          },
          "onChange": {

          }
        }
      }
      ...
    ],
    "stateTemplatesToRemove": ["string", ...],
    "stateTemplatesToUpdate": [
      {
        "identifier": "string",
        "stateTemplateUpdateStrategy": {
          "periodic": {
            "stateTemplateUpdateRate": {
              "unit": "MILLISECOND"|"SECOND"|"MINUTE"|"HOUR",
              "value": integer
            }
          },
          "onChange": {

          }
        }
      }
      ...
    ]
  }
  ...
]
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

vehicles -> (list)

A list of information about the batch of updated vehicles.

### Note

This list contains only unique IDs for the vehicles that were updated.

(structure)

Information about the updated vehicle.

vehicleName -> (string)

The unique ID of the updated vehicle.

arn -> (string)

The Amazon Resource Name (ARN) of the updated vehicle.

errors -> (list)

A list of information about errors returned while updating a batch of vehicles, or, if there arenât any errors, an empty list.

(structure)

An HTTP error resulting from updating the description for a vehicle.

vehicleName -> (string)

The ID of the vehicle with the error.

code -> (integer)

The relevant HTTP error code (400+).

message -> (string)

A message associated with the error.