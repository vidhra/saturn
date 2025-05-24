# describe-mapÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/describe-map.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/describe-map.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [location](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/index.html#cli-aws-location) ]

# describe-map

## Description

Retrieves the map resource details.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/location-2020-11-19/DescribeMap)

## Synopsis

```
describe-map
--map-name <value>
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

`--map-name` (string)

The name of the map resource.

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

MapName -> (string)

The map style selected from an available provider.

MapArn -> (string)

The Amazon Resource Name (ARN) for the map resource. Used to specify a resource across all Amazon Web Services.

- Format example: `arn:aws:geo:region:account-id:map/ExampleMap`

PricingPlan -> (string)

No longer used. Always returns `RequestBasedUsage` .

DataSource -> (string)

Specifies the data provider for the associated map tiles.

Configuration -> (structure)

Specifies the map tile style selected from a partner data provider.

Style -> (string)

Specifies the map style selected from an available data provider.

Valid [Esri map styles](https://docs.aws.amazon.com/location/latest/developerguide/esri.html) :

- `VectorEsriDarkGrayCanvas` â The Esri Dark Gray Canvas map style. A vector basemap with a dark gray, neutral background with minimal colors, labels, and features thatâs designed to draw attention to your thematic content.
- `RasterEsriImagery` â The Esri Imagery map style. A raster basemap that provides one meter or better satellite and aerial imagery in many parts of the world and lower resolution satellite imagery worldwide.
- `VectorEsriLightGrayCanvas` â The Esri Light Gray Canvas map style, which provides a detailed vector basemap with a light gray, neutral background style with minimal colors, labels, and features thatâs designed to draw attention to your thematic content.
- `VectorEsriTopographic` â The Esri Light map style, which provides a detailed vector basemap with a classic Esri map style.
- `VectorEsriStreets` â The Esri Street Map style, which provides a detailed vector basemap for the world symbolized with a classic Esri street map style. The vector tile layer is similar in content and style to the World Street Map raster map.
- `VectorEsriNavigation` â The Esri Navigation map style, which provides a detailed basemap for the world symbolized with a custom navigation map style thatâs designed for use during the day in mobile devices.

Valid [HERE Technologies map styles](https://docs.aws.amazon.com/location/latest/developerguide/HERE.html) :

- `VectorHereContrast` â The HERE Contrast (Berlin) map style is a high contrast detailed base map of the world that blends 3D and 2D rendering.

### Note

The `VectorHereContrast` style has been renamed from `VectorHereBerlin` . `VectorHereBerlin` has been deprecated, but will continue to work in applications that use it.

- `VectorHereExplore` â A default HERE map style containing a neutral, global map and its features including roads, buildings, landmarks, and water features. It also now includes a fully designed map of Japan.
- `VectorHereExploreTruck` â A global map containing truck restrictions and attributes (e.g. width / height / HAZMAT) symbolized with highlighted segments and icons on top of HERE Explore to support use cases within transport and logistics.
- `RasterHereExploreSatellite` â A global map containing high resolution satellite imagery.
- `HybridHereExploreSatellite` â A global map displaying the road network, street names, and city labels over satellite imagery. This style will automatically retrieve both raster and vector tiles, and your charges will be based on total tiles retrieved.

### Note

Hybrid styles use both vector and raster tiles when rendering the map that you see. This means that more tiles are retrieved than when using either vector or raster tiles alone. Your charges will include all tiles retrieved.

Valid [GrabMaps map styles](https://docs.aws.amazon.com/location/latest/developerguide/grab.html) :

- `VectorGrabStandardLight` â The Grab Standard Light map style provides a basemap with detailed land use coloring, area names, roads, landmarks, and points of interest covering Southeast Asia.
- `VectorGrabStandardDark` â The Grab Standard Dark map style provides a dark variation of the standard basemap covering Southeast Asia.

### Note

Grab provides maps only for countries in Southeast Asia, and is only available in the Asia Pacific (Singapore) Region (`ap-southeast-1` ). For more information, see [GrabMaps countries and area covered](https://docs.aws.amazon.com/location/latest/developerguide/grab.html#grab-coverage-area) .

Valid [Open Data map styles](https://docs.aws.amazon.com/location/latest/developerguide/open-data.html) :

- `VectorOpenDataStandardLight` â The Open Data Standard Light map style provides a detailed basemap for the world suitable for website and mobile application use. The map includes highways major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries.
- `VectorOpenDataStandardDark` â Open Data Standard Dark is a dark-themed map style that provides a detailed basemap for the world suitable for website and mobile application use. The map includes highways major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries.
- `VectorOpenDataVisualizationLight` â The Open Data Visualization Light map style is a light-themed style with muted colors and fewer features that aids in understanding overlaid data.
- `VectorOpenDataVisualizationDark` â The Open Data Visualization Dark map style is a dark-themed style with muted colors and fewer features that aids in understanding overlaid data.

PoliticalView -> (string)

Specifies the political view for the style. Leave unset to not use a political view, or, for styles that support specific political views, you can choose a view, such as `IND` for the Indian view.

Default is unset.

### Note

Not all map resources or styles support political view styles. See [Political views](https://docs.aws.amazon.com/location/latest/developerguide/map-concepts.html#political-views) for more information.

CustomLayers -> (list)

Specifies the custom layers for the style. Leave unset to not enable any custom layer, or, for styles that support custom layers, you can enable layer(s), such as POI layer for the VectorEsriNavigation style. Default is `unset` .

### Note

Not all map resources or styles support custom layers. See Custom Layers for more information.

(string)

Description -> (string)

The optional description for the map resource.

Tags -> (map)

Tags associated with the map resource.

key -> (string)

value -> (string)

CreateTime -> (timestamp)

The timestamp for when the map resource was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ` .

UpdateTime -> (timestamp)

The timestamp for when the map resource was last update in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ` .