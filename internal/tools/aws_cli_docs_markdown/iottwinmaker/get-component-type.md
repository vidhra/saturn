# get-component-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iottwinmaker/get-component-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iottwinmaker/get-component-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iottwinmaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iottwinmaker/index.html#cli-aws-iottwinmaker) ]

# get-component-type

## Description

Retrieves information about a component type.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iottwinmaker-2021-11-29/GetComponentType)

## Synopsis

```
get-component-type
--workspace-id <value>
--component-type-id <value>
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

`--component-type-id` (string)

The ID of the component type.

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

workspaceId -> (string)

The ID of the workspace that contains the component type.

isSingleton -> (boolean)

A Boolean value that specifies whether an entity can have more than one component of this type.

componentTypeId -> (string)

The ID of the component type.

description -> (string)

The description of the component type.

propertyDefinitions -> (map)

An object that maps strings to the property definitions in the component type. Each string in the mapping must be unique to this object.

key -> (string)

value -> (structure)

An object that contains response data from a property definition request.

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

isTimeSeries -> (boolean)

A Boolean value that specifies whether the property consists of time series data.

isRequiredInEntity -> (boolean)

A Boolean value that specifies whether the property is required in an entity.

isExternalId -> (boolean)

A Boolean value that specifies whether the property ID comes from an external data store.

isStoredExternally -> (boolean)

A Boolean value that specifies whether the property is stored externally.

isImported -> (boolean)

A Boolean value that specifies whether the property definition is imported from an external data store.

isFinal -> (boolean)

A Boolean value that specifies whether the property definition can be updated.

isInherited -> (boolean)

A Boolean value that specifies whether the property definition is inherited from a parent entity.

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

A mapping that specifies configuration information about the property.

key -> (string)

value -> (string)

displayName -> (string)

A friendly name for the property.

extendsFrom -> (list)

The name of the parent component type that this component type extends.

(string)

functions -> (map)

An object that maps strings to the functions in the component type. Each string in the mapping must be unique to this object.

key -> (string)

value -> (structure)

The function response.

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

isInherited -> (boolean)

Indicates whether this function is inherited.

creationDateTime -> (timestamp)

The date and time when the component type was created.

updateDateTime -> (timestamp)

The date and time when the component was last updated.

arn -> (string)

The ARN of the component type.

isAbstract -> (boolean)

A Boolean value that specifies whether the component type is abstract.

isSchemaInitialized -> (boolean)

A Boolean value that specifies whether the component type has a schema initializer and that the schema initializer has run.

status -> (structure)

The current status of the component type.

state -> (string)

The current state of the entity, component, component type, or workspace.

error -> (structure)

The error message.

code -> (string)

The error code.

message -> (string)

The error message.

propertyGroups -> (map)

The maximum number of results to return at one time. The default is 25.

Valid Range: Minimum value of 1. Maximum value of 250.

key -> (string)

value -> (structure)

The property group response

groupType -> (string)

The group types.

propertyNames -> (list)

The names of properties.

(string)

isInherited -> (boolean)

A Boolean value that specifies whether the property group is inherited from a parent entity

syncSource -> (string)

The syncSource of the SyncJob, if this entity was created by a SyncJob.

componentTypeName -> (string)

The component type name.

compositeComponentTypes -> (map)

This is an object that maps strings to `compositeComponentTypes` of the `componentType` . `CompositeComponentType` is referenced by `componentTypeId` .

key -> (string)

value -> (structure)

An object that returns information about the composite component types of a component type.

componentTypeId -> (string)

This is the `componentTypeId` that this `compositeComponentType` refers to.

isInherited -> (boolean)

This boolean indicates whether this `compositeComponentType` is inherited from its parent.