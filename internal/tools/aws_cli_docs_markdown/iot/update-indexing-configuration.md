# update-indexing-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-indexing-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-indexing-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# update-indexing-configuration

## Description

Updates the search configuration.

Requires permission to access the [UpdateIndexingConfiguration](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateIndexingConfiguration)

## Synopsis

```
update-indexing-configuration
[--thing-indexing-configuration <value>]
[--thing-group-indexing-configuration <value>]
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

`--thing-indexing-configuration` (structure)

Thing indexing configuration.

thingIndexingMode -> (string)

Thing indexing mode. Valid values are:

- REGISTRY â Your thing index contains registry data only.
- REGISTRY_AND_SHADOW - Your thing index contains registry and shadow data.
- OFF - Thing indexing is disabled.

thingConnectivityIndexingMode -> (string)

Thing connectivity indexing mode. Valid values are:

- STATUS â Your thing index contains connectivity status. To enable thing connectivity indexing, *thingIndexMode* must not be set to OFF.
- OFF - Thing connectivity status indexing is disabled.

deviceDefenderIndexingMode -> (string)

Device Defender indexing mode. Valid values are:

- VIOLATIONS â Your thing index contains Device Defender violations. To enable Device Defender indexing, *deviceDefenderIndexingMode* must not be set to OFF.
- OFF - Device Defender indexing is disabled.

For more information about Device Defender violations, see [Device Defender Detect.](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-detect.html)

namedShadowIndexingMode -> (string)

Named shadow indexing mode. Valid values are:

- ON â Your thing index contains named shadow. To enable thing named shadow indexing, *namedShadowIndexingMode* must not be set to OFF.
- OFF - Named shadow indexing is disabled.

For more information about Shadows, see [IoT Device Shadow service.](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html)

managedFields -> (list)

Contains fields that are indexed and whose types are already known by the Fleet Indexing service. This is an optional field. For more information, see [Managed fields](https://docs.aws.amazon.com/iot/latest/developerguide/managing-fleet-index.html#managed-field) in the *Amazon Web Services IoT Core Developer Guide* .

### Note

You canât modify managed fields by updating fleet indexing configuration.

(structure)

Describes the name and data type at a field.

name -> (string)

The name of the field.

type -> (string)

The data type of the field.

customFields -> (list)

Contains custom field names and their data type.

(structure)

Describes the name and data type at a field.

name -> (string)

The name of the field.

type -> (string)

The data type of the field.

filter -> (structure)

Provides additional selections for named shadows and geolocation data.

To add named shadows to your fleet indexing configuration, set `namedShadowIndexingMode` to be ON and specify your shadow names in `namedShadowNames` filter.

To add geolocation data to your fleet indexing configuration:

- If you store geolocation data in a class/unnamed shadow, set `thingIndexingMode` to be `REGISTRY_AND_SHADOW` and specify your geolocation data in `geoLocations` filter.
- If you store geolocation data in a named shadow, set `namedShadowIndexingMode` to be `ON` , add the shadow name in `namedShadowNames` filter, and specify your geolocation data in `geoLocations` filter. For more information, see [Managing fleet indexing](https://docs.aws.amazon.com/iot/latest/developerguide/managing-fleet-index.html) .

namedShadowNames -> (list)

The shadow names that you select to index. The default maximum number of shadow names for indexing is 10. To increase the limit, see [Amazon Web Services IoT Device Management Quotas](https://docs.aws.amazon.com/general/latest/gr/iot_device_management.html#fleet-indexing-limits) in the *Amazon Web Services General Reference* .

(string)

geoLocations -> (list)

The list of geolocation targets that you select to index. The default maximum number of geolocation targets for indexing is `1` . To increase the limit, see [Amazon Web Services IoT Device Management Quotas](https://docs.aws.amazon.com/general/latest/gr/iot_device_management.html#fleet-indexing-limits) in the *Amazon Web Services General Reference* .

(structure)

A geolocation target that you select to index. Each geolocation target contains a `name` and `order` key-value pair that specifies the geolocation target fields.

name -> (string)

The `name` of the geolocation target field. If the target field is part of a named shadow, you must select the named shadow using the `namedShadow` filter.

order -> (string)

The `order` of the geolocation target field. This field is optional. The default value is `LatLon` .

JSON Syntax:

```
{
  "thingIndexingMode": "OFF"|"REGISTRY"|"REGISTRY_AND_SHADOW",
  "thingConnectivityIndexingMode": "OFF"|"STATUS",
  "deviceDefenderIndexingMode": "OFF"|"VIOLATIONS",
  "namedShadowIndexingMode": "OFF"|"ON",
  "managedFields": [
    {
      "name": "string",
      "type": "Number"|"String"|"Boolean"
    }
    ...
  ],
  "customFields": [
    {
      "name": "string",
      "type": "Number"|"String"|"Boolean"
    }
    ...
  ],
  "filter": {
    "namedShadowNames": ["string", ...],
    "geoLocations": [
      {
        "name": "string",
        "order": "LatLon"|"LonLat"
      }
      ...
    ]
  }
}
```

`--thing-group-indexing-configuration` (structure)

Thing group indexing configuration.

thingGroupIndexingMode -> (string)

Thing group indexing mode.

managedFields -> (list)

Contains fields that are indexed and whose types are already known by the Fleet Indexing service. This is an optional field. For more information, see [Managed fields](https://docs.aws.amazon.com/iot/latest/developerguide/managing-fleet-index.html#managed-field) in the *Amazon Web Services IoT Core Developer Guide* .

### Note

You canât modify managed fields by updating fleet indexing configuration.

(structure)

Describes the name and data type at a field.

name -> (string)

The name of the field.

type -> (string)

The data type of the field.

customFields -> (list)

A list of thing group fields to index. This list cannot contain any managed fields. Use the GetIndexingConfiguration API to get a list of managed fields.

Contains custom field names and their data type.

(structure)

Describes the name and data type at a field.

name -> (string)

The name of the field.

type -> (string)

The data type of the field.

Shorthand Syntax:

```
thingGroupIndexingMode=string,managedFields=[{name=string,type=string},{name=string,type=string}],customFields=[{name=string,type=string},{name=string,type=string}]
```

JSON Syntax:

```
{
  "thingGroupIndexingMode": "OFF"|"ON",
  "managedFields": [
    {
      "name": "string",
      "type": "Number"|"String"|"Boolean"
    }
    ...
  ],
  "customFields": [
    {
      "name": "string",
      "type": "Number"|"String"|"Boolean"
    }
    ...
  ]
}
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To enable thing indexing**

The following `update-indexing-configuration` example enables thing indexing to support searching registry data, shadow data, and thing connectivity status using the AWS_Things index.

```
aws iot update-indexing-configuration
    --thing-indexing-configuration thingIndexingMode=REGISTRY_AND_SHADOW,thingConnectivityIndexingMode=STATUS
```

This command produces no output.

For more information, see [Managing Thing Indexing](https://docs.aws.amazon.com/iot/latest/developerguide/managing-index.html) in the *AWS IoT Developers Guide*.

## Output

None