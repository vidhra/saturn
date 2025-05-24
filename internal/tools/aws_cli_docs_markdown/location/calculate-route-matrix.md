# calculate-route-matrixÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/calculate-route-matrix.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/calculate-route-matrix.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [location](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/index.html#cli-aws-location) ]

# calculate-route-matrix

## Description

[Calculates a route matrix](https://docs.aws.amazon.com/location/latest/developerguide/calculate-route-matrix.html) given the following required parameters: `DeparturePositions` and `DestinationPositions` . `CalculateRouteMatrix` calculates routes and returns the travel time and travel distance from each departure position to each destination position in the request. For example, given departure positions A and B, and destination positions X and Y, `CalculateRouteMatrix` will return time and distance for routes from A to X, A to Y, B to X, and B to Y (in that order). The number of results returned (and routes calculated) will be the number of `DeparturePositions` times the number of `DestinationPositions` .

### Note

Your account is charged for each route calculated, not the number of requests.

Requires that you first [create a route calculator resource](https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CreateRouteCalculator.html) .

By default, a request that doesnât specify a departure time uses the best time of day to travel with the best traffic conditions when calculating routes.

Additional options include:

- [Specifying a departure time](https://docs.aws.amazon.com/location/latest/developerguide/departure-time.html) using either `DepartureTime` or `DepartNow` . This calculates routes based on predictive traffic data at the given time.

### Note

You canât specify both `DepartureTime` and `DepartNow` in a single request. Specifying both parameters returns a validation error.

- [Specifying a travel mode](https://docs.aws.amazon.com/location/latest/developerguide/travel-mode.html) using TravelMode sets the transportation mode used to calculate the routes. This also lets you specify additional route preferences in `CarModeOptions` if traveling by `Car` , or `TruckModeOptions` if traveling by `Truck` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/location-2020-11-19/CalculateRouteMatrix)

## Synopsis

```
calculate-route-matrix
--calculator-name <value>
--departure-positions <value>
--destination-positions <value>
[--travel-mode <value>]
[--departure-time <value>]
[--depart-now | --no-depart-now]
[--distance-unit <value>]
[--car-mode-options <value>]
[--truck-mode-options <value>]
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

The name of the route calculator resource that you want to use to calculate the route matrix.

`--departure-positions` (list)

The list of departure (origin) positions for the route matrix. An array of points, each of which is itself a 2-value array defined in [WGS 84](https://earth-info.nga.mil/GandG/wgs84/index.html) format: `[longitude, latitude]` . For example, `[-123.115, 49.285]` .

### Warning

Depending on the data provider selected in the route calculator resource there may be additional restrictions on the inputs you can choose. See [Position restrictions](https://docs.aws.amazon.com/location/latest/developerguide/calculate-route-matrix.html#matrix-routing-position-limits) in the *Amazon Location Service Developer Guide* .

### Note

For route calculators that use Esri as the data provider, if you specify a departure thatâs not located on a road, Amazon Location [moves the position to the nearest road](https://docs.aws.amazon.com/location/latest/developerguide/snap-to-nearby-road.html) . The snapped value is available in the result in `SnappedDeparturePositions` .

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

`--destination-positions` (list)

The list of destination positions for the route matrix. An array of points, each of which is itself a 2-value array defined in [WGS 84](https://earth-info.nga.mil/GandG/wgs84/index.html) format: `[longitude, latitude]` . For example, `[-122.339, 47.615]`

### Warning

Depending on the data provider selected in the route calculator resource there may be additional restrictions on the inputs you can choose. See [Position restrictions](https://docs.aws.amazon.com/location/latest/developerguide/calculate-route-matrix.html#matrix-routing-position-limits) in the *Amazon Location Service Developer Guide* .

### Note

For route calculators that use Esri as the data provider, if you specify a destination thatâs not located on a road, Amazon Location [moves the position to the nearest road](https://docs.aws.amazon.com/location/latest/developerguide/snap-to-nearby-road.html) . The snapped value is available in the result in `SnappedDestinationPositions` .

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

Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.

The `TravelMode` you specify also determines how you specify route preferences:

- If traveling by `Car` use the `CarModeOptions` parameter.
- If traveling by `Truck` use the `TruckModeOptions` parameter.

### Note

`Bicycle` or `Motorcycle` are only valid when using `Grab` as a data provider, and only within Southeast Asia.

`Truck` is not available for Grab.

For more information about using Grab as a data provider, see [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/grab.html) in the *Amazon Location Service Developer Guide* .

Default Value: `Car`

Possible values:

- `Car`
- `Truck`
- `Walking`
- `Bicycle`
- `Motorcycle`

`--departure-time` (timestamp)

Specifies the desired time of departure. Uses the given time to calculate the route matrix. You canât set both `DepartureTime` and `DepartNow` . If neither is set, the best time of day to travel with the best traffic conditions is used to calculate the route matrix.

### Note

Setting a departure time in the past returns a `400 ValidationException` error.

- In [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ` . For example, `2020â07-2T12:15:20.000Z+01:00`

`--depart-now` | `--no-depart-now` (boolean)

Sets the time of departure as the current time. Uses the current time to calculate the route matrix. You canât set both `DepartureTime` and `DepartNow` . If neither is set, the best time of day to travel with the best traffic conditions is used to calculate the route matrix.

Default Value: `false`

Valid Values: `false` | `true`

`--distance-unit` (string)

Set the unit system to specify the distance.

Default Value: `Kilometers`

Possible values:

- `Kilometers`
- `Miles`

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

RouteMatrix -> (list)

The calculated route matrix containing the results for all pairs of `DeparturePositions` to `DestinationPositions` . Each row corresponds to one entry in `DeparturePositions` . Each entry in the row corresponds to the route from that entry in `DeparturePositions` to an entry in `DestinationPositions` .

(list)

(structure)

The result for the calculated route of one `DeparturePosition` `DestinationPosition` pair.

Distance -> (double)

The total distance of travel for the route.

DurationSeconds -> (double)

The expected duration of travel for the route.

Error -> (structure)

An error corresponding to the calculation of a route between the `DeparturePosition` and `DestinationPosition` .

Code -> (string)

The type of error which occurred for the route calculation.

Message -> (string)

A message about the error that occurred for the route calculation.

SnappedDeparturePositions -> (list)

For routes calculated using an Esri route calculator resource, departure positions are snapped to the closest road. For Esri route calculator resources, this returns the list of departure/origin positions used for calculation of the `RouteMatrix` .

(list)

(double)

SnappedDestinationPositions -> (list)

The list of destination positions for the route matrix used for calculation of the `RouteMatrix` .

(list)

(double)

Summary -> (structure)

Contains information about the route matrix, `DataSource` , `DistanceUnit` , `RouteCount` and `ErrorCount` .

DataSource -> (string)

The data provider of traffic and road network data used to calculate the routes. Indicates one of the available providers:

- `Esri`
- `Grab`
- `Here`

For more information about data providers, see [Amazon Location Service data providers](https://docs.aws.amazon.com/location/latest/developerguide/what-is-data-provider.html) .

RouteCount -> (integer)

The count of cells in the route matrix. Equal to the number of `DeparturePositions` multiplied by the number of `DestinationPositions` .

ErrorCount -> (integer)

The count of error results in the route matrix. If this number is 0, all routes were calculated successfully.

DistanceUnit -> (string)

The unit of measurement for route distances.