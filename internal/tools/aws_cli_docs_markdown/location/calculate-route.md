# calculate-routeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/calculate-route.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/calculate-route.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [location](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/index.html#cli-aws-location) ]

# calculate-route

## Description

[Calculates a route](https://docs.aws.amazon.com/location/latest/developerguide/calculate-route.html) given the following required parameters: `DeparturePosition` and `DestinationPosition` . Requires that you first [create a route calculator resource](https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CreateRouteCalculator.html) .

By default, a request that doesnât specify a departure time uses the best time of day to travel with the best traffic conditions when calculating the route.

Additional options include:

- [Specifying a departure time](https://docs.aws.amazon.com/location/latest/developerguide/departure-time.html) using either `DepartureTime` or `DepartNow` . This calculates a route based on predictive traffic data at the given time.

### Note

You canât specify both `DepartureTime` and `DepartNow` in a single request. Specifying both parameters returns a validation error.

- [Specifying a travel mode](https://docs.aws.amazon.com/location/latest/developerguide/travel-mode.html) using TravelMode sets the transportation mode used to calculate the routes. This also lets you specify additional route preferences in `CarModeOptions` if traveling by `Car` , or `TruckModeOptions` if traveling by `Truck` .

### Note

If you specify `walking` for the travel mode and your data provider is Esri, the start and destination must be within 40km.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/location-2020-11-19/CalculateRoute)

## Synopsis

```
calculate-route
--calculator-name <value>
--departure-position <value>
--destination-position <value>
[--waypoint-positions <value>]
[--travel-mode <value>]
[--departure-time <value>]
[--depart-now | --no-depart-now]
[--distance-unit <value>]
[--include-leg-geometry | --no-include-leg-geometry]
[--car-mode-options <value>]
[--truck-mode-options <value>]
[--arrival-time <value>]
[--optimize-for <value>]
[--key <value>]
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

`--calculator-name` (string)

The name of the route calculator resource that you want to use to calculate the route.

`--departure-position` (list)

The start position for the route. Defined in [World Geodetic System (WGS 84)](https://earth-info.nga.mil/index.php?dir=wgs84&action=wgs84) format: `[longitude, latitude]` .

- For example, `[-123.115, 49.285]`

### Note

If you specify a departure thatâs not located on a road, Amazon Location [moves the position to the nearest road](https://docs.aws.amazon.com/location/latest/developerguide/snap-to-nearby-road.html) . If Esri is the provider for your route calculator, specifying a route that is longer than 400 km returns a `400 RoutesValidationException` error.

Valid Values: `[-180 to 180,-90 to 90]`

(double)

Syntax:

```
double double ...
```

`--destination-position` (list)

The finish position for the route. Defined in [World Geodetic System (WGS 84)](https://earth-info.nga.mil/index.php?dir=wgs84&action=wgs84) format: `[longitude, latitude]` .

- For example, `[-122.339, 47.615]`

### Note

If you specify a destination thatâs not located on a road, Amazon Location [moves the position to the nearest road](https://docs.aws.amazon.com/location/latest/developerguide/snap-to-nearby-road.html) .

Valid Values: `[-180 to 180,-90 to 90]`

(double)

Syntax:

```
double double ...
```

`--waypoint-positions` (list)

Specifies an ordered list of up to 23 intermediate positions to include along a route between the departure position and destination position.

- For example, from the `DeparturePosition` `[-123.115, 49.285]` , the route follows the order that the waypoint positions are given `[[-122.757, 49.0021],[-122.349, 47.620]]`

### Note

If you specify a waypoint position thatâs not located on a road, Amazon Location [moves the position to the nearest road](https://docs.aws.amazon.com/location/latest/developerguide/snap-to-nearby-road.html) .

Specifying more than 23 waypoints returns a `400 ValidationException` error.

If Esri is the provider for your route calculator, specifying a route that is longer than 400 km returns a `400 RoutesValidationException` error.

Valid Values: `[-180 to 180,-90 to 90]`

(list)

(double)

Shorthand Syntax:

```
double,double ...
```

JSON Syntax:

```
[
  [double, ...]
  ...
]
```

`--travel-mode` (string)

Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility. You can choose `Car` , `Truck` , `Walking` , `Bicycle` or `Motorcycle` as options for the `TravelMode` .

### Note

`Bicycle` and `Motorcycle` are only valid when using Grab as a data provider, and only within Southeast Asia.

`Truck` is not available for Grab.

For more details on the using Grab for routing, including areas of coverage, see [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/grab.html) in the *Amazon Location Service Developer Guide* .

The `TravelMode` you specify also determines how you specify route preferences:

- If traveling by `Car` use the `CarModeOptions` parameter.
- If traveling by `Truck` use the `TruckModeOptions` parameter.

Default Value: `Car`

Possible values:

- `Car`
- `Truck`
- `Walking`
- `Bicycle`
- `Motorcycle`

`--departure-time` (timestamp)

Specifies the desired time of departure. Uses the given time to calculate the route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.

- In [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ` . For example, `2020â07-2T12:15:20.000Z+01:00`

`--depart-now` | `--no-depart-now` (boolean)

Sets the time of departure as the current time. Uses the current time to calculate a route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.

Default Value: `false`

Valid Values: `false` | `true`

`--distance-unit` (string)

Set the unit system to specify the distance.

Default Value: `Kilometers`

Possible values:

- `Kilometers`
- `Miles`

`--include-leg-geometry` | `--no-include-leg-geometry` (boolean)

Set to include the geometry details in the result for each path between a pair of positions.

Default Value: `false`

Valid Values: `false` | `true`

`--car-mode-options` (structure)

Specifies route preferences when traveling by `Car` , such as avoiding routes that use ferries or tolls.

Requirements: `TravelMode` must be specified as `Car` .

AvoidFerries -> (boolean)

Avoids ferries when calculating routes.

Default Value: `false`

Valid Values: `false` | `true`

AvoidTolls -> (boolean)

Avoids tolls when calculating routes.

Default Value: `false`

Valid Values: `false` | `true`

Shorthand Syntax:

```
AvoidFerries=boolean,AvoidTolls=boolean
```

JSON Syntax:

```
{
  "AvoidFerries": true|false,
  "AvoidTolls": true|false
}
```

`--truck-mode-options` (structure)

Specifies route preferences when traveling by `Truck` , such as avoiding routes that use ferries or tolls, and truck specifications to consider when choosing an optimal road.

Requirements: `TravelMode` must be specified as `Truck` .

AvoidFerries -> (boolean)

Avoids ferries when calculating routes.

Default Value: `false`

Valid Values: `false` | `true`

AvoidTolls -> (boolean)

Avoids tolls when calculating routes.

Default Value: `false`

Valid Values: `false` | `true`

Dimensions -> (structure)

Specifies the truckâs dimension specifications including length, height, width, and unit of measurement. Used to avoid roads that canât support the truckâs dimensions.

Length -> (double)

The length of the truck.

- For example, `15.5` .

### Note

For routes calculated with a HERE resource, this value must be between 0 and 300 meters.

Height -> (double)

The height of the truck.

- For example, `4.5` .

### Note

For routes calculated with a HERE resource, this value must be between 0 and 50 meters.

Width -> (double)

The width of the truck.

- For example, `4.5` .

### Note

For routes calculated with a HERE resource, this value must be between 0 and 50 meters.

Unit -> (string)

Specifies the unit of measurement for the truck dimensions.

Default Value: `Meters`

Weight -> (structure)

Specifies the truckâs weight specifications including total weight and unit of measurement. Used to avoid roads that canât support the truckâs weight.

Total -> (double)

The total weight of the truck.

- For example, `3500` .

Unit -> (string)

The unit of measurement to use for the truck weight.

Default Value: `Kilograms`

Shorthand Syntax:

```
AvoidFerries=boolean,AvoidTolls=boolean,Dimensions={Length=double,Height=double,Width=double,Unit=string},Weight={Total=double,Unit=string}
```

JSON Syntax:

```
{
  "AvoidFerries": true|false,
  "AvoidTolls": true|false,
  "Dimensions": {
    "Length": double,
    "Height": double,
    "Width": double,
    "Unit": "Meters"|"Feet"
  },
  "Weight": {
    "Total": double,
    "Unit": "Kilograms"|"Pounds"
  }
}
```

`--arrival-time` (timestamp)

Specifies the desired time of arrival. Uses the given time to calculate the route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.

### Note

ArrivalTime is not supported Esri.

`--optimize-for` (string)

Specifies the distance to optimize for when calculating a route.

Possible values:

- `FastestRoute`
- `ShortestRoute`

`--key` (string)

The optional [API key](https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html) to authorize the request.

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

Legs -> (list)

Contains details about each path between a pair of positions included along a route such as: `StartPosition` , `EndPosition` , `Distance` , `DurationSeconds` , `Geometry` , and `Steps` . The number of legs returned corresponds to one fewer than the total number of positions in the request.

For example, a route with a departure position and destination position returns one leg with the positions [snapped to a nearby road](https://docs.aws.amazon.com/location/latest/developerguide/snap-to-nearby-road.html) :

- The `StartPosition` is the departure position.
- The `EndPosition` is the destination position.

A route with a waypoint between the departure and destination position returns two legs with the positions snapped to a nearby road:

- Leg 1: The `StartPosition` is the departure position . The `EndPosition` is the waypoint positon.
- Leg 2: The `StartPosition` is the waypoint position. The `EndPosition` is the destination position.

(structure)

Contains the calculated routeâs details for each path between a pair of positions. The number of legs returned corresponds to one fewer than the total number of positions in the request.

For example, a route with a departure position and destination position returns one leg with the positions [snapped to a nearby road](https://docs.aws.amazon.com/location/latest/developerguide/snap-to-nearby-road.html) :

- The `StartPosition` is the departure position.
- The `EndPosition` is the destination position.

A route with a waypoint between the departure and destination position returns two legs with the positions snapped to a nearby road:

- Leg 1: The `StartPosition` is the departure position . The `EndPosition` is the waypoint positon.
- Leg 2: The `StartPosition` is the waypoint position. The `EndPosition` is the destination position.

StartPosition -> (list)

The starting position of the leg. Follows the format `[longitude,latitude]` .

### Note

If the `StartPosition` isnât located on a road, itâs [snapped to a nearby road](https://docs.aws.amazon.com/location/latest/developerguide/snap-to-nearby-road.html) .

(double)

EndPosition -> (list)

The terminating position of the leg. Follows the format `[longitude,latitude]` .

### Note

If the `EndPosition` isnât located on a road, itâs [snapped to a nearby road](https://docs.aws.amazon.com/location/latest/developerguide/nap-to-nearby-road.html) .

(double)

Distance -> (double)

The distance between the legâs `StartPosition` and `EndPosition` along a calculated route.

- The default measurement is `Kilometers` unless the request specifies a `DistanceUnit` of `Miles` .

DurationSeconds -> (double)

The estimated travel time between the legâs `StartPosition` and `EndPosition` . The travel mode and departure time that you specify in the request determines the calculated time.

Geometry -> (structure)

Contains the calculated routeâs path as a linestring geometry.

LineString -> (list)

An ordered list of positions used to plot a route on a map.

The first position is closest to the start position for the leg, and the last position is the closest to the end position for the leg.

- For example, `[[-123.117, 49.284],[-123.115, 49.285],[-123.115, 49.285]]`

(list)

(double)

Steps -> (list)

Contains a list of steps, which represent subsections of a leg. Each step provides instructions for how to move to the next step in the leg such as the stepâs start position, end position, travel distance, travel duration, and geometry offset.

(structure)

Represents an element of a leg within a route. A step contains instructions for how to move to the next step in the leg.

StartPosition -> (list)

The starting position of a step. If the position is the first step in the leg, this position is the same as the start position of the leg.

(double)

EndPosition -> (list)

The end position of a step. If the position the last step in the leg, this position is the same as the end position of the leg.

(double)

Distance -> (double)

The travel distance between the stepâs `StartPosition` and `EndPosition` .

DurationSeconds -> (double)

The estimated travel time, in seconds, from the stepâs `StartPosition` to the `EndPosition` . . The travel mode and departure time that you specify in the request determines the calculated time.

GeometryOffset -> (integer)

Represents the start position, or index, in a sequence of steps within the legâs line string geometry. For example, the index of the first step in a leg geometry is `0` .

Included in the response for queries that set `IncludeLegGeometry` to `True` .

Summary -> (structure)

Contains information about the whole route, such as: `RouteBBox` , `DataSource` , `Distance` , `DistanceUnit` , and `DurationSeconds` .

RouteBBox -> (list)

Specifies a geographical box surrounding a route. Used to zoom into a route when displaying it in a map. For example, `[min x, min y, max x, max y]` .

The first 2 `bbox` parameters describe the lower southwest corner:

- The first `bbox` position is the X coordinate or longitude of the lower southwest corner.
- The second `bbox` position is the Y coordinate or latitude of the lower southwest corner.

The next 2 `bbox` parameters describe the upper northeast corner:

- The third `bbox` position is the X coordinate, or longitude of the upper northeast corner.
- The fourth `bbox` position is the Y coordinate, or latitude of the upper northeast corner.

(double)

DataSource -> (string)

The data provider of traffic and road network data used to calculate the route. Indicates one of the available providers:

- `Esri`
- `Grab`
- `Here`

For more information about data providers, see [Amazon Location Service data providers](https://docs.aws.amazon.com/location/latest/developerguide/what-is-data-provider.html) .

Distance -> (double)

The total distance covered by the route. The sum of the distance travelled between every stop on the route.

### Note

If Esri is the data source for the route calculator, the route distance canât be greater than 400 km. If the route exceeds 400 km, the response is a `400 RoutesValidationException` error.

DurationSeconds -> (double)

The total travel time for the route measured in seconds. The sum of the travel time between every stop on the route.

DistanceUnit -> (string)

The unit of measurement for route distances.