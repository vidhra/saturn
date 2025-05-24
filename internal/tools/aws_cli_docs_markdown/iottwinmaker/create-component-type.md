# create-component-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iottwinmaker/create-component-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iottwinmaker/create-component-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iottwinmaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iottwinmaker/index.html#cli-aws-iottwinmaker) ]

# create-component-type

## Description

Creates a component type.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iottwinmaker-2021-11-29/CreateComponentType)

## Synopsis

```
create-component-type
--workspace-id <value>
[--is-singleton | --no-is-singleton]
--component-type-id <value>
[--description <value>]
[--property-definitions <value>]
[--extends-from <value>]
[--functions <value>]
[--tags <value>]
[--property-groups <value>]
[--component-type-name <value>]
[--composite-component-types <value>]
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

The ID of the workspace that contains the component type.

`--is-singleton` | `--no-is-singleton` (boolean)

A Boolean value that specifies whether an entity can have more than one component of this type.

`--component-type-id` (string)

The ID of the component type.

`--description` (string)

The description of the component type.

`--property-definitions` (map)

An object that maps strings to the property definitions in the component type. Each string in the mapping must be unique to this object.

key -> (string)

value -> (structure)

An object that sets information about a property.

dataType -> (structure)

An object that contains information about the data type.

type -> (string)

The underlying type of the data type.

nestedType -> (structure)

The nested type in the data type.

type -> (string)

The underlying type of the data type.

( â¦ recursive â¦ )allowedValues -> (list)

The allowed values for this data type.

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

unitOfMeasure -> (string)

The unit of measure used in this data type.

relationship -> (structure)

A relationship that associates a component with another component.

targetComponentTypeId -> (string)

The ID of the target component type associated with this relationship.

relationshipType -> (string)

The type of the relationship.

allowedValues -> (list)

The allowed values for this data type.

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

unitOfMeasure -> (string)

The unit of measure used in this data type.

relationship -> (structure)

A relationship that associates a component with another component.

targetComponentTypeId -> (string)

The ID of the target component type associated with this relationship.

relationshipType -> (string)

The type of the relationship.

isRequiredInEntity -> (boolean)

A Boolean value that specifies whether the property is required.

isExternalId -> (boolean)

A Boolean value that specifies whether the property ID comes from an external data store.

isStoredExternally -> (boolean)

A Boolean value that specifies whether the property is stored externally.

isTimeSeries -> (boolean)

A Boolean value that specifies whether the property consists of time series data.

defaultValue -> (structure)

An object that contains the default value.

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

configuration -> (map)

A mapping that specifies configuration information about the property. Use this field to specify information that you read from and write to an external source.

key -> (string)

value -> (string)

displayName -> (string)

A friendly name for the property.

JSON Syntax:

```
{"string": {
      "dataType": {
        "type": "RELATIONSHIP"|"STRING"|"LONG"|"BOOLEAN"|"INTEGER"|"DOUBLE"|"LIST"|"MAP",
        "nestedType": {
          "type": "RELATIONSHIP"|"STRING"|"LONG"|"BOOLEAN"|"INTEGER"|"DOUBLE"|"LIST"|"MAP",
          "nestedType": { ... recursive ... },
          "allowedValues": [
            {
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
                  "listValue": ,
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
            ...
          ],
          "unitOfMeasure": "string",
          "relationship": {
            "targetComponentTypeId": "string",
            "relationshipType": "string"
          }
        },
        "allowedValues": [
          {
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
                "listValue": ,
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
          ...
        ],
        "unitOfMeasure": "string",
        "relationship": {
          "targetComponentTypeId": "string",
          "relationshipType": "string"
        }
      },
      "isRequiredInEntity": true|false,
      "isExternalId": true|false,
      "isStoredExternally": true|false,
      "isTimeSeries": true|false,
      "defaultValue": {
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
      "configuration": {"string": "string"
        ...},
      "displayName": "string"
    }
  ...}
```

`--extends-from` (list)

Specifies the parent component type to extend.

(string)

Syntax:

```
"string" "string" ...
```

`--functions` (map)

An object that maps strings to the functions in the component type. Each string in the mapping must be unique to this object.

key -> (string)

value -> (structure)

The function request body.

requiredProperties -> (list)

The required properties of the function.

(string)

scope -> (string)

The scope of the function.

implementedBy -> (structure)

The data connector.

lambda -> (structure)

The Lambda function associated with this data connector.

arn -> (string)

The ARN of the Lambda function.

isNative -> (boolean)

A Boolean value that specifies whether the data connector is native to IoT TwinMaker.

Shorthand Syntax:

```
KeyName1=requiredProperties=string,string,scope=string,implementedBy={lambda={arn=string},isNative=boolean},KeyName2=requiredProperties=string,string,scope=string,implementedBy={lambda={arn=string},isNative=boolean}
```

JSON Syntax:

```
{"string": {
      "requiredProperties": ["string", ...],
      "scope": "ENTITY"|"WORKSPACE",
      "implementedBy": {
        "lambda": {
          "arn": "string"
        },
        "isNative": true|false
      }
    }
  ...}
```

`--tags` (map)

Metadata that you can use to manage the component type.

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

`--property-groups` (map)

key -> (string)

value -> (structure)

groupType -> (string)

The group type.

propertyNames -> (list)

The names of properties.

(string)

Shorthand Syntax:

```
KeyName1=groupType=string,propertyNames=string,string,KeyName2=groupType=string,propertyNames=string,string
```

JSON Syntax:

```
{"string": {
      "groupType": "TABULAR",
      "propertyNames": ["string", ...]
    }
  ...}
```

`--component-type-name` (string)

A friendly name for the component type.

`--composite-component-types` (map)

This is an object that maps strings to `compositeComponentTypes` of the `componentType` . `CompositeComponentType` is referenced by `componentTypeId` .

key -> (string)

value -> (structure)

An object that sets information about the composite component types of a component type.

componentTypeId -> (string)

This is the `componentTypeId` that the `compositeComponentType` refers to.

Shorthand Syntax:

```
KeyName1=componentTypeId=string,KeyName2=componentTypeId=string
```

JSON Syntax:

```
{"string": {
      "componentTypeId": "string"
    }
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

arn -> (string)

The ARN of the component type.

creationDateTime -> (timestamp)

The date and time when the entity was created.

state -> (string)

The current state of the component type.