# start-earth-observation-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-geospatial/start-earth-observation-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-geospatial/start-earth-observation-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker-geospatial](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-geospatial/index.html#cli-aws-sagemaker-geospatial) ]

# start-earth-observation-job

## Description

Use this operation to create an Earth observation job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-geospatial-2020-05-27/StartEarthObservationJob)

## Synopsis

```
start-earth-observation-job
[--client-token <value>]
--execution-role-arn <value>
--input-config <value>
--job-config <value>
[--kms-key-id <value>]
--name <value>
[--tags <value>]
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

`--client-token` (string)

A unique token that guarantees that the call to this API is idempotent.

`--execution-role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role that you specified for the job.

`--input-config` (structure)

Input configuration information for the Earth Observation job.

PreviousEarthObservationJobArn -> (string)

The Amazon Resource Name (ARN) of the previous Earth Observation job.

RasterDataCollectionQuery -> (structure)

The structure representing the RasterDataCollection Query consisting of the Area of Interest, RasterDataCollectionArn,TimeRange and Property Filters.

AreaOfInterest -> (tagged union structure)

The area of interest being queried for the raster data collection.

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

PropertyFilters -> (structure)

The list of Property filters used in the Raster Data Collection Query.

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

RasterDataCollectionArn -> (string)

The Amazon Resource Name (ARN) of the raster data collection.

TimeRangeFilter -> (structure)

The TimeRange Filter used in the RasterDataCollection Query.

EndTime -> (timestamp)

The end time for the time-range filter.

StartTime -> (timestamp)

The start time for the time-range filter.

JSON Syntax:

```
{
  "PreviousEarthObservationJobArn": "string",
  "RasterDataCollectionQuery": {
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
    "RasterDataCollectionArn": "string",
    "TimeRangeFilter": {
      "EndTime": timestamp,
      "StartTime": timestamp
    }
  }
}
```

`--job-config` (tagged union structure)

An object containing information about the job configuration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `BandMathConfig`, `CloudMaskingConfig`, `CloudRemovalConfig`, `GeoMosaicConfig`, `LandCoverSegmentationConfig`, `ResamplingConfig`, `StackConfig`, `TemporalStatisticsConfig`, `ZonalStatisticsConfig`.

BandMathConfig -> (structure)

An object containing information about the job configuration for BandMath.

CustomIndices -> (structure)

CustomIndices that are computed.

Operations -> (list)

A list of BandMath indices to compute.

(structure)

Represents an arithmetic operation to compute spectral index.

Equation -> (string)

Textual representation of the math operation; Equation used to compute the spectral index.

Name -> (string)

The name of the operation.

OutputType -> (string)

The type of the operation.

PredefinedIndices -> (list)

One or many of the supported predefined indices to compute. Allowed values: `NDVI` , `EVI2` , `MSAVI` , `NDWI` , `NDMI` , `NDSI` , and `WDRVI` .

(string)

CloudMaskingConfig -> (structure)

An object containing information about the job configuration for cloud masking.

CloudRemovalConfig -> (structure)

An object containing information about the job configuration for cloud removal.

AlgorithmName -> (string)

The name of the algorithm used for cloud removal.

InterpolationValue -> (string)

The interpolation value you provide for cloud removal.

TargetBands -> (list)

TargetBands to be returned in the output of CloudRemoval operation.

(string)

GeoMosaicConfig -> (structure)

An object containing information about the job configuration for geomosaic.

AlgorithmName -> (string)

The name of the algorithm being used for geomosaic.

TargetBands -> (list)

The target bands for geomosaic.

(string)

LandCoverSegmentationConfig -> (structure)

An object containing information about the job configuration for land cover segmentation.

ResamplingConfig -> (structure)

An object containing information about the job configuration for resampling.

AlgorithmName -> (string)

The name of the algorithm used for resampling.

OutputResolution -> (structure)

The structure representing output resolution (in target georeferenced units) of the result of resampling operation.

UserDefined -> (structure)

User Defined Resolution for the output of Resampling operation defined by value and unit.

Unit -> (string)

The units for output resolution of the result.

Value -> (float)

The value for output resolution of the result.

TargetBands -> (list)

Bands used in the operation. If no target bands are specified, it uses all bands available in the input.

(string)

StackConfig -> (structure)

An object containing information about the job configuration for a Stacking Earth Observation job.

OutputResolution -> (structure)

The structure representing output resolution (in target georeferenced units) of the result of stacking operation.

Predefined -> (string)

A string value representing Predefined Output Resolution for a stacking operation. Allowed values are `HIGHEST` , `LOWEST` , and `AVERAGE` .

UserDefined -> (structure)

The structure representing User Output Resolution for a Stacking operation defined as a value and unit.

Unit -> (string)

The units for output resolution of the result.

Value -> (float)

The value for output resolution of the result.

TargetBands -> (list)

A list of bands to be stacked in the specified order. When the parameter is not provided, all the available bands in the data collection are stacked in the alphabetical order of their asset names.

(string)

TemporalStatisticsConfig -> (structure)

An object containing information about the job configuration for temporal statistics.

GroupBy -> (string)

The input for the temporal statistics grouping by time frequency option.

Statistics -> (list)

The list of the statistics method options.

(string)

TargetBands -> (list)

The list of target band names for the temporal statistic to calculate.

(string)

ZonalStatisticsConfig -> (structure)

An object containing information about the job configuration for zonal statistics.

Statistics -> (list)

List of zonal statistics to compute.

(string)

TargetBands -> (list)

Bands used in the operation. If no target bands are specified, it uses all bands available input.

(string)

ZoneS3Path -> (string)

The Amazon S3 path pointing to the GeoJSON containing the polygonal zones.

ZoneS3PathKmsKeyId -> (string)

The Amazon Resource Name (ARN) or an ID of a Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to decrypt your output artifacts with Amazon S3 server-side encryption. The SageMaker execution role must have `kms:GenerateDataKey` permission.

The `KmsKeyId` can be any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:<region>:<account>:key/<key-id-12ab-34cd-56ef-1234567890ab>"`

For more information about key identifiers, see [Key identifiers (KeyID)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id) in the Amazon Web Services Key Management Service (Amazon Web Services KMS) documentation.

JSON Syntax:

```
{
  "BandMathConfig": {
    "CustomIndices": {
      "Operations": [
        {
          "Equation": "string",
          "Name": "string",
          "OutputType": "INT32"|"FLOAT32"|"INT16"|"FLOAT64"|"UINT16"
        }
        ...
      ]
    },
    "PredefinedIndices": ["string", ...]
  },
  "CloudMaskingConfig": {

  },
  "CloudRemovalConfig": {
    "AlgorithmName": "INTERPOLATION",
    "InterpolationValue": "string",
    "TargetBands": ["string", ...]
  },
  "GeoMosaicConfig": {
    "AlgorithmName": "NEAR"|"BILINEAR"|"CUBIC"|"CUBICSPLINE"|"LANCZOS"|"AVERAGE"|"RMS"|"MODE"|"MAX"|"MIN"|"MED"|"Q1"|"Q3"|"SUM",
    "TargetBands": ["string", ...]
  },
  "LandCoverSegmentationConfig": {

  },
  "ResamplingConfig": {
    "AlgorithmName": "NEAR"|"BILINEAR"|"CUBIC"|"CUBICSPLINE"|"LANCZOS"|"AVERAGE"|"RMS"|"MODE"|"MAX"|"MIN"|"MED"|"Q1"|"Q3"|"SUM",
    "OutputResolution": {
      "UserDefined": {
        "Unit": "METERS",
        "Value": float
      }
    },
    "TargetBands": ["string", ...]
  },
  "StackConfig": {
    "OutputResolution": {
      "Predefined": "HIGHEST"|"LOWEST"|"AVERAGE",
      "UserDefined": {
        "Unit": "METERS",
        "Value": float
      }
    },
    "TargetBands": ["string", ...]
  },
  "TemporalStatisticsConfig": {
    "GroupBy": "ALL"|"YEARLY",
    "Statistics": ["MEAN"|"MEDIAN"|"STANDARD_DEVIATION", ...],
    "TargetBands": ["string", ...]
  },
  "ZonalStatisticsConfig": {
    "Statistics": ["MEAN"|"MEDIAN"|"STANDARD_DEVIATION"|"MAX"|"MIN"|"SUM", ...],
    "TargetBands": ["string", ...],
    "ZoneS3Path": "string",
    "ZoneS3PathKmsKeyId": "string"
  }
}
```

`--kms-key-id` (string)

The Key Management Service key ID for server-side encryption.

`--name` (string)

The name of the Earth Observation job.

`--tags` (map)

Each tag consists of a key and a value.

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

Arn -> (string)

The Amazon Resource Name (ARN) of the Earth Observation job.

CreationTime -> (timestamp)

The creation time.

DurationInSeconds -> (integer)

The duration of the session, in seconds.

ExecutionRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that you specified for the job.

InputConfig -> (structure)

Input configuration information for the Earth Observation job.

PreviousEarthObservationJobArn -> (string)

The Amazon Resource Name (ARN) of the previous Earth Observation job.

RasterDataCollectionQuery -> (structure)

The structure representing the RasterDataCollection Query consisting of the Area of Interest, RasterDataCollectionArn, RasterDataCollectionName, TimeRange, and Property Filters.

AreaOfInterest -> (tagged union structure)

The Area of Interest used in the search.

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

PropertyFilters -> (structure)

Property filters used in the search.

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

RasterDataCollectionArn -> (string)

The ARN of the Raster Data Collection against which the search is done.

RasterDataCollectionName -> (string)

The name of the raster data collection.

TimeRangeFilter -> (structure)

The TimeRange filter used in the search.

EndTime -> (timestamp)

The ending time for the time range filter.

StartTime -> (timestamp)

The starting time for the time range filter.

JobConfig -> (tagged union structure)

An object containing information about the job configuration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `BandMathConfig`, `CloudMaskingConfig`, `CloudRemovalConfig`, `GeoMosaicConfig`, `LandCoverSegmentationConfig`, `ResamplingConfig`, `StackConfig`, `TemporalStatisticsConfig`, `ZonalStatisticsConfig`.

BandMathConfig -> (structure)

An object containing information about the job configuration for BandMath.

CustomIndices -> (structure)

CustomIndices that are computed.

Operations -> (list)

A list of BandMath indices to compute.

(structure)

Represents an arithmetic operation to compute spectral index.

Equation -> (string)

Textual representation of the math operation; Equation used to compute the spectral index.

Name -> (string)

The name of the operation.

OutputType -> (string)

The type of the operation.

PredefinedIndices -> (list)

One or many of the supported predefined indices to compute. Allowed values: `NDVI` , `EVI2` , `MSAVI` , `NDWI` , `NDMI` , `NDSI` , and `WDRVI` .

(string)

CloudMaskingConfig -> (structure)

An object containing information about the job configuration for cloud masking.

CloudRemovalConfig -> (structure)

An object containing information about the job configuration for cloud removal.

AlgorithmName -> (string)

The name of the algorithm used for cloud removal.

InterpolationValue -> (string)

The interpolation value you provide for cloud removal.

TargetBands -> (list)

TargetBands to be returned in the output of CloudRemoval operation.

(string)

GeoMosaicConfig -> (structure)

An object containing information about the job configuration for geomosaic.

AlgorithmName -> (string)

The name of the algorithm being used for geomosaic.

TargetBands -> (list)

The target bands for geomosaic.

(string)

LandCoverSegmentationConfig -> (structure)

An object containing information about the job configuration for land cover segmentation.

ResamplingConfig -> (structure)

An object containing information about the job configuration for resampling.

AlgorithmName -> (string)

The name of the algorithm used for resampling.

OutputResolution -> (structure)

The structure representing output resolution (in target georeferenced units) of the result of resampling operation.

UserDefined -> (structure)

User Defined Resolution for the output of Resampling operation defined by value and unit.

Unit -> (string)

The units for output resolution of the result.

Value -> (float)

The value for output resolution of the result.

TargetBands -> (list)

Bands used in the operation. If no target bands are specified, it uses all bands available in the input.

(string)

StackConfig -> (structure)

An object containing information about the job configuration for a Stacking Earth Observation job.

OutputResolution -> (structure)

The structure representing output resolution (in target georeferenced units) of the result of stacking operation.

Predefined -> (string)

A string value representing Predefined Output Resolution for a stacking operation. Allowed values are `HIGHEST` , `LOWEST` , and `AVERAGE` .

UserDefined -> (structure)

The structure representing User Output Resolution for a Stacking operation defined as a value and unit.

Unit -> (string)

The units for output resolution of the result.

Value -> (float)

The value for output resolution of the result.

TargetBands -> (list)

A list of bands to be stacked in the specified order. When the parameter is not provided, all the available bands in the data collection are stacked in the alphabetical order of their asset names.

(string)

TemporalStatisticsConfig -> (structure)

An object containing information about the job configuration for temporal statistics.

GroupBy -> (string)

The input for the temporal statistics grouping by time frequency option.

Statistics -> (list)

The list of the statistics method options.

(string)

TargetBands -> (list)

The list of target band names for the temporal statistic to calculate.

(string)

ZonalStatisticsConfig -> (structure)

An object containing information about the job configuration for zonal statistics.

Statistics -> (list)

List of zonal statistics to compute.

(string)

TargetBands -> (list)

Bands used in the operation. If no target bands are specified, it uses all bands available input.

(string)

ZoneS3Path -> (string)

The Amazon S3 path pointing to the GeoJSON containing the polygonal zones.

ZoneS3PathKmsKeyId -> (string)

The Amazon Resource Name (ARN) or an ID of a Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to decrypt your output artifacts with Amazon S3 server-side encryption. The SageMaker execution role must have `kms:GenerateDataKey` permission.

The `KmsKeyId` can be any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:<region>:<account>:key/<key-id-12ab-34cd-56ef-1234567890ab>"`

For more information about key identifiers, see [Key identifiers (KeyID)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id) in the Amazon Web Services Key Management Service (Amazon Web Services KMS) documentation.

KmsKeyId -> (string)

The Key Management Service key ID for server-side encryption.

Name -> (string)

The name of the Earth Observation job.

Status -> (string)

The status of the Earth Observation job.

Tags -> (map)

Each tag consists of a key and a value.

key -> (string)

value -> (string)