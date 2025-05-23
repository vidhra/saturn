# snap-to-roadsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-routes/snap-to-roads.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-routes/snap-to-roads.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [geo-routes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-routes/index.html#cli-aws-geo-routes) ]

# snap-to-roads

## Description

`SnapToRoads` matches GPS trace to roads most likely traveled on.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/geo-routes-2020-11-19/SnapToRoads)

## Synopsis

```
snap-to-roads
[--key <value>]
[--snapped-geometry-format <value>]
[--snap-radius <value>]
--trace-points <value>
[--travel-mode <value>]
[--travel-mode-options <value>]
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

`--key` (string)

Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.

`--snapped-geometry-format` (string)

Chooses what the returned SnappedGeometry format should be.

Default Value: `FlexiblePolyline`

Possible values:

- `FlexiblePolyline`
- `Simple`

`--snap-radius` (long)

The radius around the provided tracepoint that is considered for snapping.

**Unit** : `meters`

Default value: `300`

`--trace-points` (list)

List of trace points to be snapped onto the road network.

(structure)

TracePoint indices for which the provided notice code corresponds to.

Heading -> (double)

GPS Heading at the position.

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

Speed -> (double)

Speed at the specified trace point .

**Unit** : `KilometersPerHour`

Timestamp -> (string)

Timestamp of the event.

Shorthand Syntax:

```
Heading=double,Position=double,double,Speed=double,Timestamp=string ...
```

JSON Syntax:

```
[
  {
    "Heading": double,
    "Position": [double, ...],
    "Speed": double,
    "Timestamp": "string"
  }
  ...
]
```

`--travel-mode` (string)

Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.

Default Value: `Car`

Possible values:

- `Car`
- `Pedestrian`
- `Scooter`
- `Truck`

`--travel-mode-options` (structure)

Travel mode related options for the provided travel mode.

Truck -> (structure)

Travel mode options when the provided travel mode is âTruckâ.

GrossWeight -> (long)

Gross weight of the vehicle including trailers, and goods at capacity.

**Unit** : `Kilograms`

HazardousCargos -> (list)

List of Hazardous cargos contained in the vehicle.

(string)

Height -> (long)

Height of the vehicle.

**Unit** : `centimeters`

Length -> (long)

Length of the vehicle.

**Unit** : `centimeters`

Trailer -> (structure)

Trailer options corresponding to the vehicle.

TrailerCount -> (integer)

Number of trailers attached to the vehicle.

Default Value: `0`

TunnelRestrictionCode -> (string)

The tunnel restriction code.

Tunnel categories in this list indicate the restrictions which apply to certain tunnels in Great Britain. They relate to the types of dangerous goods that can be transported through them.

- *Tunnel Category B*
- *Risk Level* : Limited risk
- *Restrictions* : Few restrictions
- *Tunnel Category C*
- *Risk Level* : Medium risk
- *Restrictions* : Some restrictions
- *Tunnel Category D*
- *Risk Level* : High risk
- *Restrictions* : Many restrictions occur
- *Tunnel Category E*
- *Risk Level* : Very high risk
- *Restrictions* : Restricted tunnel

Width -> (long)

Width of the vehicle in centimenters.

Shorthand Syntax:

```
Truck={GrossWeight=long,HazardousCargos=[string,string],Height=long,Length=long,Trailer={TrailerCount=integer},TunnelRestrictionCode=string,Width=long}
```

JSON Syntax:

```
{
  "Truck": {
    "GrossWeight": long,
    "HazardousCargos": ["Combustible"|"Corrosive"|"Explosive"|"Flammable"|"Gas"|"HarmfulToWater"|"Organic"|"Other"|"Poison"|"PoisonousInhalation"|"Radioactive", ...],
    "Height": long,
    "Length": long,
    "Trailer": {
      "TrailerCount": integer
    },
    "TunnelRestrictionCode": "string",
    "Width": long
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

## Output

Notices -> (list)

Notices are additional information returned that indicate issues that occurred during route calculation.

(structure)

Notices provide information around factors that may have influenced snapping in a manner atypical to the standard use cases.

Code -> (string)

Code corresponding to the issue.

Title -> (string)

The notice title.

TracePointIndexes -> (list)

TracePoint indices for which the provided notice code corresponds to.

(integer)

PricingBucket -> (string)

The pricing bucket for which the query is charged at.

SnappedGeometry -> (structure)

The interpolated geometry for the snapped route onto the road network.

LineString -> (list)

An ordered list of positions used to plot a route on a map.

### Note

LineString and Polyline are mutually exclusive properties.

(list)

(double)

Polyline -> (string)

An ordered list of positions used to plot a route on a map in a lossy compression format.

### Note

LineString and Polyline are mutually exclusive properties.

SnappedGeometryFormat -> (string)

Specifies the format of the geometry returned for each leg of the route.

SnappedTracePoints -> (list)

The trace points snapped onto the road network.

(structure)

TracePoints snapped onto the road network.

Confidence -> (double)

Confidence value for the correctness of this point match.

OriginalPosition -> (list)

Position of the TracePoint provided within the request, at the same index.

(double)

SnappedPosition -> (list)

Snapped position of the TracePoint provided within the request, at the same index.

(double)