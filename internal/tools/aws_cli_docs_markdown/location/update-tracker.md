# update-trackerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/update-tracker.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/update-tracker.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [location](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/index.html#cli-aws-location) ]

# update-tracker

## Description

Updates the specified properties of a given tracker resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/location-2020-11-19/UpdateTracker)

## Synopsis

```
update-tracker
--tracker-name <value>
[--pricing-plan <value>]
[--pricing-plan-data-source <value>]
[--description <value>]
[--position-filtering <value>]
[--event-bridge-enabled | --no-event-bridge-enabled]
[--kms-key-enable-geospatial-queries | --no-kms-key-enable-geospatial-queries]
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

`--tracker-name` (string)

The name of the tracker resource to update.

`--pricing-plan` (string)

No longer used. If included, the only allowed value is `RequestBasedUsage` .

Possible values:

- `RequestBasedUsage`
- `MobileAssetTracking`
- `MobileAssetManagement`

`--pricing-plan-data-source` (string)

This parameter is no longer used.

`--description` (string)

Updates the description for the tracker resource.

`--position-filtering` (string)

Updates the position filtering for the tracker resource.

Valid values:

- `TimeBased` - Location updates are evaluated against linked geofence collections, but not every location update is stored. If your update frequency is more often than 30 seconds, only one update per 30 seconds is stored for each unique device ID.
- `DistanceBased` - If the device has moved less than 30 m (98.4 ft), location updates are ignored. Location updates within this distance are neither evaluated against linked geofence collections, nor stored. This helps control costs by reducing the number of geofence evaluations and historical device positions to paginate through. Distance-based filtering can also reduce the effects of GPS noise when displaying device trajectories on a map.
- `AccuracyBased` - If the device has moved less than the measured accuracy, location updates are ignored. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is ignored if the device has moved less than 15 m. Ignored location updates are neither evaluated against linked geofence collections, nor stored. This helps educe the effects of GPS noise when displaying device trajectories on a map, and can help control costs by reducing the number of geofence evaluations.

Possible values:

- `TimeBased`
- `DistanceBased`
- `AccuracyBased`

`--event-bridge-enabled` | `--no-event-bridge-enabled` (boolean)

Whether to enable position `UPDATE` events from this tracker to be sent to EventBridge.

### Note

You do not need enable this feature to get `ENTER` and `EXIT` events for geofences with this tracker. Those events are always sent to EventBridge.

`--kms-key-enable-geospatial-queries` | `--no-kms-key-enable-geospatial-queries` (boolean)

Enables `GeospatialQueries` for a tracker that uses a [Amazon Web Services KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) .

This parameter is only used if you are using a KMS customer managed key.

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

TrackerName -> (string)

The name of the updated tracker resource.

TrackerArn -> (string)

The Amazon Resource Name (ARN) of the updated tracker resource. Used to specify a resource across AWS.

- Format example: `arn:aws:geo:region:account-id:tracker/ExampleTracker`

UpdateTime -> (timestamp)

The timestamp for when the tracker resource was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ` .