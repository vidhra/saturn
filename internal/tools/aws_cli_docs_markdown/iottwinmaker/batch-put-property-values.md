# batch-put-property-valuesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iottwinmaker/batch-put-property-values.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iottwinmaker/batch-put-property-values.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iottwinmaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iottwinmaker/index.html#cli-aws-iottwinmaker) ]

# batch-put-property-values

## Description

Sets values for multiple time series properties.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iottwinmaker-2021-11-29/BatchPutPropertyValues)

## Synopsis

```
batch-put-property-values
--workspace-id <value>
--entries <value>
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

`--workspace-id` (string)

The ID of the workspace that contains the properties to set.

`--entries` (list)

An object that maps strings to the property value entries to set. Each string in the mapping must be unique to this object.

(structure)

An object that specifies information about time series property values. This object is used and consumed by the [BatchPutPropertyValues](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_BatchPutPropertyValues.html) action.

entityPropertyReference -> (structure)

An object that contains information about the entity that has the property.

componentName -> (string)

The name of the component.

componentPath -> (string)

This string specifies the path to the composite component, starting from the top-level component.

externalIdProperty -> (map)

A mapping of external IDs to property names. External IDs uniquely identify properties from external data stores.

key -> (string)

value -> (string)

entityId -> (string)

The ID of the entity.

propertyName -> (string)

The name of the property.

propertyValues -> (list)

A list of objects that specify time series property values.

(structure)

An object that contains information about a value for a time series property.

timestamp -> (timestamp)

The timestamp of a value for a time series property.

value -> (structure)

An object that specifies a value for a time series property.

booleanValue -> (boolean)

A Boolean value.

doubleValue -> (double)

A double value.

integerValue -> (integer)

An integer value.

longValue -> (long)

A long value.

stringValue -> (string)

A string value.

listValue -> (list)

A list of multiple values.

(structure)

An object that specifies a value for a property.

booleanValue -> (boolean)

A Boolean value.

doubleValue -> (double)

A double value.

integerValue -> (integer)

An integer value.

longValue -> (long)

A long value.

stringValue -> (string)

A string value.

listValue -> (list)

A list of multiple values.

( â¦ recursive â¦ )

mapValue -> (map)

An object that maps strings to multiple `DataValue` objects.

key -> (string)

( â¦ recursive â¦ )

relationshipValue -> (structure)

A value that relates a component to another component.

targetEntityId -> (string)

The ID of the target entity associated with this relationship value.

targetComponentName -> (string)

The name of the target component associated with the relationship value.

expression -> (string)

An expression that produces the value.

mapValue -> (map)

An object that maps strings to multiple `DataValue` objects.

key -> (string)

value -> (structure)

An object that specifies a value for a property.

booleanValue -> (boolean)

A Boolean value.

doubleValue -> (double)

A double value.

integerValue -> (integer)

An integer value.

longValue -> (long)

A long value.

stringValue -> (string)

A string value.

listValue -> (list)

A list of multiple values.

( â¦ recursive â¦ )

mapValue -> (map)

An object that maps strings to multiple `DataValue` objects.

key -> (string)

( â¦ recursive â¦ )

relationshipValue -> (structure)

A value that relates a component to another component.

targetEntityId -> (string)

The ID of the target entity associated with this relationship value.

targetComponentName -> (string)

The name of the target component associated with the relationship value.

expression -> (string)

An expression that produces the value.

relationshipValue -> (structure)

A value that relates a component to another component.

targetEntityId -> (string)

The ID of the target entity associated with this relationship value.

targetComponentName -> (string)

The name of the target component associated with the relationship value.

expression -> (string)

An expression that produces the value.

time -> (string)

ISO8601 DateTime of a value for a time series property.

The time for when the property value was recorded in ISO 8601 format: *YYYY-MM-DDThh:mm:ss[.SSSSSSSSS][Z/Â±HH:mm]* .

- *[YYYY]* : year
- *[MM]* : month
- *[DD]* : day
- *[hh]* : hour
- *[mm]* : minute
- *[ss]* : seconds
- *[.SSSSSSSSS]* : additional precision, where precedence is maintained. For example: [.573123] is equal to 573123000 nanoseconds.
- *Z* : default timezone UTC
- *Â± HH:mm* : time zone offset in Hours and Minutes.

*Required sub-fields* : YYYY-MM-DDThh:mm:ss and [Z/Â±HH:mm]

JSON Syntax:

```
[
  {
    "entityPropertyReference": {
      "componentName": "string",
      "componentPath": "string",
      "externalIdProperty": {"string": "string"
        ...},
      "entityId": "string",
      "propertyName": "string"
    },
    "propertyValues": [
      {
        "timestamp": timestamp,
        "value": {
          "booleanValue": true|false,
          "doubleValue": double,
          "integerValue": integer,
          "longValue": long,
          "stringValue": "string",
          "listValue": [
            {
              "booleanValue": true|false,
              "doubleValue": double,
              "integerValue": integer,
              "longValue": long,
              "stringValue": "string",
              "listValue": [
                { ... recursive ... }
                ...
              ],
              "mapValue": {"string": { ... recursive ... }
                ...},
              "relationshipValue": {
                "targetEntityId": "string",
                "targetComponentName": "string"
              },
              "expression": "string"
            }
            ...
          ],
          "mapValue": {"string": {
                "booleanValue": true|false,
                "doubleValue": double,
                "integerValue": integer,
                "longValue": long,
                "stringValue": "string",
                "listValue": [
                  { ... recursive ... }
                  ...
                ],
                "mapValue": {"string": { ... recursive ... }
                  ...},
                "relationshipValue": {
                  "targetEntityId": "string",
                  "targetComponentName": "string"
                },
                "expression": "string"
              }
            ...},
          "relationshipValue": {
            "targetEntityId": "string",
            "targetComponentName": "string"
          },
          "expression": "string"
        },
        "time": "string"
      }
      ...
    ]
  }
  ...
]
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

errorEntries -> (list)

Entries that caused errors in the batch put operation.

(structure)

An object that contains information about errors returned by the `BatchPutProperty` action.

errors -> (list)

A list of objects that contain information about errors returned by the `BatchPutProperty` action.

(structure)

An error returned by the `BatchPutProperty` action.

errorCode -> (string)

The error code.

errorMessage -> (string)

The error message.

entry -> (structure)

An object that contains information about errors returned by the `BatchPutProperty` action.

entityPropertyReference -> (structure)

An object that contains information about the entity that has the property.

componentName -> (string)

The name of the component.

componentPath -> (string)

This string specifies the path to the composite component, starting from the top-level component.

externalIdProperty -> (map)

A mapping of external IDs to property names. External IDs uniquely identify properties from external data stores.

key -> (string)

value -> (string)

entityId -> (string)

The ID of the entity.

propertyName -> (string)

The name of the property.

propertyValues -> (list)

A list of objects that specify time series property values.

(structure)

An object that contains information about a value for a time series property.

timestamp -> (timestamp)

The timestamp of a value for a time series property.

value -> (structure)

An object that specifies a value for a time series property.

booleanValue -> (boolean)

A Boolean value.

doubleValue -> (double)

A double value.

integerValue -> (integer)

An integer value.

longValue -> (long)

A long value.

stringValue -> (string)

A string value.

listValue -> (list)

A list of multiple values.

(structure)

An object that specifies a value for a property.

booleanValue -> (boolean)

A Boolean value.

doubleValue -> (double)

A double value.

integerValue -> (integer)

An integer value.

longValue -> (long)

A long value.

stringValue -> (string)

A string value.

listValue -> (list)

A list of multiple values.

( â¦ recursive â¦ )

mapValue -> (map)

An object that maps strings to multiple `DataValue` objects.

key -> (string)

( â¦ recursive â¦ )

relationshipValue -> (structure)

A value that relates a component to another component.

targetEntityId -> (string)

The ID of the target entity associated with this relationship value.

targetComponentName -> (string)

The name of the target component associated with the relationship value.

expression -> (string)

An expression that produces the value.

mapValue -> (map)

An object that maps strings to multiple `DataValue` objects.

key -> (string)

value -> (structure)

An object that specifies a value for a property.

booleanValue -> (boolean)

A Boolean value.

doubleValue -> (double)

A double value.

integerValue -> (integer)

An integer value.

longValue -> (long)

A long value.

stringValue -> (string)

A string value.

listValue -> (list)

A list of multiple values.

( â¦ recursive â¦ )

mapValue -> (map)

An object that maps strings to multiple `DataValue` objects.

key -> (string)

( â¦ recursive â¦ )

relationshipValue -> (structure)

A value that relates a component to another component.

targetEntityId -> (string)

The ID of the target entity associated with this relationship value.

targetComponentName -> (string)

The name of the target component associated with the relationship value.

expression -> (string)

An expression that produces the value.

relationshipValue -> (structure)

A value that relates a component to another component.

targetEntityId -> (string)

The ID of the target entity associated with this relationship value.

targetComponentName -> (string)

The name of the target component associated with the relationship value.

expression -> (string)

An expression that produces the value.

time -> (string)

ISO8601 DateTime of a value for a time series property.

The time for when the property value was recorded in ISO 8601 format: *YYYY-MM-DDThh:mm:ss[.SSSSSSSSS][Z/Â±HH:mm]* .

- *[YYYY]* : year
- *[MM]* : month
- *[DD]* : day
- *[hh]* : hour
- *[mm]* : minute
- *[ss]* : seconds
- *[.SSSSSSSSS]* : additional precision, where precedence is maintained. For example: [.573123] is equal to 573123000 nanoseconds.
- *Z* : default timezone UTC
- *Â± HH:mm* : time zone offset in Hours and Minutes.

*Required sub-fields* : YYYY-MM-DDThh:mm:ss and [Z/Â±HH:mm]