# create-place-indexÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/create-place-index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/create-place-index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [location](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/index.html#cli-aws-location) ]

# create-place-index

## Description

Creates a place index resource in your Amazon Web Services account. Use a place index resource to geocode addresses and other text queries by using the `SearchPlaceIndexForText` operation, and reverse geocode coordinates by using the `SearchPlaceIndexForPosition` operation, and enable autosuggestions by using the `SearchPlaceIndexForSuggestions` operation.

### Note

If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the [Amazon Web Services service terms](http://aws.amazon.com/service-terms) for more details.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/location-2020-11-19/CreatePlaceIndex)

## Synopsis

```
create-place-index
--index-name <value>
--data-source <value>
[--pricing-plan <value>]
[--description <value>]
[--data-source-configuration <value>]
[--tags <value>]
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

The name of the place index resource.

Requirements:

- Contain only alphanumeric characters (AâZ, aâz, 0â9), hyphens (-), periods (.), and underscores (_).
- Must be a unique place index resource name.
- No spaces allowed. For example, `ExamplePlaceIndex` .

`--data-source` (string)

Specifies the geospatial data provider for the new place index.

### Note

This field is case-sensitive. Enter the valid values as shown. For example, entering `HERE` returns an error.

Valid values include:

- `Esri` â For additional information about [Esri](https://docs.aws.amazon.com/location/latest/developerguide/esri.html) âs coverage in your region of interest, see [Esri details on geocoding coverage](https://developers.arcgis.com/rest/geocode/api-reference/geocode-coverage.htm) .
- `Grab` â Grab provides place index functionality for Southeast Asia. For additional information about [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/grab.html) â coverage, see [GrabMaps countries and areas covered](https://docs.aws.amazon.com/location/latest/developerguide/grab.html#grab-coverage-area) .
- `Here` â For additional information about [HERE Technologies](https://docs.aws.amazon.com/location/latest/developerguide/HERE.html) â coverage in your region of interest, see [HERE details on goecoding coverage](https://developer.here.com/documentation/geocoder/dev_guide/topics/coverage-geocoder.html) .

### Warning

If you specify HERE Technologies (`Here` ) as the data provider, you may not [store results](https://docs.aws.amazon.com/location-places/latest/APIReference/API_DataSourceConfiguration.html) for locations in Japan. For more information, see the [Amazon Web Services Service Terms](http://aws.amazon.com/service-terms/) for Amazon Location Service.

For additional information , see [Data providers](https://docs.aws.amazon.com/location/latest/developerguide/what-is-data-provider.html) on the *Amazon Location Service Developer Guide* .

`--pricing-plan` (string)

No longer used. If included, the only allowed value is `RequestBasedUsage` .

Possible values:

- `RequestBasedUsage`
- `MobileAssetTracking`
- `MobileAssetManagement`

`--description` (string)

The optional description for the place index resource.

`--data-source-configuration` (structure)

Specifies the data storage option requesting Places.

IntendedUse -> (string)

Specifies how the results of an operation will be stored by the caller.

Valid values include:

- `SingleUse` specifies that the results wonât be stored.
- `Storage` specifies that the result can be cached or stored in a database.

Default value: `SingleUse`

Shorthand Syntax:

```
IntendedUse=string
```

JSON Syntax:

```
{
  "IntendedUse": "SingleUse"|"Storage"
}
```

`--tags` (map)

Applies one or more tags to the place index resource. A tag is a key-value pair that helps you manage, identify, search, and filter your resources.

Format: `"key" : "value"`

Restrictions:

- Maximum 50 tags per resource.
- Each tag key must be unique and must have exactly one associated value.
- Maximum key length: 128 Unicode characters in UTF-8.
- Maximum value length: 256 Unicode characters in UTF-8.
- Can use alphanumeric characters (AâZ, aâz, 0â9), and the following characters: + - = . _ : / @
- Cannot use âaws:â as a prefix for a key.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

IndexName -> (string)

The name for the place index resource.

IndexArn -> (string)

The Amazon Resource Name (ARN) for the place index resource. Used to specify a resource across Amazon Web Services.

- Format example: `arn:aws:geo:region:account-id:place-index/ExamplePlaceIndex`

CreateTime -> (timestamp)

The timestamp for when the place index resource was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ` .