# update-segmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-segment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-segment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# update-segment

## Description

Creates a new segment for an application or updates the configuration, dimension, and other settings for an existing segment thatâs associated with an application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/UpdateSegment)

## Synopsis

```
update-segment
--application-id <value>
--segment-id <value>
--write-segment-request <value>
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

`--application-id` (string)

The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console.

`--segment-id` (string)

The unique identifier for the segment.

`--write-segment-request` (structure)

Specifies the configuration, dimension, and other settings for a segment. A WriteSegmentRequest object can include a Dimensions object or a SegmentGroups object, but not both.

Dimensions -> (structure)

The criteria that define the dimensions for the segment.

Attributes -> (map)

One or more custom attributes to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies attribute-based criteria for including or excluding endpoints from a segment.

AttributeType -> (string)

The type of segment dimension to use. Valid values are:

- INCLUSIVE - endpoints that have attributes matching the values are included in the segment.
- EXCLUSIVE - endpoints that have attributes matching the values are excluded in the segment.
- CONTAINS - endpoints that have attributesâ substrings match the values are included in the segment.
- BEFORE - endpoints with attributes read as ISO_INSTANT datetimes before the value are included in the segment.
- AFTER - endpoints with attributes read as ISO_INSTANT datetimes after the value are included in the segment.
- ON - endpoints with attributes read as ISO_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.
- BETWEEN - endpoints with attributes read as ISO_INSTANT datetimes between the values are included in the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the AttributeType property, endpoints are included or excluded from the segment if their attribute values match the criteria values.

(string)

Behavior -> (structure)

The behavior-based criteria, such as how recently users have used your app, for the segment.

Recency -> (structure)

The dimension settings that are based on how recently an endpoint was active.

Duration -> (string)

The duration to use when determining whether an endpoint is active or inactive.

RecencyType -> (string)

The type of recency dimension to use for the segment. Valid values are: ACTIVE, endpoints that were active within the specified duration are included in the segment; and, INACTIVE, endpoints that werenât active within the specified duration are included in the segment.

Demographic -> (structure)

The demographic-based criteria, such as device platform, for the segment.

AppVersion -> (structure)

The app version criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Channel -> (structure)

The channel criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

DeviceType -> (structure)

The device type criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Make -> (structure)

The device make criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Model -> (structure)

The device model criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Platform -> (structure)

The device platform criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Location -> (structure)

The location-based criteria, such as region or GPS coordinates, for the segment.

Country -> (structure)

The country or region code, in ISO 3166-1 alpha-2 format, for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

GPSPoint -> (structure)

The GPS location and range for the segment.

Coordinates -> (structure)

The GPS coordinates to measure distance from.

Latitude -> (double)

The latitude coordinate of the location.

Longitude -> (double)

The longitude coordinate of the location.

RangeInKilometers -> (double)

The range, in kilometers, from the GPS coordinates.

Metrics -> (map)

One or more custom metrics to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies metric-based criteria for including or excluding endpoints from a segment. These criteria derive from custom metrics that you define for endpoints.

ComparisonOperator -> (string)

The operator to use when comparing metric values. Valid values are: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, and EQUAL.

Value -> (double)

The value to compare.

UserAttributes -> (map)

One or more custom user attributes to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies attribute-based criteria for including or excluding endpoints from a segment.

AttributeType -> (string)

The type of segment dimension to use. Valid values are:

- INCLUSIVE - endpoints that have attributes matching the values are included in the segment.
- EXCLUSIVE - endpoints that have attributes matching the values are excluded in the segment.
- CONTAINS - endpoints that have attributesâ substrings match the values are included in the segment.
- BEFORE - endpoints with attributes read as ISO_INSTANT datetimes before the value are included in the segment.
- AFTER - endpoints with attributes read as ISO_INSTANT datetimes after the value are included in the segment.
- ON - endpoints with attributes read as ISO_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.
- BETWEEN - endpoints with attributes read as ISO_INSTANT datetimes between the values are included in the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the AttributeType property, endpoints are included or excluded from the segment if their attribute values match the criteria values.

(string)

Name -> (string)

The name of the segment.

SegmentGroups -> (structure)

The segment group to use and the dimensions to apply to the groupâs base segments in order to build the segment. A segment group can consist of zero or more base segments. Your request can include only one segment group.

Groups -> (list)

An array that defines the set of segment criteria to evaluate when handling segment groups for the segment.

(structure)

Specifies the base segments and dimensions for a segment, and the relationships between these base segments and dimensions.

Dimensions -> (list)

An array that defines the dimensions for the segment.

(structure)

Specifies the dimension settings for a segment.

Attributes -> (map)

One or more custom attributes to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies attribute-based criteria for including or excluding endpoints from a segment.

AttributeType -> (string)

The type of segment dimension to use. Valid values are:

- INCLUSIVE - endpoints that have attributes matching the values are included in the segment.
- EXCLUSIVE - endpoints that have attributes matching the values are excluded in the segment.
- CONTAINS - endpoints that have attributesâ substrings match the values are included in the segment.
- BEFORE - endpoints with attributes read as ISO_INSTANT datetimes before the value are included in the segment.
- AFTER - endpoints with attributes read as ISO_INSTANT datetimes after the value are included in the segment.
- ON - endpoints with attributes read as ISO_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.
- BETWEEN - endpoints with attributes read as ISO_INSTANT datetimes between the values are included in the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the AttributeType property, endpoints are included or excluded from the segment if their attribute values match the criteria values.

(string)

Behavior -> (structure)

The behavior-based criteria, such as how recently users have used your app, for the segment.

Recency -> (structure)

The dimension settings that are based on how recently an endpoint was active.

Duration -> (string)

The duration to use when determining whether an endpoint is active or inactive.

RecencyType -> (string)

The type of recency dimension to use for the segment. Valid values are: ACTIVE, endpoints that were active within the specified duration are included in the segment; and, INACTIVE, endpoints that werenât active within the specified duration are included in the segment.

Demographic -> (structure)

The demographic-based criteria, such as device platform, for the segment.

AppVersion -> (structure)

The app version criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Channel -> (structure)

The channel criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

DeviceType -> (structure)

The device type criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Make -> (structure)

The device make criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Model -> (structure)

The device model criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Platform -> (structure)

The device platform criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Location -> (structure)

The location-based criteria, such as region or GPS coordinates, for the segment.

Country -> (structure)

The country or region code, in ISO 3166-1 alpha-2 format, for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

GPSPoint -> (structure)

The GPS location and range for the segment.

Coordinates -> (structure)

The GPS coordinates to measure distance from.

Latitude -> (double)

The latitude coordinate of the location.

Longitude -> (double)

The longitude coordinate of the location.

RangeInKilometers -> (double)

The range, in kilometers, from the GPS coordinates.

Metrics -> (map)

One or more custom metrics to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies metric-based criteria for including or excluding endpoints from a segment. These criteria derive from custom metrics that you define for endpoints.

ComparisonOperator -> (string)

The operator to use when comparing metric values. Valid values are: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, and EQUAL.

Value -> (double)

The value to compare.

UserAttributes -> (map)

One or more custom user attributes to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies attribute-based criteria for including or excluding endpoints from a segment.

AttributeType -> (string)

The type of segment dimension to use. Valid values are:

- INCLUSIVE - endpoints that have attributes matching the values are included in the segment.
- EXCLUSIVE - endpoints that have attributes matching the values are excluded in the segment.
- CONTAINS - endpoints that have attributesâ substrings match the values are included in the segment.
- BEFORE - endpoints with attributes read as ISO_INSTANT datetimes before the value are included in the segment.
- AFTER - endpoints with attributes read as ISO_INSTANT datetimes after the value are included in the segment.
- ON - endpoints with attributes read as ISO_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.
- BETWEEN - endpoints with attributes read as ISO_INSTANT datetimes between the values are included in the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the AttributeType property, endpoints are included or excluded from the segment if their attribute values match the criteria values.

(string)

SourceSegments -> (list)

The base segment to build the segment on. A base segment, also referred to as a *source segment* , defines the initial population of endpoints for a segment. When you add dimensions to a segment, Amazon Pinpoint filters the base segment by using the dimensions that you specify.

You can specify more than one dimensional segment or only one imported segment. If you specify an imported segment, the Amazon Pinpoint console displays a segment size estimate that indicates the size of the imported segment without any filters applied to it.

(structure)

Specifies the segment identifier and version of a segment.

Id -> (string)

The unique identifier for the segment.

Version -> (integer)

The version number of the segment.

SourceType -> (string)

Specifies how to handle multiple base segments for the segment. For example, if you specify three base segments for the segment, whether the resulting segment is based on all, any, or none of the base segments.

Type -> (string)

Specifies how to handle multiple dimensions for the segment. For example, if you specify three dimensions for the segment, whether the resulting segment includes endpoints that match all, any, or none of the dimensions.

Include -> (string)

Specifies how to handle multiple segment groups for the segment. For example, if the segment includes three segment groups, whether the resulting segment includes endpoints that match all, any, or none of the segment groups.

tags -> (map)

### Note

As of **22-05-2023** tags has been deprecated for update operations. After this date any value in tags is not processed and an error code is not returned. To manage tags we recommend using either [Tags](https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html) in the *API Reference for Amazon Pinpoint* , [resourcegroupstaggingapi](https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/index.html) commands in the *AWS Command Line Interface Documentation* or [resourcegroupstaggingapi](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/resourcegroupstaggingapi/package-summary.html) in the *AWS SDK* .

(Deprecated) A string-to-string map of key-value pairs that defines the tags to associate with the segment. Each tag consists of a required tag key and an associated tag value.

key -> (string)

value -> (string)

JSON Syntax:

```
{
  "Dimensions": {
    "Attributes": {"string": {
          "AttributeType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEFORE"|"AFTER"|"ON"|"BETWEEN",
          "Values": ["string", ...]
        }
      ...},
    "Behavior": {
      "Recency": {
        "Duration": "HR_24"|"DAY_7"|"DAY_14"|"DAY_30",
        "RecencyType": "ACTIVE"|"INACTIVE"
      }
    },
    "Demographic": {
      "AppVersion": {
        "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
        "Values": ["string", ...]
      },
      "Channel": {
        "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
        "Values": ["string", ...]
      },
      "DeviceType": {
        "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
        "Values": ["string", ...]
      },
      "Make": {
        "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
        "Values": ["string", ...]
      },
      "Model": {
        "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
        "Values": ["string", ...]
      },
      "Platform": {
        "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
        "Values": ["string", ...]
      }
    },
    "Location": {
      "Country": {
        "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
        "Values": ["string", ...]
      },
      "GPSPoint": {
        "Coordinates": {
          "Latitude": double,
          "Longitude": double
        },
        "RangeInKilometers": double
      }
    },
    "Metrics": {"string": {
          "ComparisonOperator": "string",
          "Value": double
        }
      ...},
    "UserAttributes": {"string": {
          "AttributeType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEFORE"|"AFTER"|"ON"|"BETWEEN",
          "Values": ["string", ...]
        }
      ...}
  },
  "Name": "string",
  "SegmentGroups": {
    "Groups": [
      {
        "Dimensions": [
          {
            "Attributes": {"string": {
                  "AttributeType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEFORE"|"AFTER"|"ON"|"BETWEEN",
                  "Values": ["string", ...]
                }
              ...},
            "Behavior": {
              "Recency": {
                "Duration": "HR_24"|"DAY_7"|"DAY_14"|"DAY_30",
                "RecencyType": "ACTIVE"|"INACTIVE"
              }
            },
            "Demographic": {
              "AppVersion": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                "Values": ["string", ...]
              },
              "Channel": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                "Values": ["string", ...]
              },
              "DeviceType": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                "Values": ["string", ...]
              },
              "Make": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                "Values": ["string", ...]
              },
              "Model": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                "Values": ["string", ...]
              },
              "Platform": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                "Values": ["string", ...]
              }
            },
            "Location": {
              "Country": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                "Values": ["string", ...]
              },
              "GPSPoint": {
                "Coordinates": {
                  "Latitude": double,
                  "Longitude": double
                },
                "RangeInKilometers": double
              }
            },
            "Metrics": {"string": {
                  "ComparisonOperator": "string",
                  "Value": double
                }
              ...},
            "UserAttributes": {"string": {
                  "AttributeType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEFORE"|"AFTER"|"ON"|"BETWEEN",
                  "Values": ["string", ...]
                }
              ...}
          }
          ...
        ],
        "SourceSegments": [
          {
            "Id": "string",
            "Version": integer
          }
          ...
        ],
        "SourceType": "ALL"|"ANY"|"NONE",
        "Type": "ALL"|"ANY"|"NONE"
      }
      ...
    ],
    "Include": "ALL"|"ANY"|"NONE"
  },
  "tags": {"string": "string"
    ...}
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

SegmentResponse -> (structure)

Provides information about the configuration, dimension, and other settings for a segment.

ApplicationId -> (string)

The unique identifier for the application that the segment is associated with.

Arn -> (string)

The Amazon Resource Name (ARN) of the segment.

CreationDate -> (string)

The date and time when the segment was created.

Dimensions -> (structure)

The dimension settings for the segment.

Attributes -> (map)

One or more custom attributes to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies attribute-based criteria for including or excluding endpoints from a segment.

AttributeType -> (string)

The type of segment dimension to use. Valid values are:

- INCLUSIVE - endpoints that have attributes matching the values are included in the segment.
- EXCLUSIVE - endpoints that have attributes matching the values are excluded in the segment.
- CONTAINS - endpoints that have attributesâ substrings match the values are included in the segment.
- BEFORE - endpoints with attributes read as ISO_INSTANT datetimes before the value are included in the segment.
- AFTER - endpoints with attributes read as ISO_INSTANT datetimes after the value are included in the segment.
- ON - endpoints with attributes read as ISO_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.
- BETWEEN - endpoints with attributes read as ISO_INSTANT datetimes between the values are included in the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the AttributeType property, endpoints are included or excluded from the segment if their attribute values match the criteria values.

(string)

Behavior -> (structure)

The behavior-based criteria, such as how recently users have used your app, for the segment.

Recency -> (structure)

The dimension settings that are based on how recently an endpoint was active.

Duration -> (string)

The duration to use when determining whether an endpoint is active or inactive.

RecencyType -> (string)

The type of recency dimension to use for the segment. Valid values are: ACTIVE, endpoints that were active within the specified duration are included in the segment; and, INACTIVE, endpoints that werenât active within the specified duration are included in the segment.

Demographic -> (structure)

The demographic-based criteria, such as device platform, for the segment.

AppVersion -> (structure)

The app version criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Channel -> (structure)

The channel criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

DeviceType -> (structure)

The device type criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Make -> (structure)

The device make criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Model -> (structure)

The device model criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Platform -> (structure)

The device platform criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Location -> (structure)

The location-based criteria, such as region or GPS coordinates, for the segment.

Country -> (structure)

The country or region code, in ISO 3166-1 alpha-2 format, for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

GPSPoint -> (structure)

The GPS location and range for the segment.

Coordinates -> (structure)

The GPS coordinates to measure distance from.

Latitude -> (double)

The latitude coordinate of the location.

Longitude -> (double)

The longitude coordinate of the location.

RangeInKilometers -> (double)

The range, in kilometers, from the GPS coordinates.

Metrics -> (map)

One or more custom metrics to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies metric-based criteria for including or excluding endpoints from a segment. These criteria derive from custom metrics that you define for endpoints.

ComparisonOperator -> (string)

The operator to use when comparing metric values. Valid values are: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, and EQUAL.

Value -> (double)

The value to compare.

UserAttributes -> (map)

One or more custom user attributes to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies attribute-based criteria for including or excluding endpoints from a segment.

AttributeType -> (string)

The type of segment dimension to use. Valid values are:

- INCLUSIVE - endpoints that have attributes matching the values are included in the segment.
- EXCLUSIVE - endpoints that have attributes matching the values are excluded in the segment.
- CONTAINS - endpoints that have attributesâ substrings match the values are included in the segment.
- BEFORE - endpoints with attributes read as ISO_INSTANT datetimes before the value are included in the segment.
- AFTER - endpoints with attributes read as ISO_INSTANT datetimes after the value are included in the segment.
- ON - endpoints with attributes read as ISO_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.
- BETWEEN - endpoints with attributes read as ISO_INSTANT datetimes between the values are included in the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the AttributeType property, endpoints are included or excluded from the segment if their attribute values match the criteria values.

(string)

Id -> (string)

The unique identifier for the segment.

ImportDefinition -> (structure)

The settings for the import job thatâs associated with the segment.

ChannelCounts -> (map)

The number of channel types in the endpoint definitions that were imported to create the segment.

key -> (string)

value -> (integer)

ExternalId -> (string)

(Deprecated) Your AWS account ID, which you assigned to an external ID key in an IAM trust policy. Amazon Pinpoint previously used this value to assume an IAM role when importing endpoint definitions, but we removed this requirement. We donât recommend use of external IDs for IAM roles that are assumed by Amazon Pinpoint.

Format -> (string)

The format of the files that were imported to create the segment. Valid values are: CSV, for comma-separated values format; and, JSON, for newline-delimited JSON format.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorized Amazon Pinpoint to access the Amazon S3 location to import endpoint definitions from.

S3Url -> (string)

The URL of the Amazon Simple Storage Service (Amazon S3) bucket that the endpoint definitions were imported from to create the segment.

Size -> (integer)

The number of endpoint definitions that were imported successfully to create the segment.

LastModifiedDate -> (string)

The date and time when the segment was last modified.

Name -> (string)

The name of the segment.

SegmentGroups -> (structure)

A list of one or more segment groups that apply to the segment. Each segment group consists of zero or more base segments and the dimensions that are applied to those base segments.

Groups -> (list)

An array that defines the set of segment criteria to evaluate when handling segment groups for the segment.

(structure)

Specifies the base segments and dimensions for a segment, and the relationships between these base segments and dimensions.

Dimensions -> (list)

An array that defines the dimensions for the segment.

(structure)

Specifies the dimension settings for a segment.

Attributes -> (map)

One or more custom attributes to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies attribute-based criteria for including or excluding endpoints from a segment.

AttributeType -> (string)

The type of segment dimension to use. Valid values are:

- INCLUSIVE - endpoints that have attributes matching the values are included in the segment.
- EXCLUSIVE - endpoints that have attributes matching the values are excluded in the segment.
- CONTAINS - endpoints that have attributesâ substrings match the values are included in the segment.
- BEFORE - endpoints with attributes read as ISO_INSTANT datetimes before the value are included in the segment.
- AFTER - endpoints with attributes read as ISO_INSTANT datetimes after the value are included in the segment.
- ON - endpoints with attributes read as ISO_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.
- BETWEEN - endpoints with attributes read as ISO_INSTANT datetimes between the values are included in the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the AttributeType property, endpoints are included or excluded from the segment if their attribute values match the criteria values.

(string)

Behavior -> (structure)

The behavior-based criteria, such as how recently users have used your app, for the segment.

Recency -> (structure)

The dimension settings that are based on how recently an endpoint was active.

Duration -> (string)

The duration to use when determining whether an endpoint is active or inactive.

RecencyType -> (string)

The type of recency dimension to use for the segment. Valid values are: ACTIVE, endpoints that were active within the specified duration are included in the segment; and, INACTIVE, endpoints that werenât active within the specified duration are included in the segment.

Demographic -> (structure)

The demographic-based criteria, such as device platform, for the segment.

AppVersion -> (structure)

The app version criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Channel -> (structure)

The channel criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

DeviceType -> (structure)

The device type criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Make -> (structure)

The device make criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Model -> (structure)

The device model criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Platform -> (structure)

The device platform criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Location -> (structure)

The location-based criteria, such as region or GPS coordinates, for the segment.

Country -> (structure)

The country or region code, in ISO 3166-1 alpha-2 format, for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

GPSPoint -> (structure)

The GPS location and range for the segment.

Coordinates -> (structure)

The GPS coordinates to measure distance from.

Latitude -> (double)

The latitude coordinate of the location.

Longitude -> (double)

The longitude coordinate of the location.

RangeInKilometers -> (double)

The range, in kilometers, from the GPS coordinates.

Metrics -> (map)

One or more custom metrics to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies metric-based criteria for including or excluding endpoints from a segment. These criteria derive from custom metrics that you define for endpoints.

ComparisonOperator -> (string)

The operator to use when comparing metric values. Valid values are: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, and EQUAL.

Value -> (double)

The value to compare.

UserAttributes -> (map)

One or more custom user attributes to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies attribute-based criteria for including or excluding endpoints from a segment.

AttributeType -> (string)

The type of segment dimension to use. Valid values are:

- INCLUSIVE - endpoints that have attributes matching the values are included in the segment.
- EXCLUSIVE - endpoints that have attributes matching the values are excluded in the segment.
- CONTAINS - endpoints that have attributesâ substrings match the values are included in the segment.
- BEFORE - endpoints with attributes read as ISO_INSTANT datetimes before the value are included in the segment.
- AFTER - endpoints with attributes read as ISO_INSTANT datetimes after the value are included in the segment.
- ON - endpoints with attributes read as ISO_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.
- BETWEEN - endpoints with attributes read as ISO_INSTANT datetimes between the values are included in the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the AttributeType property, endpoints are included or excluded from the segment if their attribute values match the criteria values.

(string)

SourceSegments -> (list)

The base segment to build the segment on. A base segment, also referred to as a *source segment* , defines the initial population of endpoints for a segment. When you add dimensions to a segment, Amazon Pinpoint filters the base segment by using the dimensions that you specify.

You can specify more than one dimensional segment or only one imported segment. If you specify an imported segment, the Amazon Pinpoint console displays a segment size estimate that indicates the size of the imported segment without any filters applied to it.

(structure)

Specifies the segment identifier and version of a segment.

Id -> (string)

The unique identifier for the segment.

Version -> (integer)

The version number of the segment.

SourceType -> (string)

Specifies how to handle multiple base segments for the segment. For example, if you specify three base segments for the segment, whether the resulting segment is based on all, any, or none of the base segments.

Type -> (string)

Specifies how to handle multiple dimensions for the segment. For example, if you specify three dimensions for the segment, whether the resulting segment includes endpoints that match all, any, or none of the dimensions.

Include -> (string)

Specifies how to handle multiple segment groups for the segment. For example, if the segment includes three segment groups, whether the resulting segment includes endpoints that match all, any, or none of the segment groups.

SegmentType -> (string)

The segment type. Valid values are:

- DIMENSIONAL - A dynamic segment, which is a segment that uses selection criteria that you specify and is based on endpoint data thatâs reported by your app. Dynamic segments can change over time.
- IMPORT - A static segment, which is a segment that uses selection criteria that you specify and is based on endpoint definitions that you import from a file. Imported segments are static; they donât change over time.

tags -> (map)

A string-to-string map of key-value pairs that identifies the tags that are associated with the segment. Each tag consists of a required tag key and an associated tag value.

key -> (string)

value -> (string)

Version -> (integer)

The version number of the segment.