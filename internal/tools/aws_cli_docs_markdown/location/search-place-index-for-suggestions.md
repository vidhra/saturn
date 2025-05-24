# search-place-index-for-suggestionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/search-place-index-for-suggestions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/search-place-index-for-suggestions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [location](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/index.html#cli-aws-location) ]

# search-place-index-for-suggestions

## Description

Generates suggestions for addresses and points of interest based on partial or misspelled free-form text. This operation is also known as autocomplete, autosuggest, or fuzzy matching.

Optional parameters let you narrow your search results by bounding box or country, or bias your search toward a specific position on the globe.

### Note

You can search for suggested place names near a specified position by using `BiasPosition` , or filter results within a bounding box by using `FilterBBox` . These parameters are mutually exclusive; using both `BiasPosition` and `FilterBBox` in the same command returns an error.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/location-2020-11-19/SearchPlaceIndexForSuggestions)

## Synopsis

```
search-place-index-for-suggestions
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

The free-form partial text to use to generate place suggestions. For example, `eiffel tow` .

`--bias-position` (list)

An optional parameter that indicates a preference for place suggestions that are closer to a specified position.

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

An optional parameter that limits the search results by returning only suggestions within a specified bounding box.

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

An optional parameter that limits the search results by returning only suggestions within the provided list of countries.

- Use the [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) 3-digit country code. For example, Australia uses three upper-case characters: `AUS` .

(string)

Syntax:

```
"string" "string" ...
```

`--max-results` (integer)

An optional parameter. The maximum number of results returned per request.

The default: `5`

`--language` (string)

The preferred language used to return results. The value must be a valid [BCP 47](https://tools.ietf.org/search/bcp47) language tag, for example, `en` for English.

This setting affects the languages used in the results. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.

For an example, weâll use the Greek language. You search for `Athens, Gr` to get suggestions with the `language` parameter set to `en` . The results found will most likely be returned as `Athens, Greece` .

If you set the `language` parameter to `el` , for Greek, then the result found will more likely be returned as `ÎÎ¸Î®Î½Î±, ÎÎ»Î»Î¬Î´Î±` .

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

Contains a summary of the request. Echoes the input values for `BiasPosition` , `FilterBBox` , `FilterCountries` , `Language` , `MaxResults` , and `Text` . Also includes the `DataSource` of the place index.

Text -> (string)

The free-form partial text input specified in the request.

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

A list of place suggestions that best match the search text.

(structure)

Contains a place suggestion resulting from a place suggestion query that is run on a place index resource.

Text -> (string)

The text of the place suggestion, typically formatted as an address string.

PlaceId -> (string)

The unique identifier of the Place. You can use this with the `GetPlace` operation to find the place again later, or to get full information for the Place.

The `GetPlace` request must use the same `PlaceIndex` resource as the `SearchPlaceIndexForSuggestions` that generated the Place ID.

### Note

For `SearchPlaceIndexForSuggestions` operations, the `PlaceId` is returned by place indexes that use Esri, Grab, or HERE as data providers.

Categories -> (list)

The Amazon Location categories that describe the Place.

For more information about using categories, including a list of Amazon Location categories, see [Categories and filtering](https://docs.aws.amazon.com/location/latest/developerguide/category-filtering.html) , in the *Amazon Location Service Developer Guide* .

(string)

SupplementalCategories -> (list)

Categories from the data provider that describe the Place that are not mapped to any Amazon Location categories.

(string)