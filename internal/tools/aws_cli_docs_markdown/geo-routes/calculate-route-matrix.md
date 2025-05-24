# calculate-route-matrixÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-routes/calculate-route-matrix.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-routes/calculate-route-matrix.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [geo-routes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-routes/index.html#cli-aws-geo-routes) ]

# calculate-route-matrix

## Description

Use `CalculateRouteMatrix` to compute results for all pairs of Origins to Destinations. Each row corresponds to one entry in Origins. Each entry in the row corresponds to the route from that entry in Origins to an entry in Destinations positions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/geo-routes-2020-11-19/CalculateRouteMatrix)

## Synopsis

```
calculate-route-matrix
[--allow <value>]
[--avoid <value>]
[--depart-now | --no-depart-now]
[--departure-time <value>]
--destinations <value>
[--exclude <value>]
[--key <value>]
[--optimize-routing-for <value>]
--origins <value>
--routing-boundary <value>
[--traffic <value>]
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

`--allow` (structure)

Features that are allowed while calculating a route.

Hot -> (boolean)

Allow Hot (High Occupancy Toll) lanes while calculating the route.

Default value: `false`

Hov -> (boolean)

Allow Hov (High Occupancy vehicle) lanes while calculating the route.

Default value: `false`

Shorthand Syntax:

```
Hot=boolean,Hov=boolean
```

JSON Syntax:

```
{
  "Hot": true|false,
  "Hov": true|false
}
```

`--avoid` (structure)

Features that are avoided while calculating a route. Avoidance is on a best-case basis. If an avoidance canât be satisfied for a particular case, it violates the avoidance and the returned response produces a notice for the violation.

Areas -> (list)

Areas to be avoided.

(structure)

Area to be avoided.

Geometry -> (structure)

Geometry of the area to be avoided.

BoundingBox -> (list)

Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.

(double)

Polygon -> (list)

Geometry defined as a polygon with only one linear ring.

(list)

(list)

(double)

PolylinePolygon -> (list)

A list of Isoline PolylinePolygon, for each isoline PolylinePolygon, it contains PolylinePolygon of the first linear ring (the outer ring) and from second item to the last item (the inner rings). For more information on polyline encoding, see [https://github.com/heremaps/flexiblepolyline/blob/master/README.md](https://github.com/heremaps/flexiblepolyline/blob/master/README.md) .

(string)

CarShuttleTrains -> (boolean)

Avoid car-shuttle-trains while calculating the route.

ControlledAccessHighways -> (boolean)

Avoid controlled access highways while calculating the route.

DirtRoads -> (boolean)

Avoid dirt roads while calculating the route.

Ferries -> (boolean)

Avoid ferries while calculating the route.

TollRoads -> (boolean)

Avoids roads where the specified toll transponders are the only mode of payment.

TollTransponders -> (boolean)

Avoids roads where the specified toll transponders are the only mode of payment.

TruckRoadTypes -> (list)

Truck road type identifiers. `BK1` through `BK4` apply only to Sweden. `A2,A4,B2,B4,C,D,ET2,ET4` apply only to Mexico.

### Note

There are currently no other supported values as of 26th April 2024.

(string)

Tunnels -> (boolean)

Avoid tunnels while calculating the route.

UTurns -> (boolean)

Avoid U-turns for calculation on highways and motorways.

ZoneCategories -> (list)

Zone categories to be avoided.

(structure)

Zone categories to be avoided.

Category -> (string)

Zone category to be avoided.

JSON Syntax:

```
{
  "Areas": [
    {
      "Geometry": {
        "BoundingBox": [double, ...],
        "Polygon": [
          [
            [double, ...]
            ...
          ]
          ...
        ],
        "PolylinePolygon": ["string", ...]
      }
    }
    ...
  ],
  "CarShuttleTrains": true|false,
  "ControlledAccessHighways": true|false,
  "DirtRoads": true|false,
  "Ferries": true|false,
  "TollRoads": true|false,
  "TollTransponders": true|false,
  "TruckRoadTypes": ["string", ...],
  "Tunnels": true|false,
  "UTurns": true|false,
  "ZoneCategories": [
    {
      "Category": "CongestionPricing"|"Environmental"|"Vignette"
    }
    ...
  ]
}
```

`--depart-now` | `--no-depart-now` (boolean)

Uses the current time as the time of departure.

`--departure-time` (string)

Time of departure from thr origin.

Time format:`YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`

Examples:

`2020-04-22T17:57:24Z`

`2020-04-22T17:57:24+02:00`

`--destinations` (list)

List of destinations for the route.

### Note

Route calculations are billed for each origin and destination pair. If you use a large matrix of origins and destinations, your costs will increase accordingly. See Amazon Locationâs pricing page <https://docs.aws.amazon.com/location/latest/developerguide/routes-pricing.html>`__ for more information.

(structure)

The route destination.

Options -> (structure)

Destination related options.

AvoidActionsForDistance -> (long)

Avoids actions for the provided distance. This is typically to consider for users in moving vehicles who may not have sufficient time to make an action at an origin or a destination.

Heading -> (double)

GPS Heading at the position.

Matching -> (structure)

Options to configure matching the provided position to the road network.

NameHint -> (string)

Attempts to match the provided position to a road similar to the provided name.

OnRoadThreshold -> (long)

If the distance to a highway/bridge/tunnel/sliproad is within threshold, the waypoint will be snapped to the highway/bridge/tunnel/sliproad.

**Unit** : `meters`

Radius -> (long)

Considers all roads within the provided radius to match the provided destination to. The roads that are considered are determined by the provided Strategy.

**Unit** : `Meters`

Strategy -> (string)

Strategy that defines matching of the position onto the road network. MatchAny considers all roads possible, whereas MatchMostSignificantRoad matches to the most significant road.

SideOfStreet -> (structure)

Options to configure matching the provided position to a side of the street.

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

UseWith -> (string)

Strategy that defines when the side of street position should be used. AnyStreet will always use the provided position.

Default Value: `DividedStreetOnly`

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

JSON Syntax:

```
[
  {
    "Options": {
      "AvoidActionsForDistance": long,
      "Heading": double,
      "Matching": {
        "NameHint": "string",
        "OnRoadThreshold": long,
        "Radius": long,
        "Strategy": "MatchAny"|"MatchMostSignificantRoad"
      },
      "SideOfStreet": {
        "Position": [double, ...],
        "UseWith": "AnyStreet"|"DividedStreetOnly"
      }
    },
    "Position": [double, ...]
  }
  ...
]
```

`--exclude` (structure)

Features to be strictly excluded while calculating the route.

Countries -> (list)

List of countries to be avoided defined by two-letter or three-letter country codes.

(string)

Shorthand Syntax:

```
Countries=string,string
```

JSON Syntax:

```
{
  "Countries": ["string", ...]
}
```

`--key` (string)

Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.

`--optimize-routing-for` (string)

Specifies the optimization criteria for calculating a route.

Default Value: `FastestRoute`

Possible values:

- `FastestRoute`
- `ShortestRoute`

`--origins` (list)

The position in longitude and latitude for the origin.

### Note

Route calculations are billed for each origin and destination pair. Using a large amount of Origins in a request can lead you to incur unexpected charges. See Amazon Locationâs pricing page <https://docs.aws.amazon.com/location/latest/developerguide/routes-pricing.html>`__ for more information.

(structure)

The start position for the route.

Options -> (structure)

Origin related options.

AvoidActionsForDistance -> (long)

Avoids actions for the provided distance. This is typically to consider for users in moving vehicles who may not have sufficient time to make an action at an origin or a destination.

Heading -> (double)

GPS Heading at the position.

Matching -> (structure)

Options to configure matching the provided position to the road network.

NameHint -> (string)

Attempts to match the provided position to a road similar to the provided name.

OnRoadThreshold -> (long)

If the distance to a highway/bridge/tunnel/sliproad is within threshold, the waypoint will be snapped to the highway/bridge/tunnel/sliproad.

**Unit** : `meters`

Radius -> (long)

Considers all roads within the provided radius to match the provided destination to. The roads that are considered are determined by the provided Strategy.

**Unit** : `Meters`

Strategy -> (string)

Strategy that defines matching of the position onto the road network. MatchAny considers all roads possible, whereas MatchMostSignificantRoad matches to the most significant road.

SideOfStreet -> (structure)

Options to configure matching the provided position to a side of the street.

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

UseWith -> (string)

Strategy that defines when the side of street position should be used. AnyStreet will always use the provided position.

Default Value: `DividedStreetOnly`

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

JSON Syntax:

```
[
  {
    "Options": {
      "AvoidActionsForDistance": long,
      "Heading": double,
      "Matching": {
        "NameHint": "string",
        "OnRoadThreshold": long,
        "Radius": long,
        "Strategy": "MatchAny"|"MatchMostSignificantRoad"
      },
      "SideOfStreet": {
        "Position": [double, ...],
        "UseWith": "AnyStreet"|"DividedStreetOnly"
      }
    },
    "Position": [double, ...]
  }
  ...
]
```

`--routing-boundary` (structure)

Boundary within which the matrix is to be calculated. All data, origins and destinations outside the boundary are considered invalid.

### Note

When request routing boundary was set as AutoCircle, the response routing boundary will return Circle derived from the AutoCircle settings.

Geometry -> (structure)

Geometry of the area to be avoided.

AutoCircle -> (structure)

Provides the circle that was used while calculating the route.

Margin -> (long)

The margin provided for the calculation.

MaxRadius -> (long)

The maximum size of the radius provided for the calculation.

Circle -> (structure)

Geometry defined as a circle. When request routing boundary was set as `AutoCircle` , the response routing boundary will return `Circle` derived from the `AutoCircle` settings.

Center -> (list)

Center of the Circle defined in longitude and latitude coordinates.

Example: `[-123.1174, 49.2847]` represents the position with longitude `-123.1174` and latitude `49.2847` .

(double)

Radius -> (double)

Radius of the Circle.

**Unit** : `meters`

BoundingBox -> (list)

Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.

(double)

Polygon -> (list)

Geometry defined as a polygon with only one linear ring.

(list)

(list)

(double)

Unbounded -> (boolean)

No restrictions in terms of a routing boundary, and is typically used for longer routes.

JSON Syntax:

```
{
  "Geometry": {
    "AutoCircle": {
      "Margin": long,
      "MaxRadius": long
    },
    "Circle": {
      "Center": [double, ...],
      "Radius": double
    },
    "BoundingBox": [double, ...],
    "Polygon": [
      [
        [double, ...]
        ...
      ]
      ...
    ]
  },
  "Unbounded": true|false
}
```

`--traffic` (structure)

Traffic related options.

FlowEventThresholdOverride -> (long)

Duration for which flow traffic is considered valid. For this period, the flow traffic is used over historical traffic data. Flow traffic refers to congestion, which changes very quickly. Duration in seconds for which flow traffic event would be considered valid. While flow traffic event is valid it will be used over the historical traffic data.

Usage -> (string)

Determines if traffic should be used or ignored while calculating the route.

Default Value: `UseTrafficData`

Shorthand Syntax:

```
FlowEventThresholdOverride=long,Usage=string
```

JSON Syntax:

```
{
  "FlowEventThresholdOverride": long,
  "Usage": "IgnoreTrafficData"|"UseTrafficData"
}
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

Car -> (structure)

Travel mode options when the provided travel mode is âCarâ

LicensePlate -> (structure)

The vehicle License Plate.

LastCharacter -> (string)

The last character of the License Plate.

MaxSpeed -> (double)

Maximum speed

**Unit** : `KilometersPerHour`

Occupancy -> (integer)

The number of occupants in the vehicle.

Default Value: `1`

Scooter -> (structure)

Travel mode options when the provided travel mode is `Scooter`

### Note

When travel mode is set to `Scooter` , then the avoidance option `ControlledAccessHighways` defaults to `true` .

LicensePlate -> (structure)

The vehicle License Plate.

LastCharacter -> (string)

The last character of the License Plate.

MaxSpeed -> (double)

Maximum speed.

**Unit** : `KilometersPerHour`

Occupancy -> (integer)

The number of occupants in the vehicle.

Default Value: `1`

Truck -> (structure)

Travel mode options when the provided travel mode is âTruckâ

AxleCount -> (integer)

Total number of axles of the vehicle.

GrossWeight -> (long)

Gross weight of the vehicle including trailers, and goods at capacity.

**Unit** : `Kilograms`

HazardousCargos -> (list)

List of Hazardous cargo contained in the vehicle.

(string)

Height -> (long)

Height of the vehicle.

**Unit** : `centimeters`

KpraLength -> (long)

Kingpin to rear axle length of the vehicle

**Unit** : `centimeters`

Length -> (long)

Length of the vehicle.

**Unit** : `centimeters`

LicensePlate -> (structure)

The vehicle License Plate.

LastCharacter -> (string)

The last character of the License Plate.

MaxSpeed -> (double)

Maximum speed

**Unit** : `KilometersPerHour`

Occupancy -> (integer)

The number of occupants in the vehicle.

Default Value: `1`

PayloadCapacity -> (long)

Payload capacity of the vehicle and trailers attached.

**Unit** : `kilograms`

Trailer -> (structure)

Trailer options corresponding to the vehicle.

TrailerCount -> (integer)

Number of trailers attached to the vehicle.

Default Value: `0`

TruckType -> (string)

Type of the truck.

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

WeightPerAxle -> (long)

Heaviest weight per axle irrespective of the axle type or the axle group. Meant for usage in countries where the differences in axle types or axle groups are not distinguished.

**Unit** : `Kilograms`

WeightPerAxleGroup -> (structure)

Specifies the total weight for the specified axle group. Meant for usage in countries that have different regulations based on the axle group type.

Single -> (long)

Weight for single axle group.

**Unit** : `Kilograms`

Tandem -> (long)

Weight for tandem axle group.

**Unit** : `Kilograms`

Triple -> (long)

Weight for triple axle group.

**Unit** : `Kilograms`

Quad -> (long)

Weight for quad axle group.

**Unit** : `Kilograms`

Quint -> (long)

Weight for quad quint group.

**Unit** : `Kilograms`

Width -> (long)

Width of the vehicle.

**Unit** : `centimeters`

Shorthand Syntax:

```
Car={LicensePlate={LastCharacter=string},MaxSpeed=double,Occupancy=integer},Scooter={LicensePlate={LastCharacter=string},MaxSpeed=double,Occupancy=integer},Truck={AxleCount=integer,GrossWeight=long,HazardousCargos=[string,string],Height=long,KpraLength=long,Length=long,LicensePlate={LastCharacter=string},MaxSpeed=double,Occupancy=integer,PayloadCapacity=long,Trailer={TrailerCount=integer},TruckType=string,TunnelRestrictionCode=string,WeightPerAxle=long,WeightPerAxleGroup={Single=long,Tandem=long,Triple=long,Quad=long,Quint=long},Width=long}
```

JSON Syntax:

```
{
  "Car": {
    "LicensePlate": {
      "LastCharacter": "string"
    },
    "MaxSpeed": double,
    "Occupancy": integer
  },
  "Scooter": {
    "LicensePlate": {
      "LastCharacter": "string"
    },
    "MaxSpeed": double,
    "Occupancy": integer
  },
  "Truck": {
    "AxleCount": integer,
    "GrossWeight": long,
    "HazardousCargos": ["Combustible"|"Corrosive"|"Explosive"|"Flammable"|"Gas"|"HarmfulToWater"|"Organic"|"Other"|"Poison"|"PoisonousInhalation"|"Radioactive", ...],
    "Height": long,
    "KpraLength": long,
    "Length": long,
    "LicensePlate": {
      "LastCharacter": "string"
    },
    "MaxSpeed": double,
    "Occupancy": integer,
    "PayloadCapacity": long,
    "Trailer": {
      "TrailerCount": integer
    },
    "TruckType": "LightTruck"|"StraightTruck"|"Tractor",
    "TunnelRestrictionCode": "string",
    "WeightPerAxle": long,
    "WeightPerAxleGroup": {
      "Single": long,
      "Tandem": long,
      "Triple": long,
      "Quad": long,
      "Quint": long
    },
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

ErrorCount -> (integer)

The count of error results in the route matrix. If this number is 0, all routes were calculated successfully.

PricingBucket -> (string)

The pricing bucket for which the query is charged at.

RouteMatrix -> (list)

The calculated route matrix containing the results for all pairs of Origins to Destination positions. Each row corresponds to one entry in Origins. Each entry in the row corresponds to the route from that entry in Origins to an entry in Destination positions.

(list)

(structure)

The calculated route matrix containing the results for all pairs of Origins to Destination positions. Each row corresponds to one entry in Origins. Each entry in the row corresponds to the route from that entry in Origins to an entry in Destination positions.

Distance -> (long)

The total distance of travel for the route.

Duration -> (long)

The expected duration of travel for the route.

**Unit** : `seconds`

Error -> (string)

Error code that occurred during calculation of the route.

RoutingBoundary -> (structure)

Boundary within which the matrix is to be calculated. All data, origins and destinations outside the boundary are considered invalid.

### Note

When request routing boundary was set as AutoCircle, the response routing boundary will return Circle derived from the AutoCircle settings.

Geometry -> (structure)

Geometry of the area to be avoided.

AutoCircle -> (structure)

Provides the circle that was used while calculating the route.

Margin -> (long)

The margin provided for the calculation.

MaxRadius -> (long)

The maximum size of the radius provided for the calculation.

Circle -> (structure)

Geometry defined as a circle. When request routing boundary was set as `AutoCircle` , the response routing boundary will return `Circle` derived from the `AutoCircle` settings.

Center -> (list)

Center of the Circle defined in longitude and latitude coordinates.

Example: `[-123.1174, 49.2847]` represents the position with longitude `-123.1174` and latitude `49.2847` .

(double)

Radius -> (double)

Radius of the Circle.

**Unit** : `meters`

BoundingBox -> (list)

Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.

(double)

Polygon -> (list)

Geometry defined as a polygon with only one linear ring.

(list)

(list)

(double)

Unbounded -> (boolean)

No restrictions in terms of a routing boundary, and is typically used for longer routes.