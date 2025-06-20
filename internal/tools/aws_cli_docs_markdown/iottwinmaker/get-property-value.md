# get-property-valueÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iottwinmaker/get-property-value.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iottwinmaker/get-property-value.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iottwinmaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iottwinmaker/index.html#cli-aws-iottwinmaker) ]

# get-property-value

## Description

Gets the property values for a component, component type, entity, or workspace.

You must specify a value for either `componentName` , `componentTypeId` , `entityId` , or `workspaceId` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iottwinmaker-2021-11-29/GetPropertyValue)

## Synopsis

```
get-property-value
[--component-name <value>]
[--component-path <value>]
[--component-type-id <value>]
[--entity-id <value>]
--selected-properties <value>
--workspace-id <value>
[--max-results <value>]
[--next-token <value>]
[--property-group-name <value>]
[--tabular-conditions <value>]
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

`--component-name` (string)

The name of the component whose property values the operation returns.

`--component-path` (string)

This string specifies the path to the composite component, starting from the top-level component.

`--component-type-id` (string)

The ID of the component type whose property values the operation returns.

`--entity-id` (string)

The ID of the entity whose property values the operation returns.

`--selected-properties` (list)

The properties whose values the operation returns.

(string)

Syntax:

```
"string" "string" ...
```

`--workspace-id` (string)

The ID of the workspace whose values the operation returns.

`--max-results` (integer)

The maximum number of results to return at one time. The default is 25.

Valid Range: Minimum value of 1. Maximum value of 250.

`--next-token` (string)

The string that specifies the next page of results.

`--property-group-name` (string)

The property group name.

`--tabular-conditions` (structure)

The tabular conditions.

orderBy -> (list)

Filter criteria that orders the output. It can be sorted in ascending or descending order.

(structure)

Filter criteria that orders the return output. It can be sorted in ascending or descending order.

order -> (string)

The set order that filters results.

propertyName -> (string)

The property name.

propertyFilters -> (list)

You can filter the request using various logical operators and a key-value format. For example:

`{"key": "serverType", "value": "webServer"}`

(structure)

An object that filters items returned by a property request.

propertyName -> (string)

The property name associated with this property filter.

operator -> (string)

The operator associated with this property filter.

value -> (structure)

The value associated with this property filter.

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

JSON Syntax:

```
{
  "orderBy": [
    {
      "order": "ASCENDING"|"DESCENDING",
      "propertyName": "string"
    }
    ...
  ],
  "propertyFilters": [
    {
      "propertyName": "string",
      "operator": "string",
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
      }
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

## Output

propertyValues -> (map)

An object that maps strings to the properties and latest property values in the response. Each string in the mapping must be unique to this object.

key -> (string)

value -> (structure)

The latest value of the property.

propertyReference -> (structure)

An object that specifies information about a property.

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

propertyValue -> (structure)

The value of the property.

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

nextToken -> (string)

The string that specifies the next page of results.

tabularPropertyValues -> (list)

A table of property values.

(list)

(map)

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