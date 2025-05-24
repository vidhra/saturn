# geocodeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-places/geocode.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-places/geocode.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [geo-places](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-places/index.html#cli-aws-geo-places) ]

# geocode

## Description

The `Geocode` action allows you to obtain coordinates, addresses, and other information about places.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/geo-places-2020-11-19/Geocode)

## Synopsis

```
geocode
[--query-text <value>]
[--query-components <value>]
[--max-results <value>]
[--bias-position <value>]
[--filter <value>]
[--additional-features <value>]
[--language <value>]
[--political-view <value>]
[--intended-use <value>]
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

`--query-text` (string)

The free-form text query to match addresses against. This is usually a partially typed address from an end user in an address box or form.

`--query-components` (structure)

A structured free text query allows you to search for places by the name or text representation of specific properties of the place.

Country -> (string)

The alpha-2 or alpha-3 character code for the country that the results will be present in.

Region -> (string)

The region or state results should be to be present in.

Example: `North Rhine-Westphalia` .

SubRegion -> (string)

The sub-region or county for which results should be present in.

Locality -> (string)

City or locality results should be present in.

Example: `Vancouver` .

District -> (string)

The district or division of a city the results should be present in.

Street -> (string)

The name of the street results should be present in.

AddressNumber -> (string)

The house number or address results should have.

PostalCode -> (string)

An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code for which the result should posses.

Shorthand Syntax:

```
Country=string,Region=string,SubRegion=string,Locality=string,District=string,Street=string,AddressNumber=string,PostalCode=string
```

JSON Syntax:

```
{
  "Country": "string",
  "Region": "string",
  "SubRegion": "string",
  "Locality": "string",
  "District": "string",
  "Street": "string",
  "AddressNumber": "string",
  "PostalCode": "string"
}
```

`--max-results` (integer)

An optional limit for the number of results returned in a single call.

`--bias-position` (list)

The position, in longitude and latitude, that the results should be close to. Typically, place results returned are ranked higher the closer they are to this position. Stored in `[lng, lat]` and in the WSG84 format.

### Note

The fields `BiasPosition` , `FilterBoundingBox` , and `FilterCircle` are mutually exclusive.

(double)

Syntax:

```
double double ...
```

`--filter` (structure)

A structure which contains a set of inclusion/exclusion properties that results must posses in order to be returned as a result.

IncludeCountries -> (list)

A list of countries that all results must be in. Countries are represented by either their alpha-2 or alpha-3 character codes.

(string)

IncludePlaceTypes -> (list)

The included place types.

(string)

Shorthand Syntax:

```
IncludeCountries=string,string,IncludePlaceTypes=string,string
```

JSON Syntax:

```
{
  "IncludeCountries": ["string", ...],
  "IncludePlaceTypes": ["Locality"|"PostalCode"|"Intersection"|"Street"|"PointAddress"|"InterpolatedAddress", ...]
}
```

`--additional-features` (list)

A list of optional additional parameters, such as time zone, that can be requested for each result.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  TimeZone
  Access
```

`--language` (string)

A list of [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag) compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.

`--political-view` (string)

The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.

`--intended-use` (string)

Indicates if the results will be stored. Defaults to `SingleUse` , if left empty.

Possible values:

- `SingleUse`
- `Storage`

`--key` (string)

Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.

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

PricingBucket -> (string)

The pricing bucket for which the query is charged at.

For more inforamtion on pricing, please visit [Amazon Location Service Pricing](https://aws.amazon.com/location/pricing/) .

ResultItems -> (list)

List of places or results returned for a query.

(structure)

The Geocoded result.

PlaceId -> (string)

The `PlaceId` of the place you wish to receive the information for.

PlaceType -> (string)

A `PlaceType` is a category that the result place must belong to.

Title -> (string)

The localized display name of this result item based on request parameter `language` .

Address -> (structure)

The placeâs address.

Label -> (string)

Assembled address value built out of the address components, according to the regional postal rules. This is the correctly formatted address.

Country -> (structure)

The country component of the address.

Code2 -> (string)

Country, represented by its alpha 2-character code.

Code3 -> (string)

Country, represented by its alpha t-character code.

Name -> (string)

Name of the country.

Region -> (structure)

The region or state results should be present in.

Example: `North Rhine-Westphalia` .

Code -> (string)

Abbreviated code for a the state, province or region of the country.

Example: `BC` .

Name -> (string)

Name for a the state, province, or region of the country.

Example: `British Columbia` .

SubRegion -> (structure)

The sub-region or county for which results should be present in.

Code -> (string)

Abbreviated code for the county or sub-region.

Name -> (string)

Name for the county or sub-region.

Locality -> (string)

The locality or city of the address.

Example: `Vancouver` .

District -> (string)

The district or division of a locality associated with this address.

SubDistrict -> (string)

A subdivision of a district.

Example: `Minden-LÃ¼bbecke` .

PostalCode -> (string)

An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code, for which the result should posses.

Block -> (string)

Name of the block.

Example: `Sunny Mansion 203 block: 2 Chome`

SubBlock -> (string)

Name of sub-block.

Example: `Sunny Mansion 203 sub-block: 4`

Intersection -> (list)

Name of the streets in the intersection.

Example: `["FriedrichstraÃe","Unter den Linden"]`

(string)

Street -> (string)

The name of the street results should be present in.

StreetComponents -> (list)

Components of the street.

Example: Younge from the âYounge streetâ.

(structure)

Components of a street.

BaseName -> (string)

Base name part of the street name.

Example: Younge from the âYounge streetâ.

Type -> (string)

Street type part of the street name.

Example: `âavenue"` .

TypePlacement -> (string)

Defines if the street type is before or after the base name.

TypeSeparator -> (string)

What character(s) separates the string from its type.

Prefix -> (string)

A prefix is a directional identifier that precedes, but is not included in, the base name of a road.

Example: E for East.

Suffix -> (string)

A suffix is a directional identifier that follows, but is not included in, the base name of a road.

Example W for West.

Direction -> (string)

Indicates the official directional identifiers assigned to highways.

Language -> (string)

A [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag) compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.

AddressNumber -> (string)

The number that identifies an address within a street.

Building -> (string)

The name of the building at the address.

AddressNumberCorrected -> (boolean)

Boolean indicating if the address provided has been corrected.

PostalCodeDetails -> (list)

Contains details about the postal code of the place/result.

(structure)

Contains details about the postal code of the place or result.

PostalCode -> (string)

An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code for which the result should posses.

PostalAuthority -> (string)

The postal authority or entity. This could be a governmental authority, a regulatory authority, or a designated postal operator.

PostalCodeType -> (string)

The postal code type.

UspsZip -> (structure)

The ZIP Classification Code, or in other words what type of postal code is it.

ZipClassificationCode -> (string)

The ZIP Classification Code, or in other words what type of postal code is it.

UspsZipPlus4 -> (structure)

The USPS ZIP+4 Record Type Code.

RecordTypeCode -> (string)

The USPS ZIP+4 Record Type Code.

Position -> (list)

The position in longitude and latitude.

(double)

Distance -> (long)

The distance in meters from the QueryPosition.

MapView -> (list)

The bounding box enclosing the geometric shape (area or line) that an individual result covers.

The bounding box formed is defined as a set 4 coordinates: `[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]`

(double)

Categories -> (list)

Categories of results that results must belong to.

(structure)

Category of the `Place` returned.

Id -> (string)

The category ID.

Name -> (string)

The category name.

LocalizedName -> (string)

Localized name of the category type.

Primary -> (boolean)

Boolean which indicates if this category is the primary offered by the place.

FoodTypes -> (list)

List of food types offered by this result.

(structure)

List of `Food` types offered by this result.

LocalizedName -> (string)

Localized name of the food type.

Id -> (string)

The Food Type Id.

Primary -> (boolean)

Boolean which indicates if this food type is the primary offered by the place. For example, if a location serves fast food, but also dessert, he primary would likely be fast food.

AccessPoints -> (list)

Position of the access point represent by longitude and latitude.

(structure)

Position of the access point represented by longitude and latitude for a vehicle.

Position -> (list)

The position, in longitude and latitude.

(double)

TimeZone -> (structure)

The time zone in which the place is located.

Name -> (string)

The time zone name.

Offset -> (string)

Time zone offset of the timezone from UTC.

OffsetSeconds -> (long)

The offset of the time zone from UTC, in seconds.

PoliticalView -> (string)

The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.

MatchScores -> (structure)

Indicates how well the entire input matches the returned. It is equal to 1 if all input tokens are recognized and matched.

Overall -> (double)

Indicates how well the entire input matches the returned. It is equal to 1 if all input tokens are recognized and matched.

Components -> (structure)

Indicates how well the component input matches the returned. It is equal to 1 if all input tokens are recognized and matched.

Title -> (double)

Indicates the starting and ending index of the title in the text query that match the found title.

Address -> (structure)

The placeâs address.

Country -> (double)

The alpha-2 or alpha-3 character code for the country that the results will be present in.

Region -> (double)

The region or state results should be to be present in.

Example: `North Rhine-Westphalia` .

SubRegion -> (double)

The sub-region or county for which results should be present in.

Locality -> (double)

The city or locality results should be present in.

Example: `Vancouver` .

District -> (double)

The district or division of a city the results should be present in.

SubDistrict -> (double)

A subdivision of a district.

Example: `Minden-LÃ¼bbecke`

PostalCode -> (double)

An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code, for which the result should posses.

Block -> (double)

Name of the block.

Example: `Sunny Mansion 203 block: 2 Chome`

SubBlock -> (double)

Name of sub-block.

Example: `Sunny Mansion 203 sub-block: 4`

Intersection -> (list)

Name of the streets in the intersection.

Example: `["FriedrichstraÃe","Unter den Linden"]`

(double)

AddressNumber -> (double)

The house number or address results should have.

Building -> (double)

The name of the building at the address.