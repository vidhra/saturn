# search-raster-data-collectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-geospatial/search-raster-data-collection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-geospatial/search-raster-data-collection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker-geospatial](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-geospatial/index.html#cli-aws-sagemaker-geospatial) ]

# search-raster-data-collection

## Description

Allows you run image query on a specific raster data collection to get a list of the satellite imagery matching the selected filters.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-geospatial-2020-05-27/SearchRasterDataCollection)

## Synopsis

```
search-raster-data-collection
--arn <value>
[--next-token <value>]
--raster-data-collection-query <value>
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

`--arn` (string)

The Amazon Resource Name (ARN) of the raster data collection.

`--next-token` (string)

If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.

`--raster-data-collection-query` (structure)

RasterDataCollectionQuery consisting of [AreaOfInterest(AOI)](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_AreaOfInterest.html) , [PropertyFilters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_PropertyFilter.html) and [TimeRangeFilterInput](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_TimeRangeFilterInput.html) used in [SearchRasterDataCollection](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_SearchRasterDataCollection.html) .

AreaOfInterest -> (tagged union structure)

The Area of interest to be used in the search query.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `AreaOfInterestGeometry`.

AreaOfInterestGeometry -> (tagged union structure)

A GeoJSON object representing the geographic extent in the coordinate space.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `MultiPolygonGeometry`, `PolygonGeometry`.

MultiPolygonGeometry -> (structure)

The structure representing the MultiPolygon Geometry.

Coordinates -> (list)

The coordinates of the multipolygon geometry.

(list)

(list)

(list)

(double)

PolygonGeometry -> (structure)

The structure representing Polygon Geometry.

Coordinates -> (list)

Coordinates representing a Polygon based on the [GeoJson spec](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.6) .

(list)

(list)

(double)

BandFilter -> (list)

The list of Bands to be displayed in the result for each item.

(string)

PropertyFilters -> (structure)

The Property Filters used in the search query.

LogicalOperator -> (string)

The Logical Operator used to combine the Property Filters.

Properties -> (list)

A list of Property Filters.

(structure)

The structure representing a single PropertyFilter.

Property -> (tagged union structure)

Represents a single property to match with when searching a raster data collection.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `EoCloudCover`, `LandsatCloudCoverLand`, `Platform`, `ViewOffNadir`, `ViewSunAzimuth`, `ViewSunElevation`.

EoCloudCover -> (structure)

The structure representing EoCloudCover property filter containing a lower bound and upper bound.

LowerBound -> (float)

Lower bound for EoCloudCover.

UpperBound -> (float)

Upper bound for EoCloudCover.

LandsatCloudCoverLand -> (structure)

The structure representing Land Cloud Cover property filter for Landsat collection containing a lower bound and upper bound.

LowerBound -> (float)

The minimum value for Land Cloud Cover property filter. This will filter items having Land Cloud Cover greater than or equal to this value.

UpperBound -> (float)

The maximum value for Land Cloud Cover property filter. This will filter items having Land Cloud Cover less than or equal to this value.

Platform -> (structure)

The structure representing Platform property filter consisting of value and comparison operator.

ComparisonOperator -> (string)

The ComparisonOperator to use with PlatformInput.

Value -> (string)

The value of the platform.

ViewOffNadir -> (structure)

The structure representing ViewOffNadir property filter containing a lower bound and upper bound.

LowerBound -> (float)

The minimum value for ViewOffNadir property filter. This filters items having ViewOffNadir greater than or equal to this value.

UpperBound -> (float)

The maximum value for ViewOffNadir property filter. This filters items having ViewOffNadir lesser than or equal to this value.

ViewSunAzimuth -> (structure)

The structure representing ViewSunAzimuth property filter containing a lower bound and upper bound.

LowerBound -> (float)

The minimum value for ViewSunAzimuth property filter. This filters items having ViewSunAzimuth greater than or equal to this value.

UpperBound -> (float)

The maximum value for ViewSunAzimuth property filter. This filters items having ViewSunAzimuth lesser than or equal to this value.

ViewSunElevation -> (structure)

The structure representing ViewSunElevation property filter containing a lower bound and upper bound.

LowerBound -> (float)

The lower bound to view the sun elevation.

UpperBound -> (float)

The upper bound to view the sun elevation.

TimeRangeFilter -> (structure)

The TimeRange Filter used in the search query.

EndTime -> (timestamp)

The end time for the time-range filter.

StartTime -> (timestamp)

The start time for the time-range filter.

JSON Syntax:

```
{
  "AreaOfInterest": {
    "AreaOfInterestGeometry": {
      "MultiPolygonGeometry": {
        "Coordinates": [
          [
            [
              [double, ...]
              ...
            ]
            ...
          ]
          ...
        ]
      },
      "PolygonGeometry": {
        "Coordinates": [
          [
            [double, ...]
            ...
          ]
          ...
        ]
      }
    }
  },
  "BandFilter": ["string", ...],
  "PropertyFilters": {
    "LogicalOperator": "AND",
    "Properties": [
      {
        "Property": {
          "EoCloudCover": {
            "LowerBound": float,
            "UpperBound": float
          },
          "LandsatCloudCoverLand": {
            "LowerBound": float,
            "UpperBound": float
          },
          "Platform": {
            "ComparisonOperator": "EQUALS"|"NOT_EQUALS"|"STARTS_WITH",
            "Value": "string"
          },
          "ViewOffNadir": {
            "LowerBound": float,
            "UpperBound": float
          },
          "ViewSunAzimuth": {
            "LowerBound": float,
            "UpperBound": float
          },
          "ViewSunElevation": {
            "LowerBound": float,
            "UpperBound": float
          }
        }
      }
      ...
    ]
  },
  "TimeRangeFilter": {
    "EndTime": timestamp,
    "StartTime": timestamp
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

ApproximateResultCount -> (integer)

Approximate number of results in the response.

Items -> (list)

List of items matching the Raster DataCollectionQuery.

(structure)

The structure representing the items in the response for SearchRasterDataCollection.

Assets -> (map)

This is a dictionary of Asset Objects data associated with the Item that can be downloaded or streamed, each with a unique key.

key -> (string)

value -> (structure)

The structure containing the asset properties.

Href -> (string)

Link to the asset object.

DateTime -> (timestamp)

The searchable date and time of the item, in UTC.

Geometry -> (structure)

The item Geometry in GeoJson format.

Coordinates -> (list)

The coordinates of the GeoJson Geometry.

(list)

(list)

(double)

Type -> (string)

GeoJson Geometry types like Polygon and MultiPolygon.

Id -> (string)

A unique Id for the source item.

Properties -> (structure)

This field contains additional properties of the item.

EoCloudCover -> (float)

Estimate of cloud cover.

LandsatCloudCoverLand -> (float)

Land cloud cover for Landsat Data Collection.

Platform -> (string)

Platform property. Platform refers to the unique name of the specific platform the instrument is attached to. For satellites it is the name of the satellite, eg. landsat-8 (Landsat-8), sentinel-2a.

ViewOffNadir -> (float)

The angle from the sensor between nadir (straight down) and the scene center. Measured in degrees (0-90).

ViewSunAzimuth -> (float)

The sun azimuth angle. From the scene center point on the ground, this is the angle between truth north and the sun. Measured clockwise in degrees (0-360).

ViewSunElevation -> (float)

The sun elevation angle. The angle from the tangent of the scene center point to the sun. Measured from the horizon in degrees (-90-90). Negative values indicate the sun is below the horizon, e.g. sun elevation of -10Â° means the data was captured during [nautical twilight](https://www.timeanddate.com/astronomy/different-types-twilight.html) .

NextToken -> (string)

If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.