# batch-evaluate-geofencesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/batch-evaluate-geofences.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/batch-evaluate-geofences.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [location](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/index.html#cli-aws-location) ]

# batch-evaluate-geofences

## Description

Evaluates device positions against the geofence geometries from a given geofence collection.

This operation always returns an empty response because geofences are asynchronously evaluated. The evaluation determines if the device has entered or exited a geofenced area, and then publishes one of the following events to Amazon EventBridge:

- `ENTER` if Amazon Location determines that the tracked device has entered a geofenced area.
- `EXIT` if Amazon Location determines that the tracked device has exited a geofenced area.

### Note

The last geofence that a device was observed within is tracked for 30 days after the most recent device position update.

### Note

Geofence evaluation uses the given device position. It does not account for the optional `Accuracy` of a `DevicePositionUpdate` .

### Note

The `DeviceID` is used as a string to represent the device. You do not need to have a `Tracker` associated with the `DeviceID` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/location-2020-11-19/BatchEvaluateGeofences)

## Synopsis

```
batch-evaluate-geofences
--collection-name <value>
--device-position-updates <value>
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

`--collection-name` (string)

The geofence collection used in evaluating the position of devices against its geofences.

`--device-position-updates` (list)

Contains device details for each device to be evaluated against the given geofence collection.

(structure)

Contains the position update details for a device.

DeviceId -> (string)

The device associated to the position update.

SampleTime -> (timestamp)

The timestamp at which the deviceâs position was determined. Uses [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`

Position -> (list)

The latest device position defined in [WGS 84](https://earth-info.nga.mil/index.php?dir=wgs84&action=wgs84) format: `[X or longitude, Y or latitude]` .

(double)

Accuracy -> (structure)

The accuracy of the device position.

Horizontal -> (double)

Estimated maximum distance, in meters, between the measured position and the true position of a device, along the Earthâs surface.

PositionProperties -> (map)

Associates one of more properties with the position update. A property is a key-value pair stored with the position update and added to any geofence event the update may trigger.

Format: `"key" : "value"`

key -> (string)

value -> (string)

Shorthand Syntax:

```
DeviceId=string,SampleTime=timestamp,Position=double,double,Accuracy={Horizontal=double},PositionProperties={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "DeviceId": "string",
    "SampleTime": timestamp,
    "Position": [double, ...],
    "Accuracy": {
      "Horizontal": double
    },
    "PositionProperties": {"string": "string"
      ...}
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

Errors -> (list)

Contains error details for each device that failed to evaluate its position against the given geofence collection.

(structure)

Contains error details for each device that failed to evaluate its position against the geofences in a given geofence collection.

DeviceId -> (string)

The device associated with the position evaluation error.

SampleTime -> (timestamp)

Specifies a timestamp for when the error occurred in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`

Error -> (structure)

Contains details associated to the batch error.

Code -> (string)

The error code associated with the batch request error.

Message -> (string)

A message with the reason for the batch request error.