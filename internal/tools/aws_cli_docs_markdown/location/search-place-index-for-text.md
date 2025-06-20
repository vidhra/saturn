# search-place-index-for-textÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/search-place-index-for-text.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/search-place-index-for-text.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [location](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/index.html#cli-aws-location) ]

# search-place-index-for-text

## Description

Geocodes free-form text, such as an address, name, city, or region to allow you to search for Places or points of interest.

Optional parameters let you narrow your search results by bounding box or country, or bias your search toward a specific position on the globe.

### Note

You can search for places near a given position using `BiasPosition` , or filter results within a bounding box using `FilterBBox` . Providing both parameters simultaneously returns an error.

Search results are returned in order of highest to lowest relevance.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/location-2020-11-19/SearchPlaceIndexForText)

## Synopsis

```
search-place-index-for-text
--index-name <value>
--text <value>
[--bias-position <value>]
[--filter-b-box <value>]
[--filter-countries <value>]
[--max-results <value>]
[--language <value>]
[--filter-categories <value>]
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

`--index-name` (string)

The name of the place index resource you want to use for the search.

`--text` (string)

The address, name, city, or region to be used in the search in free-form text format. For example, `123 Any Street` .

`--bias-position` (list)

An optional parameter that indicates a preference for places that are closer to a specified position.

If provided, this parameter must contain a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.

For example, `[-123.1174, 49.2847]` represents the position with longitude `-123.1174` and latitude `49.2847` .

### Note

`BiasPosition` and `FilterBBox` are mutually exclusive. Specifying both options results in an error.

(double)

Syntax:

```
double double ...
```

`--filter-b-box` (list)

An optional parameter that limits the search results by returning only places that are within the provided bounding box.

If provided, this parameter must contain a total of four consecutive numbers in two pairs. The first pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the southwest corner of the bounding box; the second pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the northeast corner of the bounding box.

For example, `[-12.7935, -37.4835, -12.0684, -36.9542]` represents a bounding box where the southwest corner has longitude `-12.7935` and latitude `-37.4835` , and the northeast corner has longitude `-12.0684` and latitude `-36.9542` .

### Note

`FilterBBox` and `BiasPosition` are mutually exclusive. Specifying both options results in an error.

(double)

Syntax:

```
double double ...
```

`--filter-countries` (list)

An optional parameter that limits the search results by returning only places that are in a specified list of countries.

- Valid values include [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) 3-digit country codes. For example, Australia uses three upper-case characters: `AUS` .

(string)

Syntax:

```
"string" "string" ...
```

`--max-results` (integer)

An optional parameter. The maximum number of results returned per request.

The default: `50`

`--language` (string)

The preferred language used to return results. The value must be a valid [BCP 47](https://tools.ietf.org/search/bcp47) language tag, for example, `en` for English.

This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.

For an example, weâll use the Greek language. You search for `Athens, Greece` , with the `language` parameter set to `en` . The result found will most likely be returned as `Athens` .

If you set the `language` parameter to `el` , for Greek, then the result found will more likely be returned as `ÎÎ¸Î®Î½Î±` .

If the data provider does not have a value for Greek, the result will be in a language that the provider does support.

`--filter-categories` (list)

A list of one or more Amazon Location categories to filter the returned places. If you include more than one category, the results will include results that match *any* of the categories listed.

For more information about using categories, including a list of Amazon Location categories, see [Categories and filtering](https://docs.aws.amazon.com/location/latest/developerguide/category-filtering.html) , in the *Amazon Location Service Developer Guide* .

(string)

Syntax:

```
"string" "string" ...
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

Summary -> (structure)

Contains a summary of the request. Echoes the input values for `BiasPosition` , `FilterBBox` , `FilterCountries` , `Language` , `MaxResults` , and `Text` . Also includes the `DataSource` of the place index and the bounding box, `ResultBBox` , which surrounds the search results.

Text -> (string)

The search text specified in the request.

BiasPosition -> (list)

Contains the coordinates for the optional bias position specified in the request.

This parameter contains a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.

For example, `[-123.1174, 49.2847]` represents the position with longitude `-123.1174` and latitude `49.2847` .

(double)

FilterBBox -> (list)

Contains the coordinates for the optional bounding box specified in the request.

(double)

FilterCountries -> (list)

Contains the optional country filter specified in the request.

(string)

MaxResults -> (integer)

Contains the optional result count limit specified in the request.

ResultBBox -> (list)

The bounding box that fully contains all search results.

### Note

If you specified the optional `FilterBBox` parameter in the request, `ResultBBox` is contained within `FilterBBox` .

(double)

DataSource -> (string)

The geospatial data provider attached to the place index resource specified in the request. Values can be one of the following:

- Esri
- Grab
- Here

For more information about data providers, see [Amazon Location Service data providers](https://docs.aws.amazon.com/location/latest/developerguide/what-is-data-provider.html) .

Language -> (string)

The preferred language used to return results. Matches the language in the request. The value is a valid [BCP 47](https://tools.ietf.org/search/bcp47) language tag, for example, `en` for English.

FilterCategories -> (list)

The optional category filter specified in the request.

(string)

Results -> (list)

A list of Places matching the input text. Each result contains additional information about the specific point of interest.

Not all response properties are included with all responses. Some properties may only be returned by specific data partners.

(structure)

Contains a search result from a text search query that is run on a place index resource.

Place -> (structure)

Details about the search result, such as its address and position.

Label -> (string)

The full name and address of the point of interest such as a city, region, or country. For example, `123 Any Street, Any Town, USA` .

Geometry -> (structure)

Places uses a point geometry to specify a location or a Place.

Point -> (list)

A single point geometry specifies a location for a Place using [WGS 84](https://gisgeography.com/wgs84-world-geodetic-system/) coordinates:

- *x* â Specifies the x coordinate or longitude.
- *y* â Specifies the y coordinate or latitude.

(double)

AddressNumber -> (string)

The numerical portion of an address, such as a building number.

Street -> (string)

The name for a street or a road to identify a location. For example, `Main Street` .

Neighborhood -> (string)

The name of a community district. For example, `Downtown` .

Municipality -> (string)

A name for a local area, such as a city or town name. For example, `Toronto` .

SubRegion -> (string)

A county, or an area thatâs part of a larger region. For example, `Metro Vancouver` .

Region -> (string)

A name for an area or geographical division, such as a province or state name. For example, `British Columbia` .

Country -> (string)

A country/region specified using [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) 3-digit country/region code. For example, `CAN` .

PostalCode -> (string)

A group of numbers and letters in a country-specific format, which accompanies the address for the purpose of identifying a location.

Interpolated -> (boolean)

`True` if the result is interpolated from other known places.

`False` if the Place is a known place.

Not returned when the partner does not provide the information.

For example, returns `False` for an address location that is found in the partner data, but returns `True` if an address does not exist in the partner data and its location is calculated by interpolating between other known addresses.

TimeZone -> (structure)

The time zone in which the `Place` is located. Returned only when using HERE or Grab as the selected partner.

Name -> (string)

The name of the time zone, following the [IANA time zone standard](https://www.iana.org/time-zones) . For example, `America/Los_Angeles` .

Offset -> (integer)

The time zoneâs offset, in seconds, from UTC.

UnitType -> (string)

For addresses with a `UnitNumber` , the type of unit. For example, `Apartment` .

### Note

Returned only for a place index that uses Esri as a data provider.

UnitNumber -> (string)

For addresses with multiple units, the unit identifier. Can include numbers and letters, for example `3B` or `Unit 123` .

### Note

Returned only for a place index that uses Esri or Grab as a data provider. Is not returned for `SearchPlaceIndexForPosition` .

Categories -> (list)

The Amazon Location categories that describe this Place.

For more information about using categories, including a list of Amazon Location categories, see [Categories and filtering](https://docs.aws.amazon.com/location/latest/developerguide/category-filtering.html) , in the *Amazon Location Service Developer Guide* .

(string)

SupplementalCategories -> (list)

Categories from the data provider that describe the Place that are not mapped to any Amazon Location categories.

(string)

SubMunicipality -> (string)

An area thatâs part of a larger municipality. For example, `Blissville` is a submunicipality in the Queen County in New York.

### Note

This property supported by Esri and OpenData. The Esri property is `district` , and the OpenData property is `borough` .

Distance -> (double)

The distance in meters of a great-circle arc between the bias position specified and the result. `Distance` will be returned only if a bias position was specified in the query.

### Note

A great-circle arc is the shortest path on a sphere, in this case the Earth. This returns the shortest distance between two locations.

Relevance -> (double)

The relative confidence in the match for a result among the results returned. For example, if more fields for an address match (including house number, street, city, country/region, and postal code), the relevance score is closer to 1.

Returned only when the partner selected is Esri or Grab.

PlaceId -> (string)

The unique identifier of the place. You can use this with the `GetPlace` operation to find the place again later.

### Note

For `SearchPlaceIndexForText` operations, the `PlaceId` is returned only by place indexes that use HERE or Grab as a data provider.