# get-static-mapÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-maps/get-static-map.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-maps/get-static-map.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [geo-maps](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-maps/index.html#cli-aws-geo-maps) ]

# get-static-map

## Description

`GetStaticMap` provides high-quality static map images with customizable options. You can modify the mapâs appearance and overlay additional information. Itâs an ideal solution for applications requiring tailored static map snapshots.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/geo-maps-2020-11-19/GetStaticMap)

## Synopsis

```
get-static-map
[--bounding-box <value>]
[--bounded-positions <value>]
[--center <value>]
[--color-scheme <value>]
[--compact-overlay <value>]
[--crop-labels | --no-crop-labels]
[--geo-json-overlay <value>]
--height <value>
[--key <value>]
[--label-size <value>]
[--language <value>]
[--padding <value>]
[--political-view <value>]
[--points-of-interests <value>]
[--radius <value>]
--file-name <value>
[--scale-bar-unit <value>]
[--style <value>]
--width <value>
[--zoom <value>]
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

`--bounding-box` (string)

Takes in two pairs of coordinates, [Lon, Lat], denoting south-westerly and north-easterly edges of the image. The underlying area becomes the view of the image.

Example: -123.17075,49.26959,-123.08125,49.31429

`--bounded-positions` (string)

Takes in two or more pair of coordinates, [Lon, Lat], with each coordinate separated by a comma. The API will generate an image to encompass all of the provided coordinates.

### Note

Cannot be used with `Zoom` and or `Radius`

Example: 97.170451,78.039098,99.045536,27.176178

`--center` (string)

Takes in a pair of coordinates, [Lon, Lat], which becomes the center point of the image. This parameter requires that either zoom or radius is set.

### Note

Cannot be used with `Zoom` and or `Radius`

Example: 49.295,-123.108

`--color-scheme` (string)

Sets color tone for map, such as dark and light for specific map styles. It only applies to vector map styles, such as Standard.

Example: `Light`

Default value: `Light`

### Note

Valid values for `ColorScheme` are case sensitive.

Possible values:

- `Light`
- `Dark`

`--compact-overlay` (string)

Takes in a string to draw geometries on the image. The input is a comma separated format as follows format: `[Lon, Lat]`

Example: `line:-122.407653,37.798557,-122.413291,37.802443;color=%23DD0000;width=7;outline-color=#00DD00;outline-width=5yd|point:-122.40572,37.80004;label=Fog Hill Market;size=large;text-color=%23DD0000;color=#EE4B2B`

### Note

Currently it supports the following geometry types: point, line and polygon. It does not support multiPoint , multiLine and multiPolgyon.

`--crop-labels` | `--no-crop-labels` (boolean)

It is a flag that takes in true or false. It prevents the labels that are on the edge of the image from being cut or obscured.

`--geo-json-overlay` (string)

Takes in a string to draw geometries on the image. The input is a valid GeoJSON collection object.

Example: `{"type":"FeatureCollection","features": [{"type":"Feature","geometry":{"type":"MultiPoint","coordinates": [[-90.076345,51.504107],[-0.074451,51.506892]]},"properties": {"color":"#00DD00"}}]}`

`--height` (integer)

Specifies the height of the map image.

`--key` (string)

Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.

`--label-size` (string)

Overrides the label size auto-calculated by `FileName` . Takes in one of the values - `Small` or `Large` .

Possible values:

- `Small`
- `Large`

`--language` (string)

Specifies the language on the map labels using the BCP 47 language tag, limited to ISO 639-1 two-letter language codes. If the specified language data isnât available for the map image, the labels will default to the regional primary language.

Supported codes:

- `ar`
- `as`
- `az`
- `be`
- `bg`
- `bn`
- `bs`
- `ca`
- `cs`
- `cy`
- `da`
- `de`
- `el`
- `en`
- `es`
- `et`
- `eu`
- `fi`
- `fo`
- `fr`
- `ga`
- `gl`
- `gn`
- `gu`
- `he`
- `hi`
- `hr`
- `hu`
- `hy`
- `id`
- `is`
- `it`
- `ja`
- `ka`
- `kk`
- `km`
- `kn`
- `ko`
- `ky`
- `lt`
- `lv`
- `mk`
- `ml`
- `mr`
- `ms`
- `mt`
- `my`
- `nl`
- `no`
- `or`
- `pa`
- `pl`
- `pt`
- `ro`
- `ru`
- `sk`
- `sl`
- `sq`
- `sr`
- `sv`
- `ta`
- `te`
- `th`
- `tr`
- `uk`
- `uz`
- `vi`
- `zh`

`--padding` (integer)

Applies additional space (in pixels) around overlay feature to prevent them from being cut or obscured.

### Note

Value for max and min is determined by:

Min: `1`

Max: `min(height, width)/4`

Example: `100`

`--political-view` (string)

Specifies the political view, using ISO 3166-2 or ISO 3166-3 country code format.

The following political views are currently supported:

- `ARG` : Argentinaâs view on the Southern Patagonian Ice Field and Tierra Del Fuego, including the Falkland Islands, South Georgia, and South Sandwich Islands
- `EGY` : Egyptâs view on Bir Tawil
- `IND` : Indiaâs view on Gilgit-Baltistan
- `KEN` : Kenyaâs view on the Ilemi Triangle
- `MAR` : Moroccoâs view on Western Sahara
- `RUS` : Russiaâs view on Crimea
- `SDN` : Sudanâs view on the Halaib Triangle
- `SRB` : Serbiaâs view on Kosovo, Vukovar, and Sarengrad Islands
- `SUR` : Surinameâs view on the Courantyne Headwaters and Lawa Headwaters
- `SYR` : Syriaâs view on the Golan Heights
- `TUR` : Turkeyâs view on Cyprus and Northern Cyprus
- `TZA` : Tanzaniaâs view on Lake Malawi
- `URY` : Uruguayâs view on Rincon de Artigas
- `VNM` : Vietnamâs view on the Paracel Islands and Spratly Islands

`--points-of-interests` (string)

Determines if the result image will display icons representing points of interest on the map.

Possible values:

- `Enabled`
- `Disabled`

`--radius` (long)

Used with center parameter, it specifies the zoom of the image where you can control it on a granular level. Takes in any value `>= 1` .

Example: `1500`

### Note

Cannot be used with `Zoom` .

**Unit** : `Meters`

`--file-name` (string)

The map scaling parameter to size the image, icons, and labels. It follows the pattern of `^map(@2x)?$` .

Example: `map, map@2x`

`--scale-bar-unit` (string)

Displays a scale on the bottom right of the map image with the unit specified in the input.

Example: `KilometersMiles, Miles, Kilometers, MilesKilometers`

Possible values:

- `Kilometers`
- `KilometersMiles`
- `Miles`
- `MilesKilometers`

`--style` (string)

`Style` specifies the desired map style.

Possible values:

- `Satellite`
- `Standard`

`--width` (integer)

Specifies the width of the map image.

`--zoom` (float)

Specifies the zoom level of the map image.

### Note

Cannot be used with `Radius` .

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

The blob represents a map image as a `jpeg` for the `GetStaticMap` API.

ContentType -> (string)

Header that represents the format of the response. The response returns the following as the HTTP body.

CacheControl -> (string)

Header that instructs caching configuration for the client.

ETag -> (string)

The static mapâs Etag.

PricingBucket -> (string)

The pricing bucket for which the request is charged at.