# list-geo-locationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-geo-locations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-geo-locations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# list-geo-locations

## Description

Retrieves a list of supported geographic locations.

Countries are listed first, and continents are listed last. If Amazon Route 53 supports subdivisions for a country (for example, states or provinces), the subdivisions for that country are listed in alphabetical order immediately after the corresponding country.

Route 53 does not perform authorization for this API because it retrieves information that is already available to the public.

For a list of supported geolocation codes, see the [GeoLocation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GeoLocation.html) data type.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListGeoLocations)

## Synopsis

```
list-geo-locations
[--start-continent-code <value>]
[--start-country-code <value>]
[--start-subdivision-code <value>]
[--max-items <value>]
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

`--start-continent-code` (string)

The code for the continent with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if `IsTruncated` is true, and if `NextContinentCode` from the previous response has a value, enter that value in `startcontinentcode` to return the next page of results.

Include `startcontinentcode` only if you want to list continents. Donât include `startcontinentcode` when youâre listing countries or countries with their subdivisions.

`--start-country-code` (string)

The code for the country with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if `IsTruncated` is `true` , and if `NextCountryCode` from the previous response has a value, enter that value in `startcountrycode` to return the next page of results.

`--start-subdivision-code` (string)

The code for the state of the United States with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if `IsTruncated` is `true` , and if `NextSubdivisionCode` from the previous response has a value, enter that value in `startsubdivisioncode` to return the next page of results.

To list subdivisions (U.S. states), you must include both `startcountrycode` and `startsubdivisioncode` .

`--max-items` (string)

(Optional) The maximum number of geolocations to be included in the response body for this request. If more than `maxitems` geolocations remain to be listed, then the value of the `IsTruncated` element in the response is `true` .

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

GeoLocationDetailsList -> (list)

A complex type that contains one `GeoLocationDetails` element for each location that Amazon Route 53 supports for geolocation.

(structure)

A complex type that contains the codes and full continent, country, and subdivision names for the specified `geolocation` code.

ContinentCode -> (string)

The two-letter code for the continent.

ContinentName -> (string)

The full name of the continent.

CountryCode -> (string)

The two-letter code for the country.

CountryName -> (string)

The name of the country.

SubdivisionCode -> (string)

The code for the subdivision, such as a particular state within the United States. For a list of US state abbreviations, see [Appendix B: TwoâLetter State and Possession Abbreviations](https://pe.usps.com/text/pub28/28apb.htm) on the United States Postal Service website. For a list of all supported subdivision codes, use the [ListGeoLocations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListGeoLocations.html) API.

SubdivisionName -> (string)

The full name of the subdivision. Route 53 currently supports only states in the United States.

IsTruncated -> (boolean)

A value that indicates whether more locations remain to be listed after the last location in this response. If so, the value of `IsTruncated` is `true` . To get more values, submit another request and include the values of `NextContinentCode` , `NextCountryCode` , and `NextSubdivisionCode` in the `startcontinentcode` , `startcountrycode` , and `startsubdivisioncode` , as applicable.

NextContinentCode -> (string)

If `IsTruncated` is `true` , you can make a follow-up request to display more locations. Enter the value of `NextContinentCode` in the `startcontinentcode` parameter in another `ListGeoLocations` request.

NextCountryCode -> (string)

If `IsTruncated` is `true` , you can make a follow-up request to display more locations. Enter the value of `NextCountryCode` in the `startcountrycode` parameter in another `ListGeoLocations` request.

NextSubdivisionCode -> (string)

If `IsTruncated` is `true` , you can make a follow-up request to display more locations. Enter the value of `NextSubdivisionCode` in the `startsubdivisioncode` parameter in another `ListGeoLocations` request.

MaxItems -> (string)

The value that you specified for `MaxItems` in the request.