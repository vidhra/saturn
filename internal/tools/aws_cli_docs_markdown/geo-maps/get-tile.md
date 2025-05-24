# get-tileÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-maps/get-tile.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-maps/get-tile.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [geo-maps](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-maps/index.html#cli-aws-geo-maps) ]

# get-tile

## Description

`GetTile` returns a tile. Map tiles are used by clients to render a map. theyâre addressed using a grid arrangement with an X coordinate, Y coordinate, and Z (zoom) level.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/geo-maps-2020-11-19/GetTile)

## Synopsis

```
get-tile
--tileset <value>
--z <value>
--x <value>
--y <value>
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

`--tileset` (string)

Specifies the desired tile set.

Valid Values: `raster.satellite | vector.basemap`

`--z` (string)

The zoom value for the map tile.

`--x` (string)

The X axis value for the map tile. Must be between 0 and 19.

`--y` (string)

The Y axis value for the map tile.

`--key` (string)

Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.

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

The blob represents a vector tile in `mvt` or a raster tile in an image format.

ContentType -> (string)

Header that represents the format of the response. The response returns the following as the HTTP body.

CacheControl -> (string)

Header that instructs caching configuration for the client.

ETag -> (string)

The pricing bucket for which the request is charged at.

PricingBucket -> (string)

The pricing bucket for which the request is charged at.