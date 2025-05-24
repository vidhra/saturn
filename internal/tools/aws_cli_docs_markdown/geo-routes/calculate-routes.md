# calculate-routesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-routes/calculate-routes.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-routes/calculate-routes.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [geo-routes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-routes/index.html#cli-aws-geo-routes) ]

# calculate-routes

## Description

`CalculateRoutes` computes routes given the following required parameters: `Origin` and `Destination` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/geo-routes-2020-11-19/CalculateRoutes)

## Synopsis

```
calculate-routes
[--allow <value>]
[--arrival-time <value>]
[--avoid <value>]
[--depart-now | --no-depart-now]
[--departure-time <value>]
--destination <value>
[--destination-options <value>]
[--driver <value>]
[--exclude <value>]
[--instructions-measurement-system <value>]
[--key <value>]
[--languages <value>]
[--leg-additional-features <value>]
[--leg-geometry-format <value>]
[--max-alternatives <value>]
[--optimize-routing-for <value>]
--origin <value>
[--origin-options <value>]
[--span-additional-features <value>]
[--tolls <value>]
[--traffic <value>]
[--travel-mode <value>]
[--travel-mode-options <value>]
[--travel-step-type <value>]
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

`--arrival-time` (string)

Time of arrival at the destination.

Time format:`YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`

Examples:

`2020-04-22T17:57:24Z`

`2020-04-22T17:57:24+02:00`

`--avoid` (structure)

Features that are avoided while calculating a route. Avoidance is on a best-case basis. If an avoidance canât be satisfied for a particular case, it violates the avoidance and the returned response produces a notice for the violation.

Areas -> (list)

Areas to be avoided.

(structure)

Areas to be avoided.

Except -> (list)

Exceptions to the provided avoidance geometry, to be included while calculating the route.

(structure)

Geometry of the area to be avoided.

Corridor -> (structure)

Geometry defined as a corridor - a LineString with a radius that defines the width of the corridor.

LineString -> (list)

An ordered list of positions used to plot a route on a map.

### Note

LineString and Polyline are mutually exclusive properties.

(list)

(double)

Radius -> (integer)

Radius that defines the width of the corridor.

BoundingBox -> (list)

Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.

(double)

Polygon -> (list)

Geometry defined as a polygon with only one linear ring.

(list)

(list)

(double)

PolylineCorridor -> (structure)

Geometry defined as an encoded corridor - an encoded polyline with a radius that defines the width of the corridor.

Polyline -> (string)

An ordered list of positions used to plot a route on a map in a lossy compression format.

### Note

LineString and Polyline are mutually exclusive properties.

Radius -> (integer)

Considers all roads within the provided radius to match the provided destination to. The roads that are considered are determined by the provided Strategy.

**Unit** : `Meters`

PolylinePolygon -> (list)

A list of Isoline PolylinePolygon, for each isoline PolylinePolygon, it contains PolylinePolygon of the first linear ring (the outer ring) and from 2nd item to the last item (the inner rings). For more information on polyline encoding, see [https://github.com/heremaps/flexiblepolyline/blob/master/README.md](https://github.com/heremaps/flexiblepolyline/blob/master/README.md) .

(string)

Geometry -> (structure)

Geometry of the area to be avoided.

Corridor -> (structure)

Geometry defined as a corridor - a LineString with a radius that defines the width of the corridor.

LineString -> (list)

An ordered list of positions used to plot a route on a map.

### Note

LineString and Polyline are mutually exclusive properties.

(list)

(double)

Radius -> (integer)

Radius that defines the width of the corridor.

BoundingBox -> (list)

Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.

(double)

Polygon -> (list)

Geometry defined as a polygon with only one linear ring.

(list)

(list)

(double)

PolylineCorridor -> (structure)

Geometry defined as an encoded corridor - an encoded polyline with a radius that defines the width of the corridor.

Polyline -> (string)

An ordered list of positions used to plot a route on a map in a lossy compression format.

### Note

LineString and Polyline are mutually exclusive properties.

Radius -> (integer)

Considers all roads within the provided radius to match the provided destination to. The roads that are considered are determined by the provided Strategy.

**Unit** : `Meters`

PolylinePolygon -> (list)

A list of Isoline PolylinePolygon, for each isoline PolylinePolygon, it contains PolylinePolygon of the first linear ring (the outer ring) and from 2nd item to the last item (the inner rings). For more information on polyline encoding, see [https://github.com/heremaps/flexiblepolyline/blob/master/README.md](https://github.com/heremaps/flexiblepolyline/blob/master/README.md) .

(string)

CarShuttleTrains -> (boolean)

Avoid car-shuttle-trains while calculating the route.

ControlledAccessHighways -> (boolean)

Avoid controlled access highways while calculating the route.

DirtRoads -> (boolean)

Avoid dirt roads while calculating the route.

Ferries -> (boolean)

Avoid ferries while calculating the route.

SeasonalClosure -> (boolean)

Avoid roads that have seasonal closure while calculating the route.

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
      "Except": [
        {
          "Corridor": {
            "LineString": [
              [double, ...]
              ...
            ],
            "Radius": integer
          },
          "BoundingBox": [double, ...],
          "Polygon": [
            [
              [double, ...]
              ...
            ]
            ...
          ],
          "PolylineCorridor": {
            "Polyline": "string",
            "Radius": integer
          },
          "PolylinePolygon": ["string", ...]
        }
        ...
      ],
      "Geometry": {
        "Corridor": {
          "LineString": [
            [double, ...]
            ...
          ],
          "Radius": integer
        },
        "BoundingBox": [double, ...],
        "Polygon": [
          [
            [double, ...]
            ...
          ]
          ...
        ],
        "PolylineCorridor": {
          "Polyline": "string",
          "Radius": integer
        },
        "PolylinePolygon": ["string", ...]
      }
    }
    ...
  ],
  "CarShuttleTrains": true|false,
  "ControlledAccessHighways": true|false,
  "DirtRoads": true|false,
  "Ferries": true|false,
  "SeasonalClosure": true|false,
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

`--destination` (list)

The final position for the route. In the World Geodetic System (WGS 84) format: `[longitude, latitude]` .

(double)

Syntax:

```
double double ...
```

`--destination-options` (structure)

Destination related options.

AvoidActionsForDistance -> (long)

Avoids actions for the provided distance. This is typically to consider for users in moving vehicles who may not have sufficient time to make an action at an origin or a destination.

AvoidUTurns -> (boolean)

Avoid U-turns for calculation on highways and motorways.

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

Strategy that defines when the side of street position should be used.

Default Value: `DividedStreetOnly`

StopDuration -> (long)

Duration of the stop.

**Unit** : `seconds`

Shorthand Syntax:

```
AvoidActionsForDistance=long,AvoidUTurns=boolean,Heading=double,Matching={NameHint=string,OnRoadThreshold=long,Radius=long,Strategy=string},SideOfStreet={Position=[double,double],UseWith=string},StopDuration=long
```

JSON Syntax:

```
{
  "AvoidActionsForDistance": long,
  "AvoidUTurns": true|false,
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
  },
  "StopDuration": long
}
```

`--driver` (structure)

Driver related options.

Schedule -> (list)

Driver work-rest schedule. Stops are added to fulfil the provided rest schedule.

(structure)

Interval of the driver work-rest schedule. Stops are added to fulfil the provided rest schedule.

DriveDuration -> (long)

Maximum allowed driving time before stopping to rest.

**Unit** : `seconds`

RestDuration -> (long)

Resting time before the driver can continue driving.

**Unit** : `seconds`

Shorthand Syntax:

```
Schedule=[{DriveDuration=long,RestDuration=long},{DriveDuration=long,RestDuration=long}]
```

JSON Syntax:

```
{
  "Schedule": [
    {
      "DriveDuration": long,
      "RestDuration": long
    }
    ...
  ]
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

`--instructions-measurement-system` (string)

Measurement system to be used for instructions within steps in the response.

Possible values:

- `Metric`
- `Imperial`

`--key` (string)

Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.

`--languages` (list)

List of languages for instructions within steps in the response.

### Note

Instructions in the requested language are returned only if they are available.

(string)

Syntax:

```
"string" "string" ...
```

`--leg-additional-features` (list)

A list of optional additional parameters such as timezone that can be requested for each result.

- `Elevation` : Retrieves the elevation information for each location.
- `Incidents` : Provides information on traffic incidents along the route.
- `PassThroughWaypoints` : Indicates waypoints that are passed through without stopping.
- `Summary` : Returns a summary of the route, including distance and duration.
- `Tolls` : Supplies toll cost information along the route.
- `TravelStepInstructions` : Provides step-by-step instructions for travel along the route.
- `TruckRoadTypes` : Returns information about road types suitable for trucks.
- `TypicalDuration` : Gives typical travel duration based on historical data.
- `Zones` : Specifies the time zone information for each waypoint.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  Elevation
  Incidents
  PassThroughWaypoints
  Summary
  Tolls
  TravelStepInstructions
  TruckRoadTypes
  TypicalDuration
  Zones
```

`--leg-geometry-format` (string)

Specifies the format of the geometry returned for each leg of the route. You can choose between two different geometry encoding formats.

`FlexiblePolyline` : A compact and precise encoding format for the leg geometry. For more information on the format, see the GitHub repository for ` `FlexiblePolyline` [https://github.com/heremaps/flexible](https://github.com/heremaps/flexible)-polyline`__ .

`Simple` : A less compact encoding, which is easier to decode but may be less precise and result in larger payloads.

Possible values:

- `FlexiblePolyline`
- `Simple`

`--max-alternatives` (integer)

Maximum number of alternative routes to be provided in the response, if available.

`--optimize-routing-for` (string)

Specifies the optimization criteria for calculating a route.

Default Value: `FastestRoute`

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

AvoidActionsForDistance -> (long)

Avoids actions for the provided distance. This is typically to consider for users in moving vehicles who may not have sufficient time to make an action at an origin or a destination.

AvoidUTurns -> (boolean)

Avoid U-turns for calculation on highways and motorways.

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

Strategy that defines when the side of street position should be used.

Default Value: `DividedStreetOnly`

Shorthand Syntax:

```
AvoidActionsForDistance=long,AvoidUTurns=boolean,Heading=double,Matching={NameHint=string,OnRoadThreshold=long,Radius=long,Strategy=string},SideOfStreet={Position=[double,double],UseWith=string}
```

JSON Syntax:

```
{
  "AvoidActionsForDistance": long,
  "AvoidUTurns": true|false,
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
}
```

`--span-additional-features` (list)

A list of optional features such as SpeedLimit that can be requested for a Span. A span is a section of a Leg for which the requested features have the same values.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  BestCaseDuration
  CarAccess
  Country
  Distance
  Duration
  DynamicSpeed
  FunctionalClassification
  Gates
  Incidents
  Names
  Notices
  PedestrianAccess
  RailwayCrossings
  Region
  RoadAttributes
  RouteNumbers
  ScooterAccess
  SpeedLimit
  TollSystems
  TruckAccess
  TruckRoadTypes
  TypicalDuration
  Zones
  Consumption
```

`--tolls` (structure)

Toll related options.

AllTransponders -> (boolean)

Specifies if the user has valid transponder with access to all toll systems. This impacts toll calculation, and if true the price with transponders is used.

AllVignettes -> (boolean)

Specifies if the user has valid vignettes with access for all toll roads. If a user has a vignette for a toll road, then toll cost for that road is omitted since no further payment is necessary.

Currency -> (string)

Currency code corresponding to the price. This is the same as Currency specified in the request.

EmissionType -> (structure)

Emission type of the vehicle for toll cost calculation.

**Valid values** : `Euro1, Euro2, Euro3, Euro4, Euro5, Euro6, EuroEev`

Co2EmissionClass -> (string)

The CO 2 emission classes.

Type -> (string)

Type of the emission.

**Valid values** : `Euro1, Euro2, Euro3, Euro4, Euro5, Euro6, EuroEev`

VehicleCategory -> (string)

Vehicle category for toll cost calculation.

Shorthand Syntax:

```
AllTransponders=boolean,AllVignettes=boolean,Currency=string,EmissionType={Co2EmissionClass=string,Type=string},VehicleCategory=string
```

JSON Syntax:

```
{
  "AllTransponders": true|false,
  "AllVignettes": true|false,
  "Currency": "string",
  "EmissionType": {
    "Co2EmissionClass": "string",
    "Type": "string"
  },
  "VehicleCategory": "Minibus"
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

EngineType -> (string)

Engine type of the vehicle.

LicensePlate -> (structure)

The vehicle License Plate.

LastCharacter -> (string)

The last character of the License Plate.

MaxSpeed -> (double)

Maximum speed specified.

**Unit** : `KilometersPerHour`

Occupancy -> (integer)

The number of occupants in the vehicle.

Default Value: `1`

Pedestrian -> (structure)

Travel mode options when the provided travel mode is âPedestrianâ

Speed -> (double)

Walking speed in Kilometers per hour.

Scooter -> (structure)

Travel mode options when the provided travel mode is `Scooter`

### Note

When travel mode is set to `Scooter` , then the avoidance option `ControlledAccessHighways` defaults to `true` .

EngineType -> (string)

Engine type of the vehicle.

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

Truck -> (structure)

Travel mode options when the provided travel mode is âTruckâ

AxleCount -> (integer)

Total number of axles of the vehicle.

EngineType -> (string)

Engine type of the vehicle.

GrossWeight -> (long)

Gross weight of the vehicle including trailers, and goods at capacity.

**Unit** : `Kilograms`

HazardousCargos -> (list)

List of Hazardous cargo contained in the vehicle.

(string)

Height -> (long)

Height of the vehicle.

**Unit** : `centimeters`

HeightAboveFirstAxle -> (long)

Height of the vehicle above its first axle.

**Unit** : `centimeters`

KpraLength -> (long)

Kingpin to rear axle length of the vehicle.

**Unit** : `centimeters`

Length -> (long)

Length of the vehicle.

**Unit** : `c`

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

TireCount -> (integer)

Number of tires on the vehicle.

Trailer -> (structure)

Trailer options corresponding to the vehicle.

AxleCount -> (integer)

Total number of axles of the vehicle.

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

**Unit** : `Kilograms`

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
Car={EngineType=string,LicensePlate={LastCharacter=string},MaxSpeed=double,Occupancy=integer},Pedestrian={Speed=double},Scooter={EngineType=string,LicensePlate={LastCharacter=string},MaxSpeed=double,Occupancy=integer},Truck={AxleCount=integer,EngineType=string,GrossWeight=long,HazardousCargos=[string,string],Height=long,HeightAboveFirstAxle=long,KpraLength=long,Length=long,LicensePlate={LastCharacter=string},MaxSpeed=double,Occupancy=integer,PayloadCapacity=long,TireCount=integer,Trailer={AxleCount=integer,TrailerCount=integer},TruckType=string,TunnelRestrictionCode=string,WeightPerAxle=long,WeightPerAxleGroup={Single=long,Tandem=long,Triple=long,Quad=long,Quint=long},Width=long}
```

JSON Syntax:

```
{
  "Car": {
    "EngineType": "Electric"|"InternalCombustion"|"PluginHybrid",
    "LicensePlate": {
      "LastCharacter": "string"
    },
    "MaxSpeed": double,
    "Occupancy": integer
  },
  "Pedestrian": {
    "Speed": double
  },
  "Scooter": {
    "EngineType": "Electric"|"InternalCombustion"|"PluginHybrid",
    "LicensePlate": {
      "LastCharacter": "string"
    },
    "MaxSpeed": double,
    "Occupancy": integer
  },
  "Truck": {
    "AxleCount": integer,
    "EngineType": "Electric"|"InternalCombustion"|"PluginHybrid",
    "GrossWeight": long,
    "HazardousCargos": ["Combustible"|"Corrosive"|"Explosive"|"Flammable"|"Gas"|"HarmfulToWater"|"Organic"|"Other"|"Poison"|"PoisonousInhalation"|"Radioactive", ...],
    "Height": long,
    "HeightAboveFirstAxle": long,
    "KpraLength": long,
    "Length": long,
    "LicensePlate": {
      "LastCharacter": "string"
    },
    "MaxSpeed": double,
    "Occupancy": integer,
    "PayloadCapacity": long,
    "TireCount": integer,
    "Trailer": {
      "AxleCount": integer,
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

`--travel-step-type` (string)

Type of step returned by the response. Default provides basic steps intended for web based applications. TurnByTurn provides detailed instructions with more granularity intended for a turn based navigation system.

Possible values:

- `Default`
- `TurnByTurn`

`--waypoints` (list)

List of waypoints between the Origin and Destination.

(structure)

Waypoint between the Origin and Destination.

AvoidActionsForDistance -> (long)

Avoids actions for the provided distance. This is typically to consider for users in moving vehicles who may not have sufficient time to make an action at an origin or a destination.

AvoidUTurns -> (boolean)

Avoid U-turns for calculation on highways and motorways.

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

PassThrough -> (boolean)

If the waypoint should not be treated as a stop. If yes, the waypoint is passed through and doesnât split the route into different legs.

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

SideOfStreet -> (structure)

Options to configure matching the provided position to a side of the street.

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

UseWith -> (string)

Strategy that defines when the side of street position should be used.

Default Value: `DividedStreetOnly`

StopDuration -> (long)

Duration of the stop.

**Unit** : `seconds`

Shorthand Syntax:

```
AvoidActionsForDistance=long,AvoidUTurns=boolean,Heading=double,Matching={NameHint=string,OnRoadThreshold=long,Radius=long,Strategy=string},PassThrough=boolean,Position=double,double,SideOfStreet={Position=[double,double],UseWith=string},StopDuration=long ...
```

JSON Syntax:

```
[
  {
    "AvoidActionsForDistance": long,
    "AvoidUTurns": true|false,
    "Heading": double,
    "Matching": {
      "NameHint": "string",
      "OnRoadThreshold": long,
      "Radius": long,
      "Strategy": "MatchAny"|"MatchMostSignificantRoad"
    },
    "PassThrough": true|false,
    "Position": [double, ...],
    "SideOfStreet": {
      "Position": [double, ...],
      "UseWith": "AnyStreet"|"DividedStreetOnly"
    },
    "StopDuration": long
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

LegGeometryFormat -> (string)

Specifies the format of the geometry returned for each leg of the route.

Notices -> (list)

Notices are additional information returned that indicate issues that occurred during route calculation.

(structure)

Notices are additional information returned that indicate issues that occurred during route calculation.

Code -> (string)

Code corresponding to the issue.

Impact -> (string)

Impact corresponding to the issue. While Low impact notices can be safely ignored, High impact notices must be evaluated further to determine the impact.

PricingBucket -> (string)

The pricing bucket for which the query is charged at.

Routes -> (list)

The path from the origin to the destination.

(structure)

The route.

Legs -> (list)

A leg is a section of a route from one waypoint to the next. A leg could be of type Vehicle, Pedestrian or Ferry. Legs of different types could occur together within a single route. For example, a car employing the use of a Ferry will contain Vehicle legs corresponding to journey on land, and Ferry legs corresponding to the journey via Ferry.

(structure)

A leg is a section of a route from one waypoint to the next. A leg could be of type Vehicle, Pedestrian or Ferry. Legs of different types could occur together within a single route. For example, a car employing the use of a Ferry will contain Vehicle legs corresponding to journey on land, and Ferry legs corresponding to the journey via Ferry.

FerryLegDetails -> (structure)

FerryLegDetails is populated when the Leg type is Ferry, and provides additional information that is specific

AfterTravelSteps -> (list)

Steps of a leg that must be performed after the travel portion of the leg.

(structure)

Steps of a leg that must be performed after the travel portion of the leg.

Duration -> (long)

Duration of the step.

**Unit** : `seconds`

Instruction -> (string)

Brief description of the step in the requested language.

### Note

Only available when the TravelStepType is Default.

Type -> (string)

Type of the step.

Arrival -> (structure)

Details corresponding to the arrival for the leg.

Place -> (structure)

The place details.

Name -> (string)

The name of the place.

OriginalPosition -> (list)

Position provided in the request.

(double)

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

WaypointIndex -> (integer)

Index of the waypoint in the request.

Time -> (string)

The time.

BeforeTravelSteps -> (list)

Steps of a leg that must be performed before the travel portion of the leg.

(structure)

Steps of a leg that must be performed before the travel portion of the leg.

Duration -> (long)

Duration of the step.

**Unit** : `seconds`

Instruction -> (string)

Brief description of the step in the requested language.

### Note

Only available when the TravelStepType is Default.

Type -> (string)

Type of the step.

Departure -> (structure)

Details corresponding to the departure for the leg.

Place -> (structure)

The place details.

Name -> (string)

The name of the place.

OriginalPosition -> (list)

Position provided in the request.

(double)

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

WaypointIndex -> (integer)

Index of the waypoint in the request.

Time -> (string)

The time.

Notices -> (list)

Notices are additional information returned that indicate issues that occurred during route calculation.

(structure)

Notices are additional information returned that indicate issues that occurred during route calculation.

Code -> (string)

Code corresponding to the issue.

Impact -> (string)

Impact corresponding to the issue. While Low impact notices can be safely ignored, High impact notices must be evaluated further to determine the impact.

PassThroughWaypoints -> (list)

Waypoints that were passed through during the leg. This includes the waypoints that were configured with the PassThrough option.

(structure)

If the waypoint should be treated as a stop. If yes, the route is split up into different legs around the stop.

GeometryOffset -> (integer)

Offset in the leg geometry corresponding to the start of this step.

Place -> (structure)

The place details.

OriginalPosition -> (list)

Position provided in the request.

(double)

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

WaypointIndex -> (integer)

Index of the waypoint in the request.

RouteName -> (string)

Route name of the ferry line.

Spans -> (list)

Spans that were computed for the requested SpanAdditionalFeatures.

(structure)

Span computed for the requested SpanAdditionalFeatures.

Country -> (string)

3 letter Country code corresponding to the Span.

Distance -> (long)

Distance of the computed span. This feature doesnât split a span, but is always computed on a span split by other properties.

**Unit** : `meters`

Duration -> (long)

Duration of the computed span. This feature doesnât split a span, but is always computed on a span split by other properties.

**Unit** : `seconds`

GeometryOffset -> (integer)

Offset in the leg geometry corresponding to the start of this span.

Names -> (list)

Provides an array of names of the ferry span in available languages.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

Region -> (string)

2-3 letter Region code corresponding to the Span. This is either a province or a state.

Summary -> (structure)

Summarized details of the leg.

Overview -> (structure)

Summarized details for the leg including before travel, travel and after travel steps.

Distance -> (long)

Distance of the step.

Duration -> (long)

Duration of the step.

**Unit** : `seconds`

TravelOnly -> (structure)

Summarized details for the leg including travel steps only. The Distance for the travel only portion of the journey is in meters

Duration -> (long)

Total duration in free flowing traffic, which is the best case or shortest duration possible to cover the leg.

**Unit** : `seconds`

TravelSteps -> (list)

Steps of a leg that must be performed before the travel portion of the leg.

(structure)

Steps of a leg that must be performed during the travel portion of the leg.

Distance -> (long)

Distance of the step.

Duration -> (long)

Duration of the step.

**Unit** : `seconds`

GeometryOffset -> (integer)

Offset in the leg geometry corresponding to the start of this step.

Instruction -> (string)

Brief description of the step in the requested language.

### Note

Only available when the TravelStepType is Default.

Type -> (string)

Type of the step.

Geometry -> (structure)

Geometry of the area to be avoided.

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

Language -> (string)

List of languages for instructions within steps in the response.

PedestrianLegDetails -> (structure)

Details related to the pedestrian leg.

Arrival -> (structure)

Details corresponding to the arrival for the leg.

Place -> (structure)

The place details.

Name -> (string)

The name of the place.

OriginalPosition -> (list)

Position provided in the request.

(double)

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

SideOfStreet -> (string)

Options to configure matching the provided position to a side of the street.

WaypointIndex -> (integer)

Index of the waypoint in the request.

Time -> (string)

The time.

Departure -> (structure)

Details corresponding to the departure for the leg.

Place -> (structure)

The place details.

Name -> (string)

The name of the place.

OriginalPosition -> (list)

Position provided in the request.

(double)

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

SideOfStreet -> (string)

Options to configure matching the provided position to a side of the street.

WaypointIndex -> (integer)

Index of the waypoint in the request.

Time -> (string)

The time.

Notices -> (list)

Notices are additional information returned that indicate issues that occurred during route calculation.

(structure)

Notices are additional information returned that indicate issues that occurred during route calculation.

Code -> (string)

Code corresponding to the issue.

Impact -> (string)

Impact corresponding to the issue. While Low impact notices can be safely ignored, High impact notices must be evaluated further to determine the impact.

PassThroughWaypoints -> (list)

Waypoints that were passed through during the leg. This includes the waypoints that were configured with the PassThrough option.

(structure)

If the waypoint should be treated as a stop. If yes, the route is split up into different legs around the stop.

GeometryOffset -> (integer)

Offset in the leg geometry corresponding to the start of this step.

Place -> (structure)

The place details.

OriginalPosition -> (list)

Position provided in the request.

(double)

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

WaypointIndex -> (integer)

Index of the waypoint in the request.

Spans -> (list)

Spans that were computed for the requested SpanAdditionalFeatures.

(structure)

Span computed for the requested SpanAdditionalFeatures.

BestCaseDuration -> (long)

Duration of the computed span without traffic congestion.

**Unit** : `seconds`

Country -> (string)

3 letter Country code corresponding to the Span.

Distance -> (long)

Distance of the computed span. This feature doesnât split a span, but is always computed on a span split by other properties.

Duration -> (long)

Duration of the computed span. This feature doesnât split a span, but is always computed on a span split by other properties.

**Unit** : `seconds`

DynamicSpeed -> (structure)

Dynamic speed details corresponding to the span.

**Unit** : `KilometersPerHour`

BestCaseSpeed -> (double)

Estimated speed while traversing the span without traffic congestion.

**Unit** : `KilometersPerHour`

TurnDuration -> (long)

Estimated time to turn from this span into the next.

**Unit** : `seconds`

TypicalSpeed -> (double)

Estimated speed while traversing the span under typical traffic congestion.

**Unit** : `KilometersPerHour`

FunctionalClassification -> (integer)

Functional classification of the road segment corresponding to the span.

GeometryOffset -> (integer)

Offset in the leg geometry corresponding to the start of this span.

Incidents -> (list)

Incidents corresponding to the span. These index into the Incidents in the parent Leg.

(integer)

Names -> (list)

Provides an array of names of the pedestrian span in available languages.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

PedestrianAccess -> (list)

Access attributes for a pedestrian corresponding to the span.

(string)

Region -> (string)

2-3 letter Region code corresponding to the Span. This is either a province or a state.

RoadAttributes -> (list)

Attributes for the road segment corresponding to the span.

(string)

RouteNumbers -> (list)

Designated route name or number corresponding to the span.

(structure)

The route number.

Direction -> (string)

Directional identifier of the route.

Language -> (string)

List of languages for instructions corresponding to the route number.

Value -> (string)

The route number.

SpeedLimit -> (structure)

Speed limit details corresponding to the span.

**Unit** : `KilometersPerHour`

MaxSpeed -> (double)

Maximum speed.

**Unit** : `KilometersPerHour`

Unlimited -> (boolean)

If the span doesnât have a speed limit like the Autobahn.

TypicalDuration -> (long)

Duration of the computed span under typical traffic congestion.

**Unit** : `seconds`

Summary -> (structure)

Summarized details of the leg.

Overview -> (structure)

Summarized details for the leg including before travel, travel and after travel steps.

Distance -> (long)

Distance of the step.

Duration -> (long)

Duration of the step.

TravelOnly -> (structure)

Summarized details for the leg including travel steps only. The Distance for the travel only portion of the journey is in meters

Duration -> (long)

Duration of the step.

**Unit** : `seconds`

TravelSteps -> (list)

Steps of a leg that must be performed before the travel portion of the leg.

(structure)

Steps of a leg that must be performed during the travel portion of the leg.

ContinueStepDetails -> (structure)

Details related to the continue step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

CurrentRoad -> (structure)

Details of the current road. See RouteRoad for details of sub-attributes.

RoadName -> (list)

Name of the road (localized).

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

RouteNumber -> (list)

Route number of the road.

(structure)

The route number.

Direction -> (string)

Directional identifier of the route.

Language -> (string)

List of languages for instructions corresponding to the route number.

Value -> (string)

The route number.

Towards -> (list)

Names of destinations that can be reached when traveling on the road.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

Type -> (string)

The type of road.

Distance -> (long)

Distance of the step.

Duration -> (long)

Duration of the step.

**Unit** : `seconds`

ExitNumber -> (list)

Exit number of the road exit, if applicable.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

GeometryOffset -> (integer)

Offset in the leg geometry corresponding to the start of this step.

Instruction -> (string)

Brief description of the step in the requested language.

### Note

Only available when the TravelStepType is Default.

KeepStepDetails -> (structure)

Details that are specific to a Keep step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

SteeringDirection -> (string)

Steering direction for the step.

TurnAngle -> (double)

Angle of the turn.

TurnIntensity -> (string)

Intensity of the turn.

NextRoad -> (structure)

Details of the next road. See RouteRoad for details of sub-attributes.

RoadName -> (list)

Name of the road (localized).

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

RouteNumber -> (list)

Route number of the road.

(structure)

The route number.

Direction -> (string)

Directional identifier of the route.

Language -> (string)

List of languages for instructions corresponding to the route number.

Value -> (string)

The route number.

Towards -> (list)

Names of destinations that can be reached when traveling on the road.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

Type -> (string)

The type of road.

RoundaboutEnterStepDetails -> (structure)

Details that are specific to a Roundabout Enter step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

SteeringDirection -> (string)

Steering direction for the step.

TurnAngle -> (double)

Angle of the turn.

TurnIntensity -> (string)

Intensity of the turn.

RoundaboutExitStepDetails -> (structure)

Details that are specific to a Roundabout Exit step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

RelativeExit -> (integer)

Exit to be taken.

RoundaboutAngle -> (double)

Angle of the roundabout.

SteeringDirection -> (string)

Steering direction for the step.

RoundaboutPassStepDetails -> (structure)

Details that are specific to a Roundabout Pass step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

SteeringDirection -> (string)

Steering direction for the step.

TurnAngle -> (double)

Angle of the turn.

TurnIntensity -> (string)

Intensity of the turn.

Signpost -> (structure)

Sign post information of the action, applicable only for TurnByTurn steps. See RouteSignpost for details of sub-attributes.

Labels -> (list)

Labels present on the sign post.

(structure)

Labels presented on the sign post.

RouteNumber -> (structure)

Route number of the road.

Direction -> (string)

Directional identifier of the route.

Language -> (string)

List of languages for instructions corresponding to the route number.

Value -> (string)

The route number.

Text -> (structure)

The Signpost text.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

TurnStepDetails -> (structure)

Details that are specific to a turn step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

SteeringDirection -> (string)

Steering direction for the step.

TurnAngle -> (double)

Angle of the turn.

TurnIntensity -> (string)

Intensity of the turn.

Type -> (string)

Type of the step.

TravelMode -> (string)

Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.

Default Value: `Car`

Type -> (string)

Type of the leg.

VehicleLegDetails -> (structure)

Details related to the vehicle leg.

Arrival -> (structure)

Details corresponding to the arrival for the leg.

Place -> (structure)

The place details.

Name -> (string)

The name of the place.

OriginalPosition -> (list)

Position provided in the request.

(double)

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

SideOfStreet -> (string)

Options to configure matching the provided position to a side of the street.

WaypointIndex -> (integer)

Index of the waypoint in the request.

Time -> (string)

The time.

Departure -> (structure)

Details corresponding to the departure for the leg.

Place -> (structure)

The place details.

Name -> (string)

The name of the place.

OriginalPosition -> (list)

Position provided in the request.

(double)

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

SideOfStreet -> (string)

Options to configure matching the provided position to a side of the street.

WaypointIndex -> (integer)

Index of the waypoint in the request.

Time -> (string)

The departure time.

Incidents -> (list)

Incidents corresponding to this leg of the route.

(structure)

Incidents corresponding to this leg of the route.

Description -> (string)

Brief readable description of the incident.

EndTime -> (string)

End timestamp of the incident.

Severity -> (string)

Severity of the incident Critical - The part of the route the incident affects is unusable. Major- Major impact on the leg duration, for example stop and go Minor- Minor impact on the leg duration, for example traffic jam Low - Low on duration, for example slightly increased traffic

StartTime -> (string)

Start time of the incident.

Type -> (string)

Type of the incident.

Notices -> (list)

Notices are additional information returned that indicate issues that occurred during route calculation.

(structure)

Notices are additional information returned that indicate issues that occurred during route calculation.

Code -> (string)

Code corresponding to the issue.

Details -> (list)

Additional details of the notice.

(structure)

Additional details of the notice.

Title -> (string)

The notice title.

ViolatedConstraints -> (structure)

Any violated constraints.

AllHazardsRestricted -> (boolean)

This restriction applies to truck cargo, where the resulting route excludes roads on which hazardous materials are prohibited from being transported.

AxleCount -> (structure)

Total number of axles of the vehicle.

Min -> (integer)

Minimum value for the range.

Max -> (integer)

Maximum value for the range.

HazardousCargos -> (list)

List of Hazardous cargo contained in the vehicle.

(string)

MaxHeight -> (long)

The maximum height of the vehicle.

MaxKpraLength -> (long)

The maximum Kpra length of the vehicle.

**Unit** : `centimeters`

MaxLength -> (long)

The maximum length of the vehicle.

MaxPayloadCapacity -> (long)

The maximum load capacity of the vehicle.

**Unit** : `kilograms`

MaxWeight -> (structure)

The maximum weight of the route.

**Unit** : `Kilograms`

Type -> (string)

The type of constraint.

Value -> (long)

The constraint value.

**Unit** : `Kilograms`

MaxWeightPerAxle -> (long)

The maximum weight per axle of the vehicle.

**Unit** : `Kilograms`

MaxWeightPerAxleGroup -> (structure)

The maximum weight per axle group of the vehicle.

**Unit** : `Kilograms`

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

MaxWidth -> (long)

The maximum width of the vehicle.

Occupancy -> (structure)

The number of occupants in the vehicle.

Default Value: `1`

Min -> (integer)

Minimum value for the range.

Max -> (integer)

Maximum value for the range.

RestrictedTimes -> (string)

Access radius restrictions based on time.

TimeDependent -> (boolean)

The time dependent constraint.

TrailerCount -> (structure)

Number of trailers attached to the vehicle.

Default Value: `0`

Min -> (integer)

Minimum value for the range.

Max -> (integer)

Maximum value for the range.

TravelMode -> (boolean)

Travel mode corresponding to the leg.

TruckRoadType -> (string)

Truck road type identifiers. `BK1` through `BK4` apply only to Sweden. `A2,A4,B2,B4,C,D,ET2,ET4` apply only to Mexico.

### Note

There are currently no other supported values as of 26th April 2024.

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

Impact -> (string)

Impact corresponding to the issue. While Low impact notices can be safely ignored, High impact notices must be evaluated further to determine the impact.

PassThroughWaypoints -> (list)

Waypoints that were passed through during the leg. This includes the waypoints that were configured with the PassThrough option.

(structure)

If the waypoint should be treated as a stop. If yes, the route is split up into different legs around the stop.

GeometryOffset -> (integer)

Offset in the leg geometry corresponding to the start of this step.

Place -> (structure)

The place details.

OriginalPosition -> (list)

Position provided in the request.

(double)

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

WaypointIndex -> (integer)

Index of the waypoint in the request.

Spans -> (list)

Spans that were computed for the requested SpanAdditionalFeatures.

(structure)

Span computed for the requested SpanAdditionalFeatures.

BestCaseDuration -> (long)

Duration of the computed span without traffic congestion.

**Unit** : `seconds`

CarAccess -> (list)

Access attributes for a car corresponding to the span.

(string)

Country -> (string)

3 letter Country code corresponding to the Span.

Distance -> (long)

Distance of the computed span. This feature doesnât split a span, but is always computed on a span split by other properties.

Duration -> (long)

Duration of the computed span. This feature doesnât split a span, but is always computed on a span split by other properties.

**Unit** : `seconds`

DynamicSpeed -> (structure)

Dynamic speed details corresponding to the span.

**Unit** : `KilometersPerHour`

BestCaseSpeed -> (double)

Estimated speed while traversing the span without traffic congestion.

**Unit** : `KilometersPerHour`

TurnDuration -> (long)

Estimated time to turn from this span into the next.

**Unit** : `seconds`

TypicalSpeed -> (double)

Estimated speed while traversing the span under typical traffic congestion.

**Unit** : `KilometersPerHour`

FunctionalClassification -> (integer)

Functional classification of the road segment corresponding to the span.

Gate -> (string)

Attributes corresponding to a gate. The gate is present at the end of the returned span.

GeometryOffset -> (integer)

Offset in the leg geometry corresponding to the start of this span.

Incidents -> (list)

Incidents corresponding to the span. These index into the Incidents in the parent Leg.

(integer)

Names -> (list)

Provides an array of names of the vehicle span in available languages.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

Notices -> (list)

Notices are additional information returned that indicate issues that occurred during route calculation.

(integer)

RailwayCrossing -> (string)

Attributes corresponding to a railway crossing. The gate is present at the end of the returned span.

Region -> (string)

2-3 letter Region code corresponding to the Span. This is either a province or a state.

RoadAttributes -> (list)

Attributes for the road segment corresponding to the span.

(string)

RouteNumbers -> (list)

Designated route name or number corresponding to the span.

(structure)

The route number.

Direction -> (string)

Directional identifier of the route.

Language -> (string)

List of languages for instructions corresponding to the route number.

Value -> (string)

The route number.

ScooterAccess -> (list)

Access attributes for a scooter corresponding to the span.

(string)

SpeedLimit -> (structure)

Speed limit details corresponding to the span.

**Unit** : `KilometersPerHour`

MaxSpeed -> (double)

Maximum speed.

**Unit** : `KilometersPerHour`

Unlimited -> (boolean)

If the span doesnât have a speed limit like the Autobahn.

TollSystems -> (list)

Toll systems are authorities that collect payments for the toll.

(integer)

TruckAccess -> (list)

Access attributes for a truck corresponding to the span.

(string)

TruckRoadTypes -> (list)

Truck road type identifiers. `BK1` through `BK4` apply only to Sweden. `A2,A4,B2,B4,C,D,ET2,ET4` apply only to Mexico.

### Note

There are currently no other supported values as of 26th April 2024.

(integer)

TypicalDuration -> (long)

Duration of the computed span under typical traffic congestion.

**Unit** : `seconds`

Zones -> (list)

Zones corresponding to this leg of the route.

(integer)

Summary -> (structure)

Summarized details of the leg.

Overview -> (structure)

Summarized details for the leg including before travel, travel and after travel steps.

BestCaseDuration -> (long)

Total duration in free flowing traffic, which is the best case or shortest duration possible to cover the leg.

**Unit** : `seconds`

Distance -> (long)

Distance of the step.

Duration -> (long)

Duration of the step.

**Unit** : `seconds`

TypicalDuration -> (long)

Duration of the computed span under typical traffic congestion.

**Unit** : `seconds`

TravelOnly -> (structure)

Summarized details for the leg including travel steps only. The Distance for the travel only portion of the journey is in meters

BestCaseDuration -> (long)

Total duration in free flowing traffic, which is the best case or shortest duration possible to cover the leg.

**Unit** : `seconds`

Duration -> (long)

Duration of the step.

**Unit** : `seconds`

TypicalDuration -> (long)

Duration of the computed span under typical traffic congestion.

**Unit** : `seconds`

Tolls -> (list)

Toll related options.

(structure)

Provides details about toll information along a route, including the payment sites, applicable toll rates, toll systems, and the country associated with the toll collection.

Country -> (string)

The alpha-2 or alpha-3 character code for the country.

PaymentSites -> (list)

Locations or sites where the toll fare is collected.

(structure)

Locations or sites where the toll fare is collected.

Name -> (string)

Name of the payment site.

Position -> (list)

Position defined as `[longitude, latitude]` .

(double)

Rates -> (list)

Toll rates that need to be paid to travel this leg of the route.

(structure)

The toll rate.

ApplicableTimes -> (string)

Time when the rate is valid.

ConvertedPrice -> (structure)

Price in the converted currency as specified in the request.

Currency -> (string)

Currency code corresponding to the price. This is the same as Currency specified in the request.

Estimate -> (boolean)

If the price is an estimate or an exact value.

PerDuration -> (long)

Duration for which the price corresponds to.

**Unit** : `seconds`

Range -> (boolean)

If the price is a range or an exact value. If any of the toll fares making up the route is a range, the overall price is also a range.

RangeValue -> (structure)

Price range with a minimum and maximum value, if a range.

Min -> (double)

Minimum price.

Max -> (double)

Maximum price.

Value -> (double)

Exact price, if not a range.

Id -> (string)

The Toll rate Id.

LocalPrice -> (structure)

Price in the local regional currency.

Currency -> (string)

Currency code corresponding to the price. This is the same as Currency specified in the request.

Estimate -> (boolean)

If the price is an estimate or an exact value.

PerDuration -> (long)

Duration for which the price corresponds to.

**Unit** : `seconds`

Range -> (boolean)

If the price is a range or an exact value. If any of the toll fares making up the route is a range, the overall price is also a range.

RangeValue -> (structure)

Price range with a minimum and maximum value, if a range.

Min -> (double)

Minimum price.

Max -> (double)

Maximum price.

Value -> (double)

Exact price, if not a range.

Name -> (string)

The name of the toll.

Pass -> (structure)

Details if the toll rate can be a pass that supports multiple trips.

IncludesReturnTrip -> (boolean)

If the pass includes the rate for the return leg of the trip.

SeniorPass -> (boolean)

If the pass is only valid for senior persons.

TransferCount -> (integer)

If the toll pass can be transferred, and how many times.

TripCount -> (integer)

Number of trips the pass is valid for.

ValidityPeriod -> (structure)

Period for which the pass is valid.

Period -> (string)

Validity period.

PeriodCount -> (integer)

Counts for the validity period.

PaymentMethods -> (list)

Accepted payment methods at the toll.

(string)

Transponders -> (list)

Transponders for which this toll can be applied.

(structure)

Transponders for which this toll can be applied.

SystemName -> (string)

Names of the toll system collecting the toll.

Systems -> (list)

Toll systems are authorities that collect payments for the toll.

(integer)

TollSystems -> (list)

Toll systems are authorities that collect payments for the toll.

(structure)

Toll systems are authorities that collect payments for the toll.

Name -> (string)

The toll system name.

TravelSteps -> (list)

Steps of a leg that must be performed before the travel portion of the leg.

(structure)

Steps of a leg that correspond to the travel portion of the leg.

ContinueHighwayStepDetails -> (structure)

Details that are specific to a Continue Highway step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

SteeringDirection -> (string)

Steering direction for the step.

TurnAngle -> (double)

Angle of the turn.

TurnIntensity -> (string)

Intensity of the turn.

ContinueStepDetails -> (structure)

Details that are specific to a Continue step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

CurrentRoad -> (structure)

Details of the current road.

RoadName -> (list)

Name of the road (localized).

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

RouteNumber -> (list)

Route number of the road.

(structure)

The route number.

Direction -> (string)

Directional identifier of the route.

Language -> (string)

List of languages for instructions corresponding to the route number.

Value -> (string)

The route number.

Towards -> (list)

Names of destinations that can be reached when traveling on the road.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

Type -> (string)

The type of road.

Distance -> (long)

Distance of the step.

Duration -> (long)

Duration of the step.

**Unit** : `seconds`

EnterHighwayStepDetails -> (structure)

Details that are specific to a Enter Highway step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

SteeringDirection -> (string)

Steering direction for the step.

TurnAngle -> (double)

Angle of the turn.

TurnIntensity -> (string)

Intensity of the turn.

ExitNumber -> (list)

Exit number of the road exit, if applicable.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

ExitStepDetails -> (structure)

Details that are specific to a Roundabout Exit step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

RelativeExit -> (integer)

Exit to be taken.

SteeringDirection -> (string)

Steering direction for the step.

TurnAngle -> (double)

Angle of the turn.

TurnIntensity -> (string)

Intensity of the turn.

GeometryOffset -> (integer)

Offset in the leg geometry corresponding to the start of this step.

Instruction -> (string)

Brief description of the step in the requested language.

### Note

Only available when the TravelStepType is Default.

KeepStepDetails -> (structure)

Details that are specific to a Keep step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

SteeringDirection -> (string)

Steering direction for the step.

TurnAngle -> (double)

Angle of the turn.

TurnIntensity -> (string)

Intensity of the turn.

NextRoad -> (structure)

Details of the next road. See RouteRoad for details of sub-attributes.

RoadName -> (list)

Name of the road (localized).

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

RouteNumber -> (list)

Route number of the road.

(structure)

The route number.

Direction -> (string)

Directional identifier of the route.

Language -> (string)

List of languages for instructions corresponding to the route number.

Value -> (string)

The route number.

Towards -> (list)

Names of destinations that can be reached when traveling on the road.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

Type -> (string)

The type of road.

RampStepDetails -> (structure)

Details that are specific to a Ramp step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

SteeringDirection -> (string)

Steering direction for the step.

TurnAngle -> (double)

Angle of the turn.

TurnIntensity -> (string)

Intensity of the turn.

RoundaboutEnterStepDetails -> (structure)

Details that are specific to a Roundabout Enter step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

SteeringDirection -> (string)

Steering direction for the step.

TurnAngle -> (double)

Angle of the turn.

TurnIntensity -> (string)

Intensity of the turn.

RoundaboutExitStepDetails -> (structure)

Details that are specific to a Roundabout Exit step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

RelativeExit -> (integer)

Exit to be taken.

RoundaboutAngle -> (double)

Angle of the roundabout.

SteeringDirection -> (string)

Steering direction for the step.

RoundaboutPassStepDetails -> (structure)

Details that are specific to a Roundabout Pass step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

SteeringDirection -> (string)

Steering direction for the step.

TurnAngle -> (double)

Angle of the turn.

TurnIntensity -> (string)

Intensity of the turn.

Signpost -> (structure)

Sign post information of the action, applicable only for TurnByTurn steps. See RouteSignpost for details of sub-attributes.

Labels -> (list)

Labels present on the sign post.

(structure)

Labels presented on the sign post.

RouteNumber -> (structure)

Route number of the road.

Direction -> (string)

Directional identifier of the route.

Language -> (string)

List of languages for instructions corresponding to the route number.

Value -> (string)

The route number.

Text -> (structure)

The Signpost text.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

TurnStepDetails -> (structure)

Details that are specific to a Turn step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

SteeringDirection -> (string)

Steering direction for the step.

TurnAngle -> (double)

Angle of the turn.

TurnIntensity -> (string)

Intensity of the turn.

Type -> (string)

Type of the step.

UTurnStepDetails -> (structure)

Details that are specific to a Turn step.

Intersection -> (list)

Name of the intersection, if applicable to the step.

(structure)

The localized string.

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

SteeringDirection -> (string)

Steering direction for the step.

TurnAngle -> (double)

Angle of the turn.

TurnIntensity -> (string)

Intensity of the turn.

TruckRoadTypes -> (list)

Truck road type identifiers. `BK1` through `BK4` apply only to Sweden. `A2,A4,B2,B4,C,D,ET2,ET4` apply only to Mexico.

### Note

There are currently no other supported values as of 26th April 2024.

(string)

Zones -> (list)

Zones corresponding to this leg of the route.

(structure)

The zone.

Category -> (string)

The zone category.

Name -> (string)

The name of the zone.

MajorRoadLabels -> (list)

Important labels including names and route numbers that differentiate the current route from the alternatives presented.

(structure)

Important labels including names and route numbers that differentiate the current route from the alternatives presented.

RoadName -> (structure)

Name of the road (localized).

Language -> (string)

A list of BCP 47 compliant language codes for the results to be rendered in. The request uses the regional default as the fallback if the requested language canât be provided.

Value -> (string)

The value of the localized string.

RouteNumber -> (structure)

Route number of the road.

Direction -> (string)

Directional identifier of the route.

Language -> (string)

List of languages for instructions corresponding to the route number.

Value -> (string)

The route number.

Summary -> (structure)

Summarized details of the leg.

Distance -> (long)

Distance of the route.

Duration -> (long)

Duration of the route.

**Unit** : `seconds`

Tolls -> (structure)

Toll summary for the complete route.

Total -> (structure)

Total toll summary for the complete route. Total is the only summary available today.

Currency -> (string)

Currency code corresponding to the price. This is the same as Currency specified in the request.

Estimate -> (boolean)

If the price is an estimate or an exact value.

Range -> (boolean)

If the price is a range or an exact value. If any of the toll fares making up the route is a range, the overall price is also a range.

RangeValue -> (structure)

Price range with a minimum and maximum value, if a range.

Min -> (double)

Minimum price.

Max -> (double)

Maximum price.

Value -> (double)

Exact price, if not a range.