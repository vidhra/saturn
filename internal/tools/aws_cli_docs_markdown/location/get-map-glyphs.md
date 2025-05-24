# get-map-glyphsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/get-map-glyphs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/get-map-glyphs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [location](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/index.html#cli-aws-location) ]

# get-map-glyphs

## Description

Retrieves glyphs used to display labels on a map.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/location-2020-11-19/GetMapGlyphs)

## Synopsis

```
get-map-glyphs
--map-name <value>
--font-stack <value>
--font-unicode-range <value>
[--key <value>]
<outfile>
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

`--map-name` (string)

The map resource associated with the glyph ï¬le.

`--font-stack` (string)

A comma-separated list of fonts to load glyphs from in order of preference. For example, `Noto Sans Regular, Arial Unicode` .

Valid font stacks for [Esri](https://docs.aws.amazon.com/location/latest/developerguide/esri.html) styles:

- VectorEsriDarkGrayCanvas â `Ubuntu Medium Italic` | `Ubuntu Medium` | `Ubuntu Italic` | `Ubuntu Regular` | `Ubuntu Bold`
- VectorEsriLightGrayCanvas â `Ubuntu Italic` | `Ubuntu Regular` | `Ubuntu Light` | `Ubuntu Bold`
- VectorEsriTopographic â `Noto Sans Italic` | `Noto Sans Regular` | `Noto Sans Bold` | `Noto Serif Regular` | `Roboto Condensed Light Italic`
- VectorEsriStreets â `Arial Regular` | `Arial Italic` | `Arial Bold`
- VectorEsriNavigation â `Arial Regular` | `Arial Italic` | `Arial Bold`

Valid font stacks for [HERE Technologies](https://docs.aws.amazon.com/location/latest/developerguide/HERE.html) styles:

- VectorHereContrast â `Fira GO Regular` | `Fira GO Bold`
- VectorHereExplore, VectorHereExploreTruck, HybridHereExploreSatellite â `Fira GO Italic` | `Fira GO Map` | `Fira GO Map Bold` | `Noto Sans CJK JP Bold` | `Noto Sans CJK JP Light` | `Noto Sans CJK JP Regular`

Valid font stacks for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/grab.html) styles:

- VectorGrabStandardLight, VectorGrabStandardDark â `Noto Sans Regular` | `Noto Sans Medium` | `Noto Sans Bold`

Valid font stacks for [Open Data](https://docs.aws.amazon.com/location/latest/developerguide/open-data.html) styles:

- VectorOpenDataStandardLight, VectorOpenDataStandardDark, VectorOpenDataVisualizationLight, VectorOpenDataVisualizationDark â `Amazon Ember Regular,Noto Sans Regular` | `Amazon Ember Bold,Noto Sans Bold` | `Amazon Ember Medium,Noto Sans Medium` | `Amazon Ember Regular Italic,Noto Sans Italic` | `Amazon Ember Condensed RC Regular,Noto Sans Regular` | `Amazon Ember Condensed RC Bold,Noto Sans Bold` | `Amazon Ember Regular,Noto Sans Regular,Noto Sans Arabic Regular` | `Amazon Ember Condensed RC Bold,Noto Sans Bold,Noto Sans Arabic Condensed Bold` | `Amazon Ember Bold,Noto Sans Bold,Noto Sans Arabic Bold` | `Amazon Ember Regular Italic,Noto Sans Italic,Noto Sans Arabic Regular` | `Amazon Ember Condensed RC Regular,Noto Sans Regular,Noto Sans Arabic Condensed Regular` | `Amazon Ember Medium,Noto Sans Medium,Noto Sans Arabic Medium`

### Note

The fonts used by the Open Data map styles are combined fonts that use `Amazon Ember` for most glyphs but `Noto Sans` for glyphs unsupported by `Amazon Ember` .

`--font-unicode-range` (string)

A Unicode range of characters to download glyphs for. Each response will contain 256 characters. For example, 0â255 includes all characters from range `U+0000` to `00FF` . Must be aligned to multiples of 256.

`--key` (string)

The optional [API key](https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html) to authorize the request.

`outfile` (string)
Filename where the content will be saved

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

Blob -> (blob)

The glyph, as binary blob.

ContentType -> (string)

The map glyph content type. For example, `application/octet-stream` .

CacheControl -> (string)

The HTTP Cache-Control directive for the value.