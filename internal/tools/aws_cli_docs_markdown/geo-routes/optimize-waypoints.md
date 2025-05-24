# optimize-waypointsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-routes/optimize-waypoints.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-routes/optimize-waypoints.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [geo-routes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-routes/index.html#cli-aws-geo-routes) ]

# optimize-waypoints

## Description

`OptimizeWaypoints` calculates the optimal order to travel between a set of waypoints to minimize either the travel time or the distance travelled during the journey, based on road network restrictions and the traffic pattern data.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/geo-routes-2020-11-19/OptimizeWaypoints)

## Synopsis

```
optimize-waypoints
[--avoid <value>]
[--clustering <value>]
[--departure-time <value>]
[--destination <value>]
[--destination-options <value>]
[--driver <value>]
[--exclude <value>]
[--key <value>]
[--optimize-sequencing-for <value>]
--origin <value>
[--origin-options <value>]
[--traffic <value>]
[--travel-mode <value>]
[--travel-mode-options <value>]
[--waypoints <value>]
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

`--avoid` (structure)

Features that are avoided. Avoidance is on a best-case basis. If an avoidance canât be satisfied for a particular case, this setting is ignored.

Areas -> (list)

Areas to be avoided.

(structure)

The area to be avoided.

Geometry -> (structure)

Geometry of the area to be avoided.

BoundingBox -> (list)

Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.

(double)

CarShuttleTrains -> (boolean)

Avoidance options for cars-shuttles-trains.

ControlledAccessHighways -> (boolean)

Avoid controlled access highways while calculating the route.

DirtRoads -> (boolean)

Avoid dirt roads while calculating the route.

Ferries -> (boolean)

Avoidance options for ferries.

TollRoads -> (boolean)

Avoids roads where the specified toll transponders are the only mode of payment.

Tunnels -> (boolean)

Avoid tunnels while calculating the route.

UTurns -> (boolean)

Avoid U-turns for calculation on highways and motorways.

JSON Syntax:

```
{
  "Areas": [
    {
      "Geometry": {
        "BoundingBox": [double, ...]
      }
    }
    ...
  ],
  "CarShuttleTrains": true|false,
  "ControlledAccessHighways": true|false,
  "DirtRoads": true|false,
  "Ferries": true|false,
  "TollRoads": true|false,
  "Tunnels": true|false,
  "UTurns": true|false
}
```

`--clustering` (structure)

Clustering allows you to specify how nearby waypoints can be clustered to improve the optimized sequence.

Algorithm -> (string)

The algorithm to be used. `DrivingDistance` assigns all the waypoints that are within driving distance of each other into a single cluster. `TopologySegment` assigns all the waypoints that are within the same topology segment into a single cluster. A Topology segment is a linear stretch of road between two junctions.

DrivingDistanceOptions -> (structure)

Driving distance options to be used when the clustering algorithm is DrivingDistance.

DrivingDistance -> (long)

DrivingDistance assigns all the waypoints that are within driving distance of each other into a single cluster.

Shorthand Syntax:

```
Algorithm=string,DrivingDistanceOptions={DrivingDistance=long}
```

JSON Syntax:

```
{
  "Algorithm": "DrivingDistance"|"TopologySegment",
  "DrivingDistanceOptions": {
    "DrivingDistance": long
  }
}
```

`--departure-time` (string)

Departure time from the waypoint.

Time format:`YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`

Examples:

`2020-04-22T17:57:24Z`

`2020-04-22T17:57:24+02:00`

`--destination` (list)

The final position for the route in the World Geodetic System (WGS 84) format: `[longitude, latitude]` .

(double)

Syntax:

```
double double ...
```

`--destination-options` (structure)

Destination related options.

AccessHours -> (structure)

Access hours corresponding to when a waypoint can be visited.

From -> (structure)

Contains the ID of the starting waypoint in this connection.

DayOfWeek -> (string)

Day of the week.

TimeOfDay -> (string)

Time of the day.

To -> (structure)

Contains the ID of the ending waypoint in this connection.

DayOfWeek -> (string)

Day of the week.

TimeOfDay -> (string)

Time of the day.

AppointmentTime -> (string)

Appointment time at the destination.

Heading -> (double)

GPS Heading at the position.

Id -> (string)

The waypoint Id.

ServiceDuration -> (long)

Service time spent at the destination. At an appointment, the service time should be the appointment duration.

**Unit** : `seconds`

SideOfStreet -> (structure)

Options to configure matching the provided position to a side of the street.

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

UseWith -> (string)

Strategy that defines when the side of street position should be used. AnyStreet will always use the provided position.

Default Value: `DividedStreetOnly`

Shorthand Syntax:

```
AccessHours={From={DayOfWeek=string,TimeOfDay=string},To={DayOfWeek=string,TimeOfDay=string}},AppointmentTime=string,Heading=double,Id=string,ServiceDuration=long,SideOfStreet={Position=[double,double],UseWith=string}
```

JSON Syntax:

```
{
  "AccessHours": {
    "From": {
      "DayOfWeek": "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday"|"Saturday"|"Sunday",
      "TimeOfDay": "string"
    },
    "To": {
      "DayOfWeek": "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday"|"Saturday"|"Sunday",
      "TimeOfDay": "string"
    }
  },
  "AppointmentTime": "string",
  "Heading": double,
  "Id": "string",
  "ServiceDuration": long,
  "SideOfStreet": {
    "Position": [double, ...],
    "UseWith": "AnyStreet"|"DividedStreetOnly"
  }
}
```

`--driver` (structure)

Driver related options.

RestCycles -> (structure)

Driver work-rest schedules defined by a short and long cycle. A rest needs to be taken after the short work duration. The short cycle can be repeated until you hit the long work duration, at which point the long rest duration should be taken before restarting.

LongCycle -> (structure)

Long cycle for a driver work-rest schedule.

RestDuration -> (long)

Resting phase of the cycle.

**Unit** : `seconds`

WorkDuration -> (long)

Working phase of the cycle.

**Unit** : `seconds`

ShortCycle -> (structure)

Short cycle for a driver work-rest schedule

RestDuration -> (long)

Resting phase of the cycle.

**Unit** : `seconds`

WorkDuration -> (long)

Working phase of the cycle.

**Unit** : `seconds`

RestProfile -> (structure)

Pre defined rest profiles for a driver schedule. The only currently supported profile is EU.

Profile -> (string)

Pre defined rest profiles for a driver schedule. The only currently supported profile is EU.

TreatServiceTimeAs -> (string)

If the service time provided at a waypoint/destination should be considered as rest or work. This contributes to the total time breakdown returned within the response.

Shorthand Syntax:

```
RestCycles={LongCycle={RestDuration=long,WorkDuration=long},ShortCycle={RestDuration=long,WorkDuration=long}},RestProfile={Profile=string},TreatServiceTimeAs=string
```

JSON Syntax:

```
{
  "RestCycles": {
    "LongCycle": {
      "RestDuration": long,
      "WorkDuration": long
    },
    "ShortCycle": {
      "RestDuration": long,
      "WorkDuration": long
    }
  },
  "RestProfile": {
    "Profile": "string"
  },
  "TreatServiceTimeAs": "Rest"|"Work"
}
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

`--optimize-sequencing-for` (string)

Specifies the optimization criteria for the calculated sequence.

Default Value: `FastestRoute` .

Possible values:

- `FastestRoute`
- `ShortestRoute`

`--origin` (list)

The start position for the route.

(double)

Syntax:

```
double double ...
```

`--origin-options` (structure)

Origin related options.

Id -> (string)

The Origin Id.

Shorthand Syntax:

```
Id=string
```

JSON Syntax:

```
{
  "Id": "string"
}
```

`--traffic` (structure)

Traffic-related options.

Usage -> (string)

Determines if traffic should be used or ignored while calculating the route.

Default Value: `UseTrafficData`

Shorthand Syntax:

```
Usage=string
```

JSON Syntax:

```
{
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

Pedestrian -> (structure)

Travel mode options when the provided travel mode is âPedestrianâ

Speed -> (double)

Walking speed.

**Unit** : `KilometersPerHour`

Truck -> (structure)

Travel mode options when the provided travel mode is âTruckâ

GrossWeight -> (long)

Gross weight of the vehicle including trailers, and goods at capacity.

**Unit** : `Kilograms`

HazardousCargos -> (list)

List of Hazardous cargo contained in the vehicle.

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

Width -> (long)

Width of the vehicle.

**Unit** : `centimeters`

Shorthand Syntax:

```
Pedestrian={Speed=double},Truck={GrossWeight=long,HazardousCargos=[string,string],Height=long,Length=long,Trailer={TrailerCount=integer},TruckType=string,TunnelRestrictionCode=string,WeightPerAxle=long,Width=long}
```

JSON Syntax:

```
{
  "Pedestrian": {
    "Speed": double
  },
  "Truck": {
    "GrossWeight": long,
    "HazardousCargos": ["Combustible"|"Corrosive"|"Explosive"|"Flammable"|"Gas"|"HarmfulToWater"|"Organic"|"Other"|"Poison"|"PoisonousInhalation"|"Radioactive", ...],
    "Height": long,
    "Length": long,
    "Trailer": {
      "TrailerCount": integer
    },
    "TruckType": "StraightTruck"|"Tractor",
    "TunnelRestrictionCode": "string",
    "WeightPerAxle": long,
    "Width": long
  }
}
```

`--waypoints` (list)

List of waypoints between the `Origin` and `Destination` .

(structure)

Waypoint between the Origin and Destination.

AccessHours -> (structure)

Access hours corresponding to when a waypoint can be visited.

From -> (structure)

Contains the ID of the starting waypoint in this connection.

DayOfWeek -> (string)

Day of the week.

TimeOfDay -> (string)

Time of the day.

To -> (structure)

Contains the ID of the ending waypoint in this connection.

DayOfWeek -> (string)

Day of the week.

TimeOfDay -> (string)

Time of the day.

AppointmentTime -> (string)

Appointment time at the waypoint.

Before -> (list)

Constraint defining what waypoints are to be visited after this waypoint.

(integer)

Heading -> (double)

GPS Heading at the position.

Id -> (string)

The waypoint Id.

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

ServiceDuration -> (long)

Service time spent at the waypoint. At an appointment, the service time should be the appointment duration.

**Unit** : `seconds`

SideOfStreet -> (structure)

Options to configure matching the provided position to a side of the street.

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

UseWith -> (string)

Strategy that defines when the side of street position should be used. AnyStreet will always use the provided position.

Default Value: `DividedStreetOnly`

Shorthand Syntax:

```
AccessHours={From={DayOfWeek=string,TimeOfDay=string},To={DayOfWeek=string,TimeOfDay=string}},AppointmentTime=string,Before=integer,integer,Heading=double,Id=string,Position=double,double,ServiceDuration=long,SideOfStreet={Position=[double,double],UseWith=string} ...
```

JSON Syntax:

```
[
  {
    "AccessHours": {
      "From": {
        "DayOfWeek": "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday"|"Saturday"|"Sunday",
        "TimeOfDay": "string"
      },
      "To": {
        "DayOfWeek": "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday"|"Saturday"|"Sunday",
        "TimeOfDay": "string"
      }
    },
    "AppointmentTime": "string",
    "Before": [integer, ...],
    "Heading": double,
    "Id": "string",
    "Position": [double, ...],
    "ServiceDuration": long,
    "SideOfStreet": {
      "Position": [double, ...],
      "UseWith": "AnyStreet"|"DividedStreetOnly"
    }
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

Connections -> (list)

Details about the connection from one waypoint to the next, within the optimized sequence.

(structure)

This contains information such as distance and duration from one waypoint to the next waypoint in the sequence.

Distance -> (long)

Distance of the step.

From -> (string)

contains the ID of the starting waypoint in this connection.

RestDuration -> (long)

Resting time before the driver can continue driving.

To -> (string)

Contains the ID of the ending waypoint in this connection.

TravelDuration -> (long)

Total duration.

**Unit** : `seconds`

WaitDuration -> (long)

Duration of a wait step.

**Unit** : `seconds`

Distance -> (long)

Overall distance to travel the whole sequence.

Duration -> (long)

Overall duration to travel the whole sequence.

**Unit** : `seconds`

ImpedingWaypoints -> (list)

Returns waypoints that caused the optimization problem to fail, and the constraints that were unsatisfied leading to the failure.

(structure)

The impeding waypoint.

FailedConstraints -> (list)

Failed constraints for an impeding waypoint.

(structure)

The failed constraint.

Constraint -> (string)

The failed constraint.

Reason -> (string)

Reason for the failed constraint.

Id -> (string)

The waypoint Id.

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

OptimizedWaypoints -> (list)

Waypoints in the order of the optimized sequence.

(structure)

The optimized waypoint.

ArrivalTime -> (string)

Estimated time of arrival at the destination.

Time format:`YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`

Examples:

`2020-04-22T17:57:24Z`

`2020-04-22T17:57:24+02:00`

ClusterIndex -> (integer)

Index of the cluster the waypoint is associated with. The index is included in the response only if clustering was performed while processing the request.

DepartureTime -> (string)

Estimated time of departure from thr origin.

Time format:`YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`

Examples:

`2020-04-22T17:57:24Z`

`2020-04-22T17:57:24+02:00`

Id -> (string)

The waypoint Id.

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

PricingBucket -> (string)

The pricing bucket for which the query is charged at.

TimeBreakdown -> (structure)

Time breakdown for the sequence.

RestDuration -> (long)

Resting phase of the cycle.

**Unit** : `seconds`

ServiceDuration -> (long)

Service time spent at the destination. At an appointment, the service time should be the appointment duration.

**Unit** : `seconds`

TravelDuration -> (long)

Traveling phase of the cycle.

**Unit** : `seconds`

WaitDuration -> (long)

Waiting phase of the cycle.

**Unit** : `seconds`