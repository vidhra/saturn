# autocompleteÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-places/autocomplete.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-places/autocomplete.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [geo-places](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-places/index.html#cli-aws-geo-places) ]

# autocomplete

## Description

The autocomplete operation speeds up and increases the accuracy of entering addresses by providing a list of address candidates matching a partially entered address. Results are sorted from most to least matching. Filtering and biasing can be used to increase the relevance of the results if additional search context is known

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/geo-places-2020-11-19/Autocomplete)

## Synopsis

```
autocomplete
--query-text <value>
[--max-results <value>]
[--bias-position <value>]
[--filter <value>]
[--postal-code-mode <value>]
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

`--max-results` (integer)

An optional limit for the number of results returned in a single call.

`--bias-position` (list)

The position in longitude and latitude that the results should be close to. Typically, place results returned are ranked higher the closer they are to this position. Stored in `[lng, lat]` and in the WSG84 format.

### Note

The fields `BiasPosition` , `FilterBoundingBox` , and `FilterCircle` are mutually exclusive.

(double)

Syntax:

```
double double ...
```

`--filter` (structure)

A structure which contains a set of inclusion/exclusion properties that results must posses in order to be returned as a result.

BoundingBox -> (list)

The bounding box enclosing the geometric shape (area or line) that an individual result covers.

The bounding box formed is defined as a set 4 coordinates: `[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]`

(double)

Circle -> (structure)

The `Circle` that all results must be in.

Center -> (list)

The center position, in longitude and latitude, of the `FilterCircle` .

(double)

Radius -> (long)

The radius, in meters, of the `FilterCircle` .

IncludeCountries -> (list)

A list of countries that all results must be in. Countries are represented by either their alpha-2 or alpha-3 character codes.

(string)

IncludePlaceTypes -> (list)

The included place types.

(string)

Shorthand Syntax:

```
BoundingBox=double,double,Circle={Center=[double,double],Radius=long},IncludeCountries=string,string,IncludePlaceTypes=string,string
```

JSON Syntax:

```
{
  "BoundingBox": [double, ...],
  "Circle": {
    "Center": [double, ...],
    "Radius": long
  },
  "IncludeCountries": ["string", ...],
  "IncludePlaceTypes": ["Locality"|"PostalCode", ...]
}
```

`--postal-code-mode` (string)

The `PostalCodeMode` affects how postal code results are returned. If a postal code spans multiple localities and this value is empty, partial district or locality information may be returned under a single postal code result entry. If itâs populated with the value `cityLookup` , all cities in that postal code are returned.

Possible values:

- `MergeAllSpannedLocalities`
- `EnumerateSpannedLocalities`

`--additional-features` (list)

A list of optional additional parameters that can be requested for each result.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  Core
```

`--language` (string)

A list of [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag) compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.

`--political-view` (string)

The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.

`--intended-use` (string)

Indicates if the results will be stored. Defaults to `SingleUse` , if left empty.

Possible values:

- `SingleUse`

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

A result matching the input query text.

PlaceId -> (string)

The PlaceId of the place associated with this result. This can be used to look up additional details about the result via GetPlace.

PlaceType -> (string)

PlaceType describes the type of result entry returned.

Title -> (string)

A formatted string for display when presenting this result to an end user.

Address -> (structure)

The address associated with this result.

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

Distance -> (long)

The distance in meters between the center of the search area and this result. Useful to evaluate how far away from the original bias position the result is.

Language -> (string)

A list of [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag) compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.

PoliticalView -> (string)

The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.

Highlights -> (structure)

Indicates the starting and ending index of the place in the text query that match the found title.

Title -> (list)

Indicates where the title field in the result matches the input query.

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

Address -> (structure)

Describes how part of the result address match the input query.

Label -> (list)

Indicates the starting and ending indexes for result items where they are identified to match the input query. This should be used to provide emphasis to output display to make selecting the correct result from a list easier for end users.

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

Country -> (structure)

The alpha-2 or alpha-3 character code for the country that the results will be present in.

Code -> (list)

Indicates the starting and ending index of the country code in the text query that match the found title.

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

Name -> (list)

Indicates the starting and ending index of the country code in the text query that match the found title.

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

Region -> (structure)

The region or state results should be to be present in.

Example: `North Rhine-Westphalia` .

Code -> (list)

Indicates the starting and ending index of the region in the text query that match the found title.

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

Name -> (list)

Indicates the starting and ending index of the region name in the text query that match the found title.

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

SubRegion -> (structure)

The sub-region or county for which results should be present in.

Code -> (list)

Indicates the starting and ending index of the sub-region in the text query that match the found title.

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

Name -> (list)

Indicates the starting and ending index of the name in the text query that match the found title.

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

Locality -> (list)

The city or locality results should be present in.

Example: `Vancouver` .

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

District -> (list)

The district or division of a city the results should be present in.

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

SubDistrict -> (list)

Indicates the starting and ending index of the title in the text query that match the found title.

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

Street -> (list)

The name of the street results should be present in.

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

Block -> (list)

Name of the block. Example: Sunny Mansion 203 block: 2 Chome

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

SubBlock -> (list)

Name of sub-block. Example Sunny Mansion 203 sub-block: 4

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

Intersection -> (list)

Name of the streets in the intersection. For example: e.g. [âFriedrichstraÃeâ,âUnter den Lindenâ]

(list)

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

PostalCode -> (list)

An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code for which the result should posses.

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

AddressNumber -> (list)

The house number or address results should have.

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.

Building -> (list)

The name of the building at the address.

(structure)

Describes how parts of the result response match the input query.

StartIndex -> (integer)

Start index of the highlight.

EndIndex -> (integer)

End index of the highlight.

Value -> (string)

The highlightâs value.