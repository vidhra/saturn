# put-geofenceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/put-geofence.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/put-geofence.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [location](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/index.html#cli-aws-location) ]

# put-geofence

## Description

Stores a geofence geometry in a given geofence collection, or updates the geometry of an existing geofence if a geofence ID is included in the request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/location-2020-11-19/PutGeofence)

## Synopsis

```
put-geofence
--collection-name <value>
--geofence-id <value>
--geometry <value>
[--geofence-properties <value>]
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

The geofence collection to store the geofence in.

`--geofence-id` (string)

An identifier for the geofence. For example, `ExampleGeofence-1` .

`--geometry` (structure)

Contains the details to specify the position of the geofence. Can be a polygon, a circle or a polygon encoded in Geobuf format. Including multiple selections will return a validation error.

### Note

The [geofence polygon](https://docs.aws.amazon.com/location-geofences/latest/APIReference/API_GeofenceGeometry.html) format supports a maximum of 1,000 vertices. The [Geofence Geobuf](https://docs.aws.amazon.com/location-geofences/latest/APIReference/API_GeofenceGeometry.html) format supports a maximum of 100,000 vertices.

Polygon -> (list)

A polygon is a list of linear rings which are each made up of a list of vertices.

Each vertex is a 2-dimensional point of the form: `[longitude, latitude]` . This is represented as an array of doubles of length 2 (so `[double, double]` ).

An array of 4 or more vertices, where the first and last vertex are the same (to form a closed boundary), is called a linear ring. The linear ring vertices must be listed in counter-clockwise order around the ringâs interior. The linear ring is represented as an array of vertices, or an array of arrays of doubles (`[[double, double], ...]` ).

A geofence consists of a single linear ring. To allow for future expansion, the Polygon parameter takes an array of linear rings, which is represented as an array of arrays of arrays of doubles (`[[[double, double], ...], ...]` ).

A linear ring for use in geofences can consist of between 4 and 1,000 vertices.

(list)

(list)

(double)

Circle -> (structure)

A circle on the earth, as defined by a center point and a radius.

Center -> (list)

A single point geometry, specifying the center of the circle, using [WGS 84](https://gisgeography.com/wgs84-world-geodetic-system/) coordinates, in the form `[longitude, latitude]` .

(double)

Radius -> (double)

The radius of the circle in meters. Must be greater than zero and no larger than 100,000 (100 kilometers).

Geobuf -> (blob)

Geobuf is a compact binary encoding for geographic data that provides lossless compression of GeoJSON polygons. The Geobuf must be Base64-encoded.

A polygon in Geobuf format can have up to 100,000 vertices.

JSON Syntax:

```
{
  "Polygon": [
    [
      [double, ...]
      ...
    ]
    ...
  ],
  "Circle": {
    "Center": [double, ...],
    "Radius": double
  },
  "Geobuf": blob
}
```

`--geofence-properties` (map)

Associates one of more properties with the geofence. A property is a key-value pair stored with the geofence and added to any geofence event triggered with that geofence.

Format: `"key" : "value"`

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

GeofenceId -> (string)

The geofence identifier entered in the request.

CreateTime -> (timestamp)

The timestamp for when the geofence was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`

UpdateTime -> (timestamp)

The timestamp for when the geofence was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`